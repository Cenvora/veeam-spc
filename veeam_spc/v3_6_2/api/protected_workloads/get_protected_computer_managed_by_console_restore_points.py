from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.get_protected_computer_managed_by_console_restore_points_response_200 import (
    GetProtectedComputerManagedByConsoleRestorePointsResponse200,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    backup_agent_uid: UUID,
    *,
    limit: int | Unset = 100,
    offset: int | Unset = 0,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_request_id, Unset):
        headers["X-Request-id"] = x_request_id

    if not isinstance(x_client_version, Unset):
        headers["X-Client-Version"] = x_client_version

    params: dict[str, Any] = {}

    params["limit"] = limit

    params["offset"] = offset

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/protectedWorkloads/computersManagedByConsole/{backup_agent_uid}/restorePoints".format(
            backup_agent_uid=quote(str(backup_agent_uid), safe=""),
        ),
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | ErrorResponse | GetProtectedComputerManagedByConsoleRestorePointsResponse200:
    if response.status_code == 200:
        response_200 = GetProtectedComputerManagedByConsoleRestorePointsResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 202:
        response_202 = cast(Any, None)
        return response_202

    response_default = ErrorResponse.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | ErrorResponse | GetProtectedComputerManagedByConsoleRestorePointsResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    backup_agent_uid: UUID,
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 100,
    offset: int | Unset = 0,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Response[Any | ErrorResponse | GetProtectedComputerManagedByConsoleRestorePointsResponse200]:
    """Get All Restore Points of Protected Computer Managed by Veeam Service Provider Console

     Returns a collection resource representation of restore points created for a protected computer
    managed by Veeam Service Provider Console with the specified UID of Veeam backup agent installed on
    the computer.

    Args:
        backup_agent_uid (UUID):
        limit (int | Unset):  Default: 100.
        offset (int | Unset):  Default: 0.
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ErrorResponse | GetProtectedComputerManagedByConsoleRestorePointsResponse200]
    """

    kwargs = _get_kwargs(
        backup_agent_uid=backup_agent_uid,
        limit=limit,
        offset=offset,
        x_request_id=x_request_id,
        x_client_version=x_client_version,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    backup_agent_uid: UUID,
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 100,
    offset: int | Unset = 0,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Any | ErrorResponse | GetProtectedComputerManagedByConsoleRestorePointsResponse200 | None:
    """Get All Restore Points of Protected Computer Managed by Veeam Service Provider Console

     Returns a collection resource representation of restore points created for a protected computer
    managed by Veeam Service Provider Console with the specified UID of Veeam backup agent installed on
    the computer.

    Args:
        backup_agent_uid (UUID):
        limit (int | Unset):  Default: 100.
        offset (int | Unset):  Default: 0.
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ErrorResponse | GetProtectedComputerManagedByConsoleRestorePointsResponse200
    """

    return sync_detailed(
        backup_agent_uid=backup_agent_uid,
        client=client,
        limit=limit,
        offset=offset,
        x_request_id=x_request_id,
        x_client_version=x_client_version,
    ).parsed


async def asyncio_detailed(
    backup_agent_uid: UUID,
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 100,
    offset: int | Unset = 0,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Response[Any | ErrorResponse | GetProtectedComputerManagedByConsoleRestorePointsResponse200]:
    """Get All Restore Points of Protected Computer Managed by Veeam Service Provider Console

     Returns a collection resource representation of restore points created for a protected computer
    managed by Veeam Service Provider Console with the specified UID of Veeam backup agent installed on
    the computer.

    Args:
        backup_agent_uid (UUID):
        limit (int | Unset):  Default: 100.
        offset (int | Unset):  Default: 0.
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ErrorResponse | GetProtectedComputerManagedByConsoleRestorePointsResponse200]
    """

    kwargs = _get_kwargs(
        backup_agent_uid=backup_agent_uid,
        limit=limit,
        offset=offset,
        x_request_id=x_request_id,
        x_client_version=x_client_version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    backup_agent_uid: UUID,
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 100,
    offset: int | Unset = 0,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Any | ErrorResponse | GetProtectedComputerManagedByConsoleRestorePointsResponse200 | None:
    """Get All Restore Points of Protected Computer Managed by Veeam Service Provider Console

     Returns a collection resource representation of restore points created for a protected computer
    managed by Veeam Service Provider Console with the specified UID of Veeam backup agent installed on
    the computer.

    Args:
        backup_agent_uid (UUID):
        limit (int | Unset):  Default: 100.
        offset (int | Unset):  Default: 0.
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ErrorResponse | GetProtectedComputerManagedByConsoleRestorePointsResponse200
    """

    return (
        await asyncio_detailed(
            backup_agent_uid=backup_agent_uid,
            client=client,
            limit=limit,
            offset=offset,
            x_request_id=x_request_id,
            x_client_version=x_client_version,
        )
    ).parsed
