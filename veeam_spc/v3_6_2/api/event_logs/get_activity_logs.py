import datetime
from http import HTTPStatus
from typing import Any, cast
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
    from_: datetime.datetime | Unset = UNSET,
    to: datetime.datetime | Unset = UNSET,
    organization_uid: UUID | Unset = UNSET,
    user_uid: UUID | Unset = UNSET,
    activity_log_kind: ActivityLogKind | Unset = UNSET,
    date_sorting_direction: GetActivityLogsDateSortingDirection
    | Unset = GetActivityLogsDateSortingDirection.DESCENDING,
    limit: int | Unset = 100,
    offset: int | Unset = 0,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_request_id, Unset):
        headers["X-Request-id"] = x_request_id

    if not isinstance(x_client_version, Unset):
        headers["X-Client-Version"] = x_client_version

    params: dict[str, Any] = {}

    json_from_: str | Unset = UNSET
    if not isinstance(from_, Unset):
        json_from_ = from_.isoformat()
    params["from"] = json_from_

    json_to: str | Unset = UNSET
    if not isinstance(to, Unset):
        json_to = to.isoformat()
    params["to"] = json_to

    json_organization_uid: str | Unset = UNSET
    if not isinstance(organization_uid, Unset):
        json_organization_uid = str(organization_uid)
    params["organizationUid"] = json_organization_uid

    json_user_uid: str | Unset = UNSET
    if not isinstance(user_uid, Unset):
        json_user_uid = str(user_uid)
    params["userUid"] = json_user_uid

    json_activity_log_kind: str | Unset = UNSET
    if not isinstance(activity_log_kind, Unset):
        json_activity_log_kind = activity_log_kind.value

    params["activityLogKind"] = json_activity_log_kind

    json_date_sorting_direction: str | Unset = UNSET
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
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | ErrorResponse | GetActivityLogsResponse200:
    if response.status_code == 200:
        response_200 = GetActivityLogsResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 202:
        response_202 = cast(Any, None)
        return response_202

    response_default = ErrorResponse.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | ErrorResponse | GetActivityLogsResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    from_: datetime.datetime | Unset = UNSET,
    to: datetime.datetime | Unset = UNSET,
    organization_uid: UUID | Unset = UNSET,
    user_uid: UUID | Unset = UNSET,
    activity_log_kind: ActivityLogKind | Unset = UNSET,
    date_sorting_direction: GetActivityLogsDateSortingDirection
    | Unset = GetActivityLogsDateSortingDirection.DESCENDING,
    limit: int | Unset = 100,
    offset: int | Unset = 0,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Response[Any | ErrorResponse | GetActivityLogsResponse200]:
    """Get All Activity Log Records

     Returns a collection resource representation of all activity log records.

    Args:
        from_ (datetime.datetime | Unset):
        to (datetime.datetime | Unset):
        organization_uid (UUID | Unset):
        user_uid (UUID | Unset):
        activity_log_kind (ActivityLogKind | Unset): Type of an activity.
        date_sorting_direction (GetActivityLogsDateSortingDirection | Unset):  Default:
            GetActivityLogsDateSortingDirection.DESCENDING.
        limit (int | Unset):  Default: 100.
        offset (int | Unset):  Default: 0.
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ErrorResponse | GetActivityLogsResponse200]
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
    client: AuthenticatedClient,
    from_: datetime.datetime | Unset = UNSET,
    to: datetime.datetime | Unset = UNSET,
    organization_uid: UUID | Unset = UNSET,
    user_uid: UUID | Unset = UNSET,
    activity_log_kind: ActivityLogKind | Unset = UNSET,
    date_sorting_direction: GetActivityLogsDateSortingDirection
    | Unset = GetActivityLogsDateSortingDirection.DESCENDING,
    limit: int | Unset = 100,
    offset: int | Unset = 0,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Any | ErrorResponse | GetActivityLogsResponse200 | None:
    """Get All Activity Log Records

     Returns a collection resource representation of all activity log records.

    Args:
        from_ (datetime.datetime | Unset):
        to (datetime.datetime | Unset):
        organization_uid (UUID | Unset):
        user_uid (UUID | Unset):
        activity_log_kind (ActivityLogKind | Unset): Type of an activity.
        date_sorting_direction (GetActivityLogsDateSortingDirection | Unset):  Default:
            GetActivityLogsDateSortingDirection.DESCENDING.
        limit (int | Unset):  Default: 100.
        offset (int | Unset):  Default: 0.
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ErrorResponse | GetActivityLogsResponse200
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
    client: AuthenticatedClient,
    from_: datetime.datetime | Unset = UNSET,
    to: datetime.datetime | Unset = UNSET,
    organization_uid: UUID | Unset = UNSET,
    user_uid: UUID | Unset = UNSET,
    activity_log_kind: ActivityLogKind | Unset = UNSET,
    date_sorting_direction: GetActivityLogsDateSortingDirection
    | Unset = GetActivityLogsDateSortingDirection.DESCENDING,
    limit: int | Unset = 100,
    offset: int | Unset = 0,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Response[Any | ErrorResponse | GetActivityLogsResponse200]:
    """Get All Activity Log Records

     Returns a collection resource representation of all activity log records.

    Args:
        from_ (datetime.datetime | Unset):
        to (datetime.datetime | Unset):
        organization_uid (UUID | Unset):
        user_uid (UUID | Unset):
        activity_log_kind (ActivityLogKind | Unset): Type of an activity.
        date_sorting_direction (GetActivityLogsDateSortingDirection | Unset):  Default:
            GetActivityLogsDateSortingDirection.DESCENDING.
        limit (int | Unset):  Default: 100.
        offset (int | Unset):  Default: 0.
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ErrorResponse | GetActivityLogsResponse200]
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
    client: AuthenticatedClient,
    from_: datetime.datetime | Unset = UNSET,
    to: datetime.datetime | Unset = UNSET,
    organization_uid: UUID | Unset = UNSET,
    user_uid: UUID | Unset = UNSET,
    activity_log_kind: ActivityLogKind | Unset = UNSET,
    date_sorting_direction: GetActivityLogsDateSortingDirection
    | Unset = GetActivityLogsDateSortingDirection.DESCENDING,
    limit: int | Unset = 100,
    offset: int | Unset = 0,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Any | ErrorResponse | GetActivityLogsResponse200 | None:
    """Get All Activity Log Records

     Returns a collection resource representation of all activity log records.

    Args:
        from_ (datetime.datetime | Unset):
        to (datetime.datetime | Unset):
        organization_uid (UUID | Unset):
        user_uid (UUID | Unset):
        activity_log_kind (ActivityLogKind | Unset): Type of an activity.
        date_sorting_direction (GetActivityLogsDateSortingDirection | Unset):  Default:
            GetActivityLogsDateSortingDirection.DESCENDING.
        limit (int | Unset):  Default: 100.
        offset (int | Unset):  Default: 0.
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ErrorResponse | GetActivityLogsResponse200
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
