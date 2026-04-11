from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.get_backup_server_encryption_passwords_by_server_order_column import (
    GetBackupServerEncryptionPasswordsByServerOrderColumn,
)
from ...models.get_backup_server_encryption_passwords_by_server_response_200 import (
    GetBackupServerEncryptionPasswordsByServerResponse200,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    backup_server_uid: UUID,
    *,
    mapped_organization_uid_filter: None | Unset | UUID = UNSET,
    order_column: GetBackupServerEncryptionPasswordsByServerOrderColumn | Unset = UNSET,
    order_asc: bool | None | Unset = UNSET,
    limit: int | Unset = 100,
    offset: int | Unset = 0,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_request_id, Unset):
        headers["X-Request-id"] = x_request_id

    if not isinstance(x_client_version, Unset):
        headers["X-Client-Version"] = x_client_version

    params: dict[str, Any] = {}

    json_mapped_organization_uid_filter: None | str | Unset
    if isinstance(mapped_organization_uid_filter, Unset):
        json_mapped_organization_uid_filter = UNSET
    elif isinstance(mapped_organization_uid_filter, UUID):
        json_mapped_organization_uid_filter = str(mapped_organization_uid_filter)
    else:
        json_mapped_organization_uid_filter = mapped_organization_uid_filter
    params["mappedOrganizationUidFilter"] = json_mapped_organization_uid_filter

    json_order_column: str | Unset = UNSET
    if not isinstance(order_column, Unset):
        json_order_column = order_column.value

    params["orderColumn"] = json_order_column

    json_order_asc: bool | None | Unset
    if isinstance(order_asc, Unset):
        json_order_asc = UNSET
    else:
        json_order_asc = order_asc
    params["orderAsc"] = json_order_asc

    params["limit"] = limit

    params["offset"] = offset

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/infrastructure/backupServers/{backup_server_uid}/encryptionPasswords".format(
            backup_server_uid=quote(str(backup_server_uid), safe=""),
        ),
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | ErrorResponse | GetBackupServerEncryptionPasswordsByServerResponse200:
    if response.status_code == 200:
        response_200 = GetBackupServerEncryptionPasswordsByServerResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 202:
        response_202 = cast(Any, None)
        return response_202

    response_default = ErrorResponse.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | ErrorResponse | GetBackupServerEncryptionPasswordsByServerResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    backup_server_uid: UUID,
    *,
    client: AuthenticatedClient,
    mapped_organization_uid_filter: None | Unset | UUID = UNSET,
    order_column: GetBackupServerEncryptionPasswordsByServerOrderColumn | Unset = UNSET,
    order_asc: bool | None | Unset = UNSET,
    limit: int | Unset = 100,
    offset: int | Unset = 0,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Response[Any | ErrorResponse | GetBackupServerEncryptionPasswordsByServerResponse200]:
    """Get Veeam Backup & Replication Server Encryption Passwords

     Returns a collection resource representation of all encryption passwords created on a Veeam Backup &
    Replication server with the specified UID.

    Args:
        backup_server_uid (UUID):
        mapped_organization_uid_filter (None | Unset | UUID):
        order_column (GetBackupServerEncryptionPasswordsByServerOrderColumn | Unset):
        order_asc (bool | None | Unset):
        limit (int | Unset):  Default: 100.
        offset (int | Unset):  Default: 0.
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ErrorResponse | GetBackupServerEncryptionPasswordsByServerResponse200]
    """

    kwargs = _get_kwargs(
        backup_server_uid=backup_server_uid,
        mapped_organization_uid_filter=mapped_organization_uid_filter,
        order_column=order_column,
        order_asc=order_asc,
        limit=limit,
        offset=offset,
        x_request_id=x_request_id,
        x_client_version=x_client_version,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    backup_server_uid: UUID,
    *,
    client: AuthenticatedClient,
    mapped_organization_uid_filter: None | Unset | UUID = UNSET,
    order_column: GetBackupServerEncryptionPasswordsByServerOrderColumn | Unset = UNSET,
    order_asc: bool | None | Unset = UNSET,
    limit: int | Unset = 100,
    offset: int | Unset = 0,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Any | ErrorResponse | GetBackupServerEncryptionPasswordsByServerResponse200 | None:
    """Get Veeam Backup & Replication Server Encryption Passwords

     Returns a collection resource representation of all encryption passwords created on a Veeam Backup &
    Replication server with the specified UID.

    Args:
        backup_server_uid (UUID):
        mapped_organization_uid_filter (None | Unset | UUID):
        order_column (GetBackupServerEncryptionPasswordsByServerOrderColumn | Unset):
        order_asc (bool | None | Unset):
        limit (int | Unset):  Default: 100.
        offset (int | Unset):  Default: 0.
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ErrorResponse | GetBackupServerEncryptionPasswordsByServerResponse200
    """

    return sync_detailed(
        backup_server_uid=backup_server_uid,
        client=client,
        mapped_organization_uid_filter=mapped_organization_uid_filter,
        order_column=order_column,
        order_asc=order_asc,
        limit=limit,
        offset=offset,
        x_request_id=x_request_id,
        x_client_version=x_client_version,
    ).parsed


async def asyncio_detailed(
    backup_server_uid: UUID,
    *,
    client: AuthenticatedClient,
    mapped_organization_uid_filter: None | Unset | UUID = UNSET,
    order_column: GetBackupServerEncryptionPasswordsByServerOrderColumn | Unset = UNSET,
    order_asc: bool | None | Unset = UNSET,
    limit: int | Unset = 100,
    offset: int | Unset = 0,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Response[Any | ErrorResponse | GetBackupServerEncryptionPasswordsByServerResponse200]:
    """Get Veeam Backup & Replication Server Encryption Passwords

     Returns a collection resource representation of all encryption passwords created on a Veeam Backup &
    Replication server with the specified UID.

    Args:
        backup_server_uid (UUID):
        mapped_organization_uid_filter (None | Unset | UUID):
        order_column (GetBackupServerEncryptionPasswordsByServerOrderColumn | Unset):
        order_asc (bool | None | Unset):
        limit (int | Unset):  Default: 100.
        offset (int | Unset):  Default: 0.
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ErrorResponse | GetBackupServerEncryptionPasswordsByServerResponse200]
    """

    kwargs = _get_kwargs(
        backup_server_uid=backup_server_uid,
        mapped_organization_uid_filter=mapped_organization_uid_filter,
        order_column=order_column,
        order_asc=order_asc,
        limit=limit,
        offset=offset,
        x_request_id=x_request_id,
        x_client_version=x_client_version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    backup_server_uid: UUID,
    *,
    client: AuthenticatedClient,
    mapped_organization_uid_filter: None | Unset | UUID = UNSET,
    order_column: GetBackupServerEncryptionPasswordsByServerOrderColumn | Unset = UNSET,
    order_asc: bool | None | Unset = UNSET,
    limit: int | Unset = 100,
    offset: int | Unset = 0,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Any | ErrorResponse | GetBackupServerEncryptionPasswordsByServerResponse200 | None:
    """Get Veeam Backup & Replication Server Encryption Passwords

     Returns a collection resource representation of all encryption passwords created on a Veeam Backup &
    Replication server with the specified UID.

    Args:
        backup_server_uid (UUID):
        mapped_organization_uid_filter (None | Unset | UUID):
        order_column (GetBackupServerEncryptionPasswordsByServerOrderColumn | Unset):
        order_asc (bool | None | Unset):
        limit (int | Unset):  Default: 100.
        offset (int | Unset):  Default: 0.
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ErrorResponse | GetBackupServerEncryptionPasswordsByServerResponse200
    """

    return (
        await asyncio_detailed(
            backup_server_uid=backup_server_uid,
            client=client,
            mapped_organization_uid_filter=mapped_organization_uid_filter,
            order_column=order_column,
            order_asc=order_asc,
            limit=limit,
            offset=offset,
            x_request_id=x_request_id,
            x_client_version=x_client_version,
        )
    ).parsed
