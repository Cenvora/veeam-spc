from http import HTTPStatus
from typing import Any, cast
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.company_input import CompanyInput
from ...models.create_company_response_200 import CreateCompanyResponse200
from ...models.error_response import ErrorResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: CompanyInput,
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
        "url": "/organizations/companies",
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | CreateCompanyResponse200 | ErrorResponse:
    if response.status_code == 200:
        response_200 = CreateCompanyResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 202:
        response_202 = cast(Any, None)
        return response_202

    response_default = ErrorResponse.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | CreateCompanyResponse200 | ErrorResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: CompanyInput,
    select: str | Unset = UNSET,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Response[Any | CreateCompanyResponse200 | ErrorResponse]:
    """Create Company

     Creates a new company managed in Veeam Service Provider Console.

    Args:
        select (str | Unset):
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):
        body (CompanyInput):  Example: {'resellerUid': 'ae61e533-82c7-4cb6-a030-78ae589cf49d',
            'organizationInput': {'name': 'Alpha', 'alias': 'alpha', 'taxId': '643-70-9745',
            'legalName': 'Alpha Holdings, Inc.', 'email': 's.smith@alpha.com', 'phone':
            '906-284-7082', 'country': 1, 'state': 22, 'countryName': 'USA', 'regionName': 'Midwest',
            'city': 'Marquette', 'street': '4493 Railroad Street', 'locationAdmin0Code': None,
            'locationAdmin1Code': None, 'locationAdmin2Code': None, 'notes': None, 'zipCode': '49855',
            'domain': 'alpha.com', 'website': 'www.alpha.com', 'veeamTenantId': None, 'companyId':
            None}, 'subscriptionPlanUid': None, 'isRestAccessEnabled': True, 'isAlarmDetectEnabled':
            False, 'companyServices': {'hostedServices': {'isVbPublicCloudManagementEnabled': False},
            'remoteServices': {'isBackupResourcesEnabled': True, 'backupAgentsManagement': None,
            'backupServersManagement': None, 'vb365ServersManagement': None,
            'isVbPublicCloudManagementEnabled': False}}, 'ownerCredentials': {'userName':
            'alphaowner', 'password': 'Password1'}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CreateCompanyResponse200 | ErrorResponse]
    """

    kwargs = _get_kwargs(
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
    *,
    client: AuthenticatedClient,
    body: CompanyInput,
    select: str | Unset = UNSET,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Any | CreateCompanyResponse200 | ErrorResponse | None:
    """Create Company

     Creates a new company managed in Veeam Service Provider Console.

    Args:
        select (str | Unset):
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):
        body (CompanyInput):  Example: {'resellerUid': 'ae61e533-82c7-4cb6-a030-78ae589cf49d',
            'organizationInput': {'name': 'Alpha', 'alias': 'alpha', 'taxId': '643-70-9745',
            'legalName': 'Alpha Holdings, Inc.', 'email': 's.smith@alpha.com', 'phone':
            '906-284-7082', 'country': 1, 'state': 22, 'countryName': 'USA', 'regionName': 'Midwest',
            'city': 'Marquette', 'street': '4493 Railroad Street', 'locationAdmin0Code': None,
            'locationAdmin1Code': None, 'locationAdmin2Code': None, 'notes': None, 'zipCode': '49855',
            'domain': 'alpha.com', 'website': 'www.alpha.com', 'veeamTenantId': None, 'companyId':
            None}, 'subscriptionPlanUid': None, 'isRestAccessEnabled': True, 'isAlarmDetectEnabled':
            False, 'companyServices': {'hostedServices': {'isVbPublicCloudManagementEnabled': False},
            'remoteServices': {'isBackupResourcesEnabled': True, 'backupAgentsManagement': None,
            'backupServersManagement': None, 'vb365ServersManagement': None,
            'isVbPublicCloudManagementEnabled': False}}, 'ownerCredentials': {'userName':
            'alphaowner', 'password': 'Password1'}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CreateCompanyResponse200 | ErrorResponse
    """

    return sync_detailed(
        client=client,
        body=body,
        select=select,
        x_request_id=x_request_id,
        x_client_version=x_client_version,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: CompanyInput,
    select: str | Unset = UNSET,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Response[Any | CreateCompanyResponse200 | ErrorResponse]:
    """Create Company

     Creates a new company managed in Veeam Service Provider Console.

    Args:
        select (str | Unset):
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):
        body (CompanyInput):  Example: {'resellerUid': 'ae61e533-82c7-4cb6-a030-78ae589cf49d',
            'organizationInput': {'name': 'Alpha', 'alias': 'alpha', 'taxId': '643-70-9745',
            'legalName': 'Alpha Holdings, Inc.', 'email': 's.smith@alpha.com', 'phone':
            '906-284-7082', 'country': 1, 'state': 22, 'countryName': 'USA', 'regionName': 'Midwest',
            'city': 'Marquette', 'street': '4493 Railroad Street', 'locationAdmin0Code': None,
            'locationAdmin1Code': None, 'locationAdmin2Code': None, 'notes': None, 'zipCode': '49855',
            'domain': 'alpha.com', 'website': 'www.alpha.com', 'veeamTenantId': None, 'companyId':
            None}, 'subscriptionPlanUid': None, 'isRestAccessEnabled': True, 'isAlarmDetectEnabled':
            False, 'companyServices': {'hostedServices': {'isVbPublicCloudManagementEnabled': False},
            'remoteServices': {'isBackupResourcesEnabled': True, 'backupAgentsManagement': None,
            'backupServersManagement': None, 'vb365ServersManagement': None,
            'isVbPublicCloudManagementEnabled': False}}, 'ownerCredentials': {'userName':
            'alphaowner', 'password': 'Password1'}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CreateCompanyResponse200 | ErrorResponse]
    """

    kwargs = _get_kwargs(
        body=body,
        select=select,
        x_request_id=x_request_id,
        x_client_version=x_client_version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: CompanyInput,
    select: str | Unset = UNSET,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Any | CreateCompanyResponse200 | ErrorResponse | None:
    """Create Company

     Creates a new company managed in Veeam Service Provider Console.

    Args:
        select (str | Unset):
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):
        body (CompanyInput):  Example: {'resellerUid': 'ae61e533-82c7-4cb6-a030-78ae589cf49d',
            'organizationInput': {'name': 'Alpha', 'alias': 'alpha', 'taxId': '643-70-9745',
            'legalName': 'Alpha Holdings, Inc.', 'email': 's.smith@alpha.com', 'phone':
            '906-284-7082', 'country': 1, 'state': 22, 'countryName': 'USA', 'regionName': 'Midwest',
            'city': 'Marquette', 'street': '4493 Railroad Street', 'locationAdmin0Code': None,
            'locationAdmin1Code': None, 'locationAdmin2Code': None, 'notes': None, 'zipCode': '49855',
            'domain': 'alpha.com', 'website': 'www.alpha.com', 'veeamTenantId': None, 'companyId':
            None}, 'subscriptionPlanUid': None, 'isRestAccessEnabled': True, 'isAlarmDetectEnabled':
            False, 'companyServices': {'hostedServices': {'isVbPublicCloudManagementEnabled': False},
            'remoteServices': {'isBackupResourcesEnabled': True, 'backupAgentsManagement': None,
            'backupServersManagement': None, 'vb365ServersManagement': None,
            'isVbPublicCloudManagementEnabled': False}}, 'ownerCredentials': {'userName':
            'alphaowner', 'password': 'Password1'}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CreateCompanyResponse200 | ErrorResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            select=select,
            x_request_id=x_request_id,
            x_client_version=x_client_version,
        )
    ).parsed
