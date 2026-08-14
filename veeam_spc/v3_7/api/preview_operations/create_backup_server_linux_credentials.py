from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.backup_server_credentials_linux_input import BackupServerCredentialsLinuxInput
from ...models.create_backup_server_linux_credentials_response_200 import CreateBackupServerLinuxCredentialsResponse200
from ...models.error_response import ErrorResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    backup_server_uid: UUID,
    *,
    body: BackupServerCredentialsLinuxInput,
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
        "method": "post",
        "url": "/infrastructure/backupServers/{backup_server_uid}/credentials/linux".format(
            backup_server_uid=quote(str(backup_server_uid), safe=""),
        ),
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | CreateBackupServerLinuxCredentialsResponse200 | ErrorResponse:
    if response.status_code == 200:
        response_200 = CreateBackupServerLinuxCredentialsResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 202:
        response_202 = cast(Any, None)
        return response_202

    response_default = ErrorResponse.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | CreateBackupServerLinuxCredentialsResponse200 | ErrorResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    backup_server_uid: UUID,
    *,
    client: AuthenticatedClient,
    body: BackupServerCredentialsLinuxInput,
    select: str | Unset = UNSET,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Response[Any | CreateBackupServerLinuxCredentialsResponse200 | ErrorResponse]:
    """Add Veeam Backup & Replication Server Linux Credentials

     Adds Linux credentials for a Veeam Backup & Replication server with the specified UID.

    Args:
        backup_server_uid (UUID):
        select (str | Unset):
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):
        body (BackupServerCredentialsLinuxInput):  Example: {'username': 'admin', 'password':
            'Password1', 'description': 'Credentials for Alpha company administrator',
            'mappedOrganizationUid': '988c4583-5336-4e20-892d-eabcca0b34ac', 'sshPort': 22,
            'autoElevated': True, 'addToSudoers': True, 'useSu': False, 'privateKey': '-----BEGIN RSA
            PRIVATE KEY-----MIIEowIBAAKCAQEAmqsrgygo+hDxXAZVB6nyqAL/O8h+SQn/iVcW8wfCsqw7S9KMnRvEQ3PM7U
            LZvOFDKCoBt1j4kHELVm3HKRtqatEyqCPrB8gBZuTVsi14naNYL40qJqgCuMCsNRosoG6pSUEwddSQ2uELez3eDm/f
            0H0kuyMf3VRqz5o3mRo0Vujs+xhD8FXQYEuTvEANetdIlA8FrQQAlx0dxTKuKK1tYvbPqASP01eHmj/Vr/nKJX/BoZ
            cSSSbEwpbqS4KlQHhlC0a7x/pfTurLwNKCQJWivhab6hCUanpttac3Hb2hQFdhymoI15j571i9yXam6Ul6i9qkW+M0
            x7m8Kd6lrOyVnwIDAQABAoIBAFib+9+2IFOzZTNdhVVQre5HWUY8xOy/R6C9Pi6ZoZePSKFVzK0tfTFPpHXBONEXFM
            xr1HPgCvdlbCNl3RXV2Q+9LhJaEYpxsSvrqencVx+otxr2+tEOrBCAgagiiLKY828+Y679ysc66sL+XLtUqJrfNy3n
            H5hDhrXNGlEiTB4Fi85f4us4Iqzg3Wc2TdAL6GX8qGmzopHG2PWGjHVeVnPerBfLgXhEtZSng3B57LGs9KQzfOi9ki
            e0Cso3e5yorky10Y4B7cd/hioI34PZMlfSsRuc0UfnQUAtLMiLCSFBejZbyvp8EW3sVLzN/Ho1aKbQWS7A9m0FKKdd
            JyVptdECgYEAx+2WSjaOL9HQMgT+j9U0DfXY321m+F/IRfcDRIBE/4fVeB2sfS5k/4zvgXEAsmoclRea7S8d2gQ81y
            o87mQbfkseM1SeA7uQzjOTPTiIcdNip/O5kDKUMszaMqckDAVflcD8M+F+mXdoLUgFH13S/UVRHZLJUoK1wP0RmIWq
            LQUCgYEAxgwM+m1hXfLPQi//D1aPk1ok3n1++aSCkzzucrMQ+pIZOnpE6x0EOBrccc9qkYzuDAj7VTJKhD39OD8+ZI
            IkICo1m9RVjfP/t+mgycBp4LaFsPaq7hhJOVhU7UvupnqJpOag3VUTKeUWtxbozNS/KqZa1bTq/kCEr4d42wH4mVMC
            gYAC3hmFvvqTHQNLdF7iWUCB4sDVk5Aih90rg7t8RAq5T410R5itwviX4cGdra1A4dy/FrOWK1LWSbFFtMli8fSi/x
            jTy6bojswo6Px3qFPsrgeAOTK0KsWNZPrMNzGBKqKQV1BGvjk+okPQQnQwWvwnvdLIBc71bAKHXhnegixKsQKBgQC0
            pmFgPU3HaKhtc2JxF0A35M4ktMyR4uHIdJf8wCIIriOdF9Kts/YZR0c1+UD4K1koWTkI6arXHcRQ/j9nZt6VCGuGDR
            VNOvhTRiSIY58wfs1MMnSQYk7IpC4zlkPGT5gmdsjdm7CzUmh58cfAr38A5GWO8kw4R5nAkw5Gl3GwSQKBgCgsVH+K
            xM4Y1jTyL+p/JK3roQ4wbFPQH3yTOYbQKUcLjzXY9yQ4OecoUoXjrbsaMn6unRdoSgosxP9s4OoTHpUdUfWJhhjr3z
            vm6/tU3dPc+U0UbUf4DZvto+JzdSVqUtBQlo5T/yYK0OIhQakvHGunaeWnj4cUT86kFzTizeJT-----END RSA
            PRIVATE KEY-----', 'passphrase': 'Passphrase1', 'rootPassword': 'Rootpass1'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CreateBackupServerLinuxCredentialsResponse200 | ErrorResponse]
    """

    kwargs = _get_kwargs(
        backup_server_uid=backup_server_uid,
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
    backup_server_uid: UUID,
    *,
    client: AuthenticatedClient,
    body: BackupServerCredentialsLinuxInput,
    select: str | Unset = UNSET,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Any | CreateBackupServerLinuxCredentialsResponse200 | ErrorResponse | None:
    """Add Veeam Backup & Replication Server Linux Credentials

     Adds Linux credentials for a Veeam Backup & Replication server with the specified UID.

    Args:
        backup_server_uid (UUID):
        select (str | Unset):
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):
        body (BackupServerCredentialsLinuxInput):  Example: {'username': 'admin', 'password':
            'Password1', 'description': 'Credentials for Alpha company administrator',
            'mappedOrganizationUid': '988c4583-5336-4e20-892d-eabcca0b34ac', 'sshPort': 22,
            'autoElevated': True, 'addToSudoers': True, 'useSu': False, 'privateKey': '-----BEGIN RSA
            PRIVATE KEY-----MIIEowIBAAKCAQEAmqsrgygo+hDxXAZVB6nyqAL/O8h+SQn/iVcW8wfCsqw7S9KMnRvEQ3PM7U
            LZvOFDKCoBt1j4kHELVm3HKRtqatEyqCPrB8gBZuTVsi14naNYL40qJqgCuMCsNRosoG6pSUEwddSQ2uELez3eDm/f
            0H0kuyMf3VRqz5o3mRo0Vujs+xhD8FXQYEuTvEANetdIlA8FrQQAlx0dxTKuKK1tYvbPqASP01eHmj/Vr/nKJX/BoZ
            cSSSbEwpbqS4KlQHhlC0a7x/pfTurLwNKCQJWivhab6hCUanpttac3Hb2hQFdhymoI15j571i9yXam6Ul6i9qkW+M0
            x7m8Kd6lrOyVnwIDAQABAoIBAFib+9+2IFOzZTNdhVVQre5HWUY8xOy/R6C9Pi6ZoZePSKFVzK0tfTFPpHXBONEXFM
            xr1HPgCvdlbCNl3RXV2Q+9LhJaEYpxsSvrqencVx+otxr2+tEOrBCAgagiiLKY828+Y679ysc66sL+XLtUqJrfNy3n
            H5hDhrXNGlEiTB4Fi85f4us4Iqzg3Wc2TdAL6GX8qGmzopHG2PWGjHVeVnPerBfLgXhEtZSng3B57LGs9KQzfOi9ki
            e0Cso3e5yorky10Y4B7cd/hioI34PZMlfSsRuc0UfnQUAtLMiLCSFBejZbyvp8EW3sVLzN/Ho1aKbQWS7A9m0FKKdd
            JyVptdECgYEAx+2WSjaOL9HQMgT+j9U0DfXY321m+F/IRfcDRIBE/4fVeB2sfS5k/4zvgXEAsmoclRea7S8d2gQ81y
            o87mQbfkseM1SeA7uQzjOTPTiIcdNip/O5kDKUMszaMqckDAVflcD8M+F+mXdoLUgFH13S/UVRHZLJUoK1wP0RmIWq
            LQUCgYEAxgwM+m1hXfLPQi//D1aPk1ok3n1++aSCkzzucrMQ+pIZOnpE6x0EOBrccc9qkYzuDAj7VTJKhD39OD8+ZI
            IkICo1m9RVjfP/t+mgycBp4LaFsPaq7hhJOVhU7UvupnqJpOag3VUTKeUWtxbozNS/KqZa1bTq/kCEr4d42wH4mVMC
            gYAC3hmFvvqTHQNLdF7iWUCB4sDVk5Aih90rg7t8RAq5T410R5itwviX4cGdra1A4dy/FrOWK1LWSbFFtMli8fSi/x
            jTy6bojswo6Px3qFPsrgeAOTK0KsWNZPrMNzGBKqKQV1BGvjk+okPQQnQwWvwnvdLIBc71bAKHXhnegixKsQKBgQC0
            pmFgPU3HaKhtc2JxF0A35M4ktMyR4uHIdJf8wCIIriOdF9Kts/YZR0c1+UD4K1koWTkI6arXHcRQ/j9nZt6VCGuGDR
            VNOvhTRiSIY58wfs1MMnSQYk7IpC4zlkPGT5gmdsjdm7CzUmh58cfAr38A5GWO8kw4R5nAkw5Gl3GwSQKBgCgsVH+K
            xM4Y1jTyL+p/JK3roQ4wbFPQH3yTOYbQKUcLjzXY9yQ4OecoUoXjrbsaMn6unRdoSgosxP9s4OoTHpUdUfWJhhjr3z
            vm6/tU3dPc+U0UbUf4DZvto+JzdSVqUtBQlo5T/yYK0OIhQakvHGunaeWnj4cUT86kFzTizeJT-----END RSA
            PRIVATE KEY-----', 'passphrase': 'Passphrase1', 'rootPassword': 'Rootpass1'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CreateBackupServerLinuxCredentialsResponse200 | ErrorResponse
    """

    return sync_detailed(
        backup_server_uid=backup_server_uid,
        client=client,
        body=body,
        select=select,
        x_request_id=x_request_id,
        x_client_version=x_client_version,
    ).parsed


async def asyncio_detailed(
    backup_server_uid: UUID,
    *,
    client: AuthenticatedClient,
    body: BackupServerCredentialsLinuxInput,
    select: str | Unset = UNSET,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Response[Any | CreateBackupServerLinuxCredentialsResponse200 | ErrorResponse]:
    """Add Veeam Backup & Replication Server Linux Credentials

     Adds Linux credentials for a Veeam Backup & Replication server with the specified UID.

    Args:
        backup_server_uid (UUID):
        select (str | Unset):
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):
        body (BackupServerCredentialsLinuxInput):  Example: {'username': 'admin', 'password':
            'Password1', 'description': 'Credentials for Alpha company administrator',
            'mappedOrganizationUid': '988c4583-5336-4e20-892d-eabcca0b34ac', 'sshPort': 22,
            'autoElevated': True, 'addToSudoers': True, 'useSu': False, 'privateKey': '-----BEGIN RSA
            PRIVATE KEY-----MIIEowIBAAKCAQEAmqsrgygo+hDxXAZVB6nyqAL/O8h+SQn/iVcW8wfCsqw7S9KMnRvEQ3PM7U
            LZvOFDKCoBt1j4kHELVm3HKRtqatEyqCPrB8gBZuTVsi14naNYL40qJqgCuMCsNRosoG6pSUEwddSQ2uELez3eDm/f
            0H0kuyMf3VRqz5o3mRo0Vujs+xhD8FXQYEuTvEANetdIlA8FrQQAlx0dxTKuKK1tYvbPqASP01eHmj/Vr/nKJX/BoZ
            cSSSbEwpbqS4KlQHhlC0a7x/pfTurLwNKCQJWivhab6hCUanpttac3Hb2hQFdhymoI15j571i9yXam6Ul6i9qkW+M0
            x7m8Kd6lrOyVnwIDAQABAoIBAFib+9+2IFOzZTNdhVVQre5HWUY8xOy/R6C9Pi6ZoZePSKFVzK0tfTFPpHXBONEXFM
            xr1HPgCvdlbCNl3RXV2Q+9LhJaEYpxsSvrqencVx+otxr2+tEOrBCAgagiiLKY828+Y679ysc66sL+XLtUqJrfNy3n
            H5hDhrXNGlEiTB4Fi85f4us4Iqzg3Wc2TdAL6GX8qGmzopHG2PWGjHVeVnPerBfLgXhEtZSng3B57LGs9KQzfOi9ki
            e0Cso3e5yorky10Y4B7cd/hioI34PZMlfSsRuc0UfnQUAtLMiLCSFBejZbyvp8EW3sVLzN/Ho1aKbQWS7A9m0FKKdd
            JyVptdECgYEAx+2WSjaOL9HQMgT+j9U0DfXY321m+F/IRfcDRIBE/4fVeB2sfS5k/4zvgXEAsmoclRea7S8d2gQ81y
            o87mQbfkseM1SeA7uQzjOTPTiIcdNip/O5kDKUMszaMqckDAVflcD8M+F+mXdoLUgFH13S/UVRHZLJUoK1wP0RmIWq
            LQUCgYEAxgwM+m1hXfLPQi//D1aPk1ok3n1++aSCkzzucrMQ+pIZOnpE6x0EOBrccc9qkYzuDAj7VTJKhD39OD8+ZI
            IkICo1m9RVjfP/t+mgycBp4LaFsPaq7hhJOVhU7UvupnqJpOag3VUTKeUWtxbozNS/KqZa1bTq/kCEr4d42wH4mVMC
            gYAC3hmFvvqTHQNLdF7iWUCB4sDVk5Aih90rg7t8RAq5T410R5itwviX4cGdra1A4dy/FrOWK1LWSbFFtMli8fSi/x
            jTy6bojswo6Px3qFPsrgeAOTK0KsWNZPrMNzGBKqKQV1BGvjk+okPQQnQwWvwnvdLIBc71bAKHXhnegixKsQKBgQC0
            pmFgPU3HaKhtc2JxF0A35M4ktMyR4uHIdJf8wCIIriOdF9Kts/YZR0c1+UD4K1koWTkI6arXHcRQ/j9nZt6VCGuGDR
            VNOvhTRiSIY58wfs1MMnSQYk7IpC4zlkPGT5gmdsjdm7CzUmh58cfAr38A5GWO8kw4R5nAkw5Gl3GwSQKBgCgsVH+K
            xM4Y1jTyL+p/JK3roQ4wbFPQH3yTOYbQKUcLjzXY9yQ4OecoUoXjrbsaMn6unRdoSgosxP9s4OoTHpUdUfWJhhjr3z
            vm6/tU3dPc+U0UbUf4DZvto+JzdSVqUtBQlo5T/yYK0OIhQakvHGunaeWnj4cUT86kFzTizeJT-----END RSA
            PRIVATE KEY-----', 'passphrase': 'Passphrase1', 'rootPassword': 'Rootpass1'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CreateBackupServerLinuxCredentialsResponse200 | ErrorResponse]
    """

    kwargs = _get_kwargs(
        backup_server_uid=backup_server_uid,
        body=body,
        select=select,
        x_request_id=x_request_id,
        x_client_version=x_client_version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    backup_server_uid: UUID,
    *,
    client: AuthenticatedClient,
    body: BackupServerCredentialsLinuxInput,
    select: str | Unset = UNSET,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Any | CreateBackupServerLinuxCredentialsResponse200 | ErrorResponse | None:
    """Add Veeam Backup & Replication Server Linux Credentials

     Adds Linux credentials for a Veeam Backup & Replication server with the specified UID.

    Args:
        backup_server_uid (UUID):
        select (str | Unset):
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):
        body (BackupServerCredentialsLinuxInput):  Example: {'username': 'admin', 'password':
            'Password1', 'description': 'Credentials for Alpha company administrator',
            'mappedOrganizationUid': '988c4583-5336-4e20-892d-eabcca0b34ac', 'sshPort': 22,
            'autoElevated': True, 'addToSudoers': True, 'useSu': False, 'privateKey': '-----BEGIN RSA
            PRIVATE KEY-----MIIEowIBAAKCAQEAmqsrgygo+hDxXAZVB6nyqAL/O8h+SQn/iVcW8wfCsqw7S9KMnRvEQ3PM7U
            LZvOFDKCoBt1j4kHELVm3HKRtqatEyqCPrB8gBZuTVsi14naNYL40qJqgCuMCsNRosoG6pSUEwddSQ2uELez3eDm/f
            0H0kuyMf3VRqz5o3mRo0Vujs+xhD8FXQYEuTvEANetdIlA8FrQQAlx0dxTKuKK1tYvbPqASP01eHmj/Vr/nKJX/BoZ
            cSSSbEwpbqS4KlQHhlC0a7x/pfTurLwNKCQJWivhab6hCUanpttac3Hb2hQFdhymoI15j571i9yXam6Ul6i9qkW+M0
            x7m8Kd6lrOyVnwIDAQABAoIBAFib+9+2IFOzZTNdhVVQre5HWUY8xOy/R6C9Pi6ZoZePSKFVzK0tfTFPpHXBONEXFM
            xr1HPgCvdlbCNl3RXV2Q+9LhJaEYpxsSvrqencVx+otxr2+tEOrBCAgagiiLKY828+Y679ysc66sL+XLtUqJrfNy3n
            H5hDhrXNGlEiTB4Fi85f4us4Iqzg3Wc2TdAL6GX8qGmzopHG2PWGjHVeVnPerBfLgXhEtZSng3B57LGs9KQzfOi9ki
            e0Cso3e5yorky10Y4B7cd/hioI34PZMlfSsRuc0UfnQUAtLMiLCSFBejZbyvp8EW3sVLzN/Ho1aKbQWS7A9m0FKKdd
            JyVptdECgYEAx+2WSjaOL9HQMgT+j9U0DfXY321m+F/IRfcDRIBE/4fVeB2sfS5k/4zvgXEAsmoclRea7S8d2gQ81y
            o87mQbfkseM1SeA7uQzjOTPTiIcdNip/O5kDKUMszaMqckDAVflcD8M+F+mXdoLUgFH13S/UVRHZLJUoK1wP0RmIWq
            LQUCgYEAxgwM+m1hXfLPQi//D1aPk1ok3n1++aSCkzzucrMQ+pIZOnpE6x0EOBrccc9qkYzuDAj7VTJKhD39OD8+ZI
            IkICo1m9RVjfP/t+mgycBp4LaFsPaq7hhJOVhU7UvupnqJpOag3VUTKeUWtxbozNS/KqZa1bTq/kCEr4d42wH4mVMC
            gYAC3hmFvvqTHQNLdF7iWUCB4sDVk5Aih90rg7t8RAq5T410R5itwviX4cGdra1A4dy/FrOWK1LWSbFFtMli8fSi/x
            jTy6bojswo6Px3qFPsrgeAOTK0KsWNZPrMNzGBKqKQV1BGvjk+okPQQnQwWvwnvdLIBc71bAKHXhnegixKsQKBgQC0
            pmFgPU3HaKhtc2JxF0A35M4ktMyR4uHIdJf8wCIIriOdF9Kts/YZR0c1+UD4K1koWTkI6arXHcRQ/j9nZt6VCGuGDR
            VNOvhTRiSIY58wfs1MMnSQYk7IpC4zlkPGT5gmdsjdm7CzUmh58cfAr38A5GWO8kw4R5nAkw5Gl3GwSQKBgCgsVH+K
            xM4Y1jTyL+p/JK3roQ4wbFPQH3yTOYbQKUcLjzXY9yQ4OecoUoXjrbsaMn6unRdoSgosxP9s4OoTHpUdUfWJhhjr3z
            vm6/tU3dPc+U0UbUf4DZvto+JzdSVqUtBQlo5T/yYK0OIhQakvHGunaeWnj4cUT86kFzTizeJT-----END RSA
            PRIVATE KEY-----', 'passphrase': 'Passphrase1', 'rootPassword': 'Rootpass1'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CreateBackupServerLinuxCredentialsResponse200 | ErrorResponse
    """

    return (
        await asyncio_detailed(
            backup_server_uid=backup_server_uid,
            client=client,
            body=body,
            select=select,
            x_request_id=x_request_id,
            x_client_version=x_client_version,
        )
    ).parsed
