from http import HTTPStatus
from typing import Any, cast
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
        "method": "put",
        "url": "/users/resetpassword",
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | CompleteResetPasswordRequestResponse200 | ErrorResponse:
    if response.status_code == 200:
        response_200 = CompleteResetPasswordRequestResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 202:
        response_202 = cast(Any, None)
        return response_202

    response_default = ErrorResponse.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | CompleteResetPasswordRequestResponse200 | ErrorResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CompleteResetPasswordRequestBody,
    select: str | Unset = UNSET,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Response[Any | CompleteResetPasswordRequestResponse200 | ErrorResponse]:
    """Complete Password Reset

     Completes a request for password reset.

    Args:
        select (str | Unset):
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):
        body (CompleteResetPasswordRequestBody):  Example: {'code': 'E2DF8F84479511910E4469B624C72
            B359C84AC6AE340D7D225BC8FC237BB2E491C217849C5B45F23D0FD6D53BD1B75F37704D908D647D25ADE59147
            60CEED5256C889432323F9B382826B650969C344C9ACE7E50F11A04F4256F97DA4A881F1EC2E53BB04D773BCD3
            B4A1935B958D253732CF3C493D868B24EBC0C17A9F4DB58DE07F91952D80E50', 'newPassword':
            'password'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CompleteResetPasswordRequestResponse200 | ErrorResponse]
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
    client: AuthenticatedClient | Client,
    body: CompleteResetPasswordRequestBody,
    select: str | Unset = UNSET,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Any | CompleteResetPasswordRequestResponse200 | ErrorResponse | None:
    """Complete Password Reset

     Completes a request for password reset.

    Args:
        select (str | Unset):
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):
        body (CompleteResetPasswordRequestBody):  Example: {'code': 'E2DF8F84479511910E4469B624C72
            B359C84AC6AE340D7D225BC8FC237BB2E491C217849C5B45F23D0FD6D53BD1B75F37704D908D647D25ADE59147
            60CEED5256C889432323F9B382826B650969C344C9ACE7E50F11A04F4256F97DA4A881F1EC2E53BB04D773BCD3
            B4A1935B958D253732CF3C493D868B24EBC0C17A9F4DB58DE07F91952D80E50', 'newPassword':
            'password'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CompleteResetPasswordRequestResponse200 | ErrorResponse
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
    client: AuthenticatedClient | Client,
    body: CompleteResetPasswordRequestBody,
    select: str | Unset = UNSET,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Response[Any | CompleteResetPasswordRequestResponse200 | ErrorResponse]:
    """Complete Password Reset

     Completes a request for password reset.

    Args:
        select (str | Unset):
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):
        body (CompleteResetPasswordRequestBody):  Example: {'code': 'E2DF8F84479511910E4469B624C72
            B359C84AC6AE340D7D225BC8FC237BB2E491C217849C5B45F23D0FD6D53BD1B75F37704D908D647D25ADE59147
            60CEED5256C889432323F9B382826B650969C344C9ACE7E50F11A04F4256F97DA4A881F1EC2E53BB04D773BCD3
            B4A1935B958D253732CF3C493D868B24EBC0C17A9F4DB58DE07F91952D80E50', 'newPassword':
            'password'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CompleteResetPasswordRequestResponse200 | ErrorResponse]
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
    client: AuthenticatedClient | Client,
    body: CompleteResetPasswordRequestBody,
    select: str | Unset = UNSET,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Any | CompleteResetPasswordRequestResponse200 | ErrorResponse | None:
    """Complete Password Reset

     Completes a request for password reset.

    Args:
        select (str | Unset):
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):
        body (CompleteResetPasswordRequestBody):  Example: {'code': 'E2DF8F84479511910E4469B624C72
            B359C84AC6AE340D7D225BC8FC237BB2E491C217849C5B45F23D0FD6D53BD1B75F37704D908D647D25ADE59147
            60CEED5256C889432323F9B382826B650969C344C9ACE7E50F11A04F4256F97DA4A881F1EC2E53BB04D773BCD3
            B4A1935B958D253732CF3C493D868B24EBC0C17A9F4DB58DE07F91952D80E50', 'newPassword':
            'password'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CompleteResetPasswordRequestResponse200 | ErrorResponse
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
