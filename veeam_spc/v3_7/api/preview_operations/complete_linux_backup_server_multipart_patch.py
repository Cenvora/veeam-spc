from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.complete_linux_backup_server_multipart_patch_response_200 import (
    CompleteLinuxBackupServerMultipartPatchResponse200,
)
from ...models.error_response import ErrorResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    clustered_agent_uid: UUID,
    *,
    upload_uid: UUID,
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

    json_upload_uid = str(upload_uid)
    params["uploadUid"] = json_upload_uid

    params["select"] = select

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/infrastructure/backupServers/{clustered_agent_uid}/patchLinux/upload/multipart/complete".format(
            clustered_agent_uid=quote(str(clustered_agent_uid), safe=""),
        ),
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | CompleteLinuxBackupServerMultipartPatchResponse200 | ErrorResponse:
    if response.status_code == 200:
        response_200 = CompleteLinuxBackupServerMultipartPatchResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 202:
        response_202 = cast(Any, None)
        return response_202

    response_default = ErrorResponse.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | CompleteLinuxBackupServerMultipartPatchResponse200 | ErrorResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    clustered_agent_uid: UUID,
    *,
    client: AuthenticatedClient,
    upload_uid: UUID,
    select: str | Unset = UNSET,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Response[Any | CompleteLinuxBackupServerMultipartPatchResponse200 | ErrorResponse]:
    """Complete Patch Upload to Veeam Backup & Replication Linux Server

     Finalizes an upload of a patch to Veeam Backup & Replication linux server with the specified UID.

    Args:
        clustered_agent_uid (UUID):
        upload_uid (UUID):
        select (str | Unset):
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CompleteLinuxBackupServerMultipartPatchResponse200 | ErrorResponse]
    """

    kwargs = _get_kwargs(
        clustered_agent_uid=clustered_agent_uid,
        upload_uid=upload_uid,
        select=select,
        x_request_id=x_request_id,
        x_client_version=x_client_version,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    clustered_agent_uid: UUID,
    *,
    client: AuthenticatedClient,
    upload_uid: UUID,
    select: str | Unset = UNSET,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Any | CompleteLinuxBackupServerMultipartPatchResponse200 | ErrorResponse | None:
    """Complete Patch Upload to Veeam Backup & Replication Linux Server

     Finalizes an upload of a patch to Veeam Backup & Replication linux server with the specified UID.

    Args:
        clustered_agent_uid (UUID):
        upload_uid (UUID):
        select (str | Unset):
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CompleteLinuxBackupServerMultipartPatchResponse200 | ErrorResponse
    """

    return sync_detailed(
        clustered_agent_uid=clustered_agent_uid,
        client=client,
        upload_uid=upload_uid,
        select=select,
        x_request_id=x_request_id,
        x_client_version=x_client_version,
    ).parsed


async def asyncio_detailed(
    clustered_agent_uid: UUID,
    *,
    client: AuthenticatedClient,
    upload_uid: UUID,
    select: str | Unset = UNSET,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Response[Any | CompleteLinuxBackupServerMultipartPatchResponse200 | ErrorResponse]:
    """Complete Patch Upload to Veeam Backup & Replication Linux Server

     Finalizes an upload of a patch to Veeam Backup & Replication linux server with the specified UID.

    Args:
        clustered_agent_uid (UUID):
        upload_uid (UUID):
        select (str | Unset):
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CompleteLinuxBackupServerMultipartPatchResponse200 | ErrorResponse]
    """

    kwargs = _get_kwargs(
        clustered_agent_uid=clustered_agent_uid,
        upload_uid=upload_uid,
        select=select,
        x_request_id=x_request_id,
        x_client_version=x_client_version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    clustered_agent_uid: UUID,
    *,
    client: AuthenticatedClient,
    upload_uid: UUID,
    select: str | Unset = UNSET,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Any | CompleteLinuxBackupServerMultipartPatchResponse200 | ErrorResponse | None:
    """Complete Patch Upload to Veeam Backup & Replication Linux Server

     Finalizes an upload of a patch to Veeam Backup & Replication linux server with the specified UID.

    Args:
        clustered_agent_uid (UUID):
        upload_uid (UUID):
        select (str | Unset):
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CompleteLinuxBackupServerMultipartPatchResponse200 | ErrorResponse
    """

    return (
        await asyncio_detailed(
            clustered_agent_uid=clustered_agent_uid,
            client=client,
            upload_uid=upload_uid,
            select=select,
            x_request_id=x_request_id,
            x_client_version=x_client_version,
        )
    ).parsed
