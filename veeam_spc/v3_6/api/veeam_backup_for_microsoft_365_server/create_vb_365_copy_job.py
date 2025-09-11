from http import HTTPStatus
from typing import Any, Optional, Union, cast
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.create_vb_365_copy_job_response_200 import CreateVb365CopyJobResponse200
from ...models.error_response import ErrorResponse
from ...models.vb_365_copy_job import Vb365CopyJob
from ...types import UNSET, Response, Unset


def _get_kwargs(
    vb_365_server_uid: UUID,
    *,
    body: Vb365CopyJob,
    start_job_after_creation: Union[Unset, bool] = False,
    x_request_id: Union[Unset, UUID] = UNSET,
    x_client_version: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_request_id, Unset):
        headers["X-Request-id"] = x_request_id

    if not isinstance(x_client_version, Unset):
        headers["X-Client-Version"] = x_client_version

    params: dict[str, Any] = {}

    params["startJobAfterCreation"] = start_job_after_creation

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/infrastructure/vb365Servers/{vb_365_server_uid}/organizations/jobs/copy",
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Union[Any, CreateVb365CopyJobResponse200, ErrorResponse]:
    if response.status_code == 200:
        response_200 = CreateVb365CopyJobResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 202:
        response_202 = cast(Any, None)
        return response_202

    response_default = ErrorResponse.from_dict(response.json())

    return response_default


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, CreateVb365CopyJobResponse200, ErrorResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    vb_365_server_uid: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
    body: Vb365CopyJob,
    start_job_after_creation: Union[Unset, bool] = False,
    x_request_id: Union[Unset, UUID] = UNSET,
    x_client_version: Union[Unset, str] = UNSET,
) -> Response[Union[Any, CreateVb365CopyJobResponse200, ErrorResponse]]:
    """Create Veeam Backup for Microsoft 365 Backup Copy Job

     Creates a new Veeam Backup for Microsoft 365 backup copy job.
    > You can save the job schedule only if that functionality is enabled for you in the Veeam Backup
    for Microsoft 365 resource configuration. Otherwise the operation will result in error.

    Args:
        vb_365_server_uid (UUID):
        start_job_after_creation (Union[Unset, bool]):  Default: False.
        x_request_id (Union[Unset, UUID]):
        x_client_version (Union[Unset, str]):
        body (Vb365CopyJob):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, CreateVb365CopyJobResponse200, ErrorResponse]]
    """

    kwargs = _get_kwargs(
        vb_365_server_uid=vb_365_server_uid,
        body=body,
        start_job_after_creation=start_job_after_creation,
        x_request_id=x_request_id,
        x_client_version=x_client_version,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    vb_365_server_uid: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
    body: Vb365CopyJob,
    start_job_after_creation: Union[Unset, bool] = False,
    x_request_id: Union[Unset, UUID] = UNSET,
    x_client_version: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, CreateVb365CopyJobResponse200, ErrorResponse]]:
    """Create Veeam Backup for Microsoft 365 Backup Copy Job

     Creates a new Veeam Backup for Microsoft 365 backup copy job.
    > You can save the job schedule only if that functionality is enabled for you in the Veeam Backup
    for Microsoft 365 resource configuration. Otherwise the operation will result in error.

    Args:
        vb_365_server_uid (UUID):
        start_job_after_creation (Union[Unset, bool]):  Default: False.
        x_request_id (Union[Unset, UUID]):
        x_client_version (Union[Unset, str]):
        body (Vb365CopyJob):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, CreateVb365CopyJobResponse200, ErrorResponse]
    """

    return sync_detailed(
        vb_365_server_uid=vb_365_server_uid,
        client=client,
        body=body,
        start_job_after_creation=start_job_after_creation,
        x_request_id=x_request_id,
        x_client_version=x_client_version,
    ).parsed


async def asyncio_detailed(
    vb_365_server_uid: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
    body: Vb365CopyJob,
    start_job_after_creation: Union[Unset, bool] = False,
    x_request_id: Union[Unset, UUID] = UNSET,
    x_client_version: Union[Unset, str] = UNSET,
) -> Response[Union[Any, CreateVb365CopyJobResponse200, ErrorResponse]]:
    """Create Veeam Backup for Microsoft 365 Backup Copy Job

     Creates a new Veeam Backup for Microsoft 365 backup copy job.
    > You can save the job schedule only if that functionality is enabled for you in the Veeam Backup
    for Microsoft 365 resource configuration. Otherwise the operation will result in error.

    Args:
        vb_365_server_uid (UUID):
        start_job_after_creation (Union[Unset, bool]):  Default: False.
        x_request_id (Union[Unset, UUID]):
        x_client_version (Union[Unset, str]):
        body (Vb365CopyJob):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, CreateVb365CopyJobResponse200, ErrorResponse]]
    """

    kwargs = _get_kwargs(
        vb_365_server_uid=vb_365_server_uid,
        body=body,
        start_job_after_creation=start_job_after_creation,
        x_request_id=x_request_id,
        x_client_version=x_client_version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    vb_365_server_uid: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
    body: Vb365CopyJob,
    start_job_after_creation: Union[Unset, bool] = False,
    x_request_id: Union[Unset, UUID] = UNSET,
    x_client_version: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, CreateVb365CopyJobResponse200, ErrorResponse]]:
    """Create Veeam Backup for Microsoft 365 Backup Copy Job

     Creates a new Veeam Backup for Microsoft 365 backup copy job.
    > You can save the job schedule only if that functionality is enabled for you in the Veeam Backup
    for Microsoft 365 resource configuration. Otherwise the operation will result in error.

    Args:
        vb_365_server_uid (UUID):
        start_job_after_creation (Union[Unset, bool]):  Default: False.
        x_request_id (Union[Unset, UUID]):
        x_client_version (Union[Unset, str]):
        body (Vb365CopyJob):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, CreateVb365CopyJobResponse200, ErrorResponse]
    """

    return (
        await asyncio_detailed(
            vb_365_server_uid=vb_365_server_uid,
            client=client,
            body=body,
            start_job_after_creation=start_job_after_creation,
            x_request_id=x_request_id,
            x_client_version=x_client_version,
        )
    ).parsed
