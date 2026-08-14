from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.add_existing_public_cloud_azure_appliance_response_200 import (
    AddExistingPublicCloudAzureApplianceResponse200,
)
from ...models.error_response import ErrorResponse
from ...models.public_cloud_azure_add_existing_appliance_input import PublicCloudAzureAddExistingApplianceInput
from ...types import UNSET, Response, Unset


def _get_kwargs(
    site_uid: UUID,
    *,
    body: PublicCloudAzureAddExistingApplianceInput,
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
        "url": "/infrastructure/sites/{site_uid}/publicCloud/azure/appliances/connect".format(
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
) -> AddExistingPublicCloudAzureApplianceResponse200 | Any | ErrorResponse:
    if response.status_code == 200:
        response_200 = AddExistingPublicCloudAzureApplianceResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 202:
        response_202 = cast(Any, None)
        return response_202

    response_default = ErrorResponse.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[AddExistingPublicCloudAzureApplianceResponse200 | Any | ErrorResponse]:
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
    body: PublicCloudAzureAddExistingApplianceInput,
    select: str | Unset = UNSET,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Response[AddExistingPublicCloudAzureApplianceResponse200 | Any | ErrorResponse]:
    """Connect Veeam Backup for Microsoft Azure Appliance

     Connect an existing Veeam Backup for Microsoft Azure appliance registered on a Veeam Cloud Connect
    site with the specified UID.

    Args:
        site_uid (UUID):
        select (str | Unset):
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):
        body (PublicCloudAzureAddExistingApplianceInput):  Example: {'account': {'accountUid':
            '07e5070f-f170-4a89-8e44-206b56692624', 'subscriptionId': '3a485c0d-3911-48a9-94ff-
            fe325503e892', 'dataCenterId': 'westeurope', 'connectionUid':
            'eefa8303-cf95-4912-9ba6-3ba635d2ba86', 'environment': 'Global'}, 'virtualMachine':
            {'virtualMachineId':
            '/subscriptions/13e8e398-9860-4de9-9a0c-290d9724c6bf/resourcegroups/dma-vspc-
            pc/providers/microsoft.compute/virtualmachines/dmavspcazurepluginpermanent',
            'description': 'Existing appliance added.'}, 'network': None, 'guestOsCredentials':
            {'guestOsCredentialsUid': 'e2cfa41f-bc14-41e1-b6a0-2fdb04178e37'}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AddExistingPublicCloudAzureApplianceResponse200 | Any | ErrorResponse]
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
    body: PublicCloudAzureAddExistingApplianceInput,
    select: str | Unset = UNSET,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> AddExistingPublicCloudAzureApplianceResponse200 | Any | ErrorResponse | None:
    """Connect Veeam Backup for Microsoft Azure Appliance

     Connect an existing Veeam Backup for Microsoft Azure appliance registered on a Veeam Cloud Connect
    site with the specified UID.

    Args:
        site_uid (UUID):
        select (str | Unset):
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):
        body (PublicCloudAzureAddExistingApplianceInput):  Example: {'account': {'accountUid':
            '07e5070f-f170-4a89-8e44-206b56692624', 'subscriptionId': '3a485c0d-3911-48a9-94ff-
            fe325503e892', 'dataCenterId': 'westeurope', 'connectionUid':
            'eefa8303-cf95-4912-9ba6-3ba635d2ba86', 'environment': 'Global'}, 'virtualMachine':
            {'virtualMachineId':
            '/subscriptions/13e8e398-9860-4de9-9a0c-290d9724c6bf/resourcegroups/dma-vspc-
            pc/providers/microsoft.compute/virtualmachines/dmavspcazurepluginpermanent',
            'description': 'Existing appliance added.'}, 'network': None, 'guestOsCredentials':
            {'guestOsCredentialsUid': 'e2cfa41f-bc14-41e1-b6a0-2fdb04178e37'}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AddExistingPublicCloudAzureApplianceResponse200 | Any | ErrorResponse
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
    body: PublicCloudAzureAddExistingApplianceInput,
    select: str | Unset = UNSET,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Response[AddExistingPublicCloudAzureApplianceResponse200 | Any | ErrorResponse]:
    """Connect Veeam Backup for Microsoft Azure Appliance

     Connect an existing Veeam Backup for Microsoft Azure appliance registered on a Veeam Cloud Connect
    site with the specified UID.

    Args:
        site_uid (UUID):
        select (str | Unset):
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):
        body (PublicCloudAzureAddExistingApplianceInput):  Example: {'account': {'accountUid':
            '07e5070f-f170-4a89-8e44-206b56692624', 'subscriptionId': '3a485c0d-3911-48a9-94ff-
            fe325503e892', 'dataCenterId': 'westeurope', 'connectionUid':
            'eefa8303-cf95-4912-9ba6-3ba635d2ba86', 'environment': 'Global'}, 'virtualMachine':
            {'virtualMachineId':
            '/subscriptions/13e8e398-9860-4de9-9a0c-290d9724c6bf/resourcegroups/dma-vspc-
            pc/providers/microsoft.compute/virtualmachines/dmavspcazurepluginpermanent',
            'description': 'Existing appliance added.'}, 'network': None, 'guestOsCredentials':
            {'guestOsCredentialsUid': 'e2cfa41f-bc14-41e1-b6a0-2fdb04178e37'}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AddExistingPublicCloudAzureApplianceResponse200 | Any | ErrorResponse]
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
    body: PublicCloudAzureAddExistingApplianceInput,
    select: str | Unset = UNSET,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> AddExistingPublicCloudAzureApplianceResponse200 | Any | ErrorResponse | None:
    """Connect Veeam Backup for Microsoft Azure Appliance

     Connect an existing Veeam Backup for Microsoft Azure appliance registered on a Veeam Cloud Connect
    site with the specified UID.

    Args:
        site_uid (UUID):
        select (str | Unset):
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):
        body (PublicCloudAzureAddExistingApplianceInput):  Example: {'account': {'accountUid':
            '07e5070f-f170-4a89-8e44-206b56692624', 'subscriptionId': '3a485c0d-3911-48a9-94ff-
            fe325503e892', 'dataCenterId': 'westeurope', 'connectionUid':
            'eefa8303-cf95-4912-9ba6-3ba635d2ba86', 'environment': 'Global'}, 'virtualMachine':
            {'virtualMachineId':
            '/subscriptions/13e8e398-9860-4de9-9a0c-290d9724c6bf/resourcegroups/dma-vspc-
            pc/providers/microsoft.compute/virtualmachines/dmavspcazurepluginpermanent',
            'description': 'Existing appliance added.'}, 'network': None, 'guestOsCredentials':
            {'guestOsCredentialsUid': 'e2cfa41f-bc14-41e1-b6a0-2fdb04178e37'}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AddExistingPublicCloudAzureApplianceResponse200 | Any | ErrorResponse
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
