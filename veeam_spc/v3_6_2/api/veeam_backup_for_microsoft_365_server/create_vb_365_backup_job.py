from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.create_vb_365_backup_job_response_200 import CreateVb365BackupJobResponse200
from ...models.error_response import ErrorResponse
from ...models.vb_365_backup_job import Vb365BackupJob
from ...types import UNSET, Response, Unset


def _get_kwargs(
    vb_365_server_uid: UUID,
    vb_365_organization_uid: UUID,
    *,
    body: Vb365BackupJob,
    start_job_after_creation: bool | Unset = False,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_request_id, Unset):
        headers["X-Request-id"] = x_request_id

    if not isinstance(x_client_version, Unset):
        headers["X-Client-Version"] = x_client_version

    params: dict[str, Any] = {}

    params["startJobAfterCreation"] = start_job_after_creation

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/infrastructure/vb365Servers/{vb_365_server_uid}/organizations/{vb_365_organization_uid}/jobs/backup".format(
            vb_365_server_uid=quote(str(vb_365_server_uid), safe=""),
            vb_365_organization_uid=quote(str(vb_365_organization_uid), safe=""),
        ),
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | CreateVb365BackupJobResponse200 | ErrorResponse:
    if response.status_code == 200:
        response_200 = CreateVb365BackupJobResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 202:
        response_202 = cast(Any, None)
        return response_202

    response_default = ErrorResponse.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | CreateVb365BackupJobResponse200 | ErrorResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    vb_365_server_uid: UUID,
    vb_365_organization_uid: UUID,
    *,
    client: AuthenticatedClient,
    body: Vb365BackupJob,
    start_job_after_creation: bool | Unset = False,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Response[Any | CreateVb365BackupJobResponse200 | ErrorResponse]:
    """Create Veeam Backup for Microsoft 365 Backup Job

     Creates a new Veeam Backup for Microsoft 365 backup job.
    > [For Veeam Backup for Microsoft 365 servers hosted by Veeam Service Provider Console] Company
    users must pass the `null` value for the `schedulePolicy` property. Otherwise the operation will
    result in error.

    Args:
        vb_365_server_uid (UUID):
        vb_365_organization_uid (UUID):
        start_job_after_creation (bool | Unset):  Default: False.
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):
        body (Vb365BackupJob):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CreateVb365BackupJobResponse200 | ErrorResponse]
    """

    kwargs = _get_kwargs(
        vb_365_server_uid=vb_365_server_uid,
        vb_365_organization_uid=vb_365_organization_uid,
        body=body,
        start_job_after_creation=start_job_after_creation,
        x_request_id=x_request_id,
        x_client_version=x_client_version,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    vb_365_server_uid: UUID,
    vb_365_organization_uid: UUID,
    *,
    client: AuthenticatedClient,
    body: Vb365BackupJob,
    start_job_after_creation: bool | Unset = False,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Any | CreateVb365BackupJobResponse200 | ErrorResponse | None:
    """Create Veeam Backup for Microsoft 365 Backup Job

     Creates a new Veeam Backup for Microsoft 365 backup job.
    > [For Veeam Backup for Microsoft 365 servers hosted by Veeam Service Provider Console] Company
    users must pass the `null` value for the `schedulePolicy` property. Otherwise the operation will
    result in error.

    Args:
        vb_365_server_uid (UUID):
        vb_365_organization_uid (UUID):
        start_job_after_creation (bool | Unset):  Default: False.
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):
        body (Vb365BackupJob):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CreateVb365BackupJobResponse200 | ErrorResponse
    """

    return sync_detailed(
        vb_365_server_uid=vb_365_server_uid,
        vb_365_organization_uid=vb_365_organization_uid,
        client=client,
        body=body,
        start_job_after_creation=start_job_after_creation,
        x_request_id=x_request_id,
        x_client_version=x_client_version,
    ).parsed


async def asyncio_detailed(
    vb_365_server_uid: UUID,
    vb_365_organization_uid: UUID,
    *,
    client: AuthenticatedClient,
    body: Vb365BackupJob,
    start_job_after_creation: bool | Unset = False,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Response[Any | CreateVb365BackupJobResponse200 | ErrorResponse]:
    """Create Veeam Backup for Microsoft 365 Backup Job

     Creates a new Veeam Backup for Microsoft 365 backup job.
    > [For Veeam Backup for Microsoft 365 servers hosted by Veeam Service Provider Console] Company
    users must pass the `null` value for the `schedulePolicy` property. Otherwise the operation will
    result in error.

    Args:
        vb_365_server_uid (UUID):
        vb_365_organization_uid (UUID):
        start_job_after_creation (bool | Unset):  Default: False.
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):
        body (Vb365BackupJob):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CreateVb365BackupJobResponse200 | ErrorResponse]
    """

    kwargs = _get_kwargs(
        vb_365_server_uid=vb_365_server_uid,
        vb_365_organization_uid=vb_365_organization_uid,
        body=body,
        start_job_after_creation=start_job_after_creation,
        x_request_id=x_request_id,
        x_client_version=x_client_version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    vb_365_server_uid: UUID,
    vb_365_organization_uid: UUID,
    *,
    client: AuthenticatedClient,
    body: Vb365BackupJob,
    start_job_after_creation: bool | Unset = False,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Any | CreateVb365BackupJobResponse200 | ErrorResponse | None:
    """Create Veeam Backup for Microsoft 365 Backup Job

     Creates a new Veeam Backup for Microsoft 365 backup job.
    > [For Veeam Backup for Microsoft 365 servers hosted by Veeam Service Provider Console] Company
    users must pass the `null` value for the `schedulePolicy` property. Otherwise the operation will
    result in error.

    Args:
        vb_365_server_uid (UUID):
        vb_365_organization_uid (UUID):
        start_job_after_creation (bool | Unset):  Default: False.
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):
        body (Vb365BackupJob):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CreateVb365BackupJobResponse200 | ErrorResponse
    """

    return (
        await asyncio_detailed(
            vb_365_server_uid=vb_365_server_uid,
            vb_365_organization_uid=vb_365_organization_uid,
            client=client,
            body=body,
            start_job_after_creation=start_job_after_creation,
            x_request_id=x_request_id,
            x_client_version=x_client_version,
        )
    ).parsed
