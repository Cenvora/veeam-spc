from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.get_sub_tenants_by_site_response_200 import GetSubTenantsBySiteResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    site_uid: UUID,
    *,
    filter_: str | Unset = UNSET,
    sort: str | Unset = UNSET,
    limit: int | Unset = 100,
    offset: int | Unset = 0,
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

    params["select"] = select

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/infrastructure/sites/{site_uid}/tenants/subtenants".format(
            site_uid=quote(str(site_uid), safe=""),
        ),
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | ErrorResponse | GetSubTenantsBySiteResponse200:
    if response.status_code == 200:
        response_200 = GetSubTenantsBySiteResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 202:
        response_202 = cast(Any, None)
        return response_202

    response_default = ErrorResponse.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | ErrorResponse | GetSubTenantsBySiteResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    site_uid: UUID,
    *,
    client: AuthenticatedClient,
    filter_: str | Unset = UNSET,
    sort: str | Unset = UNSET,
    limit: int | Unset = 100,
    offset: int | Unset = 0,
    select: str | Unset = UNSET,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Response[Any | ErrorResponse | GetSubTenantsBySiteResponse200]:
    """Get All Subtenants Registered on Site

     Returns a collection resource representation of all subtenants provided with resources of a Veeam
    Cloud Connect site with the specified UID.

    Args:
        site_uid (UUID):
        filter_ (str | Unset):
        sort (str | Unset):
        limit (int | Unset):  Default: 100.
        offset (int | Unset):  Default: 0.
        select (str | Unset):
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ErrorResponse | GetSubTenantsBySiteResponse200]
    """

    kwargs = _get_kwargs(
        site_uid=site_uid,
        filter_=filter_,
        sort=sort,
        limit=limit,
        offset=offset,
        select=select,
        x_request_id=x_request_id,
        x_client_version=x_client_version,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    site_uid: UUID,
    *,
    client: AuthenticatedClient,
    filter_: str | Unset = UNSET,
    sort: str | Unset = UNSET,
    limit: int | Unset = 100,
    offset: int | Unset = 0,
    select: str | Unset = UNSET,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Any | ErrorResponse | GetSubTenantsBySiteResponse200 | None:
    """Get All Subtenants Registered on Site

     Returns a collection resource representation of all subtenants provided with resources of a Veeam
    Cloud Connect site with the specified UID.

    Args:
        site_uid (UUID):
        filter_ (str | Unset):
        sort (str | Unset):
        limit (int | Unset):  Default: 100.
        offset (int | Unset):  Default: 0.
        select (str | Unset):
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ErrorResponse | GetSubTenantsBySiteResponse200
    """

    return sync_detailed(
        site_uid=site_uid,
        client=client,
        filter_=filter_,
        sort=sort,
        limit=limit,
        offset=offset,
        select=select,
        x_request_id=x_request_id,
        x_client_version=x_client_version,
    ).parsed


async def asyncio_detailed(
    site_uid: UUID,
    *,
    client: AuthenticatedClient,
    filter_: str | Unset = UNSET,
    sort: str | Unset = UNSET,
    limit: int | Unset = 100,
    offset: int | Unset = 0,
    select: str | Unset = UNSET,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Response[Any | ErrorResponse | GetSubTenantsBySiteResponse200]:
    """Get All Subtenants Registered on Site

     Returns a collection resource representation of all subtenants provided with resources of a Veeam
    Cloud Connect site with the specified UID.

    Args:
        site_uid (UUID):
        filter_ (str | Unset):
        sort (str | Unset):
        limit (int | Unset):  Default: 100.
        offset (int | Unset):  Default: 0.
        select (str | Unset):
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ErrorResponse | GetSubTenantsBySiteResponse200]
    """

    kwargs = _get_kwargs(
        site_uid=site_uid,
        filter_=filter_,
        sort=sort,
        limit=limit,
        offset=offset,
        select=select,
        x_request_id=x_request_id,
        x_client_version=x_client_version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    site_uid: UUID,
    *,
    client: AuthenticatedClient,
    filter_: str | Unset = UNSET,
    sort: str | Unset = UNSET,
    limit: int | Unset = 100,
    offset: int | Unset = 0,
    select: str | Unset = UNSET,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Any | ErrorResponse | GetSubTenantsBySiteResponse200 | None:
    """Get All Subtenants Registered on Site

     Returns a collection resource representation of all subtenants provided with resources of a Veeam
    Cloud Connect site with the specified UID.

    Args:
        site_uid (UUID):
        filter_ (str | Unset):
        sort (str | Unset):
        limit (int | Unset):  Default: 100.
        offset (int | Unset):  Default: 0.
        select (str | Unset):
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ErrorResponse | GetSubTenantsBySiteResponse200
    """

    return (
        await asyncio_detailed(
            site_uid=site_uid,
            client=client,
            filter_=filter_,
            sort=sort,
            limit=limit,
            offset=offset,
            select=select,
            x_request_id=x_request_id,
            x_client_version=x_client_version,
        )
    ).parsed
