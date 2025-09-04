from http import HTTPStatus
from typing import Any, Optional, Union, cast
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.add_existing_public_cloud_azure_account_response_200 import AddExistingPublicCloudAzureAccountResponse200
from ...models.error_response import ErrorResponse
from ...models.public_cloud_existing_azure_account_input import PublicCloudExistingAzureAccountInput
from ...types import UNSET, Response, Unset


def _get_kwargs(
    site_uid: UUID,
    *,
    body: PublicCloudExistingAzureAccountInput,
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
        "url": f"/infrastructure/sites/{site_uid}/publicCloud/azure/accounts/existing",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Union[AddExistingPublicCloudAzureAccountResponse200, Any, ErrorResponse]:
    if response.status_code == 200:
        response_200 = AddExistingPublicCloudAzureAccountResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 202:
        response_202 = cast(Any, None)
        return response_202

    response_default = ErrorResponse.from_dict(response.json())

    return response_default


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[AddExistingPublicCloudAzureAccountResponse200, Any, ErrorResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    site_uid: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
    body: PublicCloudExistingAzureAccountInput,
    x_request_id: Union[Unset, UUID] = UNSET,
    x_client_version: Union[Unset, str] = UNSET,
) -> Response[Union[AddExistingPublicCloudAzureAccountResponse200, Any, ErrorResponse]]:
    """Add Existing Microsoft Azure Account

     Registers an existing Microsoft Azure on a Veeam Cloud Connect site with the specified UID.

    Args:
        site_uid (UUID):
        x_request_id (Union[Unset, UUID]):
        x_client_version (Union[Unset, str]):
        body (PublicCloudExistingAzureAccountInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[AddExistingPublicCloudAzureAccountResponse200, Any, ErrorResponse]]
    """

    kwargs = _get_kwargs(
        site_uid=site_uid,
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
    *,
    client: Union[AuthenticatedClient, Client],
    body: PublicCloudExistingAzureAccountInput,
    x_request_id: Union[Unset, UUID] = UNSET,
    x_client_version: Union[Unset, str] = UNSET,
) -> Optional[Union[AddExistingPublicCloudAzureAccountResponse200, Any, ErrorResponse]]:
    """Add Existing Microsoft Azure Account

     Registers an existing Microsoft Azure on a Veeam Cloud Connect site with the specified UID.

    Args:
        site_uid (UUID):
        x_request_id (Union[Unset, UUID]):
        x_client_version (Union[Unset, str]):
        body (PublicCloudExistingAzureAccountInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[AddExistingPublicCloudAzureAccountResponse200, Any, ErrorResponse]
    """

    return sync_detailed(
        site_uid=site_uid,
        client=client,
        body=body,
        x_request_id=x_request_id,
        x_client_version=x_client_version,
    ).parsed


async def asyncio_detailed(
    site_uid: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
    body: PublicCloudExistingAzureAccountInput,
    x_request_id: Union[Unset, UUID] = UNSET,
    x_client_version: Union[Unset, str] = UNSET,
) -> Response[Union[AddExistingPublicCloudAzureAccountResponse200, Any, ErrorResponse]]:
    """Add Existing Microsoft Azure Account

     Registers an existing Microsoft Azure on a Veeam Cloud Connect site with the specified UID.

    Args:
        site_uid (UUID):
        x_request_id (Union[Unset, UUID]):
        x_client_version (Union[Unset, str]):
        body (PublicCloudExistingAzureAccountInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[AddExistingPublicCloudAzureAccountResponse200, Any, ErrorResponse]]
    """

    kwargs = _get_kwargs(
        site_uid=site_uid,
        body=body,
        x_request_id=x_request_id,
        x_client_version=x_client_version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    site_uid: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
    body: PublicCloudExistingAzureAccountInput,
    x_request_id: Union[Unset, UUID] = UNSET,
    x_client_version: Union[Unset, str] = UNSET,
) -> Optional[Union[AddExistingPublicCloudAzureAccountResponse200, Any, ErrorResponse]]:
    """Add Existing Microsoft Azure Account

     Registers an existing Microsoft Azure on a Veeam Cloud Connect site with the specified UID.

    Args:
        site_uid (UUID):
        x_request_id (Union[Unset, UUID]):
        x_client_version (Union[Unset, str]):
        body (PublicCloudExistingAzureAccountInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[AddExistingPublicCloudAzureAccountResponse200, Any, ErrorResponse]
    """

    return (
        await asyncio_detailed(
            site_uid=site_uid,
            client=client,
            body=body,
            x_request_id=x_request_id,
            x_client_version=x_client_version,
        )
    ).parsed
