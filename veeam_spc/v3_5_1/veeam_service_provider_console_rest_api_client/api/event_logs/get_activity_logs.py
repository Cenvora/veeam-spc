import datetime
from http import HTTPStatus
from typing import Any, Optional, Union, cast
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.activity_log_kind import ActivityLogKind
from ...models.error_response import ErrorResponse
from ...models.get_activity_logs_date_sorting_direction import GetActivityLogsDateSortingDirection
from ...models.get_activity_logs_response_200 import GetActivityLogsResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    from_: Union[Unset, datetime.datetime] = UNSET,
    to: Union[Unset, datetime.datetime] = UNSET,
    organization_uid: Union[Unset, UUID] = UNSET,
    user_uid: Union[Unset, UUID] = UNSET,
    activity_log_kind: Union[Unset, ActivityLogKind] = UNSET,
    date_sorting_direction: Union[
        Unset, GetActivityLogsDateSortingDirection
    ] = GetActivityLogsDateSortingDirection.DESCENDING,
    limit: Union[Unset, int] = 100,
    offset: Union[Unset, int] = 0,
    x_request_id: Union[Unset, UUID] = UNSET,
    x_client_version: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_request_id, Unset):
        headers["X-Request-id"] = x_request_id

    if not isinstance(x_client_version, Unset):
        headers["X-Client-Version"] = x_client_version

    params: dict[str, Any] = {}

    json_from_: Union[Unset, str] = UNSET
    if not isinstance(from_, Unset):
        json_from_ = from_.isoformat()
    params["from"] = json_from_

    json_to: Union[Unset, str] = UNSET
    if not isinstance(to, Unset):
        json_to = to.isoformat()
    params["to"] = json_to

    json_organization_uid: Union[Unset, str] = UNSET
    if not isinstance(organization_uid, Unset):
        json_organization_uid = str(organization_uid)
    params["organizationUid"] = json_organization_uid

    json_user_uid: Union[Unset, str] = UNSET
    if not isinstance(user_uid, Unset):
        json_user_uid = str(user_uid)
    params["userUid"] = json_user_uid

    json_activity_log_kind: Union[Unset, str] = UNSET
    if not isinstance(activity_log_kind, Unset):
        json_activity_log_kind = activity_log_kind.value

    params["activityLogKind"] = json_activity_log_kind

    json_date_sorting_direction: Union[Unset, str] = UNSET
    if not isinstance(date_sorting_direction, Unset):
        json_date_sorting_direction = date_sorting_direction.value

    params["dateSortingDirection"] = json_date_sorting_direction

    params["limit"] = limit

    params["offset"] = offset

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/eventLogs/activityLogs",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Union[Any, ErrorResponse, GetActivityLogsResponse200]:
    if response.status_code == 200:
        response_200 = GetActivityLogsResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 202:
        response_202 = cast(Any, None)
        return response_202

    response_default = ErrorResponse.from_dict(response.json())

    return response_default


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, ErrorResponse, GetActivityLogsResponse200]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    from_: Union[Unset, datetime.datetime] = UNSET,
    to: Union[Unset, datetime.datetime] = UNSET,
    organization_uid: Union[Unset, UUID] = UNSET,
    user_uid: Union[Unset, UUID] = UNSET,
    activity_log_kind: Union[Unset, ActivityLogKind] = UNSET,
    date_sorting_direction: Union[
        Unset, GetActivityLogsDateSortingDirection
    ] = GetActivityLogsDateSortingDirection.DESCENDING,
    limit: Union[Unset, int] = 100,
    offset: Union[Unset, int] = 0,
    x_request_id: Union[Unset, UUID] = UNSET,
    x_client_version: Union[Unset, str] = UNSET,
) -> Response[Union[Any, ErrorResponse, GetActivityLogsResponse200]]:
    """Get All Activity Log Records

     Returns a collection resource representation of all activity log records.

    Args:
        from_ (Union[Unset, datetime.datetime]):
        to (Union[Unset, datetime.datetime]):
        organization_uid (Union[Unset, UUID]):
        user_uid (Union[Unset, UUID]):
        activity_log_kind (Union[Unset, ActivityLogKind]): Type of an activity.
        date_sorting_direction (Union[Unset, GetActivityLogsDateSortingDirection]):  Default:
            GetActivityLogsDateSortingDirection.DESCENDING.
        limit (Union[Unset, int]):  Default: 100.
        offset (Union[Unset, int]):  Default: 0.
        x_request_id (Union[Unset, UUID]):
        x_client_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ErrorResponse, GetActivityLogsResponse200]]
    """

    kwargs = _get_kwargs(
        from_=from_,
        to=to,
        organization_uid=organization_uid,
        user_uid=user_uid,
        activity_log_kind=activity_log_kind,
        date_sorting_direction=date_sorting_direction,
        limit=limit,
        offset=offset,
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
    from_: Union[Unset, datetime.datetime] = UNSET,
    to: Union[Unset, datetime.datetime] = UNSET,
    organization_uid: Union[Unset, UUID] = UNSET,
    user_uid: Union[Unset, UUID] = UNSET,
    activity_log_kind: Union[Unset, ActivityLogKind] = UNSET,
    date_sorting_direction: Union[
        Unset, GetActivityLogsDateSortingDirection
    ] = GetActivityLogsDateSortingDirection.DESCENDING,
    limit: Union[Unset, int] = 100,
    offset: Union[Unset, int] = 0,
    x_request_id: Union[Unset, UUID] = UNSET,
    x_client_version: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, ErrorResponse, GetActivityLogsResponse200]]:
    """Get All Activity Log Records

     Returns a collection resource representation of all activity log records.

    Args:
        from_ (Union[Unset, datetime.datetime]):
        to (Union[Unset, datetime.datetime]):
        organization_uid (Union[Unset, UUID]):
        user_uid (Union[Unset, UUID]):
        activity_log_kind (Union[Unset, ActivityLogKind]): Type of an activity.
        date_sorting_direction (Union[Unset, GetActivityLogsDateSortingDirection]):  Default:
            GetActivityLogsDateSortingDirection.DESCENDING.
        limit (Union[Unset, int]):  Default: 100.
        offset (Union[Unset, int]):  Default: 0.
        x_request_id (Union[Unset, UUID]):
        x_client_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ErrorResponse, GetActivityLogsResponse200]
    """

    return sync_detailed(
        client=client,
        from_=from_,
        to=to,
        organization_uid=organization_uid,
        user_uid=user_uid,
        activity_log_kind=activity_log_kind,
        date_sorting_direction=date_sorting_direction,
        limit=limit,
        offset=offset,
        x_request_id=x_request_id,
        x_client_version=x_client_version,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    from_: Union[Unset, datetime.datetime] = UNSET,
    to: Union[Unset, datetime.datetime] = UNSET,
    organization_uid: Union[Unset, UUID] = UNSET,
    user_uid: Union[Unset, UUID] = UNSET,
    activity_log_kind: Union[Unset, ActivityLogKind] = UNSET,
    date_sorting_direction: Union[
        Unset, GetActivityLogsDateSortingDirection
    ] = GetActivityLogsDateSortingDirection.DESCENDING,
    limit: Union[Unset, int] = 100,
    offset: Union[Unset, int] = 0,
    x_request_id: Union[Unset, UUID] = UNSET,
    x_client_version: Union[Unset, str] = UNSET,
) -> Response[Union[Any, ErrorResponse, GetActivityLogsResponse200]]:
    """Get All Activity Log Records

     Returns a collection resource representation of all activity log records.

    Args:
        from_ (Union[Unset, datetime.datetime]):
        to (Union[Unset, datetime.datetime]):
        organization_uid (Union[Unset, UUID]):
        user_uid (Union[Unset, UUID]):
        activity_log_kind (Union[Unset, ActivityLogKind]): Type of an activity.
        date_sorting_direction (Union[Unset, GetActivityLogsDateSortingDirection]):  Default:
            GetActivityLogsDateSortingDirection.DESCENDING.
        limit (Union[Unset, int]):  Default: 100.
        offset (Union[Unset, int]):  Default: 0.
        x_request_id (Union[Unset, UUID]):
        x_client_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ErrorResponse, GetActivityLogsResponse200]]
    """

    kwargs = _get_kwargs(
        from_=from_,
        to=to,
        organization_uid=organization_uid,
        user_uid=user_uid,
        activity_log_kind=activity_log_kind,
        date_sorting_direction=date_sorting_direction,
        limit=limit,
        offset=offset,
        x_request_id=x_request_id,
        x_client_version=x_client_version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    from_: Union[Unset, datetime.datetime] = UNSET,
    to: Union[Unset, datetime.datetime] = UNSET,
    organization_uid: Union[Unset, UUID] = UNSET,
    user_uid: Union[Unset, UUID] = UNSET,
    activity_log_kind: Union[Unset, ActivityLogKind] = UNSET,
    date_sorting_direction: Union[
        Unset, GetActivityLogsDateSortingDirection
    ] = GetActivityLogsDateSortingDirection.DESCENDING,
    limit: Union[Unset, int] = 100,
    offset: Union[Unset, int] = 0,
    x_request_id: Union[Unset, UUID] = UNSET,
    x_client_version: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, ErrorResponse, GetActivityLogsResponse200]]:
    """Get All Activity Log Records

     Returns a collection resource representation of all activity log records.

    Args:
        from_ (Union[Unset, datetime.datetime]):
        to (Union[Unset, datetime.datetime]):
        organization_uid (Union[Unset, UUID]):
        user_uid (Union[Unset, UUID]):
        activity_log_kind (Union[Unset, ActivityLogKind]): Type of an activity.
        date_sorting_direction (Union[Unset, GetActivityLogsDateSortingDirection]):  Default:
            GetActivityLogsDateSortingDirection.DESCENDING.
        limit (Union[Unset, int]):  Default: 100.
        offset (Union[Unset, int]):  Default: 0.
        x_request_id (Union[Unset, UUID]):
        x_client_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ErrorResponse, GetActivityLogsResponse200]
    """

    return (
        await asyncio_detailed(
            client=client,
            from_=from_,
            to=to,
            organization_uid=organization_uid,
            user_uid=user_uid,
            activity_log_kind=activity_log_kind,
            date_sorting_direction=date_sorting_direction,
            limit=limit,
            offset=offset,
            x_request_id=x_request_id,
            x_client_version=x_client_version,
        )
    ).parsed
