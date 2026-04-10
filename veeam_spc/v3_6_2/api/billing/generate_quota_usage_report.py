import datetime
from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.empty_response import EmptyResponse
from ...models.error_response import ErrorResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    company_uid: UUID,
    *,
    from_date: datetime.date,
    to_date: datetime.date,
    send_report: bool | Unset = False,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_request_id, Unset):
        headers["X-Request-id"] = x_request_id

    if not isinstance(x_client_version, Unset):
        headers["X-Client-Version"] = x_client_version

    params: dict[str, Any] = {}

    json_from_date = from_date.isoformat()
    params["fromDate"] = json_from_date

    json_to_date = to_date.isoformat()
    params["toDate"] = json_to_date

    params["sendReport"] = send_report

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/organizations/companies/{company_uid}/billing/generateQuotaUsageReport".format(
            company_uid=quote(str(company_uid), safe=""),
        ),
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | EmptyResponse | ErrorResponse:
    if response.status_code == 200:
        response_200 = EmptyResponse.from_dict(response.json())

        return response_200

    if response.status_code == 202:
        response_202 = cast(Any, None)
        return response_202

    response_default = ErrorResponse.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | EmptyResponse | ErrorResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    company_uid: UUID,
    *,
    client: AuthenticatedClient,
    from_date: datetime.date,
    to_date: datetime.date,
    send_report: bool | Unset = False,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Response[Any | EmptyResponse | ErrorResponse]:
    """Generate Quota Usage Report for Company

     Initiates quota usage report for a company with the specified UID.

    Args:
        company_uid (UUID):
        from_date (datetime.date):
        to_date (datetime.date):
        send_report (bool | Unset):  Default: False.
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | EmptyResponse | ErrorResponse]
    """

    kwargs = _get_kwargs(
        company_uid=company_uid,
        from_date=from_date,
        to_date=to_date,
        send_report=send_report,
        x_request_id=x_request_id,
        x_client_version=x_client_version,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    company_uid: UUID,
    *,
    client: AuthenticatedClient,
    from_date: datetime.date,
    to_date: datetime.date,
    send_report: bool | Unset = False,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Any | EmptyResponse | ErrorResponse | None:
    """Generate Quota Usage Report for Company

     Initiates quota usage report for a company with the specified UID.

    Args:
        company_uid (UUID):
        from_date (datetime.date):
        to_date (datetime.date):
        send_report (bool | Unset):  Default: False.
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | EmptyResponse | ErrorResponse
    """

    return sync_detailed(
        company_uid=company_uid,
        client=client,
        from_date=from_date,
        to_date=to_date,
        send_report=send_report,
        x_request_id=x_request_id,
        x_client_version=x_client_version,
    ).parsed


async def asyncio_detailed(
    company_uid: UUID,
    *,
    client: AuthenticatedClient,
    from_date: datetime.date,
    to_date: datetime.date,
    send_report: bool | Unset = False,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Response[Any | EmptyResponse | ErrorResponse]:
    """Generate Quota Usage Report for Company

     Initiates quota usage report for a company with the specified UID.

    Args:
        company_uid (UUID):
        from_date (datetime.date):
        to_date (datetime.date):
        send_report (bool | Unset):  Default: False.
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | EmptyResponse | ErrorResponse]
    """

    kwargs = _get_kwargs(
        company_uid=company_uid,
        from_date=from_date,
        to_date=to_date,
        send_report=send_report,
        x_request_id=x_request_id,
        x_client_version=x_client_version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    company_uid: UUID,
    *,
    client: AuthenticatedClient,
    from_date: datetime.date,
    to_date: datetime.date,
    send_report: bool | Unset = False,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Any | EmptyResponse | ErrorResponse | None:
    """Generate Quota Usage Report for Company

     Initiates quota usage report for a company with the specified UID.

    Args:
        company_uid (UUID):
        from_date (datetime.date):
        to_date (datetime.date):
        send_report (bool | Unset):  Default: False.
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | EmptyResponse | ErrorResponse
    """

    return (
        await asyncio_detailed(
            company_uid=company_uid,
            client=client,
            from_date=from_date,
            to_date=to_date,
            send_report=send_report,
            x_request_id=x_request_id,
            x_client_version=x_client_version,
        )
    ).parsed
