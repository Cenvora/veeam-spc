from http import HTTPStatus
from typing import Any, Optional, Union, cast
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.create_identity_provider_rule_response_200 import CreateIdentityProviderRuleResponse200
from ...models.error_response import ErrorResponse
from ...models.identity_provider_role_mapping_rule import IdentityProviderRoleMappingRule
from ...types import UNSET, Response, Unset


def _get_kwargs(
    organization_uid: UUID,
    identity_provider_name: str,
    *,
    body: IdentityProviderRoleMappingRule,
    x_request_id: Union[Unset, UUID] = UNSET,
    x_client_version: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_request_id, Unset):
        headers["X-Request-id"] = x_request_id

    if not isinstance(x_client_version, Unset):
        headers["X-Client-Version"] = x_client_version

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/organizations/{organization_uid}/identityProviders/{identity_provider_name}/rules",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Union[Any, CreateIdentityProviderRuleResponse200, ErrorResponse]:
    if response.status_code == 200:
        response_200 = CreateIdentityProviderRuleResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 202:
        response_202 = cast(Any, None)
        return response_202

    response_default = ErrorResponse.from_dict(response.json())

    return response_default


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, CreateIdentityProviderRuleResponse200, ErrorResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    organization_uid: UUID,
    identity_provider_name: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: IdentityProviderRoleMappingRule,
    x_request_id: Union[Unset, UUID] = UNSET,
    x_client_version: Union[Unset, str] = UNSET,
) -> Response[Union[Any, CreateIdentityProviderRuleResponse200, ErrorResponse]]:
    """Create Mapping Rule for Organization Identity Provider

     Creates mapping rule for an organization identity provider with the specified name.

    Args:
        organization_uid (UUID):
        identity_provider_name (str):
        x_request_id (Union[Unset, UUID]):
        x_client_version (Union[Unset, str]):
        body (IdentityProviderRoleMappingRule):  Example: {'name': 'Portal operators',
            'desciption': 'Portal operators from ADFS', 'role': 'PortalOperator',
            'managedCompaniesUids': ['ab452a99-51bf-4a40-a1c4-df01506f56a3',
            'd8ba8d10-f2fb-4592-8c41-184d0e1b03f1'], 'organizationMappingSourceClaimType':
            'http://schemas.xmlsoap.org/ws/2005/05/identity/claims/ComanyNameAndAlias',
            'additionalMappings': [{'claimType':
            'http://schemas.xmlsoap.org/ws/2005/05/identity/claims/emailaddress', 'operator':
            'Contains', 'value': '@mycompany.com', 'matchCase': False}], 'attributeMappings':
            [{'claimType': 'http://schemas.xmlsoap.org/ws/2005/05/identity/claims/firstName',
            'allowAliases': True, 'attribute': 'FirstName'}, {'claimType':
            'http://schemas.xmlsoap.org/ws/2005/05/identity/claims/lastName', 'allowAliases': True,
            'attribute': 'LastName'}, {'claimType':
            'http://schemas.xmlsoap.org/ws/2005/05/identity/claims/name', 'allowAliases': True,
            'attribute': 'Name'}, {'claimType':
            'http://schemas.xmlsoap.org/ws/2005/05/identity/claims/address', 'allowAliases': True,
            'attribute': 'Address'}, {'claimType':
            'http://schemas.xmlsoap.org/ws/2005/05/identity/claims/phone', 'allowAliases': True,
            'attribute': 'Phone'}], 'providerInfo': {'name': 'adfs', 'displayName': 'Microsoft Entra
            ID Federation Services', 'template': 'ADFS', 'type': 'SAML2', 'organizationUid':
            '0242e3ca-1cc2-4d90-8285-0e7a9b375418', 'enabled': True}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, CreateIdentityProviderRuleResponse200, ErrorResponse]]
    """

    kwargs = _get_kwargs(
        organization_uid=organization_uid,
        identity_provider_name=identity_provider_name,
        body=body,
        x_request_id=x_request_id,
        x_client_version=x_client_version,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    organization_uid: UUID,
    identity_provider_name: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: IdentityProviderRoleMappingRule,
    x_request_id: Union[Unset, UUID] = UNSET,
    x_client_version: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, CreateIdentityProviderRuleResponse200, ErrorResponse]]:
    """Create Mapping Rule for Organization Identity Provider

     Creates mapping rule for an organization identity provider with the specified name.

    Args:
        organization_uid (UUID):
        identity_provider_name (str):
        x_request_id (Union[Unset, UUID]):
        x_client_version (Union[Unset, str]):
        body (IdentityProviderRoleMappingRule):  Example: {'name': 'Portal operators',
            'desciption': 'Portal operators from ADFS', 'role': 'PortalOperator',
            'managedCompaniesUids': ['ab452a99-51bf-4a40-a1c4-df01506f56a3',
            'd8ba8d10-f2fb-4592-8c41-184d0e1b03f1'], 'organizationMappingSourceClaimType':
            'http://schemas.xmlsoap.org/ws/2005/05/identity/claims/ComanyNameAndAlias',
            'additionalMappings': [{'claimType':
            'http://schemas.xmlsoap.org/ws/2005/05/identity/claims/emailaddress', 'operator':
            'Contains', 'value': '@mycompany.com', 'matchCase': False}], 'attributeMappings':
            [{'claimType': 'http://schemas.xmlsoap.org/ws/2005/05/identity/claims/firstName',
            'allowAliases': True, 'attribute': 'FirstName'}, {'claimType':
            'http://schemas.xmlsoap.org/ws/2005/05/identity/claims/lastName', 'allowAliases': True,
            'attribute': 'LastName'}, {'claimType':
            'http://schemas.xmlsoap.org/ws/2005/05/identity/claims/name', 'allowAliases': True,
            'attribute': 'Name'}, {'claimType':
            'http://schemas.xmlsoap.org/ws/2005/05/identity/claims/address', 'allowAliases': True,
            'attribute': 'Address'}, {'claimType':
            'http://schemas.xmlsoap.org/ws/2005/05/identity/claims/phone', 'allowAliases': True,
            'attribute': 'Phone'}], 'providerInfo': {'name': 'adfs', 'displayName': 'Microsoft Entra
            ID Federation Services', 'template': 'ADFS', 'type': 'SAML2', 'organizationUid':
            '0242e3ca-1cc2-4d90-8285-0e7a9b375418', 'enabled': True}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, CreateIdentityProviderRuleResponse200, ErrorResponse]
    """

    return sync_detailed(
        organization_uid=organization_uid,
        identity_provider_name=identity_provider_name,
        client=client,
        body=body,
        x_request_id=x_request_id,
        x_client_version=x_client_version,
    ).parsed


