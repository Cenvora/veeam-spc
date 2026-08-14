from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.json_patch import JsonPatch
from ...models.patch_windows_active_directory_based_discovery_rule_response_200 import (
    PatchWindowsActiveDirectoryBasedDiscoveryRuleResponse200,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    rule_uid: UUID,
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
        "url": "/discovery/rules/windows/adBased/{rule_uid}".format(
            rule_uid=quote(str(rule_uid), safe=""),
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
) -> Any | ErrorResponse | PatchWindowsActiveDirectoryBasedDiscoveryRuleResponse200:
    if response.status_code == 200:
        response_200 = PatchWindowsActiveDirectoryBasedDiscoveryRuleResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 202:
        response_202 = cast(Any, None)
        return response_202

    response_default = ErrorResponse.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | ErrorResponse | PatchWindowsActiveDirectoryBasedDiscoveryRuleResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    rule_uid: UUID,
    *,
    client: AuthenticatedClient,
    body: list[JsonPatch],
    select: str | Unset = UNSET,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Response[Any | ErrorResponse | PatchWindowsActiveDirectoryBasedDiscoveryRuleResponse200]:
    """Modify Microsoft Entra ID Discovery Rule for Windows

     Modifies an Microsoft Entra ID discovery rule with the specified UID.

    Args:
        rule_uid (UUID):
        select (str | Unset):
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):
        body (list[JsonPatch]):  Example: [{'value': 12477400693578140, 'path': 'storageQuota',
            'op': 'replace'}].

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ErrorResponse | PatchWindowsActiveDirectoryBasedDiscoveryRuleResponse200]
    """

    kwargs = _get_kwargs(
        rule_uid=rule_uid,
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
    rule_uid: UUID,
    *,
    client: AuthenticatedClient,
    body: list[JsonPatch],
    select: str | Unset = UNSET,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Any | ErrorResponse | PatchWindowsActiveDirectoryBasedDiscoveryRuleResponse200 | None:
    """Modify Microsoft Entra ID Discovery Rule for Windows

     Modifies an Microsoft Entra ID discovery rule with the specified UID.

    Args:
        rule_uid (UUID):
        select (str | Unset):
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):
        body (list[JsonPatch]):  Example: [{'value': 12477400693578140, 'path': 'storageQuota',
            'op': 'replace'}].

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ErrorResponse | PatchWindowsActiveDirectoryBasedDiscoveryRuleResponse200
    """

    return sync_detailed(
        rule_uid=rule_uid,
        client=client,
        body=body,
        select=select,
        x_request_id=x_request_id,
        x_client_version=x_client_version,
    ).parsed


async def asyncio_detailed(
    rule_uid: UUID,
    *,
    client: AuthenticatedClient,
    body: list[JsonPatch],
    select: str | Unset = UNSET,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Response[Any | ErrorResponse | PatchWindowsActiveDirectoryBasedDiscoveryRuleResponse200]:
    """Modify Microsoft Entra ID Discovery Rule for Windows

     Modifies an Microsoft Entra ID discovery rule with the specified UID.

    Args:
        rule_uid (UUID):
        select (str | Unset):
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):
        body (list[JsonPatch]):  Example: [{'value': 12477400693578140, 'path': 'storageQuota',
            'op': 'replace'}].

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ErrorResponse | PatchWindowsActiveDirectoryBasedDiscoveryRuleResponse200]
    """

    kwargs = _get_kwargs(
        rule_uid=rule_uid,
        body=body,
        select=select,
        x_request_id=x_request_id,
        x_client_version=x_client_version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    rule_uid: UUID,
    *,
    client: AuthenticatedClient,
    body: list[JsonPatch],
    select: str | Unset = UNSET,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Any | ErrorResponse | PatchWindowsActiveDirectoryBasedDiscoveryRuleResponse200 | None:
    """Modify Microsoft Entra ID Discovery Rule for Windows

     Modifies an Microsoft Entra ID discovery rule with the specified UID.

    Args:
        rule_uid (UUID):
        select (str | Unset):
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):
        body (list[JsonPatch]):  Example: [{'value': 12477400693578140, 'path': 'storageQuota',
            'op': 'replace'}].

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ErrorResponse | PatchWindowsActiveDirectoryBasedDiscoveryRuleResponse200
    """

    return (
        await asyncio_detailed(
            rule_uid=rule_uid,
            client=client,
            body=body,
            select=select,
            x_request_id=x_request_id,
            x_client_version=x_client_version,
        )
    ).parsed
