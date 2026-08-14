from http import HTTPStatus
from typing import Any, cast
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.discover_objects_for_local_user_rule_response_200 import DiscoverObjectsForLocalUserRuleResponse200
from ...models.discover_objects_for_local_user_rule_type import DiscoverObjectsForLocalUserRuleType
from ...models.error_response import ErrorResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    domain: str,
    type_: DiscoverObjectsForLocalUserRuleType,
    filter_name: str | Unset = UNSET,
    user_name: str,
    password: str,
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

    params["domain"] = domain

    json_type_ = type_.value
    params["type"] = json_type_

    params["filterName"] = filter_name

    params["userName"] = user_name

    params["password"] = password

    params["select"] = select

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/users/serviceProvider/localUserRule/discovery",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | DiscoverObjectsForLocalUserRuleResponse200 | ErrorResponse:
    if response.status_code == 200:
        response_200 = DiscoverObjectsForLocalUserRuleResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 202:
        response_202 = cast(Any, None)
        return response_202

    response_default = ErrorResponse.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | DiscoverObjectsForLocalUserRuleResponse200 | ErrorResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    domain: str,
    type_: DiscoverObjectsForLocalUserRuleType,
    filter_name: str | Unset = UNSET,
    user_name: str,
    password: str,
    select: str | Unset = UNSET,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Response[Any | DiscoverObjectsForLocalUserRuleResponse200 | ErrorResponse]:
    """Discover Domain Users and Groups

     Discovers users and groups in the domain and on the machine on which Veeam Service Provider Console
    is installed.

    Args:
        domain (str):
        type_ (DiscoverObjectsForLocalUserRuleType):
        filter_name (str | Unset):
        user_name (str):
        password (str):
        select (str | Unset):
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DiscoverObjectsForLocalUserRuleResponse200 | ErrorResponse]
    """

    kwargs = _get_kwargs(
        domain=domain,
        type_=type_,
        filter_name=filter_name,
        user_name=user_name,
        password=password,
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
    domain: str,
    type_: DiscoverObjectsForLocalUserRuleType,
    filter_name: str | Unset = UNSET,
    user_name: str,
    password: str,
    select: str | Unset = UNSET,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Any | DiscoverObjectsForLocalUserRuleResponse200 | ErrorResponse | None:
    """Discover Domain Users and Groups

     Discovers users and groups in the domain and on the machine on which Veeam Service Provider Console
    is installed.

    Args:
        domain (str):
        type_ (DiscoverObjectsForLocalUserRuleType):
        filter_name (str | Unset):
        user_name (str):
        password (str):
        select (str | Unset):
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DiscoverObjectsForLocalUserRuleResponse200 | ErrorResponse
    """

    return sync_detailed(
        client=client,
        domain=domain,
        type_=type_,
        filter_name=filter_name,
        user_name=user_name,
        password=password,
        select=select,
        x_request_id=x_request_id,
        x_client_version=x_client_version,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    domain: str,
    type_: DiscoverObjectsForLocalUserRuleType,
    filter_name: str | Unset = UNSET,
    user_name: str,
    password: str,
    select: str | Unset = UNSET,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Response[Any | DiscoverObjectsForLocalUserRuleResponse200 | ErrorResponse]:
    """Discover Domain Users and Groups

     Discovers users and groups in the domain and on the machine on which Veeam Service Provider Console
    is installed.

    Args:
        domain (str):
        type_ (DiscoverObjectsForLocalUserRuleType):
        filter_name (str | Unset):
        user_name (str):
        password (str):
        select (str | Unset):
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DiscoverObjectsForLocalUserRuleResponse200 | ErrorResponse]
    """

    kwargs = _get_kwargs(
        domain=domain,
        type_=type_,
        filter_name=filter_name,
        user_name=user_name,
        password=password,
        select=select,
        x_request_id=x_request_id,
        x_client_version=x_client_version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    domain: str,
    type_: DiscoverObjectsForLocalUserRuleType,
    filter_name: str | Unset = UNSET,
    user_name: str,
    password: str,
    select: str | Unset = UNSET,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Any | DiscoverObjectsForLocalUserRuleResponse200 | ErrorResponse | None:
    """Discover Domain Users and Groups

     Discovers users and groups in the domain and on the machine on which Veeam Service Provider Console
    is installed.

    Args:
        domain (str):
        type_ (DiscoverObjectsForLocalUserRuleType):
        filter_name (str | Unset):
        user_name (str):
        password (str):
        select (str | Unset):
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DiscoverObjectsForLocalUserRuleResponse200 | ErrorResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            domain=domain,
            type_=type_,
            filter_name=filter_name,
            user_name=user_name,
            password=password,
            select=select,
            x_request_id=x_request_id,
            x_client_version=x_client_version,
        )
    ).parsed
