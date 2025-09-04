from http import HTTPStatus
from typing import Any, Optional, Union, cast
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.create_company_by_pulse_tenant_response_200 import CreateCompanyByPulseTenantResponse200
from ...models.error_response import ErrorResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    tenant_uid: str,
    *,
    site_uid: UUID,
    gateway_pool_uid: Union[Unset, UUID] = UNSET,
    x_request_id: Union[Unset, UUID] = UNSET,
    x_client_version: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_request_id, Unset):
        headers["X-Request-id"] = x_request_id

    if not isinstance(x_client_version, Unset):
        headers["X-Client-Version"] = x_client_version

    params: dict[str, Any] = {}

    json_site_uid = str(site_uid)
    params["siteUid"] = json_site_uid

    json_gateway_pool_uid: Union[Unset, str] = UNSET
    if not isinstance(gateway_pool_uid, Unset):
        json_gateway_pool_uid = str(gateway_pool_uid)
    params["gatewayPoolUid"] = json_gateway_pool_uid

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/pulse/tenants/{tenant_uid}/createCompany",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Union[Any, CreateCompanyByPulseTenantResponse200, ErrorResponse]:
    if response.status_code == 200:
        response_200 = CreateCompanyByPulseTenantResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 202:
        response_202 = cast(Any, None)
        return response_202

    response_default = ErrorResponse.from_dict(response.json())

    return response_default


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, CreateCompanyByPulseTenantResponse200, ErrorResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    tenant_uid: str,
    *,
    client: Union[AuthenticatedClient, Client],
    site_uid: UUID,
    gateway_pool_uid: Union[Unset, UUID] = UNSET,
    x_request_id: Union[Unset, UUID] = UNSET,
    x_client_version: Union[Unset, str] = UNSET,
) -> Response[Union[Any, CreateCompanyByPulseTenantResponse200, ErrorResponse]]:
    """Create Company from VCSP Tenant

     Creates a company based on VCSP Pulse tenant with the specified UID.

    Args:
        tenant_uid (str):
        site_uid (UUID):
        gateway_pool_uid (Union[Unset, UUID]):
        x_request_id (Union[Unset, UUID]):
        x_client_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, CreateCompanyByPulseTenantResponse200, ErrorResponse]]
    """

    kwargs = _get_kwargs(
        tenant_uid=tenant_uid,
        site_uid=site_uid,
        gateway_pool_uid=gateway_pool_uid,
        x_request_id=x_request_id,
        x_client_version=x_client_version,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    tenant_uid: str,
    *,
    client: Union[AuthenticatedClient, Client],
    site_uid: UUID,
    gateway_pool_uid: Union[Unset, UUID] = UNSET,
    x_request_id: Union[Unset, UUID] = UNSET,
    x_client_version: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, CreateCompanyByPulseTenantResponse200, ErrorResponse]]:
    """Create Company from VCSP Tenant

     Creates a company based on VCSP Pulse tenant with the specified UID.

    Args:
        tenant_uid (str):
        site_uid (UUID):
        gateway_pool_uid (Union[Unset, UUID]):
        x_request_id (Union[Unset, UUID]):
        x_client_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, CreateCompanyByPulseTenantResponse200, ErrorResponse]
    """

    return sync_detailed(
        tenant_uid=tenant_uid,
        client=client,
        site_uid=site_uid,
        gateway_pool_uid=gateway_pool_uid,
        x_request_id=x_request_id,
        x_client_version=x_client_version,
    ).parsed


async def asyncio_detailed(
    tenant_uid: str,
    *,
    client: Union[AuthenticatedClient, Client],
    site_uid: UUID,
    gateway_pool_uid: Union[Unset, UUID] = UNSET,
    x_request_id: Union[Unset, UUID] = UNSET,
    x_client_version: Union[Unset, str] = UNSET,
) -> Response[Union[Any, CreateCompanyByPulseTenantResponse200, ErrorResponse]]:
    """Create Company from VCSP Tenant

     Creates a company based on VCSP Pulse tenant with the specified UID.

    Args:
        tenant_uid (str):
        site_uid (UUID):
        gateway_pool_uid (Union[Unset, UUID]):
        x_request_id (Union[Unset, UUID]):
        x_client_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, CreateCompanyByPulseTenantResponse200, ErrorResponse]]
    """

    kwargs = _get_kwargs(
        tenant_uid=tenant_uid,
        site_uid=site_uid,
        gateway_pool_uid=gateway_pool_uid,
        x_request_id=x_request_id,
        x_client_version=x_client_version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    tenant_uid: str,
    *,
    client: Union[AuthenticatedClient, Client],
    site_uid: UUID,
    gateway_pool_uid: Union[Unset, UUID] = UNSET,
    x_request_id: Union[Unset, UUID] = UNSET,
    x_client_version: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, CreateCompanyByPulseTenantResponse200, ErrorResponse]]:
    """Create Company from VCSP Tenant

     Creates a company based on VCSP Pulse tenant with the specified UID.

    Args:
        tenant_uid (str):
        site_uid (UUID):
        gateway_pool_uid (Union[Unset, UUID]):
        x_request_id (Union[Unset, UUID]):
        x_client_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, CreateCompanyByPulseTenantResponse200, ErrorResponse]
    """

    return (
        await asyncio_detailed(
            tenant_uid=tenant_uid,
            client=client,
            site_uid=site_uid,
            gateway_pool_uid=gateway_pool_uid,
            x_request_id=x_request_id,
            x_client_version=x_client_version,
        )
    ).parsed
