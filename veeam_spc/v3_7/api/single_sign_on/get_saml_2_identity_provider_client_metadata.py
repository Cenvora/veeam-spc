from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.get_saml_2_identity_provider_client_metadata_response_200 import (
    GetSaml2IdentityProviderClientMetadataResponse200,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    organization_uid: UUID,
    identity_provider_name: str,
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
        "url": "/organizations/{organization_uid}/identityProviders/saml2/{identity_provider_name}/metadata".format(
            organization_uid=quote(str(organization_uid), safe=""),
            identity_provider_name=quote(str(identity_provider_name), safe=""),
        ),
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | ErrorResponse | GetSaml2IdentityProviderClientMetadataResponse200:
    if response.status_code == 200:
        response_200 = GetSaml2IdentityProviderClientMetadataResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 202:
        response_202 = cast(Any, None)
        return response_202

    response_default = ErrorResponse.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | ErrorResponse | GetSaml2IdentityProviderClientMetadataResponse200]:
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
    client: AuthenticatedClient | Client,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Response[Any | ErrorResponse | GetSaml2IdentityProviderClientMetadataResponse200]:
    """Get Metadata for Organization Identity Provider.

     Returns content of the metadata XML file that is sent to an organization identity provider.
    > Error response is returned in the JSON format.

    Args:
        organization_uid (UUID):
        identity_provider_name (str):
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ErrorResponse | GetSaml2IdentityProviderClientMetadataResponse200]
    """

    kwargs = _get_kwargs(
        organization_uid=organization_uid,
        identity_provider_name=identity_provider_name,
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
    client: AuthenticatedClient | Client,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Any | ErrorResponse | GetSaml2IdentityProviderClientMetadataResponse200 | None:
    """Get Metadata for Organization Identity Provider.

     Returns content of the metadata XML file that is sent to an organization identity provider.
    > Error response is returned in the JSON format.

    Args:
        organization_uid (UUID):
        identity_provider_name (str):
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ErrorResponse | GetSaml2IdentityProviderClientMetadataResponse200
    """

    return sync_detailed(
        organization_uid=organization_uid,
        identity_provider_name=identity_provider_name,
        client=client,
        x_request_id=x_request_id,
        x_client_version=x_client_version,
    ).parsed


async def asyncio_detailed(
    organization_uid: UUID,
    identity_provider_name: str,
    *,
    client: AuthenticatedClient | Client,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Response[Any | ErrorResponse | GetSaml2IdentityProviderClientMetadataResponse200]:
    """Get Metadata for Organization Identity Provider.

     Returns content of the metadata XML file that is sent to an organization identity provider.
    > Error response is returned in the JSON format.

    Args:
        organization_uid (UUID):
        identity_provider_name (str):
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ErrorResponse | GetSaml2IdentityProviderClientMetadataResponse200]
    """

    kwargs = _get_kwargs(
        organization_uid=organization_uid,
        identity_provider_name=identity_provider_name,
        x_request_id=x_request_id,
        x_client_version=x_client_version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    organization_uid: UUID,
    identity_provider_name: str,
    *,
    client: AuthenticatedClient | Client,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Any | ErrorResponse | GetSaml2IdentityProviderClientMetadataResponse200 | None:
    """Get Metadata for Organization Identity Provider.

     Returns content of the metadata XML file that is sent to an organization identity provider.
    > Error response is returned in the JSON format.

    Args:
        organization_uid (UUID):
        identity_provider_name (str):
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ErrorResponse | GetSaml2IdentityProviderClientMetadataResponse200
    """

    return (
        await asyncio_detailed(
            organization_uid=organization_uid,
            identity_provider_name=identity_provider_name,
            client=client,
            x_request_id=x_request_id,
            x_client_version=x_client_version,
        )
    ).parsed
