from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.generate_new_rsa_key_pair_response_200 import GenerateNewRsaKeyPairResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    key_size: Union[Unset, int] = UNSET,
    x_client_version: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_client_version, Unset):
        headers["X-Client-Version"] = x_client_version

    params: dict[str, Any] = {}

    params["keySize"] = key_size

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/authentication/keys/rsa",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Union[ErrorResponse, GenerateNewRsaKeyPairResponse200]:
    if response.status_code == 200:
        response_200 = GenerateNewRsaKeyPairResponse200.from_dict(response.json())

        return response_200

    response_default = ErrorResponse.from_dict(response.json())

    return response_default


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[ErrorResponse, GenerateNewRsaKeyPairResponse200]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    key_size: Union[Unset, int] = UNSET,
    x_client_version: Union[Unset, str] = UNSET,
) -> Response[Union[ErrorResponse, GenerateNewRsaKeyPairResponse200]]:
    """Obtain RSA Keys

     Issues an RSA key pair.
    > You can specify the key size if needed.

    Args:
        key_size (Union[Unset, int]):
        x_client_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, GenerateNewRsaKeyPairResponse200]]
    """

    kwargs = _get_kwargs(
        key_size=key_size,
        x_client_version=x_client_version,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    key_size: Union[Unset, int] = UNSET,
    x_client_version: Union[Unset, str] = UNSET,
) -> Optional[Union[ErrorResponse, GenerateNewRsaKeyPairResponse200]]:
    """Obtain RSA Keys

     Issues an RSA key pair.
    > You can specify the key size if needed.

    Args:
        key_size (Union[Unset, int]):
        x_client_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, GenerateNewRsaKeyPairResponse200]
    """

    return sync_detailed(
        client=client,
        key_size=key_size,
        x_client_version=x_client_version,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    key_size: Union[Unset, int] = UNSET,
    x_client_version: Union[Unset, str] = UNSET,
) -> Response[Union[ErrorResponse, GenerateNewRsaKeyPairResponse200]]:
    """Obtain RSA Keys

     Issues an RSA key pair.
    > You can specify the key size if needed.

    Args:
        key_size (Union[Unset, int]):
        x_client_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, GenerateNewRsaKeyPairResponse200]]
    """

    kwargs = _get_kwargs(
        key_size=key_size,
        x_client_version=x_client_version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    key_size: Union[Unset, int] = UNSET,
    x_client_version: Union[Unset, str] = UNSET,
) -> Optional[Union[ErrorResponse, GenerateNewRsaKeyPairResponse200]]:
    """Obtain RSA Keys

     Issues an RSA key pair.
    > You can specify the key size if needed.

    Args:
        key_size (Union[Unset, int]):
        x_client_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, GenerateNewRsaKeyPairResponse200]
    """

    return (
        await asyncio_detailed(
            client=client,
            key_size=key_size,
            x_client_version=x_client_version,
        )
    ).parsed
