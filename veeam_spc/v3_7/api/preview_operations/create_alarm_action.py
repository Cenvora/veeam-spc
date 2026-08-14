from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.alarm_action_input import AlarmActionInput
from ...models.create_alarm_action_response_201 import CreateAlarmActionResponse201
from ...models.error_response import ErrorResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    alarm_uid: UUID,
    *,
    body: AlarmActionInput,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_request_id, Unset):
        headers["X-Request-id"] = x_request_id

    if not isinstance(x_client_version, Unset):
        headers["X-Client-Version"] = x_client_version

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/alarms/templates/{alarm_uid}/actions".format(
            alarm_uid=quote(str(alarm_uid), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | CreateAlarmActionResponse201 | ErrorResponse:
    if response.status_code == 201:
        response_201 = CreateAlarmActionResponse201.from_dict(response.json())

        return response_201

    if response.status_code == 202:
        response_202 = cast(Any, None)
        return response_202

    response_default = ErrorResponse.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | CreateAlarmActionResponse201 | ErrorResponse]:
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
    body: AlarmActionInput,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Response[Any | CreateAlarmActionResponse201 | ErrorResponse]:
    """Create Alarm Action

     Creates a new action for an alarm template with the specified UID.

    Args:
        alarm_uid (UUID):
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):
        body (AlarmActionInput):  Example: {'type': 'SendCustomEmail', 'condition':
            'ErrorsAndWarnings', 'isEnabled': True, 'value': 'noc@techcompany.local', 'comment':
            'Notify the NOC team about job failures and warnings.'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CreateAlarmActionResponse201 | ErrorResponse]
    """

    kwargs = _get_kwargs(
        alarm_uid=alarm_uid,
        body=body,
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
    body: AlarmActionInput,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Any | CreateAlarmActionResponse201 | ErrorResponse | None:
    """Create Alarm Action

     Creates a new action for an alarm template with the specified UID.

    Args:
        alarm_uid (UUID):
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):
        body (AlarmActionInput):  Example: {'type': 'SendCustomEmail', 'condition':
            'ErrorsAndWarnings', 'isEnabled': True, 'value': 'noc@techcompany.local', 'comment':
            'Notify the NOC team about job failures and warnings.'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CreateAlarmActionResponse201 | ErrorResponse
    """

    return sync_detailed(
        alarm_uid=alarm_uid,
        client=client,
        body=body,
        x_request_id=x_request_id,
        x_client_version=x_client_version,
    ).parsed


async def asyncio_detailed(
    alarm_uid: UUID,
    *,
    client: AuthenticatedClient,
    body: AlarmActionInput,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Response[Any | CreateAlarmActionResponse201 | ErrorResponse]:
    """Create Alarm Action

     Creates a new action for an alarm template with the specified UID.

    Args:
        alarm_uid (UUID):
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):
        body (AlarmActionInput):  Example: {'type': 'SendCustomEmail', 'condition':
            'ErrorsAndWarnings', 'isEnabled': True, 'value': 'noc@techcompany.local', 'comment':
            'Notify the NOC team about job failures and warnings.'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CreateAlarmActionResponse201 | ErrorResponse]
    """

    kwargs = _get_kwargs(
        alarm_uid=alarm_uid,
        body=body,
        x_request_id=x_request_id,
        x_client_version=x_client_version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    alarm_uid: UUID,
    *,
    client: AuthenticatedClient,
    body: AlarmActionInput,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Any | CreateAlarmActionResponse201 | ErrorResponse | None:
    """Create Alarm Action

     Creates a new action for an alarm template with the specified UID.

    Args:
        alarm_uid (UUID):
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):
        body (AlarmActionInput):  Example: {'type': 'SendCustomEmail', 'condition':
            'ErrorsAndWarnings', 'isEnabled': True, 'value': 'noc@techcompany.local', 'comment':
            'Notify the NOC team about job failures and warnings.'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CreateAlarmActionResponse201 | ErrorResponse
    """

    return (
        await asyncio_detailed(
            alarm_uid=alarm_uid,
            client=client,
            body=body,
            x_request_id=x_request_id,
            x_client_version=x_client_version,
        )
    ).parsed
