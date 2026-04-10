from http import HTTPStatus
from typing import Any, Optional, Union, cast
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.get_backup_server_deployment_configuration_xml_backup_server_deployment_type import (
    GetBackupServerDeploymentConfigurationXmlBackupServerDeploymentType,
)
from ...models.get_backup_server_deployment_configuration_xml_response_200 import (
    GetBackupServerDeploymentConfigurationXmlResponse200,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    backup_server_deployment_type: GetBackupServerDeploymentConfigurationXmlBackupServerDeploymentType,
    management_agent_uid: Union[None, UUID, Unset] = UNSET,
    escape_characters: Union[Unset, bool] = False,
    x_request_id: Union[Unset, UUID] = UNSET,
    x_client_version: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_request_id, Unset):
        headers["X-Request-id"] = x_request_id

    if not isinstance(x_client_version, Unset):
        headers["X-Client-Version"] = x_client_version

    params: dict[str, Any] = {}

    json_backup_server_deployment_type = backup_server_deployment_type.value
    params["backupServerDeploymentType"] = json_backup_server_deployment_type

    json_management_agent_uid: Union[None, Unset, str]
    if isinstance(management_agent_uid, Unset):
        json_management_agent_uid = UNSET
    elif isinstance(management_agent_uid, UUID):
        json_management_agent_uid = str(management_agent_uid)
    else:
        json_management_agent_uid = management_agent_uid
    params["managementAgentUid"] = json_management_agent_uid

    params["escapeCharacters"] = escape_characters

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/deployment/deploy/backupServers/configuration/xml",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Union[Any, ErrorResponse, GetBackupServerDeploymentConfigurationXmlResponse200]:
    if response.status_code == 200:
        response_200 = GetBackupServerDeploymentConfigurationXmlResponse200.from_dict(response.content)

        return response_200

    if response.status_code == 202:
        response_202 = cast(Any, None)
        return response_202

    response_default = ErrorResponse.from_dict(response.json())

    return response_default


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, ErrorResponse, GetBackupServerDeploymentConfigurationXmlResponse200]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    backup_server_deployment_type: GetBackupServerDeploymentConfigurationXmlBackupServerDeploymentType,
    management_agent_uid: Union[None, UUID, Unset] = UNSET,
    escape_characters: Union[Unset, bool] = False,
    x_request_id: Union[Unset, UUID] = UNSET,
    x_client_version: Union[Unset, str] = UNSET,
) -> Response[Union[Any, ErrorResponse, GetBackupServerDeploymentConfigurationXmlResponse200]]:
    """Get Example for Veeam Backup & Replication Server Deployment Configuration

     Returns a resource representation of an example for Veeam Backup & Replication server deployment
    configuration in the `XML` format.
    > Error response is returned in the `JSON` format.

    Args:
        backup_server_deployment_type
            (GetBackupServerDeploymentConfigurationXmlBackupServerDeploymentType):
        management_agent_uid (Union[None, UUID, Unset]):
        escape_characters (Union[Unset, bool]):  Default: False.
        x_request_id (Union[Unset, UUID]):
        x_client_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ErrorResponse, GetBackupServerDeploymentConfigurationXmlResponse200]]
    """

    kwargs = _get_kwargs(
        backup_server_deployment_type=backup_server_deployment_type,
        management_agent_uid=management_agent_uid,
        escape_characters=escape_characters,
        x_request_id=x_request_id,
        x_client_version=x_client_version,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    backup_server_deployment_type: GetBackupServerDeploymentConfigurationXmlBackupServerDeploymentType,
    management_agent_uid: Union[None, UUID, Unset] = UNSET,
    escape_characters: Union[Unset, bool] = False,
    x_request_id: Union[Unset, UUID] = UNSET,
    x_client_version: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, ErrorResponse, GetBackupServerDeploymentConfigurationXmlResponse200]]:
    """Get Example for Veeam Backup & Replication Server Deployment Configuration

     Returns a resource representation of an example for Veeam Backup & Replication server deployment
    configuration in the `XML` format.
    > Error response is returned in the `JSON` format.

    Args:
        backup_server_deployment_type
            (GetBackupServerDeploymentConfigurationXmlBackupServerDeploymentType):
        management_agent_uid (Union[None, UUID, Unset]):
        escape_characters (Union[Unset, bool]):  Default: False.
        x_request_id (Union[Unset, UUID]):
        x_client_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ErrorResponse, GetBackupServerDeploymentConfigurationXmlResponse200]
    """

    return sync_detailed(
        client=client,
        backup_server_deployment_type=backup_server_deployment_type,
        management_agent_uid=management_agent_uid,
        escape_characters=escape_characters,
        x_request_id=x_request_id,
        x_client_version=x_client_version,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    backup_server_deployment_type: GetBackupServerDeploymentConfigurationXmlBackupServerDeploymentType,
    management_agent_uid: Union[None, UUID, Unset] = UNSET,
    escape_characters: Union[Unset, bool] = False,
    x_request_id: Union[Unset, UUID] = UNSET,
    x_client_version: Union[Unset, str] = UNSET,
) -> Response[Union[Any, ErrorResponse, GetBackupServerDeploymentConfigurationXmlResponse200]]:
    """Get Example for Veeam Backup & Replication Server Deployment Configuration

     Returns a resource representation of an example for Veeam Backup & Replication server deployment
    configuration in the `XML` format.
    > Error response is returned in the `JSON` format.

    Args:
        backup_server_deployment_type
            (GetBackupServerDeploymentConfigurationXmlBackupServerDeploymentType):
        management_agent_uid (Union[None, UUID, Unset]):
        escape_characters (Union[Unset, bool]):  Default: False.
        x_request_id (Union[Unset, UUID]):
        x_client_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ErrorResponse, GetBackupServerDeploymentConfigurationXmlResponse200]]
    """

    kwargs = _get_kwargs(
        backup_server_deployment_type=backup_server_deployment_type,
        management_agent_uid=management_agent_uid,
        escape_characters=escape_characters,
        x_request_id=x_request_id,
        x_client_version=x_client_version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    backup_server_deployment_type: GetBackupServerDeploymentConfigurationXmlBackupServerDeploymentType,
    management_agent_uid: Union[None, UUID, Unset] = UNSET,
    escape_characters: Union[Unset, bool] = False,
    x_request_id: Union[Unset, UUID] = UNSET,
    x_client_version: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, ErrorResponse, GetBackupServerDeploymentConfigurationXmlResponse200]]:
    """Get Example for Veeam Backup & Replication Server Deployment Configuration

     Returns a resource representation of an example for Veeam Backup & Replication server deployment
    configuration in the `XML` format.
    > Error response is returned in the `JSON` format.

    Args:
        backup_server_deployment_type
            (GetBackupServerDeploymentConfigurationXmlBackupServerDeploymentType):
        management_agent_uid (Union[None, UUID, Unset]):
        escape_characters (Union[Unset, bool]):  Default: False.
        x_request_id (Union[Unset, UUID]):
        x_client_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ErrorResponse, GetBackupServerDeploymentConfigurationXmlResponse200]
    """

    return (
        await asyncio_detailed(
            client=client,
            backup_server_deployment_type=backup_server_deployment_type,
            management_agent_uid=management_agent_uid,
            escape_characters=escape_characters,
            x_request_id=x_request_id,
            x_client_version=x_client_version,
        )
    ).parsed
