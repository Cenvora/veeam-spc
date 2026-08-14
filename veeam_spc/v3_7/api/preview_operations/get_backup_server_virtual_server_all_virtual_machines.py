from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.get_backup_server_virtual_server_all_virtual_machines_name_sorting_direction import (
    GetBackupServerVirtualServerAllVirtualMachinesNameSortingDirection,
)
from ...models.get_backup_server_virtual_server_all_virtual_machines_response_200 import (
    GetBackupServerVirtualServerAllVirtualMachinesResponse200,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    backup_server_uid: UUID,
    *,
    company_uid: UUID | Unset = UNSET,
    name_filter: str | Unset = UNSET,
    name_sorting_direction: GetBackupServerVirtualServerAllVirtualMachinesNameSortingDirection
    | Unset = GetBackupServerVirtualServerAllVirtualMachinesNameSortingDirection.ASCENDING,
    limit: int | Unset = 100,
    offset: int | Unset = 0,
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

    json_company_uid: str | Unset = UNSET
    if not isinstance(company_uid, Unset):
        json_company_uid = str(company_uid)
    params["companyUid"] = json_company_uid

    params["nameFilter"] = name_filter

    json_name_sorting_direction: str | Unset = UNSET
    if not isinstance(name_sorting_direction, Unset):
        json_name_sorting_direction = name_sorting_direction.value

    params["nameSortingDirection"] = json_name_sorting_direction

    params["limit"] = limit

    params["offset"] = offset

    params["select"] = select

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/infrastructure/backupServers/{backup_server_uid}/servers/virtualMachines".format(
            backup_server_uid=quote(str(backup_server_uid), safe=""),
        ),
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | ErrorResponse | GetBackupServerVirtualServerAllVirtualMachinesResponse200:
    if response.status_code == 200:
        response_200 = GetBackupServerVirtualServerAllVirtualMachinesResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 202:
        response_202 = cast(Any, None)
        return response_202

    response_default = ErrorResponse.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | ErrorResponse | GetBackupServerVirtualServerAllVirtualMachinesResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    backup_server_uid: UUID,
    *,
    client: AuthenticatedClient,
    company_uid: UUID | Unset = UNSET,
    name_filter: str | Unset = UNSET,
    name_sorting_direction: GetBackupServerVirtualServerAllVirtualMachinesNameSortingDirection
    | Unset = GetBackupServerVirtualServerAllVirtualMachinesNameSortingDirection.ASCENDING,
    limit: int | Unset = 100,
    offset: int | Unset = 0,
    select: str | Unset = UNSET,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Response[Any | ErrorResponse | GetBackupServerVirtualServerAllVirtualMachinesResponse200]:
    """Get All VMs Marked With Tags From All Connected vCenter Servers

     Returns a collection resource representation of all VMs marked with tags in all vCenter Servers
    connected to a Veeam Backup & Replication server with the specified UID.

    Args:
        backup_server_uid (UUID):
        company_uid (UUID | Unset):
        name_filter (str | Unset):
        name_sorting_direction (GetBackupServerVirtualServerAllVirtualMachinesNameSortingDirection
            | Unset):  Default:
            GetBackupServerVirtualServerAllVirtualMachinesNameSortingDirection.ASCENDING.
        limit (int | Unset):  Default: 100.
        offset (int | Unset):  Default: 0.
        select (str | Unset):
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ErrorResponse | GetBackupServerVirtualServerAllVirtualMachinesResponse200]
    """

    kwargs = _get_kwargs(
        backup_server_uid=backup_server_uid,
        company_uid=company_uid,
        name_filter=name_filter,
        name_sorting_direction=name_sorting_direction,
        limit=limit,
        offset=offset,
        select=select,
        x_request_id=x_request_id,
        x_client_version=x_client_version,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    backup_server_uid: UUID,
    *,
    client: AuthenticatedClient,
    company_uid: UUID | Unset = UNSET,
    name_filter: str | Unset = UNSET,
    name_sorting_direction: GetBackupServerVirtualServerAllVirtualMachinesNameSortingDirection
    | Unset = GetBackupServerVirtualServerAllVirtualMachinesNameSortingDirection.ASCENDING,
    limit: int | Unset = 100,
    offset: int | Unset = 0,
    select: str | Unset = UNSET,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Any | ErrorResponse | GetBackupServerVirtualServerAllVirtualMachinesResponse200 | None:
    """Get All VMs Marked With Tags From All Connected vCenter Servers

     Returns a collection resource representation of all VMs marked with tags in all vCenter Servers
    connected to a Veeam Backup & Replication server with the specified UID.

    Args:
        backup_server_uid (UUID):
        company_uid (UUID | Unset):
        name_filter (str | Unset):
        name_sorting_direction (GetBackupServerVirtualServerAllVirtualMachinesNameSortingDirection
            | Unset):  Default:
            GetBackupServerVirtualServerAllVirtualMachinesNameSortingDirection.ASCENDING.
        limit (int | Unset):  Default: 100.
        offset (int | Unset):  Default: 0.
        select (str | Unset):
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ErrorResponse | GetBackupServerVirtualServerAllVirtualMachinesResponse200
    """

    return sync_detailed(
        backup_server_uid=backup_server_uid,
        client=client,
        company_uid=company_uid,
        name_filter=name_filter,
        name_sorting_direction=name_sorting_direction,
        limit=limit,
        offset=offset,
        select=select,
        x_request_id=x_request_id,
        x_client_version=x_client_version,
    ).parsed


async def asyncio_detailed(
    backup_server_uid: UUID,
    *,
    client: AuthenticatedClient,
    company_uid: UUID | Unset = UNSET,
    name_filter: str | Unset = UNSET,
    name_sorting_direction: GetBackupServerVirtualServerAllVirtualMachinesNameSortingDirection
    | Unset = GetBackupServerVirtualServerAllVirtualMachinesNameSortingDirection.ASCENDING,
    limit: int | Unset = 100,
    offset: int | Unset = 0,
    select: str | Unset = UNSET,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Response[Any | ErrorResponse | GetBackupServerVirtualServerAllVirtualMachinesResponse200]:
    """Get All VMs Marked With Tags From All Connected vCenter Servers

     Returns a collection resource representation of all VMs marked with tags in all vCenter Servers
    connected to a Veeam Backup & Replication server with the specified UID.

    Args:
        backup_server_uid (UUID):
        company_uid (UUID | Unset):
        name_filter (str | Unset):
        name_sorting_direction (GetBackupServerVirtualServerAllVirtualMachinesNameSortingDirection
            | Unset):  Default:
            GetBackupServerVirtualServerAllVirtualMachinesNameSortingDirection.ASCENDING.
        limit (int | Unset):  Default: 100.
        offset (int | Unset):  Default: 0.
        select (str | Unset):
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ErrorResponse | GetBackupServerVirtualServerAllVirtualMachinesResponse200]
    """

    kwargs = _get_kwargs(
        backup_server_uid=backup_server_uid,
        company_uid=company_uid,
        name_filter=name_filter,
        name_sorting_direction=name_sorting_direction,
        limit=limit,
        offset=offset,
        select=select,
        x_request_id=x_request_id,
        x_client_version=x_client_version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    backup_server_uid: UUID,
    *,
    client: AuthenticatedClient,
    company_uid: UUID | Unset = UNSET,
    name_filter: str | Unset = UNSET,
    name_sorting_direction: GetBackupServerVirtualServerAllVirtualMachinesNameSortingDirection
    | Unset = GetBackupServerVirtualServerAllVirtualMachinesNameSortingDirection.ASCENDING,
    limit: int | Unset = 100,
    offset: int | Unset = 0,
    select: str | Unset = UNSET,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Any | ErrorResponse | GetBackupServerVirtualServerAllVirtualMachinesResponse200 | None:
    """Get All VMs Marked With Tags From All Connected vCenter Servers

     Returns a collection resource representation of all VMs marked with tags in all vCenter Servers
    connected to a Veeam Backup & Replication server with the specified UID.

    Args:
        backup_server_uid (UUID):
        company_uid (UUID | Unset):
        name_filter (str | Unset):
        name_sorting_direction (GetBackupServerVirtualServerAllVirtualMachinesNameSortingDirection
            | Unset):  Default:
            GetBackupServerVirtualServerAllVirtualMachinesNameSortingDirection.ASCENDING.
        limit (int | Unset):  Default: 100.
        offset (int | Unset):  Default: 0.
        select (str | Unset):
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ErrorResponse | GetBackupServerVirtualServerAllVirtualMachinesResponse200
    """

    return (
        await asyncio_detailed(
            backup_server_uid=backup_server_uid,
            client=client,
            company_uid=company_uid,
            name_filter=name_filter,
            name_sorting_direction=name_sorting_direction,
            limit=limit,
            offset=offset,
            select=select,
            x_request_id=x_request_id,
            x_client_version=x_client_version,
        )
    ).parsed
