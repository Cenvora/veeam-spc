from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.get_public_cloud_appliance_response_200 import GetPublicCloudApplianceResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    site_uid: UUID,
    appliance_uid: UUID,
    *,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_request_id, Unset):
        headers["X-Request-id"] = x_request_id

    if not isinstance(x_client_version, Unset):
        headers["X-Client-Version"] = x_client_version

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/infrastructure/sites/{site_uid}/publicCloud/appliances/{appliance_uid}".format(
            site_uid=quote(str(site_uid), safe=""),
            appliance_uid=quote(str(appliance_uid), safe=""),
        ),
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | ErrorResponse | GetPublicCloudApplianceResponse200:
    if response.status_code == 200:
        response_200 = GetPublicCloudApplianceResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 202:
        response_202 = cast(Any, None)
        return response_202

    response_default = ErrorResponse.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | ErrorResponse | GetPublicCloudApplianceResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    site_uid: UUID,
    appliance_uid: UUID,
    *,
    client: AuthenticatedClient,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Response[Any | ErrorResponse | GetPublicCloudApplianceResponse200]:
    """Get Veeam Backup for Public Clouds Appliance Registered on Veeam Cloud Connect Site

     Returns a resource representation of a Veeam Backup for Public Clouds appliance with the specified
    UID registered on a Veeam Cloud Connect site.

    Args:
        site_uid (UUID):
        appliance_uid (UUID):
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ErrorResponse | GetPublicCloudApplianceResponse200]
    """

    kwargs = _get_kwargs(
        site_uid=site_uid,
        appliance_uid=appliance_uid,
        x_request_id=x_request_id,
        x_client_version=x_client_version,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    site_uid: UUID,
    appliance_uid: UUID,
    *,
    client: AuthenticatedClient,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Any | ErrorResponse | GetPublicCloudApplianceResponse200 | None:
    """Get Veeam Backup for Public Clouds Appliance Registered on Veeam Cloud Connect Site

     Returns a resource representation of a Veeam Backup for Public Clouds appliance with the specified
    UID registered on a Veeam Cloud Connect site.

    Args:
        site_uid (UUID):
        appliance_uid (UUID):
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ErrorResponse | GetPublicCloudApplianceResponse200
    """

    return sync_detailed(
        site_uid=site_uid,
        appliance_uid=appliance_uid,
        client=client,
        x_request_id=x_request_id,
        x_client_version=x_client_version,
    ).parsed


async def asyncio_detailed(
    site_uid: UUID,
    appliance_uid: UUID,
    *,
    client: AuthenticatedClient,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Response[Any | ErrorResponse | GetPublicCloudApplianceResponse200]:
    """Get Veeam Backup for Public Clouds Appliance Registered on Veeam Cloud Connect Site

     Returns a resource representation of a Veeam Backup for Public Clouds appliance with the specified
    UID registered on a Veeam Cloud Connect site.

    Args:
        site_uid (UUID):
        appliance_uid (UUID):
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ErrorResponse | GetPublicCloudApplianceResponse200]
    """

    kwargs = _get_kwargs(
        site_uid=site_uid,
        appliance_uid=appliance_uid,
        x_request_id=x_request_id,
        x_client_version=x_client_version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    site_uid: UUID,
    appliance_uid: UUID,
    *,
    client: AuthenticatedClient,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Any | ErrorResponse | GetPublicCloudApplianceResponse200 | None:
    """Get Veeam Backup for Public Clouds Appliance Registered on Veeam Cloud Connect Site

     Returns a resource representation of a Veeam Backup for Public Clouds appliance with the specified
    UID registered on a Veeam Cloud Connect site.

    Args:
        site_uid (UUID):
        appliance_uid (UUID):
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ErrorResponse | GetPublicCloudApplianceResponse200
    """

    return (
        await asyncio_detailed(
            site_uid=site_uid,
            appliance_uid=appliance_uid,
            client=client,
            x_request_id=x_request_id,
            x_client_version=x_client_version,
        )
    ).parsed
