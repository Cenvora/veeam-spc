from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.deployment_configuration import DeploymentConfiguration
from ...models.error_response import ErrorResponse
from ...models.install_backup_agent_on_discovery_computer_response_200 import (
    InstallBackupAgentOnDiscoveryComputerResponse200,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    computer_uid: UUID,
    *,
    body: DeploymentConfiguration,
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
        "url": "/discovery/computers/{computer_uid}/installBackupAgent".format(
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
) -> Any | ErrorResponse | InstallBackupAgentOnDiscoveryComputerResponse200:
    if response.status_code == 200:
        response_200 = InstallBackupAgentOnDiscoveryComputerResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 202:
        response_202 = cast(Any, None)
        return response_202

    response_default = ErrorResponse.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | ErrorResponse | InstallBackupAgentOnDiscoveryComputerResponse200]:
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
    body: DeploymentConfiguration,
    select: str | Unset = UNSET,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Response[Any | ErrorResponse | InstallBackupAgentOnDiscoveryComputerResponse200]:
    """Install Backup Agent on Discovered Computer

     Deploys Veeam backup agent and management agent on a discovered computer with the specified UID.
    Deploys only the missing component if the other one is already installed.
    > To track the deployment progress, you can use the `WaitDeploymentTask` operation.

    Args:
        computer_uid (UUID):
        select (str | Unset):
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):
        body (DeploymentConfiguration):  Example: {'backupPolicyUid':
            '70069387-2799-489b-9592-4b11c55012d7', 'allowAutoRebootIfNeeded': True,
            'setReadOnlyAccess': True, 'installCbtDriver': False, 'credentials': None,
            'backupAgentSettings': None}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ErrorResponse | InstallBackupAgentOnDiscoveryComputerResponse200]
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
    body: DeploymentConfiguration,
    select: str | Unset = UNSET,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Any | ErrorResponse | InstallBackupAgentOnDiscoveryComputerResponse200 | None:
    """Install Backup Agent on Discovered Computer

     Deploys Veeam backup agent and management agent on a discovered computer with the specified UID.
    Deploys only the missing component if the other one is already installed.
    > To track the deployment progress, you can use the `WaitDeploymentTask` operation.

    Args:
        computer_uid (UUID):
        select (str | Unset):
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):
        body (DeploymentConfiguration):  Example: {'backupPolicyUid':
            '70069387-2799-489b-9592-4b11c55012d7', 'allowAutoRebootIfNeeded': True,
            'setReadOnlyAccess': True, 'installCbtDriver': False, 'credentials': None,
            'backupAgentSettings': None}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ErrorResponse | InstallBackupAgentOnDiscoveryComputerResponse200
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
    body: DeploymentConfiguration,
    select: str | Unset = UNSET,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Response[Any | ErrorResponse | InstallBackupAgentOnDiscoveryComputerResponse200]:
    """Install Backup Agent on Discovered Computer

     Deploys Veeam backup agent and management agent on a discovered computer with the specified UID.
    Deploys only the missing component if the other one is already installed.
    > To track the deployment progress, you can use the `WaitDeploymentTask` operation.

    Args:
        computer_uid (UUID):
        select (str | Unset):
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):
        body (DeploymentConfiguration):  Example: {'backupPolicyUid':
            '70069387-2799-489b-9592-4b11c55012d7', 'allowAutoRebootIfNeeded': True,
            'setReadOnlyAccess': True, 'installCbtDriver': False, 'credentials': None,
            'backupAgentSettings': None}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ErrorResponse | InstallBackupAgentOnDiscoveryComputerResponse200]
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
    body: DeploymentConfiguration,
    select: str | Unset = UNSET,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Any | ErrorResponse | InstallBackupAgentOnDiscoveryComputerResponse200 | None:
    """Install Backup Agent on Discovered Computer

     Deploys Veeam backup agent and management agent on a discovered computer with the specified UID.
    Deploys only the missing component if the other one is already installed.
    > To track the deployment progress, you can use the `WaitDeploymentTask` operation.

    Args:
        computer_uid (UUID):
        select (str | Unset):
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):
        body (DeploymentConfiguration):  Example: {'backupPolicyUid':
            '70069387-2799-489b-9592-4b11c55012d7', 'allowAutoRebootIfNeeded': True,
            'setReadOnlyAccess': True, 'installCbtDriver': False, 'credentials': None,
            'backupAgentSettings': None}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ErrorResponse | InstallBackupAgentOnDiscoveryComputerResponse200
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
