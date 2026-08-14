from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.update_mac_backup_agent_response_200 import UpdateMacBackupAgentResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    backup_agent_uid: UUID,
    *,
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
        "url": "/infrastructure/backupAgents/mac/{backup_agent_uid}/update".format(
            backup_agent_uid=quote(str(backup_agent_uid), safe=""),
        ),
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | ErrorResponse | UpdateMacBackupAgentResponse200:
    if response.status_code == 200:
        response_200 = UpdateMacBackupAgentResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 202:
        response_202 = cast(Any, None)
        return response_202

    response_default = ErrorResponse.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | ErrorResponse | UpdateMacBackupAgentResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    backup_agent_uid: UUID,
    *,
    client: AuthenticatedClient,
    select: str | Unset = UNSET,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Response[Any | ErrorResponse | UpdateMacBackupAgentResponse200]:
    """Update Veeam Agent for Mac

     Updates a Veeam Agent for Mac with the specified UID.
    > To track the deployment progress, you can use the `WaitDeploymentTask` operation.

    Args:
        backup_agent_uid (UUID):
        select (str | Unset):
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ErrorResponse | UpdateMacBackupAgentResponse200]
    """

    kwargs = _get_kwargs(
        backup_agent_uid=backup_agent_uid,
        select=select,
        x_request_id=x_request_id,
        x_client_version=x_client_version,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    backup_agent_uid: UUID,
    *,
    client: AuthenticatedClient,
    select: str | Unset = UNSET,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Any | ErrorResponse | UpdateMacBackupAgentResponse200 | None:
    """Update Veeam Agent for Mac

     Updates a Veeam Agent for Mac with the specified UID.
    > To track the deployment progress, you can use the `WaitDeploymentTask` operation.

    Args:
        backup_agent_uid (UUID):
        select (str | Unset):
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ErrorResponse | UpdateMacBackupAgentResponse200
    """

    return sync_detailed(
        backup_agent_uid=backup_agent_uid,
        client=client,
        select=select,
        x_request_id=x_request_id,
        x_client_version=x_client_version,
    ).parsed


async def asyncio_detailed(
    backup_agent_uid: UUID,
    *,
    client: AuthenticatedClient,
    select: str | Unset = UNSET,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Response[Any | ErrorResponse | UpdateMacBackupAgentResponse200]:
    """Update Veeam Agent for Mac

     Updates a Veeam Agent for Mac with the specified UID.
    > To track the deployment progress, you can use the `WaitDeploymentTask` operation.

    Args:
        backup_agent_uid (UUID):
        select (str | Unset):
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ErrorResponse | UpdateMacBackupAgentResponse200]
    """

    kwargs = _get_kwargs(
        backup_agent_uid=backup_agent_uid,
        select=select,
        x_request_id=x_request_id,
        x_client_version=x_client_version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    backup_agent_uid: UUID,
    *,
    client: AuthenticatedClient,
    select: str | Unset = UNSET,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Any | ErrorResponse | UpdateMacBackupAgentResponse200 | None:
    """Update Veeam Agent for Mac

     Updates a Veeam Agent for Mac with the specified UID.
    > To track the deployment progress, you can use the `WaitDeploymentTask` operation.

    Args:
        backup_agent_uid (UUID):
        select (str | Unset):
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ErrorResponse | UpdateMacBackupAgentResponse200
    """

    return (
        await asyncio_detailed(
            backup_agent_uid=backup_agent_uid,
            client=client,
            select=select,
            x_request_id=x_request_id,
            x_client_version=x_client_version,
        )
    ).parsed
