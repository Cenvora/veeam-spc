from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.clone_alarm_response_200 import CloneAlarmResponse200
from ...models.error_response import ErrorResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    alarm_uid: UUID,
    *,
    clone_name: str | Unset = UNSET,
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

    params["cloneName"] = clone_name

    params["select"] = select

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/alarms/templates/{alarm_uid}/clone".format(
            alarm_uid=quote(str(alarm_uid), safe=""),
        ),
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | CloneAlarmResponse200 | ErrorResponse:
    if response.status_code == 200:
        response_200 = CloneAlarmResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 202:
        response_202 = cast(Any, None)
        return response_202

    response_default = ErrorResponse.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | CloneAlarmResponse200 | ErrorResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    alarm_uid: UUID,
    *,
    client: AuthenticatedClient,
    clone_name: str | Unset = UNSET,
    select: str | Unset = UNSET,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Response[Any | CloneAlarmResponse200 | ErrorResponse]:
    """Clone Alarm Template

     Creates a clone of an alarm template with the specified UID.

    Args:
        alarm_uid (UUID):
        clone_name (str | Unset):
        select (str | Unset):
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CloneAlarmResponse200 | ErrorResponse]
    """

    kwargs = _get_kwargs(
        alarm_uid=alarm_uid,
        clone_name=clone_name,
        select=select,
        x_request_id=x_request_id,
        x_client_version=x_client_version,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    alarm_uid: UUID,
    *,
    client: AuthenticatedClient,
    clone_name: str | Unset = UNSET,
    select: str | Unset = UNSET,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Any | CloneAlarmResponse200 | ErrorResponse | None:
    """Clone Alarm Template

     Creates a clone of an alarm template with the specified UID.

    Args:
        alarm_uid (UUID):
        clone_name (str | Unset):
        select (str | Unset):
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CloneAlarmResponse200 | ErrorResponse
    """

    return sync_detailed(
        alarm_uid=alarm_uid,
        client=client,
        clone_name=clone_name,
        select=select,
        x_request_id=x_request_id,
        x_client_version=x_client_version,
    ).parsed


async def asyncio_detailed(
    alarm_uid: UUID,
    *,
    client: AuthenticatedClient,
    clone_name: str | Unset = UNSET,
    select: str | Unset = UNSET,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Response[Any | CloneAlarmResponse200 | ErrorResponse]:
    """Clone Alarm Template

     Creates a clone of an alarm template with the specified UID.

    Args:
        alarm_uid (UUID):
        clone_name (str | Unset):
        select (str | Unset):
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CloneAlarmResponse200 | ErrorResponse]
    """

    kwargs = _get_kwargs(
        alarm_uid=alarm_uid,
        clone_name=clone_name,
        select=select,
        x_request_id=x_request_id,
        x_client_version=x_client_version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    alarm_uid: UUID,
    *,
    client: AuthenticatedClient,
    clone_name: str | Unset = UNSET,
    select: str | Unset = UNSET,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Any | CloneAlarmResponse200 | ErrorResponse | None:
    """Clone Alarm Template

     Creates a clone of an alarm template with the specified UID.

    Args:
        alarm_uid (UUID):
        clone_name (str | Unset):
        select (str | Unset):
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CloneAlarmResponse200 | ErrorResponse
    """

    return (
        await asyncio_detailed(
            alarm_uid=alarm_uid,
            client=client,
            clone_name=clone_name,
            select=select,
            x_request_id=x_request_id,
            x_client_version=x_client_version,
        )
    ).parsed
