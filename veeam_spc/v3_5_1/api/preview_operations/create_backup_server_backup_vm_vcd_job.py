from http import HTTPStatus
from typing import Any, Optional, Union, cast
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.backup_server_cloud_director_backup_job_configuration import (
    BackupServerCloudDirectorBackupJobConfiguration,
)
from ...models.create_backup_server_backup_vm_vcd_job_response_200 import CreateBackupServerBackupVmVcdJobResponse200
from ...models.error_response import ErrorResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    backup_server_uid: UUID,
    *,
    body: BackupServerCloudDirectorBackupJobConfiguration,
    mapped_organization_uid: Union[Unset, UUID] = UNSET,
    x_request_id: Union[Unset, UUID] = UNSET,
    x_client_version: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_request_id, Unset):
        headers["X-Request-id"] = x_request_id

    if not isinstance(x_client_version, Unset):
        headers["X-Client-Version"] = x_client_version

    params: dict[str, Any] = {}

    json_mapped_organization_uid: Union[Unset, str] = UNSET
    if not isinstance(mapped_organization_uid, Unset):
        json_mapped_organization_uid = str(mapped_organization_uid)
    params["mappedOrganizationUid"] = json_mapped_organization_uid

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/infrastructure/backupServers/{backup_server_uid}/jobs/backupVmJobs/vcd",
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Union[Any, CreateBackupServerBackupVmVcdJobResponse200, ErrorResponse]:
    if response.status_code == 200:
        response_200 = CreateBackupServerBackupVmVcdJobResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 202:
        response_202 = cast(Any, None)
        return response_202

    response_default = ErrorResponse.from_dict(response.json())

    return response_default


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, CreateBackupServerBackupVmVcdJobResponse200, ErrorResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    backup_server_uid: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
    body: BackupServerCloudDirectorBackupJobConfiguration,
    mapped_organization_uid: Union[Unset, UUID] = UNSET,
    x_request_id: Union[Unset, UUID] = UNSET,
    x_client_version: Union[Unset, str] = UNSET,
) -> Response[Union[Any, CreateBackupServerBackupVmVcdJobResponse200, ErrorResponse]]:
    """Create VMware Cloud Director VM Backup Job

     Creates a VMware Cloud Director VM backup job on a Veeam Backup & Replication server with the
    specified UID.

    Args:
        backup_server_uid (UUID):
        mapped_organization_uid (Union[Unset, UUID]):
        x_request_id (Union[Unset, UUID]):
        x_client_version (Union[Unset, str]):
        body (BackupServerCloudDirectorBackupJobConfiguration): VMware Cloud Director backup job
            configuration.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, CreateBackupServerBackupVmVcdJobResponse200, ErrorResponse]]
    """

    kwargs = _get_kwargs(
        backup_server_uid=backup_server_uid,
        body=body,
        mapped_organization_uid=mapped_organization_uid,
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
    client: Union[AuthenticatedClient, Client],
    body: BackupServerCloudDirectorBackupJobConfiguration,
    mapped_organization_uid: Union[Unset, UUID] = UNSET,
    x_request_id: Union[Unset, UUID] = UNSET,
    x_client_version: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, CreateBackupServerBackupVmVcdJobResponse200, ErrorResponse]]:
    """Create VMware Cloud Director VM Backup Job

     Creates a VMware Cloud Director VM backup job on a Veeam Backup & Replication server with the
    specified UID.

    Args:
        backup_server_uid (UUID):
        mapped_organization_uid (Union[Unset, UUID]):
        x_request_id (Union[Unset, UUID]):
        x_client_version (Union[Unset, str]):
        body (BackupServerCloudDirectorBackupJobConfiguration): VMware Cloud Director backup job
            configuration.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, CreateBackupServerBackupVmVcdJobResponse200, ErrorResponse]
    """

    return sync_detailed(
        backup_server_uid=backup_server_uid,
        client=client,
        body=body,
        mapped_organization_uid=mapped_organization_uid,
        x_request_id=x_request_id,
        x_client_version=x_client_version,
    ).parsed


async def asyncio_detailed(
    backup_server_uid: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
    body: BackupServerCloudDirectorBackupJobConfiguration,
    mapped_organization_uid: Union[Unset, UUID] = UNSET,
    x_request_id: Union[Unset, UUID] = UNSET,
    x_client_version: Union[Unset, str] = UNSET,
) -> Response[Union[Any, CreateBackupServerBackupVmVcdJobResponse200, ErrorResponse]]:
    """Create VMware Cloud Director VM Backup Job

     Creates a VMware Cloud Director VM backup job on a Veeam Backup & Replication server with the
    specified UID.

    Args:
        backup_server_uid (UUID):
        mapped_organization_uid (Union[Unset, UUID]):
        x_request_id (Union[Unset, UUID]):
        x_client_version (Union[Unset, str]):
        body (BackupServerCloudDirectorBackupJobConfiguration): VMware Cloud Director backup job
            configuration.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, CreateBackupServerBackupVmVcdJobResponse200, ErrorResponse]]
    """

    kwargs = _get_kwargs(
        backup_server_uid=backup_server_uid,
        body=body,
        mapped_organization_uid=mapped_organization_uid,
        x_request_id=x_request_id,
        x_client_version=x_client_version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    backup_server_uid: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
    body: BackupServerCloudDirectorBackupJobConfiguration,
    mapped_organization_uid: Union[Unset, UUID] = UNSET,
    x_request_id: Union[Unset, UUID] = UNSET,
    x_client_version: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, CreateBackupServerBackupVmVcdJobResponse200, ErrorResponse]]:
    """Create VMware Cloud Director VM Backup Job

     Creates a VMware Cloud Director VM backup job on a Veeam Backup & Replication server with the
    specified UID.

    Args:
        backup_server_uid (UUID):
        mapped_organization_uid (Union[Unset, UUID]):
        x_request_id (Union[Unset, UUID]):
        x_client_version (Union[Unset, str]):
        body (BackupServerCloudDirectorBackupJobConfiguration): VMware Cloud Director backup job
            configuration.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, CreateBackupServerBackupVmVcdJobResponse200, ErrorResponse]
    """

    return (
        await asyncio_detailed(
            backup_server_uid=backup_server_uid,
            client=client,
            body=body,
            mapped_organization_uid=mapped_organization_uid,
            x_request_id=x_request_id,
            x_client_version=x_client_version,
        )
    ).parsed
