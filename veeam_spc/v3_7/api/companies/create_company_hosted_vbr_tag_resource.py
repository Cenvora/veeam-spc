from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.company_hosted_vbr_tag_resource_input import CompanyHostedVbrTagResourceInput
from ...models.create_company_hosted_vbr_tag_resource_response_200 import CreateCompanyHostedVbrTagResourceResponse200
from ...models.error_response import ErrorResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    company_uid: UUID,
    vbr_hosted_resource_uid: UUID,
    *,
    body: CompanyHostedVbrTagResourceInput,
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

    params["select"] = select

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/organizations/companies/{company_uid}/hostedResources/vbr/{vbr_hosted_resource_uid}/tagResources".format(
            company_uid=quote(str(company_uid), safe=""),
            vbr_hosted_resource_uid=quote(str(vbr_hosted_resource_uid), safe=""),
        ),
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | CreateCompanyHostedVbrTagResourceResponse200 | ErrorResponse:
    if response.status_code == 200:
        response_200 = CreateCompanyHostedVbrTagResourceResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 202:
        response_202 = cast(Any, None)
        return response_202

    response_default = ErrorResponse.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | CreateCompanyHostedVbrTagResourceResponse200 | ErrorResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    company_uid: UUID,
    vbr_hosted_resource_uid: UUID,
    *,
    client: AuthenticatedClient,
    body: CompanyHostedVbrTagResourceInput,
    select: str | Unset = UNSET,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Response[Any | CreateCompanyHostedVbrTagResourceResponse200 | ErrorResponse]:
    """Create Tag Resource on Company Hosted Server Resource

     Allocates a new tag resource to a company on a hosted Veeam Backup & Replication server resource
    with the specified UID.

    Args:
        company_uid (UUID):
        vbr_hosted_resource_uid (UUID):
        select (str | Unset):
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):
        body (CompanyHostedVbrTagResourceInput):  Example: {'virtualCenterUid':
            '23c54529-5c14-4ebf-aa2c-64f3503a1070', 'virtualServerTag': {'urn':
            'urn:vmomi:InventoryServiceTag:88788f9e-d8f5-4eb4-bc4f-9b3f5403bcec', 'name': 'VSPC',
            'hostUid': '23c54529-5c14-4ebf-aa2c-64f3503a1070', 'hostName': 'vcenter01.tech.local'}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CreateCompanyHostedVbrTagResourceResponse200 | ErrorResponse]
    """

    kwargs = _get_kwargs(
        company_uid=company_uid,
        vbr_hosted_resource_uid=vbr_hosted_resource_uid,
        body=body,
        select=select,
        x_request_id=x_request_id,
        x_client_version=x_client_version,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    company_uid: UUID,
    vbr_hosted_resource_uid: UUID,
    *,
    client: AuthenticatedClient,
    body: CompanyHostedVbrTagResourceInput,
    select: str | Unset = UNSET,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Any | CreateCompanyHostedVbrTagResourceResponse200 | ErrorResponse | None:
    """Create Tag Resource on Company Hosted Server Resource

     Allocates a new tag resource to a company on a hosted Veeam Backup & Replication server resource
    with the specified UID.

    Args:
        company_uid (UUID):
        vbr_hosted_resource_uid (UUID):
        select (str | Unset):
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):
        body (CompanyHostedVbrTagResourceInput):  Example: {'virtualCenterUid':
            '23c54529-5c14-4ebf-aa2c-64f3503a1070', 'virtualServerTag': {'urn':
            'urn:vmomi:InventoryServiceTag:88788f9e-d8f5-4eb4-bc4f-9b3f5403bcec', 'name': 'VSPC',
            'hostUid': '23c54529-5c14-4ebf-aa2c-64f3503a1070', 'hostName': 'vcenter01.tech.local'}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CreateCompanyHostedVbrTagResourceResponse200 | ErrorResponse
    """

    return sync_detailed(
        company_uid=company_uid,
        vbr_hosted_resource_uid=vbr_hosted_resource_uid,
        client=client,
        body=body,
        select=select,
        x_request_id=x_request_id,
        x_client_version=x_client_version,
    ).parsed


async def asyncio_detailed(
    company_uid: UUID,
    vbr_hosted_resource_uid: UUID,
    *,
    client: AuthenticatedClient,
    body: CompanyHostedVbrTagResourceInput,
    select: str | Unset = UNSET,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Response[Any | CreateCompanyHostedVbrTagResourceResponse200 | ErrorResponse]:
    """Create Tag Resource on Company Hosted Server Resource

     Allocates a new tag resource to a company on a hosted Veeam Backup & Replication server resource
    with the specified UID.

    Args:
        company_uid (UUID):
        vbr_hosted_resource_uid (UUID):
        select (str | Unset):
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):
        body (CompanyHostedVbrTagResourceInput):  Example: {'virtualCenterUid':
            '23c54529-5c14-4ebf-aa2c-64f3503a1070', 'virtualServerTag': {'urn':
            'urn:vmomi:InventoryServiceTag:88788f9e-d8f5-4eb4-bc4f-9b3f5403bcec', 'name': 'VSPC',
            'hostUid': '23c54529-5c14-4ebf-aa2c-64f3503a1070', 'hostName': 'vcenter01.tech.local'}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CreateCompanyHostedVbrTagResourceResponse200 | ErrorResponse]
    """

    kwargs = _get_kwargs(
        company_uid=company_uid,
        vbr_hosted_resource_uid=vbr_hosted_resource_uid,
        body=body,
        select=select,
        x_request_id=x_request_id,
        x_client_version=x_client_version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    company_uid: UUID,
    vbr_hosted_resource_uid: UUID,
    *,
    client: AuthenticatedClient,
    body: CompanyHostedVbrTagResourceInput,
    select: str | Unset = UNSET,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Any | CreateCompanyHostedVbrTagResourceResponse200 | ErrorResponse | None:
    """Create Tag Resource on Company Hosted Server Resource

     Allocates a new tag resource to a company on a hosted Veeam Backup & Replication server resource
    with the specified UID.

    Args:
        company_uid (UUID):
        vbr_hosted_resource_uid (UUID):
        select (str | Unset):
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):
        body (CompanyHostedVbrTagResourceInput):  Example: {'virtualCenterUid':
            '23c54529-5c14-4ebf-aa2c-64f3503a1070', 'virtualServerTag': {'urn':
            'urn:vmomi:InventoryServiceTag:88788f9e-d8f5-4eb4-bc4f-9b3f5403bcec', 'name': 'VSPC',
            'hostUid': '23c54529-5c14-4ebf-aa2c-64f3503a1070', 'hostName': 'vcenter01.tech.local'}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CreateCompanyHostedVbrTagResourceResponse200 | ErrorResponse
    """

    return (
        await asyncio_detailed(
            company_uid=company_uid,
            vbr_hosted_resource_uid=vbr_hosted_resource_uid,
            client=client,
            body=body,
            select=select,
            x_request_id=x_request_id,
            x_client_version=x_client_version,
        )
    ).parsed
