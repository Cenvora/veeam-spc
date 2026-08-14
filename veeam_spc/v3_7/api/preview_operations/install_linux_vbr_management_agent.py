from http import HTTPStatus
from typing import Any, cast
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.install_linux_vbr_management_agent_response_200 import InstallLinuxVbrManagementAgentResponse200
from ...models.linux_vbr_management_agent_installation_configuration import (
    LinuxVbrManagementAgentInstallationConfiguration,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: LinuxVbrManagementAgentInstallationConfiguration,
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
        "url": "/deployment/installLinuxVbrManagementAgent",
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | ErrorResponse | InstallLinuxVbrManagementAgentResponse200:
    if response.status_code == 200:
        response_200 = InstallLinuxVbrManagementAgentResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 202:
        response_202 = cast(Any, None)
        return response_202

    response_default = ErrorResponse.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | ErrorResponse | InstallLinuxVbrManagementAgentResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: LinuxVbrManagementAgentInstallationConfiguration,
    select: str | Unset = UNSET,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Response[Any | ErrorResponse | InstallLinuxVbrManagementAgentResponse200]:
    """Install Management Agent on Linux-Based Veeam Backup & Replication Server

     Installs a Veeam Service Provider Console management agent on an existing Linux-based Veeam Backup &
    Replication server. Cluster role of a server is determined automatically:
    * Standalone server -- management agent is registered as non-clustered.
    * High availability primary node -- management agent is registered as primary clustered.
    * High availability secondary node -- management agent is attached to an existing primary clustered
    management agent. If no primary clustered management agent is found, the operation returns an error
    with the `409 Conflict` code.

    Args:
        select (str | Unset):
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):
        body (LinuxVbrManagementAgentInstallationConfiguration):  Example: {'hostname': 'vbr-
            linux01.tech.local', 'port': 10006, 'trustedThumbprint':
            '9F86D081884C7D659A2FEAA0C55AD015A3BF4F1B', 'sshUsername': 'root', 'sshPassword':
            'P@ssw0rd123!', 'description': 'Linux VBR management agent deployed via VSPC'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ErrorResponse | InstallLinuxVbrManagementAgentResponse200]
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
    body: LinuxVbrManagementAgentInstallationConfiguration,
    select: str | Unset = UNSET,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Any | ErrorResponse | InstallLinuxVbrManagementAgentResponse200 | None:
    """Install Management Agent on Linux-Based Veeam Backup & Replication Server

     Installs a Veeam Service Provider Console management agent on an existing Linux-based Veeam Backup &
    Replication server. Cluster role of a server is determined automatically:
    * Standalone server -- management agent is registered as non-clustered.
    * High availability primary node -- management agent is registered as primary clustered.
    * High availability secondary node -- management agent is attached to an existing primary clustered
    management agent. If no primary clustered management agent is found, the operation returns an error
    with the `409 Conflict` code.

    Args:
        select (str | Unset):
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):
        body (LinuxVbrManagementAgentInstallationConfiguration):  Example: {'hostname': 'vbr-
            linux01.tech.local', 'port': 10006, 'trustedThumbprint':
            '9F86D081884C7D659A2FEAA0C55AD015A3BF4F1B', 'sshUsername': 'root', 'sshPassword':
            'P@ssw0rd123!', 'description': 'Linux VBR management agent deployed via VSPC'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ErrorResponse | InstallLinuxVbrManagementAgentResponse200
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
    body: LinuxVbrManagementAgentInstallationConfiguration,
    select: str | Unset = UNSET,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Response[Any | ErrorResponse | InstallLinuxVbrManagementAgentResponse200]:
    """Install Management Agent on Linux-Based Veeam Backup & Replication Server

     Installs a Veeam Service Provider Console management agent on an existing Linux-based Veeam Backup &
    Replication server. Cluster role of a server is determined automatically:
    * Standalone server -- management agent is registered as non-clustered.
    * High availability primary node -- management agent is registered as primary clustered.
    * High availability secondary node -- management agent is attached to an existing primary clustered
    management agent. If no primary clustered management agent is found, the operation returns an error
    with the `409 Conflict` code.

    Args:
        select (str | Unset):
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):
        body (LinuxVbrManagementAgentInstallationConfiguration):  Example: {'hostname': 'vbr-
            linux01.tech.local', 'port': 10006, 'trustedThumbprint':
            '9F86D081884C7D659A2FEAA0C55AD015A3BF4F1B', 'sshUsername': 'root', 'sshPassword':
            'P@ssw0rd123!', 'description': 'Linux VBR management agent deployed via VSPC'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ErrorResponse | InstallLinuxVbrManagementAgentResponse200]
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
    body: LinuxVbrManagementAgentInstallationConfiguration,
    select: str | Unset = UNSET,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Any | ErrorResponse | InstallLinuxVbrManagementAgentResponse200 | None:
    """Install Management Agent on Linux-Based Veeam Backup & Replication Server

     Installs a Veeam Service Provider Console management agent on an existing Linux-based Veeam Backup &
    Replication server. Cluster role of a server is determined automatically:
    * Standalone server -- management agent is registered as non-clustered.
    * High availability primary node -- management agent is registered as primary clustered.
    * High availability secondary node -- management agent is attached to an existing primary clustered
    management agent. If no primary clustered management agent is found, the operation returns an error
    with the `409 Conflict` code.

    Args:
        select (str | Unset):
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):
        body (LinuxVbrManagementAgentInstallationConfiguration):  Example: {'hostname': 'vbr-
            linux01.tech.local', 'port': 10006, 'trustedThumbprint':
            '9F86D081884C7D659A2FEAA0C55AD015A3BF4F1B', 'sshUsername': 'root', 'sshPassword':
            'P@ssw0rd123!', 'description': 'Linux VBR management agent deployed via VSPC'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ErrorResponse | InstallLinuxVbrManagementAgentResponse200
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
