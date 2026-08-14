"""Work out which REST API version to speak to a Veeam Service Provider Console with.

VSPC does not version its URLs the way the other Veeam products do: every release since 8.1
answers on ``/api/v3``, and the client declares what it can handle with an
``X-Client-Version`` header. So there is nothing to probe — a path that exists on 3.6.2
exists on 3.5.1 too, and asking for one version or another changes the shape of the answer
rather than whether there is one.

What the console does report is its own build, from ``GET /api/v3/about``. Each console
release corresponds to exactly one REST API version (see ``SERVER_TO_API_VERSION``, which
mirrors the support table in the README), so the server version answers the question.

That endpoint needs a bearer token, which makes this the one Veeam product where version
detection cannot run before credentials exist. Detection logs in with the *oldest* version
this package ships, because ``X-Client-Version`` declares a client capability: an older
declaration is the one an older console will accept, and the login response is the same
either way.

Detection is best-effort by contract. An unreachable console, a rejected login or an
unreadable answer all return None, so a caller falls back to a version of its own choosing
rather than failing outright.

Callers should resolve once and store the result. Re-detecting on every start would silently
move an existing deployment onto a newer version after a console upgrade, and versions rename
enum values and add required fields.
"""

from __future__ import annotations

import logging
from collections.abc import Iterable, Sequence
from typing import Any

from .versions import VERSION_TO_PACKAGE

_LOGGER = logging.getLogger(__name__)

# Console release -> REST API version it serves. Mirrors the support table in the README;
# extend both together when a new console release is packaged.
SERVER_TO_API_VERSION = {
    "8.1": "3.5.1",
    "9.0": "3.6",
    "9.1": "3.6.1",
    "9.2": "3.6.2",
}


def _version_key(version: Any) -> tuple[int, ...] | None:
    """Parse a dotted version into comparable integers, or None if it is not one."""
    try:
        return tuple(int(part) for part in str(version).strip().split("."))
    except (AttributeError, TypeError, ValueError):
        return None


def _padded(keys: Iterable[tuple[int, ...]]) -> list[tuple[int, ...]]:
    """Pad version keys to a common length so "9" and "9.0" compare equal."""
    keys = list(keys)
    width = max((len(key) for key in keys), default=0)
    return [key + (0,) * (width - len(key)) for key in keys]


def newest_first(versions: Iterable[str]) -> list[str]:
    """Order API versions newest first, dropping any that are not recognizable.

    Versions look like "3.6.2". Comparing the numbers rather than the strings keeps a
    hypothetical "3.10" above "3.6" instead of below it, and lets "3.6" sit below "3.6.1".
    """
    ranked = [(_version_key(version), version) for version in versions]
    ranked = [entry for entry in ranked if entry[0]]
    if not ranked:
        return []

    padded = _padded(key for key, _ in ranked)
    return [version for _, version in sorted(zip(padded, (v for _, v in ranked)), reverse=True)]


def oldest_first(versions: Iterable[str]) -> list[str]:
    """Order API versions oldest first. See ``newest_first``."""
    return list(reversed(newest_first(versions)))


