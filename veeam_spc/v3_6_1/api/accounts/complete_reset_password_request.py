from http import HTTPStatus
from typing import Any, Optional, Union, cast
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.complete_reset_password_request_body import CompleteResetPasswordRequestBody
from ...models.complete_reset_password_request_response_200 import CompleteResetPasswordRequestResponse200
from ...models.error_response import ErrorResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: CompleteResetPasswordRequestBody,
    x_request_id: Union[Unset, UUID] = UNSET,
    x_client_version: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_request_id, Unset):
        headers["X-Request-id"] = x_request_id

    if not isinstance(x_client_version, Unset):
        headers["X-Client-Version"] = x_client_version

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/users/resetpassword",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Union[Any, CompleteResetPasswordRequestResponse200, ErrorResponse]:
    if response.status_code == 200:
        response_200 = CompleteResetPasswordRequestResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 202:
        response_202 = cast(Any, None)
        return response_202

    response_default = ErrorResponse.from_dict(response.json())

    return response_default


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, CompleteResetPasswordRequestResponse200, ErrorResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: CompleteResetPasswordRequestBody,
    x_request_id: Union[Unset, UUID] = UNSET,
    x_client_version: Union[Unset, str] = UNSET,
) -> Response[Union[Any, CompleteResetPasswordRequestResponse200, ErrorResponse]]:
    """Complete Password Reset

     Completes a request for password reset.

    Args:
        x_request_id (Union[Unset, UUID]):
        x_client_version (Union[Unset, str]):
        body (CompleteResetPasswordRequestBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, CompleteResetPasswordRequestResponse200, ErrorResponse]]
    """

    kwargs = _get_kwargs(
        body=body,
        x_request_id=x_request_id,
        x_client_version=x_client_version,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    body: CompleteResetPasswordRequestBody,
    x_request_id: Union[Unset, UUID] = UNSET,
    x_client_version: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, CompleteResetPasswordRequestResponse200, ErrorResponse]]:
    """Complete Password Reset

     Completes a request for password reset.

    Args:
        x_request_id (Union[Unset, UUID]):
        x_client_version (Union[Unset, str]):
        body (CompleteResetPasswordRequestBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, CompleteResetPasswordRequestResponse200, ErrorResponse]
    """

    return sync_detailed(
        client=client,
        body=body,
        x_request_id=x_request_id,
        x_client_version=x_client_version,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: CompleteResetPasswordRequestBody,
    x_request_id: Union[Unset, UUID] = UNSET,
    x_client_version: Union[Unset, str] = UNSET,
) -> Response[Union[Any, CompleteResetPasswordRequestResponse200, ErrorResponse]]:
    """Complete Password Reset

     Completes a request for password reset.

    Args:
        x_request_id (Union[Unset, UUID]):
        x_client_version (Union[Unset, str]):
        body (CompleteResetPasswordRequestBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, CompleteResetPasswordRequestResponse200, ErrorResponse]]
    """

    kwargs = _get_kwargs(
        body=body,
        x_request_id=x_request_id,
        x_client_version=x_client_version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    body: CompleteResetPasswordRequestBody,
    x_request_id: Union[Unset, UUID] = UNSET,
    x_client_version: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, CompleteResetPasswordRequestResponse200, ErrorResponse]]:
    """Complete Password Reset

     Completes a request for password reset.

    Args:
        x_request_id (Union[Unset, UUID]):
        x_client_version (Union[Unset, str]):
        body (CompleteResetPasswordRequestBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, CompleteResetPasswordRequestResponse200, ErrorResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            x_request_id=x_request_id,
            x_client_version=x_client_version,
        )
    ).parsed
