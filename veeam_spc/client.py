import importlib
import re
from datetime import datetime, timedelta, timezone
from typing import Any


# ----------------------------
# helpers
# ----------------------------


def _camel_to_snake(name: str) -> str:
    s1 = re.sub("(.)([A-Z][a-z]+)", r"\1_\2", name)
    return re.sub("([a-z0-9])([A-Z])", r"\1_\2", s1).lower()


# ----------------------------
# API namespace proxy
# ----------------------------


class ApiNamespace:
    """
    Lazy namespace for openapi-python-client operation modules.

    Example:
        vc.api("provider").get_provider
        → veeam_spc.v3_6.api.provider.get_provider.asyncio
    """

    def __init__(self, client: "VeeamClient", base_module: str):
        self._client = client
        self._base = base_module

    def __getattr__(self, name: str):
        mod = importlib.import_module(f"{self._base}.{name}")
        return mod.asyncio


# ----------------------------
# main client
# ----------------------------


class VeeamClient:
    """
    Shared async client for versioned openapi-python-client SDKs.

    Responsibilities:
    - version routing
    - authentication (username/password or token)
    - token refresh (for password-based auth)
    - X-Client-Version header injection
    - API namespace routing
    """

    def __init__(
        self,
        host: str,
        api_version: str,
        verify_ssl: bool = True,
        username: str | None = None,
        password: str | None = None,
        token: str | None = None,
    ):
        self.host = self._normalize_host(host)
        self.api_version = api_version
        self.verify_ssl = verify_ssl
        
        # Support either username/password OR token
        if token:
            self.token = token
            self.username = None
            self.password = None
        elif username and password:
            self.username = username
            self.password = password
            self.token = None
        else:
            raise ValueError("Must provide either 'token' or both 'username' and 'password'")

        from .versions import VERSION_TO_PACKAGE

        if api_version not in VERSION_TO_PACKAGE:
            raise ValueError(f"Unsupported API version: {api_version}")

        self.package = VERSION_TO_PACKAGE[api_version]

        self._client = None
        self._access_token = None
        self._refresh_token = None
        self._expires_at: datetime | None = None

    @staticmethod
    def _normalize_host(host: str) -> str:
        """Remove trailing slashes and /api/v3 suffix if present"""
        cleaned = host.rstrip("/")
        # Remove common API path suffixes
        for suffix in ["/api/v3", "/api"]:
            if cleaned.endswith(suffix):
                cleaned = cleaned[: -len(suffix)]
        return cleaned

    # ----------------------------
    # connection + auth
    # ----------------------------

    async def connect(self):
        Client = getattr(importlib.import_module(f"{self.package}.client"), "Client")
        AuthenticatedClient = getattr(
            importlib.import_module(f"{self.package}.client"), "AuthenticatedClient"
        )

        # If using a pre-existing token, skip authentication
        if self.token:
            self._access_token = self.token
            self._client = AuthenticatedClient(
                base_url=f"{self.host}/api/v3",
                token=self._access_token,
                verify_ssl=self.verify_ssl,
            )
            return

        # Otherwise, authenticate with username/password
        o_auth_2_issue_token = importlib.import_module(
            f"{self.package}.api.authentication.o_auth_2_issue_token"
        )

        OAuth2IssueTokenBody = getattr(
            importlib.import_module(f"{self.package}.models.o_auth_2_issue_token_body"),
            "OAuth2IssueTokenBody",
        )
        OAuth2IssueTokenBodyGrantType = getattr(
            importlib.import_module(
                f"{self.package}.models.o_auth_2_issue_token_body_grant_type"
            ),
            "OAuth2IssueTokenBodyGrantType",
        )

        # unauthenticated client for initial auth
        self._client = Client(
            base_url=f"{self.host}/api/v3",
            verify_ssl=self.verify_ssl,
        )

        body = OAuth2IssueTokenBody(
            grant_type=OAuth2IssueTokenBodyGrantType.PASSWORD,
            username=self.username,
            password=self.password,
        )

        token = await o_auth_2_issue_token.asyncio(
            client=self._client,
            body=body,
            x_client_version=self.api_version,
        )

        self._store_token(token, AuthenticatedClient)

    async def close(self):
        # openapi-python-client has no shared session to close
        pass

    # ----------------------------
    # token handling
    # ----------------------------

    def _store_token(self, token, AuthenticatedClient):
        self._access_token = token.access_token
        self._refresh_token = token.refresh_token
        self._expires_at = datetime.now(timezone.utc) + timedelta(seconds=token.expires_in - 30)

        self._client = AuthenticatedClient(
            base_url=f"{self.host}/api/v3",
            token=self._access_token,
            verify_ssl=self.verify_ssl,
        )

    async def _refresh_token_if_needed(self):
        # Skip refresh for permanent tokens
        if self.token:
            return
            
        if self._expires_at and datetime.now(timezone.utc) < self._expires_at:
            return

        o_auth_2_issue_token = importlib.import_module(
            f"{self.package}.api.authentication.o_auth_2_issue_token"
        )

        OAuth2IssueTokenBody = getattr(
            importlib.import_module(f"{self.package}.models.o_auth_2_issue_token_body"),
            "OAuth2IssueTokenBody",
        )
        OAuth2IssueTokenBodyGrantType = getattr(
            importlib.import_module(
                f"{self.package}.models.o_auth_2_issue_token_body_grant_type"
            ),
            "OAuth2IssueTokenBodyGrantType",
        )

        Client = getattr(importlib.import_module(f"{self.package}.client"), "Client")
        AuthenticatedClient = getattr(
            importlib.import_module(f"{self.package}.client"), "AuthenticatedClient"
        )

        # try refresh first
        try:
            body = OAuth2IssueTokenBody(
                grant_type=OAuth2IssueTokenBodyGrantType.REFRESH_TOKEN,
                refresh_token=self._refresh_token,
            )
            token = await o_auth_2_issue_token.asyncio(
                client=self._client,
                body=body,
                x_client_version=self.api_version,
            )
        except Exception:
            # fallback to password
            tmp = Client(
                base_url=f"{self.host}/api/v3",
                verify_ssl=self.verify_ssl,
            )
            body = OAuth2IssueTokenBody(
                grant_type=OAuth2IssueTokenBodyGrantType.PASSWORD,
                username=self.username,
                password=self.password,
            )
            token = await o_auth_2_issue_token.asyncio(
                client=tmp,
                body=body,
                x_client_version=self.api_version,
            )

        self._store_token(token, AuthenticatedClient)

    # ----------------------------
    # API access
    # ----------------------------

    def api(self, name: str) -> Any:
        """
        Smart API accessor.

        Examples:
            vc.api("provider").get_provider
            vc.api("provider.get_provider")
        """

        # direct operation
        if "." in name:
            mod = importlib.import_module(f"{self.package}.api.{name}")
            return mod.asyncio

        # namespace
        return ApiNamespace(self, f"{self.package}.api.{name}")

    async def call(self, fn, *args, **kwargs):
        """
        Wrap any API call with:
        - automatic token refresh
        - automatic X-Client-Version injection
        """
        await self._refresh_token_if_needed()

        if "x_client_version" not in kwargs:
            kwargs["x_client_version"] = self.api_version

        return await fn(client=self._client, *args, **kwargs)
