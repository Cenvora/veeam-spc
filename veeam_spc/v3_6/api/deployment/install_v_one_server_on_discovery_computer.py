from http import HTTPStatus
from typing import Any, Optional, Union, cast
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
        "url": f"/discovery/computers/{computer_uid}/installVOneServer",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Union[Any, ErrorResponse, InstallVOneServerOnDiscoveryComputerResponse200]:
    if response.status_code == 200:
        response_200 = InstallVOneServerOnDiscoveryComputerResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 202:
        response_202 = cast(Any, None)
        return response_202

    response_default = ErrorResponse.from_dict(response.json())

    return response_default


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, ErrorResponse, InstallVOneServerOnDiscoveryComputerResponse200]]:
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
    body: VOneDeploymentConfigurationWithCredentials,
    x_request_id: Union[Unset, UUID] = UNSET,
    x_client_version: Union[Unset, str] = UNSET,
) -> Response[Union[Any, ErrorResponse, InstallVOneServerOnDiscoveryComputerResponse200]]:
    """Install Veeam ONE on Discovered Computer

     Installs Veeam ONE and management agent on a discovered computer with the specified UID.
    > Deploys only the missing component if the other one is already installed.
    > To track the deployment progress, you can use the `WaitDeploymentTask` operation.

    Args:
        computer_uid (UUID):
        x_request_id (Union[Unset, UUID]):
        x_client_version (Union[Unset, str]):
        body (VOneDeploymentConfigurationWithCredentials):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ErrorResponse, InstallVOneServerOnDiscoveryComputerResponse200]]
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
    body: VOneDeploymentConfigurationWithCredentials,
    x_request_id: Union[Unset, UUID] = UNSET,
    x_client_version: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, ErrorResponse, InstallVOneServerOnDiscoveryComputerResponse200]]:
    """Install Veeam ONE on Discovered Computer

     Installs Veeam ONE and management agent on a discovered computer with the specified UID.
    > Deploys only the missing component if the other one is already installed.
    > To track the deployment progress, you can use the `WaitDeploymentTask` operation.

    Args:
        computer_uid (UUID):
        x_request_id (Union[Unset, UUID]):
        x_client_version (Union[Unset, str]):
        body (VOneDeploymentConfigurationWithCredentials):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ErrorResponse, InstallVOneServerOnDiscoveryComputerResponse200]
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
    body: VOneDeploymentConfigurationWithCredentials,
    x_request_id: Union[Unset, UUID] = UNSET,
    x_client_version: Union[Unset, str] = UNSET,
) -> Response[Union[Any, ErrorResponse, InstallVOneServerOnDiscoveryComputerResponse200]]:
    """Install Veeam ONE on Discovered Computer

     Installs Veeam ONE and management agent on a discovered computer with the specified UID.
    > Deploys only the missing component if the other one is already installed.
    > To track the deployment progress, you can use the `WaitDeploymentTask` operation.

    Args:
        computer_uid (UUID):
        x_request_id (Union[Unset, UUID]):
        x_client_version (Union[Unset, str]):
        body (VOneDeploymentConfigurationWithCredentials):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ErrorResponse, InstallVOneServerOnDiscoveryComputerResponse200]]
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
    body: VOneDeploymentConfigurationWithCredentials,
    x_request_id: Union[Unset, UUID] = UNSET,
    x_client_version: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, ErrorResponse, InstallVOneServerOnDiscoveryComputerResponse200]]:
    """Install Veeam ONE on Discovered Computer

     Installs Veeam ONE and management agent on a discovered computer with the specified UID.
    > Deploys only the missing component if the other one is already installed.
    > To track the deployment progress, you can use the `WaitDeploymentTask` operation.

    Args:
        computer_uid (UUID):
        x_request_id (Union[Unset, UUID]):
        x_client_version (Union[Unset, str]):
        body (VOneDeploymentConfigurationWithCredentials):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ErrorResponse, InstallVOneServerOnDiscoveryComputerResponse200]
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
