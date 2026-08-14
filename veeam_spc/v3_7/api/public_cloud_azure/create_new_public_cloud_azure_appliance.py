from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.create_new_public_cloud_azure_appliance_response_200 import CreateNewPublicCloudAzureApplianceResponse200
from ...models.error_response import ErrorResponse
from ...models.public_cloud_azure_new_appliance_input import PublicCloudAzureNewApplianceInput
from ...types import UNSET, Response, Unset


def _get_kwargs(
    site_uid: UUID,
    *,
    body: PublicCloudAzureNewApplianceInput,
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
        "url": "/infrastructure/sites/{site_uid}/publicCloud/azure/appliances/deploy".format(
            site_uid=quote(str(site_uid), safe=""),
        ),
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | CreateNewPublicCloudAzureApplianceResponse200 | ErrorResponse:
    if response.status_code == 200:
        response_200 = CreateNewPublicCloudAzureApplianceResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 202:
        response_202 = cast(Any, None)
        return response_202

    response_default = ErrorResponse.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | CreateNewPublicCloudAzureApplianceResponse200 | ErrorResponse]:
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
    body: PublicCloudAzureNewApplianceInput,
    select: str | Unset = UNSET,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Response[Any | CreateNewPublicCloudAzureApplianceResponse200 | ErrorResponse]:
    """Create Veeam Backup for Microsoft Azure Appliance

     Creates a new Veeam Backup for Microsoft Azure appliance regitered on a Veeam Cloud Connect site
    with the specified UID.

    Args:
        site_uid (UUID):
        select (str | Unset):
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):
        body (PublicCloudAzureNewApplianceInput):  Example: {'account': {'connectionUid':
            'de26c441-b776-4aff-bcc3-9f8336d06b1a', 'environment': 'Global', 'resourceGroupName':
            'dma-vspc-pc', 'subscriptionId': '0381fa98-9d97-4b9a-923a-4746bdd9fbcb', 'dataCenterId':
            'westeurope', 'accountUid': '91bd2d80-e9ba-4a62-9b3a-2f6ee26a40ba'}, 'virtualMachine':
            {'virtualMachineName': 'dmaVspcAzurePluginTemporary', 'description': 'Created at [1:47:35
            PM] by [PortalAdministrator]'}, 'network': {'networkId':
            '/subscriptions/0381fa98-9d97-4b9a-923a-4746bdd9fbcb/resourcegroups/dma-vspc-
            pc/providers/microsoft.network/virtualnetworks/dma-vspc-pc-net', 'subnetName': 'default',
            'securityGroupId':
            '/subscriptions/0381fa98-9d97-4b9a-923a-4746bdd9fbcb/resourcegroups/dma-vspc-
            pc/providers/microsoft.network/networksecuritygroups/dma-vspc-pc-sg'}, 'ipAddress':
            {'backupServerIpAddresses': '89.296.226.25', 'applianceIp': {'applianceIpAddressId': None,
            'newIpAddressType': 'dynamic'}}, 'guestOsCredentials': {'guestOsCredentialsUid':
            'f7d20bb9-4c56-46d6-aedc-738e77d104a2', 'keyPairName': 'dma-vspc-azure-plugin',
            'timeZoneId': 'Etc/GMT+2'}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CreateNewPublicCloudAzureApplianceResponse200 | ErrorResponse]
    """

    kwargs = _get_kwargs(
        site_uid=site_uid,
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
    site_uid: UUID,
    *,
    client: AuthenticatedClient,
    body: PublicCloudAzureNewApplianceInput,
    select: str | Unset = UNSET,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Any | CreateNewPublicCloudAzureApplianceResponse200 | ErrorResponse | None:
    """Create Veeam Backup for Microsoft Azure Appliance

     Creates a new Veeam Backup for Microsoft Azure appliance regitered on a Veeam Cloud Connect site
    with the specified UID.

    Args:
        site_uid (UUID):
        select (str | Unset):
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):
        body (PublicCloudAzureNewApplianceInput):  Example: {'account': {'connectionUid':
            'de26c441-b776-4aff-bcc3-9f8336d06b1a', 'environment': 'Global', 'resourceGroupName':
            'dma-vspc-pc', 'subscriptionId': '0381fa98-9d97-4b9a-923a-4746bdd9fbcb', 'dataCenterId':
            'westeurope', 'accountUid': '91bd2d80-e9ba-4a62-9b3a-2f6ee26a40ba'}, 'virtualMachine':
            {'virtualMachineName': 'dmaVspcAzurePluginTemporary', 'description': 'Created at [1:47:35
            PM] by [PortalAdministrator]'}, 'network': {'networkId':
            '/subscriptions/0381fa98-9d97-4b9a-923a-4746bdd9fbcb/resourcegroups/dma-vspc-
            pc/providers/microsoft.network/virtualnetworks/dma-vspc-pc-net', 'subnetName': 'default',
            'securityGroupId':
            '/subscriptions/0381fa98-9d97-4b9a-923a-4746bdd9fbcb/resourcegroups/dma-vspc-
            pc/providers/microsoft.network/networksecuritygroups/dma-vspc-pc-sg'}, 'ipAddress':
            {'backupServerIpAddresses': '89.296.226.25', 'applianceIp': {'applianceIpAddressId': None,
            'newIpAddressType': 'dynamic'}}, 'guestOsCredentials': {'guestOsCredentialsUid':
            'f7d20bb9-4c56-46d6-aedc-738e77d104a2', 'keyPairName': 'dma-vspc-azure-plugin',
            'timeZoneId': 'Etc/GMT+2'}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CreateNewPublicCloudAzureApplianceResponse200 | ErrorResponse
    """

    return sync_detailed(
        site_uid=site_uid,
        client=client,
        body=body,
        select=select,
        x_request_id=x_request_id,
        x_client_version=x_client_version,
    ).parsed


async def asyncio_detailed(
    site_uid: UUID,
    *,
    client: AuthenticatedClient,
    body: PublicCloudAzureNewApplianceInput,
    select: str | Unset = UNSET,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Response[Any | CreateNewPublicCloudAzureApplianceResponse200 | ErrorResponse]:
    """Create Veeam Backup for Microsoft Azure Appliance

     Creates a new Veeam Backup for Microsoft Azure appliance regitered on a Veeam Cloud Connect site
    with the specified UID.

    Args:
        site_uid (UUID):
        select (str | Unset):
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):
        body (PublicCloudAzureNewApplianceInput):  Example: {'account': {'connectionUid':
            'de26c441-b776-4aff-bcc3-9f8336d06b1a', 'environment': 'Global', 'resourceGroupName':
            'dma-vspc-pc', 'subscriptionId': '0381fa98-9d97-4b9a-923a-4746bdd9fbcb', 'dataCenterId':
            'westeurope', 'accountUid': '91bd2d80-e9ba-4a62-9b3a-2f6ee26a40ba'}, 'virtualMachine':
            {'virtualMachineName': 'dmaVspcAzurePluginTemporary', 'description': 'Created at [1:47:35
            PM] by [PortalAdministrator]'}, 'network': {'networkId':
            '/subscriptions/0381fa98-9d97-4b9a-923a-4746bdd9fbcb/resourcegroups/dma-vspc-
            pc/providers/microsoft.network/virtualnetworks/dma-vspc-pc-net', 'subnetName': 'default',
            'securityGroupId':
            '/subscriptions/0381fa98-9d97-4b9a-923a-4746bdd9fbcb/resourcegroups/dma-vspc-
            pc/providers/microsoft.network/networksecuritygroups/dma-vspc-pc-sg'}, 'ipAddress':
            {'backupServerIpAddresses': '89.296.226.25', 'applianceIp': {'applianceIpAddressId': None,
            'newIpAddressType': 'dynamic'}}, 'guestOsCredentials': {'guestOsCredentialsUid':
            'f7d20bb9-4c56-46d6-aedc-738e77d104a2', 'keyPairName': 'dma-vspc-azure-plugin',
            'timeZoneId': 'Etc/GMT+2'}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CreateNewPublicCloudAzureApplianceResponse200 | ErrorResponse]
    """

    kwargs = _get_kwargs(
        site_uid=site_uid,
        body=body,
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
    body: PublicCloudAzureNewApplianceInput,
    select: str | Unset = UNSET,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Any | CreateNewPublicCloudAzureApplianceResponse200 | ErrorResponse | None:
    """Create Veeam Backup for Microsoft Azure Appliance

     Creates a new Veeam Backup for Microsoft Azure appliance regitered on a Veeam Cloud Connect site
    with the specified UID.

    Args:
        site_uid (UUID):
        select (str | Unset):
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):
        body (PublicCloudAzureNewApplianceInput):  Example: {'account': {'connectionUid':
            'de26c441-b776-4aff-bcc3-9f8336d06b1a', 'environment': 'Global', 'resourceGroupName':
            'dma-vspc-pc', 'subscriptionId': '0381fa98-9d97-4b9a-923a-4746bdd9fbcb', 'dataCenterId':
            'westeurope', 'accountUid': '91bd2d80-e9ba-4a62-9b3a-2f6ee26a40ba'}, 'virtualMachine':
            {'virtualMachineName': 'dmaVspcAzurePluginTemporary', 'description': 'Created at [1:47:35
            PM] by [PortalAdministrator]'}, 'network': {'networkId':
            '/subscriptions/0381fa98-9d97-4b9a-923a-4746bdd9fbcb/resourcegroups/dma-vspc-
            pc/providers/microsoft.network/virtualnetworks/dma-vspc-pc-net', 'subnetName': 'default',
            'securityGroupId':
            '/subscriptions/0381fa98-9d97-4b9a-923a-4746bdd9fbcb/resourcegroups/dma-vspc-
            pc/providers/microsoft.network/networksecuritygroups/dma-vspc-pc-sg'}, 'ipAddress':
            {'backupServerIpAddresses': '89.296.226.25', 'applianceIp': {'applianceIpAddressId': None,
            'newIpAddressType': 'dynamic'}}, 'guestOsCredentials': {'guestOsCredentialsUid':
            'f7d20bb9-4c56-46d6-aedc-738e77d104a2', 'keyPairName': 'dma-vspc-azure-plugin',
            'timeZoneId': 'Etc/GMT+2'}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CreateNewPublicCloudAzureApplianceResponse200 | ErrorResponse
    """

    return (
        await asyncio_detailed(
            site_uid=site_uid,
            client=client,
            body=body,
            select=select,
            x_request_id=x_request_id,
            x_client_version=x_client_version,
        )
    ).parsed
