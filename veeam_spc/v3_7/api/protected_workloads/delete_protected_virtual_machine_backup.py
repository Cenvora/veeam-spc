from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.delete_protected_virtual_machine_backup_response_200 import (
    DeleteProtectedVirtualMachineBackupResponse200,
)
from ...models.error_response import ErrorResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    backup_uid: UUID,
    *,
    backup_object_uid: UUID,
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

    json_backup_object_uid = str(backup_object_uid)
    params["backupObjectUid"] = json_backup_object_uid

    params["select"] = select

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/protectedWorkloads/virtualMachines/backups/{backup_uid}".format(
            backup_uid=quote(str(backup_uid), safe=""),
        ),
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | DeleteProtectedVirtualMachineBackupResponse200 | ErrorResponse:
    if response.status_code == 200:
        response_200 = DeleteProtectedVirtualMachineBackupResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 202:
        response_202 = cast(Any, None)
        return response_202

    response_default = ErrorResponse.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | DeleteProtectedVirtualMachineBackupResponse200 | ErrorResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    backup_uid: UUID,
    *,
    client: AuthenticatedClient,
    backup_object_uid: UUID,
    select: str | Unset = UNSET,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Response[Any | DeleteProtectedVirtualMachineBackupResponse200 | ErrorResponse]:
    """Delete Protected VM Backup Object

     Deletes a protected VM backup object with the specified UID.

    Args:
        backup_uid (UUID):
        backup_object_uid (UUID):
        select (str | Unset):
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DeleteProtectedVirtualMachineBackupResponse200 | ErrorResponse]
    """

    kwargs = _get_kwargs(
        backup_uid=backup_uid,
        backup_object_uid=backup_object_uid,
        select=select,
        x_request_id=x_request_id,
        x_client_version=x_client_version,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    backup_uid: UUID,
    *,
    client: AuthenticatedClient,
    backup_object_uid: UUID,
    select: str | Unset = UNSET,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Any | DeleteProtectedVirtualMachineBackupResponse200 | ErrorResponse | None:
    """Delete Protected VM Backup Object

     Deletes a protected VM backup object with the specified UID.

    Args:
        backup_uid (UUID):
        backup_object_uid (UUID):
        select (str | Unset):
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DeleteProtectedVirtualMachineBackupResponse200 | ErrorResponse
    """

    return sync_detailed(
        backup_uid=backup_uid,
        client=client,
        backup_object_uid=backup_object_uid,
        select=select,
        x_request_id=x_request_id,
        x_client_version=x_client_version,
    ).parsed


async def asyncio_detailed(
    backup_uid: UUID,
    *,
    client: AuthenticatedClient,
    backup_object_uid: UUID,
    select: str | Unset = UNSET,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Response[Any | DeleteProtectedVirtualMachineBackupResponse200 | ErrorResponse]:
    """Delete Protected VM Backup Object

     Deletes a protected VM backup object with the specified UID.

    Args:
        backup_uid (UUID):
        backup_object_uid (UUID):
        select (str | Unset):
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DeleteProtectedVirtualMachineBackupResponse200 | ErrorResponse]
    """

    kwargs = _get_kwargs(
        backup_uid=backup_uid,
        backup_object_uid=backup_object_uid,
        select=select,
        x_request_id=x_request_id,
        x_client_version=x_client_version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    backup_uid: UUID,
    *,
    client: AuthenticatedClient,
    backup_object_uid: UUID,
    select: str | Unset = UNSET,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Any | DeleteProtectedVirtualMachineBackupResponse200 | ErrorResponse | None:
    """Delete Protected VM Backup Object

     Deletes a protected VM backup object with the specified UID.

    Args:
        backup_uid (UUID):
        backup_object_uid (UUID):
        select (str | Unset):
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DeleteProtectedVirtualMachineBackupResponse200 | ErrorResponse
    """

    return (
        await asyncio_detailed(
            backup_uid=backup_uid,
            client=client,
            backup_object_uid=backup_object_uid,
            select=select,
            x_request_id=x_request_id,
            x_client_version=x_client_version,
        )
    ).parsed
