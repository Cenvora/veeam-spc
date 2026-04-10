from http import HTTPStatus
from typing import Any, Optional, Union, cast
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.smtp_settings_type_0 import SmtpSettingsType0
from ...models.test_notification_smtp_settings_response_200 import TestNotificationSmtpSettingsResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    organization_uid: UUID,
    *,
    body: Union["SmtpSettingsType0", None],
    x_request_id: Union[Unset, UUID] = UNSET,
    x_client_version: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_request_id, Unset):
        headers["X-Request-id"] = x_request_id

    if not isinstance(x_client_version, Unset):
        headers["X-Client-Version"] = x_client_version

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/organizations/{organization_uid}/configuration/notification/smtp/test",
    }

    _kwargs["json"]: Union[None, dict[str, Any]]
    if isinstance(body, SmtpSettingsType0):
        _kwargs["json"] = body.to_dict()
    else:
        _kwargs["json"] = body

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Union[Any, ErrorResponse, TestNotificationSmtpSettingsResponse200]:
    if response.status_code == 200:
        response_200 = TestNotificationSmtpSettingsResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 202:
        response_202 = cast(Any, None)
        return response_202

    response_default = ErrorResponse.from_dict(response.json())

    return response_default


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, ErrorResponse, TestNotificationSmtpSettingsResponse200]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    organization_uid: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
    body: Union["SmtpSettingsType0", None],
    x_request_id: Union[Unset, UUID] = UNSET,
    x_client_version: Union[Unset, str] = UNSET,
) -> Response[Union[Any, ErrorResponse, TestNotificationSmtpSettingsResponse200]]:
    """Test SMTP Server Settings

     Checks provided SMTP server settings. Returns updated and corrected settings and additional
    information on SMTP server.

    Args:
        organization_uid (UUID):
        x_request_id (Union[Unset, UUID]):
        x_client_version (Union[Unset, str]):
        body (Union['SmtpSettingsType0', None]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ErrorResponse, TestNotificationSmtpSettingsResponse200]]
    """

    kwargs = _get_kwargs(
        organization_uid=organization_uid,
        body=body,
        x_request_id=x_request_id,
        x_client_version=x_client_version,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    organization_uid: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
    body: Union["SmtpSettingsType0", None],
    x_request_id: Union[Unset, UUID] = UNSET,
    x_client_version: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, ErrorResponse, TestNotificationSmtpSettingsResponse200]]:
    """Test SMTP Server Settings

     Checks provided SMTP server settings. Returns updated and corrected settings and additional
    information on SMTP server.

    Args:
        organization_uid (UUID):
        x_request_id (Union[Unset, UUID]):
        x_client_version (Union[Unset, str]):
        body (Union['SmtpSettingsType0', None]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ErrorResponse, TestNotificationSmtpSettingsResponse200]
    """

    return sync_detailed(
        organization_uid=organization_uid,
        client=client,
        body=body,
        x_request_id=x_request_id,
        x_client_version=x_client_version,
    ).parsed


async def asyncio_detailed(
    organization_uid: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
    body: Union["SmtpSettingsType0", None],
    x_request_id: Union[Unset, UUID] = UNSET,
    x_client_version: Union[Unset, str] = UNSET,
) -> Response[Union[Any, ErrorResponse, TestNotificationSmtpSettingsResponse200]]:
    """Test SMTP Server Settings

     Checks provided SMTP server settings. Returns updated and corrected settings and additional
    information on SMTP server.

    Args:
        organization_uid (UUID):
        x_request_id (Union[Unset, UUID]):
        x_client_version (Union[Unset, str]):
        body (Union['SmtpSettingsType0', None]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ErrorResponse, TestNotificationSmtpSettingsResponse200]]
    """

    kwargs = _get_kwargs(
        organization_uid=organization_uid,
        body=body,
        x_request_id=x_request_id,
        x_client_version=x_client_version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    organization_uid: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
    body: Union["SmtpSettingsType0", None],
    x_request_id: Union[Unset, UUID] = UNSET,
    x_client_version: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, ErrorResponse, TestNotificationSmtpSettingsResponse200]]:
    """Test SMTP Server Settings

     Checks provided SMTP server settings. Returns updated and corrected settings and additional
    information on SMTP server.

    Args:
        organization_uid (UUID):
        x_request_id (Union[Unset, UUID]):
        x_client_version (Union[Unset, str]):
        body (Union['SmtpSettingsType0', None]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ErrorResponse, TestNotificationSmtpSettingsResponse200]
    """

    return (
        await asyncio_detailed(
            organization_uid=organization_uid,
            client=client,
            body=body,
            x_request_id=x_request_id,
            x_client_version=x_client_version,
        )
    ).parsed
