from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.grant_public_cloud_appliance_platform_credentials_for_migration_response_200 import (
    GrantPublicCloudAppliancePlatformCredentialsForMigrationResponse200,
)
from ...models.public_cloud_grant_permissions_for_migration_input import PublicCloudGrantPermissionsForMigrationInput
from ...types import UNSET, Response, Unset


def _get_kwargs(
    site_uid: UUID,
    account_uid: UUID,
    *,
    body: PublicCloudGrantPermissionsForMigrationInput,
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
        "url": "/infrastructure/sites/{site_uid}/publicCloud/aws/accounts/{account_uid}/grantPermissionsForMigration".format(
            site_uid=quote(str(site_uid), safe=""),
            account_uid=quote(str(account_uid), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | ErrorResponse | GrantPublicCloudAppliancePlatformCredentialsForMigrationResponse200:
    if response.status_code == 200:
        response_200 = GrantPublicCloudAppliancePlatformCredentialsForMigrationResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 202:
        response_202 = cast(Any, None)
        return response_202

    response_default = ErrorResponse.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | ErrorResponse | GrantPublicCloudAppliancePlatformCredentialsForMigrationResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    site_uid: UUID,
    account_uid: UUID,
    *,
    client: AuthenticatedClient,
    body: PublicCloudGrantPermissionsForMigrationInput,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Response[Any | ErrorResponse | GrantPublicCloudAppliancePlatformCredentialsForMigrationResponse200]:
    """Grant Permissions to Update Veeam Backup for AWS Appliance

     Grants permissions necessary to update an Veeam Backup for AWS appliance to an account with the
    specified UID.

    Args:
        site_uid (UUID):
        account_uid (UUID):
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):
        body (PublicCloudGrantPermissionsForMigrationInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ErrorResponse | GrantPublicCloudAppliancePlatformCredentialsForMigrationResponse200]
    """

    kwargs = _get_kwargs(
        site_uid=site_uid,
        account_uid=account_uid,
        body=body,
        x_request_id=x_request_id,
        x_client_version=x_client_version,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    site_uid: UUID,
    account_uid: UUID,
    *,
    client: AuthenticatedClient,
    body: PublicCloudGrantPermissionsForMigrationInput,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Any | ErrorResponse | GrantPublicCloudAppliancePlatformCredentialsForMigrationResponse200 | None:
    """Grant Permissions to Update Veeam Backup for AWS Appliance

     Grants permissions necessary to update an Veeam Backup for AWS appliance to an account with the
    specified UID.

    Args:
        site_uid (UUID):
        account_uid (UUID):
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):
        body (PublicCloudGrantPermissionsForMigrationInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ErrorResponse | GrantPublicCloudAppliancePlatformCredentialsForMigrationResponse200
    """

    return sync_detailed(
        site_uid=site_uid,
        account_uid=account_uid,
        client=client,
        body=body,
        x_request_id=x_request_id,
        x_client_version=x_client_version,
    ).parsed


async def asyncio_detailed(
    site_uid: UUID,
    account_uid: UUID,
    *,
    client: AuthenticatedClient,
    body: PublicCloudGrantPermissionsForMigrationInput,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Response[Any | ErrorResponse | GrantPublicCloudAppliancePlatformCredentialsForMigrationResponse200]:
    """Grant Permissions to Update Veeam Backup for AWS Appliance

     Grants permissions necessary to update an Veeam Backup for AWS appliance to an account with the
    specified UID.

    Args:
        site_uid (UUID):
        account_uid (UUID):
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):
        body (PublicCloudGrantPermissionsForMigrationInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ErrorResponse | GrantPublicCloudAppliancePlatformCredentialsForMigrationResponse200]
    """

    kwargs = _get_kwargs(
        site_uid=site_uid,
        account_uid=account_uid,
        body=body,
        x_request_id=x_request_id,
        x_client_version=x_client_version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    site_uid: UUID,
    account_uid: UUID,
    *,
    client: AuthenticatedClient,
    body: PublicCloudGrantPermissionsForMigrationInput,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Any | ErrorResponse | GrantPublicCloudAppliancePlatformCredentialsForMigrationResponse200 | None:
    """Grant Permissions to Update Veeam Backup for AWS Appliance

     Grants permissions necessary to update an Veeam Backup for AWS appliance to an account with the
    specified UID.

    Args:
        site_uid (UUID):
        account_uid (UUID):
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):
        body (PublicCloudGrantPermissionsForMigrationInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ErrorResponse | GrantPublicCloudAppliancePlatformCredentialsForMigrationResponse200
    """

    return (
        await asyncio_detailed(
            site_uid=site_uid,
            account_uid=account_uid,
            client=client,
            body=body,
            x_request_id=x_request_id,
            x_client_version=x_client_version,
        )
    ).parsed