def api_version_for_server(
    server_version: Any, versions: Sequence[str] | None = None
) -> str | None:
    """Map a reported console version to the API version to talk to it with.

    A console newer than anything in ``SERVER_TO_API_VERSION`` maps to the newest API version
    this package ships: VSPC keeps older ``X-Client-Version`` values working, so the newest
    known version is both the closest match and a supported one. A console older than the
    oldest entry returns None — that is a console this package does not support, and guessing
    would produce confusing failures deep in a response parse instead of a clear "unsupported".

    Args:
        server_version: The ``serverVersion`` reported by ``/api/v3/about``, e.g. "9.2.0.32907".
        versions: API versions the caller can accept. Defaults to everything this package
            can speak.

    Returns:
        An API version string such as "3.6.2", or None.
    """
    reported = _version_key(server_version)
    if not reported:
        return None

    supported = set(VERSION_TO_PACKAGE if versions is None else versions)

    # Ordered oldest to newest, keeping only mappings the caller can actually use
    known = [
        (_version_key(server), api)
        for server, api in SERVER_TO_API_VERSION.items()
        if api in supported
    ]
    known = [entry for entry in known if entry[0]]
    if not known:
        return None
    known.sort()

    # Console versions carry four components ("9.2.0.32907") while the table carries two, so
    # compare on the leading components the table actually distinguishes
    depth = max(len(key) for key, _ in known)
    trimmed = reported[:depth] + (0,) * max(0, depth - len(reported))

    match = None
    for server_key, api_version in known:
        padded = server_key + (0,) * (depth - len(server_key))
        if trimmed >= padded:
            match = api_version

    if match is None:
        _LOGGER.debug(
            "Console version %s is older than the oldest supported console (%s)",
            server_version,
            ".".join(str(part) for part in known[0][0]),
        )
    return match


async def detect_server_version(
    host: str,
    *,
    username: str | None = None,
    password: str | None = None,
    token: str | None = None,
    verify_ssl: bool = True,
    client: Any | None = None,
) -> str | None:
    """Return the console's own version string, or None if it could not be read.

    Args:
        host: Console base URL, e.g. "https://vspc.example.com:1280". A trailing "/api/v3"
            is tolerated, as everywhere else in this package.
        username: Console user to log in as. Required unless ``token`` or ``client`` is given.
        password: That user's password.
        token: A pre-existing bearer token to use instead of logging in.
        verify_ssl: Whether to verify the console certificate.
        client: An already-connected ``VeeamClient`` to reuse instead of logging in. Its
            declared version does not affect the answer — ``/api/v3/about`` reports the
            console's build, not the caller's.
    """
    owns_client = client is None
    if owns_client:
        from .client import VeeamClient

        # Oldest first: X-Client-Version declares what this caller can handle, and an older
        # declaration is the one an older console will accept
        candidates = oldest_first(VERSION_TO_PACKAGE)
        if not candidates:
            return None

        try:
            client = VeeamClient(
                host=host,
                api_version=candidates[0],
                verify_ssl=verify_ssl,
                username=username,
                password=password,
                token=token,
            )
            await client.connect()
        except Exception as err:  # noqa: BLE001 - detection never raises on the caller's behalf
            _LOGGER.debug("Could not log in to %s to read its version: %s", host, err)
            return None

    try:
        about = await client.call(client.api("about").get_about_information)
    except Exception as err:  # noqa: BLE001 - see above
        _LOGGER.debug("Could not read /about from %s: %s", host, err)
        return None
    finally:
        if owns_client:
            try:
                await client.close()
            except Exception as err:  # noqa: BLE001
                _LOGGER.debug("Could not close the detection client: %s", err)

    server_version = getattr(about, "server_version", None)
    if not isinstance(server_version, str) or not server_version.strip():
        _LOGGER.debug("%s did not report a server version", host)
        return None

    return server_version.strip()


async def detect_api_version(
    host: str,
    *,
    username: str | None = None,
    password: str | None = None,
    token: str | None = None,
    verify_ssl: bool = True,
    versions: Sequence[str] | None = None,
    client: Any | None = None,
) -> str | None:
    """Return the API version to talk to this console with, or None.

    Reads the console's version from ``/api/v3/about`` and maps it through
    ``SERVER_TO_API_VERSION``. See ``detect_server_version`` for the arguments; ``versions``
    narrows the answer to API versions the caller can accept.
    """
    server_version = await detect_server_version(
        host,
        username=username,
        password=password,
        token=token,
        verify_ssl=verify_ssl,
        client=client,
    )
    if server_version is None:
        return None

    detected = api_version_for_server(server_version, versions=versions)
    if detected is None:
        _LOGGER.debug("No supported API version matches console version %s", server_version)
    else:
        _LOGGER.debug(
            "Console %s reports version %s; selected API %s", host, server_version, detected
        )
    return detected
