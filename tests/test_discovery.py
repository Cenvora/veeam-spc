"""Tests for API version detection.

VSPC serves every version on /api/v3, so there is nothing to probe — detection reads the
console's own version from /about and maps it. The console is stood in for by a stub client
with the same surface VeeamClient exposes.
"""

import pytest

from veeam_spc.discovery import (
    SERVER_TO_API_VERSION,
    api_version_for_server,
    detect_api_version,
    detect_server_version,
    newest_first,
    oldest_first,
)
from veeam_spc.versions import VERSION_TO_PACKAGE

HOST = "https://vspc.example.com:1280"


class StubAbout:
    def __init__(self, server_version):
        self.server_version = server_version


class StubClient:
    """Stands in for a connected VeeamClient.

    Records what was asked for so tests can assert the /about operation is the one used.
    """

    def __init__(self, about=None, fail_with=None):
        self._about = about
        self._fail_with = fail_with
        self.calls = []
        self.closed = False

    def api(self, name):
        self.calls.append(name)
        return self

    async def get_about_information(self):
        raise AssertionError("the operation should be handed to call(), not invoked directly")

    async def call(self, fn, *args, **kwargs):
        if self._fail_with is not None:
            raise self._fail_with
        return self._about

    async def close(self):
        self.closed = True


# ---------------------------------------------------------------------------
# Version ordering and mapping
# ---------------------------------------------------------------------------


@pytest.mark.parametrize(
    "versions,expected",
    [
        (["3.5.1", "3.6.2", "3.6"], ["3.6.2", "3.6", "3.5.1"]),
        # Numeric ordering, which string sorting would get wrong
        (["3.6", "3.10"], ["3.10", "3.6"]),
        # A version with more components sorts above the same prefix
        (["3.6", "3.6.1"], ["3.6.1", "3.6"]),
        # Unrecognizable entries are dropped rather than ordered arbitrarily
        (["3.6", "nonsense", None, ""], ["3.6"]),
        ([], []),
    ],
)
def test_newest_first(versions, expected):
    assert newest_first(versions) == expected


def test_oldest_first_is_the_reverse():
    assert oldest_first(VERSION_TO_PACKAGE) == list(reversed(newest_first(VERSION_TO_PACKAGE)))


@pytest.mark.parametrize(
    "server_version,expected",
    [
        # The four-component build strings a console actually reports
        ("9.3.0.35057", "3.7"),
        ("9.2.0.32907", "3.6.2"),
        ("9.1.0.100", "3.6.1"),
        ("9.0.0.1", "3.6"),
        ("8.1.0.1", "3.5.1"),
        # Two-component forms map the same way
        ("9.3", "3.7"),
        ("9.2", "3.6.2"),
        ("9", "3.6"),
        # A console newer than anything packaged gets the newest version this package speaks,
        # since VSPC keeps older X-Client-Version values working
        ("10.0.0.1", "3.7"),
        ("9.4.0.1", "3.7"),
        # Older than the oldest supported console: say so rather than guess
        ("8.0.0.1", None),
        ("7.9", None),
        # Not a version at all
        ("", None),
        (None, None),
        ("unknown", None),
    ],
)
def test_api_version_for_server(server_version, expected):
    assert api_version_for_server(server_version) == expected


def test_every_mapped_api_version_is_packaged():
    """A mapping pointing at a version this package cannot speak would be a dead end."""
    assert set(SERVER_TO_API_VERSION.values()) <= set(VERSION_TO_PACKAGE)


def test_every_packaged_api_version_is_reachable_by_detection():
    """The direction that actually goes wrong.

    Packaging a version and forgetting to map the console release that serves it is silent:
    detection still answers, because a console newer than everything mapped falls back to the
    newest mapped version. So a 9.3 console kept resolving to 3.6.2 after 3.7 was added, and
    nothing failed — it just quietly spoke the older API.
    """
    unmapped = set(VERSION_TO_PACKAGE) - set(SERVER_TO_API_VERSION.values())

    assert not unmapped, (
        f"{sorted(unmapped)} can be spoken but no console release maps to it; add the release "
        "to SERVER_TO_API_VERSION"
    )


