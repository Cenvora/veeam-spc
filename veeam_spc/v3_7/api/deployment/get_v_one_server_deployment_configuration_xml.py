from http import HTTPStatus
from typing import Any, cast
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.get_v_one_server_deployment_configuration_xml_response_200 import (
    GetVOneServerDeploymentConfigurationXmlResponse200,
)
from ...models.get_v_one_server_deployment_configuration_xml_vone_server_deployment_type import (
    GetVOneServerDeploymentConfigurationXmlVoneServerDeploymentType,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    vone_server_deployment_type: GetVOneServerDeploymentConfigurationXmlVoneServerDeploymentType,
    management_agent_uid: UUID | Unset = UNSET,
    escape_characters: bool | Unset = False,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_request_id, Unset):
        headers["X-Request-id"] = x_request_id

    if not isinstance(x_client_version, Unset):
        headers["X-Client-Version"] = x_client_version

    params: dict[str, Any] = {}

    json_vone_server_deployment_type = vone_server_deployment_type.value
    params["voneServerDeploymentType"] = json_vone_server_deployment_type

    json_management_agent_uid: str | Unset = UNSET
    if not isinstance(management_agent_uid, Unset):
        json_management_agent_uid = str(management_agent_uid)
    params["managementAgentUid"] = json_management_agent_uid

    params["escapeCharacters"] = escape_characters

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/deployment/deploy/voneServers/configuration/xml",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | ErrorResponse | GetVOneServerDeploymentConfigurationXmlResponse200:
    if response.status_code == 200:
        response_200 = GetVOneServerDeploymentConfigurationXmlResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 202:
        response_202 = cast(Any, None)
        return response_202

    response_default = ErrorResponse.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | ErrorResponse | GetVOneServerDeploymentConfigurationXmlResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    vone_server_deployment_type: GetVOneServerDeploymentConfigurationXmlVoneServerDeploymentType,
    management_agent_uid: UUID | Unset = UNSET,
    escape_characters: bool | Unset = False,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Response[Any | ErrorResponse | GetVOneServerDeploymentConfigurationXmlResponse200]:
    """Get Example for Veeam ONE Server Deployment Configuration

     Returns a resource representation of an example for Veeam ONE server deployment configuration in the
    `XML` format.
    > Error response is returned in the `JSON` format.

    Args:
        vone_server_deployment_type
            (GetVOneServerDeploymentConfigurationXmlVoneServerDeploymentType):
        management_agent_uid (UUID | Unset):
        escape_characters (bool | Unset):  Default: False.
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ErrorResponse | GetVOneServerDeploymentConfigurationXmlResponse200]
    """

    kwargs = _get_kwargs(
        vone_server_deployment_type=vone_server_deployment_type,
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
    client: AuthenticatedClient,
    vone_server_deployment_type: GetVOneServerDeploymentConfigurationXmlVoneServerDeploymentType,
    management_agent_uid: UUID | Unset = UNSET,
    escape_characters: bool | Unset = False,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Any | ErrorResponse | GetVOneServerDeploymentConfigurationXmlResponse200 | None:
    """Get Example for Veeam ONE Server Deployment Configuration

     Returns a resource representation of an example for Veeam ONE server deployment configuration in the
    `XML` format.
    > Error response is returned in the `JSON` format.

    Args:
        vone_server_deployment_type
            (GetVOneServerDeploymentConfigurationXmlVoneServerDeploymentType):
        management_agent_uid (UUID | Unset):
        escape_characters (bool | Unset):  Default: False.
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ErrorResponse | GetVOneServerDeploymentConfigurationXmlResponse200
    """

    return sync_detailed(
        client=client,
        vone_server_deployment_type=vone_server_deployment_type,
        management_agent_uid=management_agent_uid,
        escape_characters=escape_characters,
        x_request_id=x_request_id,
        x_client_version=x_client_version,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    vone_server_deployment_type: GetVOneServerDeploymentConfigurationXmlVoneServerDeploymentType,
    management_agent_uid: UUID | Unset = UNSET,
    escape_characters: bool | Unset = False,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Response[Any | ErrorResponse | GetVOneServerDeploymentConfigurationXmlResponse200]:
    """Get Example for Veeam ONE Server Deployment Configuration

     Returns a resource representation of an example for Veeam ONE server deployment configuration in the
    `XML` format.
    > Error response is returned in the `JSON` format.

    Args:
        vone_server_deployment_type
            (GetVOneServerDeploymentConfigurationXmlVoneServerDeploymentType):
        management_agent_uid (UUID | Unset):
        escape_characters (bool | Unset):  Default: False.
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ErrorResponse | GetVOneServerDeploymentConfigurationXmlResponse200]
    """

    kwargs = _get_kwargs(
        vone_server_deployment_type=vone_server_deployment_type,
        management_agent_uid=management_agent_uid,
        escape_characters=escape_characters,
        x_request_id=x_request_id,
        x_client_version=x_client_version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    vone_server_deployment_type: GetVOneServerDeploymentConfigurationXmlVoneServerDeploymentType,
    management_agent_uid: UUID | Unset = UNSET,
    escape_characters: bool | Unset = False,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Any | ErrorResponse | GetVOneServerDeploymentConfigurationXmlResponse200 | None:
    """Get Example for Veeam ONE Server Deployment Configuration

     Returns a resource representation of an example for Veeam ONE server deployment configuration in the
    `XML` format.
    > Error response is returned in the `JSON` format.

    Args:
        vone_server_deployment_type
            (GetVOneServerDeploymentConfigurationXmlVoneServerDeploymentType):
        management_agent_uid (UUID | Unset):
        escape_characters (bool | Unset):  Default: False.
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ErrorResponse | GetVOneServerDeploymentConfigurationXmlResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            vone_server_deployment_type=vone_server_deployment_type,
            management_agent_uid=management_agent_uid,
            escape_characters=escape_characters,
            x_request_id=x_request_id,
            x_client_version=x_client_version,
        )
    ).parsed
