from http import HTTPStatus
from typing import Any, Optional, Union, cast
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.empty_response import EmptyResponse
from ...models.error_response import ErrorResponse
from ...types import UNSET, File, Response, Unset


def _get_kwargs(
    v_one_server_uid: UUID,
    *,
    body: File,
    upload_uid: UUID,
    file_stream_uid: UUID,
    part_number: int,
    x_request_id: Union[Unset, UUID] = UNSET,
    x_client_version: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_request_id, Unset):
        headers["X-Request-id"] = x_request_id

    if not isinstance(x_client_version, Unset):
        headers["X-Client-Version"] = x_client_version

    params: dict[str, Any] = {}

    json_upload_uid = str(upload_uid)
    params["uploadUid"] = json_upload_uid

    json_file_stream_uid = str(file_stream_uid)
    params["fileStreamUid"] = json_file_stream_uid

    params["partNumber"] = part_number

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/infrastructure/voneServers/{v_one_server_uid}/patch/upload/multipart/uploadPart",
        "params": params,
    }

    _kwargs["content"] = body.payload

    headers["Content-Type"] = "application/octet-stream"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Union[Any, EmptyResponse, ErrorResponse]:
    if response.status_code == 200:
        response_200 = EmptyResponse.from_dict(response.json())

        return response_200

    if response.status_code == 202:
        response_202 = cast(Any, None)
        return response_202

    response_default = ErrorResponse.from_dict(response.json())

    return response_default


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, EmptyResponse, ErrorResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    v_one_server_uid: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
    body: File,
    upload_uid: UUID,
    file_stream_uid: UUID,
    part_number: int,
    x_request_id: Union[Unset, UUID] = UNSET,
    x_client_version: Union[Unset, str] = UNSET,
) -> Response[Union[Any, EmptyResponse, ErrorResponse]]:
    """Upload Patch File Chunk to Veeam ONE Server

     Uploads a patch file chunk to Veeam ONE server with the specified UID.

    Args:
        v_one_server_uid (UUID):
        upload_uid (UUID):
        file_stream_uid (UUID):
        part_number (int):
        x_request_id (Union[Unset, UUID]):
        x_client_version (Union[Unset, str]):
        body (File):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, EmptyResponse, ErrorResponse]]
    """

    kwargs = _get_kwargs(
        v_one_server_uid=v_one_server_uid,
        body=body,
        upload_uid=upload_uid,
        file_stream_uid=file_stream_uid,
        part_number=part_number,
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
    client: Union[AuthenticatedClient, Client],
    body: File,
    upload_uid: UUID,
    file_stream_uid: UUID,
    part_number: int,
    x_request_id: Union[Unset, UUID] = UNSET,
    x_client_version: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, EmptyResponse, ErrorResponse]]:
    """Upload Patch File Chunk to Veeam ONE Server

     Uploads a patch file chunk to Veeam ONE server with the specified UID.

    Args:
        v_one_server_uid (UUID):
        upload_uid (UUID):
        file_stream_uid (UUID):
        part_number (int):
        x_request_id (Union[Unset, UUID]):
        x_client_version (Union[Unset, str]):
        body (File):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, EmptyResponse, ErrorResponse]
    """

    return sync_detailed(
        v_one_server_uid=v_one_server_uid,
        client=client,
        body=body,
        upload_uid=upload_uid,
        file_stream_uid=file_stream_uid,
        part_number=part_number,
        x_request_id=x_request_id,
        x_client_version=x_client_version,
    ).parsed


async def asyncio_detailed(
    v_one_server_uid: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
    body: File,
    upload_uid: UUID,
    file_stream_uid: UUID,
    part_number: int,
    x_request_id: Union[Unset, UUID] = UNSET,
    x_client_version: Union[Unset, str] = UNSET,
) -> Response[Union[Any, EmptyResponse, ErrorResponse]]:
    """Upload Patch File Chunk to Veeam ONE Server

     Uploads a patch file chunk to Veeam ONE server with the specified UID.

    Args:
        v_one_server_uid (UUID):
        upload_uid (UUID):
        file_stream_uid (UUID):
        part_number (int):
        x_request_id (Union[Unset, UUID]):
        x_client_version (Union[Unset, str]):
        body (File):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, EmptyResponse, ErrorResponse]]
    """

    kwargs = _get_kwargs(
        v_one_server_uid=v_one_server_uid,
        body=body,
        upload_uid=upload_uid,
        file_stream_uid=file_stream_uid,
        part_number=part_number,
        x_request_id=x_request_id,
        x_client_version=x_client_version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    v_one_server_uid: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
    body: File,
    upload_uid: UUID,
    file_stream_uid: UUID,
    part_number: int,
    x_request_id: Union[Unset, UUID] = UNSET,
    x_client_version: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, EmptyResponse, ErrorResponse]]:
    """Upload Patch File Chunk to Veeam ONE Server

     Uploads a patch file chunk to Veeam ONE server with the specified UID.

    Args:
        v_one_server_uid (UUID):
        upload_uid (UUID):
        file_stream_uid (UUID):
        part_number (int):
        x_request_id (Union[Unset, UUID]):
        x_client_version (Union[Unset, str]):
        body (File):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, EmptyResponse, ErrorResponse]
    """

    return (
        await asyncio_detailed(
            v_one_server_uid=v_one_server_uid,
            client=client,
            body=body,
            upload_uid=upload_uid,
            file_stream_uid=file_stream_uid,
            part_number=part_number,
            x_request_id=x_request_id,
            x_client_version=x_client_version,
        )
    ).parsed
