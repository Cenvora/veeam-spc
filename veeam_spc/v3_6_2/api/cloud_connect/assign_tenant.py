from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.assign_tenant_response_200 import AssignTenantResponse200
from ...models.error_response import ErrorResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    tenant_uid: UUID,
    *,
    company_uid: UUID,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_request_id, Unset):
        headers["X-Request-id"] = x_request_id

    if not isinstance(x_client_version, Unset):
        headers["X-Client-Version"] = x_client_version

    params: dict[str, Any] = {}

    json_company_uid = str(company_uid)
    params["companyUid"] = json_company_uid

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/infrastructure/sites/tenants/{tenant_uid}/assignForCompany".format(
            tenant_uid=quote(str(tenant_uid), safe=""),
        ),
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | AssignTenantResponse200 | ErrorResponse:
    if response.status_code == 200:
        response_200 = AssignTenantResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 202:
        response_202 = cast(Any, None)
        return response_202

    response_default = ErrorResponse.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | AssignTenantResponse200 | ErrorResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    tenant_uid: UUID,
    *,
    client: AuthenticatedClient,
    company_uid: UUID,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Response[Any | AssignTenantResponse200 | ErrorResponse]:
    """Assign Cloud Tenant to Company

     Assigns a cloud tenant with the specified UID to a company.

    Args:
        tenant_uid (UUID):
        company_uid (UUID):
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | AssignTenantResponse200 | ErrorResponse]
    """

    kwargs = _get_kwargs(
        tenant_uid=tenant_uid,
        company_uid=company_uid,
        x_request_id=x_request_id,
        x_client_version=x_client_version,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    tenant_uid: UUID,
    *,
    client: AuthenticatedClient,
    company_uid: UUID,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Any | AssignTenantResponse200 | ErrorResponse | None:
    """Assign Cloud Tenant to Company

     Assigns a cloud tenant with the specified UID to a company.

    Args:
        tenant_uid (UUID):
        company_uid (UUID):
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | AssignTenantResponse200 | ErrorResponse
    """

    return sync_detailed(
        tenant_uid=tenant_uid,
        client=client,
        company_uid=company_uid,
        x_request_id=x_request_id,
        x_client_version=x_client_version,
    ).parsed


async def asyncio_detailed(
    tenant_uid: UUID,
    *,
    client: AuthenticatedClient,
    company_uid: UUID,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Response[Any | AssignTenantResponse200 | ErrorResponse]:
    """Assign Cloud Tenant to Company

     Assigns a cloud tenant with the specified UID to a company.

    Args:
        tenant_uid (UUID):
        company_uid (UUID):
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | AssignTenantResponse200 | ErrorResponse]
    """

    kwargs = _get_kwargs(
        tenant_uid=tenant_uid,
        company_uid=company_uid,
        x_request_id=x_request_id,
        x_client_version=x_client_version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    tenant_uid: UUID,
    *,
    client: AuthenticatedClient,
    company_uid: UUID,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Any | AssignTenantResponse200 | ErrorResponse | None:
    """Assign Cloud Tenant to Company

     Assigns a cloud tenant with the specified UID to a company.

    Args:
        tenant_uid (UUID):
        company_uid (UUID):
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | AssignTenantResponse200 | ErrorResponse
    """

    return (
        await asyncio_detailed(
            tenant_uid=tenant_uid,
            client=client,
            company_uid=company_uid,
            x_request_id=x_request_id,
            x_client_version=x_client_version,
        )
    ).parsed
