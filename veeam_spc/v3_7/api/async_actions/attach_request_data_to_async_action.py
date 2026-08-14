from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.async_action_request_data import AsyncActionRequestData
from ...models.attach_request_data_to_async_action_response_200 import AttachRequestDataToAsyncActionResponse200
from ...models.error_response import ErrorResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    action_id: UUID,
    *,
    body: AsyncActionRequestData,
    select: str | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_client_version, Unset):
        headers["X-Client-Version"] = x_client_version

    params: dict[str, Any] = {}

    params["select"] = select

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/asyncActions/{action_id}/requestData".format(
            action_id=quote(str(action_id), safe=""),
        ),
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AttachRequestDataToAsyncActionResponse200 | ErrorResponse:
    if response.status_code == 200:
        response_200 = AttachRequestDataToAsyncActionResponse200.from_dict(response.json())

        return response_200

    response_default = ErrorResponse.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[AttachRequestDataToAsyncActionResponse200 | ErrorResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    action_id: UUID,
    *,
    client: AuthenticatedClient,
    body: AsyncActionRequestData,
    select: str | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Response[AttachRequestDataToAsyncActionResponse200 | ErrorResponse]:
    """Attach Request Data to Async Action

     Attaches provided request data to an async action with the specified UID.

    Args:
        action_id (UUID):
        select (str | Unset):
        x_client_version (str | Unset):
        body (AsyncActionRequestData):  Example: {'requestBody': '{ "siteUid":
            "d18f40ef-a80f-45c0-a4b6-0de1f5615145", "cloudTenantType": "General",
            "vCloudOrganizationUid": null, "leaseExpirationEnabled": false, "ownerCredentials": {
            "userName": "Alpha", "password": "Password1" }, "description": "Site Resource for Alpha
            Company", "throttlingEnabled": false, "throttlingValue": 1, "throttlingUnit":
            "MbitPerSec", "maxConcurrentTask": 1, "backupProtectionEnabled": false,
            "backupProtectionPeriodDays": 1, "gatewaySelectionType": "StandaloneGateways",
            "isGatewayFailoverEnabled": false}', 'queryParameters': None}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AttachRequestDataToAsyncActionResponse200 | ErrorResponse]
    """

    kwargs = _get_kwargs(
        action_id=action_id,
        body=body,
        select=select,
        x_client_version=x_client_version,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    action_id: UUID,
    *,
    client: AuthenticatedClient,
    body: AsyncActionRequestData,
    select: str | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> AttachRequestDataToAsyncActionResponse200 | ErrorResponse | None:
    """Attach Request Data to Async Action

     Attaches provided request data to an async action with the specified UID.

    Args:
        action_id (UUID):
        select (str | Unset):
        x_client_version (str | Unset):
        body (AsyncActionRequestData):  Example: {'requestBody': '{ "siteUid":
            "d18f40ef-a80f-45c0-a4b6-0de1f5615145", "cloudTenantType": "General",
            "vCloudOrganizationUid": null, "leaseExpirationEnabled": false, "ownerCredentials": {
            "userName": "Alpha", "password": "Password1" }, "description": "Site Resource for Alpha
            Company", "throttlingEnabled": false, "throttlingValue": 1, "throttlingUnit":
            "MbitPerSec", "maxConcurrentTask": 1, "backupProtectionEnabled": false,
            "backupProtectionPeriodDays": 1, "gatewaySelectionType": "StandaloneGateways",
            "isGatewayFailoverEnabled": false}', 'queryParameters': None}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AttachRequestDataToAsyncActionResponse200 | ErrorResponse
    """

    return sync_detailed(
        action_id=action_id,
        client=client,
        body=body,
        select=select,
        x_client_version=x_client_version,
    ).parsed


async def asyncio_detailed(
    action_id: UUID,
    *,
    client: AuthenticatedClient,
    body: AsyncActionRequestData,
    select: str | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Response[AttachRequestDataToAsyncActionResponse200 | ErrorResponse]:
    """Attach Request Data to Async Action

     Attaches provided request data to an async action with the specified UID.

    Args:
        action_id (UUID):
        select (str | Unset):
        x_client_version (str | Unset):
        body (AsyncActionRequestData):  Example: {'requestBody': '{ "siteUid":
            "d18f40ef-a80f-45c0-a4b6-0de1f5615145", "cloudTenantType": "General",
            "vCloudOrganizationUid": null, "leaseExpirationEnabled": false, "ownerCredentials": {
            "userName": "Alpha", "password": "Password1" }, "description": "Site Resource for Alpha
            Company", "throttlingEnabled": false, "throttlingValue": 1, "throttlingUnit":
            "MbitPerSec", "maxConcurrentTask": 1, "backupProtectionEnabled": false,
            "backupProtectionPeriodDays": 1, "gatewaySelectionType": "StandaloneGateways",
            "isGatewayFailoverEnabled": false}', 'queryParameters': None}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AttachRequestDataToAsyncActionResponse200 | ErrorResponse]
    """

    kwargs = _get_kwargs(
        action_id=action_id,
        body=body,
        select=select,
        x_client_version=x_client_version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    action_id: UUID,
    *,
    client: AuthenticatedClient,
    body: AsyncActionRequestData,
    select: str | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> AttachRequestDataToAsyncActionResponse200 | ErrorResponse | None:
    """Attach Request Data to Async Action

     Attaches provided request data to an async action with the specified UID.

    Args:
        action_id (UUID):
        select (str | Unset):
        x_client_version (str | Unset):
        body (AsyncActionRequestData):  Example: {'requestBody': '{ "siteUid":
            "d18f40ef-a80f-45c0-a4b6-0de1f5615145", "cloudTenantType": "General",
            "vCloudOrganizationUid": null, "leaseExpirationEnabled": false, "ownerCredentials": {
            "userName": "Alpha", "password": "Password1" }, "description": "Site Resource for Alpha
            Company", "throttlingEnabled": false, "throttlingValue": 1, "throttlingUnit":
            "MbitPerSec", "maxConcurrentTask": 1, "backupProtectionEnabled": false,
            "backupProtectionPeriodDays": 1, "gatewaySelectionType": "StandaloneGateways",
            "isGatewayFailoverEnabled": false}', 'queryParameters': None}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AttachRequestDataToAsyncActionResponse200 | ErrorResponse
    """

    return (
        await asyncio_detailed(
            action_id=action_id,
            client=client,
            body=body,
            select=select,
            x_client_version=x_client_version,
        )
    ).parsed
