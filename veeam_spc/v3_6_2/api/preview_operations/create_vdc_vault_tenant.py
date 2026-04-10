from http import HTTPStatus
from typing import Any, cast
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.create_vdc_vault_tenant_response_200 import CreateVdcVaultTenantResponse200
from ...models.error_response import ErrorResponse
from ...models.vdc_vault_tenant_input import VdcVaultTenantInput
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: VdcVaultTenantInput,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_request_id, Unset):
        headers["X-Request-id"] = x_request_id

    if not isinstance(x_client_version, Unset):
        headers["X-Client-Version"] = x_client_version

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/vdcVault/tenants",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | CreateVdcVaultTenantResponse200 | ErrorResponse:
    if response.status_code == 200:
        response_200 = CreateVdcVaultTenantResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 202:
        response_202 = cast(Any, None)
        return response_202

    response_default = ErrorResponse.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | CreateVdcVaultTenantResponse200 | ErrorResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: VdcVaultTenantInput,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Response[Any | CreateVdcVaultTenantResponse200 | ErrorResponse]:
    """Add Veeam Data Cloud Vault Tenant

     Adds a new Veeam Data Cloud Vault tenant.

    Args:
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):
        body (VdcVaultTenantInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CreateVdcVaultTenantResponse200 | ErrorResponse]
    """

    kwargs = _get_kwargs(
        body=body,
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
    body: VdcVaultTenantInput,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Any | CreateVdcVaultTenantResponse200 | ErrorResponse | None:
    """Add Veeam Data Cloud Vault Tenant

     Adds a new Veeam Data Cloud Vault tenant.

    Args:
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):
        body (VdcVaultTenantInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CreateVdcVaultTenantResponse200 | ErrorResponse
    """

    return sync_detailed(
        client=client,
        body=body,
        x_request_id=x_request_id,
        x_client_version=x_client_version,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: VdcVaultTenantInput,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Response[Any | CreateVdcVaultTenantResponse200 | ErrorResponse]:
    """Add Veeam Data Cloud Vault Tenant

     Adds a new Veeam Data Cloud Vault tenant.

    Args:
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):
        body (VdcVaultTenantInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CreateVdcVaultTenantResponse200 | ErrorResponse]
    """

    kwargs = _get_kwargs(
        body=body,
        x_request_id=x_request_id,
        x_client_version=x_client_version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: VdcVaultTenantInput,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Any | CreateVdcVaultTenantResponse200 | ErrorResponse | None:
    """Add Veeam Data Cloud Vault Tenant

     Adds a new Veeam Data Cloud Vault tenant.

    Args:
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):
        body (VdcVaultTenantInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CreateVdcVaultTenantResponse200 | ErrorResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            x_request_id=x_request_id,
            x_client_version=x_client_version,
        )
    ).parsed
