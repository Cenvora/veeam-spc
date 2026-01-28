from http import HTTPStatus
from typing import Any, Optional, Union, cast
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.delete_user_login_response_200 import DeleteUserLoginResponse200
from ...models.error_response import ErrorResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    user_uid: UUID,
    user_login_id: int,
    *,
    x_request_id: Union[Unset, UUID] = UNSET,
    x_client_version: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_request_id, Unset):
        headers["X-Request-id"] = x_request_id

    if not isinstance(x_client_version, Unset):
        headers["X-Client-Version"] = x_client_version

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": f"/users/{user_uid}/logins/{user_login_id}",
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Union[Any, DeleteUserLoginResponse200, ErrorResponse]:
    if response.status_code == 200:
        response_200 = DeleteUserLoginResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 202:
        response_202 = cast(Any, None)
        return response_202

    response_default = ErrorResponse.from_dict(response.json())

    return response_default


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, DeleteUserLoginResponse200, ErrorResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    user_uid: UUID,
    user_login_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    x_request_id: Union[Unset, UUID] = UNSET,
    x_client_version: Union[Unset, str] = UNSET,
) -> Response[Union[Any, DeleteUserLoginResponse200, ErrorResponse]]:
    """Delete User Identity

     Deletes a user identity with the specified ID.

    Args:
        user_uid (UUID):
        user_login_id (int):
        x_request_id (Union[Unset, UUID]):
        x_client_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, DeleteUserLoginResponse200, ErrorResponse]]
    """

    kwargs = _get_kwargs(
        user_uid=user_uid,
        user_login_id=user_login_id,
        x_request_id=x_request_id,
        x_client_version=x_client_version,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    user_uid: UUID,
    user_login_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    x_request_id: Union[Unset, UUID] = UNSET,
    x_client_version: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, DeleteUserLoginResponse200, ErrorResponse]]:
    """Delete User Identity

     Deletes a user identity with the specified ID.

    Args:
        user_uid (UUID):
        user_login_id (int):
        x_request_id (Union[Unset, UUID]):
        x_client_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, DeleteUserLoginResponse200, ErrorResponse]
    """

    return sync_detailed(
        user_uid=user_uid,
        user_login_id=user_login_id,
        client=client,
        x_request_id=x_request_id,
        x_client_version=x_client_version,
    ).parsed


async def asyncio_detailed(
    user_uid: UUID,
    user_login_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    x_request_id: Union[Unset, UUID] = UNSET,
    x_client_version: Union[Unset, str] = UNSET,
) -> Response[Union[Any, DeleteUserLoginResponse200, ErrorResponse]]:
    """Delete User Identity

     Deletes a user identity with the specified ID.

    Args:
        user_uid (UUID):
        user_login_id (int):
        x_request_id (Union[Unset, UUID]):
        x_client_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, DeleteUserLoginResponse200, ErrorResponse]]
    """

    kwargs = _get_kwargs(
        user_uid=user_uid,
        user_login_id=user_login_id,
        x_request_id=x_request_id,
        x_client_version=x_client_version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    user_uid: UUID,
    user_login_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    x_request_id: Union[Unset, UUID] = UNSET,
    x_client_version: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, DeleteUserLoginResponse200, ErrorResponse]]:
    """Delete User Identity

     Deletes a user identity with the specified ID.

    Args:
        user_uid (UUID):
        user_login_id (int):
        x_request_id (Union[Unset, UUID]):
        x_client_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, DeleteUserLoginResponse200, ErrorResponse]
    """

    return (
        await asyncio_detailed(
            user_uid=user_uid,
            user_login_id=user_login_id,
            client=client,
            x_request_id=x_request_id,
            x_client_version=x_client_version,
        )
    ).parsed
