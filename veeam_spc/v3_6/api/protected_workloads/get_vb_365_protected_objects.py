from http import HTTPStatus
from typing import Any, Optional, Union, cast
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.get_vb_365_protected_objects_order_direction import GetVb365ProtectedObjectsOrderDirection
from ...models.get_vb_365_protected_objects_response_200 import GetVb365ProtectedObjectsResponse200
from ...models.vb_365_protected_object_type import Vb365ProtectedObjectType
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    order_by: Union[Unset, str] = UNSET,
    order_direction: Union[
        Unset, GetVb365ProtectedObjectsOrderDirection
    ] = GetVb365ProtectedObjectsOrderDirection.ASCENDING,
    object_name_filter: Union[Unset, str] = UNSET,
    object_type_filter: Union[Unset, list[Vb365ProtectedObjectType]] = UNSET,
    skip_cache: Union[Unset, bool] = UNSET,
    limit: Union[Unset, int] = 100,
    offset: Union[Unset, int] = 0,
    site_filter: Union[Unset, list[UUID]] = UNSET,
    organization_filter: Union[Unset, UUID] = UNSET,
    location_filter: Union[Unset, UUID] = UNSET,
    x_request_id: Union[Unset, UUID] = UNSET,
    x_client_version: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_request_id, Unset):
        headers["X-Request-id"] = x_request_id

    if not isinstance(x_client_version, Unset):
        headers["X-Client-Version"] = x_client_version

    params: dict[str, Any] = {}

    params["orderBy"] = order_by

    json_order_direction: Union[Unset, str] = UNSET
    if not isinstance(order_direction, Unset):
        json_order_direction = order_direction.value

    params["orderDirection"] = json_order_direction

    params["objectNameFilter"] = object_name_filter

    json_object_type_filter: Union[Unset, list[str]] = UNSET
    if not isinstance(object_type_filter, Unset):
        json_object_type_filter = []
        for object_type_filter_item_data in object_type_filter:
            object_type_filter_item = object_type_filter_item_data.value
            json_object_type_filter.append(object_type_filter_item)

    params["objectTypeFilter"] = json_object_type_filter

    params["skipCache"] = skip_cache

    params["limit"] = limit

    params["offset"] = offset

    json_site_filter: Union[Unset, list[str]] = UNSET
    if not isinstance(site_filter, Unset):
        json_site_filter = []
        for site_filter_item_data in site_filter:
            site_filter_item = str(site_filter_item_data)
            json_site_filter.append(site_filter_item)

    params["siteFilter"] = json_site_filter

    json_organization_filter: Union[Unset, str] = UNSET
    if not isinstance(organization_filter, Unset):
        json_organization_filter = str(organization_filter)
    params["organizationFilter"] = json_organization_filter

    json_location_filter: Union[Unset, str] = UNSET
    if not isinstance(location_filter, Unset):
        json_location_filter = str(location_filter)
    params["locationFilter"] = json_location_filter

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/protectedWorkloads/vb365ProtectedObjects",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Union[Any, ErrorResponse, GetVb365ProtectedObjectsResponse200]:
    if response.status_code == 200:
        response_200 = GetVb365ProtectedObjectsResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 202:
        response_202 = cast(Any, None)
        return response_202

    response_default = ErrorResponse.from_dict(response.json())

    return response_default


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, ErrorResponse, GetVb365ProtectedObjectsResponse200]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    order_by: Union[Unset, str] = UNSET,
    order_direction: Union[
        Unset, GetVb365ProtectedObjectsOrderDirection
    ] = GetVb365ProtectedObjectsOrderDirection.ASCENDING,
    object_name_filter: Union[Unset, str] = UNSET,
    object_type_filter: Union[Unset, list[Vb365ProtectedObjectType]] = UNSET,
    skip_cache: Union[Unset, bool] = UNSET,
    limit: Union[Unset, int] = 100,
    offset: Union[Unset, int] = 0,
    site_filter: Union[Unset, list[UUID]] = UNSET,
    organization_filter: Union[Unset, UUID] = UNSET,
    location_filter: Union[Unset, UUID] = UNSET,
    x_request_id: Union[Unset, UUID] = UNSET,
    x_client_version: Union[Unset, str] = UNSET,
) -> Response[Union[Any, ErrorResponse, GetVb365ProtectedObjectsResponse200]]:
    """Get All Objects Protected by Veeam Backup for Microsoft 365

     Returns a collection resource representation of all objects protected by Veeam Backup for Microsoft
    365.

    Args:
        order_by (Union[Unset, str]):
        order_direction (Union[Unset, GetVb365ProtectedObjectsOrderDirection]):  Default:
            GetVb365ProtectedObjectsOrderDirection.ASCENDING.
        object_name_filter (Union[Unset, str]):
        object_type_filter (Union[Unset, list[Vb365ProtectedObjectType]]):
        skip_cache (Union[Unset, bool]):
        limit (Union[Unset, int]):  Default: 100.
        offset (Union[Unset, int]):  Default: 0.
        site_filter (Union[Unset, list[UUID]]):
        organization_filter (Union[Unset, UUID]):
        location_filter (Union[Unset, UUID]):
        x_request_id (Union[Unset, UUID]):
        x_client_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ErrorResponse, GetVb365ProtectedObjectsResponse200]]
    """

    kwargs = _get_kwargs(
        order_by=order_by,
        order_direction=order_direction,
        object_name_filter=object_name_filter,
        object_type_filter=object_type_filter,
        skip_cache=skip_cache,
        limit=limit,
        offset=offset,
        site_filter=site_filter,
        organization_filter=organization_filter,
        location_filter=location_filter,
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
    order_by: Union[Unset, str] = UNSET,
    order_direction: Union[
        Unset, GetVb365ProtectedObjectsOrderDirection
    ] = GetVb365ProtectedObjectsOrderDirection.ASCENDING,
    object_name_filter: Union[Unset, str] = UNSET,
    object_type_filter: Union[Unset, list[Vb365ProtectedObjectType]] = UNSET,
    skip_cache: Union[Unset, bool] = UNSET,
    limit: Union[Unset, int] = 100,
    offset: Union[Unset, int] = 0,
    site_filter: Union[Unset, list[UUID]] = UNSET,
    organization_filter: Union[Unset, UUID] = UNSET,
    location_filter: Union[Unset, UUID] = UNSET,
    x_request_id: Union[Unset, UUID] = UNSET,
    x_client_version: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, ErrorResponse, GetVb365ProtectedObjectsResponse200]]:
    """Get All Objects Protected by Veeam Backup for Microsoft 365

     Returns a collection resource representation of all objects protected by Veeam Backup for Microsoft
    365.

    Args:
        order_by (Union[Unset, str]):
        order_direction (Union[Unset, GetVb365ProtectedObjectsOrderDirection]):  Default:
            GetVb365ProtectedObjectsOrderDirection.ASCENDING.
        object_name_filter (Union[Unset, str]):
        object_type_filter (Union[Unset, list[Vb365ProtectedObjectType]]):
        skip_cache (Union[Unset, bool]):
        limit (Union[Unset, int]):  Default: 100.
        offset (Union[Unset, int]):  Default: 0.
        site_filter (Union[Unset, list[UUID]]):
        organization_filter (Union[Unset, UUID]):
        location_filter (Union[Unset, UUID]):
        x_request_id (Union[Unset, UUID]):
        x_client_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ErrorResponse, GetVb365ProtectedObjectsResponse200]
    """

    return sync_detailed(
        client=client,
        order_by=order_by,
        order_direction=order_direction,
        object_name_filter=object_name_filter,
        object_type_filter=object_type_filter,
        skip_cache=skip_cache,
        limit=limit,
        offset=offset,
        site_filter=site_filter,
        organization_filter=organization_filter,
        location_filter=location_filter,
        x_request_id=x_request_id,
        x_client_version=x_client_version,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    order_by: Union[Unset, str] = UNSET,
    order_direction: Union[
        Unset, GetVb365ProtectedObjectsOrderDirection
    ] = GetVb365ProtectedObjectsOrderDirection.ASCENDING,
    object_name_filter: Union[Unset, str] = UNSET,
    object_type_filter: Union[Unset, list[Vb365ProtectedObjectType]] = UNSET,
    skip_cache: Union[Unset, bool] = UNSET,
    limit: Union[Unset, int] = 100,
    offset: Union[Unset, int] = 0,
    site_filter: Union[Unset, list[UUID]] = UNSET,
    organization_filter: Union[Unset, UUID] = UNSET,
    location_filter: Union[Unset, UUID] = UNSET,
    x_request_id: Union[Unset, UUID] = UNSET,
    x_client_version: Union[Unset, str] = UNSET,
) -> Response[Union[Any, ErrorResponse, GetVb365ProtectedObjectsResponse200]]:
    """Get All Objects Protected by Veeam Backup for Microsoft 365

     Returns a collection resource representation of all objects protected by Veeam Backup for Microsoft
    365.

    Args:
        order_by (Union[Unset, str]):
        order_direction (Union[Unset, GetVb365ProtectedObjectsOrderDirection]):  Default:
            GetVb365ProtectedObjectsOrderDirection.ASCENDING.
        object_name_filter (Union[Unset, str]):
        object_type_filter (Union[Unset, list[Vb365ProtectedObjectType]]):
        skip_cache (Union[Unset, bool]):
        limit (Union[Unset, int]):  Default: 100.
        offset (Union[Unset, int]):  Default: 0.
        site_filter (Union[Unset, list[UUID]]):
        organization_filter (Union[Unset, UUID]):
        location_filter (Union[Unset, UUID]):
        x_request_id (Union[Unset, UUID]):
        x_client_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ErrorResponse, GetVb365ProtectedObjectsResponse200]]
    """

    kwargs = _get_kwargs(
        order_by=order_by,
        order_direction=order_direction,
        object_name_filter=object_name_filter,
        object_type_filter=object_type_filter,
        skip_cache=skip_cache,
        limit=limit,
        offset=offset,
        site_filter=site_filter,
        organization_filter=organization_filter,
        location_filter=location_filter,
        x_request_id=x_request_id,
        x_client_version=x_client_version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    order_by: Union[Unset, str] = UNSET,
    order_direction: Union[
        Unset, GetVb365ProtectedObjectsOrderDirection
    ] = GetVb365ProtectedObjectsOrderDirection.ASCENDING,
    object_name_filter: Union[Unset, str] = UNSET,
    object_type_filter: Union[Unset, list[Vb365ProtectedObjectType]] = UNSET,
    skip_cache: Union[Unset, bool] = UNSET,
    limit: Union[Unset, int] = 100,
    offset: Union[Unset, int] = 0,
    site_filter: Union[Unset, list[UUID]] = UNSET,
    organization_filter: Union[Unset, UUID] = UNSET,
    location_filter: Union[Unset, UUID] = UNSET,
    x_request_id: Union[Unset, UUID] = UNSET,
    x_client_version: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, ErrorResponse, GetVb365ProtectedObjectsResponse200]]:
    """Get All Objects Protected by Veeam Backup for Microsoft 365

     Returns a collection resource representation of all objects protected by Veeam Backup for Microsoft
    365.

    Args:
        order_by (Union[Unset, str]):
        order_direction (Union[Unset, GetVb365ProtectedObjectsOrderDirection]):  Default:
            GetVb365ProtectedObjectsOrderDirection.ASCENDING.
        object_name_filter (Union[Unset, str]):
        object_type_filter (Union[Unset, list[Vb365ProtectedObjectType]]):
        skip_cache (Union[Unset, bool]):
        limit (Union[Unset, int]):  Default: 100.
        offset (Union[Unset, int]):  Default: 0.
        site_filter (Union[Unset, list[UUID]]):
        organization_filter (Union[Unset, UUID]):
        location_filter (Union[Unset, UUID]):
        x_request_id (Union[Unset, UUID]):
        x_client_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ErrorResponse, GetVb365ProtectedObjectsResponse200]
    """

    return (
        await asyncio_detailed(
            client=client,
            order_by=order_by,
            order_direction=order_direction,
            object_name_filter=object_name_filter,
            object_type_filter=object_type_filter,
            skip_cache=skip_cache,
            limit=limit,
            offset=offset,
            site_filter=site_filter,
            organization_filter=organization_filter,
            location_filter=location_filter,
            x_request_id=x_request_id,
            x_client_version=x_client_version,
        )
    ).parsed
