from http import HTTPStatus
from typing import Any, cast
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.get_vb_365_jobs_response_200 import GetVb365JobsResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    filter_: str | Unset = UNSET,
    sort: str | Unset = UNSET,
    limit: int | Unset = 100,
    offset: int | Unset = 0,
    site_filter: list[UUID] | Unset = UNSET,
    organization_filter: UUID | Unset = UNSET,
    location_filter: UUID | Unset = UNSET,
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

    params["filter"] = filter_

    params["sort"] = sort

    params["limit"] = limit

    params["offset"] = offset

    json_site_filter: list[str] | Unset = UNSET
    if not isinstance(site_filter, Unset):
        json_site_filter = []
        for site_filter_item_data in site_filter:
            site_filter_item = str(site_filter_item_data)
            json_site_filter.append(site_filter_item)

    params["siteFilter"] = json_site_filter

    json_organization_filter: str | Unset = UNSET
    if not isinstance(organization_filter, Unset):
        json_organization_filter = str(organization_filter)
    params["organizationFilter"] = json_organization_filter

    json_location_filter: str | Unset = UNSET
    if not isinstance(location_filter, Unset):
        json_location_filter = str(location_filter)
    params["locationFilter"] = json_location_filter

    params["select"] = select

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/infrastructure/vb365Servers/organizations/jobs",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | ErrorResponse | GetVb365JobsResponse200:
    if response.status_code == 200:
        response_200 = GetVb365JobsResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 202:
        response_202 = cast(Any, None)
        return response_202

    response_default = ErrorResponse.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | ErrorResponse | GetVb365JobsResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    filter_: str | Unset = UNSET,
    sort: str | Unset = UNSET,
    limit: int | Unset = 100,
    offset: int | Unset = 0,
    site_filter: list[UUID] | Unset = UNSET,
    organization_filter: UUID | Unset = UNSET,
    location_filter: UUID | Unset = UNSET,
    select: str | Unset = UNSET,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Response[Any | ErrorResponse | GetVb365JobsResponse200]:
    """Get All Veeam Backup for Microsoft 365 Jobs

     Returns a collection resource representation of all Veeam Backup for Microsoft 365 jobs.

    Args:
        filter_ (str | Unset):
        sort (str | Unset):
        limit (int | Unset):  Default: 100.
        offset (int | Unset):  Default: 0.
        site_filter (list[UUID] | Unset):
        organization_filter (UUID | Unset):
        location_filter (UUID | Unset):
        select (str | Unset):
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ErrorResponse | GetVb365JobsResponse200]
    """

    kwargs = _get_kwargs(
        filter_=filter_,
        sort=sort,
        limit=limit,
        offset=offset,
        site_filter=site_filter,
        organization_filter=organization_filter,
        location_filter=location_filter,
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
    filter_: str | Unset = UNSET,
    sort: str | Unset = UNSET,
    limit: int | Unset = 100,
    offset: int | Unset = 0,
    site_filter: list[UUID] | Unset = UNSET,
    organization_filter: UUID | Unset = UNSET,
    location_filter: UUID | Unset = UNSET,
    select: str | Unset = UNSET,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Any | ErrorResponse | GetVb365JobsResponse200 | None:
    """Get All Veeam Backup for Microsoft 365 Jobs

     Returns a collection resource representation of all Veeam Backup for Microsoft 365 jobs.

    Args:
        filter_ (str | Unset):
        sort (str | Unset):
        limit (int | Unset):  Default: 100.
        offset (int | Unset):  Default: 0.
        site_filter (list[UUID] | Unset):
        organization_filter (UUID | Unset):
        location_filter (UUID | Unset):
        select (str | Unset):
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ErrorResponse | GetVb365JobsResponse200
    """

    return sync_detailed(
        client=client,
        filter_=filter_,
        sort=sort,
        limit=limit,
        offset=offset,
        site_filter=site_filter,
        organization_filter=organization_filter,
        location_filter=location_filter,
        select=select,
        x_request_id=x_request_id,
        x_client_version=x_client_version,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    filter_: str | Unset = UNSET,
    sort: str | Unset = UNSET,
    limit: int | Unset = 100,
    offset: int | Unset = 0,
    site_filter: list[UUID] | Unset = UNSET,
    organization_filter: UUID | Unset = UNSET,
    location_filter: UUID | Unset = UNSET,
    select: str | Unset = UNSET,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Response[Any | ErrorResponse | GetVb365JobsResponse200]:
    """Get All Veeam Backup for Microsoft 365 Jobs

     Returns a collection resource representation of all Veeam Backup for Microsoft 365 jobs.

    Args:
        filter_ (str | Unset):
        sort (str | Unset):
        limit (int | Unset):  Default: 100.
        offset (int | Unset):  Default: 0.
        site_filter (list[UUID] | Unset):
        organization_filter (UUID | Unset):
        location_filter (UUID | Unset):
        select (str | Unset):
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ErrorResponse | GetVb365JobsResponse200]
    """

    kwargs = _get_kwargs(
        filter_=filter_,
        sort=sort,
        limit=limit,
        offset=offset,
        site_filter=site_filter,
        organization_filter=organization_filter,
        location_filter=location_filter,
        select=select,
        x_request_id=x_request_id,
        x_client_version=x_client_version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    filter_: str | Unset = UNSET,
    sort: str | Unset = UNSET,
    limit: int | Unset = 100,
    offset: int | Unset = 0,
    site_filter: list[UUID] | Unset = UNSET,
    organization_filter: UUID | Unset = UNSET,
    location_filter: UUID | Unset = UNSET,
    select: str | Unset = UNSET,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Any | ErrorResponse | GetVb365JobsResponse200 | None:
    """Get All Veeam Backup for Microsoft 365 Jobs

     Returns a collection resource representation of all Veeam Backup for Microsoft 365 jobs.

    Args:
        filter_ (str | Unset):
        sort (str | Unset):
        limit (int | Unset):  Default: 100.
        offset (int | Unset):  Default: 0.
        site_filter (list[UUID] | Unset):
        organization_filter (UUID | Unset):
        location_filter (UUID | Unset):
        select (str | Unset):
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ErrorResponse | GetVb365JobsResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            filter_=filter_,
            sort=sort,
            limit=limit,
            offset=offset,
            site_filter=site_filter,
            organization_filter=organization_filter,
            location_filter=location_filter,
            select=select,
            x_request_id=x_request_id,
            x_client_version=x_client_version,
        )
    ).parsed
