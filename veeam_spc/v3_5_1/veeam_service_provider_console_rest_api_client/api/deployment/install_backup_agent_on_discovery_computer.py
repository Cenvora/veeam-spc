from http import HTTPStatus
from typing import Any, Optional, Union, cast
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
    x_request_id: Union[Unset, UUID] = UNSET,
    x_client_version: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_request_id, Unset):
        headers["X-Request-id"] = x_request_id

    if not isinstance(x_client_version, Unset):
        headers["X-Client-Version"] = x_client_version

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/discovery/computers/{computer_uid}/installBackupAgent",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Union[Any, ErrorResponse, InstallBackupAgentOnDiscoveryComputerResponse200]:
    if response.status_code == 200:
        response_200 = InstallBackupAgentOnDiscoveryComputerResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 202:
        response_202 = cast(Any, None)
        return response_202

    response_default = ErrorResponse.from_dict(response.json())

    return response_default


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, ErrorResponse, InstallBackupAgentOnDiscoveryComputerResponse200]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    computer_uid: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
    body: DeploymentConfiguration,
    x_request_id: Union[Unset, UUID] = UNSET,
    x_client_version: Union[Unset, str] = UNSET,
) -> Response[Union[Any, ErrorResponse, InstallBackupAgentOnDiscoveryComputerResponse200]]:
    """Install Backup Agent on Discovered Computer

     Deploys Veeam backup agent and management agent on a discovered computer with the specified UID.
    Deploys only the missing component if the other one is already installed.
    > To track the deployment progress, you can use the `WaitDeploymentTask` operation.

    Args:
        computer_uid (UUID):
        x_request_id (Union[Unset, UUID]):
        x_client_version (Union[Unset, str]):
        body (DeploymentConfiguration):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ErrorResponse, InstallBackupAgentOnDiscoveryComputerResponse200]]
    """

    kwargs = _get_kwargs(
        computer_uid=computer_uid,
        body=body,
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
    client: Union[AuthenticatedClient, Client],
    body: DeploymentConfiguration,
    x_request_id: Union[Unset, UUID] = UNSET,
    x_client_version: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, ErrorResponse, InstallBackupAgentOnDiscoveryComputerResponse200]]:
    """Install Backup Agent on Discovered Computer

     Deploys Veeam backup agent and management agent on a discovered computer with the specified UID.
    Deploys only the missing component if the other one is already installed.
    > To track the deployment progress, you can use the `WaitDeploymentTask` operation.

    Args:
        computer_uid (UUID):
        x_request_id (Union[Unset, UUID]):
        x_client_version (Union[Unset, str]):
        body (DeploymentConfiguration):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ErrorResponse, InstallBackupAgentOnDiscoveryComputerResponse200]
    """

    return sync_detailed(
        computer_uid=computer_uid,
        client=client,
        body=body,
        x_request_id=x_request_id,
        x_client_version=x_client_version,
    ).parsed


async def asyncio_detailed(
    computer_uid: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
    body: DeploymentConfiguration,
    x_request_id: Union[Unset, UUID] = UNSET,
    x_client_version: Union[Unset, str] = UNSET,
) -> Response[Union[Any, ErrorResponse, InstallBackupAgentOnDiscoveryComputerResponse200]]:
    """Install Backup Agent on Discovered Computer

     Deploys Veeam backup agent and management agent on a discovered computer with the specified UID.
    Deploys only the missing component if the other one is already installed.
    > To track the deployment progress, you can use the `WaitDeploymentTask` operation.

    Args:
        computer_uid (UUID):
        x_request_id (Union[Unset, UUID]):
        x_client_version (Union[Unset, str]):
        body (DeploymentConfiguration):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ErrorResponse, InstallBackupAgentOnDiscoveryComputerResponse200]]
    """

    kwargs = _get_kwargs(
        computer_uid=computer_uid,
        body=body,
        x_request_id=x_request_id,
        x_client_version=x_client_version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    computer_uid: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
    body: DeploymentConfiguration,
    x_request_id: Union[Unset, UUID] = UNSET,
    x_client_version: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, ErrorResponse, InstallBackupAgentOnDiscoveryComputerResponse200]]:
    """Install Backup Agent on Discovered Computer

     Deploys Veeam backup agent and management agent on a discovered computer with the specified UID.
    Deploys only the missing component if the other one is already installed.
    > To track the deployment progress, you can use the `WaitDeploymentTask` operation.

    Args:
        computer_uid (UUID):
        x_request_id (Union[Unset, UUID]):
        x_client_version (Union[Unset, str]):
        body (DeploymentConfiguration):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ErrorResponse, InstallBackupAgentOnDiscoveryComputerResponse200]
    """

    return (
        await asyncio_detailed(
            computer_uid=computer_uid,
            client=client,
            body=body,
            x_request_id=x_request_id,
            x_client_version=x_client_version,
        )
    ).parsed
