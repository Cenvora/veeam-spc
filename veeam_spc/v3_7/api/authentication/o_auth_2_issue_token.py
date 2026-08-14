from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.o_auth_2_error import OAuth2Error
from ...models.o_auth_2_issue_token_body import OAuth2IssueTokenBody
from ...models.o_auth_2_result import OAuth2Result
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: OAuth2IssueTokenBody,
    select: str | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_client_version, Unset):
        headers["X-Client-Version"] = x_client_version

    params: dict[str, Any] = {}

    params["select"] = select

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/token",
        "params": params,
    }

    _kwargs["data"] = body.to_dict()

    headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> OAuth2Error | OAuth2Result | None:
    if response.status_code == 200:
        response_200 = OAuth2Result.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = OAuth2Error.from_dict(response.json())

        return response_400

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[OAuth2Error | OAuth2Result]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: OAuth2IssueTokenBody,
    select: str | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Response[OAuth2Error | OAuth2Result]:
    """OAuth 2.0 Authentication

     Performs authentication using the OAuth 2.0 Authorization Framework.

    Args:
        select (str | Unset):
        x_client_version (str | Unset):
        body (OAuth2IssueTokenBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OAuth2Error | OAuth2Result]
    """

    kwargs = _get_kwargs(
        body=body,
        select=select,
        x_client_version=x_client_version,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: OAuth2IssueTokenBody,
    select: str | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> OAuth2Error | OAuth2Result | None:
    """OAuth 2.0 Authentication

     Performs authentication using the OAuth 2.0 Authorization Framework.

    Args:
        select (str | Unset):
        x_client_version (str | Unset):
        body (OAuth2IssueTokenBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OAuth2Error | OAuth2Result
    """

    return sync_detailed(
        client=client,
        body=body,
        select=select,
        x_client_version=x_client_version,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: OAuth2IssueTokenBody,
    select: str | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Response[OAuth2Error | OAuth2Result]:
    """OAuth 2.0 Authentication

     Performs authentication using the OAuth 2.0 Authorization Framework.

    Args:
        select (str | Unset):
        x_client_version (str | Unset):
        body (OAuth2IssueTokenBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OAuth2Error | OAuth2Result]
    """

    kwargs = _get_kwargs(
        body=body,
        select=select,
        x_client_version=x_client_version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: OAuth2IssueTokenBody,
    select: str | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> OAuth2Error | OAuth2Result | None:
    """OAuth 2.0 Authentication

     Performs authentication using the OAuth 2.0 Authorization Framework.

    Args:
        select (str | Unset):
        x_client_version (str | Unset):
        body (OAuth2IssueTokenBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OAuth2Error | OAuth2Result
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            select=select,
            x_client_version=x_client_version,
        )
    ).parsed
