from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.refresh_token_authenticate_body import RefreshTokenAuthenticateBody
from ...models.refresh_token_authenticate_response_200 import RefreshTokenAuthenticateResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: RefreshTokenAuthenticateBody,
    x_client_version: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_client_version, Unset):
        headers["X-Client-Version"] = x_client_version

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/authentication/refresh",
    }

    _kwargs["files"] = body.to_multipart()

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Union[ErrorResponse, RefreshTokenAuthenticateResponse200]:
    if response.status_code == 200:
        response_200 = RefreshTokenAuthenticateResponse200.from_dict(response.json())

        return response_200

    response_default = ErrorResponse.from_dict(response.json())

    return response_default


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[ErrorResponse, RefreshTokenAuthenticateResponse200]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: RefreshTokenAuthenticateBody,
    x_client_version: Union[Unset, str] = UNSET,
) -> Response[Union[ErrorResponse, RefreshTokenAuthenticateResponse200]]:
    """Obtain New Pair of Tokens

     Returns access and refresh tokens in response to refresh token.
    > Operation is deprecated. We recommend to authorize using the `/token` endpoint.

    Args:
        x_client_version (Union[Unset, str]):
        body (RefreshTokenAuthenticateBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, RefreshTokenAuthenticateResponse200]]
    """

    kwargs = _get_kwargs(
        body=body,
        x_client_version=x_client_version,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    body: RefreshTokenAuthenticateBody,
    x_client_version: Union[Unset, str] = UNSET,
) -> Optional[Union[ErrorResponse, RefreshTokenAuthenticateResponse200]]:
    """Obtain New Pair of Tokens

     Returns access and refresh tokens in response to refresh token.
    > Operation is deprecated. We recommend to authorize using the `/token` endpoint.

    Args:
        x_client_version (Union[Unset, str]):
        body (RefreshTokenAuthenticateBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, RefreshTokenAuthenticateResponse200]
    """

    return sync_detailed(
        client=client,
        body=body,
        x_client_version=x_client_version,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: RefreshTokenAuthenticateBody,
    x_client_version: Union[Unset, str] = UNSET,
) -> Response[Union[ErrorResponse, RefreshTokenAuthenticateResponse200]]:
    """Obtain New Pair of Tokens

     Returns access and refresh tokens in response to refresh token.
    > Operation is deprecated. We recommend to authorize using the `/token` endpoint.

    Args:
        x_client_version (Union[Unset, str]):
        body (RefreshTokenAuthenticateBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, RefreshTokenAuthenticateResponse200]]
    """

    kwargs = _get_kwargs(
        body=body,
        x_client_version=x_client_version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    body: RefreshTokenAuthenticateBody,
    x_client_version: Union[Unset, str] = UNSET,
) -> Optional[Union[ErrorResponse, RefreshTokenAuthenticateResponse200]]:
    """Obtain New Pair of Tokens

     Returns access and refresh tokens in response to refresh token.
    > Operation is deprecated. We recommend to authorize using the `/token` endpoint.

    Args:
        x_client_version (Union[Unset, str]):
        body (RefreshTokenAuthenticateBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, RefreshTokenAuthenticateResponse200]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            x_client_version=x_client_version,
        )
    ).parsed
