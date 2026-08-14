from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.install_v_one_server_on_discovery_computer_response_200 import (
    InstallVOneServerOnDiscoveryComputerResponse200,
)
from ...models.v_one_deployment_configuration_with_credentials import VOneDeploymentConfigurationWithCredentials
from ...types import UNSET, Response, Unset


def _get_kwargs(
    computer_uid: UUID,
    *,
    body: VOneDeploymentConfigurationWithCredentials,
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
        "url": "/discovery/computers/{computer_uid}/installVOneServer".format(
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
) -> Any | ErrorResponse | InstallVOneServerOnDiscoveryComputerResponse200:
    if response.status_code == 200:
        response_200 = InstallVOneServerOnDiscoveryComputerResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 202:
        response_202 = cast(Any, None)
        return response_202

    response_default = ErrorResponse.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | ErrorResponse | InstallVOneServerOnDiscoveryComputerResponse200]:
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
    body: VOneDeploymentConfigurationWithCredentials,
    select: str | Unset = UNSET,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Response[Any | ErrorResponse | InstallVOneServerOnDiscoveryComputerResponse200]:
    r"""Install Veeam ONE on Discovered Computer

     Installs Veeam ONE and management agent on a discovered computer with the specified UID.
    > Deploys only the missing component if the other one is already installed.
    > To track the deployment progress, you can use the `WaitDeploymentTask` operation.

    Args:
        computer_uid (UUID):
        select (str | Unset):
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):
        body (VOneDeploymentConfigurationWithCredentials):  Example: {'configuration':
            {'distribution': {'filePath':
            '\\\\tech.local\\tech\\VSPC\\VBR\\13\\Butler\\VeeamONE_13.0.0.5457_20250723.iso',
            'userName': 'vspc\\admin', 'password': 'Password1'}, 'usePredownloadedIso': None,
            'answerXml': '<?xml version="1.0"
            encoding="utf-8"?>\r\n<unattendedInstallationConfiguration bundle="Vo" mode="install"
            version="1.0">\r\n  <properties>\r\n\r\n    <!--License agreements-->\r\n    <property
            name="ACCEPT_EULA" value="1" />\r\n    <property name="ACCEPT_LICENSING_POLICY" value="1"
            />\r\n    <property name="ACCEPT_THIRDPARTY_LICENSES" value="1" />\r\n    <property
            name="ACCEPT_REQUIRED_SOFTWARE" value="1" />\r\n\r\n    <!--License file-->\r\n
            <property name="VO_LICENSE_FILE" value="" />\r\n    <property name="VO_LICENSE_AUTOUPDATE"
            value="1" />\r\n\r\n    <!--Standalone components-->\r\n    <property
            name="VO_SERVER_COMPONENT" value="1" />\r\n    <property name="VO_WEB_COMPONENT" value="1"
            />\r\n    <property name="VO_CLIENT_COMPONENT" value="1" />\r\n\r\n    <!--Service
            account-->\r\n    <property name="VO_SERVICE_USER" value="vspc\\administrator" />\r\n
            <property name="VO_SERVICE_PASSWORD" value="Password1" hidden="1" />\r\n\r\n    <!--
            Database configuration-->\r\n    <property name="VO_SQLSERVER_INSTALL" value="1" />\r\n
            <property name="VO_SQLSERVER_SERVER" value="localhost\\VEEAMSQL2017" />\r\n    <property
            name="VO_SQLSERVER_DATABASE" value="VeeamONE" />\r\n    <property
            name="VO_SQLSERVER_AUTHENTICATION" value="0" />\r\n    <property
            name="VO_SQLSERVER_USERNAME" value="" />\r\n    <property name="VO_SQLSERVER_PASSWORD"
            value="" hidden="1"/>\r\n\r\n    <!-- Reporting database configuration-->\r\n    <property
            name="VO_POSTGRESQL_INSTALL" value="1" />\r\n    <property name="VO_POSTGRESQL_SERVER"
            value="localhost" />\r\n    <property name="VO_POSTGRESQL_PORT" value="5432" />\r\n
            <property name="VO_POSTGRESQL_DATABASE" value="VeeamONEWarehouse" />\r\n    <property
            name="VO_POSTGRESQL_AUTHENTICATION" value="0" />\r\n    <property
            name="VO_POSTGRESQL_USERNAME" value="postgres" />\r\n    <property
            name="VO_POSTGRESQL_PASSWORD" value="" hidden="1"/>\r\n\r\n    <!--Data collection
            mode-->\r\n    <property name="VO_INSTALLATION_TYPE" value="2" />\r\n\r\n    <!--Ports
            configuration-->\r\n    <property name="VO_MONITORING_SERVICE_PORT" value="2714" />\r\n
            <property name="VO_REPORTING_SERVICE_PORT" value="2742" />\r\n    <property
            name="VO_CACHING_SERVICE_PORT" value="2743" />\r\n    <property
            name="VO_INTERNAL_WEB_API_PORT" value="2741"  />\r\n    <property name="VO_WEBSITE_PORT"
            value="1239" />\r\n    <property name="VO_AGENT_SERVICE_PORT" value="2805" />\r\n\r\n
            <!--Certificate configuration-->\r\n    <property name="VO_CERTIFICATE_THUMBPRINT"
            value="" />\r\n\r\n    <!--Data locations-->\r\n    <property name="INSTALLDIR"
            value="C:\\Program Files\\Veeam\\Veeam ONE" />\r\n    <property name="VO_PERFCACHE"
            value="C:\\PerfCache" />\r\n\r\n    <!--Server connection-->\r\n    <property
            name="VO_CONNECTION_SERVER_NAME" value="" />\r\n    <property
            name="VO_CONNECTION_WEB_API_PORT" value="" />\r\n    <property name="VO_CONNECTION_USER"
            value="" />\r\n    <property name="VO_CONNECTION_PASSWORD" value="" hidden="1" />\r\n\r\n
            <!--Setup settings-->\r\n    <property name="REBOOT_IF_REQUIRED" value="0" />\r\n
            <property name="DONT_ADD_USER_TO_ADMINS" value="1" />\r\n\r\n
            </properties>\r\n</unattendedInstallationConfiguration>', 'allowAutoReboot': True,
            'stopAllActivities': None, 'useManagementAgentCredentials': None, 'adminCredentials':
            {'username': 'vspc\\administrator', 'password': 'Password1'}}, 'licenseSettings':
            {'licenseFileContent': 'BADANBgkqhkiG9w0BAQEFAASCAmEwggJdAgEAAoGBAIPK6bojg0Tj/GcvQvg5iTFpm
            GbAdAFXRmOE4L5gDiYdTIPSMMJnGDITqF33lTX6nkVA5EQQy14xHziMvONEmHkIsNwudIthody3H07aiKp+fakIwlC
            AsFCC3TnSHBuc1+Xp0r8L9ILi9UNWmss/XdsXiaPZd03daAR2JLUzXp3zAgMBAAECgYB6sez4utkZyLqSAaDyYPZFh
            0430tHs8ah5PBrTga+KclpqmsOEKOCQtlZX7Qf/seupA6m/aHc8oLS1O+kaGCFtpwsFSnin/7f8vXXlDpFSZYfWO+1
            u7W0ub50E9zmSH/Uup4QFPQm20Vf45Frq1KTpJfkywMKf5jbNwaEcEmFvYQJBAONHojOa1sAijDMUqdq4sZdIhvnz9
            EdCalzNGO3GCWV0ptwLGh7V4zP0heQnl1aaz/Tt9QJ7RlOUZomNIc/0siMCQQCUclNptWWp72iG0QmwVEmvn9vs8nl
            unGbmBBeo++a/46T51qU2GQxRSSi1M8T8aXrxHwA8HFjd5T1PK17tBJnxAkEAtYfMlP0yU2oEovP5KppkNhoWvOPOE
            3CHtbGXHKsVbDR85bn0VfauLxw6KN46cVDbkpzRGfdOV4lrUKgp/ohKEwJAN62N1bdA83UlanObQ7TJkoLOFVh47WD
            iQ2HDkhExYkW7Ci5U9y577T0YdKZ/OwFBKJEtIF6tgkTKMxicWSABsQJBANKIj6wkNfnxn5EwniB1959xNS0PrpeaL
            VedEhW2HJKrBBzQKpfv0A3aGl1CwTAfld0lNiFJ7jMo1J6rlDHXw9QwggJeAgEAAoGBAJ5ghbXlirsjv5Fdn7BFruU
            fE1w48BPp0M3jUIQXsN3bB4nj5a5soCQjKVN80p9N5j+ns53Opd/7Zm6nBFhwJ+ahG2DkMvvN6ceS4gUQIJfQqcWJm
            JV8876I+MAr6WpA4yG2kBOntXw4kmB0dbNLsG5KRp96/Y30haSaJhicd27tAgMBAAECgYEAhOTZTdheoMlOZdv5sx/
            FsdxxkmD0ksEPxLOJTE3Uy1SO7tWcVNAxUCFw++0xjxr+qUs/HJvZ9Cgvu4nJy6vQzhNPwA09Yjw7IDVE73/wKydmd
            bI9sW4vSxpAHzP3khahqMCeAMjfoY1Ji/G0tiFtgUGY4cqhoM3eMGVyTfUroMECQQDLwmxU7vncEirPyRUj7S21ns9
            EIeKrgHChMk+wwdX3XBABCji5IKPNMheMCuOjzxFMLZxZQSNWBuRg57I9fdn7AkEAxvt2eRTcqHz7gNuKYP4bam9OD
            AVkVOkYFXSv2PjsohI1FALVBAffu7E0mJFbbs8aL1vO5wbr2bbYVuApjr+uNwJBAMgI6Dd9oPgnMbZpz4JEr3I1JX/
            a0F/UKT5nWQrLUNaVn/SVZ1h/ra+d9LX8Xr0LZQznXi3Vn+4tt/lWnYp2yg8CQHMTzyqrhAn1bkbRsS/zBcwCXzLYk
            3P/8qvF9kUXgVMiEIxoLuXL3/reuzpZJnXpVI17HSfDevdIpclojuA9vvUCQQCcxDFk/oAFnwIND7Xy5Jy0fzCCzvW
            W05mVCzYAnj2rKIw6y+q55jE6hExG1Z8Pfn36MS/cw1GmNlvKeq9hG+8b=', 'licenseUid': None,
            'licenseSource': 'LicenseFileContent'}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ErrorResponse | InstallVOneServerOnDiscoveryComputerResponse200]
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
    body: VOneDeploymentConfigurationWithCredentials,
    select: str | Unset = UNSET,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Any | ErrorResponse | InstallVOneServerOnDiscoveryComputerResponse200 | None:
    r"""Install Veeam ONE on Discovered Computer

     Installs Veeam ONE and management agent on a discovered computer with the specified UID.
    > Deploys only the missing component if the other one is already installed.
    > To track the deployment progress, you can use the `WaitDeploymentTask` operation.

    Args:
        computer_uid (UUID):
        select (str | Unset):
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):
        body (VOneDeploymentConfigurationWithCredentials):  Example: {'configuration':
            {'distribution': {'filePath':
            '\\\\tech.local\\tech\\VSPC\\VBR\\13\\Butler\\VeeamONE_13.0.0.5457_20250723.iso',
            'userName': 'vspc\\admin', 'password': 'Password1'}, 'usePredownloadedIso': None,
            'answerXml': '<?xml version="1.0"
            encoding="utf-8"?>\r\n<unattendedInstallationConfiguration bundle="Vo" mode="install"
            version="1.0">\r\n  <properties>\r\n\r\n    <!--License agreements-->\r\n    <property
            name="ACCEPT_EULA" value="1" />\r\n    <property name="ACCEPT_LICENSING_POLICY" value="1"
            />\r\n    <property name="ACCEPT_THIRDPARTY_LICENSES" value="1" />\r\n    <property
            name="ACCEPT_REQUIRED_SOFTWARE" value="1" />\r\n\r\n    <!--License file-->\r\n
            <property name="VO_LICENSE_FILE" value="" />\r\n    <property name="VO_LICENSE_AUTOUPDATE"
            value="1" />\r\n\r\n    <!--Standalone components-->\r\n    <property
            name="VO_SERVER_COMPONENT" value="1" />\r\n    <property name="VO_WEB_COMPONENT" value="1"
            />\r\n    <property name="VO_CLIENT_COMPONENT" value="1" />\r\n\r\n    <!--Service
            account-->\r\n    <property name="VO_SERVICE_USER" value="vspc\\administrator" />\r\n
            <property name="VO_SERVICE_PASSWORD" value="Password1" hidden="1" />\r\n\r\n    <!--
            Database configuration-->\r\n    <property name="VO_SQLSERVER_INSTALL" value="1" />\r\n
            <property name="VO_SQLSERVER_SERVER" value="localhost\\VEEAMSQL2017" />\r\n    <property
            name="VO_SQLSERVER_DATABASE" value="VeeamONE" />\r\n    <property
            name="VO_SQLSERVER_AUTHENTICATION" value="0" />\r\n    <property
            name="VO_SQLSERVER_USERNAME" value="" />\r\n    <property name="VO_SQLSERVER_PASSWORD"
            value="" hidden="1"/>\r\n\r\n    <!-- Reporting database configuration-->\r\n    <property
            name="VO_POSTGRESQL_INSTALL" value="1" />\r\n    <property name="VO_POSTGRESQL_SERVER"
            value="localhost" />\r\n    <property name="VO_POSTGRESQL_PORT" value="5432" />\r\n
            <property name="VO_POSTGRESQL_DATABASE" value="VeeamONEWarehouse" />\r\n    <property
            name="VO_POSTGRESQL_AUTHENTICATION" value="0" />\r\n    <property
            name="VO_POSTGRESQL_USERNAME" value="postgres" />\r\n    <property
            name="VO_POSTGRESQL_PASSWORD" value="" hidden="1"/>\r\n\r\n    <!--Data collection
            mode-->\r\n    <property name="VO_INSTALLATION_TYPE" value="2" />\r\n\r\n    <!--Ports
            configuration-->\r\n    <property name="VO_MONITORING_SERVICE_PORT" value="2714" />\r\n
            <property name="VO_REPORTING_SERVICE_PORT" value="2742" />\r\n    <property
            name="VO_CACHING_SERVICE_PORT" value="2743" />\r\n    <property
            name="VO_INTERNAL_WEB_API_PORT" value="2741"  />\r\n    <property name="VO_WEBSITE_PORT"
            value="1239" />\r\n    <property name="VO_AGENT_SERVICE_PORT" value="2805" />\r\n\r\n
            <!--Certificate configuration-->\r\n    <property name="VO_CERTIFICATE_THUMBPRINT"
            value="" />\r\n\r\n    <!--Data locations-->\r\n    <property name="INSTALLDIR"
            value="C:\\Program Files\\Veeam\\Veeam ONE" />\r\n    <property name="VO_PERFCACHE"
            value="C:\\PerfCache" />\r\n\r\n    <!--Server connection-->\r\n    <property
            name="VO_CONNECTION_SERVER_NAME" value="" />\r\n    <property
            name="VO_CONNECTION_WEB_API_PORT" value="" />\r\n    <property name="VO_CONNECTION_USER"
            value="" />\r\n    <property name="VO_CONNECTION_PASSWORD" value="" hidden="1" />\r\n\r\n
            <!--Setup settings-->\r\n    <property name="REBOOT_IF_REQUIRED" value="0" />\r\n
            <property name="DONT_ADD_USER_TO_ADMINS" value="1" />\r\n\r\n
            </properties>\r\n</unattendedInstallationConfiguration>', 'allowAutoReboot': True,
            'stopAllActivities': None, 'useManagementAgentCredentials': None, 'adminCredentials':
            {'username': 'vspc\\administrator', 'password': 'Password1'}}, 'licenseSettings':
            {'licenseFileContent': 'BADANBgkqhkiG9w0BAQEFAASCAmEwggJdAgEAAoGBAIPK6bojg0Tj/GcvQvg5iTFpm
            GbAdAFXRmOE4L5gDiYdTIPSMMJnGDITqF33lTX6nkVA5EQQy14xHziMvONEmHkIsNwudIthody3H07aiKp+fakIwlC
            AsFCC3TnSHBuc1+Xp0r8L9ILi9UNWmss/XdsXiaPZd03daAR2JLUzXp3zAgMBAAECgYB6sez4utkZyLqSAaDyYPZFh
            0430tHs8ah5PBrTga+KclpqmsOEKOCQtlZX7Qf/seupA6m/aHc8oLS1O+kaGCFtpwsFSnin/7f8vXXlDpFSZYfWO+1
            u7W0ub50E9zmSH/Uup4QFPQm20Vf45Frq1KTpJfkywMKf5jbNwaEcEmFvYQJBAONHojOa1sAijDMUqdq4sZdIhvnz9
            EdCalzNGO3GCWV0ptwLGh7V4zP0heQnl1aaz/Tt9QJ7RlOUZomNIc/0siMCQQCUclNptWWp72iG0QmwVEmvn9vs8nl
            unGbmBBeo++a/46T51qU2GQxRSSi1M8T8aXrxHwA8HFjd5T1PK17tBJnxAkEAtYfMlP0yU2oEovP5KppkNhoWvOPOE
            3CHtbGXHKsVbDR85bn0VfauLxw6KN46cVDbkpzRGfdOV4lrUKgp/ohKEwJAN62N1bdA83UlanObQ7TJkoLOFVh47WD
            iQ2HDkhExYkW7Ci5U9y577T0YdKZ/OwFBKJEtIF6tgkTKMxicWSABsQJBANKIj6wkNfnxn5EwniB1959xNS0PrpeaL
            VedEhW2HJKrBBzQKpfv0A3aGl1CwTAfld0lNiFJ7jMo1J6rlDHXw9QwggJeAgEAAoGBAJ5ghbXlirsjv5Fdn7BFruU
            fE1w48BPp0M3jUIQXsN3bB4nj5a5soCQjKVN80p9N5j+ns53Opd/7Zm6nBFhwJ+ahG2DkMvvN6ceS4gUQIJfQqcWJm
            JV8876I+MAr6WpA4yG2kBOntXw4kmB0dbNLsG5KRp96/Y30haSaJhicd27tAgMBAAECgYEAhOTZTdheoMlOZdv5sx/
            FsdxxkmD0ksEPxLOJTE3Uy1SO7tWcVNAxUCFw++0xjxr+qUs/HJvZ9Cgvu4nJy6vQzhNPwA09Yjw7IDVE73/wKydmd
            bI9sW4vSxpAHzP3khahqMCeAMjfoY1Ji/G0tiFtgUGY4cqhoM3eMGVyTfUroMECQQDLwmxU7vncEirPyRUj7S21ns9
            EIeKrgHChMk+wwdX3XBABCji5IKPNMheMCuOjzxFMLZxZQSNWBuRg57I9fdn7AkEAxvt2eRTcqHz7gNuKYP4bam9OD
            AVkVOkYFXSv2PjsohI1FALVBAffu7E0mJFbbs8aL1vO5wbr2bbYVuApjr+uNwJBAMgI6Dd9oPgnMbZpz4JEr3I1JX/
            a0F/UKT5nWQrLUNaVn/SVZ1h/ra+d9LX8Xr0LZQznXi3Vn+4tt/lWnYp2yg8CQHMTzyqrhAn1bkbRsS/zBcwCXzLYk
            3P/8qvF9kUXgVMiEIxoLuXL3/reuzpZJnXpVI17HSfDevdIpclojuA9vvUCQQCcxDFk/oAFnwIND7Xy5Jy0fzCCzvW
            W05mVCzYAnj2rKIw6y+q55jE6hExG1Z8Pfn36MS/cw1GmNlvKeq9hG+8b=', 'licenseUid': None,
            'licenseSource': 'LicenseFileContent'}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ErrorResponse | InstallVOneServerOnDiscoveryComputerResponse200
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
    body: VOneDeploymentConfigurationWithCredentials,
    select: str | Unset = UNSET,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Response[Any | ErrorResponse | InstallVOneServerOnDiscoveryComputerResponse200]:
    r"""Install Veeam ONE on Discovered Computer

     Installs Veeam ONE and management agent on a discovered computer with the specified UID.
    > Deploys only the missing component if the other one is already installed.
    > To track the deployment progress, you can use the `WaitDeploymentTask` operation.

    Args:
        computer_uid (UUID):
        select (str | Unset):
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):
        body (VOneDeploymentConfigurationWithCredentials):  Example: {'configuration':
            {'distribution': {'filePath':
            '\\\\tech.local\\tech\\VSPC\\VBR\\13\\Butler\\VeeamONE_13.0.0.5457_20250723.iso',
            'userName': 'vspc\\admin', 'password': 'Password1'}, 'usePredownloadedIso': None,
            'answerXml': '<?xml version="1.0"
            encoding="utf-8"?>\r\n<unattendedInstallationConfiguration bundle="Vo" mode="install"
            version="1.0">\r\n  <properties>\r\n\r\n    <!--License agreements-->\r\n    <property
            name="ACCEPT_EULA" value="1" />\r\n    <property name="ACCEPT_LICENSING_POLICY" value="1"
            />\r\n    <property name="ACCEPT_THIRDPARTY_LICENSES" value="1" />\r\n    <property
            name="ACCEPT_REQUIRED_SOFTWARE" value="1" />\r\n\r\n    <!--License file-->\r\n
            <property name="VO_LICENSE_FILE" value="" />\r\n    <property name="VO_LICENSE_AUTOUPDATE"
            value="1" />\r\n\r\n    <!--Standalone components-->\r\n    <property
            name="VO_SERVER_COMPONENT" value="1" />\r\n    <property name="VO_WEB_COMPONENT" value="1"
            />\r\n    <property name="VO_CLIENT_COMPONENT" value="1" />\r\n\r\n    <!--Service
            account-->\r\n    <property name="VO_SERVICE_USER" value="vspc\\administrator" />\r\n
            <property name="VO_SERVICE_PASSWORD" value="Password1" hidden="1" />\r\n\r\n    <!--
            Database configuration-->\r\n    <property name="VO_SQLSERVER_INSTALL" value="1" />\r\n
            <property name="VO_SQLSERVER_SERVER" value="localhost\\VEEAMSQL2017" />\r\n    <property
            name="VO_SQLSERVER_DATABASE" value="VeeamONE" />\r\n    <property
            name="VO_SQLSERVER_AUTHENTICATION" value="0" />\r\n    <property
            name="VO_SQLSERVER_USERNAME" value="" />\r\n    <property name="VO_SQLSERVER_PASSWORD"
            value="" hidden="1"/>\r\n\r\n    <!-- Reporting database configuration-->\r\n    <property
            name="VO_POSTGRESQL_INSTALL" value="1" />\r\n    <property name="VO_POSTGRESQL_SERVER"
            value="localhost" />\r\n    <property name="VO_POSTGRESQL_PORT" value="5432" />\r\n
            <property name="VO_POSTGRESQL_DATABASE" value="VeeamONEWarehouse" />\r\n    <property
            name="VO_POSTGRESQL_AUTHENTICATION" value="0" />\r\n    <property
            name="VO_POSTGRESQL_USERNAME" value="postgres" />\r\n    <property
            name="VO_POSTGRESQL_PASSWORD" value="" hidden="1"/>\r\n\r\n    <!--Data collection
            mode-->\r\n    <property name="VO_INSTALLATION_TYPE" value="2" />\r\n\r\n    <!--Ports
            configuration-->\r\n    <property name="VO_MONITORING_SERVICE_PORT" value="2714" />\r\n
            <property name="VO_REPORTING_SERVICE_PORT" value="2742" />\r\n    <property
            name="VO_CACHING_SERVICE_PORT" value="2743" />\r\n    <property
            name="VO_INTERNAL_WEB_API_PORT" value="2741"  />\r\n    <property name="VO_WEBSITE_PORT"
            value="1239" />\r\n    <property name="VO_AGENT_SERVICE_PORT" value="2805" />\r\n\r\n
            <!--Certificate configuration-->\r\n    <property name="VO_CERTIFICATE_THUMBPRINT"
            value="" />\r\n\r\n    <!--Data locations-->\r\n    <property name="INSTALLDIR"
            value="C:\\Program Files\\Veeam\\Veeam ONE" />\r\n    <property name="VO_PERFCACHE"
            value="C:\\PerfCache" />\r\n\r\n    <!--Server connection-->\r\n    <property
            name="VO_CONNECTION_SERVER_NAME" value="" />\r\n    <property
            name="VO_CONNECTION_WEB_API_PORT" value="" />\r\n    <property name="VO_CONNECTION_USER"
            value="" />\r\n    <property name="VO_CONNECTION_PASSWORD" value="" hidden="1" />\r\n\r\n
            <!--Setup settings-->\r\n    <property name="REBOOT_IF_REQUIRED" value="0" />\r\n
            <property name="DONT_ADD_USER_TO_ADMINS" value="1" />\r\n\r\n
            </properties>\r\n</unattendedInstallationConfiguration>', 'allowAutoReboot': True,
            'stopAllActivities': None, 'useManagementAgentCredentials': None, 'adminCredentials':
            {'username': 'vspc\\administrator', 'password': 'Password1'}}, 'licenseSettings':
            {'licenseFileContent': 'BADANBgkqhkiG9w0BAQEFAASCAmEwggJdAgEAAoGBAIPK6bojg0Tj/GcvQvg5iTFpm
            GbAdAFXRmOE4L5gDiYdTIPSMMJnGDITqF33lTX6nkVA5EQQy14xHziMvONEmHkIsNwudIthody3H07aiKp+fakIwlC
            AsFCC3TnSHBuc1+Xp0r8L9ILi9UNWmss/XdsXiaPZd03daAR2JLUzXp3zAgMBAAECgYB6sez4utkZyLqSAaDyYPZFh
            0430tHs8ah5PBrTga+KclpqmsOEKOCQtlZX7Qf/seupA6m/aHc8oLS1O+kaGCFtpwsFSnin/7f8vXXlDpFSZYfWO+1
            u7W0ub50E9zmSH/Uup4QFPQm20Vf45Frq1KTpJfkywMKf5jbNwaEcEmFvYQJBAONHojOa1sAijDMUqdq4sZdIhvnz9
            EdCalzNGO3GCWV0ptwLGh7V4zP0heQnl1aaz/Tt9QJ7RlOUZomNIc/0siMCQQCUclNptWWp72iG0QmwVEmvn9vs8nl
            unGbmBBeo++a/46T51qU2GQxRSSi1M8T8aXrxHwA8HFjd5T1PK17tBJnxAkEAtYfMlP0yU2oEovP5KppkNhoWvOPOE
            3CHtbGXHKsVbDR85bn0VfauLxw6KN46cVDbkpzRGfdOV4lrUKgp/ohKEwJAN62N1bdA83UlanObQ7TJkoLOFVh47WD
            iQ2HDkhExYkW7Ci5U9y577T0YdKZ/OwFBKJEtIF6tgkTKMxicWSABsQJBANKIj6wkNfnxn5EwniB1959xNS0PrpeaL
            VedEhW2HJKrBBzQKpfv0A3aGl1CwTAfld0lNiFJ7jMo1J6rlDHXw9QwggJeAgEAAoGBAJ5ghbXlirsjv5Fdn7BFruU
            fE1w48BPp0M3jUIQXsN3bB4nj5a5soCQjKVN80p9N5j+ns53Opd/7Zm6nBFhwJ+ahG2DkMvvN6ceS4gUQIJfQqcWJm
            JV8876I+MAr6WpA4yG2kBOntXw4kmB0dbNLsG5KRp96/Y30haSaJhicd27tAgMBAAECgYEAhOTZTdheoMlOZdv5sx/
            FsdxxkmD0ksEPxLOJTE3Uy1SO7tWcVNAxUCFw++0xjxr+qUs/HJvZ9Cgvu4nJy6vQzhNPwA09Yjw7IDVE73/wKydmd
            bI9sW4vSxpAHzP3khahqMCeAMjfoY1Ji/G0tiFtgUGY4cqhoM3eMGVyTfUroMECQQDLwmxU7vncEirPyRUj7S21ns9
            EIeKrgHChMk+wwdX3XBABCji5IKPNMheMCuOjzxFMLZxZQSNWBuRg57I9fdn7AkEAxvt2eRTcqHz7gNuKYP4bam9OD
            AVkVOkYFXSv2PjsohI1FALVBAffu7E0mJFbbs8aL1vO5wbr2bbYVuApjr+uNwJBAMgI6Dd9oPgnMbZpz4JEr3I1JX/
            a0F/UKT5nWQrLUNaVn/SVZ1h/ra+d9LX8Xr0LZQznXi3Vn+4tt/lWnYp2yg8CQHMTzyqrhAn1bkbRsS/zBcwCXzLYk
            3P/8qvF9kUXgVMiEIxoLuXL3/reuzpZJnXpVI17HSfDevdIpclojuA9vvUCQQCcxDFk/oAFnwIND7Xy5Jy0fzCCzvW
            W05mVCzYAnj2rKIw6y+q55jE6hExG1Z8Pfn36MS/cw1GmNlvKeq9hG+8b=', 'licenseUid': None,
            'licenseSource': 'LicenseFileContent'}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ErrorResponse | InstallVOneServerOnDiscoveryComputerResponse200]
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
    body: VOneDeploymentConfigurationWithCredentials,
    select: str | Unset = UNSET,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Any | ErrorResponse | InstallVOneServerOnDiscoveryComputerResponse200 | None:
    r"""Install Veeam ONE on Discovered Computer

     Installs Veeam ONE and management agent on a discovered computer with the specified UID.
    > Deploys only the missing component if the other one is already installed.
    > To track the deployment progress, you can use the `WaitDeploymentTask` operation.

    Args:
        computer_uid (UUID):
        select (str | Unset):
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):
        body (VOneDeploymentConfigurationWithCredentials):  Example: {'configuration':
            {'distribution': {'filePath':
            '\\\\tech.local\\tech\\VSPC\\VBR\\13\\Butler\\VeeamONE_13.0.0.5457_20250723.iso',
            'userName': 'vspc\\admin', 'password': 'Password1'}, 'usePredownloadedIso': None,
            'answerXml': '<?xml version="1.0"
            encoding="utf-8"?>\r\n<unattendedInstallationConfiguration bundle="Vo" mode="install"
            version="1.0">\r\n  <properties>\r\n\r\n    <!--License agreements-->\r\n    <property
            name="ACCEPT_EULA" value="1" />\r\n    <property name="ACCEPT_LICENSING_POLICY" value="1"
            />\r\n    <property name="ACCEPT_THIRDPARTY_LICENSES" value="1" />\r\n    <property
            name="ACCEPT_REQUIRED_SOFTWARE" value="1" />\r\n\r\n    <!--License file-->\r\n
            <property name="VO_LICENSE_FILE" value="" />\r\n    <property name="VO_LICENSE_AUTOUPDATE"
            value="1" />\r\n\r\n    <!--Standalone components-->\r\n    <property
            name="VO_SERVER_COMPONENT" value="1" />\r\n    <property name="VO_WEB_COMPONENT" value="1"
            />\r\n    <property name="VO_CLIENT_COMPONENT" value="1" />\r\n\r\n    <!--Service
            account-->\r\n    <property name="VO_SERVICE_USER" value="vspc\\administrator" />\r\n
            <property name="VO_SERVICE_PASSWORD" value="Password1" hidden="1" />\r\n\r\n    <!--
            Database configuration-->\r\n    <property name="VO_SQLSERVER_INSTALL" value="1" />\r\n
            <property name="VO_SQLSERVER_SERVER" value="localhost\\VEEAMSQL2017" />\r\n    <property
            name="VO_SQLSERVER_DATABASE" value="VeeamONE" />\r\n    <property
            name="VO_SQLSERVER_AUTHENTICATION" value="0" />\r\n    <property
            name="VO_SQLSERVER_USERNAME" value="" />\r\n    <property name="VO_SQLSERVER_PASSWORD"
            value="" hidden="1"/>\r\n\r\n    <!-- Reporting database configuration-->\r\n    <property
            name="VO_POSTGRESQL_INSTALL" value="1" />\r\n    <property name="VO_POSTGRESQL_SERVER"
            value="localhost" />\r\n    <property name="VO_POSTGRESQL_PORT" value="5432" />\r\n
            <property name="VO_POSTGRESQL_DATABASE" value="VeeamONEWarehouse" />\r\n    <property
            name="VO_POSTGRESQL_AUTHENTICATION" value="0" />\r\n    <property
            name="VO_POSTGRESQL_USERNAME" value="postgres" />\r\n    <property
            name="VO_POSTGRESQL_PASSWORD" value="" hidden="1"/>\r\n\r\n    <!--Data collection
            mode-->\r\n    <property name="VO_INSTALLATION_TYPE" value="2" />\r\n\r\n    <!--Ports
            configuration-->\r\n    <property name="VO_MONITORING_SERVICE_PORT" value="2714" />\r\n
            <property name="VO_REPORTING_SERVICE_PORT" value="2742" />\r\n    <property
            name="VO_CACHING_SERVICE_PORT" value="2743" />\r\n    <property
            name="VO_INTERNAL_WEB_API_PORT" value="2741"  />\r\n    <property name="VO_WEBSITE_PORT"
            value="1239" />\r\n    <property name="VO_AGENT_SERVICE_PORT" value="2805" />\r\n\r\n
            <!--Certificate configuration-->\r\n    <property name="VO_CERTIFICATE_THUMBPRINT"
            value="" />\r\n\r\n    <!--Data locations-->\r\n    <property name="INSTALLDIR"
            value="C:\\Program Files\\Veeam\\Veeam ONE" />\r\n    <property name="VO_PERFCACHE"
            value="C:\\PerfCache" />\r\n\r\n    <!--Server connection-->\r\n    <property
            name="VO_CONNECTION_SERVER_NAME" value="" />\r\n    <property
            name="VO_CONNECTION_WEB_API_PORT" value="" />\r\n    <property name="VO_CONNECTION_USER"
            value="" />\r\n    <property name="VO_CONNECTION_PASSWORD" value="" hidden="1" />\r\n\r\n
            <!--Setup settings-->\r\n    <property name="REBOOT_IF_REQUIRED" value="0" />\r\n
            <property name="DONT_ADD_USER_TO_ADMINS" value="1" />\r\n\r\n
            </properties>\r\n</unattendedInstallationConfiguration>', 'allowAutoReboot': True,
            'stopAllActivities': None, 'useManagementAgentCredentials': None, 'adminCredentials':
            {'username': 'vspc\\administrator', 'password': 'Password1'}}, 'licenseSettings':
            {'licenseFileContent': 'BADANBgkqhkiG9w0BAQEFAASCAmEwggJdAgEAAoGBAIPK6bojg0Tj/GcvQvg5iTFpm
            GbAdAFXRmOE4L5gDiYdTIPSMMJnGDITqF33lTX6nkVA5EQQy14xHziMvONEmHkIsNwudIthody3H07aiKp+fakIwlC
            AsFCC3TnSHBuc1+Xp0r8L9ILi9UNWmss/XdsXiaPZd03daAR2JLUzXp3zAgMBAAECgYB6sez4utkZyLqSAaDyYPZFh
            0430tHs8ah5PBrTga+KclpqmsOEKOCQtlZX7Qf/seupA6m/aHc8oLS1O+kaGCFtpwsFSnin/7f8vXXlDpFSZYfWO+1
            u7W0ub50E9zmSH/Uup4QFPQm20Vf45Frq1KTpJfkywMKf5jbNwaEcEmFvYQJBAONHojOa1sAijDMUqdq4sZdIhvnz9
            EdCalzNGO3GCWV0ptwLGh7V4zP0heQnl1aaz/Tt9QJ7RlOUZomNIc/0siMCQQCUclNptWWp72iG0QmwVEmvn9vs8nl
            unGbmBBeo++a/46T51qU2GQxRSSi1M8T8aXrxHwA8HFjd5T1PK17tBJnxAkEAtYfMlP0yU2oEovP5KppkNhoWvOPOE
            3CHtbGXHKsVbDR85bn0VfauLxw6KN46cVDbkpzRGfdOV4lrUKgp/ohKEwJAN62N1bdA83UlanObQ7TJkoLOFVh47WD
            iQ2HDkhExYkW7Ci5U9y577T0YdKZ/OwFBKJEtIF6tgkTKMxicWSABsQJBANKIj6wkNfnxn5EwniB1959xNS0PrpeaL
            VedEhW2HJKrBBzQKpfv0A3aGl1CwTAfld0lNiFJ7jMo1J6rlDHXw9QwggJeAgEAAoGBAJ5ghbXlirsjv5Fdn7BFruU
            fE1w48BPp0M3jUIQXsN3bB4nj5a5soCQjKVN80p9N5j+ns53Opd/7Zm6nBFhwJ+ahG2DkMvvN6ceS4gUQIJfQqcWJm
            JV8876I+MAr6WpA4yG2kBOntXw4kmB0dbNLsG5KRp96/Y30haSaJhicd27tAgMBAAECgYEAhOTZTdheoMlOZdv5sx/
            FsdxxkmD0ksEPxLOJTE3Uy1SO7tWcVNAxUCFw++0xjxr+qUs/HJvZ9Cgvu4nJy6vQzhNPwA09Yjw7IDVE73/wKydmd
            bI9sW4vSxpAHzP3khahqMCeAMjfoY1Ji/G0tiFtgUGY4cqhoM3eMGVyTfUroMECQQDLwmxU7vncEirPyRUj7S21ns9
            EIeKrgHChMk+wwdX3XBABCji5IKPNMheMCuOjzxFMLZxZQSNWBuRg57I9fdn7AkEAxvt2eRTcqHz7gNuKYP4bam9OD
            AVkVOkYFXSv2PjsohI1FALVBAffu7E0mJFbbs8aL1vO5wbr2bbYVuApjr+uNwJBAMgI6Dd9oPgnMbZpz4JEr3I1JX/
            a0F/UKT5nWQrLUNaVn/SVZ1h/ra+d9LX8Xr0LZQznXi3Vn+4tt/lWnYp2yg8CQHMTzyqrhAn1bkbRsS/zBcwCXzLYk
            3P/8qvF9kUXgVMiEIxoLuXL3/reuzpZJnXpVI17HSfDevdIpclojuA9vvUCQQCcxDFk/oAFnwIND7Xy5Jy0fzCCzvW
            W05mVCzYAnj2rKIw6y+q55jE6hExG1Z8Pfn36MS/cw1GmNlvKeq9hG+8b=', 'licenseUid': None,
            'licenseSource': 'LicenseFileContent'}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ErrorResponse | InstallVOneServerOnDiscoveryComputerResponse200
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
