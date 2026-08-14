from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.create_vb_365_microsoft_365_organization_response_200 import (
    CreateVb365Microsoft365OrganizationResponse200,
)
from ...models.error_response import ErrorResponse
from ...models.vb_365_microsoft_365_organization import Vb365Microsoft365Organization
from ...types import UNSET, Response, Unset


def _get_kwargs(
    vb_365_server_uid: UUID,
    *,
    body: Vb365Microsoft365Organization,
    company_uid: UUID | Unset = UNSET,
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

    json_company_uid: str | Unset = UNSET
    if not isinstance(company_uid, Unset):
        json_company_uid = str(company_uid)
    params["companyUid"] = json_company_uid

    params["select"] = select

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/infrastructure/vb365Servers/{vb_365_server_uid}/organizations/Microsoft365".format(
            vb_365_server_uid=quote(str(vb_365_server_uid), safe=""),
        ),
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | CreateVb365Microsoft365OrganizationResponse200 | ErrorResponse:
    if response.status_code == 200:
        response_200 = CreateVb365Microsoft365OrganizationResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 202:
        response_202 = cast(Any, None)
        return response_202

    response_default = ErrorResponse.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | CreateVb365Microsoft365OrganizationResponse200 | ErrorResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    vb_365_server_uid: UUID,
    *,
    client: AuthenticatedClient,
    body: Vb365Microsoft365Organization,
    company_uid: UUID | Unset = UNSET,
    select: str | Unset = UNSET,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Response[Any | CreateVb365Microsoft365OrganizationResponse200 | ErrorResponse]:
    """Create Microsoft 365 Organization

     Creates a new Microsoft 365 organization on a Veeam Backup for Microsoft 365 server with the
    specified UID.

    Args:
        vb_365_server_uid (UUID):
        company_uid (UUID | Unset):
        select (str | Unset):
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):
        body (Vb365Microsoft365Organization):  Example: {'isTeamsOnline': True,
            'isTeamsChatsOnline': False, 'exchangeAndSharePointOnlineConnectionSettings':
            {'modernAppOnlyAuthenticationSettings': {'configureApplication': False, 'userCode': None,
            'newApplicationName': None, 'applicationId': 'ae61e533-82c7-4cb6-a030-78ae589cf49d',
            'applicationCertificate': 'MIIEoQIBAAKCAQBJ4W/TVQeIynO0BL/f/lc65mUzZmput1JCZsMLcjQB9eAteBV
            l5NRN4O5jUrWqXwk1IX17qtDiu3L8O07e0HlL+nHkRYeUDaztVbyhtvKc+YwNwZTQP8IvnWBpgrd2uJw167I7iQ5nu
            N2O7QL/8idBiKhgsOKz9frPMSp/QIXA3MQoi+Yp8TiyDvGps+iMn1KpLgkHehlXUFmuZvi27T6wSZGh97rHekpIj9b
            SirZFcG+7qupx8HFE4wNdhvxcvbmNkfMaJTmmi3YzGKYESwNyvwAIuohq1MoeQmNf1Q50NO04GOOPY+66uykOQkDkT
            a8/Vu90O6cux6/Ntyt04hndAgMBAAECggEABtA/m+HPnBHvsb5uY531NX1h/+eGEUfe0jjf7AJQQY4HaqoUbx03Zyd
            DVO2fy2KQWtIH3IvYT9CxvglKMMpRJWynbEHtSv4n4ItzpgZVQZzSCcK8kqgOpI2DArgHa2+DGIXwHgV5yp8F79Rz3
            l7at/R+csxdW/NnegwyuyGcNDkOjp8//HcrHQXPjljF5mwh4UZCFUvscKVjQbsOpiMvGeGN3z0/ZfKHi2egEA4+t1N
            LJykDiovNamtxE2xDkU8TXwn9STI8owzmxGtAA4HXDMuUQ0UXqxN0ED3WLJeqEKa0vuQ34+so5sa6EiwhF3q5rs0HF
            MklvUOxfnhgcpxgkQKBgQCMsiDpIh8BDKTxF20b8Az7NDtvm78vxfhF2rnCYIh9Q+3VKxbvoiNNTTJmlGT4Hi5App3
            l2GKIvRVZ9mE/vbtcWDk71/GgyiyuLixJYrY9gy2kYTz84R8v4ZMhjLB+Ba7VXkGU2u/Mj5LXzsQWCYRelC9DWlgco
            ReRXMHUbP4XwKBgQCGbYgE1gvW5ZYyi3xTrUIw8Bz7iUtbkO2Dg8egWLAYzRJizis6fd30xIG3wNheMVa/qqU3RrvS
            62N0QHZBjXJTH27li8JVQ9mfVbGZxcRLEwimBSEf5SNFlucwq02kvdJnL6vx5fE0XUziDPcgIUF9LO+VcCFKXE7kVN
            n1P/KHQwKBgDsxJc9vX4Pdgfc8V9cNIyj8TJUj/UdoDo+bnhSwsIbSLlwfyHRjrbY3zsqZ4JdIQWlQ+B/dJxWm5CzZ
            83f3/WTh3zNxlZTOID/Q/qL4Qf4DFe/4RyyyaAnUvMmcYpTcb6qrQSnJ4P0U18fyjdLQblYtpmrhK5mx7eMQq/QOwZ
            AoGAU3ftTjtt7Ihv44CSuQ5KnEJrbJAKV5e8sr1/lYOcDDpBYVJsqwv+Zn4hoWw/rPTrzWTy40irVULNZSCljPx78T
            sCS8uk5faUSQgXl8ihoo/1/cgPklNfvFT/xkuHkXRAEcwa8r95Lq+EDpRIWg3sMQJW3S5brWV1ovdAwrRrLisCgYAk
            +F2L604Ss7zgEbBGJEQoD+OFVP29WSrKThtVLaabYP1N8qVr+W/P5ojRZ94aqZ0wBLfklfdejOp399llcoFoMShc1k
            +ScpYZb7k3cHhLGdZsm+gCNuVQZlpYWvhnSjOfEHafQRckxtPtvVTVda/uHtWNwoDv39eSXMS4WLprug==',
            'applicationCertificatePassword': 'Password1', 'sharePointSettings':
            {'sharePointSaveAllWebParts': False, 'officeOrganizationName':
            'mycompany.onmicrosoft.com'}, 'exchangeSettings': {'account':
            'admin@mycompany.onmicrosoft.com'}}, 'modernAuthenticationWithLegacyProtocolsSettings':
            None, 'basicAuthenticationSettings': None}, 'region': 'Default'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CreateVb365Microsoft365OrganizationResponse200 | ErrorResponse]
    """

    kwargs = _get_kwargs(
        vb_365_server_uid=vb_365_server_uid,
        body=body,
        company_uid=company_uid,
        select=select,
        x_request_id=x_request_id,
        x_client_version=x_client_version,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    vb_365_server_uid: UUID,
    *,
    client: AuthenticatedClient,
    body: Vb365Microsoft365Organization,
    company_uid: UUID | Unset = UNSET,
    select: str | Unset = UNSET,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Any | CreateVb365Microsoft365OrganizationResponse200 | ErrorResponse | None:
    """Create Microsoft 365 Organization

     Creates a new Microsoft 365 organization on a Veeam Backup for Microsoft 365 server with the
    specified UID.

    Args:
        vb_365_server_uid (UUID):
        company_uid (UUID | Unset):
        select (str | Unset):
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):
        body (Vb365Microsoft365Organization):  Example: {'isTeamsOnline': True,
            'isTeamsChatsOnline': False, 'exchangeAndSharePointOnlineConnectionSettings':
            {'modernAppOnlyAuthenticationSettings': {'configureApplication': False, 'userCode': None,
            'newApplicationName': None, 'applicationId': 'ae61e533-82c7-4cb6-a030-78ae589cf49d',
            'applicationCertificate': 'MIIEoQIBAAKCAQBJ4W/TVQeIynO0BL/f/lc65mUzZmput1JCZsMLcjQB9eAteBV
            l5NRN4O5jUrWqXwk1IX17qtDiu3L8O07e0HlL+nHkRYeUDaztVbyhtvKc+YwNwZTQP8IvnWBpgrd2uJw167I7iQ5nu
            N2O7QL/8idBiKhgsOKz9frPMSp/QIXA3MQoi+Yp8TiyDvGps+iMn1KpLgkHehlXUFmuZvi27T6wSZGh97rHekpIj9b
            SirZFcG+7qupx8HFE4wNdhvxcvbmNkfMaJTmmi3YzGKYESwNyvwAIuohq1MoeQmNf1Q50NO04GOOPY+66uykOQkDkT
            a8/Vu90O6cux6/Ntyt04hndAgMBAAECggEABtA/m+HPnBHvsb5uY531NX1h/+eGEUfe0jjf7AJQQY4HaqoUbx03Zyd
            DVO2fy2KQWtIH3IvYT9CxvglKMMpRJWynbEHtSv4n4ItzpgZVQZzSCcK8kqgOpI2DArgHa2+DGIXwHgV5yp8F79Rz3
            l7at/R+csxdW/NnegwyuyGcNDkOjp8//HcrHQXPjljF5mwh4UZCFUvscKVjQbsOpiMvGeGN3z0/ZfKHi2egEA4+t1N
            LJykDiovNamtxE2xDkU8TXwn9STI8owzmxGtAA4HXDMuUQ0UXqxN0ED3WLJeqEKa0vuQ34+so5sa6EiwhF3q5rs0HF
            MklvUOxfnhgcpxgkQKBgQCMsiDpIh8BDKTxF20b8Az7NDtvm78vxfhF2rnCYIh9Q+3VKxbvoiNNTTJmlGT4Hi5App3
            l2GKIvRVZ9mE/vbtcWDk71/GgyiyuLixJYrY9gy2kYTz84R8v4ZMhjLB+Ba7VXkGU2u/Mj5LXzsQWCYRelC9DWlgco
            ReRXMHUbP4XwKBgQCGbYgE1gvW5ZYyi3xTrUIw8Bz7iUtbkO2Dg8egWLAYzRJizis6fd30xIG3wNheMVa/qqU3RrvS
            62N0QHZBjXJTH27li8JVQ9mfVbGZxcRLEwimBSEf5SNFlucwq02kvdJnL6vx5fE0XUziDPcgIUF9LO+VcCFKXE7kVN
            n1P/KHQwKBgDsxJc9vX4Pdgfc8V9cNIyj8TJUj/UdoDo+bnhSwsIbSLlwfyHRjrbY3zsqZ4JdIQWlQ+B/dJxWm5CzZ
            83f3/WTh3zNxlZTOID/Q/qL4Qf4DFe/4RyyyaAnUvMmcYpTcb6qrQSnJ4P0U18fyjdLQblYtpmrhK5mx7eMQq/QOwZ
            AoGAU3ftTjtt7Ihv44CSuQ5KnEJrbJAKV5e8sr1/lYOcDDpBYVJsqwv+Zn4hoWw/rPTrzWTy40irVULNZSCljPx78T
            sCS8uk5faUSQgXl8ihoo/1/cgPklNfvFT/xkuHkXRAEcwa8r95Lq+EDpRIWg3sMQJW3S5brWV1ovdAwrRrLisCgYAk
            +F2L604Ss7zgEbBGJEQoD+OFVP29WSrKThtVLaabYP1N8qVr+W/P5ojRZ94aqZ0wBLfklfdejOp399llcoFoMShc1k
            +ScpYZb7k3cHhLGdZsm+gCNuVQZlpYWvhnSjOfEHafQRckxtPtvVTVda/uHtWNwoDv39eSXMS4WLprug==',
            'applicationCertificatePassword': 'Password1', 'sharePointSettings':
            {'sharePointSaveAllWebParts': False, 'officeOrganizationName':
            'mycompany.onmicrosoft.com'}, 'exchangeSettings': {'account':
            'admin@mycompany.onmicrosoft.com'}}, 'modernAuthenticationWithLegacyProtocolsSettings':
            None, 'basicAuthenticationSettings': None}, 'region': 'Default'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CreateVb365Microsoft365OrganizationResponse200 | ErrorResponse
    """

    return sync_detailed(
        vb_365_server_uid=vb_365_server_uid,
        client=client,
        body=body,
        company_uid=company_uid,
        select=select,
        x_request_id=x_request_id,
        x_client_version=x_client_version,
    ).parsed


async def asyncio_detailed(
    vb_365_server_uid: UUID,
    *,
    client: AuthenticatedClient,
    body: Vb365Microsoft365Organization,
    company_uid: UUID | Unset = UNSET,
    select: str | Unset = UNSET,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Response[Any | CreateVb365Microsoft365OrganizationResponse200 | ErrorResponse]:
    """Create Microsoft 365 Organization

     Creates a new Microsoft 365 organization on a Veeam Backup for Microsoft 365 server with the
    specified UID.

    Args:
        vb_365_server_uid (UUID):
        company_uid (UUID | Unset):
        select (str | Unset):
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):
        body (Vb365Microsoft365Organization):  Example: {'isTeamsOnline': True,
            'isTeamsChatsOnline': False, 'exchangeAndSharePointOnlineConnectionSettings':
            {'modernAppOnlyAuthenticationSettings': {'configureApplication': False, 'userCode': None,
            'newApplicationName': None, 'applicationId': 'ae61e533-82c7-4cb6-a030-78ae589cf49d',
            'applicationCertificate': 'MIIEoQIBAAKCAQBJ4W/TVQeIynO0BL/f/lc65mUzZmput1JCZsMLcjQB9eAteBV
            l5NRN4O5jUrWqXwk1IX17qtDiu3L8O07e0HlL+nHkRYeUDaztVbyhtvKc+YwNwZTQP8IvnWBpgrd2uJw167I7iQ5nu
            N2O7QL/8idBiKhgsOKz9frPMSp/QIXA3MQoi+Yp8TiyDvGps+iMn1KpLgkHehlXUFmuZvi27T6wSZGh97rHekpIj9b
            SirZFcG+7qupx8HFE4wNdhvxcvbmNkfMaJTmmi3YzGKYESwNyvwAIuohq1MoeQmNf1Q50NO04GOOPY+66uykOQkDkT
            a8/Vu90O6cux6/Ntyt04hndAgMBAAECggEABtA/m+HPnBHvsb5uY531NX1h/+eGEUfe0jjf7AJQQY4HaqoUbx03Zyd
            DVO2fy2KQWtIH3IvYT9CxvglKMMpRJWynbEHtSv4n4ItzpgZVQZzSCcK8kqgOpI2DArgHa2+DGIXwHgV5yp8F79Rz3
            l7at/R+csxdW/NnegwyuyGcNDkOjp8//HcrHQXPjljF5mwh4UZCFUvscKVjQbsOpiMvGeGN3z0/ZfKHi2egEA4+t1N
            LJykDiovNamtxE2xDkU8TXwn9STI8owzmxGtAA4HXDMuUQ0UXqxN0ED3WLJeqEKa0vuQ34+so5sa6EiwhF3q5rs0HF
            MklvUOxfnhgcpxgkQKBgQCMsiDpIh8BDKTxF20b8Az7NDtvm78vxfhF2rnCYIh9Q+3VKxbvoiNNTTJmlGT4Hi5App3
            l2GKIvRVZ9mE/vbtcWDk71/GgyiyuLixJYrY9gy2kYTz84R8v4ZMhjLB+Ba7VXkGU2u/Mj5LXzsQWCYRelC9DWlgco
            ReRXMHUbP4XwKBgQCGbYgE1gvW5ZYyi3xTrUIw8Bz7iUtbkO2Dg8egWLAYzRJizis6fd30xIG3wNheMVa/qqU3RrvS
            62N0QHZBjXJTH27li8JVQ9mfVbGZxcRLEwimBSEf5SNFlucwq02kvdJnL6vx5fE0XUziDPcgIUF9LO+VcCFKXE7kVN
            n1P/KHQwKBgDsxJc9vX4Pdgfc8V9cNIyj8TJUj/UdoDo+bnhSwsIbSLlwfyHRjrbY3zsqZ4JdIQWlQ+B/dJxWm5CzZ
            83f3/WTh3zNxlZTOID/Q/qL4Qf4DFe/4RyyyaAnUvMmcYpTcb6qrQSnJ4P0U18fyjdLQblYtpmrhK5mx7eMQq/QOwZ
            AoGAU3ftTjtt7Ihv44CSuQ5KnEJrbJAKV5e8sr1/lYOcDDpBYVJsqwv+Zn4hoWw/rPTrzWTy40irVULNZSCljPx78T
            sCS8uk5faUSQgXl8ihoo/1/cgPklNfvFT/xkuHkXRAEcwa8r95Lq+EDpRIWg3sMQJW3S5brWV1ovdAwrRrLisCgYAk
            +F2L604Ss7zgEbBGJEQoD+OFVP29WSrKThtVLaabYP1N8qVr+W/P5ojRZ94aqZ0wBLfklfdejOp399llcoFoMShc1k
            +ScpYZb7k3cHhLGdZsm+gCNuVQZlpYWvhnSjOfEHafQRckxtPtvVTVda/uHtWNwoDv39eSXMS4WLprug==',
            'applicationCertificatePassword': 'Password1', 'sharePointSettings':
            {'sharePointSaveAllWebParts': False, 'officeOrganizationName':
            'mycompany.onmicrosoft.com'}, 'exchangeSettings': {'account':
            'admin@mycompany.onmicrosoft.com'}}, 'modernAuthenticationWithLegacyProtocolsSettings':
            None, 'basicAuthenticationSettings': None}, 'region': 'Default'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CreateVb365Microsoft365OrganizationResponse200 | ErrorResponse]
    """

    kwargs = _get_kwargs(
        vb_365_server_uid=vb_365_server_uid,
        body=body,
        company_uid=company_uid,
        select=select,
        x_request_id=x_request_id,
        x_client_version=x_client_version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    vb_365_server_uid: UUID,
    *,
    client: AuthenticatedClient,
    body: Vb365Microsoft365Organization,
    company_uid: UUID | Unset = UNSET,
    select: str | Unset = UNSET,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Any | CreateVb365Microsoft365OrganizationResponse200 | ErrorResponse | None:
    """Create Microsoft 365 Organization

     Creates a new Microsoft 365 organization on a Veeam Backup for Microsoft 365 server with the
    specified UID.

    Args:
        vb_365_server_uid (UUID):
        company_uid (UUID | Unset):
        select (str | Unset):
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):
        body (Vb365Microsoft365Organization):  Example: {'isTeamsOnline': True,
            'isTeamsChatsOnline': False, 'exchangeAndSharePointOnlineConnectionSettings':
            {'modernAppOnlyAuthenticationSettings': {'configureApplication': False, 'userCode': None,
            'newApplicationName': None, 'applicationId': 'ae61e533-82c7-4cb6-a030-78ae589cf49d',
            'applicationCertificate': 'MIIEoQIBAAKCAQBJ4W/TVQeIynO0BL/f/lc65mUzZmput1JCZsMLcjQB9eAteBV
            l5NRN4O5jUrWqXwk1IX17qtDiu3L8O07e0HlL+nHkRYeUDaztVbyhtvKc+YwNwZTQP8IvnWBpgrd2uJw167I7iQ5nu
            N2O7QL/8idBiKhgsOKz9frPMSp/QIXA3MQoi+Yp8TiyDvGps+iMn1KpLgkHehlXUFmuZvi27T6wSZGh97rHekpIj9b
            SirZFcG+7qupx8HFE4wNdhvxcvbmNkfMaJTmmi3YzGKYESwNyvwAIuohq1MoeQmNf1Q50NO04GOOPY+66uykOQkDkT
            a8/Vu90O6cux6/Ntyt04hndAgMBAAECggEABtA/m+HPnBHvsb5uY531NX1h/+eGEUfe0jjf7AJQQY4HaqoUbx03Zyd
            DVO2fy2KQWtIH3IvYT9CxvglKMMpRJWynbEHtSv4n4ItzpgZVQZzSCcK8kqgOpI2DArgHa2+DGIXwHgV5yp8F79Rz3
            l7at/R+csxdW/NnegwyuyGcNDkOjp8//HcrHQXPjljF5mwh4UZCFUvscKVjQbsOpiMvGeGN3z0/ZfKHi2egEA4+t1N
            LJykDiovNamtxE2xDkU8TXwn9STI8owzmxGtAA4HXDMuUQ0UXqxN0ED3WLJeqEKa0vuQ34+so5sa6EiwhF3q5rs0HF
            MklvUOxfnhgcpxgkQKBgQCMsiDpIh8BDKTxF20b8Az7NDtvm78vxfhF2rnCYIh9Q+3VKxbvoiNNTTJmlGT4Hi5App3
            l2GKIvRVZ9mE/vbtcWDk71/GgyiyuLixJYrY9gy2kYTz84R8v4ZMhjLB+Ba7VXkGU2u/Mj5LXzsQWCYRelC9DWlgco
            ReRXMHUbP4XwKBgQCGbYgE1gvW5ZYyi3xTrUIw8Bz7iUtbkO2Dg8egWLAYzRJizis6fd30xIG3wNheMVa/qqU3RrvS
            62N0QHZBjXJTH27li8JVQ9mfVbGZxcRLEwimBSEf5SNFlucwq02kvdJnL6vx5fE0XUziDPcgIUF9LO+VcCFKXE7kVN
            n1P/KHQwKBgDsxJc9vX4Pdgfc8V9cNIyj8TJUj/UdoDo+bnhSwsIbSLlwfyHRjrbY3zsqZ4JdIQWlQ+B/dJxWm5CzZ
            83f3/WTh3zNxlZTOID/Q/qL4Qf4DFe/4RyyyaAnUvMmcYpTcb6qrQSnJ4P0U18fyjdLQblYtpmrhK5mx7eMQq/QOwZ
            AoGAU3ftTjtt7Ihv44CSuQ5KnEJrbJAKV5e8sr1/lYOcDDpBYVJsqwv+Zn4hoWw/rPTrzWTy40irVULNZSCljPx78T
            sCS8uk5faUSQgXl8ihoo/1/cgPklNfvFT/xkuHkXRAEcwa8r95Lq+EDpRIWg3sMQJW3S5brWV1ovdAwrRrLisCgYAk
            +F2L604Ss7zgEbBGJEQoD+OFVP29WSrKThtVLaabYP1N8qVr+W/P5ojRZ94aqZ0wBLfklfdejOp399llcoFoMShc1k
            +ScpYZb7k3cHhLGdZsm+gCNuVQZlpYWvhnSjOfEHafQRckxtPtvVTVda/uHtWNwoDv39eSXMS4WLprug==',
            'applicationCertificatePassword': 'Password1', 'sharePointSettings':
            {'sharePointSaveAllWebParts': False, 'officeOrganizationName':
            'mycompany.onmicrosoft.com'}, 'exchangeSettings': {'account':
            'admin@mycompany.onmicrosoft.com'}}, 'modernAuthenticationWithLegacyProtocolsSettings':
            None, 'basicAuthenticationSettings': None}, 'region': 'Default'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CreateVb365Microsoft365OrganizationResponse200 | ErrorResponse
    """

    return (
        await asyncio_detailed(
            vb_365_server_uid=vb_365_server_uid,
            client=client,
            body=body,
            company_uid=company_uid,
            select=select,
            x_request_id=x_request_id,
            x_client_version=x_client_version,
        )
    ).parsed
