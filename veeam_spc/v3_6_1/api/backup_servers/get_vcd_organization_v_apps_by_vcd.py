from http import HTTPStatus
from typing import Any, Optional, Union, cast
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.get_vcd_organization_v_apps_by_vcd_name_sorting_direction import (
    GetVcdOrganizationVAppsByVcdNameSortingDirection,
)
from ...models.get_vcd_organization_v_apps_by_vcd_response_200 import GetVcdOrganizationVAppsByVcdResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    backup_server_uid: UUID,
    vcd_server_uid: UUID,
    *,
    company_uid: Union[None, UUID, Unset] = UNSET,
    name_filter: Union[None, Unset, str] = UNSET,
    vcd_organization_uid_filter: Union[None, UUID, Unset] = UNSET,
    name_sorting_direction: Union[
        Unset, GetVcdOrganizationVAppsByVcdNameSortingDirection
    ] = GetVcdOrganizationVAppsByVcdNameSortingDirection.ASCENDING,
    limit: Union[Unset, int] = 100,
    offset: Union[Unset, int] = 0,
    x_request_id: Union[Unset, UUID] = UNSET,
    x_client_version: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_request_id, Unset):
        headers["X-Request-id"] = x_request_id

    if not isinstance(x_client_version, Unset):
        headers["X-Client-Version"] = x_client_version

    params: dict[str, Any] = {}

    json_company_uid: Union[None, Unset, str]
    if isinstance(company_uid, Unset):
        json_company_uid = UNSET
    elif isinstance(company_uid, UUID):
        json_company_uid = str(company_uid)
    else:
        json_company_uid = company_uid
    params["companyUid"] = json_company_uid

    json_name_filter: Union[None, Unset, str]
    if isinstance(name_filter, Unset):
        json_name_filter = UNSET
    else:
        json_name_filter = name_filter
    params["nameFilter"] = json_name_filter

    json_vcd_organization_uid_filter: Union[None, Unset, str]
    if isinstance(vcd_organization_uid_filter, Unset):
        json_vcd_organization_uid_filter = UNSET
    elif isinstance(vcd_organization_uid_filter, UUID):
        json_vcd_organization_uid_filter = str(vcd_organization_uid_filter)
    else:
        json_vcd_organization_uid_filter = vcd_organization_uid_filter
    params["vcdOrganizationUidFilter"] = json_vcd_organization_uid_filter

    json_name_sorting_direction: Union[Unset, str] = UNSET
    if not isinstance(name_sorting_direction, Unset):
        json_name_sorting_direction = name_sorting_direction.value

    params["nameSortingDirection"] = json_name_sorting_direction

    params["limit"] = limit

    params["offset"] = offset

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/infrastructure/backupServers/{backup_server_uid}/vcdServers/{vcd_server_uid}/vcdOrganizations/vDCs/vApps",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Union[Any, ErrorResponse, GetVcdOrganizationVAppsByVcdResponse200]:
    if response.status_code == 200:
        response_200 = GetVcdOrganizationVAppsByVcdResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 202:
        response_202 = cast(Any, None)
        return response_202

    response_default = ErrorResponse.from_dict(response.json())

    return response_default


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, ErrorResponse, GetVcdOrganizationVAppsByVcdResponse200]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    backup_server_uid: UUID,
    vcd_server_uid: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
    company_uid: Union[None, UUID, Unset] = UNSET,
    name_filter: Union[None, Unset, str] = UNSET,
    vcd_organization_uid_filter: Union[None, UUID, Unset] = UNSET,
    name_sorting_direction: Union[
        Unset, GetVcdOrganizationVAppsByVcdNameSortingDirection
    ] = GetVcdOrganizationVAppsByVcdNameSortingDirection.ASCENDING,
    limit: Union[Unset, int] = 100,
    offset: Union[Unset, int] = 0,
    x_request_id: Union[Unset, UUID] = UNSET,
    x_client_version: Union[Unset, str] = UNSET,
) -> Response[Union[Any, ErrorResponse, GetVcdOrganizationVAppsByVcdResponse200]]:
    """Get vApps Configured on VMware Cloud Director Server

     Returns a collection resource representation of all vApps configured on a VMware Cloud Director
    server with the specified UID.

    Args:
        backup_server_uid (UUID):
        vcd_server_uid (UUID):
        company_uid (Union[None, UUID, Unset]):
        name_filter (Union[None, Unset, str]):
        vcd_organization_uid_filter (Union[None, UUID, Unset]):
        name_sorting_direction (Union[Unset, GetVcdOrganizationVAppsByVcdNameSortingDirection]):
            Default: GetVcdOrganizationVAppsByVcdNameSortingDirection.ASCENDING.
        limit (Union[Unset, int]):  Default: 100.
        offset (Union[Unset, int]):  Default: 0.
        x_request_id (Union[Unset, UUID]):
        x_client_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ErrorResponse, GetVcdOrganizationVAppsByVcdResponse200]]
    """

    kwargs = _get_kwargs(
        backup_server_uid=backup_server_uid,
        vcd_server_uid=vcd_server_uid,
        company_uid=company_uid,
        name_filter=name_filter,
        vcd_organization_uid_filter=vcd_organization_uid_filter,
        name_sorting_direction=name_sorting_direction,
        limit=limit,
        offset=offset,
        x_request_id=x_request_id,
        x_client_version=x_client_version,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    backup_server_uid: UUID,
    vcd_server_uid: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
    company_uid: Union[None, UUID, Unset] = UNSET,
    name_filter: Union[None, Unset, str] = UNSET,
    vcd_organization_uid_filter: Union[None, UUID, Unset] = UNSET,
    name_sorting_direction: Union[
        Unset, GetVcdOrganizationVAppsByVcdNameSortingDirection
    ] = GetVcdOrganizationVAppsByVcdNameSortingDirection.ASCENDING,
    limit: Union[Unset, int] = 100,
    offset: Union[Unset, int] = 0,
    x_request_id: Union[Unset, UUID] = UNSET,
    x_client_version: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, ErrorResponse, GetVcdOrganizationVAppsByVcdResponse200]]:
    """Get vApps Configured on VMware Cloud Director Server

     Returns a collection resource representation of all vApps configured on a VMware Cloud Director
    server with the specified UID.

    Args:
        backup_server_uid (UUID):
        vcd_server_uid (UUID):
        company_uid (Union[None, UUID, Unset]):
        name_filter (Union[None, Unset, str]):
        vcd_organization_uid_filter (Union[None, UUID, Unset]):
        name_sorting_direction (Union[Unset, GetVcdOrganizationVAppsByVcdNameSortingDirection]):
            Default: GetVcdOrganizationVAppsByVcdNameSortingDirection.ASCENDING.
        limit (Union[Unset, int]):  Default: 100.
        offset (Union[Unset, int]):  Default: 0.
        x_request_id (Union[Unset, UUID]):
        x_client_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ErrorResponse, GetVcdOrganizationVAppsByVcdResponse200]
    """

    return sync_detailed(
        backup_server_uid=backup_server_uid,
        vcd_server_uid=vcd_server_uid,
        client=client,
        company_uid=company_uid,
        name_filter=name_filter,
        vcd_organization_uid_filter=vcd_organization_uid_filter,
        name_sorting_direction=name_sorting_direction,
        limit=limit,
        offset=offset,
        x_request_id=x_request_id,
        x_client_version=x_client_version,
    ).parsed


