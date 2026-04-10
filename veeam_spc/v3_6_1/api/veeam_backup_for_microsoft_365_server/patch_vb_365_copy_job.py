from http import HTTPStatus
from typing import Any, Optional, Union, cast
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.json_patch import JsonPatch
from ...models.patch_vb_365_copy_job_response_200 import PatchVb365CopyJobResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    vb_365_server_uid: UUID,
    vb_365_copy_job_uid: UUID,
    *,
    body: list["JsonPatch"],
    x_request_id: Union[Unset, UUID] = UNSET,
    x_client_version: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_request_id, Unset):
        headers["X-Request-id"] = x_request_id

    if not isinstance(x_client_version, Unset):
        headers["X-Client-Version"] = x_client_version

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": f"/infrastructure/vb365Servers/{vb_365_server_uid}/organizations/jobs/copy/{vb_365_copy_job_uid}",
    }

    _kwargs["json"] = []
    for componentsschemas_json_patches_item_data in body:
        componentsschemas_json_patches_item = componentsschemas_json_patches_item_data.to_dict()
        _kwargs["json"].append(componentsschemas_json_patches_item)

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Union[Any, ErrorResponse, PatchVb365CopyJobResponse200]:
    if response.status_code == 200:
        response_200 = PatchVb365CopyJobResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 202:
        response_202 = cast(Any, None)
        return response_202

    response_default = ErrorResponse.from_dict(response.json())

    return response_default


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, ErrorResponse, PatchVb365CopyJobResponse200]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    vb_365_server_uid: UUID,
    vb_365_copy_job_uid: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
    body: list["JsonPatch"],
    x_request_id: Union[Unset, UUID] = UNSET,
    x_client_version: Union[Unset, str] = UNSET,
) -> Response[Union[Any, ErrorResponse, PatchVb365CopyJobResponse200]]:
    """Modify Veeam Backup for Microsoft 365 Backup Copy Job

     Modifies a Veeam Backup for Microsoft 365 backup copy job with the specified UID.
    > You can save the job schedule only if that functionality is enabled for you in the Veeam Backup
    for Microsoft 365 resource configuration. Otherwise the operation will result in error.

    Args:
        vb_365_server_uid (UUID):
        vb_365_copy_job_uid (UUID):
        x_request_id (Union[Unset, UUID]):
        x_client_version (Union[Unset, str]):
        body (list['JsonPatch']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ErrorResponse, PatchVb365CopyJobResponse200]]
    """

    kwargs = _get_kwargs(
        vb_365_server_uid=vb_365_server_uid,
        vb_365_copy_job_uid=vb_365_copy_job_uid,
        body=body,
        x_request_id=x_request_id,
        x_client_version=x_client_version,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    vb_365_server_uid: UUID,
    vb_365_copy_job_uid: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
    body: list["JsonPatch"],
    x_request_id: Union[Unset, UUID] = UNSET,
    x_client_version: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, ErrorResponse, PatchVb365CopyJobResponse200]]:
    """Modify Veeam Backup for Microsoft 365 Backup Copy Job

     Modifies a Veeam Backup for Microsoft 365 backup copy job with the specified UID.
    > You can save the job schedule only if that functionality is enabled for you in the Veeam Backup
    for Microsoft 365 resource configuration. Otherwise the operation will result in error.

    Args:
        vb_365_server_uid (UUID):
        vb_365_copy_job_uid (UUID):
        x_request_id (Union[Unset, UUID]):
        x_client_version (Union[Unset, str]):
        body (list['JsonPatch']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ErrorResponse, PatchVb365CopyJobResponse200]
    """

    return sync_detailed(
        vb_365_server_uid=vb_365_server_uid,
        vb_365_copy_job_uid=vb_365_copy_job_uid,
        client=client,
        body=body,
        x_request_id=x_request_id,
        x_client_version=x_client_version,
    ).parsed


async def asyncio_detailed(
    vb_365_server_uid: UUID,
    vb_365_copy_job_uid: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
    body: list["JsonPatch"],
    x_request_id: Union[Unset, UUID] = UNSET,
    x_client_version: Union[Unset, str] = UNSET,
) -> Response[Union[Any, ErrorResponse, PatchVb365CopyJobResponse200]]:
    """Modify Veeam Backup for Microsoft 365 Backup Copy Job

     Modifies a Veeam Backup for Microsoft 365 backup copy job with the specified UID.
    > You can save the job schedule only if that functionality is enabled for you in the Veeam Backup
    for Microsoft 365 resource configuration. Otherwise the operation will result in error.

    Args:
        vb_365_server_uid (UUID):
        vb_365_copy_job_uid (UUID):
        x_request_id (Union[Unset, UUID]):
        x_client_version (Union[Unset, str]):
        body (list['JsonPatch']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ErrorResponse, PatchVb365CopyJobResponse200]]
    """

    kwargs = _get_kwargs(
        vb_365_server_uid=vb_365_server_uid,
        vb_365_copy_job_uid=vb_365_copy_job_uid,
        body=body,
        x_request_id=x_request_id,
        x_client_version=x_client_version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    vb_365_server_uid: UUID,
    vb_365_copy_job_uid: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
    body: list["JsonPatch"],
    x_request_id: Union[Unset, UUID] = UNSET,
    x_client_version: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, ErrorResponse, PatchVb365CopyJobResponse200]]:
    """Modify Veeam Backup for Microsoft 365 Backup Copy Job

     Modifies a Veeam Backup for Microsoft 365 backup copy job with the specified UID.
    > You can save the job schedule only if that functionality is enabled for you in the Veeam Backup
    for Microsoft 365 resource configuration. Otherwise the operation will result in error.

    Args:
        vb_365_server_uid (UUID):
        vb_365_copy_job_uid (UUID):
        x_request_id (Union[Unset, UUID]):
        x_client_version (Union[Unset, str]):
        body (list['JsonPatch']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ErrorResponse, PatchVb365CopyJobResponse200]
    """

    return (
        await asyncio_detailed(
            vb_365_server_uid=vb_365_server_uid,
            vb_365_copy_job_uid=vb_365_copy_job_uid,
            client=client,
            body=body,
            x_request_id=x_request_id,
            x_client_version=x_client_version,
        )
    ).parsed
