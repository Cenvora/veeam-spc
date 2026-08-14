from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.create_new_public_cloud_aws_appliance_response_200 import CreateNewPublicCloudAwsApplianceResponse200
from ...models.error_response import ErrorResponse
from ...models.public_cloud_aws_new_appliance_input import PublicCloudAwsNewApplianceInput
from ...types import UNSET, Response, Unset


def _get_kwargs(
    site_uid: UUID,
    *,
    body: PublicCloudAwsNewApplianceInput,
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
        "url": "/infrastructure/sites/{site_uid}/publicCloud/aws/appliances/deploy".format(
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
) -> Any | CreateNewPublicCloudAwsApplianceResponse200 | ErrorResponse:
    if response.status_code == 200:
        response_200 = CreateNewPublicCloudAwsApplianceResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 202:
        response_202 = cast(Any, None)
        return response_202

    response_default = ErrorResponse.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | CreateNewPublicCloudAwsApplianceResponse200 | ErrorResponse]:
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
    body: PublicCloudAwsNewApplianceInput,
    select: str | Unset = UNSET,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Response[Any | CreateNewPublicCloudAwsApplianceResponse200 | ErrorResponse]:
    """Create Veeam Backup for AWS Appliance

     Creates a new Veeam Backup for AWS appliance registered on a Veeam Cloud Connect site with the
    specified UID.

    Args:
        site_uid (UUID):
        select (str | Unset):
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):
        body (PublicCloudAwsNewApplianceInput):  Example: {'account': {'connectionUid':
            'c0300e84-e8c0-40df-97f1-cbdbdcecafa9', 'accountUid':
            '73f86291-d5ff-423c-88da-9b60be21964d', 'dataCenterId': 'eu-central-1', 'regionId':
            'Global'}, 'virtualMachine': {'virtualMachineName': 'dma12', 'description': 'Created at
            [1:19:55 PM] by [PortalAdministrator]'}, 'network': {'networkId': 'vpc-09ae9e55dd75a5f6b',
            'subnetId': 'subnet-0b2131c783c96c1f9', 'securityGroupId': 'sg-0ad0a345b8059c199'},
            'ipAddress': {'applianceIp': {'applianceIpAddressId': None, 'newIpAddressType':
            'dynamic'}, 'backupServerIpAddresses': '89.185.226.14/32'}, 'guestOsCredentials':
            {'guestOsCredentialsUid': '18f0a96a-16e1-4b27-ace3-307fd65da25a', 'keyPairName':
            'VeeamDefaultKeyPair', 'timeZoneId': 'Europe/Prague'}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CreateNewPublicCloudAwsApplianceResponse200 | ErrorResponse]
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
    body: PublicCloudAwsNewApplianceInput,
    select: str | Unset = UNSET,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Any | CreateNewPublicCloudAwsApplianceResponse200 | ErrorResponse | None:
    """Create Veeam Backup for AWS Appliance

     Creates a new Veeam Backup for AWS appliance registered on a Veeam Cloud Connect site with the
    specified UID.

    Args:
        site_uid (UUID):
        select (str | Unset):
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):
        body (PublicCloudAwsNewApplianceInput):  Example: {'account': {'connectionUid':
            'c0300e84-e8c0-40df-97f1-cbdbdcecafa9', 'accountUid':
            '73f86291-d5ff-423c-88da-9b60be21964d', 'dataCenterId': 'eu-central-1', 'regionId':
            'Global'}, 'virtualMachine': {'virtualMachineName': 'dma12', 'description': 'Created at
            [1:19:55 PM] by [PortalAdministrator]'}, 'network': {'networkId': 'vpc-09ae9e55dd75a5f6b',
            'subnetId': 'subnet-0b2131c783c96c1f9', 'securityGroupId': 'sg-0ad0a345b8059c199'},
            'ipAddress': {'applianceIp': {'applianceIpAddressId': None, 'newIpAddressType':
            'dynamic'}, 'backupServerIpAddresses': '89.185.226.14/32'}, 'guestOsCredentials':
            {'guestOsCredentialsUid': '18f0a96a-16e1-4b27-ace3-307fd65da25a', 'keyPairName':
            'VeeamDefaultKeyPair', 'timeZoneId': 'Europe/Prague'}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CreateNewPublicCloudAwsApplianceResponse200 | ErrorResponse
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
    body: PublicCloudAwsNewApplianceInput,
    select: str | Unset = UNSET,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Response[Any | CreateNewPublicCloudAwsApplianceResponse200 | ErrorResponse]:
    """Create Veeam Backup for AWS Appliance

     Creates a new Veeam Backup for AWS appliance registered on a Veeam Cloud Connect site with the
    specified UID.

    Args:
        site_uid (UUID):
        select (str | Unset):
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):
        body (PublicCloudAwsNewApplianceInput):  Example: {'account': {'connectionUid':
            'c0300e84-e8c0-40df-97f1-cbdbdcecafa9', 'accountUid':
            '73f86291-d5ff-423c-88da-9b60be21964d', 'dataCenterId': 'eu-central-1', 'regionId':
            'Global'}, 'virtualMachine': {'virtualMachineName': 'dma12', 'description': 'Created at
            [1:19:55 PM] by [PortalAdministrator]'}, 'network': {'networkId': 'vpc-09ae9e55dd75a5f6b',
            'subnetId': 'subnet-0b2131c783c96c1f9', 'securityGroupId': 'sg-0ad0a345b8059c199'},
            'ipAddress': {'applianceIp': {'applianceIpAddressId': None, 'newIpAddressType':
            'dynamic'}, 'backupServerIpAddresses': '89.185.226.14/32'}, 'guestOsCredentials':
            {'guestOsCredentialsUid': '18f0a96a-16e1-4b27-ace3-307fd65da25a', 'keyPairName':
            'VeeamDefaultKeyPair', 'timeZoneId': 'Europe/Prague'}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CreateNewPublicCloudAwsApplianceResponse200 | ErrorResponse]
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
    body: PublicCloudAwsNewApplianceInput,
    select: str | Unset = UNSET,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Any | CreateNewPublicCloudAwsApplianceResponse200 | ErrorResponse | None:
    """Create Veeam Backup for AWS Appliance

     Creates a new Veeam Backup for AWS appliance registered on a Veeam Cloud Connect site with the
    specified UID.

    Args:
        site_uid (UUID):
        select (str | Unset):
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):
        body (PublicCloudAwsNewApplianceInput):  Example: {'account': {'connectionUid':
            'c0300e84-e8c0-40df-97f1-cbdbdcecafa9', 'accountUid':
            '73f86291-d5ff-423c-88da-9b60be21964d', 'dataCenterId': 'eu-central-1', 'regionId':
            'Global'}, 'virtualMachine': {'virtualMachineName': 'dma12', 'description': 'Created at
            [1:19:55 PM] by [PortalAdministrator]'}, 'network': {'networkId': 'vpc-09ae9e55dd75a5f6b',
            'subnetId': 'subnet-0b2131c783c96c1f9', 'securityGroupId': 'sg-0ad0a345b8059c199'},
            'ipAddress': {'applianceIp': {'applianceIpAddressId': None, 'newIpAddressType':
            'dynamic'}, 'backupServerIpAddresses': '89.185.226.14/32'}, 'guestOsCredentials':
            {'guestOsCredentialsUid': '18f0a96a-16e1-4b27-ace3-307fd65da25a', 'keyPairName':
            'VeeamDefaultKeyPair', 'timeZoneId': 'Europe/Prague'}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CreateNewPublicCloudAwsApplianceResponse200 | ErrorResponse
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
