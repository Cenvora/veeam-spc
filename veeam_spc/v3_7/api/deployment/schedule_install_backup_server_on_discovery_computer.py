from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.schedule_install_backup_server_on_discovery_computer_response_200 import (
    ScheduleInstallBackupServerOnDiscoveryComputerResponse200,
)
from ...models.vbr_scheduled_deployment_configuration_with_credentials import (
    VbrScheduledDeploymentConfigurationWithCredentials,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    computer_uid: UUID,
    *,
    body: VbrScheduledDeploymentConfigurationWithCredentials,
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
        "url": "/discovery/computers/{computer_uid}/scheduledTasks/installBackupServer".format(
            computer_uid=quote(str(computer_uid), safe=""),
        ),
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | ErrorResponse | ScheduleInstallBackupServerOnDiscoveryComputerResponse200:
    if response.status_code == 200:
        response_200 = ScheduleInstallBackupServerOnDiscoveryComputerResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 202:
        response_202 = cast(Any, None)
        return response_202

    response_default = ErrorResponse.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | ErrorResponse | ScheduleInstallBackupServerOnDiscoveryComputerResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    computer_uid: UUID,
    *,
    client: AuthenticatedClient,
    body: VbrScheduledDeploymentConfigurationWithCredentials,
    select: str | Unset = UNSET,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Response[Any | ErrorResponse | ScheduleInstallBackupServerOnDiscoveryComputerResponse200]:
    r"""Schedule Veeam Backup & Replication Installation on Discovered Computer

     Creates a sheduled task that installs Veeam Backup & Replication and management agent on a
    discovered computer with the specified UID.
    > Deploys only the missing component if the other one is already installed.

    Args:
        computer_uid (UUID):
        select (str | Unset):
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):
        body (VbrScheduledDeploymentConfigurationWithCredentials):  Example: {'configuration':
            {'configuration': {'distribution': {'filePath':
            '\\\\tech.local\\tech\\VSPC\\VBR\\13\\Butler\\VeeamBackup&Replication_13.iso', 'userName':
            'tech\\svc-datam', 'password': 'n_59=r2wc%k8Rx.X'}, 'usePredownloadedIso': False,
            'answerXml': '<?xml version="1.0"
            encoding="utf-8"?>\r\n<unattendedInstallationConfiguration bundle="VBR"
            mode="install">\r\n  <properties>\r\n\r\n    <!--License agreements-->\r\n    <property
            name="ACCEPT_EULA" value="1" />\r\n    <property name="ACCEPT_LICENSING_POLICY" value="1"
            />\r\n    <property name="ACCEPT_THIRDPARTY_LICENSES" value="1" />\r\n    <property
            name="ACCEPT_REQUIRED_SOFTWARE" value="1" />\r\n\r\n    <!--License file-->\r\n
            <property name="VBR_LICENSE_FILE" value="" />\r\n    <property
            name="VBR_LICENSE_AUTOUPDATE" value="1" />\r\n\r\n    <!--Service account-->\r\n
            <property name="VBR_SERVICE_USER" value="vspc1\\administrator" />\r\n    <property
            name="VBR_SERVICE_PASSWORD" value="Password1" hidden="1" />\r\n\r\n    <!--Database
            configuration-->\r\n    <property name="VBR_SQLSERVER_INSTALL" value="0" />\r\n
            <property name="VBR_SQLSERVER_ENGINE" value="1" />\r\n    <property
            name="VBR_SQLSERVER_SERVER" value="localhost" />\r\n    <property
            name="VBR_SQLSERVER_DATABASE" value="VeeamBackup" />\r\n    <property
            name="VBR_SQLSERVER_AUTHENTICATION" value="1" />\r\n    <property
            name="VBR_SQLSERVER_USERNAME" value="postgres" />\r\n    <property
            name="VBR_SQLSERVER_PASSWORD" value="Password1" hidden="1"/>\r\n\r\n    <!--Ports
            configuration-->\r\n    <property name="VBRC_SERVICE_PORT" value="9393" />\r\n
            <property name="VBR_SERVICE_PORT" value="9392" />\r\n    <property
            name="VBR_SECURE_CONNECTIONS_PORT" value="9401" />\r\n    <property
            name="VBR_RESTSERVICE_PORT" value="9419" />\r\n\r\n    <!--Data locations-->\r\n
            <property name="INSTALLDIR" value="C:\\Program Files\\Veeam\\Backup and Replication"
            />\r\n    <property name="VM_CATALOGPATH" value="C:\\VBRCatalog" />\r\n    <property
            name="VBR_IRCACHE" value="C:\\ProgramData\\Veeam\\Backup\\IRCache" />\r\n\r\n    <!--
            Automatic update settings-->\r\n    <property name="VBR_CHECK_UPDATES" value="1"
            />\r\n\r\n    <!--Plug-ins for Veeam Backup & Replication-->\r\n    <property
            name="AHV_INSTALL" value="0" />\r\n    <property name="RHV_INSTALL" value="0" />\r\n
            <property name="AWS_INSTALL" value="0" />\r\n    <property name="AZURE_INSTALL" value="0"
            />\r\n    <property name="GCP_INSTALL" value="0" />\r\n    <property name="KASTEN_INSTALL"
            value="0" />\r\n\r\n  </properties>\r\n</unattendedInstallationConfiguration>',
            'allowAutoReboot': True, 'stopAllActivities': False, 'useManagementAgentCredentials':
            False, 'adminCredentials': {'username': 'vspc1\\administrator', 'password': 'Password1'}},
            'licenseSettings': {'licenseFileContent': 'BADANBgkqhkiG9w0BAQEFAASCAmEwggJdAgEAAoGBAIPK6b
            ojg0Tj/GcvQvg5iTFpmGbAdAFXRmOE4L5gDiYdTIPSMMJnGDITqF33lTX6nkVA5EQQy14xHziMvONEmHkIsNwudIth
            ody3H07aiKp+fakIwlCAsFCC3TnSHBuc1+Xp0r8L9ILi9UNWmss/XdsXiaPZd03daAR2JLUzXp3zAgMBAAECgYB6se
            z4utkZyLqSAaDyYPZFh0430tHs8ah5PBrTga+KclpqmsOEKOCQtlZX7Qf/seupA6m/aHc8oLS1O+kaGCFtpwsFSnin
            /7f8vXXlDpFSZYfWO+1u7W0ub50E9zmSH/Uup4QFPQm20Vf45Frq1KTpJfkywMKf5jbNwaEcEmFvYQJBAONHojOa1s
            AijDMUqdq4sZdIhvnz9EdCalzNGO3GCWV0ptwLGh7V4zP0heQnl1aaz/Tt9QJ7RlOUZomNIc/0siMCQQCUclNptWWp
            72iG0QmwVEmvn9vs8nlunGbmBBeo++a/46T51qU2GQxRSSi1M8T8aXrxHwA8HFjd5T1PK17tBJnxAkEAtYfMlP0yU2
            oEovP5KppkNhoWvOPOE3CHtbGXHKsVbDR85bn0VfauLxw6KN46cVDbkpzRGfdOV4lrUKgp/ohKEwJAN62N1bdA83Ul
            anObQ7TJkoLOFVh47WDiQ2HDkhExYkW7Ci5U9y577T0YdKZ/OwFBKJEtIF6tgkTKMxicWSABsQJBANKIj6wkNfnxn5
            EwniB1959xNS0PrpeaLVedEhW2HJKrBBzQKpfv0A3aGl1CwTAfld0lNiFJ7jMo1J6rlDHXw9QwggJeAgEAAoGBAJ5g
            hbXlirsjv5Fdn7BFruUfE1w48BPp0M3jUIQXsN3bB4nj5a5soCQjKVN80p9N5j+ns53Opd/7Zm6nBFhwJ+ahG2DkMv
            vN6ceS4gUQIJfQqcWJmJV8876I+MAr6WpA4yG2kBOntXw4kmB0dbNLsG5KRp96/Y30haSaJhicd27tAgMBAAECgYEA
            hOTZTdheoMlOZdv5sx/FsdxxkmD0ksEPxLOJTE3Uy1SO7tWcVNAxUCFw++0xjxr+qUs/HJvZ9Cgvu4nJy6vQzhNPwA
            09Yjw7IDVE73/wKydmdbI9sW4vSxpAHzP3khahqMCeAMjfoY1Ji/G0tiFtgUGY4cqhoM3eMGVyTfUroMECQQDLwmxU
            7vncEirPyRUj7S21ns9EIeKrgHChMk+wwdX3XBABCji5IKPNMheMCuOjzxFMLZxZQSNWBuRg57I9fdn7AkEAxvt2eR
            TcqHz7gNuKYP4bam9ODAVkVOkYFXSv2PjsohI1FALVBAffu7E0mJFbbs8aL1vO5wbr2bbYVuApjr+uNwJBAMgI6Dd9
            oPgnMbZpz4JEr3I1JX/a0F/UKT5nWQrLUNaVn/SVZ1h/ra+d9LX8Xr0LZQznXi3Vn+4tt/lWnYp2yg8CQHMTzyqrhA
            n1bkbRsS/zBcwCXzLYk3P/8qvF9kUXgVMiEIxoLuXL3/reuzpZJnXpVI17HSfDevdIpclojuA9vvUCQQCcxDFk/oAF
            nwIND7Xy5Jy0fzCCzvWW05mVCzYAnj2rKIw6y+q55jE6hExG1Z8Pfn36MS/cw1GmNlvKeq9hG+8b=',
            'licenseUid': None, 'licenseSource': 'LicenseFileContent'}, 'credentials': {'tenantName':
            'alphaadmin', 'tenantPassword': 'Password1'}}, 'schedule': {'dateTime':
            '2025-07-23T19:55:26.3617936-05:00'}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ErrorResponse | ScheduleInstallBackupServerOnDiscoveryComputerResponse200]
    """

    kwargs = _get_kwargs(
        computer_uid=computer_uid,
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
    computer_uid: UUID,
    *,
    client: AuthenticatedClient,
    body: VbrScheduledDeploymentConfigurationWithCredentials,
    select: str | Unset = UNSET,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Any | ErrorResponse | ScheduleInstallBackupServerOnDiscoveryComputerResponse200 | None:
    r"""Schedule Veeam Backup & Replication Installation on Discovered Computer

     Creates a sheduled task that installs Veeam Backup & Replication and management agent on a
    discovered computer with the specified UID.
    > Deploys only the missing component if the other one is already installed.

    Args:
        computer_uid (UUID):
        select (str | Unset):
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):
        body (VbrScheduledDeploymentConfigurationWithCredentials):  Example: {'configuration':
            {'configuration': {'distribution': {'filePath':
            '\\\\tech.local\\tech\\VSPC\\VBR\\13\\Butler\\VeeamBackup&Replication_13.iso', 'userName':
            'tech\\svc-datam', 'password': 'n_59=r2wc%k8Rx.X'}, 'usePredownloadedIso': False,
            'answerXml': '<?xml version="1.0"
            encoding="utf-8"?>\r\n<unattendedInstallationConfiguration bundle="VBR"
            mode="install">\r\n  <properties>\r\n\r\n    <!--License agreements-->\r\n    <property
            name="ACCEPT_EULA" value="1" />\r\n    <property name="ACCEPT_LICENSING_POLICY" value="1"
            />\r\n    <property name="ACCEPT_THIRDPARTY_LICENSES" value="1" />\r\n    <property
            name="ACCEPT_REQUIRED_SOFTWARE" value="1" />\r\n\r\n    <!--License file-->\r\n
            <property name="VBR_LICENSE_FILE" value="" />\r\n    <property
            name="VBR_LICENSE_AUTOUPDATE" value="1" />\r\n\r\n    <!--Service account-->\r\n
            <property name="VBR_SERVICE_USER" value="vspc1\\administrator" />\r\n    <property
            name="VBR_SERVICE_PASSWORD" value="Password1" hidden="1" />\r\n\r\n    <!--Database
            configuration-->\r\n    <property name="VBR_SQLSERVER_INSTALL" value="0" />\r\n
            <property name="VBR_SQLSERVER_ENGINE" value="1" />\r\n    <property
            name="VBR_SQLSERVER_SERVER" value="localhost" />\r\n    <property
            name="VBR_SQLSERVER_DATABASE" value="VeeamBackup" />\r\n    <property
            name="VBR_SQLSERVER_AUTHENTICATION" value="1" />\r\n    <property
            name="VBR_SQLSERVER_USERNAME" value="postgres" />\r\n    <property
            name="VBR_SQLSERVER_PASSWORD" value="Password1" hidden="1"/>\r\n\r\n    <!--Ports
            configuration-->\r\n    <property name="VBRC_SERVICE_PORT" value="9393" />\r\n
            <property name="VBR_SERVICE_PORT" value="9392" />\r\n    <property
            name="VBR_SECURE_CONNECTIONS_PORT" value="9401" />\r\n    <property
            name="VBR_RESTSERVICE_PORT" value="9419" />\r\n\r\n    <!--Data locations-->\r\n
            <property name="INSTALLDIR" value="C:\\Program Files\\Veeam\\Backup and Replication"
            />\r\n    <property name="VM_CATALOGPATH" value="C:\\VBRCatalog" />\r\n    <property
            name="VBR_IRCACHE" value="C:\\ProgramData\\Veeam\\Backup\\IRCache" />\r\n\r\n    <!--
            Automatic update settings-->\r\n    <property name="VBR_CHECK_UPDATES" value="1"
            />\r\n\r\n    <!--Plug-ins for Veeam Backup & Replication-->\r\n    <property
            name="AHV_INSTALL" value="0" />\r\n    <property name="RHV_INSTALL" value="0" />\r\n
            <property name="AWS_INSTALL" value="0" />\r\n    <property name="AZURE_INSTALL" value="0"
            />\r\n    <property name="GCP_INSTALL" value="0" />\r\n    <property name="KASTEN_INSTALL"
            value="0" />\r\n\r\n  </properties>\r\n</unattendedInstallationConfiguration>',
            'allowAutoReboot': True, 'stopAllActivities': False, 'useManagementAgentCredentials':
            False, 'adminCredentials': {'username': 'vspc1\\administrator', 'password': 'Password1'}},
            'licenseSettings': {'licenseFileContent': 'BADANBgkqhkiG9w0BAQEFAASCAmEwggJdAgEAAoGBAIPK6b
            ojg0Tj/GcvQvg5iTFpmGbAdAFXRmOE4L5gDiYdTIPSMMJnGDITqF33lTX6nkVA5EQQy14xHziMvONEmHkIsNwudIth
            ody3H07aiKp+fakIwlCAsFCC3TnSHBuc1+Xp0r8L9ILi9UNWmss/XdsXiaPZd03daAR2JLUzXp3zAgMBAAECgYB6se
            z4utkZyLqSAaDyYPZFh0430tHs8ah5PBrTga+KclpqmsOEKOCQtlZX7Qf/seupA6m/aHc8oLS1O+kaGCFtpwsFSnin
            /7f8vXXlDpFSZYfWO+1u7W0ub50E9zmSH/Uup4QFPQm20Vf45Frq1KTpJfkywMKf5jbNwaEcEmFvYQJBAONHojOa1s
            AijDMUqdq4sZdIhvnz9EdCalzNGO3GCWV0ptwLGh7V4zP0heQnl1aaz/Tt9QJ7RlOUZomNIc/0siMCQQCUclNptWWp
            72iG0QmwVEmvn9vs8nlunGbmBBeo++a/46T51qU2GQxRSSi1M8T8aXrxHwA8HFjd5T1PK17tBJnxAkEAtYfMlP0yU2
            oEovP5KppkNhoWvOPOE3CHtbGXHKsVbDR85bn0VfauLxw6KN46cVDbkpzRGfdOV4lrUKgp/ohKEwJAN62N1bdA83Ul
            anObQ7TJkoLOFVh47WDiQ2HDkhExYkW7Ci5U9y577T0YdKZ/OwFBKJEtIF6tgkTKMxicWSABsQJBANKIj6wkNfnxn5
            EwniB1959xNS0PrpeaLVedEhW2HJKrBBzQKpfv0A3aGl1CwTAfld0lNiFJ7jMo1J6rlDHXw9QwggJeAgEAAoGBAJ5g
            hbXlirsjv5Fdn7BFruUfE1w48BPp0M3jUIQXsN3bB4nj5a5soCQjKVN80p9N5j+ns53Opd/7Zm6nBFhwJ+ahG2DkMv
            vN6ceS4gUQIJfQqcWJmJV8876I+MAr6WpA4yG2kBOntXw4kmB0dbNLsG5KRp96/Y30haSaJhicd27tAgMBAAECgYEA
            hOTZTdheoMlOZdv5sx/FsdxxkmD0ksEPxLOJTE3Uy1SO7tWcVNAxUCFw++0xjxr+qUs/HJvZ9Cgvu4nJy6vQzhNPwA
            09Yjw7IDVE73/wKydmdbI9sW4vSxpAHzP3khahqMCeAMjfoY1Ji/G0tiFtgUGY4cqhoM3eMGVyTfUroMECQQDLwmxU
            7vncEirPyRUj7S21ns9EIeKrgHChMk+wwdX3XBABCji5IKPNMheMCuOjzxFMLZxZQSNWBuRg57I9fdn7AkEAxvt2eR
            TcqHz7gNuKYP4bam9ODAVkVOkYFXSv2PjsohI1FALVBAffu7E0mJFbbs8aL1vO5wbr2bbYVuApjr+uNwJBAMgI6Dd9
            oPgnMbZpz4JEr3I1JX/a0F/UKT5nWQrLUNaVn/SVZ1h/ra+d9LX8Xr0LZQznXi3Vn+4tt/lWnYp2yg8CQHMTzyqrhA
            n1bkbRsS/zBcwCXzLYk3P/8qvF9kUXgVMiEIxoLuXL3/reuzpZJnXpVI17HSfDevdIpclojuA9vvUCQQCcxDFk/oAF
            nwIND7Xy5Jy0fzCCzvWW05mVCzYAnj2rKIw6y+q55jE6hExG1Z8Pfn36MS/cw1GmNlvKeq9hG+8b=',
            'licenseUid': None, 'licenseSource': 'LicenseFileContent'}, 'credentials': {'tenantName':
            'alphaadmin', 'tenantPassword': 'Password1'}}, 'schedule': {'dateTime':
            '2025-07-23T19:55:26.3617936-05:00'}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ErrorResponse | ScheduleInstallBackupServerOnDiscoveryComputerResponse200
    """

    return sync_detailed(
        computer_uid=computer_uid,
        client=client,
        body=body,
        select=select,
        x_request_id=x_request_id,
        x_client_version=x_client_version,
    ).parsed


async def asyncio_detailed(
    computer_uid: UUID,
    *,
    client: AuthenticatedClient,
    body: VbrScheduledDeploymentConfigurationWithCredentials,
    select: str | Unset = UNSET,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Response[Any | ErrorResponse | ScheduleInstallBackupServerOnDiscoveryComputerResponse200]:
    r"""Schedule Veeam Backup & Replication Installation on Discovered Computer

     Creates a sheduled task that installs Veeam Backup & Replication and management agent on a
    discovered computer with the specified UID.
    > Deploys only the missing component if the other one is already installed.

    Args:
        computer_uid (UUID):
        select (str | Unset):
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):
        body (VbrScheduledDeploymentConfigurationWithCredentials):  Example: {'configuration':
            {'configuration': {'distribution': {'filePath':
            '\\\\tech.local\\tech\\VSPC\\VBR\\13\\Butler\\VeeamBackup&Replication_13.iso', 'userName':
            'tech\\svc-datam', 'password': 'n_59=r2wc%k8Rx.X'}, 'usePredownloadedIso': False,
            'answerXml': '<?xml version="1.0"
            encoding="utf-8"?>\r\n<unattendedInstallationConfiguration bundle="VBR"
            mode="install">\r\n  <properties>\r\n\r\n    <!--License agreements-->\r\n    <property
            name="ACCEPT_EULA" value="1" />\r\n    <property name="ACCEPT_LICENSING_POLICY" value="1"
            />\r\n    <property name="ACCEPT_THIRDPARTY_LICENSES" value="1" />\r\n    <property
            name="ACCEPT_REQUIRED_SOFTWARE" value="1" />\r\n\r\n    <!--License file-->\r\n
            <property name="VBR_LICENSE_FILE" value="" />\r\n    <property
            name="VBR_LICENSE_AUTOUPDATE" value="1" />\r\n\r\n    <!--Service account-->\r\n
            <property name="VBR_SERVICE_USER" value="vspc1\\administrator" />\r\n    <property
            name="VBR_SERVICE_PASSWORD" value="Password1" hidden="1" />\r\n\r\n    <!--Database
            configuration-->\r\n    <property name="VBR_SQLSERVER_INSTALL" value="0" />\r\n
            <property name="VBR_SQLSERVER_ENGINE" value="1" />\r\n    <property
            name="VBR_SQLSERVER_SERVER" value="localhost" />\r\n    <property
            name="VBR_SQLSERVER_DATABASE" value="VeeamBackup" />\r\n    <property
            name="VBR_SQLSERVER_AUTHENTICATION" value="1" />\r\n    <property
            name="VBR_SQLSERVER_USERNAME" value="postgres" />\r\n    <property
            name="VBR_SQLSERVER_PASSWORD" value="Password1" hidden="1"/>\r\n\r\n    <!--Ports
            configuration-->\r\n    <property name="VBRC_SERVICE_PORT" value="9393" />\r\n
            <property name="VBR_SERVICE_PORT" value="9392" />\r\n    <property
            name="VBR_SECURE_CONNECTIONS_PORT" value="9401" />\r\n    <property
            name="VBR_RESTSERVICE_PORT" value="9419" />\r\n\r\n    <!--Data locations-->\r\n
            <property name="INSTALLDIR" value="C:\\Program Files\\Veeam\\Backup and Replication"
            />\r\n    <property name="VM_CATALOGPATH" value="C:\\VBRCatalog" />\r\n    <property
            name="VBR_IRCACHE" value="C:\\ProgramData\\Veeam\\Backup\\IRCache" />\r\n\r\n    <!--
            Automatic update settings-->\r\n    <property name="VBR_CHECK_UPDATES" value="1"
            />\r\n\r\n    <!--Plug-ins for Veeam Backup & Replication-->\r\n    <property
            name="AHV_INSTALL" value="0" />\r\n    <property name="RHV_INSTALL" value="0" />\r\n
            <property name="AWS_INSTALL" value="0" />\r\n    <property name="AZURE_INSTALL" value="0"
            />\r\n    <property name="GCP_INSTALL" value="0" />\r\n    <property name="KASTEN_INSTALL"
            value="0" />\r\n\r\n  </properties>\r\n</unattendedInstallationConfiguration>',
            'allowAutoReboot': True, 'stopAllActivities': False, 'useManagementAgentCredentials':
            False, 'adminCredentials': {'username': 'vspc1\\administrator', 'password': 'Password1'}},
            'licenseSettings': {'licenseFileContent': 'BADANBgkqhkiG9w0BAQEFAASCAmEwggJdAgEAAoGBAIPK6b
            ojg0Tj/GcvQvg5iTFpmGbAdAFXRmOE4L5gDiYdTIPSMMJnGDITqF33lTX6nkVA5EQQy14xHziMvONEmHkIsNwudIth
            ody3H07aiKp+fakIwlCAsFCC3TnSHBuc1+Xp0r8L9ILi9UNWmss/XdsXiaPZd03daAR2JLUzXp3zAgMBAAECgYB6se
            z4utkZyLqSAaDyYPZFh0430tHs8ah5PBrTga+KclpqmsOEKOCQtlZX7Qf/seupA6m/aHc8oLS1O+kaGCFtpwsFSnin
            /7f8vXXlDpFSZYfWO+1u7W0ub50E9zmSH/Uup4QFPQm20Vf45Frq1KTpJfkywMKf5jbNwaEcEmFvYQJBAONHojOa1s
            AijDMUqdq4sZdIhvnz9EdCalzNGO3GCWV0ptwLGh7V4zP0heQnl1aaz/Tt9QJ7RlOUZomNIc/0siMCQQCUclNptWWp
            72iG0QmwVEmvn9vs8nlunGbmBBeo++a/46T51qU2GQxRSSi1M8T8aXrxHwA8HFjd5T1PK17tBJnxAkEAtYfMlP0yU2
            oEovP5KppkNhoWvOPOE3CHtbGXHKsVbDR85bn0VfauLxw6KN46cVDbkpzRGfdOV4lrUKgp/ohKEwJAN62N1bdA83Ul
            anObQ7TJkoLOFVh47WDiQ2HDkhExYkW7Ci5U9y577T0YdKZ/OwFBKJEtIF6tgkTKMxicWSABsQJBANKIj6wkNfnxn5
            EwniB1959xNS0PrpeaLVedEhW2HJKrBBzQKpfv0A3aGl1CwTAfld0lNiFJ7jMo1J6rlDHXw9QwggJeAgEAAoGBAJ5g
            hbXlirsjv5Fdn7BFruUfE1w48BPp0M3jUIQXsN3bB4nj5a5soCQjKVN80p9N5j+ns53Opd/7Zm6nBFhwJ+ahG2DkMv
            vN6ceS4gUQIJfQqcWJmJV8876I+MAr6WpA4yG2kBOntXw4kmB0dbNLsG5KRp96/Y30haSaJhicd27tAgMBAAECgYEA
            hOTZTdheoMlOZdv5sx/FsdxxkmD0ksEPxLOJTE3Uy1SO7tWcVNAxUCFw++0xjxr+qUs/HJvZ9Cgvu4nJy6vQzhNPwA
            09Yjw7IDVE73/wKydmdbI9sW4vSxpAHzP3khahqMCeAMjfoY1Ji/G0tiFtgUGY4cqhoM3eMGVyTfUroMECQQDLwmxU
            7vncEirPyRUj7S21ns9EIeKrgHChMk+wwdX3XBABCji5IKPNMheMCuOjzxFMLZxZQSNWBuRg57I9fdn7AkEAxvt2eR
            TcqHz7gNuKYP4bam9ODAVkVOkYFXSv2PjsohI1FALVBAffu7E0mJFbbs8aL1vO5wbr2bbYVuApjr+uNwJBAMgI6Dd9
            oPgnMbZpz4JEr3I1JX/a0F/UKT5nWQrLUNaVn/SVZ1h/ra+d9LX8Xr0LZQznXi3Vn+4tt/lWnYp2yg8CQHMTzyqrhA
            n1bkbRsS/zBcwCXzLYk3P/8qvF9kUXgVMiEIxoLuXL3/reuzpZJnXpVI17HSfDevdIpclojuA9vvUCQQCcxDFk/oAF
            nwIND7Xy5Jy0fzCCzvWW05mVCzYAnj2rKIw6y+q55jE6hExG1Z8Pfn36MS/cw1GmNlvKeq9hG+8b=',
            'licenseUid': None, 'licenseSource': 'LicenseFileContent'}, 'credentials': {'tenantName':
            'alphaadmin', 'tenantPassword': 'Password1'}}, 'schedule': {'dateTime':
            '2025-07-23T19:55:26.3617936-05:00'}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ErrorResponse | ScheduleInstallBackupServerOnDiscoveryComputerResponse200]
    """

    kwargs = _get_kwargs(
        computer_uid=computer_uid,
        body=body,
        select=select,
        x_request_id=x_request_id,
        x_client_version=x_client_version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    computer_uid: UUID,
    *,
    client: AuthenticatedClient,
    body: VbrScheduledDeploymentConfigurationWithCredentials,
    select: str | Unset = UNSET,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Any | ErrorResponse | ScheduleInstallBackupServerOnDiscoveryComputerResponse200 | None:
    r"""Schedule Veeam Backup & Replication Installation on Discovered Computer

     Creates a sheduled task that installs Veeam Backup & Replication and management agent on a
    discovered computer with the specified UID.
    > Deploys only the missing component if the other one is already installed.

    Args:
        computer_uid (UUID):
        select (str | Unset):
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):
        body (VbrScheduledDeploymentConfigurationWithCredentials):  Example: {'configuration':
            {'configuration': {'distribution': {'filePath':
            '\\\\tech.local\\tech\\VSPC\\VBR\\13\\Butler\\VeeamBackup&Replication_13.iso', 'userName':
            'tech\\svc-datam', 'password': 'n_59=r2wc%k8Rx.X'}, 'usePredownloadedIso': False,
            'answerXml': '<?xml version="1.0"
            encoding="utf-8"?>\r\n<unattendedInstallationConfiguration bundle="VBR"
            mode="install">\r\n  <properties>\r\n\r\n    <!--License agreements-->\r\n    <property
            name="ACCEPT_EULA" value="1" />\r\n    <property name="ACCEPT_LICENSING_POLICY" value="1"
            />\r\n    <property name="ACCEPT_THIRDPARTY_LICENSES" value="1" />\r\n    <property
            name="ACCEPT_REQUIRED_SOFTWARE" value="1" />\r\n\r\n    <!--License file-->\r\n
            <property name="VBR_LICENSE_FILE" value="" />\r\n    <property
            name="VBR_LICENSE_AUTOUPDATE" value="1" />\r\n\r\n    <!--Service account-->\r\n
            <property name="VBR_SERVICE_USER" value="vspc1\\administrator" />\r\n    <property
            name="VBR_SERVICE_PASSWORD" value="Password1" hidden="1" />\r\n\r\n    <!--Database
            configuration-->\r\n    <property name="VBR_SQLSERVER_INSTALL" value="0" />\r\n
            <property name="VBR_SQLSERVER_ENGINE" value="1" />\r\n    <property
            name="VBR_SQLSERVER_SERVER" value="localhost" />\r\n    <property
            name="VBR_SQLSERVER_DATABASE" value="VeeamBackup" />\r\n    <property
            name="VBR_SQLSERVER_AUTHENTICATION" value="1" />\r\n    <property
            name="VBR_SQLSERVER_USERNAME" value="postgres" />\r\n    <property
            name="VBR_SQLSERVER_PASSWORD" value="Password1" hidden="1"/>\r\n\r\n    <!--Ports
            configuration-->\r\n    <property name="VBRC_SERVICE_PORT" value="9393" />\r\n
            <property name="VBR_SERVICE_PORT" value="9392" />\r\n    <property
            name="VBR_SECURE_CONNECTIONS_PORT" value="9401" />\r\n    <property
            name="VBR_RESTSERVICE_PORT" value="9419" />\r\n\r\n    <!--Data locations-->\r\n
            <property name="INSTALLDIR" value="C:\\Program Files\\Veeam\\Backup and Replication"
            />\r\n    <property name="VM_CATALOGPATH" value="C:\\VBRCatalog" />\r\n    <property
            name="VBR_IRCACHE" value="C:\\ProgramData\\Veeam\\Backup\\IRCache" />\r\n\r\n    <!--
            Automatic update settings-->\r\n    <property name="VBR_CHECK_UPDATES" value="1"
            />\r\n\r\n    <!--Plug-ins for Veeam Backup & Replication-->\r\n    <property
            name="AHV_INSTALL" value="0" />\r\n    <property name="RHV_INSTALL" value="0" />\r\n
            <property name="AWS_INSTALL" value="0" />\r\n    <property name="AZURE_INSTALL" value="0"
            />\r\n    <property name="GCP_INSTALL" value="0" />\r\n    <property name="KASTEN_INSTALL"
            value="0" />\r\n\r\n  </properties>\r\n</unattendedInstallationConfiguration>',
            'allowAutoReboot': True, 'stopAllActivities': False, 'useManagementAgentCredentials':
            False, 'adminCredentials': {'username': 'vspc1\\administrator', 'password': 'Password1'}},
            'licenseSettings': {'licenseFileContent': 'BADANBgkqhkiG9w0BAQEFAASCAmEwggJdAgEAAoGBAIPK6b
            ojg0Tj/GcvQvg5iTFpmGbAdAFXRmOE4L5gDiYdTIPSMMJnGDITqF33lTX6nkVA5EQQy14xHziMvONEmHkIsNwudIth
            ody3H07aiKp+fakIwlCAsFCC3TnSHBuc1+Xp0r8L9ILi9UNWmss/XdsXiaPZd03daAR2JLUzXp3zAgMBAAECgYB6se
            z4utkZyLqSAaDyYPZFh0430tHs8ah5PBrTga+KclpqmsOEKOCQtlZX7Qf/seupA6m/aHc8oLS1O+kaGCFtpwsFSnin
            /7f8vXXlDpFSZYfWO+1u7W0ub50E9zmSH/Uup4QFPQm20Vf45Frq1KTpJfkywMKf5jbNwaEcEmFvYQJBAONHojOa1s
            AijDMUqdq4sZdIhvnz9EdCalzNGO3GCWV0ptwLGh7V4zP0heQnl1aaz/Tt9QJ7RlOUZomNIc/0siMCQQCUclNptWWp
            72iG0QmwVEmvn9vs8nlunGbmBBeo++a/46T51qU2GQxRSSi1M8T8aXrxHwA8HFjd5T1PK17tBJnxAkEAtYfMlP0yU2
            oEovP5KppkNhoWvOPOE3CHtbGXHKsVbDR85bn0VfauLxw6KN46cVDbkpzRGfdOV4lrUKgp/ohKEwJAN62N1bdA83Ul
            anObQ7TJkoLOFVh47WDiQ2HDkhExYkW7Ci5U9y577T0YdKZ/OwFBKJEtIF6tgkTKMxicWSABsQJBANKIj6wkNfnxn5
            EwniB1959xNS0PrpeaLVedEhW2HJKrBBzQKpfv0A3aGl1CwTAfld0lNiFJ7jMo1J6rlDHXw9QwggJeAgEAAoGBAJ5g
            hbXlirsjv5Fdn7BFruUfE1w48BPp0M3jUIQXsN3bB4nj5a5soCQjKVN80p9N5j+ns53Opd/7Zm6nBFhwJ+ahG2DkMv
            vN6ceS4gUQIJfQqcWJmJV8876I+MAr6WpA4yG2kBOntXw4kmB0dbNLsG5KRp96/Y30haSaJhicd27tAgMBAAECgYEA
            hOTZTdheoMlOZdv5sx/FsdxxkmD0ksEPxLOJTE3Uy1SO7tWcVNAxUCFw++0xjxr+qUs/HJvZ9Cgvu4nJy6vQzhNPwA
            09Yjw7IDVE73/wKydmdbI9sW4vSxpAHzP3khahqMCeAMjfoY1Ji/G0tiFtgUGY4cqhoM3eMGVyTfUroMECQQDLwmxU
            7vncEirPyRUj7S21ns9EIeKrgHChMk+wwdX3XBABCji5IKPNMheMCuOjzxFMLZxZQSNWBuRg57I9fdn7AkEAxvt2eR
            TcqHz7gNuKYP4bam9ODAVkVOkYFXSv2PjsohI1FALVBAffu7E0mJFbbs8aL1vO5wbr2bbYVuApjr+uNwJBAMgI6Dd9
            oPgnMbZpz4JEr3I1JX/a0F/UKT5nWQrLUNaVn/SVZ1h/ra+d9LX8Xr0LZQznXi3Vn+4tt/lWnYp2yg8CQHMTzyqrhA
            n1bkbRsS/zBcwCXzLYk3P/8qvF9kUXgVMiEIxoLuXL3/reuzpZJnXpVI17HSfDevdIpclojuA9vvUCQQCcxDFk/oAF
            nwIND7Xy5Jy0fzCCzvWW05mVCzYAnj2rKIw6y+q55jE6hExG1Z8Pfn36MS/cw1GmNlvKeq9hG+8b=',
            'licenseUid': None, 'licenseSource': 'LicenseFileContent'}, 'credentials': {'tenantName':
            'alphaadmin', 'tenantPassword': 'Password1'}}, 'schedule': {'dateTime':
            '2025-07-23T19:55:26.3617936-05:00'}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ErrorResponse | ScheduleInstallBackupServerOnDiscoveryComputerResponse200
    """

    return (
        await asyncio_detailed(
            computer_uid=computer_uid,
            client=client,
            body=body,
            select=select,
            x_request_id=x_request_id,
            x_client_version=x_client_version,
        )
    ).parsed
