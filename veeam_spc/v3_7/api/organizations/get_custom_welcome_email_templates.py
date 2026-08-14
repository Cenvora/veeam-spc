from http import HTTPStatus
from typing import Any, cast
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.get_custom_welcome_email_templates_organization_scope import (
    GetCustomWelcomeEmailTemplatesOrganizationScope,
)
from ...models.get_custom_welcome_email_templates_organization_type import (
    GetCustomWelcomeEmailTemplatesOrganizationType,
)
from ...models.get_custom_welcome_email_templates_response_200 import GetCustomWelcomeEmailTemplatesResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    organization_uid: UUID | Unset = UNSET,
    organization_type: GetCustomWelcomeEmailTemplatesOrganizationType | Unset = UNSET,
    organization_scope: GetCustomWelcomeEmailTemplatesOrganizationScope | Unset = UNSET,
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

    json_organization_uid: str | Unset = UNSET
    if not isinstance(organization_uid, Unset):
        json_organization_uid = str(organization_uid)
    params["organizationUid"] = json_organization_uid

    json_organization_type: str | Unset = UNSET
    if not isinstance(organization_type, Unset):
        json_organization_type = organization_type.value

    params["organizationType"] = json_organization_type

    json_organization_scope: str | Unset = UNSET
    if not isinstance(organization_scope, Unset):
        json_organization_scope = organization_scope.value

    params["organizationScope"] = json_organization_scope

    params["select"] = select

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/organizations/configuration/notification/welcomeEmails",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | ErrorResponse | GetCustomWelcomeEmailTemplatesResponse200:
    if response.status_code == 200:
        response_200 = GetCustomWelcomeEmailTemplatesResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 202:
        response_202 = cast(Any, None)
        return response_202

    response_default = ErrorResponse.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | ErrorResponse | GetCustomWelcomeEmailTemplatesResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    organization_uid: UUID | Unset = UNSET,
    organization_type: GetCustomWelcomeEmailTemplatesOrganizationType | Unset = UNSET,
    organization_scope: GetCustomWelcomeEmailTemplatesOrganizationScope | Unset = UNSET,
    select: str | Unset = UNSET,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Response[Any | ErrorResponse | GetCustomWelcomeEmailTemplatesResponse200]:
    """Get All Custom Settings of Email Notification

     Returns a collection resource representation of all custom settings configured for email
    notifications.

    Args:
        organization_uid (UUID | Unset):
        organization_type (GetCustomWelcomeEmailTemplatesOrganizationType | Unset):
        organization_scope (GetCustomWelcomeEmailTemplatesOrganizationScope | Unset):
        select (str | Unset):
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ErrorResponse | GetCustomWelcomeEmailTemplatesResponse200]
    """

    kwargs = _get_kwargs(
        organization_uid=organization_uid,
        organization_type=organization_type,
        organization_scope=organization_scope,
        select=select,
        x_request_id=x_request_id,
        x_client_version=x_client_version,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    organization_uid: UUID | Unset = UNSET,
    organization_type: GetCustomWelcomeEmailTemplatesOrganizationType | Unset = UNSET,
    organization_scope: GetCustomWelcomeEmailTemplatesOrganizationScope | Unset = UNSET,
    select: str | Unset = UNSET,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Any | ErrorResponse | GetCustomWelcomeEmailTemplatesResponse200 | None:
    """Get All Custom Settings of Email Notification

     Returns a collection resource representation of all custom settings configured for email
    notifications.

    Args:
        organization_uid (UUID | Unset):
        organization_type (GetCustomWelcomeEmailTemplatesOrganizationType | Unset):
        organization_scope (GetCustomWelcomeEmailTemplatesOrganizationScope | Unset):
        select (str | Unset):
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ErrorResponse | GetCustomWelcomeEmailTemplatesResponse200
    """

    return sync_detailed(
        client=client,
        organization_uid=organization_uid,
        organization_type=organization_type,
        organization_scope=organization_scope,
        select=select,
        x_request_id=x_request_id,
        x_client_version=x_client_version,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    organization_uid: UUID | Unset = UNSET,
    organization_type: GetCustomWelcomeEmailTemplatesOrganizationType | Unset = UNSET,
    organization_scope: GetCustomWelcomeEmailTemplatesOrganizationScope | Unset = UNSET,
    select: str | Unset = UNSET,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Response[Any | ErrorResponse | GetCustomWelcomeEmailTemplatesResponse200]:
    """Get All Custom Settings of Email Notification

     Returns a collection resource representation of all custom settings configured for email
    notifications.

    Args:
        organization_uid (UUID | Unset):
        organization_type (GetCustomWelcomeEmailTemplatesOrganizationType | Unset):
        organization_scope (GetCustomWelcomeEmailTemplatesOrganizationScope | Unset):
        select (str | Unset):
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ErrorResponse | GetCustomWelcomeEmailTemplatesResponse200]
    """

    kwargs = _get_kwargs(
        organization_uid=organization_uid,
        organization_type=organization_type,
        organization_scope=organization_scope,
        select=select,
        x_request_id=x_request_id,
        x_client_version=x_client_version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    organization_uid: UUID | Unset = UNSET,
    organization_type: GetCustomWelcomeEmailTemplatesOrganizationType | Unset = UNSET,
    organization_scope: GetCustomWelcomeEmailTemplatesOrganizationScope | Unset = UNSET,
    select: str | Unset = UNSET,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Any | ErrorResponse | GetCustomWelcomeEmailTemplatesResponse200 | None:
    """Get All Custom Settings of Email Notification

     Returns a collection resource representation of all custom settings configured for email
    notifications.

    Args:
        organization_uid (UUID | Unset):
        organization_type (GetCustomWelcomeEmailTemplatesOrganizationType | Unset):
        organization_scope (GetCustomWelcomeEmailTemplatesOrganizationScope | Unset):
        select (str | Unset):
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ErrorResponse | GetCustomWelcomeEmailTemplatesResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            organization_uid=organization_uid,
            organization_type=organization_type,
            organization_scope=organization_scope,
            select=select,
            x_request_id=x_request_id,
            x_client_version=x_client_version,
        )
    ).parsed
