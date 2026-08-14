from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.empty_response import EmptyResponse
from ...models.error_response import ErrorResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    action_id: UUID,
    *,
    x_client_version: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_client_version, Unset):
        headers["X-Client-Version"] = x_client_version

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/asyncActions/{action_id}".format(
            action_id=quote(str(action_id), safe=""),
        ),
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> EmptyResponse | ErrorResponse:
    if response.status_code == 200:
        response_200 = EmptyResponse.from_dict(response.json())

        return response_200

    response_default = ErrorResponse.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[EmptyResponse | ErrorResponse]:
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
    x_client_version: str | Unset = UNSET,
) -> Response[EmptyResponse | ErrorResponse]:
    """Cancel Async Action

     Cancels an action with the specified UID.

    Args:
        action_id (UUID):
        x_client_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[EmptyResponse | ErrorResponse]
    """

    kwargs = _get_kwargs(
        action_id=action_id,
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
    x_client_version: str | Unset = UNSET,
) -> EmptyResponse | ErrorResponse | None:
    """Cancel Async Action

     Cancels an action with the specified UID.

    Args:
        action_id (UUID):
        x_client_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        EmptyResponse | ErrorResponse
    """

    return sync_detailed(
        action_id=action_id,
        client=client,
        x_client_version=x_client_version,
    ).parsed


async def asyncio_detailed(
    action_id: UUID,
    *,
    client: AuthenticatedClient,
    x_client_version: str | Unset = UNSET,
) -> Response[EmptyResponse | ErrorResponse]:
    """Cancel Async Action

     Cancels an action with the specified UID.

    Args:
        action_id (UUID):
        x_client_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[EmptyResponse | ErrorResponse]
    """

    kwargs = _get_kwargs(
        action_id=action_id,
        x_client_version=x_client_version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    action_id: UUID,
    *,
    client: AuthenticatedClient,
    x_client_version: str | Unset = UNSET,
) -> EmptyResponse | ErrorResponse | None:
    """Cancel Async Action

     Cancels an action with the specified UID.

    Args:
        action_id (UUID):
        x_client_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        EmptyResponse | ErrorResponse
    """

    return (
        await asyncio_detailed(
            action_id=action_id,
            client=client,
            x_client_version=x_client_version,
        )
    ).parsed