def test_candidate_list_can_be_narrowed():
    """A caller that cannot use the newest version should not be handed it."""
    assert api_version_for_server("9.2.0.32907", versions=["3.5.1", "3.6"]) == "3.6"


def test_narrowing_to_nothing_supported_returns_none():
    assert api_version_for_server("9.2.0.32907", versions=[]) is None


# ---------------------------------------------------------------------------
# Reading the console version
# ---------------------------------------------------------------------------


@pytest.mark.asyncio
async def test_reads_the_server_version_from_about():
    client = StubClient(about=StubAbout("9.2.0.32907"))

    assert await detect_server_version(HOST, client=client) == "9.2.0.32907"
    assert client.calls == ["about"]


@pytest.mark.asyncio
async def test_a_supplied_client_is_left_open():
    """Reusing a caller's client must not close it out from under them."""
    client = StubClient(about=StubAbout("9.2.0.32907"))

    await detect_server_version(HOST, client=client)

    assert not client.closed


@pytest.mark.asyncio
async def test_returns_none_when_about_fails():
    client = StubClient(fail_with=RuntimeError("permission denied"))

    assert await detect_server_version(HOST, client=client) is None


@pytest.mark.asyncio
async def test_returns_none_when_no_version_is_reported():
    client = StubClient(about=StubAbout(""))

    assert await detect_server_version(HOST, client=client) is None


@pytest.mark.asyncio
async def test_returns_none_when_about_is_missing_the_field():
    client = StubClient(about=object())

    assert await detect_server_version(HOST, client=client) is None


@pytest.mark.asyncio
async def test_detects_the_api_version_end_to_end():
    client = StubClient(about=StubAbout("9.1.0.404"))

    assert await detect_api_version(HOST, client=client) == "3.6.1"


@pytest.mark.asyncio
async def test_detection_failure_leaves_the_choice_to_the_caller():
    client = StubClient(fail_with=RuntimeError("unreachable"))

    assert await detect_api_version(HOST, client=client) is None


@pytest.mark.asyncio
async def test_detected_version_is_usable_with_veeam_client():
    """Detection is only useful if its result routes to a real SDK package."""
    from veeam_spc.client import VeeamClient

    client = StubClient(about=StubAbout("9.2.0.32907"))
    detected = await detect_api_version(HOST, client=client)

    vc = VeeamClient(host=HOST, api_version=detected, token="token")
    assert vc.package == VERSION_TO_PACKAGE[detected]


@pytest.mark.asyncio
async def test_login_failure_returns_none_rather_than_raising(monkeypatch):
    """Detection is best-effort: a refused login is an answer of None, not an exception."""

    class Refusing:
        def __init__(self, **kwargs):
            self.api_version = kwargs.get("api_version")

        async def connect(self):
            raise PermissionError("invalid credentials")

    import veeam_spc.client as client_module

    monkeypatch.setattr(client_module, "VeeamClient", Refusing)

    assert await detect_api_version(HOST, username="administrator", password="wrong") is None


@pytest.mark.asyncio
async def test_logs_in_declaring_the_oldest_supported_version(monkeypatch):
    """X-Client-Version declares a client capability, and an old console accepts only old ones."""
    seen = {}

    class Recording:
        def __init__(self, **kwargs):
            seen.update(kwargs)

        async def connect(self):
            pass

        def api(self, name):
            return self

        async def get_about_information(self):
            raise AssertionError("the operation should be handed to call()")

        async def call(self, fn, *args, **kwargs):
            return StubAbout("8.1.0.1")

        async def close(self):
            seen["closed"] = True

    import veeam_spc.client as client_module

    monkeypatch.setattr(client_module, "VeeamClient", Recording)

    detected = await detect_api_version(HOST, username="administrator", password="pw")

    assert seen["api_version"] == oldest_first(VERSION_TO_PACKAGE)[0]
    assert seen["closed"] is True
    assert detected == "3.5.1"
