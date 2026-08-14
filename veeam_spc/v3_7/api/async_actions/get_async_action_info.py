from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.get_async_action_info_response_200 import GetAsyncActionInfoResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    action_id: UUID,
    *,
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
        "method": "get",
        "url": "/asyncActions/{action_id}".format(
            action_id=quote(str(action_id), safe=""),
        ),
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | GetAsyncActionInfoResponse200:
    if response.status_code == 200:
        response_200 = GetAsyncActionInfoResponse200.from_dict(response.json())

        return response_200

    response_default = ErrorResponse.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ErrorResponse | GetAsyncActionInfoResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    action_id: UUID,
    *,
    client: AuthenticatedClient,
    select: str | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Response[ErrorResponse | GetAsyncActionInfoResponse200]:
    """Get Async Action

     Returns a resource representation of an async action with the specified UID.

    Args:
        action_id (UUID):
        select (str | Unset):
        x_client_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | GetAsyncActionInfoResponse200]
    """

    kwargs = _get_kwargs(
        action_id=action_id,
        select=select,
        x_client_version=x_client_version,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    action_id: UUID,
    *,
    client: AuthenticatedClient,
    select: str | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> ErrorResponse | GetAsyncActionInfoResponse200 | None:
    """Get Async Action

     Returns a resource representation of an async action with the specified UID.

    Args:
        action_id (UUID):
        select (str | Unset):
        x_client_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | GetAsyncActionInfoResponse200
    """

    return sync_detailed(
        action_id=action_id,
        client=client,
        select=select,
        x_client_version=x_client_version,
    ).parsed


async def asyncio_detailed(
    action_id: UUID,
    *,
    client: AuthenticatedClient,
    select: str | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Response[ErrorResponse | GetAsyncActionInfoResponse200]:
    """Get Async Action

     Returns a resource representation of an async action with the specified UID.

    Args:
        action_id (UUID):
        select (str | Unset):
        x_client_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | GetAsyncActionInfoResponse200]
    """

    kwargs = _get_kwargs(
        action_id=action_id,
        select=select,
        x_client_version=x_client_version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    action_id: UUID,
    *,
    client: AuthenticatedClient,
    select: str | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> ErrorResponse | GetAsyncActionInfoResponse200 | None:
    """Get Async Action

     Returns a resource representation of an async action with the specified UID.

    Args:
        action_id (UUID):
        select (str | Unset):
        x_client_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | GetAsyncActionInfoResponse200
    """

    return (
        await asyncio_detailed(
            action_id=action_id,
            client=client,
            select=select,
            x_client_version=x_client_version,
        )
    ).parsed
