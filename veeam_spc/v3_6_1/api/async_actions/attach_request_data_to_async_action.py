from http import HTTPStatus
from typing import Any, Optional, Union
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
    x_client_version: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_client_version, Unset):
        headers["X-Client-Version"] = x_client_version

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": f"/asyncActions/{action_id}/requestData",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Union[AttachRequestDataToAsyncActionResponse200, ErrorResponse]:
    if response.status_code == 200:
        response_200 = AttachRequestDataToAsyncActionResponse200.from_dict(response.json())

        return response_200

    response_default = ErrorResponse.from_dict(response.json())

    return response_default


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[AttachRequestDataToAsyncActionResponse200, ErrorResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    action_id: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
    body: AsyncActionRequestData,
    x_client_version: Union[Unset, str] = UNSET,
) -> Response[Union[AttachRequestDataToAsyncActionResponse200, ErrorResponse]]:
    """Attach Request Data to Async Action

     Attaches provided request data to an async action with the specified UID.

    Args:
        action_id (UUID):
        x_client_version (Union[Unset, str]):
        body (AsyncActionRequestData):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[AttachRequestDataToAsyncActionResponse200, ErrorResponse]]
    """

    kwargs = _get_kwargs(
        action_id=action_id,
        body=body,
        x_client_version=x_client_version,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    action_id: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
    body: AsyncActionRequestData,
    x_client_version: Union[Unset, str] = UNSET,
) -> Optional[Union[AttachRequestDataToAsyncActionResponse200, ErrorResponse]]:
    """Attach Request Data to Async Action

     Attaches provided request data to an async action with the specified UID.

    Args:
        action_id (UUID):
        x_client_version (Union[Unset, str]):
        body (AsyncActionRequestData):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[AttachRequestDataToAsyncActionResponse200, ErrorResponse]
    """

    return sync_detailed(
        action_id=action_id,
        client=client,
        body=body,
        x_client_version=x_client_version,
    ).parsed


async def asyncio_detailed(
    action_id: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
    body: AsyncActionRequestData,
    x_client_version: Union[Unset, str] = UNSET,
) -> Response[Union[AttachRequestDataToAsyncActionResponse200, ErrorResponse]]:
    """Attach Request Data to Async Action

     Attaches provided request data to an async action with the specified UID.

    Args:
        action_id (UUID):
        x_client_version (Union[Unset, str]):
        body (AsyncActionRequestData):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[AttachRequestDataToAsyncActionResponse200, ErrorResponse]]
    """

    kwargs = _get_kwargs(
        action_id=action_id,
        body=body,
        x_client_version=x_client_version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    action_id: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
    body: AsyncActionRequestData,
    x_client_version: Union[Unset, str] = UNSET,
) -> Optional[Union[AttachRequestDataToAsyncActionResponse200, ErrorResponse]]:
    """Attach Request Data to Async Action

     Attaches provided request data to an async action with the specified UID.

    Args:
        action_id (UUID):
        x_client_version (Union[Unset, str]):
        body (AsyncActionRequestData):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[AttachRequestDataToAsyncActionResponse200, ErrorResponse]
    """

    return (
        await asyncio_detailed(
            action_id=action_id,
            client=client,
            body=body,
            x_client_version=x_client_version,
        )
    ).parsed
