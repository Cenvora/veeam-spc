from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.complete_smtp_o_auth_2_sign_in_response_200 import CompleteSmtpOAuth2SignInResponse200
from ...models.error_response import ErrorResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    organization_uid: UUID,
    *,
    error: str | Unset = UNSET,
    error_description: str | Unset = UNSET,
    code: str | Unset = UNSET,
    state: str | Unset = UNSET,
    select: str | Unset = UNSET,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_request_id, Unset):
        headers["X-Request-id"] = x_request_id

    if not isinstance(x_client_version, Unset):
        headers["X-Client-Version"] = x_client_version

    params: dict[str, Any] = {}

    params["error"] = error

    params["error_description"] = error_description

    params["code"] = code

    params["state"] = state

    params["select"] = select

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/organizations/{organization_uid}/configuration/notification/oauth2/signin/completion".format(
            organization_uid=quote(str(organization_uid), safe=""),
        ),
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | CompleteSmtpOAuth2SignInResponse200 | ErrorResponse:
    if response.status_code == 200:
        response_200 = CompleteSmtpOAuth2SignInResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 202:
        response_202 = cast(Any, None)
        return response_202

    response_default = ErrorResponse.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | CompleteSmtpOAuth2SignInResponse200 | ErrorResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    organization_uid: UUID,
    *,
    client: AuthenticatedClient,
    error: str | Unset = UNSET,
    error_description: str | Unset = UNSET,
    code: str | Unset = UNSET,
    state: str | Unset = UNSET,
    select: str | Unset = UNSET,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Response[Any | CompleteSmtpOAuth2SignInResponse200 | ErrorResponse]:
    """Obtain SMTP Server OAuth 2.0 Authorization Tokens

     Returns a pair of OAuth 2.0 authorization tokens to access an SMTP server for an organization with
    the specified UID.

    Args:
        organization_uid (UUID):
        error (str | Unset):
        error_description (str | Unset):
        code (str | Unset):
        state (str | Unset):
        select (str | Unset):
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CompleteSmtpOAuth2SignInResponse200 | ErrorResponse]
    """

    kwargs = _get_kwargs(
        organization_uid=organization_uid,
        error=error,
        error_description=error_description,
        code=code,
        state=state,
        select=select,
        x_request_id=x_request_id,
        x_client_version=x_client_version,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    organization_uid: UUID,
    *,
    client: AuthenticatedClient,
    error: str | Unset = UNSET,
    error_description: str | Unset = UNSET,
    code: str | Unset = UNSET,
    state: str | Unset = UNSET,
    select: str | Unset = UNSET,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Any | CompleteSmtpOAuth2SignInResponse200 | ErrorResponse | None:
    """Obtain SMTP Server OAuth 2.0 Authorization Tokens

     Returns a pair of OAuth 2.0 authorization tokens to access an SMTP server for an organization with
    the specified UID.

    Args:
        organization_uid (UUID):
        error (str | Unset):
        error_description (str | Unset):
        code (str | Unset):
        state (str | Unset):
        select (str | Unset):
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CompleteSmtpOAuth2SignInResponse200 | ErrorResponse
    """

    return sync_detailed(
        organization_uid=organization_uid,
        client=client,
        error=error,
        error_description=error_description,
        code=code,
        state=state,
        select=select,
        x_request_id=x_request_id,
        x_client_version=x_client_version,
    ).parsed


async def asyncio_detailed(
    organization_uid: UUID,
    *,
    client: AuthenticatedClient,
    error: str | Unset = UNSET,
    error_description: str | Unset = UNSET,
    code: str | Unset = UNSET,
    state: str | Unset = UNSET,
    select: str | Unset = UNSET,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Response[Any | CompleteSmtpOAuth2SignInResponse200 | ErrorResponse]:
    """Obtain SMTP Server OAuth 2.0 Authorization Tokens

     Returns a pair of OAuth 2.0 authorization tokens to access an SMTP server for an organization with
    the specified UID.

    Args:
        organization_uid (UUID):
        error (str | Unset):
        error_description (str | Unset):
        code (str | Unset):
        state (str | Unset):
        select (str | Unset):
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CompleteSmtpOAuth2SignInResponse200 | ErrorResponse]
    """

    kwargs = _get_kwargs(
        organization_uid=organization_uid,
        error=error,
        error_description=error_description,
        code=code,
        state=state,
        select=select,
        x_request_id=x_request_id,
        x_client_version=x_client_version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    organization_uid: UUID,
    *,
    client: AuthenticatedClient,
    error: str | Unset = UNSET,
    error_description: str | Unset = UNSET,
    code: str | Unset = UNSET,
    state: str | Unset = UNSET,
    select: str | Unset = UNSET,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Any | CompleteSmtpOAuth2SignInResponse200 | ErrorResponse | None:
    """Obtain SMTP Server OAuth 2.0 Authorization Tokens

     Returns a pair of OAuth 2.0 authorization tokens to access an SMTP server for an organization with
    the specified UID.

    Args:
        organization_uid (UUID):
        error (str | Unset):
        error_description (str | Unset):
        code (str | Unset):
        state (str | Unset):
        select (str | Unset):
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CompleteSmtpOAuth2SignInResponse200 | ErrorResponse
    """

    return (
        await asyncio_detailed(
            organization_uid=organization_uid,
            client=client,
            error=error,
            error_description=error_description,
            code=code,
            state=state,
            select=select,
            x_request_id=x_request_id,
            x_client_version=x_client_version,
        )
    ).parsed
