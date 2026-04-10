from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.get_vcd_organizations_by_vcd_response_200 import GetVcdOrganizationsByVcdResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    backup_server_uid: UUID,
    vcd_server_uid: UUID,
    *,
    company_uid: UUID | Unset = UNSET,
    limit: int | Unset = 100,
    offset: int | Unset = 0,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_request_id, Unset):
        headers["X-Request-id"] = x_request_id

    if not isinstance(x_client_version, Unset):
        headers["X-Client-Version"] = x_client_version

    params: dict[str, Any] = {}

    json_company_uid: str | Unset = UNSET
    if not isinstance(company_uid, Unset):
        json_company_uid = str(company_uid)
    params["companyUid"] = json_company_uid

    params["limit"] = limit

    params["offset"] = offset

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/infrastructure/backupServers/{backup_server_uid}/vcdServers/{vcd_server_uid}/vcdOrganizations".format(
            backup_server_uid=quote(str(backup_server_uid), safe=""),
            vcd_server_uid=quote(str(vcd_server_uid), safe=""),
        ),
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | ErrorResponse | GetVcdOrganizationsByVcdResponse200:
    if response.status_code == 200:
        response_200 = GetVcdOrganizationsByVcdResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 202:
        response_202 = cast(Any, None)
        return response_202

    response_default = ErrorResponse.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | ErrorResponse | GetVcdOrganizationsByVcdResponse200]:
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
    client: AuthenticatedClient,
    company_uid: UUID | Unset = UNSET,
    limit: int | Unset = 100,
    offset: int | Unset = 0,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Response[Any | ErrorResponse | GetVcdOrganizationsByVcdResponse200]:
    """Get All VMware Cloud Director Organizations Configured on VMware Cloud Director Server

     Returns a collection resource representation of all VMware Cloud Director organizations configured
    on a VMware Cloud Director server with the specified UID.

    Args:
        backup_server_uid (UUID):
        vcd_server_uid (UUID):
        company_uid (UUID | Unset):
        limit (int | Unset):  Default: 100.
        offset (int | Unset):  Default: 0.
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ErrorResponse | GetVcdOrganizationsByVcdResponse200]
    """

    kwargs = _get_kwargs(
        backup_server_uid=backup_server_uid,
        vcd_server_uid=vcd_server_uid,
        company_uid=company_uid,
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
    client: AuthenticatedClient,
    company_uid: UUID | Unset = UNSET,
    limit: int | Unset = 100,
    offset: int | Unset = 0,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Any | ErrorResponse | GetVcdOrganizationsByVcdResponse200 | None:
    """Get All VMware Cloud Director Organizations Configured on VMware Cloud Director Server

     Returns a collection resource representation of all VMware Cloud Director organizations configured
    on a VMware Cloud Director server with the specified UID.

    Args:
        backup_server_uid (UUID):
        vcd_server_uid (UUID):
        company_uid (UUID | Unset):
        limit (int | Unset):  Default: 100.
        offset (int | Unset):  Default: 0.
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ErrorResponse | GetVcdOrganizationsByVcdResponse200
    """

    return sync_detailed(
        backup_server_uid=backup_server_uid,
        vcd_server_uid=vcd_server_uid,
        client=client,
        company_uid=company_uid,
        limit=limit,
        offset=offset,
        x_request_id=x_request_id,
        x_client_version=x_client_version,
    ).parsed


async def asyncio_detailed(
    backup_server_uid: UUID,
    vcd_server_uid: UUID,
    *,
    client: AuthenticatedClient,
    company_uid: UUID | Unset = UNSET,
    limit: int | Unset = 100,
    offset: int | Unset = 0,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Response[Any | ErrorResponse | GetVcdOrganizationsByVcdResponse200]:
    """Get All VMware Cloud Director Organizations Configured on VMware Cloud Director Server

     Returns a collection resource representation of all VMware Cloud Director organizations configured
    on a VMware Cloud Director server with the specified UID.

    Args:
        backup_server_uid (UUID):
        vcd_server_uid (UUID):
        company_uid (UUID | Unset):
        limit (int | Unset):  Default: 100.
        offset (int | Unset):  Default: 0.
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ErrorResponse | GetVcdOrganizationsByVcdResponse200]
    """

    kwargs = _get_kwargs(
        backup_server_uid=backup_server_uid,
        vcd_server_uid=vcd_server_uid,
        company_uid=company_uid,
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
    client: AuthenticatedClient,
    company_uid: UUID | Unset = UNSET,
    limit: int | Unset = 100,
    offset: int | Unset = 0,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Any | ErrorResponse | GetVcdOrganizationsByVcdResponse200 | None:
    """Get All VMware Cloud Director Organizations Configured on VMware Cloud Director Server

     Returns a collection resource representation of all VMware Cloud Director organizations configured
    on a VMware Cloud Director server with the specified UID.

    Args:
        backup_server_uid (UUID):
        vcd_server_uid (UUID):
        company_uid (UUID | Unset):
        limit (int | Unset):  Default: 100.
        offset (int | Unset):  Default: 0.
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ErrorResponse | GetVcdOrganizationsByVcdResponse200
    """

    return (
        await asyncio_detailed(
            backup_server_uid=backup_server_uid,
            vcd_server_uid=vcd_server_uid,
            client=client,
            company_uid=company_uid,
            limit=limit,
            offset=offset,
            x_request_id=x_request_id,
            x_client_version=x_client_version,
        )
    ).parsed
