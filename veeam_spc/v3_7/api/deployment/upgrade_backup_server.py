from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.upgrade_backup_server_response_200 import UpgradeBackupServerResponse200
from ...models.vbr_deployment_configuration import VbrDeploymentConfiguration
from ...types import UNSET, Response, Unset


def _get_kwargs(
    backup_server_uid: UUID,
    *,
    body: VbrDeploymentConfiguration,
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
        "url": "/infrastructure/backupServers/{backup_server_uid}/upgrade".format(
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
) -> Any | ErrorResponse | UpgradeBackupServerResponse200:
    if response.status_code == 200:
        response_200 = UpgradeBackupServerResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 202:
        response_202 = cast(Any, None)
        return response_202

    response_default = ErrorResponse.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | ErrorResponse | UpgradeBackupServerResponse200]:
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
    body: VbrDeploymentConfiguration,
    select: str | Unset = UNSET,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Response[Any | ErrorResponse | UpgradeBackupServerResponse200]:
    r"""Update Veeam Backup & Replication on Server

     Installs the latest update of Veeam Backup & Replication on a server with the specified UID.
    > To track the installation progress, you can use the `WaitDeploymentTask` operation.

    Args:
        backup_server_uid (UUID):
        select (str | Unset):
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):
        body (VbrDeploymentConfiguration): If the `distribution` and `usePredownloadedIso`
            properties have the `null` value, the most recent version of Veeam Backup & Replication
            will be downloaded automatically. Example: {'distribution': {'filePath':
            '\\\\tech.local\\tech\\VSPC\\VBR\\13\\Butler\\VeeamBackup&Replication_13.iso', 'userName':
            'vspc1\\admin', 'password': 'Password1'}, 'usePredownloadedIso': False, 'answerXml':
            '<?xml version="1.0" encoding="utf-8"?>\r\n<unattendedInstallationConfiguration
            bundle="VBR" mode="upgrade">\r\n  <properties>\r\n\r\n    <!--License agreements-->\r\n
            <property name="ACCEPT_EULA" value="1" />\r\n    <property name="ACCEPT_LICENSING_POLICY"
            value="1" />\r\n    <property name="ACCEPT_THIRDPARTY_LICENSES" value="1" />\r\n
            <property name="ACCEPT_REQUIRED_SOFTWARE" value="1" />\r\n\r\n    <!--License file-->\r\n
            <!--property name="VBR_LICENSE_FILE" value="" /-->\r\n    <property
            name="VBR_LICENSE_AUTOUPDATE" value="1" />\r\n\r\n    <!--Service account-->\r\n    <!--
            property name="VBR_SERVICE_PASSWORD" value="" hidden="1"/-->\r\n\r\n    <!--Database
            configuration-->\r\n    <property name="VBR_SQLSERVER_PASSWORD" value="Password1"
            hidden="1"/>\r\n\r\n    <!--Automatic update settings-->\r\n    <property
            name="VBR_AUTO_UPGRADE" value="1" />\r\n\r\n
            </properties>\r\n</unattendedInstallationConfiguration>\r\n', 'allowAutoReboot': True,
            'stopAllActivities': True, 'useManagementAgentCredentials': False, 'adminCredentials':
            {'username': 'vspc1\\admin', 'password': 'Password1'}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ErrorResponse | UpgradeBackupServerResponse200]
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
    body: VbrDeploymentConfiguration,
    select: str | Unset = UNSET,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Any | ErrorResponse | UpgradeBackupServerResponse200 | None:
    r"""Update Veeam Backup & Replication on Server

     Installs the latest update of Veeam Backup & Replication on a server with the specified UID.
    > To track the installation progress, you can use the `WaitDeploymentTask` operation.

    Args:
        backup_server_uid (UUID):
        select (str | Unset):
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):
        body (VbrDeploymentConfiguration): If the `distribution` and `usePredownloadedIso`
            properties have the `null` value, the most recent version of Veeam Backup & Replication
            will be downloaded automatically. Example: {'distribution': {'filePath':
            '\\\\tech.local\\tech\\VSPC\\VBR\\13\\Butler\\VeeamBackup&Replication_13.iso', 'userName':
            'vspc1\\admin', 'password': 'Password1'}, 'usePredownloadedIso': False, 'answerXml':
            '<?xml version="1.0" encoding="utf-8"?>\r\n<unattendedInstallationConfiguration
            bundle="VBR" mode="upgrade">\r\n  <properties>\r\n\r\n    <!--License agreements-->\r\n
            <property name="ACCEPT_EULA" value="1" />\r\n    <property name="ACCEPT_LICENSING_POLICY"
            value="1" />\r\n    <property name="ACCEPT_THIRDPARTY_LICENSES" value="1" />\r\n
            <property name="ACCEPT_REQUIRED_SOFTWARE" value="1" />\r\n\r\n    <!--License file-->\r\n
            <!--property name="VBR_LICENSE_FILE" value="" /-->\r\n    <property
            name="VBR_LICENSE_AUTOUPDATE" value="1" />\r\n\r\n    <!--Service account-->\r\n    <!--
            property name="VBR_SERVICE_PASSWORD" value="" hidden="1"/-->\r\n\r\n    <!--Database
            configuration-->\r\n    <property name="VBR_SQLSERVER_PASSWORD" value="Password1"
            hidden="1"/>\r\n\r\n    <!--Automatic update settings-->\r\n    <property
            name="VBR_AUTO_UPGRADE" value="1" />\r\n\r\n
            </properties>\r\n</unattendedInstallationConfiguration>\r\n', 'allowAutoReboot': True,
            'stopAllActivities': True, 'useManagementAgentCredentials': False, 'adminCredentials':
            {'username': 'vspc1\\admin', 'password': 'Password1'}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ErrorResponse | UpgradeBackupServerResponse200
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
    body: VbrDeploymentConfiguration,
    select: str | Unset = UNSET,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Response[Any | ErrorResponse | UpgradeBackupServerResponse200]:
    r"""Update Veeam Backup & Replication on Server

     Installs the latest update of Veeam Backup & Replication on a server with the specified UID.
    > To track the installation progress, you can use the `WaitDeploymentTask` operation.

    Args:
        backup_server_uid (UUID):
        select (str | Unset):
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):
        body (VbrDeploymentConfiguration): If the `distribution` and `usePredownloadedIso`
            properties have the `null` value, the most recent version of Veeam Backup & Replication
            will be downloaded automatically. Example: {'distribution': {'filePath':
            '\\\\tech.local\\tech\\VSPC\\VBR\\13\\Butler\\VeeamBackup&Replication_13.iso', 'userName':
            'vspc1\\admin', 'password': 'Password1'}, 'usePredownloadedIso': False, 'answerXml':
            '<?xml version="1.0" encoding="utf-8"?>\r\n<unattendedInstallationConfiguration
            bundle="VBR" mode="upgrade">\r\n  <properties>\r\n\r\n    <!--License agreements-->\r\n
            <property name="ACCEPT_EULA" value="1" />\r\n    <property name="ACCEPT_LICENSING_POLICY"
            value="1" />\r\n    <property name="ACCEPT_THIRDPARTY_LICENSES" value="1" />\r\n
            <property name="ACCEPT_REQUIRED_SOFTWARE" value="1" />\r\n\r\n    <!--License file-->\r\n
            <!--property name="VBR_LICENSE_FILE" value="" /-->\r\n    <property
            name="VBR_LICENSE_AUTOUPDATE" value="1" />\r\n\r\n    <!--Service account-->\r\n    <!--
            property name="VBR_SERVICE_PASSWORD" value="" hidden="1"/-->\r\n\r\n    <!--Database
            configuration-->\r\n    <property name="VBR_SQLSERVER_PASSWORD" value="Password1"
            hidden="1"/>\r\n\r\n    <!--Automatic update settings-->\r\n    <property
            name="VBR_AUTO_UPGRADE" value="1" />\r\n\r\n
            </properties>\r\n</unattendedInstallationConfiguration>\r\n', 'allowAutoReboot': True,
            'stopAllActivities': True, 'useManagementAgentCredentials': False, 'adminCredentials':
            {'username': 'vspc1\\admin', 'password': 'Password1'}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ErrorResponse | UpgradeBackupServerResponse200]
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
    body: VbrDeploymentConfiguration,
    select: str | Unset = UNSET,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Any | ErrorResponse | UpgradeBackupServerResponse200 | None:
    r"""Update Veeam Backup & Replication on Server

     Installs the latest update of Veeam Backup & Replication on a server with the specified UID.
    > To track the installation progress, you can use the `WaitDeploymentTask` operation.

    Args:
        backup_server_uid (UUID):
        select (str | Unset):
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):
        body (VbrDeploymentConfiguration): If the `distribution` and `usePredownloadedIso`
            properties have the `null` value, the most recent version of Veeam Backup & Replication
            will be downloaded automatically. Example: {'distribution': {'filePath':
            '\\\\tech.local\\tech\\VSPC\\VBR\\13\\Butler\\VeeamBackup&Replication_13.iso', 'userName':
            'vspc1\\admin', 'password': 'Password1'}, 'usePredownloadedIso': False, 'answerXml':
            '<?xml version="1.0" encoding="utf-8"?>\r\n<unattendedInstallationConfiguration
            bundle="VBR" mode="upgrade">\r\n  <properties>\r\n\r\n    <!--License agreements-->\r\n
            <property name="ACCEPT_EULA" value="1" />\r\n    <property name="ACCEPT_LICENSING_POLICY"
            value="1" />\r\n    <property name="ACCEPT_THIRDPARTY_LICENSES" value="1" />\r\n
            <property name="ACCEPT_REQUIRED_SOFTWARE" value="1" />\r\n\r\n    <!--License file-->\r\n
            <!--property name="VBR_LICENSE_FILE" value="" /-->\r\n    <property
            name="VBR_LICENSE_AUTOUPDATE" value="1" />\r\n\r\n    <!--Service account-->\r\n    <!--
            property name="VBR_SERVICE_PASSWORD" value="" hidden="1"/-->\r\n\r\n    <!--Database
            configuration-->\r\n    <property name="VBR_SQLSERVER_PASSWORD" value="Password1"
            hidden="1"/>\r\n\r\n    <!--Automatic update settings-->\r\n    <property
            name="VBR_AUTO_UPGRADE" value="1" />\r\n\r\n
            </properties>\r\n</unattendedInstallationConfiguration>\r\n', 'allowAutoReboot': True,
            'stopAllActivities': True, 'useManagementAgentCredentials': False, 'adminCredentials':
            {'username': 'vspc1\\admin', 'password': 'Password1'}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ErrorResponse | UpgradeBackupServerResponse200
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