async def asyncio_detailed(
    backup_server_uid: UUID,
    vcd_server_uid: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
    company_uid: Union[None, UUID, Unset] = UNSET,
    name_filter: Union[None, Unset, str] = UNSET,
    vcd_organization_uid_filter: Union[None, UUID, Unset] = UNSET,
    name_sorting_direction: Union[
        Unset, GetVcdOrganizationVAppsByVcdNameSortingDirection
    ] = GetVcdOrganizationVAppsByVcdNameSortingDirection.ASCENDING,
    limit: Union[Unset, int] = 100,
    offset: Union[Unset, int] = 0,
    x_request_id: Union[Unset, UUID] = UNSET,
    x_client_version: Union[Unset, str] = UNSET,
) -> Response[Union[Any, ErrorResponse, GetVcdOrganizationVAppsByVcdResponse200]]:
    """Get vApps Configured on VMware Cloud Director Server

     Returns a collection resource representation of all vApps configured on a VMware Cloud Director
    server with the specified UID.

    Args:
        backup_server_uid (UUID):
        vcd_server_uid (UUID):
        company_uid (Union[None, UUID, Unset]):
        name_filter (Union[None, Unset, str]):
        vcd_organization_uid_filter (Union[None, UUID, Unset]):
        name_sorting_direction (Union[Unset, GetVcdOrganizationVAppsByVcdNameSortingDirection]):
            Default: GetVcdOrganizationVAppsByVcdNameSortingDirection.ASCENDING.
        limit (Union[Unset, int]):  Default: 100.
        offset (Union[Unset, int]):  Default: 0.
        x_request_id (Union[Unset, UUID]):
        x_client_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ErrorResponse, GetVcdOrganizationVAppsByVcdResponse200]]
    """

    kwargs = _get_kwargs(
        backup_server_uid=backup_server_uid,
        vcd_server_uid=vcd_server_uid,
        company_uid=company_uid,
        name_filter=name_filter,
        vcd_organization_uid_filter=vcd_organization_uid_filter,
        name_sorting_direction=name_sorting_direction,
        limit=limit,
        offset=offset,
        x_request_id=x_request_id,
        x_client_version=x_client_version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    backup_server_uid: UUID,
    vcd_server_uid: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
    company_uid: Union[None, UUID, Unset] = UNSET,
    name_filter: Union[None, Unset, str] = UNSET,
    vcd_organization_uid_filter: Union[None, UUID, Unset] = UNSET,
    name_sorting_direction: Union[
        Unset, GetVcdOrganizationVAppsByVcdNameSortingDirection
    ] = GetVcdOrganizationVAppsByVcdNameSortingDirection.ASCENDING,
    limit: Union[Unset, int] = 100,
    offset: Union[Unset, int] = 0,
    x_request_id: Union[Unset, UUID] = UNSET,
    x_client_version: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, ErrorResponse, GetVcdOrganizationVAppsByVcdResponse200]]:
    """Get vApps Configured on VMware Cloud Director Server

     Returns a collection resource representation of all vApps configured on a VMware Cloud Director
    server with the specified UID.

    Args:
        backup_server_uid (UUID):
        vcd_server_uid (UUID):
        company_uid (Union[None, UUID, Unset]):
        name_filter (Union[None, Unset, str]):
        vcd_organization_uid_filter (Union[None, UUID, Unset]):
        name_sorting_direction (Union[Unset, GetVcdOrganizationVAppsByVcdNameSortingDirection]):
            Default: GetVcdOrganizationVAppsByVcdNameSortingDirection.ASCENDING.
        limit (Union[Unset, int]):  Default: 100.
        offset (Union[Unset, int]):  Default: 0.
        x_request_id (Union[Unset, UUID]):
        x_client_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ErrorResponse, GetVcdOrganizationVAppsByVcdResponse200]
    """

    return (
        await asyncio_detailed(
            backup_server_uid=backup_server_uid,
            vcd_server_uid=vcd_server_uid,
            client=client,
            company_uid=company_uid,
            name_filter=name_filter,
            vcd_organization_uid_filter=vcd_organization_uid_filter,
            name_sorting_direction=name_sorting_direction,
            limit=limit,
            offset=offset,
            x_request_id=x_request_id,
            x_client_version=x_client_version,
        )
    ).parsed
