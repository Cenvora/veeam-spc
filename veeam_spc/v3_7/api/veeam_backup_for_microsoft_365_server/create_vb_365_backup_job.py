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

    params["startJobAfterCreation"] = start_job_after_creation

    params["select"] = select

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
    select: str | Unset = UNSET,
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
        select (str | Unset):
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):
        body (Vb365BackupJob):  Example: {'name': 'BackupJob2', 'description': 'Veeam Backup for
            Microsoft 365 backup job', 'repositoryUid': '92421aa8-db1e-42ef-b210-b5d7750baffa',
            'isEnabled': False, 'backupType': 'SelectedItems', 'selectedItems': [{'itemType': 'User',
            'folders': [], 'backupMailbox': True, 'backupOneDrive': True, 'backupArchiveMailbox':
            True, 'backupPersonalSite': True, 'backupSites': False, 'backupTeams': False,
            'backupTeamsChats': False, 'backupMembers': False, 'backupMemberMailbox': False,
            'backupMemberArchiveMailbox': False, 'backupMemberOneDrive': False, 'backupMemberSite':
            False, 'backupGroupSite': False, 'site': None, 'team': None, 'user': {'id': 'lrs.onmicroso
            ft.com:00000000-0000-0000-0000-000000000000:00000000-0000-0000-0000-000000000000:858bae82-
            7ff7-4ab5-be78-3c2da97c9c3d:00000000-0000-0000-0000-000000000000', 'onPremisesSid': None,
            'userType': 'User', 'name': 'ktang@mycompany.onmicrosoft.com', 'displayName': 'Kate
            Tang'}, 'group': None}, {'itemType': 'Team', 'folders': [], 'backupMailbox': False,
            'backupOneDrive': False, 'backupArchiveMailbox': False, 'backupPersonalSite': False,
            'backupSites': False, 'backupTeams': False, 'backupTeamsChats': False, 'backupMembers':
            False, 'backupMemberMailbox': False, 'backupMemberArchiveMailbox': False,
            'backupMemberOneDrive': False, 'backupMemberSite': False, 'backupGroupSite': False,
            'site': None, 'team': {'id': '97033983-9122-1907-94e2-46445967791a', 'displayName':
            'Lrsvbm', 'description': 'Lrsvbm', 'mail': 'Lrsvbm@mycompany.onmicrosoft.com'}, 'user':
            None, 'group': None}, {'itemType': 'Site', 'folders': [], 'backupMailbox': False,
            'backupOneDrive': False, 'backupArchiveMailbox': False, 'backupPersonalSite': False,
            'backupSites': False, 'backupTeams': False, 'backupTeamsChats': False, 'backupMembers':
            False, 'backupMemberMailbox': False, 'backupMemberArchiveMailbox': False,
            'backupMemberOneDrive': False, 'backupMemberSite': False, 'backupGroupSite': False,
            'site': {'id': 'c518d8b0-db04-6bb8-8c39-21b18ebe71345c38aa48-1b78-4411-a0a7-15a83d0e8d50',
            'title': 'Team Site', 'url': 'https://mycompany.sharepoint.com/sites/contentTypeHub'},
            'team': None, 'user': None, 'group': None}], 'excludedItems': [], 'schedulePolicy':
            {'schedulePolicyType': 'ManualOnly', 'periodicallyEvery': None, 'dailyType': None,
            'scheduleEnabled': False, 'backupWindowEnabled': False, 'backupWindowSettings':
            {'backupWindow': [True, True, True, True, True, True, True, True, True, True, True, True,
            True, True, True, True, True, True, True, True, True, True, True, True, True, True, True,
            True, True, True, True, True, True, True, True, True, True, True, True, True, True, True,
            True, True, True, True, True, True, True, True, True, True, True, True, True, True, True,
            True, True, True, True, True, True, True, True, True, True, True, True, True, True, True,
            True, True, True, True, True, True, True, True, True, True, True, True, True, True, True,
            True, True, True, True, True, True, True, True, True, True, True, True, True, True, True,
            True, True, True, True, True, True, True, True, True, True, True, True, True, True, True,
            True, True, True, True, True, True, True, True, True, True, True, True, True, True, True,
            True, True, True, True, True, True, True, True, True, True, True, True, True, True, True,
            True, True, True, True, True, True, True, True, True, True, True, True, True, True, True,
            True, True, True, True, True, True], 'minuteOffset': None}, 'periodicallyWindowSettings':
            {'backupWindow': [True, True, True, True, True, True, True, True, True, True, True, True,
            True, True, True, True, True, True, True, True, True, True, True, True, True, True, True,
            True, True, True, True, True, True, True, True, True, True, True, True, True, True, True,
            True, True, True, True, True, True, True, True, True, True, True, True, True, True, True,
            True, True, True, True, True, True, True, True, True, True, True, True, True, True, True,
            True, True, True, True, True, True, True, True, True, True, True, True, True, True, True,
            True, True, True, True, True, True, True, True, True, True, True, True, True, True, True,
            True, True, True, True, True, True, True, True, True, True, True, True, True, True, True,
            True, True, True, True, True, True, True, True, True, True, True, True, True, True, True,
            True, True, True, True, True, True, True, True, True, True, True, True, True, True, True,
            True, True, True, True, True, True, True, True, True, True, True, True, True, True, True,
            True, True, True, True, True, True], 'minuteOffset': None}, 'periodicallyWindowEnabled':
            False, 'periodicallyOffsetMinutes': None, 'dailyTime': None, 'retryEnabled': False,
            'retryNumber': None, 'retryWaitInterval': None}}.

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
        select=select,
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
    select: str | Unset = UNSET,
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
        select (str | Unset):
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):
        body (Vb365BackupJob):  Example: {'name': 'BackupJob2', 'description': 'Veeam Backup for
            Microsoft 365 backup job', 'repositoryUid': '92421aa8-db1e-42ef-b210-b5d7750baffa',
            'isEnabled': False, 'backupType': 'SelectedItems', 'selectedItems': [{'itemType': 'User',
            'folders': [], 'backupMailbox': True, 'backupOneDrive': True, 'backupArchiveMailbox':
            True, 'backupPersonalSite': True, 'backupSites': False, 'backupTeams': False,
            'backupTeamsChats': False, 'backupMembers': False, 'backupMemberMailbox': False,
            'backupMemberArchiveMailbox': False, 'backupMemberOneDrive': False, 'backupMemberSite':
            False, 'backupGroupSite': False, 'site': None, 'team': None, 'user': {'id': 'lrs.onmicroso
            ft.com:00000000-0000-0000-0000-000000000000:00000000-0000-0000-0000-000000000000:858bae82-
            7ff7-4ab5-be78-3c2da97c9c3d:00000000-0000-0000-0000-000000000000', 'onPremisesSid': None,
            'userType': 'User', 'name': 'ktang@mycompany.onmicrosoft.com', 'displayName': 'Kate
            Tang'}, 'group': None}, {'itemType': 'Team', 'folders': [], 'backupMailbox': False,
            'backupOneDrive': False, 'backupArchiveMailbox': False, 'backupPersonalSite': False,
            'backupSites': False, 'backupTeams': False, 'backupTeamsChats': False, 'backupMembers':
            False, 'backupMemberMailbox': False, 'backupMemberArchiveMailbox': False,
            'backupMemberOneDrive': False, 'backupMemberSite': False, 'backupGroupSite': False,
            'site': None, 'team': {'id': '97033983-9122-1907-94e2-46445967791a', 'displayName':
            'Lrsvbm', 'description': 'Lrsvbm', 'mail': 'Lrsvbm@mycompany.onmicrosoft.com'}, 'user':
            None, 'group': None}, {'itemType': 'Site', 'folders': [], 'backupMailbox': False,
            'backupOneDrive': False, 'backupArchiveMailbox': False, 'backupPersonalSite': False,
            'backupSites': False, 'backupTeams': False, 'backupTeamsChats': False, 'backupMembers':
            False, 'backupMemberMailbox': False, 'backupMemberArchiveMailbox': False,
            'backupMemberOneDrive': False, 'backupMemberSite': False, 'backupGroupSite': False,
            'site': {'id': 'c518d8b0-db04-6bb8-8c39-21b18ebe71345c38aa48-1b78-4411-a0a7-15a83d0e8d50',
            'title': 'Team Site', 'url': 'https://mycompany.sharepoint.com/sites/contentTypeHub'},
            'team': None, 'user': None, 'group': None}], 'excludedItems': [], 'schedulePolicy':
            {'schedulePolicyType': 'ManualOnly', 'periodicallyEvery': None, 'dailyType': None,
            'scheduleEnabled': False, 'backupWindowEnabled': False, 'backupWindowSettings':
            {'backupWindow': [True, True, True, True, True, True, True, True, True, True, True, True,
            True, True, True, True, True, True, True, True, True, True, True, True, True, True, True,
            True, True, True, True, True, True, True, True, True, True, True, True, True, True, True,
            True, True, True, True, True, True, True, True, True, True, True, True, True, True, True,
            True, True, True, True, True, True, True, True, True, True, True, True, True, True, True,
            True, True, True, True, True, True, True, True, True, True, True, True, True, True, True,
            True, True, True, True, True, True, True, True, True, True, True, True, True, True, True,
            True, True, True, True, True, True, True, True, True, True, True, True, True, True, True,
            True, True, True, True, True, True, True, True, True, True, True, True, True, True, True,
            True, True, True, True, True, True, True, True, True, True, True, True, True, True, True,
            True, True, True, True, True, True, True, True, True, True, True, True, True, True, True,
            True, True, True, True, True, True], 'minuteOffset': None}, 'periodicallyWindowSettings':
            {'backupWindow': [True, True, True, True, True, True, True, True, True, True, True, True,
            True, True, True, True, True, True, True, True, True, True, True, True, True, True, True,
            True, True, True, True, True, True, True, True, True, True, True, True, True, True, True,
            True, True, True, True, True, True, True, True, True, True, True, True, True, True, True,
            True, True, True, True, True, True, True, True, True, True, True, True, True, True, True,
            True, True, True, True, True, True, True, True, True, True, True, True, True, True, True,
            True, True, True, True, True, True, True, True, True, True, True, True, True, True, True,
            True, True, True, True, True, True, True, True, True, True, True, True, True, True, True,
            True, True, True, True, True, True, True, True, True, True, True, True, True, True, True,
            True, True, True, True, True, True, True, True, True, True, True, True, True, True, True,
            True, True, True, True, True, True, True, True, True, True, True, True, True, True, True,
            True, True, True, True, True, True], 'minuteOffset': None}, 'periodicallyWindowEnabled':
            False, 'periodicallyOffsetMinutes': None, 'dailyTime': None, 'retryEnabled': False,
            'retryNumber': None, 'retryWaitInterval': None}}.

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
        select=select,
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
    select: str | Unset = UNSET,
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
        select (str | Unset):
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):
        body (Vb365BackupJob):  Example: {'name': 'BackupJob2', 'description': 'Veeam Backup for
            Microsoft 365 backup job', 'repositoryUid': '92421aa8-db1e-42ef-b210-b5d7750baffa',
            'isEnabled': False, 'backupType': 'SelectedItems', 'selectedItems': [{'itemType': 'User',
            'folders': [], 'backupMailbox': True, 'backupOneDrive': True, 'backupArchiveMailbox':
            True, 'backupPersonalSite': True, 'backupSites': False, 'backupTeams': False,
            'backupTeamsChats': False, 'backupMembers': False, 'backupMemberMailbox': False,
            'backupMemberArchiveMailbox': False, 'backupMemberOneDrive': False, 'backupMemberSite':
            False, 'backupGroupSite': False, 'site': None, 'team': None, 'user': {'id': 'lrs.onmicroso
            ft.com:00000000-0000-0000-0000-000000000000:00000000-0000-0000-0000-000000000000:858bae82-
            7ff7-4ab5-be78-3c2da97c9c3d:00000000-0000-0000-0000-000000000000', 'onPremisesSid': None,
            'userType': 'User', 'name': 'ktang@mycompany.onmicrosoft.com', 'displayName': 'Kate
            Tang'}, 'group': None}, {'itemType': 'Team', 'folders': [], 'backupMailbox': False,
            'backupOneDrive': False, 'backupArchiveMailbox': False, 'backupPersonalSite': False,
            'backupSites': False, 'backupTeams': False, 'backupTeamsChats': False, 'backupMembers':
            False, 'backupMemberMailbox': False, 'backupMemberArchiveMailbox': False,
            'backupMemberOneDrive': False, 'backupMemberSite': False, 'backupGroupSite': False,
            'site': None, 'team': {'id': '97033983-9122-1907-94e2-46445967791a', 'displayName':
            'Lrsvbm', 'description': 'Lrsvbm', 'mail': 'Lrsvbm@mycompany.onmicrosoft.com'}, 'user':
            None, 'group': None}, {'itemType': 'Site', 'folders': [], 'backupMailbox': False,
            'backupOneDrive': False, 'backupArchiveMailbox': False, 'backupPersonalSite': False,
            'backupSites': False, 'backupTeams': False, 'backupTeamsChats': False, 'backupMembers':
            False, 'backupMemberMailbox': False, 'backupMemberArchiveMailbox': False,
            'backupMemberOneDrive': False, 'backupMemberSite': False, 'backupGroupSite': False,
            'site': {'id': 'c518d8b0-db04-6bb8-8c39-21b18ebe71345c38aa48-1b78-4411-a0a7-15a83d0e8d50',
            'title': 'Team Site', 'url': 'https://mycompany.sharepoint.com/sites/contentTypeHub'},
            'team': None, 'user': None, 'group': None}], 'excludedItems': [], 'schedulePolicy':
            {'schedulePolicyType': 'ManualOnly', 'periodicallyEvery': None, 'dailyType': None,
            'scheduleEnabled': False, 'backupWindowEnabled': False, 'backupWindowSettings':
            {'backupWindow': [True, True, True, True, True, True, True, True, True, True, True, True,
            True, True, True, True, True, True, True, True, True, True, True, True, True, True, True,
            True, True, True, True, True, True, True, True, True, True, True, True, True, True, True,
            True, True, True, True, True, True, True, True, True, True, True, True, True, True, True,
            True, True, True, True, True, True, True, True, True, True, True, True, True, True, True,
            True, True, True, True, True, True, True, True, True, True, True, True, True, True, True,
            True, True, True, True, True, True, True, True, True, True, True, True, True, True, True,
            True, True, True, True, True, True, True, True, True, True, True, True, True, True, True,
            True, True, True, True, True, True, True, True, True, True, True, True, True, True, True,
            True, True, True, True, True, True, True, True, True, True, True, True, True, True, True,
            True, True, True, True, True, True, True, True, True, True, True, True, True, True, True,
            True, True, True, True, True, True], 'minuteOffset': None}, 'periodicallyWindowSettings':
            {'backupWindow': [True, True, True, True, True, True, True, True, True, True, True, True,
            True, True, True, True, True, True, True, True, True, True, True, True, True, True, True,
            True, True, True, True, True, True, True, True, True, True, True, True, True, True, True,
            True, True, True, True, True, True, True, True, True, True, True, True, True, True, True,
            True, True, True, True, True, True, True, True, True, True, True, True, True, True, True,
            True, True, True, True, True, True, True, True, True, True, True, True, True, True, True,
            True, True, True, True, True, True, True, True, True, True, True, True, True, True, True,
            True, True, True, True, True, True, True, True, True, True, True, True, True, True, True,
            True, True, True, True, True, True, True, True, True, True, True, True, True, True, True,
            True, True, True, True, True, True, True, True, True, True, True, True, True, True, True,
            True, True, True, True, True, True, True, True, True, True, True, True, True, True, True,
            True, True, True, True, True, True], 'minuteOffset': None}, 'periodicallyWindowEnabled':
            False, 'periodicallyOffsetMinutes': None, 'dailyTime': None, 'retryEnabled': False,
            'retryNumber': None, 'retryWaitInterval': None}}.

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
        select=select,
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
    select: str | Unset = UNSET,
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
        select (str | Unset):
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):
        body (Vb365BackupJob):  Example: {'name': 'BackupJob2', 'description': 'Veeam Backup for
            Microsoft 365 backup job', 'repositoryUid': '92421aa8-db1e-42ef-b210-b5d7750baffa',
            'isEnabled': False, 'backupType': 'SelectedItems', 'selectedItems': [{'itemType': 'User',
            'folders': [], 'backupMailbox': True, 'backupOneDrive': True, 'backupArchiveMailbox':
            True, 'backupPersonalSite': True, 'backupSites': False, 'backupTeams': False,
            'backupTeamsChats': False, 'backupMembers': False, 'backupMemberMailbox': False,
            'backupMemberArchiveMailbox': False, 'backupMemberOneDrive': False, 'backupMemberSite':
            False, 'backupGroupSite': False, 'site': None, 'team': None, 'user': {'id': 'lrs.onmicroso
            ft.com:00000000-0000-0000-0000-000000000000:00000000-0000-0000-0000-000000000000:858bae82-
            7ff7-4ab5-be78-3c2da97c9c3d:00000000-0000-0000-0000-000000000000', 'onPremisesSid': None,
            'userType': 'User', 'name': 'ktang@mycompany.onmicrosoft.com', 'displayName': 'Kate
            Tang'}, 'group': None}, {'itemType': 'Team', 'folders': [], 'backupMailbox': False,
            'backupOneDrive': False, 'backupArchiveMailbox': False, 'backupPersonalSite': False,
            'backupSites': False, 'backupTeams': False, 'backupTeamsChats': False, 'backupMembers':
            False, 'backupMemberMailbox': False, 'backupMemberArchiveMailbox': False,
            'backupMemberOneDrive': False, 'backupMemberSite': False, 'backupGroupSite': False,
            'site': None, 'team': {'id': '97033983-9122-1907-94e2-46445967791a', 'displayName':
            'Lrsvbm', 'description': 'Lrsvbm', 'mail': 'Lrsvbm@mycompany.onmicrosoft.com'}, 'user':
            None, 'group': None}, {'itemType': 'Site', 'folders': [], 'backupMailbox': False,
            'backupOneDrive': False, 'backupArchiveMailbox': False, 'backupPersonalSite': False,
            'backupSites': False, 'backupTeams': False, 'backupTeamsChats': False, 'backupMembers':
            False, 'backupMemberMailbox': False, 'backupMemberArchiveMailbox': False,
            'backupMemberOneDrive': False, 'backupMemberSite': False, 'backupGroupSite': False,
            'site': {'id': 'c518d8b0-db04-6bb8-8c39-21b18ebe71345c38aa48-1b78-4411-a0a7-15a83d0e8d50',
            'title': 'Team Site', 'url': 'https://mycompany.sharepoint.com/sites/contentTypeHub'},
            'team': None, 'user': None, 'group': None}], 'excludedItems': [], 'schedulePolicy':
            {'schedulePolicyType': 'ManualOnly', 'periodicallyEvery': None, 'dailyType': None,
            'scheduleEnabled': False, 'backupWindowEnabled': False, 'backupWindowSettings':
            {'backupWindow': [True, True, True, True, True, True, True, True, True, True, True, True,
            True, True, True, True, True, True, True, True, True, True, True, True, True, True, True,
            True, True, True, True, True, True, True, True, True, True, True, True, True, True, True,
            True, True, True, True, True, True, True, True, True, True, True, True, True, True, True,
            True, True, True, True, True, True, True, True, True, True, True, True, True, True, True,
            True, True, True, True, True, True, True, True, True, True, True, True, True, True, True,
            True, True, True, True, True, True, True, True, True, True, True, True, True, True, True,
            True, True, True, True, True, True, True, True, True, True, True, True, True, True, True,
            True, True, True, True, True, True, True, True, True, True, True, True, True, True, True,
            True, True, True, True, True, True, True, True, True, True, True, True, True, True, True,
            True, True, True, True, True, True, True, True, True, True, True, True, True, True, True,
            True, True, True, True, True, True], 'minuteOffset': None}, 'periodicallyWindowSettings':
            {'backupWindow': [True, True, True, True, True, True, True, True, True, True, True, True,
            True, True, True, True, True, True, True, True, True, True, True, True, True, True, True,
            True, True, True, True, True, True, True, True, True, True, True, True, True, True, True,
            True, True, True, True, True, True, True, True, True, True, True, True, True, True, True,
            True, True, True, True, True, True, True, True, True, True, True, True, True, True, True,
            True, True, True, True, True, True, True, True, True, True, True, True, True, True, True,
            True, True, True, True, True, True, True, True, True, True, True, True, True, True, True,
            True, True, True, True, True, True, True, True, True, True, True, True, True, True, True,
            True, True, True, True, True, True, True, True, True, True, True, True, True, True, True,
            True, True, True, True, True, True, True, True, True, True, True, True, True, True, True,
            True, True, True, True, True, True, True, True, True, True, True, True, True, True, True,
            True, True, True, True, True, True], 'minuteOffset': None}, 'periodicallyWindowEnabled':
            False, 'periodicallyOffsetMinutes': None, 'dailyTime': None, 'retryEnabled': False,
            'retryNumber': None, 'retryWaitInterval': None}}.

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
            select=select,
            x_request_id=x_request_id,
            x_client_version=x_client_version,
        )
    ).parsed
