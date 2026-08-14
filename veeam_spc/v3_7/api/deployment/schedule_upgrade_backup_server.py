from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.schedule_upgrade_backup_server_response_200 import ScheduleUpgradeBackupServerResponse200
from ...models.vbr_scheduled_deployment_configuration import VbrScheduledDeploymentConfiguration
from ...types import UNSET, Response, Unset


def _get_kwargs(
    backup_server_uid: UUID,
    *,
    body: VbrScheduledDeploymentConfiguration,
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

    params["select"] = select

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/infrastructure/backupServers/{backup_server_uid}/scheduledTasks/upgrade".format(
            backup_server_uid=quote(str(backup_server_uid), safe=""),
        ),
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | ErrorResponse | ScheduleUpgradeBackupServerResponse200:
    if response.status_code == 200:
        response_200 = ScheduleUpgradeBackupServerResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 202:
        response_202 = cast(Any, None)
        return response_202

    response_default = ErrorResponse.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | ErrorResponse | ScheduleUpgradeBackupServerResponse200]:
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
    body: VbrScheduledDeploymentConfiguration,
    select: str | Unset = UNSET,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Response[Any | ErrorResponse | ScheduleUpgradeBackupServerResponse200]:
    r"""Schedule Veeam Backup & Replication Update

     Creates a scheduled task that installs the latest Veeam Backup & Replication update on a server with
    the specified UID.

    Args:
        backup_server_uid (UUID):
        select (str | Unset):
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):
        body (VbrScheduledDeploymentConfiguration):  Example: {'configuration': {'distribution':
            {'filePath':
            '\\\\tech.local\\tech\\VSPC\\VBR\\13\\Butler\\VeeamBackup&Replication_13.iso', 'userName':
            'vspc\\admin', 'password': 'Password1'}, 'usePredownloadedIso': False, 'answerXml': '<?xml
            version="1.0" encoding="utf-8"?>\r\n<unattendedInstallationConfiguration bundle="VBR"
            mode="upgrade">\r\n  <properties>\r\n\r\n    <!--License agreements-->\r\n    <property
            name="ACCEPT_EULA" value="1" />\r\n    <property name="ACCEPT_LICENSING_POLICY" value="1"
            />\r\n    <property name="ACCEPT_THIRDPARTY_LICENSES" value="1" />\r\n    <property
            name="ACCEPT_REQUIRED_SOFTWARE" value="1" />\r\n\r\n    <!--License file-->\r\n
            <property name="VBR_LICENSE_AUTOUPDATE" value="1" />\r\n\r\n    <!--Service account-->\r\n
            <property name="VBR_SERVICE_PASSWORD" value="Password1" hidden="1" />\r\n\r\n    <!--
            Database configuration-->\r\n    <property name="VBR_SQLSERVER_PASSWORD" value="Password1"
            hidden="1" />\r\n\r\n    <!--Automatic update settings-->\r\n    <property
            name="VBR_AUTO_UPGRADE" value="1" />\r\n\r\n
            </properties>\r\n</unattendedInstallationConfiguration>\r\n', 'allowAutoReboot': True,
            'stopAllActivities': True, 'useManagementAgentCredentials': True, 'adminCredentials':
            {'username': 'vspc\\admin', 'password': 'Password1'}}, 'schedule': {'dateTime':
            '2025-07-24T00:23:16.3525528-05:00'}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ErrorResponse | ScheduleUpgradeBackupServerResponse200]
    """

    kwargs = _get_kwargs(
        backup_server_uid=backup_server_uid,
        body=body,
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
    body: VbrScheduledDeploymentConfiguration,
    select: str | Unset = UNSET,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Any | ErrorResponse | ScheduleUpgradeBackupServerResponse200 | None:
    r"""Schedule Veeam Backup & Replication Update

     Creates a scheduled task that installs the latest Veeam Backup & Replication update on a server with
    the specified UID.

    Args:
        backup_server_uid (UUID):
        select (str | Unset):
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):
        body (VbrScheduledDeploymentConfiguration):  Example: {'configuration': {'distribution':
            {'filePath':
            '\\\\tech.local\\tech\\VSPC\\VBR\\13\\Butler\\VeeamBackup&Replication_13.iso', 'userName':
            'vspc\\admin', 'password': 'Password1'}, 'usePredownloadedIso': False, 'answerXml': '<?xml
            version="1.0" encoding="utf-8"?>\r\n<unattendedInstallationConfiguration bundle="VBR"
            mode="upgrade">\r\n  <properties>\r\n\r\n    <!--License agreements-->\r\n    <property
            name="ACCEPT_EULA" value="1" />\r\n    <property name="ACCEPT_LICENSING_POLICY" value="1"
            />\r\n    <property name="ACCEPT_THIRDPARTY_LICENSES" value="1" />\r\n    <property
            name="ACCEPT_REQUIRED_SOFTWARE" value="1" />\r\n\r\n    <!--License file-->\r\n
            <property name="VBR_LICENSE_AUTOUPDATE" value="1" />\r\n\r\n    <!--Service account-->\r\n
            <property name="VBR_SERVICE_PASSWORD" value="Password1" hidden="1" />\r\n\r\n    <!--
            Database configuration-->\r\n    <property name="VBR_SQLSERVER_PASSWORD" value="Password1"
            hidden="1" />\r\n\r\n    <!--Automatic update settings-->\r\n    <property
            name="VBR_AUTO_UPGRADE" value="1" />\r\n\r\n
            </properties>\r\n</unattendedInstallationConfiguration>\r\n', 'allowAutoReboot': True,
            'stopAllActivities': True, 'useManagementAgentCredentials': True, 'adminCredentials':
            {'username': 'vspc\\admin', 'password': 'Password1'}}, 'schedule': {'dateTime':
            '2025-07-24T00:23:16.3525528-05:00'}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ErrorResponse | ScheduleUpgradeBackupServerResponse200
    """

    return sync_detailed(
        backup_server_uid=backup_server_uid,
        client=client,
        body=body,
        select=select,
        x_request_id=x_request_id,
        x_client_version=x_client_version,
    ).parsed


async def asyncio_detailed(
    backup_server_uid: UUID,
    *,
    client: AuthenticatedClient,
    body: VbrScheduledDeploymentConfiguration,
    select: str | Unset = UNSET,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Response[Any | ErrorResponse | ScheduleUpgradeBackupServerResponse200]:
    r"""Schedule Veeam Backup & Replication Update

     Creates a scheduled task that installs the latest Veeam Backup & Replication update on a server with
    the specified UID.

    Args:
        backup_server_uid (UUID):
        select (str | Unset):
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):
        body (VbrScheduledDeploymentConfiguration):  Example: {'configuration': {'distribution':
            {'filePath':
            '\\\\tech.local\\tech\\VSPC\\VBR\\13\\Butler\\VeeamBackup&Replication_13.iso', 'userName':
            'vspc\\admin', 'password': 'Password1'}, 'usePredownloadedIso': False, 'answerXml': '<?xml
            version="1.0" encoding="utf-8"?>\r\n<unattendedInstallationConfiguration bundle="VBR"
            mode="upgrade">\r\n  <properties>\r\n\r\n    <!--License agreements-->\r\n    <property
            name="ACCEPT_EULA" value="1" />\r\n    <property name="ACCEPT_LICENSING_POLICY" value="1"
            />\r\n    <property name="ACCEPT_THIRDPARTY_LICENSES" value="1" />\r\n    <property
            name="ACCEPT_REQUIRED_SOFTWARE" value="1" />\r\n\r\n    <!--License file-->\r\n
            <property name="VBR_LICENSE_AUTOUPDATE" value="1" />\r\n\r\n    <!--Service account-->\r\n
            <property name="VBR_SERVICE_PASSWORD" value="Password1" hidden="1" />\r\n\r\n    <!--
            Database configuration-->\r\n    <property name="VBR_SQLSERVER_PASSWORD" value="Password1"
            hidden="1" />\r\n\r\n    <!--Automatic update settings-->\r\n    <property
            name="VBR_AUTO_UPGRADE" value="1" />\r\n\r\n
            </properties>\r\n</unattendedInstallationConfiguration>\r\n', 'allowAutoReboot': True,
            'stopAllActivities': True, 'useManagementAgentCredentials': True, 'adminCredentials':
            {'username': 'vspc\\admin', 'password': 'Password1'}}, 'schedule': {'dateTime':
            '2025-07-24T00:23:16.3525528-05:00'}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ErrorResponse | ScheduleUpgradeBackupServerResponse200]
    """

    kwargs = _get_kwargs(
        backup_server_uid=backup_server_uid,
        body=body,
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
    body: VbrScheduledDeploymentConfiguration,
    select: str | Unset = UNSET,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Any | ErrorResponse | ScheduleUpgradeBackupServerResponse200 | None:
    r"""Schedule Veeam Backup & Replication Update

     Creates a scheduled task that installs the latest Veeam Backup & Replication update on a server with
    the specified UID.

    Args:
        backup_server_uid (UUID):
        select (str | Unset):
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):
        body (VbrScheduledDeploymentConfiguration):  Example: {'configuration': {'distribution':
            {'filePath':
            '\\\\tech.local\\tech\\VSPC\\VBR\\13\\Butler\\VeeamBackup&Replication_13.iso', 'userName':
            'vspc\\admin', 'password': 'Password1'}, 'usePredownloadedIso': False, 'answerXml': '<?xml
            version="1.0" encoding="utf-8"?>\r\n<unattendedInstallationConfiguration bundle="VBR"
            mode="upgrade">\r\n  <properties>\r\n\r\n    <!--License agreements-->\r\n    <property
            name="ACCEPT_EULA" value="1" />\r\n    <property name="ACCEPT_LICENSING_POLICY" value="1"
            />\r\n    <property name="ACCEPT_THIRDPARTY_LICENSES" value="1" />\r\n    <property
            name="ACCEPT_REQUIRED_SOFTWARE" value="1" />\r\n\r\n    <!--License file-->\r\n
            <property name="VBR_LICENSE_AUTOUPDATE" value="1" />\r\n\r\n    <!--Service account-->\r\n
            <property name="VBR_SERVICE_PASSWORD" value="Password1" hidden="1" />\r\n\r\n    <!--
            Database configuration-->\r\n    <property name="VBR_SQLSERVER_PASSWORD" value="Password1"
            hidden="1" />\r\n\r\n    <!--Automatic update settings-->\r\n    <property
            name="VBR_AUTO_UPGRADE" value="1" />\r\n\r\n
            </properties>\r\n</unattendedInstallationConfiguration>\r\n', 'allowAutoReboot': True,
            'stopAllActivities': True, 'useManagementAgentCredentials': True, 'adminCredentials':
            {'username': 'vspc\\admin', 'password': 'Password1'}}, 'schedule': {'dateTime':
            '2025-07-24T00:23:16.3525528-05:00'}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ErrorResponse | ScheduleUpgradeBackupServerResponse200
    """

    return (
        await asyncio_detailed(
            backup_server_uid=backup_server_uid,
            client=client,
            body=body,
            select=select,
            x_request_id=x_request_id,
            x_client_version=x_client_version,
        )
    ).parsed
