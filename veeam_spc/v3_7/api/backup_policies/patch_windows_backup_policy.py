from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.json_patch import JsonPatch
from ...models.patch_windows_backup_policy_response_200 import PatchWindowsBackupPolicyResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    policy_uid: UUID,
    *,
    body: list[JsonPatch],
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
        "method": "patch",
        "url": "/configuration/backupPolicies/windows/{policy_uid}".format(
            policy_uid=quote(str(policy_uid), safe=""),
        ),
        "params": params,
    }

    _kwargs["json"] = []
    for componentsschemas_json_patches_item_data in body:
        componentsschemas_json_patches_item = componentsschemas_json_patches_item_data.to_dict()
        _kwargs["json"].append(componentsschemas_json_patches_item)

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | ErrorResponse | PatchWindowsBackupPolicyResponse200:
    if response.status_code == 200:
        response_200 = PatchWindowsBackupPolicyResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 202:
        response_202 = cast(Any, None)
        return response_202

    response_default = ErrorResponse.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | ErrorResponse | PatchWindowsBackupPolicyResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    policy_uid: UUID,
    *,
    client: AuthenticatedClient,
    body: list[JsonPatch],
    select: str | Unset = UNSET,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Response[Any | ErrorResponse | PatchWindowsBackupPolicyResponse200]:
    """Modify Backup Policy for Windows Computers

     Modifies a Windows computer backup policy with the specified UID.

    Args:
        policy_uid (UUID):
        select (str | Unset):
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):
        body (list[JsonPatch]):  Example: [{'value': 12477400693578140, 'path': 'storageQuota',
            'op': 'replace'}].

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ErrorResponse | PatchWindowsBackupPolicyResponse200]
    """

    kwargs = _get_kwargs(
        policy_uid=policy_uid,
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
    policy_uid: UUID,
    *,
    client: AuthenticatedClient,
    body: list[JsonPatch],
    select: str | Unset = UNSET,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Any | ErrorResponse | PatchWindowsBackupPolicyResponse200 | None:
    """Modify Backup Policy for Windows Computers

     Modifies a Windows computer backup policy with the specified UID.

    Args:
        policy_uid (UUID):
        select (str | Unset):
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):
        body (list[JsonPatch]):  Example: [{'value': 12477400693578140, 'path': 'storageQuota',
            'op': 'replace'}].

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ErrorResponse | PatchWindowsBackupPolicyResponse200
    """

    return sync_detailed(
        policy_uid=policy_uid,
        client=client,
        body=body,
        select=select,
        x_request_id=x_request_id,
        x_client_version=x_client_version,
    ).parsed


async def asyncio_detailed(
    policy_uid: UUID,
    *,
    client: AuthenticatedClient,
    body: list[JsonPatch],
    select: str | Unset = UNSET,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Response[Any | ErrorResponse | PatchWindowsBackupPolicyResponse200]:
    """Modify Backup Policy for Windows Computers

     Modifies a Windows computer backup policy with the specified UID.

    Args:
        policy_uid (UUID):
        select (str | Unset):
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):
        body (list[JsonPatch]):  Example: [{'value': 12477400693578140, 'path': 'storageQuota',
            'op': 'replace'}].

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ErrorResponse | PatchWindowsBackupPolicyResponse200]
    """

    kwargs = _get_kwargs(
        policy_uid=policy_uid,
        body=body,
        select=select,
        x_request_id=x_request_id,
        x_client_version=x_client_version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    policy_uid: UUID,
    *,
    client: AuthenticatedClient,
    body: list[JsonPatch],
    select: str | Unset = UNSET,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Any | ErrorResponse | PatchWindowsBackupPolicyResponse200 | None:
    """Modify Backup Policy for Windows Computers

     Modifies a Windows computer backup policy with the specified UID.

    Args:
        policy_uid (UUID):
        select (str | Unset):
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):
        body (list[JsonPatch]):  Example: [{'value': 12477400693578140, 'path': 'storageQuota',
            'op': 'replace'}].

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ErrorResponse | PatchWindowsBackupPolicyResponse200
    """

    return (
        await asyncio_detailed(
            policy_uid=policy_uid,
            client=client,
            body=body,
            select=select,
            x_request_id=x_request_id,
            x_client_version=x_client_version,
        )
    ).parsed
