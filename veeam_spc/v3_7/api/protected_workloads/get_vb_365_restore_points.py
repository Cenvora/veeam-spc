from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.get_vb_365_restore_points_response_200 import GetVb365RestorePointsResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    vb_365_protected_object_id: str,
    *,
    vb_365_server_uid: UUID,
    vb_365_backup_repository_uid: UUID | Unset = UNSET,
    filter_: str | Unset = UNSET,
    sort: str | Unset = UNSET,
    limit: int | Unset = 100,
    offset: int | Unset = 0,
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

    json_vb_365_server_uid = str(vb_365_server_uid)
    params["vb365ServerUid"] = json_vb_365_server_uid

    json_vb_365_backup_repository_uid: str | Unset = UNSET
    if not isinstance(vb_365_backup_repository_uid, Unset):
        json_vb_365_backup_repository_uid = str(vb_365_backup_repository_uid)
    params["vb365BackupRepositoryUid"] = json_vb_365_backup_repository_uid

    params["filter"] = filter_

    params["sort"] = sort

    params["limit"] = limit

    params["offset"] = offset

    params["select"] = select

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/protectedWorkloads/vb365ProtectedObjects/{vb_365_protected_object_id}/restorePoints".format(
            vb_365_protected_object_id=quote(str(vb_365_protected_object_id), safe=""),
        ),
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | ErrorResponse | GetVb365RestorePointsResponse200:
    if response.status_code == 200:
        response_200 = GetVb365RestorePointsResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 202:
        response_202 = cast(Any, None)
        return response_202

    response_default = ErrorResponse.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | ErrorResponse | GetVb365RestorePointsResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    vb_365_protected_object_id: str,
    *,
    client: AuthenticatedClient,
    vb_365_server_uid: UUID,
    vb_365_backup_repository_uid: UUID | Unset = UNSET,
    filter_: str | Unset = UNSET,
    sort: str | Unset = UNSET,
    limit: int | Unset = 100,
    offset: int | Unset = 0,
    select: str | Unset = UNSET,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Response[Any | ErrorResponse | GetVb365RestorePointsResponse200]:
    """Get All Restore Points of Object Protected by Veeam Backup for Microsoft 365

     Returns a collection resource representation of all restore points of an object with the specified
    UID protected by Veeam Backup for Microsoft 365.

    Args:
        vb_365_protected_object_id (str):
        vb_365_server_uid (UUID):
        vb_365_backup_repository_uid (UUID | Unset):
        filter_ (str | Unset):
        sort (str | Unset):
        limit (int | Unset):  Default: 100.
        offset (int | Unset):  Default: 0.
        select (str | Unset):
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ErrorResponse | GetVb365RestorePointsResponse200]
    """

    kwargs = _get_kwargs(
        vb_365_protected_object_id=vb_365_protected_object_id,
        vb_365_server_uid=vb_365_server_uid,
        vb_365_backup_repository_uid=vb_365_backup_repository_uid,
        filter_=filter_,
        sort=sort,
        limit=limit,
        offset=offset,
        select=select,
        x_request_id=x_request_id,
        x_client_version=x_client_version,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    vb_365_protected_object_id: str,
    *,
    client: AuthenticatedClient,
    vb_365_server_uid: UUID,
    vb_365_backup_repository_uid: UUID | Unset = UNSET,
    filter_: str | Unset = UNSET,
    sort: str | Unset = UNSET,
    limit: int | Unset = 100,
    offset: int | Unset = 0,
    select: str | Unset = UNSET,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Any | ErrorResponse | GetVb365RestorePointsResponse200 | None:
    """Get All Restore Points of Object Protected by Veeam Backup for Microsoft 365

     Returns a collection resource representation of all restore points of an object with the specified
    UID protected by Veeam Backup for Microsoft 365.

    Args:
        vb_365_protected_object_id (str):
        vb_365_server_uid (UUID):
        vb_365_backup_repository_uid (UUID | Unset):
        filter_ (str | Unset):
        sort (str | Unset):
        limit (int | Unset):  Default: 100.
        offset (int | Unset):  Default: 0.
        select (str | Unset):
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ErrorResponse | GetVb365RestorePointsResponse200
    """

    return sync_detailed(
        vb_365_protected_object_id=vb_365_protected_object_id,
        client=client,
        vb_365_server_uid=vb_365_server_uid,
        vb_365_backup_repository_uid=vb_365_backup_repository_uid,
        filter_=filter_,
        sort=sort,
        limit=limit,
        offset=offset,
        select=select,
        x_request_id=x_request_id,
        x_client_version=x_client_version,
    ).parsed


async def asyncio_detailed(
    vb_365_protected_object_id: str,
    *,
    client: AuthenticatedClient,
    vb_365_server_uid: UUID,
    vb_365_backup_repository_uid: UUID | Unset = UNSET,
    filter_: str | Unset = UNSET,
    sort: str | Unset = UNSET,
    limit: int | Unset = 100,
    offset: int | Unset = 0,
    select: str | Unset = UNSET,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Response[Any | ErrorResponse | GetVb365RestorePointsResponse200]:
    """Get All Restore Points of Object Protected by Veeam Backup for Microsoft 365

     Returns a collection resource representation of all restore points of an object with the specified
    UID protected by Veeam Backup for Microsoft 365.

    Args:
        vb_365_protected_object_id (str):
        vb_365_server_uid (UUID):
        vb_365_backup_repository_uid (UUID | Unset):
        filter_ (str | Unset):
        sort (str | Unset):
        limit (int | Unset):  Default: 100.
        offset (int | Unset):  Default: 0.
        select (str | Unset):
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ErrorResponse | GetVb365RestorePointsResponse200]
    """

    kwargs = _get_kwargs(
        vb_365_protected_object_id=vb_365_protected_object_id,
        vb_365_server_uid=vb_365_server_uid,
        vb_365_backup_repository_uid=vb_365_backup_repository_uid,
        filter_=filter_,
        sort=sort,
        limit=limit,
        offset=offset,
        select=select,
        x_request_id=x_request_id,
        x_client_version=x_client_version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    vb_365_protected_object_id: str,
    *,
    client: AuthenticatedClient,
    vb_365_server_uid: UUID,
    vb_365_backup_repository_uid: UUID | Unset = UNSET,
    filter_: str | Unset = UNSET,
    sort: str | Unset = UNSET,
    limit: int | Unset = 100,
    offset: int | Unset = 0,
    select: str | Unset = UNSET,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Any | ErrorResponse | GetVb365RestorePointsResponse200 | None:
    """Get All Restore Points of Object Protected by Veeam Backup for Microsoft 365

     Returns a collection resource representation of all restore points of an object with the specified
    UID protected by Veeam Backup for Microsoft 365.

    Args:
        vb_365_protected_object_id (str):
        vb_365_server_uid (UUID):
        vb_365_backup_repository_uid (UUID | Unset):
        filter_ (str | Unset):
        sort (str | Unset):
        limit (int | Unset):  Default: 100.
        offset (int | Unset):  Default: 0.
        select (str | Unset):
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ErrorResponse | GetVb365RestorePointsResponse200
    """

    return (
        await asyncio_detailed(
            vb_365_protected_object_id=vb_365_protected_object_id,
            client=client,
            vb_365_server_uid=vb_365_server_uid,
            vb_365_backup_repository_uid=vb_365_backup_repository_uid,
            filter_=filter_,
            sort=sort,
            limit=limit,
            offset=offset,
            select=select,
            x_request_id=x_request_id,
            x_client_version=x_client_version,
        )
    ).parsed
