from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.get_organization_policy_settings_response_200 import GetOrganizationPolicySettingsResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    organization_uid: UUID,
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
        "url": "/organizations/{organization_uid}/configuration/policy".format(
            organization_uid=quote(str(organization_uid), safe=""),
        ),
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | ErrorResponse | GetOrganizationPolicySettingsResponse200:
    if response.status_code == 200:
        response_200 = GetOrganizationPolicySettingsResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 202:
        response_202 = cast(Any, None)
        return response_202

    response_default = ErrorResponse.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | ErrorResponse | GetOrganizationPolicySettingsResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    organization_uid: UUID,
    *,
    client: AuthenticatedClient,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Response[Any | ErrorResponse | GetOrganizationPolicySettingsResponse200]:
    """Get Organization Policy Settings

     Returns a resource representation of policy settings configured for an organization with the
    specified UID.

    Args:
        organization_uid (UUID):
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ErrorResponse | GetOrganizationPolicySettingsResponse200]
    """

    kwargs = _get_kwargs(
        organization_uid=organization_uid,
        x_request_id=x_request_id,
        x_client_version=x_client_version,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    organization_uid: UUID,
    *,
    client: AuthenticatedClient,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Any | ErrorResponse | GetOrganizationPolicySettingsResponse200 | None:
    """Get Organization Policy Settings

     Returns a resource representation of policy settings configured for an organization with the
    specified UID.

    Args:
        organization_uid (UUID):
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ErrorResponse | GetOrganizationPolicySettingsResponse200
    """

    return sync_detailed(
        organization_uid=organization_uid,
        client=client,
        x_request_id=x_request_id,
        x_client_version=x_client_version,
    ).parsed


async def asyncio_detailed(
    organization_uid: UUID,
    *,
    client: AuthenticatedClient,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Response[Any | ErrorResponse | GetOrganizationPolicySettingsResponse200]:
    """Get Organization Policy Settings

     Returns a resource representation of policy settings configured for an organization with the
    specified UID.

    Args:
        organization_uid (UUID):
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ErrorResponse | GetOrganizationPolicySettingsResponse200]
    """

    kwargs = _get_kwargs(
        organization_uid=organization_uid,
        x_request_id=x_request_id,
        x_client_version=x_client_version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    organization_uid: UUID,
    *,
    client: AuthenticatedClient,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Any | ErrorResponse | GetOrganizationPolicySettingsResponse200 | None:
    """Get Organization Policy Settings

     Returns a resource representation of policy settings configured for an organization with the
    specified UID.

    Args:
        organization_uid (UUID):
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ErrorResponse | GetOrganizationPolicySettingsResponse200
    """

    return (
        await asyncio_detailed(
            organization_uid=organization_uid,
            client=client,
            x_request_id=x_request_id,
            x_client_version=x_client_version,
        )
    ).parsed
