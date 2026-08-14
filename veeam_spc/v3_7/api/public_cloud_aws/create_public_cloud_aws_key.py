from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.create_public_cloud_aws_key_response_200 import CreatePublicCloudAwsKeyResponse200
from ...models.error_response import ErrorResponse
from ...models.public_cloud_aws_key_pair_input import PublicCloudAwsKeyPairInput
from ...types import UNSET, Response, Unset


def _get_kwargs(
    site_uid: UUID,
    *,
    body: PublicCloudAwsKeyPairInput,
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
        "url": "/infrastructure/sites/{site_uid}/publicCloud/aws/keys".format(
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
) -> Any | CreatePublicCloudAwsKeyResponse200 | ErrorResponse:
    if response.status_code == 200:
        response_200 = CreatePublicCloudAwsKeyResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 202:
        response_202 = cast(Any, None)
        return response_202

    response_default = ErrorResponse.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | CreatePublicCloudAwsKeyResponse200 | ErrorResponse]:
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
    body: PublicCloudAwsKeyPairInput,
    select: str | Unset = UNSET,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Response[Any | CreatePublicCloudAwsKeyResponse200 | ErrorResponse]:
    """Create Amazon Encryption Key

     Creates an Amazon encryption key.

    Args:
        site_uid (UUID):
        select (str | Unset):
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):
        body (PublicCloudAwsKeyPairInput):  Example: {'connectionUid': 'f854a9fc-
            df97-40c9-8c32-c5fab9ad13d5', 'name': '[PortalAdministrator]_keyPair'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CreatePublicCloudAwsKeyResponse200 | ErrorResponse]
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
    body: PublicCloudAwsKeyPairInput,
    select: str | Unset = UNSET,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Any | CreatePublicCloudAwsKeyResponse200 | ErrorResponse | None:
    """Create Amazon Encryption Key

     Creates an Amazon encryption key.

    Args:
        site_uid (UUID):
        select (str | Unset):
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):
        body (PublicCloudAwsKeyPairInput):  Example: {'connectionUid': 'f854a9fc-
            df97-40c9-8c32-c5fab9ad13d5', 'name': '[PortalAdministrator]_keyPair'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CreatePublicCloudAwsKeyResponse200 | ErrorResponse
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
    body: PublicCloudAwsKeyPairInput,
    select: str | Unset = UNSET,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Response[Any | CreatePublicCloudAwsKeyResponse200 | ErrorResponse]:
    """Create Amazon Encryption Key

     Creates an Amazon encryption key.

    Args:
        site_uid (UUID):
        select (str | Unset):
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):
        body (PublicCloudAwsKeyPairInput):  Example: {'connectionUid': 'f854a9fc-
            df97-40c9-8c32-c5fab9ad13d5', 'name': '[PortalAdministrator]_keyPair'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CreatePublicCloudAwsKeyResponse200 | ErrorResponse]
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
    body: PublicCloudAwsKeyPairInput,
    select: str | Unset = UNSET,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Any | CreatePublicCloudAwsKeyResponse200 | ErrorResponse | None:
    """Create Amazon Encryption Key

     Creates an Amazon encryption key.

    Args:
        site_uid (UUID):
        select (str | Unset):
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):
        body (PublicCloudAwsKeyPairInput):  Example: {'connectionUid': 'f854a9fc-
            df97-40c9-8c32-c5fab9ad13d5', 'name': '[PortalAdministrator]_keyPair'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CreatePublicCloudAwsKeyResponse200 | ErrorResponse
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
