from http import HTTPStatus
from typing import Any, cast
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.create_pulse_license_response_200 import CreatePulseLicenseResponse200
from ...models.error_response import ErrorResponse
from ...models.pulse_license_input import PulseLicenseInput
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PulseLicenseInput,
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
        "url": "/pulse/licenses",
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | CreatePulseLicenseResponse200 | ErrorResponse:
    if response.status_code == 200:
        response_200 = CreatePulseLicenseResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 202:
        response_202 = cast(Any, None)
        return response_202

    response_default = ErrorResponse.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | CreatePulseLicenseResponse200 | ErrorResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: PulseLicenseInput,
    select: str | Unset = UNSET,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Response[Any | CreatePulseLicenseResponse200 | ErrorResponse]:
    """Add License to VCSP Pulse

     Adds a new license configuration with the specified parameters to VCSP Pulse.

    Args:
        select (str | Unset):
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):
        body (PulseLicenseInput):  Example: {'productId': 'VBR_PLS_12_0_0', 'contractId':
            '02553275', 'description': None, 'expirationDate': '2024-04-17T21:09:36.3594704-05:00',
            'isAutomaticReportingEnabled': False, 'workloads': [{'workloadId': 'Public Cloud
            Database_VBR_PLS_12_0_0', 'count': 1}, {'workloadId': 'Public Cloud
            Fileshare_VBR_PLS_12_0_0', 'count': 1}, {'workloadId': 'Server_VBR_PLS_12_0_0', 'count':
            1}, {'workloadId': 'VM_VBR_PLS_12_0_0', 'count': 1}, {'workloadId':
            'Workstation_VBR_PLS_12_0_0', 'count': 1}, {'workloadId': 'Public Cloud
            VM_VBR_PLS_12_0_0', 'count': 1}, {'workloadId': 'File Share_VBR_PLS_12_0_0', 'count': 1},
            {'workloadId': 'Application_VBR_PLS_12_0_0', 'count': 1}]}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CreatePulseLicenseResponse200 | ErrorResponse]
    """

    kwargs = _get_kwargs(
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
    *,
    client: AuthenticatedClient,
    body: PulseLicenseInput,
    select: str | Unset = UNSET,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Any | CreatePulseLicenseResponse200 | ErrorResponse | None:
    """Add License to VCSP Pulse

     Adds a new license configuration with the specified parameters to VCSP Pulse.

    Args:
        select (str | Unset):
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):
        body (PulseLicenseInput):  Example: {'productId': 'VBR_PLS_12_0_0', 'contractId':
            '02553275', 'description': None, 'expirationDate': '2024-04-17T21:09:36.3594704-05:00',
            'isAutomaticReportingEnabled': False, 'workloads': [{'workloadId': 'Public Cloud
            Database_VBR_PLS_12_0_0', 'count': 1}, {'workloadId': 'Public Cloud
            Fileshare_VBR_PLS_12_0_0', 'count': 1}, {'workloadId': 'Server_VBR_PLS_12_0_0', 'count':
            1}, {'workloadId': 'VM_VBR_PLS_12_0_0', 'count': 1}, {'workloadId':
            'Workstation_VBR_PLS_12_0_0', 'count': 1}, {'workloadId': 'Public Cloud
            VM_VBR_PLS_12_0_0', 'count': 1}, {'workloadId': 'File Share_VBR_PLS_12_0_0', 'count': 1},
            {'workloadId': 'Application_VBR_PLS_12_0_0', 'count': 1}]}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CreatePulseLicenseResponse200 | ErrorResponse
    """

    return sync_detailed(
        client=client,
        body=body,
        select=select,
        x_request_id=x_request_id,
        x_client_version=x_client_version,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: PulseLicenseInput,
    select: str | Unset = UNSET,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Response[Any | CreatePulseLicenseResponse200 | ErrorResponse]:
    """Add License to VCSP Pulse

     Adds a new license configuration with the specified parameters to VCSP Pulse.

    Args:
        select (str | Unset):
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):
        body (PulseLicenseInput):  Example: {'productId': 'VBR_PLS_12_0_0', 'contractId':
            '02553275', 'description': None, 'expirationDate': '2024-04-17T21:09:36.3594704-05:00',
            'isAutomaticReportingEnabled': False, 'workloads': [{'workloadId': 'Public Cloud
            Database_VBR_PLS_12_0_0', 'count': 1}, {'workloadId': 'Public Cloud
            Fileshare_VBR_PLS_12_0_0', 'count': 1}, {'workloadId': 'Server_VBR_PLS_12_0_0', 'count':
            1}, {'workloadId': 'VM_VBR_PLS_12_0_0', 'count': 1}, {'workloadId':
            'Workstation_VBR_PLS_12_0_0', 'count': 1}, {'workloadId': 'Public Cloud
            VM_VBR_PLS_12_0_0', 'count': 1}, {'workloadId': 'File Share_VBR_PLS_12_0_0', 'count': 1},
            {'workloadId': 'Application_VBR_PLS_12_0_0', 'count': 1}]}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CreatePulseLicenseResponse200 | ErrorResponse]
    """

    kwargs = _get_kwargs(
        body=body,
        select=select,
        x_request_id=x_request_id,
        x_client_version=x_client_version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: PulseLicenseInput,
    select: str | Unset = UNSET,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Any | CreatePulseLicenseResponse200 | ErrorResponse | None:
    """Add License to VCSP Pulse

     Adds a new license configuration with the specified parameters to VCSP Pulse.

    Args:
        select (str | Unset):
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):
        body (PulseLicenseInput):  Example: {'productId': 'VBR_PLS_12_0_0', 'contractId':
            '02553275', 'description': None, 'expirationDate': '2024-04-17T21:09:36.3594704-05:00',
            'isAutomaticReportingEnabled': False, 'workloads': [{'workloadId': 'Public Cloud
            Database_VBR_PLS_12_0_0', 'count': 1}, {'workloadId': 'Public Cloud
            Fileshare_VBR_PLS_12_0_0', 'count': 1}, {'workloadId': 'Server_VBR_PLS_12_0_0', 'count':
            1}, {'workloadId': 'VM_VBR_PLS_12_0_0', 'count': 1}, {'workloadId':
            'Workstation_VBR_PLS_12_0_0', 'count': 1}, {'workloadId': 'Public Cloud
            VM_VBR_PLS_12_0_0', 'count': 1}, {'workloadId': 'File Share_VBR_PLS_12_0_0', 'count': 1},
            {'workloadId': 'Application_VBR_PLS_12_0_0', 'count': 1}]}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CreatePulseLicenseResponse200 | ErrorResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            select=select,
            x_request_id=x_request_id,
            x_client_version=x_client_version,
        )
    ).parsed