async def asyncio_detailed(
    organization_uid: UUID,
    identity_provider_name: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: IdentityProviderRoleMappingRule,
    x_request_id: Union[Unset, UUID] = UNSET,
    x_client_version: Union[Unset, str] = UNSET,
) -> Response[Union[Any, CreateIdentityProviderRuleResponse200, ErrorResponse]]:
    """Create Mapping Rule for Organization Identity Provider

     Creates mapping rule for an organization identity provider with the specified name.

    Args:
        organization_uid (UUID):
        identity_provider_name (str):
        x_request_id (Union[Unset, UUID]):
        x_client_version (Union[Unset, str]):
        body (IdentityProviderRoleMappingRule):  Example: {'name': 'Portal operators',
            'desciption': 'Portal operators from ADFS', 'role': 'PortalOperator',
            'managedCompaniesUids': ['ab452a99-51bf-4a40-a1c4-df01506f56a3',
            'd8ba8d10-f2fb-4592-8c41-184d0e1b03f1'], 'organizationMappingSourceClaimType':
            'http://schemas.xmlsoap.org/ws/2005/05/identity/claims/ComanyNameAndAlias',
            'additionalMappings': [{'claimType':
            'http://schemas.xmlsoap.org/ws/2005/05/identity/claims/emailaddress', 'operator':
            'Contains', 'value': '@mycompany.com', 'matchCase': False}], 'attributeMappings':
            [{'claimType': 'http://schemas.xmlsoap.org/ws/2005/05/identity/claims/firstName',
            'allowAliases': True, 'attribute': 'FirstName'}, {'claimType':
            'http://schemas.xmlsoap.org/ws/2005/05/identity/claims/lastName', 'allowAliases': True,
            'attribute': 'LastName'}, {'claimType':
            'http://schemas.xmlsoap.org/ws/2005/05/identity/claims/name', 'allowAliases': True,
            'attribute': 'Name'}, {'claimType':
            'http://schemas.xmlsoap.org/ws/2005/05/identity/claims/address', 'allowAliases': True,
            'attribute': 'Address'}, {'claimType':
            'http://schemas.xmlsoap.org/ws/2005/05/identity/claims/phone', 'allowAliases': True,
            'attribute': 'Phone'}], 'providerInfo': {'name': 'adfs', 'displayName': 'Microsoft Entra
            ID Federation Services', 'template': 'ADFS', 'type': 'SAML2', 'organizationUid':
            '0242e3ca-1cc2-4d90-8285-0e7a9b375418', 'enabled': True}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, CreateIdentityProviderRuleResponse200, ErrorResponse]]
    """

    kwargs = _get_kwargs(
        organization_uid=organization_uid,
        identity_provider_name=identity_provider_name,
        body=body,
        x_request_id=x_request_id,
        x_client_version=x_client_version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    organization_uid: UUID,
    identity_provider_name: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: IdentityProviderRoleMappingRule,
    x_request_id: Union[Unset, UUID] = UNSET,
    x_client_version: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, CreateIdentityProviderRuleResponse200, ErrorResponse]]:
    """Create Mapping Rule for Organization Identity Provider

     Creates mapping rule for an organization identity provider with the specified name.

    Args:
        organization_uid (UUID):
        identity_provider_name (str):
        x_request_id (Union[Unset, UUID]):
        x_client_version (Union[Unset, str]):
        body (IdentityProviderRoleMappingRule):  Example: {'name': 'Portal operators',
            'desciption': 'Portal operators from ADFS', 'role': 'PortalOperator',
            'managedCompaniesUids': ['ab452a99-51bf-4a40-a1c4-df01506f56a3',
            'd8ba8d10-f2fb-4592-8c41-184d0e1b03f1'], 'organizationMappingSourceClaimType':
            'http://schemas.xmlsoap.org/ws/2005/05/identity/claims/ComanyNameAndAlias',
            'additionalMappings': [{'claimType':
            'http://schemas.xmlsoap.org/ws/2005/05/identity/claims/emailaddress', 'operator':
            'Contains', 'value': '@mycompany.com', 'matchCase': False}], 'attributeMappings':
            [{'claimType': 'http://schemas.xmlsoap.org/ws/2005/05/identity/claims/firstName',
            'allowAliases': True, 'attribute': 'FirstName'}, {'claimType':
            'http://schemas.xmlsoap.org/ws/2005/05/identity/claims/lastName', 'allowAliases': True,
            'attribute': 'LastName'}, {'claimType':
            'http://schemas.xmlsoap.org/ws/2005/05/identity/claims/name', 'allowAliases': True,
            'attribute': 'Name'}, {'claimType':
            'http://schemas.xmlsoap.org/ws/2005/05/identity/claims/address', 'allowAliases': True,
            'attribute': 'Address'}, {'claimType':
            'http://schemas.xmlsoap.org/ws/2005/05/identity/claims/phone', 'allowAliases': True,
            'attribute': 'Phone'}], 'providerInfo': {'name': 'adfs', 'displayName': 'Microsoft Entra
            ID Federation Services', 'template': 'ADFS', 'type': 'SAML2', 'organizationUid':
            '0242e3ca-1cc2-4d90-8285-0e7a9b375418', 'enabled': True}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, CreateIdentityProviderRuleResponse200, ErrorResponse]
    """

    return (
        await asyncio_detailed(
            organization_uid=organization_uid,
            identity_provider_name=identity_provider_name,
            client=client,
            body=body,
            x_request_id=x_request_id,
            x_client_version=x_client_version,
        )
    ).parsed
