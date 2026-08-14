from http import HTTPStatus
from typing import Any, cast
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.create_user_response_200 import CreateUserResponse200
from ...models.error_response import ErrorResponse
from ...models.user_input import UserInput
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: UserInput,
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
        "url": "/users",
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | CreateUserResponse200 | ErrorResponse:
    if response.status_code == 200:
        response_200 = CreateUserResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 202:
        response_202 = cast(Any, None)
        return response_202

    response_default = ErrorResponse.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | CreateUserResponse200 | ErrorResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: UserInput,
    select: str | Unset = UNSET,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Response[Any | CreateUserResponse200 | ErrorResponse]:
    """Create User

     Creates a new user with specific properties.

    Args:
        select (str | Unset):
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):
        body (UserInput):  Example: {'organizationUid': 'bb591af2-7c6b-4bca-856b-603ae6088a1a',
            'role': 'CompanySubtenant', 'mfaPolicyStatus': 'Enabled', 'profile': {'firstName': 'John',
            'lastName': 'Brown', 'title': 'Mr', 'email': 'j.brown@exon.com', 'address': None, 'phone':
            '301 329 9338'}, 'credentials': {'userName': 'subtenant', 'password': 'Password1'},
            'backupResource': {'siteUid': '4d32d061-993c-4b69-b9a9-0ea2c9aa891e',
            'tenantBackupResourceUid': 'bbd634fd-e881-4e03-8aaf-bec7beccd5fb', 'description': None,
            'vcdUserId': None, 'resourceFriendlyName': 'SubtenantRepo', 'storageQuota': 1073741824,
            'isStorageQuotaUnlimited': False}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CreateUserResponse200 | ErrorResponse]
    """

    kwargs = _get_kwargs(
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
    *,
    client: AuthenticatedClient,
    body: UserInput,
    select: str | Unset = UNSET,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Any | CreateUserResponse200 | ErrorResponse | None:
    """Create User

     Creates a new user with specific properties.

    Args:
        select (str | Unset):
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):
        body (UserInput):  Example: {'organizationUid': 'bb591af2-7c6b-4bca-856b-603ae6088a1a',
            'role': 'CompanySubtenant', 'mfaPolicyStatus': 'Enabled', 'profile': {'firstName': 'John',
            'lastName': 'Brown', 'title': 'Mr', 'email': 'j.brown@exon.com', 'address': None, 'phone':
            '301 329 9338'}, 'credentials': {'userName': 'subtenant', 'password': 'Password1'},
            'backupResource': {'siteUid': '4d32d061-993c-4b69-b9a9-0ea2c9aa891e',
            'tenantBackupResourceUid': 'bbd634fd-e881-4e03-8aaf-bec7beccd5fb', 'description': None,
            'vcdUserId': None, 'resourceFriendlyName': 'SubtenantRepo', 'storageQuota': 1073741824,
            'isStorageQuotaUnlimited': False}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CreateUserResponse200 | ErrorResponse
    """

    return sync_detailed(
        client=client,
        body=body,
        select=select,
        x_request_id=x_request_id,
        x_client_version=x_client_version,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: UserInput,
    select: str | Unset = UNSET,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Response[Any | CreateUserResponse200 | ErrorResponse]:
    """Create User

     Creates a new user with specific properties.

    Args:
        select (str | Unset):
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):
        body (UserInput):  Example: {'organizationUid': 'bb591af2-7c6b-4bca-856b-603ae6088a1a',
            'role': 'CompanySubtenant', 'mfaPolicyStatus': 'Enabled', 'profile': {'firstName': 'John',
            'lastName': 'Brown', 'title': 'Mr', 'email': 'j.brown@exon.com', 'address': None, 'phone':
            '301 329 9338'}, 'credentials': {'userName': 'subtenant', 'password': 'Password1'},
            'backupResource': {'siteUid': '4d32d061-993c-4b69-b9a9-0ea2c9aa891e',
            'tenantBackupResourceUid': 'bbd634fd-e881-4e03-8aaf-bec7beccd5fb', 'description': None,
            'vcdUserId': None, 'resourceFriendlyName': 'SubtenantRepo', 'storageQuota': 1073741824,
            'isStorageQuotaUnlimited': False}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CreateUserResponse200 | ErrorResponse]
    """

    kwargs = _get_kwargs(
        body=body,
        select=select,
        x_request_id=x_request_id,
        x_client_version=x_client_version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: UserInput,
    select: str | Unset = UNSET,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Any | CreateUserResponse200 | ErrorResponse | None:
    """Create User

     Creates a new user with specific properties.

    Args:
        select (str | Unset):
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):
        body (UserInput):  Example: {'organizationUid': 'bb591af2-7c6b-4bca-856b-603ae6088a1a',
            'role': 'CompanySubtenant', 'mfaPolicyStatus': 'Enabled', 'profile': {'firstName': 'John',
            'lastName': 'Brown', 'title': 'Mr', 'email': 'j.brown@exon.com', 'address': None, 'phone':
            '301 329 9338'}, 'credentials': {'userName': 'subtenant', 'password': 'Password1'},
            'backupResource': {'siteUid': '4d32d061-993c-4b69-b9a9-0ea2c9aa891e',
            'tenantBackupResourceUid': 'bbd634fd-e881-4e03-8aaf-bec7beccd5fb', 'description': None,
            'vcdUserId': None, 'resourceFriendlyName': 'SubtenantRepo', 'storageQuota': 1073741824,
            'isStorageQuotaUnlimited': False}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CreateUserResponse200 | ErrorResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            select=select,
            x_request_id=x_request_id,
            x_client_version=x_client_version,
        )
    ).parsed
