from http import HTTPStatus
from typing import Any, Optional, Union, cast
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.empty_response import EmptyResponse
from ...models.error_response import ErrorResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    site_uid: UUID,
    appliance_uid: UUID,
    *,
    with_cloud_resources: bool,
    x_request_id: Union[Unset, UUID] = UNSET,
    x_client_version: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_request_id, Unset):
        headers["X-Request-id"] = x_request_id

    if not isinstance(x_client_version, Unset):
        headers["X-Client-Version"] = x_client_version

    params: dict[str, Any] = {}

    params["withCloudResources"] = with_cloud_resources

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": f"/infrastructure/sites/{site_uid}/publicCloud/appliances/{appliance_uid}",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Union[Any, EmptyResponse, ErrorResponse]:
    if response.status_code == 200:
        response_200 = EmptyResponse.from_dict(response.json())

        return response_200

    if response.status_code == 202:
        response_202 = cast(Any, None)
        return response_202

    response_default = ErrorResponse.from_dict(response.json())

    return response_default


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, EmptyResponse, ErrorResponse]]:
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
    client: Union[AuthenticatedClient, Client],
    with_cloud_resources: bool,
    x_request_id: Union[Unset, UUID] = UNSET,
    x_client_version: Union[Unset, str] = UNSET,
) -> Response[Union[Any, EmptyResponse, ErrorResponse]]:
    """Delete Veeam Backup for Public Clouds Appliance Registered on Veeam Cloud Connect Site

     Removes a Veeam Backup for Public Clouds appliance with the specified UID registered on a Veeam
    Cloud Connect site.

    Args:
        site_uid (UUID):
        appliance_uid (UUID):
        with_cloud_resources (bool):
        x_request_id (Union[Unset, UUID]):
        x_client_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, EmptyResponse, ErrorResponse]]
    """

    kwargs = _get_kwargs(
        site_uid=site_uid,
        appliance_uid=appliance_uid,
        with_cloud_resources=with_cloud_resources,
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
    client: Union[AuthenticatedClient, Client],
    with_cloud_resources: bool,
    x_request_id: Union[Unset, UUID] = UNSET,
    x_client_version: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, EmptyResponse, ErrorResponse]]:
    """Delete Veeam Backup for Public Clouds Appliance Registered on Veeam Cloud Connect Site

     Removes a Veeam Backup for Public Clouds appliance with the specified UID registered on a Veeam
    Cloud Connect site.

    Args:
        site_uid (UUID):
        appliance_uid (UUID):
        with_cloud_resources (bool):
        x_request_id (Union[Unset, UUID]):
        x_client_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, EmptyResponse, ErrorResponse]
    """

    return sync_detailed(
        site_uid=site_uid,
        appliance_uid=appliance_uid,
        client=client,
        with_cloud_resources=with_cloud_resources,
        x_request_id=x_request_id,
        x_client_version=x_client_version,
    ).parsed


async def asyncio_detailed(
    site_uid: UUID,
    appliance_uid: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
    with_cloud_resources: bool,
    x_request_id: Union[Unset, UUID] = UNSET,
    x_client_version: Union[Unset, str] = UNSET,
) -> Response[Union[Any, EmptyResponse, ErrorResponse]]:
    """Delete Veeam Backup for Public Clouds Appliance Registered on Veeam Cloud Connect Site

     Removes a Veeam Backup for Public Clouds appliance with the specified UID registered on a Veeam
    Cloud Connect site.

    Args:
        site_uid (UUID):
        appliance_uid (UUID):
        with_cloud_resources (bool):
        x_request_id (Union[Unset, UUID]):
        x_client_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, EmptyResponse, ErrorResponse]]
    """

    kwargs = _get_kwargs(
        site_uid=site_uid,
        appliance_uid=appliance_uid,
        with_cloud_resources=with_cloud_resources,
        x_request_id=x_request_id,
        x_client_version=x_client_version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    site_uid: UUID,
    appliance_uid: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
    with_cloud_resources: bool,
    x_request_id: Union[Unset, UUID] = UNSET,
    x_client_version: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, EmptyResponse, ErrorResponse]]:
    """Delete Veeam Backup for Public Clouds Appliance Registered on Veeam Cloud Connect Site

     Removes a Veeam Backup for Public Clouds appliance with the specified UID registered on a Veeam
    Cloud Connect site.

    Args:
        site_uid (UUID):
        appliance_uid (UUID):
        with_cloud_resources (bool):
        x_request_id (Union[Unset, UUID]):
        x_client_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, EmptyResponse, ErrorResponse]
    """

    return (
        await asyncio_detailed(
            site_uid=site_uid,
            appliance_uid=appliance_uid,
            client=client,
            with_cloud_resources=with_cloud_resources,
            x_request_id=x_request_id,
            x_client_version=x_client_version,
        )
    ).parsed
