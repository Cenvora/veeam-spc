from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.backup_server_backup_job_vmware_object_size import BackupServerBackupJobVmwareObjectSize
from ...models.error_response import ErrorResponse
from ...models.expand_backup_server_virtual_server_objects_response_200 import (
    ExpandBackupServerVirtualServerObjectsResponse200,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    backup_server_uid: UUID,
    *,
    body: list[BackupServerBackupJobVmwareObjectSize],
    filter_: str | Unset = UNSET,
    sort: str | Unset = UNSET,
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

    params["filter"] = filter_

    params["sort"] = sort

    params["limit"] = limit

    params["offset"] = offset

    params["select"] = select

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/infrastructure/backupServers/{backup_server_uid}/servers/objects/expand".format(
            backup_server_uid=quote(str(backup_server_uid), safe=""),
        ),
        "params": params,
    }

    _kwargs["json"] = []
    for body_item_data in body:
        body_item = body_item_data.to_dict()
        _kwargs["json"].append(body_item)

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | ErrorResponse | ExpandBackupServerVirtualServerObjectsResponse200:
    if response.status_code == 200:
        response_200 = ExpandBackupServerVirtualServerObjectsResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 202:
        response_202 = cast(Any, None)
        return response_202

    response_default = ErrorResponse.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | ErrorResponse | ExpandBackupServerVirtualServerObjectsResponse200]:
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
    body: list[BackupServerBackupJobVmwareObjectSize],
    filter_: str | Unset = UNSET,
    sort: str | Unset = UNSET,
    limit: int | Unset = 100,
    offset: int | Unset = 0,
    select: str | Unset = UNSET,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Response[Any | ErrorResponse | ExpandBackupServerVirtualServerObjectsResponse200]:
    """Get VMs in VMware vSphere VM Containers of All vCenter Servers

     Returns a collection resource representation of VMs included in VM containers of all vCenter Servers
    connected to a Veeam Backup & Replication server with the specified UID.
    > Currently, only tags are supported. If you specify other VM containers, you will receive resource
    representations of these containers instead of VMs included in them.

    Args:
        backup_server_uid (UUID):
        filter_ (str | Unset):
        sort (str | Unset):
        limit (int | Unset):  Default: 100.
        offset (int | Unset):  Default: 0.
        select (str | Unset):
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):
        body (list[BackupServerBackupJobVmwareObjectSize]):  Example: [{'inventoryObject':
            {'hostName': 'vcenter01.tech.local', 'name': 'Production', 'type': 'Tag', 'objectId':
            'urn:vmomi:InventoryServiceTag:8f3c2b91-4d5e-4a6b-9c1d-2e7f0a5b3c44:GLOBAL'}, 'size':
            None}].

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ErrorResponse | ExpandBackupServerVirtualServerObjectsResponse200]
    """

    kwargs = _get_kwargs(
        backup_server_uid=backup_server_uid,
        body=body,
        filter_=filter_,
        sort=sort,
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
    body: list[BackupServerBackupJobVmwareObjectSize],
    filter_: str | Unset = UNSET,
    sort: str | Unset = UNSET,
    limit: int | Unset = 100,
    offset: int | Unset = 0,
    select: str | Unset = UNSET,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Any | ErrorResponse | ExpandBackupServerVirtualServerObjectsResponse200 | None:
    """Get VMs in VMware vSphere VM Containers of All vCenter Servers

     Returns a collection resource representation of VMs included in VM containers of all vCenter Servers
    connected to a Veeam Backup & Replication server with the specified UID.
    > Currently, only tags are supported. If you specify other VM containers, you will receive resource
    representations of these containers instead of VMs included in them.

    Args:
        backup_server_uid (UUID):
        filter_ (str | Unset):
        sort (str | Unset):
        limit (int | Unset):  Default: 100.
        offset (int | Unset):  Default: 0.
        select (str | Unset):
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):
        body (list[BackupServerBackupJobVmwareObjectSize]):  Example: [{'inventoryObject':
            {'hostName': 'vcenter01.tech.local', 'name': 'Production', 'type': 'Tag', 'objectId':
            'urn:vmomi:InventoryServiceTag:8f3c2b91-4d5e-4a6b-9c1d-2e7f0a5b3c44:GLOBAL'}, 'size':
            None}].

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ErrorResponse | ExpandBackupServerVirtualServerObjectsResponse200
    """

    return sync_detailed(
        backup_server_uid=backup_server_uid,
        client=client,
        body=body,
        filter_=filter_,
        sort=sort,
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
    body: list[BackupServerBackupJobVmwareObjectSize],
    filter_: str | Unset = UNSET,
    sort: str | Unset = UNSET,
    limit: int | Unset = 100,
    offset: int | Unset = 0,
    select: str | Unset = UNSET,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Response[Any | ErrorResponse | ExpandBackupServerVirtualServerObjectsResponse200]:
    """Get VMs in VMware vSphere VM Containers of All vCenter Servers

     Returns a collection resource representation of VMs included in VM containers of all vCenter Servers
    connected to a Veeam Backup & Replication server with the specified UID.
    > Currently, only tags are supported. If you specify other VM containers, you will receive resource
    representations of these containers instead of VMs included in them.

    Args:
        backup_server_uid (UUID):
        filter_ (str | Unset):
        sort (str | Unset):
        limit (int | Unset):  Default: 100.
        offset (int | Unset):  Default: 0.
        select (str | Unset):
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):
        body (list[BackupServerBackupJobVmwareObjectSize]):  Example: [{'inventoryObject':
            {'hostName': 'vcenter01.tech.local', 'name': 'Production', 'type': 'Tag', 'objectId':
            'urn:vmomi:InventoryServiceTag:8f3c2b91-4d5e-4a6b-9c1d-2e7f0a5b3c44:GLOBAL'}, 'size':
            None}].

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ErrorResponse | ExpandBackupServerVirtualServerObjectsResponse200]
    """

    kwargs = _get_kwargs(
        backup_server_uid=backup_server_uid,
        body=body,
        filter_=filter_,
        sort=sort,
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
    body: list[BackupServerBackupJobVmwareObjectSize],
    filter_: str | Unset = UNSET,
    sort: str | Unset = UNSET,
    limit: int | Unset = 100,
    offset: int | Unset = 0,
    select: str | Unset = UNSET,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Any | ErrorResponse | ExpandBackupServerVirtualServerObjectsResponse200 | None:
    """Get VMs in VMware vSphere VM Containers of All vCenter Servers

     Returns a collection resource representation of VMs included in VM containers of all vCenter Servers
    connected to a Veeam Backup & Replication server with the specified UID.
    > Currently, only tags are supported. If you specify other VM containers, you will receive resource
    representations of these containers instead of VMs included in them.

    Args:
        backup_server_uid (UUID):
        filter_ (str | Unset):
        sort (str | Unset):
        limit (int | Unset):  Default: 100.
        offset (int | Unset):  Default: 0.
        select (str | Unset):
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):
        body (list[BackupServerBackupJobVmwareObjectSize]):  Example: [{'inventoryObject':
            {'hostName': 'vcenter01.tech.local', 'name': 'Production', 'type': 'Tag', 'objectId':
            'urn:vmomi:InventoryServiceTag:8f3c2b91-4d5e-4a6b-9c1d-2e7f0a5b3c44:GLOBAL'}, 'size':
            None}].

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ErrorResponse | ExpandBackupServerVirtualServerObjectsResponse200
    """

    return (
        await asyncio_detailed(
            backup_server_uid=backup_server_uid,
            client=client,
            body=body,
            filter_=filter_,
            sort=sort,
            limit=limit,
            offset=offset,
            select=select,
            x_request_id=x_request_id,
            x_client_version=x_client_version,
        )
    ).parsed
