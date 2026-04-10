from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.get_site_vcd_organization_response_200 import GetSiteVcdOrganizationResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    site_uid: UUID,
    vcd_organization_uid: UUID,
    *,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_request_id, Unset):
        headers["X-Request-id"] = x_request_id

    if not isinstance(x_client_version, Unset):
        headers["X-Client-Version"] = x_client_version

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/infrastructure/sites/{site_uid}/vcdServers/vcdOrganizations/{vcd_organization_uid}".format(
            site_uid=quote(str(site_uid), safe=""),
            vcd_organization_uid=quote(str(vcd_organization_uid), safe=""),
        ),
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | ErrorResponse | GetSiteVcdOrganizationResponse200:
    if response.status_code == 200:
        response_200 = GetSiteVcdOrganizationResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 202:
        response_202 = cast(Any, None)
        return response_202

    response_default = ErrorResponse.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | ErrorResponse | GetSiteVcdOrganizationResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    site_uid: UUID,
    vcd_organization_uid: UUID,
    *,
    client: AuthenticatedClient,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Response[Any | ErrorResponse | GetSiteVcdOrganizationResponse200]:
    """Get VMware Cloud Director Organization Managed by Veeam Cloud Connect Site

     Returns a resource representation of a VMware Cloud Director organization with the specified UID
    managed by Veeam Cloud Connect Site.

    Args:
        site_uid (UUID):
        vcd_organization_uid (UUID):
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ErrorResponse | GetSiteVcdOrganizationResponse200]
    """

    kwargs = _get_kwargs(
        site_uid=site_uid,
        vcd_organization_uid=vcd_organization_uid,
        x_request_id=x_request_id,
        x_client_version=x_client_version,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    site_uid: UUID,
    vcd_organization_uid: UUID,
    *,
    client: AuthenticatedClient,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Any | ErrorResponse | GetSiteVcdOrganizationResponse200 | None:
    """Get VMware Cloud Director Organization Managed by Veeam Cloud Connect Site

     Returns a resource representation of a VMware Cloud Director organization with the specified UID
    managed by Veeam Cloud Connect Site.

    Args:
        site_uid (UUID):
        vcd_organization_uid (UUID):
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ErrorResponse | GetSiteVcdOrganizationResponse200
    """

    return sync_detailed(
        site_uid=site_uid,
        vcd_organization_uid=vcd_organization_uid,
        client=client,
        x_request_id=x_request_id,
        x_client_version=x_client_version,
    ).parsed


async def asyncio_detailed(
    site_uid: UUID,
    vcd_organization_uid: UUID,
    *,
    client: AuthenticatedClient,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Response[Any | ErrorResponse | GetSiteVcdOrganizationResponse200]:
    """Get VMware Cloud Director Organization Managed by Veeam Cloud Connect Site

     Returns a resource representation of a VMware Cloud Director organization with the specified UID
    managed by Veeam Cloud Connect Site.

    Args:
        site_uid (UUID):
        vcd_organization_uid (UUID):
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ErrorResponse | GetSiteVcdOrganizationResponse200]
    """

    kwargs = _get_kwargs(
        site_uid=site_uid,
        vcd_organization_uid=vcd_organization_uid,
        x_request_id=x_request_id,
        x_client_version=x_client_version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    site_uid: UUID,
    vcd_organization_uid: UUID,
    *,
    client: AuthenticatedClient,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Any | ErrorResponse | GetSiteVcdOrganizationResponse200 | None:
    """Get VMware Cloud Director Organization Managed by Veeam Cloud Connect Site

     Returns a resource representation of a VMware Cloud Director organization with the specified UID
    managed by Veeam Cloud Connect Site.

    Args:
        site_uid (UUID):
        vcd_organization_uid (UUID):
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ErrorResponse | GetSiteVcdOrganizationResponse200
    """

    return (
        await asyncio_detailed(
            site_uid=site_uid,
            vcd_organization_uid=vcd_organization_uid,
            client=client,
            x_request_id=x_request_id,
            x_client_version=x_client_version,
        )
    ).parsed
