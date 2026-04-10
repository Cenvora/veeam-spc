from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.create_azure_device_code_region import CreateAzureDeviceCodeRegion
from ...models.create_azure_device_code_response_200 import CreateAzureDeviceCodeResponse200
from ...models.error_response import ErrorResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    vb_365_server_uid: UUID,
    *,
    region: CreateAzureDeviceCodeRegion | Unset = CreateAzureDeviceCodeRegion.DEFAULT,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_request_id, Unset):
        headers["X-Request-id"] = x_request_id

    if not isinstance(x_client_version, Unset):
        headers["X-Client-Version"] = x_client_version

    params: dict[str, Any] = {}

    json_region: str | Unset = UNSET
    if not isinstance(region, Unset):
        json_region = region.value

    params["region"] = json_region

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/infrastructure/vb365Servers/{vb_365_server_uid}/organizations/deviceCode".format(
            vb_365_server_uid=quote(str(vb_365_server_uid), safe=""),
        ),
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | CreateAzureDeviceCodeResponse200 | ErrorResponse:
    if response.status_code == 200:
        response_200 = CreateAzureDeviceCodeResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 202:
        response_202 = cast(Any, None)
        return response_202

    response_default = ErrorResponse.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | CreateAzureDeviceCodeResponse200 | ErrorResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    vb_365_server_uid: UUID,
    *,
    client: AuthenticatedClient,
    region: CreateAzureDeviceCodeRegion | Unset = CreateAzureDeviceCodeRegion.DEFAULT,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Response[Any | CreateAzureDeviceCodeResponse200 | ErrorResponse]:
    """Create Device Code

     Generates a device code to log in to a Microsoft organization.
    > You can get a device code from Microsoft Azure to sign in to the [Microsoft authentication
    portal](https://login.microsoftonline.com/common/oauth2/deviceauth).

    Args:
        vb_365_server_uid (UUID):
        region (CreateAzureDeviceCodeRegion | Unset):  Default:
            CreateAzureDeviceCodeRegion.DEFAULT.
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CreateAzureDeviceCodeResponse200 | ErrorResponse]
    """

    kwargs = _get_kwargs(
        vb_365_server_uid=vb_365_server_uid,
        region=region,
        x_request_id=x_request_id,
        x_client_version=x_client_version,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    vb_365_server_uid: UUID,
    *,
    client: AuthenticatedClient,
    region: CreateAzureDeviceCodeRegion | Unset = CreateAzureDeviceCodeRegion.DEFAULT,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Any | CreateAzureDeviceCodeResponse200 | ErrorResponse | None:
    """Create Device Code

     Generates a device code to log in to a Microsoft organization.
    > You can get a device code from Microsoft Azure to sign in to the [Microsoft authentication
    portal](https://login.microsoftonline.com/common/oauth2/deviceauth).

    Args:
        vb_365_server_uid (UUID):
        region (CreateAzureDeviceCodeRegion | Unset):  Default:
            CreateAzureDeviceCodeRegion.DEFAULT.
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CreateAzureDeviceCodeResponse200 | ErrorResponse
    """

    return sync_detailed(
        vb_365_server_uid=vb_365_server_uid,
        client=client,
        region=region,
        x_request_id=x_request_id,
        x_client_version=x_client_version,
    ).parsed


async def asyncio_detailed(
    vb_365_server_uid: UUID,
    *,
    client: AuthenticatedClient,
    region: CreateAzureDeviceCodeRegion | Unset = CreateAzureDeviceCodeRegion.DEFAULT,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Response[Any | CreateAzureDeviceCodeResponse200 | ErrorResponse]:
    """Create Device Code

     Generates a device code to log in to a Microsoft organization.
    > You can get a device code from Microsoft Azure to sign in to the [Microsoft authentication
    portal](https://login.microsoftonline.com/common/oauth2/deviceauth).

    Args:
        vb_365_server_uid (UUID):
        region (CreateAzureDeviceCodeRegion | Unset):  Default:
            CreateAzureDeviceCodeRegion.DEFAULT.
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CreateAzureDeviceCodeResponse200 | ErrorResponse]
    """

    kwargs = _get_kwargs(
        vb_365_server_uid=vb_365_server_uid,
        region=region,
        x_request_id=x_request_id,
        x_client_version=x_client_version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    vb_365_server_uid: UUID,
    *,
    client: AuthenticatedClient,
    region: CreateAzureDeviceCodeRegion | Unset = CreateAzureDeviceCodeRegion.DEFAULT,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Any | CreateAzureDeviceCodeResponse200 | ErrorResponse | None:
    """Create Device Code

     Generates a device code to log in to a Microsoft organization.
    > You can get a device code from Microsoft Azure to sign in to the [Microsoft authentication
    portal](https://login.microsoftonline.com/common/oauth2/deviceauth).

    Args:
        vb_365_server_uid (UUID):
        region (CreateAzureDeviceCodeRegion | Unset):  Default:
            CreateAzureDeviceCodeRegion.DEFAULT.
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CreateAzureDeviceCodeResponse200 | ErrorResponse
    """

    return (
        await asyncio_detailed(
            vb_365_server_uid=vb_365_server_uid,
            client=client,
            region=region,
            x_request_id=x_request_id,
            x_client_version=x_client_version,
        )
    ).parsed
