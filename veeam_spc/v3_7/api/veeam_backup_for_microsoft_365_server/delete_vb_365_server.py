from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.empty_response import EmptyResponse
from ...models.error_response import ErrorResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    vb_365_server_uid: UUID,
    *,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_request_id, Unset):
        headers["X-Request-id"] = x_request_id

    if not isinstance(x_client_version, Unset):
        headers["X-Client-Version"] = x_client_version

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/infrastructure/vb365Servers/{vb_365_server_uid}".format(
            vb_365_server_uid=quote(str(vb_365_server_uid), safe=""),
        ),
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | EmptyResponse | ErrorResponse:
    if response.status_code == 200:
        response_200 = EmptyResponse.from_dict(response.json())

        return response_200

    if response.status_code == 202:
        response_202 = cast(Any, None)
        return response_202

    response_default = ErrorResponse.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | EmptyResponse | ErrorResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    vb_365_server_uid: UUID,
    *,
    client: AuthenticatedClient,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Response[Any | EmptyResponse | ErrorResponse]:
    """Delete Veeam Backup for Microsoft 365 Server

     Removes a Veeam Backup for Microsoft 365 server with the specified UID from the Veeam Service
    Provider Console database.

    Args:
        vb_365_server_uid (UUID):
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | EmptyResponse | ErrorResponse]
    """

    kwargs = _get_kwargs(
        vb_365_server_uid=vb_365_server_uid,
        x_request_id=x_request_id,
        x_client_version=x_client_version,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    vb_365_server_uid: UUID,
    *,
    client: AuthenticatedClient,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Any | EmptyResponse | ErrorResponse | None:
    """Delete Veeam Backup for Microsoft 365 Server

     Removes a Veeam Backup for Microsoft 365 server with the specified UID from the Veeam Service
    Provider Console database.

    Args:
        vb_365_server_uid (UUID):
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | EmptyResponse | ErrorResponse
    """

    return sync_detailed(
        vb_365_server_uid=vb_365_server_uid,
        client=client,
        x_request_id=x_request_id,
        x_client_version=x_client_version,
    ).parsed


async def asyncio_detailed(
    vb_365_server_uid: UUID,
    *,
    client: AuthenticatedClient,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Response[Any | EmptyResponse | ErrorResponse]:
    """Delete Veeam Backup for Microsoft 365 Server

     Removes a Veeam Backup for Microsoft 365 server with the specified UID from the Veeam Service
    Provider Console database.

    Args:
        vb_365_server_uid (UUID):
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | EmptyResponse | ErrorResponse]
    """

    kwargs = _get_kwargs(
        vb_365_server_uid=vb_365_server_uid,
        x_request_id=x_request_id,
        x_client_version=x_client_version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    vb_365_server_uid: UUID,
    *,
    client: AuthenticatedClient,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Any | EmptyResponse | ErrorResponse | None:
    """Delete Veeam Backup for Microsoft 365 Server

     Removes a Veeam Backup for Microsoft 365 server with the specified UID from the Veeam Service
    Provider Console database.

    Args:
        vb_365_server_uid (UUID):
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | EmptyResponse | ErrorResponse
    """

    return (
        await asyncio_detailed(
            vb_365_server_uid=vb_365_server_uid,
            client=client,
            x_request_id=x_request_id,
            x_client_version=x_client_version,
        )
    ).parsed
