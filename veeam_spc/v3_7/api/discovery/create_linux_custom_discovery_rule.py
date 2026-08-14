from http import HTTPStatus
from typing import Any, cast
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.create_linux_custom_discovery_rule_response_200 import CreateLinuxCustomDiscoveryRuleResponse200
from ...models.error_response import ErrorResponse
from ...models.linux_custom_discovery_rule_input import LinuxCustomDiscoveryRuleInput
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: LinuxCustomDiscoveryRuleInput,
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
        "url": "/discovery/rules/linux/custom",
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | CreateLinuxCustomDiscoveryRuleResponse200 | ErrorResponse:
    if response.status_code == 200:
        response_200 = CreateLinuxCustomDiscoveryRuleResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 202:
        response_202 = cast(Any, None)
        return response_202

    response_default = ErrorResponse.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | CreateLinuxCustomDiscoveryRuleResponse200 | ErrorResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: LinuxCustomDiscoveryRuleInput,
    select: str | Unset = UNSET,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Response[Any | CreateLinuxCustomDiscoveryRuleResponse200 | ErrorResponse]:
    """Create Import-Based Discovery Rule for Linux

     Creates a Linux rule based on a list of IP addresses and DNS names.

    Args:
        select (str | Unset):
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):
        body (LinuxCustomDiscoveryRuleInput):  Example: {'name': 'Linux Custom Rule',
            'masterAgentUid': 'da463bea-d186-4a14-b809-4aba366b03e8', 'hosts': ['r2val'],
            'credentials': [{'username': 'root', 'password': 'Password1', 'priority': 0,
            'description': None, 'sshPort': 22, 'elevateAccountPrivileges': False,
            'addAccountToSudoersFile': False, 'useSuIfsudoFails': False, 'rootPassword': '1',
            'sshPrivateKey': None, 'passphrase': None, 'type': 'LinuxBased'}], 'filter': None,
            'notificationSettings': None, 'deploymentSettings': None, 'scheduleSettings':
            {'scheduleType': 'NotScheduled', 'timeZone': None, 'dailyScheduleSettings': None,
            'monthlyScheduleSettings': None, 'periodicalScheduleSettings': None}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CreateLinuxCustomDiscoveryRuleResponse200 | ErrorResponse]
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
    body: LinuxCustomDiscoveryRuleInput,
    select: str | Unset = UNSET,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Any | CreateLinuxCustomDiscoveryRuleResponse200 | ErrorResponse | None:
    """Create Import-Based Discovery Rule for Linux

     Creates a Linux rule based on a list of IP addresses and DNS names.

    Args:
        select (str | Unset):
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):
        body (LinuxCustomDiscoveryRuleInput):  Example: {'name': 'Linux Custom Rule',
            'masterAgentUid': 'da463bea-d186-4a14-b809-4aba366b03e8', 'hosts': ['r2val'],
            'credentials': [{'username': 'root', 'password': 'Password1', 'priority': 0,
            'description': None, 'sshPort': 22, 'elevateAccountPrivileges': False,
            'addAccountToSudoersFile': False, 'useSuIfsudoFails': False, 'rootPassword': '1',
            'sshPrivateKey': None, 'passphrase': None, 'type': 'LinuxBased'}], 'filter': None,
            'notificationSettings': None, 'deploymentSettings': None, 'scheduleSettings':
            {'scheduleType': 'NotScheduled', 'timeZone': None, 'dailyScheduleSettings': None,
            'monthlyScheduleSettings': None, 'periodicalScheduleSettings': None}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CreateLinuxCustomDiscoveryRuleResponse200 | ErrorResponse
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
    body: LinuxCustomDiscoveryRuleInput,
    select: str | Unset = UNSET,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Response[Any | CreateLinuxCustomDiscoveryRuleResponse200 | ErrorResponse]:
    """Create Import-Based Discovery Rule for Linux

     Creates a Linux rule based on a list of IP addresses and DNS names.

    Args:
        select (str | Unset):
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):
        body (LinuxCustomDiscoveryRuleInput):  Example: {'name': 'Linux Custom Rule',
            'masterAgentUid': 'da463bea-d186-4a14-b809-4aba366b03e8', 'hosts': ['r2val'],
            'credentials': [{'username': 'root', 'password': 'Password1', 'priority': 0,
            'description': None, 'sshPort': 22, 'elevateAccountPrivileges': False,
            'addAccountToSudoersFile': False, 'useSuIfsudoFails': False, 'rootPassword': '1',
            'sshPrivateKey': None, 'passphrase': None, 'type': 'LinuxBased'}], 'filter': None,
            'notificationSettings': None, 'deploymentSettings': None, 'scheduleSettings':
            {'scheduleType': 'NotScheduled', 'timeZone': None, 'dailyScheduleSettings': None,
            'monthlyScheduleSettings': None, 'periodicalScheduleSettings': None}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CreateLinuxCustomDiscoveryRuleResponse200 | ErrorResponse]
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
    body: LinuxCustomDiscoveryRuleInput,
    select: str | Unset = UNSET,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Any | CreateLinuxCustomDiscoveryRuleResponse200 | ErrorResponse | None:
    """Create Import-Based Discovery Rule for Linux

     Creates a Linux rule based on a list of IP addresses and DNS names.

    Args:
        select (str | Unset):
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):
        body (LinuxCustomDiscoveryRuleInput):  Example: {'name': 'Linux Custom Rule',
            'masterAgentUid': 'da463bea-d186-4a14-b809-4aba366b03e8', 'hosts': ['r2val'],
            'credentials': [{'username': 'root', 'password': 'Password1', 'priority': 0,
            'description': None, 'sshPort': 22, 'elevateAccountPrivileges': False,
            'addAccountToSudoersFile': False, 'useSuIfsudoFails': False, 'rootPassword': '1',
            'sshPrivateKey': None, 'passphrase': None, 'type': 'LinuxBased'}], 'filter': None,
            'notificationSettings': None, 'deploymentSettings': None, 'scheduleSettings':
            {'scheduleType': 'NotScheduled', 'timeZone': None, 'dailyScheduleSettings': None,
            'monthlyScheduleSettings': None, 'periodicalScheduleSettings': None}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CreateLinuxCustomDiscoveryRuleResponse200 | ErrorResponse
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
