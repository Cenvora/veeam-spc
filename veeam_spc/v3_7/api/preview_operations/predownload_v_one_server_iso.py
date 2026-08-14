from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.predownload_v_one_server_iso_response_200 import PredownloadVOneServerIsoResponse200
from ...models.v_one_iso_predownload_input import VOneIsoPredownloadInput
from ...types import UNSET, Response, Unset


def _get_kwargs(
    v_one_server_uid: UUID,
    *,
    body: VOneIsoPredownloadInput,
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
        "url": "/infrastructure/voneServers/{v_one_server_uid}/upgrade/iso/predownload".format(
            v_one_server_uid=quote(str(v_one_server_uid), safe=""),
        ),
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | ErrorResponse | PredownloadVOneServerIsoResponse200:
    if response.status_code == 200:
        response_200 = PredownloadVOneServerIsoResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 202:
        response_202 = cast(Any, None)
        return response_202

    response_default = ErrorResponse.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | ErrorResponse | PredownloadVOneServerIsoResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    v_one_server_uid: UUID,
    *,
    client: AuthenticatedClient,
    body: VOneIsoPredownloadInput,
    select: str | Unset = UNSET,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Response[Any | ErrorResponse | PredownloadVOneServerIsoResponse200]:
    r"""Download Veeam ONE Upgrade Setup File

     Downloads the Veeam ONE upgrade setup file for further installation to a server with the specified
    UID.

    Args:
        v_one_server_uid (UUID):
        select (str | Unset):
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):
        body (VOneIsoPredownloadInput): Setup file predownload configuration. Example: {'path':
            'C:\\ProgramData\\Veeam\\Veeam Availability Console'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ErrorResponse | PredownloadVOneServerIsoResponse200]
    """

    kwargs = _get_kwargs(
        v_one_server_uid=v_one_server_uid,
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
    v_one_server_uid: UUID,
    *,
    client: AuthenticatedClient,
    body: VOneIsoPredownloadInput,
    select: str | Unset = UNSET,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Any | ErrorResponse | PredownloadVOneServerIsoResponse200 | None:
    r"""Download Veeam ONE Upgrade Setup File

     Downloads the Veeam ONE upgrade setup file for further installation to a server with the specified
    UID.

    Args:
        v_one_server_uid (UUID):
        select (str | Unset):
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):
        body (VOneIsoPredownloadInput): Setup file predownload configuration. Example: {'path':
            'C:\\ProgramData\\Veeam\\Veeam Availability Console'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ErrorResponse | PredownloadVOneServerIsoResponse200
    """

    return sync_detailed(
        v_one_server_uid=v_one_server_uid,
        client=client,
        body=body,
        select=select,
        x_request_id=x_request_id,
        x_client_version=x_client_version,
    ).parsed


async def asyncio_detailed(
    v_one_server_uid: UUID,
    *,
    client: AuthenticatedClient,
    body: VOneIsoPredownloadInput,
    select: str | Unset = UNSET,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Response[Any | ErrorResponse | PredownloadVOneServerIsoResponse200]:
    r"""Download Veeam ONE Upgrade Setup File

     Downloads the Veeam ONE upgrade setup file for further installation to a server with the specified
    UID.

    Args:
        v_one_server_uid (UUID):
        select (str | Unset):
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):
        body (VOneIsoPredownloadInput): Setup file predownload configuration. Example: {'path':
            'C:\\ProgramData\\Veeam\\Veeam Availability Console'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ErrorResponse | PredownloadVOneServerIsoResponse200]
    """

    kwargs = _get_kwargs(
        v_one_server_uid=v_one_server_uid,
        body=body,
        select=select,
        x_request_id=x_request_id,
        x_client_version=x_client_version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    v_one_server_uid: UUID,
    *,
    client: AuthenticatedClient,
    body: VOneIsoPredownloadInput,
    select: str | Unset = UNSET,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Any | ErrorResponse | PredownloadVOneServerIsoResponse200 | None:
    r"""Download Veeam ONE Upgrade Setup File

     Downloads the Veeam ONE upgrade setup file for further installation to a server with the specified
    UID.

    Args:
        v_one_server_uid (UUID):
        select (str | Unset):
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):
        body (VOneIsoPredownloadInput): Setup file predownload configuration. Example: {'path':
            'C:\\ProgramData\\Veeam\\Veeam Availability Console'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ErrorResponse | PredownloadVOneServerIsoResponse200
    """

    return (
        await asyncio_detailed(
            v_one_server_uid=v_one_server_uid,
            client=client,
            body=body,
            select=select,
            x_request_id=x_request_id,
            x_client_version=x_client_version,
        )
    ).parsed
