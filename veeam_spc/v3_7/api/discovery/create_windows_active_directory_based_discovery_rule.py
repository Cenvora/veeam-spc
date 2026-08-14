from http import HTTPStatus
from typing import Any, cast
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.create_windows_active_directory_based_discovery_rule_response_200 import (
    CreateWindowsActiveDirectoryBasedDiscoveryRuleResponse200,
)
from ...models.error_response import ErrorResponse
from ...models.windows_active_directory_based_discovery_rule_input import WindowsActiveDirectoryBasedDiscoveryRuleInput
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: WindowsActiveDirectoryBasedDiscoveryRuleInput,
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
        "url": "/discovery/rules/windows/adBased",
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | CreateWindowsActiveDirectoryBasedDiscoveryRuleResponse200 | ErrorResponse:
    if response.status_code == 200:
        response_200 = CreateWindowsActiveDirectoryBasedDiscoveryRuleResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 202:
        response_202 = cast(Any, None)
        return response_202

    response_default = ErrorResponse.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | CreateWindowsActiveDirectoryBasedDiscoveryRuleResponse200 | ErrorResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: WindowsActiveDirectoryBasedDiscoveryRuleInput,
    select: str | Unset = UNSET,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Response[Any | CreateWindowsActiveDirectoryBasedDiscoveryRuleResponse200 | ErrorResponse]:
    r"""Create Microsoft Entra ID Discovery Rule for Windows

     Creates an Microsoft Entra ID discovery rule.

    Args:
        select (str | Unset):
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):
        body (WindowsActiveDirectoryBasedDiscoveryRuleInput):  Example: {'name': 'Complex AD Rule
            By Query', 'masterAgentUid': '4ae8db95-8a4e-4a6a-b1fb-89a0d4b8aca5',
            'skipOfflineComputersDays': 45, 'customQuery': 'OU=auto, DC=n, DC=local', 'adMethod':
            'Query', 'useMasterManagementAgentCredentials': True, 'accessAccount': {'userName':
            'tech\\administrator', 'password': 'Password1'}, 'filter': {'exclusionMask': ['string'],
            'ignoreInaccessibleMachine': True, 'osTypes': ['WindowsServer'], 'applications':
            ['MicrosoftExchangeServer', 'MicrosoftActiveDirectory'], 'customApplication': None,
            'platforms': ['MicrosoftHyperVandVmWareVSphere']}, 'notificationSettings': {'isEnabled':
            True, 'scheduleType': 'Days', 'scheduleTime': '08:00', 'weekSettings': None, 'to':
            'administrator@vspc1.com', 'subject': 'VSPC Discovery Results', 'notifyOnTheFirstRun':
            False}, 'deploymentSettings': {'isEnabled': True, 'backupPolicyUid':
            '7a8f9468-4c46-4b52-b011-cce3507f6b04', 'setReadOnlyAccess': True, 'backupAgentSettings':
            {'disableScheduledBackups': True, 'disableControlPanelNotification': True,
            'disableBackupOverMeteredConnection': True, 'disableScheduleWakeup': True,
            'throttleBackupActivity': True, 'restrictVpnConnections': True,
            'limitBandwidthConsumption': False, 'bandwidthSpeedLimit': 2, 'bandwidthSpeedLimitUnit':
            'MbitPerSec', 'flrWithoutAdminPrivilegesAllowed': True}}, 'scheduleSettings':
            {'scheduleType': 'NotScheduled', 'timeZone': None, 'dailyScheduleSettings': None,
            'monthlyScheduleSettings': None, 'periodicalScheduleSettings': None}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CreateWindowsActiveDirectoryBasedDiscoveryRuleResponse200 | ErrorResponse]
    """

    kwargs = _get_kwargs(
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
    *,
    client: AuthenticatedClient,
    body: WindowsActiveDirectoryBasedDiscoveryRuleInput,
    select: str | Unset = UNSET,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Any | CreateWindowsActiveDirectoryBasedDiscoveryRuleResponse200 | ErrorResponse | None:
    r"""Create Microsoft Entra ID Discovery Rule for Windows

     Creates an Microsoft Entra ID discovery rule.

    Args:
        select (str | Unset):
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):
        body (WindowsActiveDirectoryBasedDiscoveryRuleInput):  Example: {'name': 'Complex AD Rule
            By Query', 'masterAgentUid': '4ae8db95-8a4e-4a6a-b1fb-89a0d4b8aca5',
            'skipOfflineComputersDays': 45, 'customQuery': 'OU=auto, DC=n, DC=local', 'adMethod':
            'Query', 'useMasterManagementAgentCredentials': True, 'accessAccount': {'userName':
            'tech\\administrator', 'password': 'Password1'}, 'filter': {'exclusionMask': ['string'],
            'ignoreInaccessibleMachine': True, 'osTypes': ['WindowsServer'], 'applications':
            ['MicrosoftExchangeServer', 'MicrosoftActiveDirectory'], 'customApplication': None,
            'platforms': ['MicrosoftHyperVandVmWareVSphere']}, 'notificationSettings': {'isEnabled':
            True, 'scheduleType': 'Days', 'scheduleTime': '08:00', 'weekSettings': None, 'to':
            'administrator@vspc1.com', 'subject': 'VSPC Discovery Results', 'notifyOnTheFirstRun':
            False}, 'deploymentSettings': {'isEnabled': True, 'backupPolicyUid':
            '7a8f9468-4c46-4b52-b011-cce3507f6b04', 'setReadOnlyAccess': True, 'backupAgentSettings':
            {'disableScheduledBackups': True, 'disableControlPanelNotification': True,
            'disableBackupOverMeteredConnection': True, 'disableScheduleWakeup': True,
            'throttleBackupActivity': True, 'restrictVpnConnections': True,
            'limitBandwidthConsumption': False, 'bandwidthSpeedLimit': 2, 'bandwidthSpeedLimitUnit':
            'MbitPerSec', 'flrWithoutAdminPrivilegesAllowed': True}}, 'scheduleSettings':
            {'scheduleType': 'NotScheduled', 'timeZone': None, 'dailyScheduleSettings': None,
            'monthlyScheduleSettings': None, 'periodicalScheduleSettings': None}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CreateWindowsActiveDirectoryBasedDiscoveryRuleResponse200 | ErrorResponse
    """

    return sync_detailed(
        client=client,
        body=body,
        select=select,
        x_request_id=x_request_id,
        x_client_version=x_client_version,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: WindowsActiveDirectoryBasedDiscoveryRuleInput,
    select: str | Unset = UNSET,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Response[Any | CreateWindowsActiveDirectoryBasedDiscoveryRuleResponse200 | ErrorResponse]:
    r"""Create Microsoft Entra ID Discovery Rule for Windows

     Creates an Microsoft Entra ID discovery rule.

    Args:
        select (str | Unset):
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):
        body (WindowsActiveDirectoryBasedDiscoveryRuleInput):  Example: {'name': 'Complex AD Rule
            By Query', 'masterAgentUid': '4ae8db95-8a4e-4a6a-b1fb-89a0d4b8aca5',
            'skipOfflineComputersDays': 45, 'customQuery': 'OU=auto, DC=n, DC=local', 'adMethod':
            'Query', 'useMasterManagementAgentCredentials': True, 'accessAccount': {'userName':
            'tech\\administrator', 'password': 'Password1'}, 'filter': {'exclusionMask': ['string'],
            'ignoreInaccessibleMachine': True, 'osTypes': ['WindowsServer'], 'applications':
            ['MicrosoftExchangeServer', 'MicrosoftActiveDirectory'], 'customApplication': None,
            'platforms': ['MicrosoftHyperVandVmWareVSphere']}, 'notificationSettings': {'isEnabled':
            True, 'scheduleType': 'Days', 'scheduleTime': '08:00', 'weekSettings': None, 'to':
            'administrator@vspc1.com', 'subject': 'VSPC Discovery Results', 'notifyOnTheFirstRun':
            False}, 'deploymentSettings': {'isEnabled': True, 'backupPolicyUid':
            '7a8f9468-4c46-4b52-b011-cce3507f6b04', 'setReadOnlyAccess': True, 'backupAgentSettings':
            {'disableScheduledBackups': True, 'disableControlPanelNotification': True,
            'disableBackupOverMeteredConnection': True, 'disableScheduleWakeup': True,
            'throttleBackupActivity': True, 'restrictVpnConnections': True,
            'limitBandwidthConsumption': False, 'bandwidthSpeedLimit': 2, 'bandwidthSpeedLimitUnit':
            'MbitPerSec', 'flrWithoutAdminPrivilegesAllowed': True}}, 'scheduleSettings':
            {'scheduleType': 'NotScheduled', 'timeZone': None, 'dailyScheduleSettings': None,
            'monthlyScheduleSettings': None, 'periodicalScheduleSettings': None}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CreateWindowsActiveDirectoryBasedDiscoveryRuleResponse200 | ErrorResponse]
    """

    kwargs = _get_kwargs(
        body=body,
        select=select,
        x_request_id=x_request_id,
        x_client_version=x_client_version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: WindowsActiveDirectoryBasedDiscoveryRuleInput,
    select: str | Unset = UNSET,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Any | CreateWindowsActiveDirectoryBasedDiscoveryRuleResponse200 | ErrorResponse | None:
    r"""Create Microsoft Entra ID Discovery Rule for Windows

     Creates an Microsoft Entra ID discovery rule.

    Args:
        select (str | Unset):
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):
        body (WindowsActiveDirectoryBasedDiscoveryRuleInput):  Example: {'name': 'Complex AD Rule
            By Query', 'masterAgentUid': '4ae8db95-8a4e-4a6a-b1fb-89a0d4b8aca5',
            'skipOfflineComputersDays': 45, 'customQuery': 'OU=auto, DC=n, DC=local', 'adMethod':
            'Query', 'useMasterManagementAgentCredentials': True, 'accessAccount': {'userName':
            'tech\\administrator', 'password': 'Password1'}, 'filter': {'exclusionMask': ['string'],
            'ignoreInaccessibleMachine': True, 'osTypes': ['WindowsServer'], 'applications':
            ['MicrosoftExchangeServer', 'MicrosoftActiveDirectory'], 'customApplication': None,
            'platforms': ['MicrosoftHyperVandVmWareVSphere']}, 'notificationSettings': {'isEnabled':
            True, 'scheduleType': 'Days', 'scheduleTime': '08:00', 'weekSettings': None, 'to':
            'administrator@vspc1.com', 'subject': 'VSPC Discovery Results', 'notifyOnTheFirstRun':
            False}, 'deploymentSettings': {'isEnabled': True, 'backupPolicyUid':
            '7a8f9468-4c46-4b52-b011-cce3507f6b04', 'setReadOnlyAccess': True, 'backupAgentSettings':
            {'disableScheduledBackups': True, 'disableControlPanelNotification': True,
            'disableBackupOverMeteredConnection': True, 'disableScheduleWakeup': True,
            'throttleBackupActivity': True, 'restrictVpnConnections': True,
            'limitBandwidthConsumption': False, 'bandwidthSpeedLimit': 2, 'bandwidthSpeedLimitUnit':
            'MbitPerSec', 'flrWithoutAdminPrivilegesAllowed': True}}, 'scheduleSettings':
            {'scheduleType': 'NotScheduled', 'timeZone': None, 'dailyScheduleSettings': None,
            'monthlyScheduleSettings': None, 'periodicalScheduleSettings': None}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CreateWindowsActiveDirectoryBasedDiscoveryRuleResponse200 | ErrorResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            select=select,
            x_request_id=x_request_id,
            x_client_version=x_client_version,
        )
    ).parsed
