from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ...client import AuthenticatedClient, Client
from ...models.asymmetric_algorithm_challenge_response_200 import AsymmetricAlgorithmChallengeResponse200
from ...models.error_response import ErrorResponse
from ...types import UNSET, File, Response, Unset


def _get_kwargs(
    *,
    body: File,
    x_client_version: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_client_version, Unset):
        headers["X-Client-Version"] = x_client_version

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/authentication/asymmetricalgorithm",
    }

    _kwargs["content"] = body.payload

    headers["Content-Type"] = "application/octet-stream"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Union[AsymmetricAlgorithmChallengeResponse200, ErrorResponse]:
    if response.status_code == 200:
        response_200 = AsymmetricAlgorithmChallengeResponse200.from_dict(response.json())

        return response_200

    response_default = ErrorResponse.from_dict(response.json())

    return response_default


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[AsymmetricAlgorithmChallengeResponse200, ErrorResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: File,
    x_client_version: Union[Unset, str] = UNSET,
) -> Response[Union[AsymmetricAlgorithmChallengeResponse200, ErrorResponse]]:
    """Generate Asymmetric Authentication Challenge

     Generates a decryption challenge for the specified public key. The challenge must be decrypted in 30
    seconds.
    > Operation is deprecated. We recommend to authorize using the `/users/{userUid}/logins/apikey` or
    `/token` endpoint.

    Args:
        x_client_version (Union[Unset, str]):
        body (File):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[AsymmetricAlgorithmChallengeResponse200, ErrorResponse]]
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
    body: File,
    x_client_version: Union[Unset, str] = UNSET,
) -> Optional[Union[AsymmetricAlgorithmChallengeResponse200, ErrorResponse]]:
    """Generate Asymmetric Authentication Challenge

     Generates a decryption challenge for the specified public key. The challenge must be decrypted in 30
    seconds.
    > Operation is deprecated. We recommend to authorize using the `/users/{userUid}/logins/apikey` or
    `/token` endpoint.

    Args:
        x_client_version (Union[Unset, str]):
        body (File):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[AsymmetricAlgorithmChallengeResponse200, ErrorResponse]
    """

    return sync_detailed(
        client=client,
        body=body,
        x_client_version=x_client_version,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: File,
    x_client_version: Union[Unset, str] = UNSET,
) -> Response[Union[AsymmetricAlgorithmChallengeResponse200, ErrorResponse]]:
    """Generate Asymmetric Authentication Challenge

     Generates a decryption challenge for the specified public key. The challenge must be decrypted in 30
    seconds.
    > Operation is deprecated. We recommend to authorize using the `/users/{userUid}/logins/apikey` or
    `/token` endpoint.

    Args:
        x_client_version (Union[Unset, str]):
        body (File):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[AsymmetricAlgorithmChallengeResponse200, ErrorResponse]]
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
    body: File,
    x_client_version: Union[Unset, str] = UNSET,
) -> Optional[Union[AsymmetricAlgorithmChallengeResponse200, ErrorResponse]]:
    """Generate Asymmetric Authentication Challenge

     Generates a decryption challenge for the specified public key. The challenge must be decrypted in 30
    seconds.
    > Operation is deprecated. We recommend to authorize using the `/users/{userUid}/logins/apikey` or
    `/token` endpoint.

    Args:
        x_client_version (Union[Unset, str]):
        body (File):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[AsymmetricAlgorithmChallengeResponse200, ErrorResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            x_client_version=x_client_version,
        )
    ).parsed
