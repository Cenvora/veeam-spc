from http import HTTPStatus
from typing import Any, Optional, Union, cast
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.get_vb_365_microsoft_365_organization_response_200 import GetVb365Microsoft365OrganizationResponse200
from ...models.vb_365_microsoft_365_organization_expand import Vb365Microsoft365OrganizationExpand
from ...types import UNSET, Response, Unset


def _get_kwargs(
    vb_365_server_uid: UUID,
    vb_365_organization_uid: UUID,
    *,
    expand: Union[Unset, list[Vb365Microsoft365OrganizationExpand]] = UNSET,
    x_request_id: Union[Unset, UUID] = UNSET,
    x_client_version: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_request_id, Unset):
        headers["X-Request-id"] = x_request_id

    if not isinstance(x_client_version, Unset):
        headers["X-Client-Version"] = x_client_version

    params: dict[str, Any] = {}

    json_expand: Union[Unset, list[str]] = UNSET
    if not isinstance(expand, Unset):
        json_expand = []
        for expand_item_data in expand:
            expand_item = expand_item_data.value
            json_expand.append(expand_item)

    params["expand"] = json_expand

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/infrastructure/vb365Servers/{vb_365_server_uid}/organizations/Microsoft365/{vb_365_organization_uid}",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Union[Any, ErrorResponse, GetVb365Microsoft365OrganizationResponse200]:
    if response.status_code == 200:
        response_200 = GetVb365Microsoft365OrganizationResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 202:
        response_202 = cast(Any, None)
        return response_202

    response_default = ErrorResponse.from_dict(response.json())

    return response_default


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, ErrorResponse, GetVb365Microsoft365OrganizationResponse200]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    vb_365_server_uid: UUID,
    vb_365_organization_uid: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
    expand: Union[Unset, list[Vb365Microsoft365OrganizationExpand]] = UNSET,
    x_request_id: Union[Unset, UUID] = UNSET,
    x_client_version: Union[Unset, str] = UNSET,
) -> Response[Union[Any, ErrorResponse, GetVb365Microsoft365OrganizationResponse200]]:
    """Get Microsoft 365 Organization

     Returns a resource representation of a Microsoft 365 organization with the specified UID.

    Args:
        vb_365_server_uid (UUID):
        vb_365_organization_uid (UUID):
        expand (Union[Unset, list[Vb365Microsoft365OrganizationExpand]]):
        x_request_id (Union[Unset, UUID]):
        x_client_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ErrorResponse, GetVb365Microsoft365OrganizationResponse200]]
    """

    kwargs = _get_kwargs(
        vb_365_server_uid=vb_365_server_uid,
        vb_365_organization_uid=vb_365_organization_uid,
        expand=expand,
        x_request_id=x_request_id,
        x_client_version=x_client_version,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    vb_365_server_uid: UUID,
    vb_365_organization_uid: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
    expand: Union[Unset, list[Vb365Microsoft365OrganizationExpand]] = UNSET,
    x_request_id: Union[Unset, UUID] = UNSET,
    x_client_version: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, ErrorResponse, GetVb365Microsoft365OrganizationResponse200]]:
    """Get Microsoft 365 Organization

     Returns a resource representation of a Microsoft 365 organization with the specified UID.

    Args:
        vb_365_server_uid (UUID):
        vb_365_organization_uid (UUID):
        expand (Union[Unset, list[Vb365Microsoft365OrganizationExpand]]):
        x_request_id (Union[Unset, UUID]):
        x_client_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ErrorResponse, GetVb365Microsoft365OrganizationResponse200]
    """

    return sync_detailed(
        vb_365_server_uid=vb_365_server_uid,
        vb_365_organization_uid=vb_365_organization_uid,
        client=client,
        expand=expand,
        x_request_id=x_request_id,
        x_client_version=x_client_version,
    ).parsed


async def asyncio_detailed(
    vb_365_server_uid: UUID,
    vb_365_organization_uid: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
    expand: Union[Unset, list[Vb365Microsoft365OrganizationExpand]] = UNSET,
    x_request_id: Union[Unset, UUID] = UNSET,
    x_client_version: Union[Unset, str] = UNSET,
) -> Response[Union[Any, ErrorResponse, GetVb365Microsoft365OrganizationResponse200]]:
    """Get Microsoft 365 Organization

     Returns a resource representation of a Microsoft 365 organization with the specified UID.

    Args:
        vb_365_server_uid (UUID):
        vb_365_organization_uid (UUID):
        expand (Union[Unset, list[Vb365Microsoft365OrganizationExpand]]):
        x_request_id (Union[Unset, UUID]):
        x_client_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ErrorResponse, GetVb365Microsoft365OrganizationResponse200]]
    """

    kwargs = _get_kwargs(
        vb_365_server_uid=vb_365_server_uid,
        vb_365_organization_uid=vb_365_organization_uid,
        expand=expand,
        x_request_id=x_request_id,
        x_client_version=x_client_version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    vb_365_server_uid: UUID,
    vb_365_organization_uid: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
    expand: Union[Unset, list[Vb365Microsoft365OrganizationExpand]] = UNSET,
    x_request_id: Union[Unset, UUID] = UNSET,
    x_client_version: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, ErrorResponse, GetVb365Microsoft365OrganizationResponse200]]:
    """Get Microsoft 365 Organization

     Returns a resource representation of a Microsoft 365 organization with the specified UID.

    Args:
        vb_365_server_uid (UUID):
        vb_365_organization_uid (UUID):
        expand (Union[Unset, list[Vb365Microsoft365OrganizationExpand]]):
        x_request_id (Union[Unset, UUID]):
        x_client_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ErrorResponse, GetVb365Microsoft365OrganizationResponse200]
    """

    return (
        await asyncio_detailed(
            vb_365_server_uid=vb_365_server_uid,
            vb_365_organization_uid=vb_365_organization_uid,
            client=client,
            expand=expand,
            x_request_id=x_request_id,
            x_client_version=x_client_version,
        )
    ).parsed
