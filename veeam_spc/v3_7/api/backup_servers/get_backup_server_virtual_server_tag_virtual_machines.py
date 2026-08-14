from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.get_backup_server_virtual_server_tag_virtual_machines_name_sorting_direction import (
    GetBackupServerVirtualServerTagVirtualMachinesNameSortingDirection,
)
from ...models.get_backup_server_virtual_server_tag_virtual_machines_response_200 import (
    GetBackupServerVirtualServerTagVirtualMachinesResponse200,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    backup_server_uid: UUID,
    virtual_center_uid: UUID,
    tag_urn: str,
    *,
    name_filter: str | Unset = UNSET,
    name_sorting_direction: GetBackupServerVirtualServerTagVirtualMachinesNameSortingDirection
    | Unset = GetBackupServerVirtualServerTagVirtualMachinesNameSortingDirection.ASCENDING,
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
        "url": "/infrastructure/backupServers/{backup_server_uid}/servers/virtualCenter/{virtual_center_uid}/tags/{tag_urn}/virtualMachines".format(
            backup_server_uid=quote(str(backup_server_uid), safe=""),
            virtual_center_uid=quote(str(virtual_center_uid), safe=""),
            tag_urn=quote(str(tag_urn), safe=""),
        ),
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | ErrorResponse | GetBackupServerVirtualServerTagVirtualMachinesResponse200:
    if response.status_code == 200:
        response_200 = GetBackupServerVirtualServerTagVirtualMachinesResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 202:
        response_202 = cast(Any, None)
        return response_202

    response_default = ErrorResponse.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | ErrorResponse | GetBackupServerVirtualServerTagVirtualMachinesResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    backup_server_uid: UUID,
    virtual_center_uid: UUID,
    tag_urn: str,
    *,
    client: AuthenticatedClient,
    name_filter: str | Unset = UNSET,
    name_sorting_direction: GetBackupServerVirtualServerTagVirtualMachinesNameSortingDirection
    | Unset = GetBackupServerVirtualServerTagVirtualMachinesNameSortingDirection.ASCENDING,
    limit: int | Unset = 100,
    offset: int | Unset = 0,
    select: str | Unset = UNSET,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Response[Any | ErrorResponse | GetBackupServerVirtualServerTagVirtualMachinesResponse200]:
    """Get All VMs Marked with vCenter Server Tag

     Returns a resource representation of all VMs marked with a vCenter Server tag with the specified
    URN.

    Args:
        backup_server_uid (UUID):
        virtual_center_uid (UUID):
        tag_urn (str):
        name_filter (str | Unset):
        name_sorting_direction (GetBackupServerVirtualServerTagVirtualMachinesNameSortingDirection
            | Unset):  Default:
            GetBackupServerVirtualServerTagVirtualMachinesNameSortingDirection.ASCENDING.
        limit (int | Unset):  Default: 100.
        offset (int | Unset):  Default: 0.
        select (str | Unset):
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ErrorResponse | GetBackupServerVirtualServerTagVirtualMachinesResponse200]
    """

    kwargs = _get_kwargs(
        backup_server_uid=backup_server_uid,
        virtual_center_uid=virtual_center_uid,
        tag_urn=tag_urn,
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
    virtual_center_uid: UUID,
    tag_urn: str,
    *,
    client: AuthenticatedClient,
    name_filter: str | Unset = UNSET,
    name_sorting_direction: GetBackupServerVirtualServerTagVirtualMachinesNameSortingDirection
    | Unset = GetBackupServerVirtualServerTagVirtualMachinesNameSortingDirection.ASCENDING,
    limit: int | Unset = 100,
    offset: int | Unset = 0,
    select: str | Unset = UNSET,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Any | ErrorResponse | GetBackupServerVirtualServerTagVirtualMachinesResponse200 | None:
    """Get All VMs Marked with vCenter Server Tag

     Returns a resource representation of all VMs marked with a vCenter Server tag with the specified
    URN.

    Args:
        backup_server_uid (UUID):
        virtual_center_uid (UUID):
        tag_urn (str):
        name_filter (str | Unset):
        name_sorting_direction (GetBackupServerVirtualServerTagVirtualMachinesNameSortingDirection
            | Unset):  Default:
            GetBackupServerVirtualServerTagVirtualMachinesNameSortingDirection.ASCENDING.
        limit (int | Unset):  Default: 100.
        offset (int | Unset):  Default: 0.
        select (str | Unset):
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ErrorResponse | GetBackupServerVirtualServerTagVirtualMachinesResponse200
    """

    return sync_detailed(
        backup_server_uid=backup_server_uid,
        virtual_center_uid=virtual_center_uid,
        tag_urn=tag_urn,
        client=client,
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
    virtual_center_uid: UUID,
    tag_urn: str,
    *,
    client: AuthenticatedClient,
    name_filter: str | Unset = UNSET,
    name_sorting_direction: GetBackupServerVirtualServerTagVirtualMachinesNameSortingDirection
    | Unset = GetBackupServerVirtualServerTagVirtualMachinesNameSortingDirection.ASCENDING,
    limit: int | Unset = 100,
    offset: int | Unset = 0,
    select: str | Unset = UNSET,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Response[Any | ErrorResponse | GetBackupServerVirtualServerTagVirtualMachinesResponse200]:
    """Get All VMs Marked with vCenter Server Tag

     Returns a resource representation of all VMs marked with a vCenter Server tag with the specified
    URN.

    Args:
        backup_server_uid (UUID):
        virtual_center_uid (UUID):
        tag_urn (str):
        name_filter (str | Unset):
        name_sorting_direction (GetBackupServerVirtualServerTagVirtualMachinesNameSortingDirection
            | Unset):  Default:
            GetBackupServerVirtualServerTagVirtualMachinesNameSortingDirection.ASCENDING.
        limit (int | Unset):  Default: 100.
        offset (int | Unset):  Default: 0.
        select (str | Unset):
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ErrorResponse | GetBackupServerVirtualServerTagVirtualMachinesResponse200]
    """

    kwargs = _get_kwargs(
        backup_server_uid=backup_server_uid,
        virtual_center_uid=virtual_center_uid,
        tag_urn=tag_urn,
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
    virtual_center_uid: UUID,
    tag_urn: str,
    *,
    client: AuthenticatedClient,
    name_filter: str | Unset = UNSET,
    name_sorting_direction: GetBackupServerVirtualServerTagVirtualMachinesNameSortingDirection
    | Unset = GetBackupServerVirtualServerTagVirtualMachinesNameSortingDirection.ASCENDING,
    limit: int | Unset = 100,
    offset: int | Unset = 0,
    select: str | Unset = UNSET,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Any | ErrorResponse | GetBackupServerVirtualServerTagVirtualMachinesResponse200 | None:
    """Get All VMs Marked with vCenter Server Tag

     Returns a resource representation of all VMs marked with a vCenter Server tag with the specified
    URN.

    Args:
        backup_server_uid (UUID):
        virtual_center_uid (UUID):
        tag_urn (str):
        name_filter (str | Unset):
        name_sorting_direction (GetBackupServerVirtualServerTagVirtualMachinesNameSortingDirection
            | Unset):  Default:
            GetBackupServerVirtualServerTagVirtualMachinesNameSortingDirection.ASCENDING.
        limit (int | Unset):  Default: 100.
        offset (int | Unset):  Default: 0.
        select (str | Unset):
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ErrorResponse | GetBackupServerVirtualServerTagVirtualMachinesResponse200
    """

    return (
        await asyncio_detailed(
            backup_server_uid=backup_server_uid,
            virtual_center_uid=virtual_center_uid,
            tag_urn=tag_urn,
            client=client,
            name_filter=name_filter,
            name_sorting_direction=name_sorting_direction,
            limit=limit,
            offset=offset,
            select=select,
            x_request_id=x_request_id,
            x_client_version=x_client_version,
        )
    ).parsed
