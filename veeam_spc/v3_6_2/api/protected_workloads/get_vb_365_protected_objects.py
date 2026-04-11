from http import HTTPStatus
from typing import Any, cast
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
    order_by: None | str | Unset = UNSET,
    order_direction: GetVb365ProtectedObjectsOrderDirection | Unset = GetVb365ProtectedObjectsOrderDirection.ASCENDING,
    object_name_filter: None | str | Unset = UNSET,
    object_type_filter: list[Vb365ProtectedObjectType] | None | Unset = UNSET,
    educational_filter: bool | None | Unset = UNSET,
    licensed_filter: bool | None | Unset = UNSET,
    skip_cache: bool | None | Unset = UNSET,
    limit: int | Unset = 100,
    offset: int | Unset = 0,
    site_filter: list[UUID] | None | Unset = UNSET,
    organization_filter: None | Unset | UUID = UNSET,
    location_filter: None | Unset | UUID = UNSET,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_request_id, Unset):
        headers["X-Request-id"] = x_request_id

    if not isinstance(x_client_version, Unset):
        headers["X-Client-Version"] = x_client_version

    params: dict[str, Any] = {}

    json_order_by: None | str | Unset
    if isinstance(order_by, Unset):
        json_order_by = UNSET
    else:
        json_order_by = order_by
    params["orderBy"] = json_order_by

    json_order_direction: str | Unset = UNSET
    if not isinstance(order_direction, Unset):
        json_order_direction = order_direction.value

    params["orderDirection"] = json_order_direction

    json_object_name_filter: None | str | Unset
    if isinstance(object_name_filter, Unset):
        json_object_name_filter = UNSET
    else:
        json_object_name_filter = object_name_filter
    params["objectNameFilter"] = json_object_name_filter

    json_object_type_filter: list[str] | None | Unset
    if isinstance(object_type_filter, Unset):
        json_object_type_filter = UNSET
    elif isinstance(object_type_filter, list):
        json_object_type_filter = []
        for object_type_filter_type_0_item_data in object_type_filter:
            object_type_filter_type_0_item = object_type_filter_type_0_item_data.value
            json_object_type_filter.append(object_type_filter_type_0_item)

    else:
        json_object_type_filter = object_type_filter
    params["objectTypeFilter"] = json_object_type_filter

    json_educational_filter: bool | None | Unset
    if isinstance(educational_filter, Unset):
        json_educational_filter = UNSET
    else:
        json_educational_filter = educational_filter
    params["educationalFilter"] = json_educational_filter

    json_licensed_filter: bool | None | Unset
    if isinstance(licensed_filter, Unset):
        json_licensed_filter = UNSET
    else:
        json_licensed_filter = licensed_filter
    params["licensedFilter"] = json_licensed_filter

    json_skip_cache: bool | None | Unset
    if isinstance(skip_cache, Unset):
        json_skip_cache = UNSET
    else:
        json_skip_cache = skip_cache
    params["skipCache"] = json_skip_cache

    params["limit"] = limit

    params["offset"] = offset

    json_site_filter: list[str] | None | Unset
    if isinstance(site_filter, Unset):
        json_site_filter = UNSET
    elif isinstance(site_filter, list):
        json_site_filter = []
        for site_filter_type_0_item_data in site_filter:
            site_filter_type_0_item = str(site_filter_type_0_item_data)
            json_site_filter.append(site_filter_type_0_item)

    else:
        json_site_filter = site_filter
    params["siteFilter"] = json_site_filter

    json_organization_filter: None | str | Unset
    if isinstance(organization_filter, Unset):
        json_organization_filter = UNSET
    elif isinstance(organization_filter, UUID):
        json_organization_filter = str(organization_filter)
    else:
        json_organization_filter = organization_filter
    params["organizationFilter"] = json_organization_filter

    json_location_filter: None | str | Unset
    if isinstance(location_filter, Unset):
        json_location_filter = UNSET
    elif isinstance(location_filter, UUID):
        json_location_filter = str(location_filter)
    else:
        json_location_filter = location_filter
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
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | ErrorResponse | GetVb365ProtectedObjectsResponse200:
    if response.status_code == 200:
        response_200 = GetVb365ProtectedObjectsResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 202:
        response_202 = cast(Any, None)
        return response_202

    response_default = ErrorResponse.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | ErrorResponse | GetVb365ProtectedObjectsResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    order_by: None | str | Unset = UNSET,
    order_direction: GetVb365ProtectedObjectsOrderDirection | Unset = GetVb365ProtectedObjectsOrderDirection.ASCENDING,
    object_name_filter: None | str | Unset = UNSET,
    object_type_filter: list[Vb365ProtectedObjectType] | None | Unset = UNSET,
    educational_filter: bool | None | Unset = UNSET,
    licensed_filter: bool | None | Unset = UNSET,
    skip_cache: bool | None | Unset = UNSET,
    limit: int | Unset = 100,
    offset: int | Unset = 0,
    site_filter: list[UUID] | None | Unset = UNSET,
    organization_filter: None | Unset | UUID = UNSET,
    location_filter: None | Unset | UUID = UNSET,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Response[Any | ErrorResponse | GetVb365ProtectedObjectsResponse200]:
    """Get All Objects Protected by Veeam Backup for Microsoft 365

     Returns a collection resource representation of all objects protected by Veeam Backup for Microsoft
    365.

    Args:
        order_by (None | str | Unset):
        order_direction (GetVb365ProtectedObjectsOrderDirection | Unset):  Default:
            GetVb365ProtectedObjectsOrderDirection.ASCENDING.
        object_name_filter (None | str | Unset):
        object_type_filter (list[Vb365ProtectedObjectType] | None | Unset):
        educational_filter (bool | None | Unset):
        licensed_filter (bool | None | Unset):
        skip_cache (bool | None | Unset):
        limit (int | Unset):  Default: 100.
        offset (int | Unset):  Default: 0.
        site_filter (list[UUID] | None | Unset):
        organization_filter (None | Unset | UUID):
        location_filter (None | Unset | UUID):
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ErrorResponse | GetVb365ProtectedObjectsResponse200]
    """

    kwargs = _get_kwargs(
        order_by=order_by,
        order_direction=order_direction,
        object_name_filter=object_name_filter,
        object_type_filter=object_type_filter,
        educational_filter=educational_filter,
        licensed_filter=licensed_filter,
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
    client: AuthenticatedClient,
    order_by: None | str | Unset = UNSET,
    order_direction: GetVb365ProtectedObjectsOrderDirection | Unset = GetVb365ProtectedObjectsOrderDirection.ASCENDING,
    object_name_filter: None | str | Unset = UNSET,
    object_type_filter: list[Vb365ProtectedObjectType] | None | Unset = UNSET,
    educational_filter: bool | None | Unset = UNSET,
    licensed_filter: bool | None | Unset = UNSET,
    skip_cache: bool | None | Unset = UNSET,
    limit: int | Unset = 100,
    offset: int | Unset = 0,
    site_filter: list[UUID] | None | Unset = UNSET,
    organization_filter: None | Unset | UUID = UNSET,
    location_filter: None | Unset | UUID = UNSET,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Any | ErrorResponse | GetVb365ProtectedObjectsResponse200 | None:
    """Get All Objects Protected by Veeam Backup for Microsoft 365

     Returns a collection resource representation of all objects protected by Veeam Backup for Microsoft
    365.

    Args:
        order_by (None | str | Unset):
        order_direction (GetVb365ProtectedObjectsOrderDirection | Unset):  Default:
            GetVb365ProtectedObjectsOrderDirection.ASCENDING.
        object_name_filter (None | str | Unset):
        object_type_filter (list[Vb365ProtectedObjectType] | None | Unset):
        educational_filter (bool | None | Unset):
        licensed_filter (bool | None | Unset):
        skip_cache (bool | None | Unset):
        limit (int | Unset):  Default: 100.
        offset (int | Unset):  Default: 0.
        site_filter (list[UUID] | None | Unset):
        organization_filter (None | Unset | UUID):
        location_filter (None | Unset | UUID):
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ErrorResponse | GetVb365ProtectedObjectsResponse200
    """

    return sync_detailed(
        client=client,
        order_by=order_by,
        order_direction=order_direction,
        object_name_filter=object_name_filter,
        object_type_filter=object_type_filter,
        educational_filter=educational_filter,
        licensed_filter=licensed_filter,
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
    client: AuthenticatedClient,
    order_by: None | str | Unset = UNSET,
    order_direction: GetVb365ProtectedObjectsOrderDirection | Unset = GetVb365ProtectedObjectsOrderDirection.ASCENDING,
    object_name_filter: None | str | Unset = UNSET,
    object_type_filter: list[Vb365ProtectedObjectType] | None | Unset = UNSET,
    educational_filter: bool | None | Unset = UNSET,
    licensed_filter: bool | None | Unset = UNSET,
    skip_cache: bool | None | Unset = UNSET,
    limit: int | Unset = 100,
    offset: int | Unset = 0,
    site_filter: list[UUID] | None | Unset = UNSET,
    organization_filter: None | Unset | UUID = UNSET,
    location_filter: None | Unset | UUID = UNSET,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Response[Any | ErrorResponse | GetVb365ProtectedObjectsResponse200]:
    """Get All Objects Protected by Veeam Backup for Microsoft 365

     Returns a collection resource representation of all objects protected by Veeam Backup for Microsoft
    365.

    Args:
        order_by (None | str | Unset):
        order_direction (GetVb365ProtectedObjectsOrderDirection | Unset):  Default:
            GetVb365ProtectedObjectsOrderDirection.ASCENDING.
        object_name_filter (None | str | Unset):
        object_type_filter (list[Vb365ProtectedObjectType] | None | Unset):
        educational_filter (bool | None | Unset):
        licensed_filter (bool | None | Unset):
        skip_cache (bool | None | Unset):
        limit (int | Unset):  Default: 100.
        offset (int | Unset):  Default: 0.
        site_filter (list[UUID] | None | Unset):
        organization_filter (None | Unset | UUID):
        location_filter (None | Unset | UUID):
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ErrorResponse | GetVb365ProtectedObjectsResponse200]
    """

    kwargs = _get_kwargs(
        order_by=order_by,
        order_direction=order_direction,
        object_name_filter=object_name_filter,
        object_type_filter=object_type_filter,
        educational_filter=educational_filter,
        licensed_filter=licensed_filter,
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
    client: AuthenticatedClient,
    order_by: None | str | Unset = UNSET,
    order_direction: GetVb365ProtectedObjectsOrderDirection | Unset = GetVb365ProtectedObjectsOrderDirection.ASCENDING,
    object_name_filter: None | str | Unset = UNSET,
    object_type_filter: list[Vb365ProtectedObjectType] | None | Unset = UNSET,
    educational_filter: bool | None | Unset = UNSET,
    licensed_filter: bool | None | Unset = UNSET,
    skip_cache: bool | None | Unset = UNSET,
    limit: int | Unset = 100,
    offset: int | Unset = 0,
    site_filter: list[UUID] | None | Unset = UNSET,
    organization_filter: None | Unset | UUID = UNSET,
    location_filter: None | Unset | UUID = UNSET,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Any | ErrorResponse | GetVb365ProtectedObjectsResponse200 | None:
    """Get All Objects Protected by Veeam Backup for Microsoft 365

     Returns a collection resource representation of all objects protected by Veeam Backup for Microsoft
    365.

    Args:
        order_by (None | str | Unset):
        order_direction (GetVb365ProtectedObjectsOrderDirection | Unset):  Default:
            GetVb365ProtectedObjectsOrderDirection.ASCENDING.
        object_name_filter (None | str | Unset):
        object_type_filter (list[Vb365ProtectedObjectType] | None | Unset):
        educational_filter (bool | None | Unset):
        licensed_filter (bool | None | Unset):
        skip_cache (bool | None | Unset):
        limit (int | Unset):  Default: 100.
        offset (int | Unset):  Default: 0.
        site_filter (list[UUID] | None | Unset):
        organization_filter (None | Unset | UUID):
        location_filter (None | Unset | UUID):
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ErrorResponse | GetVb365ProtectedObjectsResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            order_by=order_by,
            order_direction=order_direction,
            object_name_filter=object_name_filter,
            object_type_filter=object_type_filter,
            educational_filter=educational_filter,
            licensed_filter=licensed_filter,
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
