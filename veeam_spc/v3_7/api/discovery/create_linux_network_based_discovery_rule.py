from http import HTTPStatus
from typing import Any, cast
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.create_linux_network_based_discovery_rule_response_200 import (
    CreateLinuxNetworkBasedDiscoveryRuleResponse200,
)
from ...models.error_response import ErrorResponse
from ...models.linux_network_based_discovery_rule_input import LinuxNetworkBasedDiscoveryRuleInput
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: LinuxNetworkBasedDiscoveryRuleInput,
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
        "url": "/discovery/rules/linux/networkBased",
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | CreateLinuxNetworkBasedDiscoveryRuleResponse200 | ErrorResponse:
    if response.status_code == 200:
        response_200 = CreateLinuxNetworkBasedDiscoveryRuleResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 202:
        response_202 = cast(Any, None)
        return response_202

    response_default = ErrorResponse.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | CreateLinuxNetworkBasedDiscoveryRuleResponse200 | ErrorResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: LinuxNetworkBasedDiscoveryRuleInput,
    select: str | Unset = UNSET,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Response[Any | CreateLinuxNetworkBasedDiscoveryRuleResponse200 | ErrorResponse]:
    r"""Create Network-Based Discovery Rule for Linux

     Creates a Linux network-based discovery rule.

    Args:
        select (str | Unset):
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):
        body (LinuxNetworkBasedDiscoveryRuleInput):  Example: {'name': 'Complex Linux Network
            Rule', 'masterAgentUid': 'da463bea-d186-4a14-b809-4aba366b03e8', 'networks':
            [{'networkName': 'netw', 'firstIp': '172.36.48.41', 'lastIp': '172.36.48.41',
            'trustOptions': {'trustOption': 'KnownList', 'knownHostList': 'valNet'}}], 'credentials':
            [{'username': 'root', 'password': 'Password1', 'priority': 0, 'description': 'Network-
            based rule for Linux computers', 'sshPort': 22, 'elevateAccountPrivileges': True,
            'addAccountToSudoersFile': True, 'useSuIfsudoFails': True, 'rootPassword': 'Password1',
            'sshPrivateKey': '-----BEGIN RSA PRIVATE KEY-----
            \nMIIEogIBAAKCAQEArVMvwKOymfth5E0wq38d7svfmLVsVAHtIJYMlJBTx6Y+R2+3\nDcAqVLZG9neFJU2ivudafb
            Znu1TykuM0sKRXRix+cpMUGevoY026m6lo0s7m3ft9\nF5oOrr1LefsSadI7MTRhCPrHBKt+G9taMhovnGHq/8JzUf
            lX2k1v7Sjy+zhJzpGW\nmJckhHZ+Jyd28JCdAWNiSEZgoEKGdLBL8/nkEm8Su4SRRKiTxRSbHtof+tUjIdoL\ntmdT
            9CiYM11eb46GMV8haaDEwpd0pL7iWZfXIo6ZZcKZ60JU70tYmz69JaYfVOLb\nasaI3ng22dzmt89Kk4C1i0ueVMH3
            WE7MvndpzwIBJQKCAQAODantBlqW3Qfv6pU+\nVmo19NrHMU34+Ty9c/Muo+seBo9tk2+1Ab4+OErxY6MDBkt3QzDZ
            wq52+Qy/zTuf\nnp9K4QNVZd8JBUoxkK5D+PqpTwvMzzOn08wAVImURMokQXprxfoHpaFvFNLfqgBk\n7V3OaM3dYs
            sUfAA0S3fHHv7xxijIfW/F4EKGk7B1+WX1LIoka4OF3fRtktqlv0xV\nIDG1YqugiwEHL2cxVHmviqJOfP496JKzz9
            TXS6TMWbRThykQjXf8irOfQsAbjmuO\nFFp+FCK8XITKuS9tBinpKpsUZoLiZ3r+uAO3gVWutdsdrJChYP87+Aaj82
            PWr+tv\nfSNlAoGBAOynYVyFklx597Yg4jdVg6+TEMlQ8Ga4TK6Iba8NzGPt6qRq1UeRninF\ncw7jIVojtqdqzKnn
            m+d5Ri4tS5rjLJjTwyePpR5HU3mwlDCpaJIS0XUptNOwwqso\n9Y/a92iwzAMA1Z4s3q+ye2tinP0WZb1B7RxMjrBN
            Ouswnv3An7BFAoGBALt+eoI1\nNujkC/JXQVYgkkWtJJgu+d314qSate929cW8w37p/OevwcafOlocCvQPGOa7g6XP
            \nyCtw6CQtv2jbiZ2RddyvTP8kYg71o4MtND5SGiJ+Q2B2PmDbCcPZ5IZ5PyNru6Wj\nClX/bFVh0lszbpWLPKKwdJ
            whd+d6i3dJewUDAoGBALMW4eUmz5/tmNzanVpOjSrr\n1VoTvNgcxGhnPj9Itll1xlLpEBp8CP0EH7g9Lf8GRQkSjQ
            r0dftHBK1StcFR+DxN\nOb0SwiTAWtihTYyb4G6KyAWjBWHtjGXZzpZgg+CFytHXHjKC0ghrZFFDtRKNfWyg\nl8Jj
            cuZISENHY4+YsDJdAoGAfq9niGklGeYxleft4D+FbVlQE8y2qrrlPslmLC3I\nqDNvVcCxzPo20k/pKCDJIXH8EYWe
            I+1CD4OjxWsEyk8lodD8nAe+ZzRCQXWKKDNM\n0Cmi9LYthl27ceAbWtF+u7m1ChhcMaWDhjb2K9pP3MHi72vqsx1H
            3x2IXiJeO9ez\n/HcCgYEAvbcMG79y8Io4lm+c/emqnIPIL0fyrwo7SJ9qdojN63IV3YtQvct+V/Za\nOnLVizuPAy
            e0Bk2qbc4nSt9Jj+E3PrOrZCyEtdQHwT90WM5fzb5OOk6sIwMJaajn\nY6mMXL0VW0XYI6PhfFPdwKhi2nPP07VzN3
            02VWxTI3HeNT7Hg6A=\n-----END RSA PRIVATE KEY-----\n', 'passphrase': '', 'type':
            'LinuxCertificate'}], 'filter': {'exclusionMask': [], 'ignoreInaccessibleMachine': True,
            'osTypes': ['Debian', 'Ubuntu'], 'applications': [], 'customApplication': None,
            'platforms': ['MicrosoftHyperVandVmWareVSphere', 'Physical']}, 'notificationSettings':
            {'isEnabled': True, 'scheduleType': 'Weeks', 'scheduleTime': '05:00', 'weekSettings':
            {'scheduleDay': 'Monday'}, 'to': 'admin@mycompany.com', 'subject': 'Linux Discovery',
            'notifyOnTheFirstRun': False}, 'deploymentSettings': {'isEnabled': False,
            'backupPolicyUid': None, 'setReadOnlyAccess': True}, 'scheduleSettings': {'scheduleType':
            'NotScheduled', 'timeZone': None, 'dailyScheduleSettings': None,
            'monthlyScheduleSettings': None, 'periodicalScheduleSettings': None}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CreateLinuxNetworkBasedDiscoveryRuleResponse200 | ErrorResponse]
    """

    kwargs = _get_kwargs(
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
    *,
    client: AuthenticatedClient,
    body: LinuxNetworkBasedDiscoveryRuleInput,
    select: str | Unset = UNSET,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Any | CreateLinuxNetworkBasedDiscoveryRuleResponse200 | ErrorResponse | None:
    r"""Create Network-Based Discovery Rule for Linux

     Creates a Linux network-based discovery rule.

    Args:
        select (str | Unset):
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):
        body (LinuxNetworkBasedDiscoveryRuleInput):  Example: {'name': 'Complex Linux Network
            Rule', 'masterAgentUid': 'da463bea-d186-4a14-b809-4aba366b03e8', 'networks':
            [{'networkName': 'netw', 'firstIp': '172.36.48.41', 'lastIp': '172.36.48.41',
            'trustOptions': {'trustOption': 'KnownList', 'knownHostList': 'valNet'}}], 'credentials':
            [{'username': 'root', 'password': 'Password1', 'priority': 0, 'description': 'Network-
            based rule for Linux computers', 'sshPort': 22, 'elevateAccountPrivileges': True,
            'addAccountToSudoersFile': True, 'useSuIfsudoFails': True, 'rootPassword': 'Password1',
            'sshPrivateKey': '-----BEGIN RSA PRIVATE KEY-----
            \nMIIEogIBAAKCAQEArVMvwKOymfth5E0wq38d7svfmLVsVAHtIJYMlJBTx6Y+R2+3\nDcAqVLZG9neFJU2ivudafb
            Znu1TykuM0sKRXRix+cpMUGevoY026m6lo0s7m3ft9\nF5oOrr1LefsSadI7MTRhCPrHBKt+G9taMhovnGHq/8JzUf
            lX2k1v7Sjy+zhJzpGW\nmJckhHZ+Jyd28JCdAWNiSEZgoEKGdLBL8/nkEm8Su4SRRKiTxRSbHtof+tUjIdoL\ntmdT
            9CiYM11eb46GMV8haaDEwpd0pL7iWZfXIo6ZZcKZ60JU70tYmz69JaYfVOLb\nasaI3ng22dzmt89Kk4C1i0ueVMH3
            WE7MvndpzwIBJQKCAQAODantBlqW3Qfv6pU+\nVmo19NrHMU34+Ty9c/Muo+seBo9tk2+1Ab4+OErxY6MDBkt3QzDZ
            wq52+Qy/zTuf\nnp9K4QNVZd8JBUoxkK5D+PqpTwvMzzOn08wAVImURMokQXprxfoHpaFvFNLfqgBk\n7V3OaM3dYs
            sUfAA0S3fHHv7xxijIfW/F4EKGk7B1+WX1LIoka4OF3fRtktqlv0xV\nIDG1YqugiwEHL2cxVHmviqJOfP496JKzz9
            TXS6TMWbRThykQjXf8irOfQsAbjmuO\nFFp+FCK8XITKuS9tBinpKpsUZoLiZ3r+uAO3gVWutdsdrJChYP87+Aaj82
            PWr+tv\nfSNlAoGBAOynYVyFklx597Yg4jdVg6+TEMlQ8Ga4TK6Iba8NzGPt6qRq1UeRninF\ncw7jIVojtqdqzKnn
            m+d5Ri4tS5rjLJjTwyePpR5HU3mwlDCpaJIS0XUptNOwwqso\n9Y/a92iwzAMA1Z4s3q+ye2tinP0WZb1B7RxMjrBN
            Ouswnv3An7BFAoGBALt+eoI1\nNujkC/JXQVYgkkWtJJgu+d314qSate929cW8w37p/OevwcafOlocCvQPGOa7g6XP
            \nyCtw6CQtv2jbiZ2RddyvTP8kYg71o4MtND5SGiJ+Q2B2PmDbCcPZ5IZ5PyNru6Wj\nClX/bFVh0lszbpWLPKKwdJ
            whd+d6i3dJewUDAoGBALMW4eUmz5/tmNzanVpOjSrr\n1VoTvNgcxGhnPj9Itll1xlLpEBp8CP0EH7g9Lf8GRQkSjQ
            r0dftHBK1StcFR+DxN\nOb0SwiTAWtihTYyb4G6KyAWjBWHtjGXZzpZgg+CFytHXHjKC0ghrZFFDtRKNfWyg\nl8Jj
            cuZISENHY4+YsDJdAoGAfq9niGklGeYxleft4D+FbVlQE8y2qrrlPslmLC3I\nqDNvVcCxzPo20k/pKCDJIXH8EYWe
            I+1CD4OjxWsEyk8lodD8nAe+ZzRCQXWKKDNM\n0Cmi9LYthl27ceAbWtF+u7m1ChhcMaWDhjb2K9pP3MHi72vqsx1H
            3x2IXiJeO9ez\n/HcCgYEAvbcMG79y8Io4lm+c/emqnIPIL0fyrwo7SJ9qdojN63IV3YtQvct+V/Za\nOnLVizuPAy
            e0Bk2qbc4nSt9Jj+E3PrOrZCyEtdQHwT90WM5fzb5OOk6sIwMJaajn\nY6mMXL0VW0XYI6PhfFPdwKhi2nPP07VzN3
            02VWxTI3HeNT7Hg6A=\n-----END RSA PRIVATE KEY-----\n', 'passphrase': '', 'type':
            'LinuxCertificate'}], 'filter': {'exclusionMask': [], 'ignoreInaccessibleMachine': True,
            'osTypes': ['Debian', 'Ubuntu'], 'applications': [], 'customApplication': None,
            'platforms': ['MicrosoftHyperVandVmWareVSphere', 'Physical']}, 'notificationSettings':
            {'isEnabled': True, 'scheduleType': 'Weeks', 'scheduleTime': '05:00', 'weekSettings':
            {'scheduleDay': 'Monday'}, 'to': 'admin@mycompany.com', 'subject': 'Linux Discovery',
            'notifyOnTheFirstRun': False}, 'deploymentSettings': {'isEnabled': False,
            'backupPolicyUid': None, 'setReadOnlyAccess': True}, 'scheduleSettings': {'scheduleType':
            'NotScheduled', 'timeZone': None, 'dailyScheduleSettings': None,
            'monthlyScheduleSettings': None, 'periodicalScheduleSettings': None}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CreateLinuxNetworkBasedDiscoveryRuleResponse200 | ErrorResponse
    """

    return sync_detailed(
        client=client,
        body=body,
        select=select,
        x_request_id=x_request_id,
        x_client_version=x_client_version,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: LinuxNetworkBasedDiscoveryRuleInput,
    select: str | Unset = UNSET,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Response[Any | CreateLinuxNetworkBasedDiscoveryRuleResponse200 | ErrorResponse]:
    r"""Create Network-Based Discovery Rule for Linux

     Creates a Linux network-based discovery rule.

    Args:
        select (str | Unset):
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):
        body (LinuxNetworkBasedDiscoveryRuleInput):  Example: {'name': 'Complex Linux Network
            Rule', 'masterAgentUid': 'da463bea-d186-4a14-b809-4aba366b03e8', 'networks':
            [{'networkName': 'netw', 'firstIp': '172.36.48.41', 'lastIp': '172.36.48.41',
            'trustOptions': {'trustOption': 'KnownList', 'knownHostList': 'valNet'}}], 'credentials':
            [{'username': 'root', 'password': 'Password1', 'priority': 0, 'description': 'Network-
            based rule for Linux computers', 'sshPort': 22, 'elevateAccountPrivileges': True,
            'addAccountToSudoersFile': True, 'useSuIfsudoFails': True, 'rootPassword': 'Password1',
            'sshPrivateKey': '-----BEGIN RSA PRIVATE KEY-----
            \nMIIEogIBAAKCAQEArVMvwKOymfth5E0wq38d7svfmLVsVAHtIJYMlJBTx6Y+R2+3\nDcAqVLZG9neFJU2ivudafb
            Znu1TykuM0sKRXRix+cpMUGevoY026m6lo0s7m3ft9\nF5oOrr1LefsSadI7MTRhCPrHBKt+G9taMhovnGHq/8JzUf
            lX2k1v7Sjy+zhJzpGW\nmJckhHZ+Jyd28JCdAWNiSEZgoEKGdLBL8/nkEm8Su4SRRKiTxRSbHtof+tUjIdoL\ntmdT
            9CiYM11eb46GMV8haaDEwpd0pL7iWZfXIo6ZZcKZ60JU70tYmz69JaYfVOLb\nasaI3ng22dzmt89Kk4C1i0ueVMH3
            WE7MvndpzwIBJQKCAQAODantBlqW3Qfv6pU+\nVmo19NrHMU34+Ty9c/Muo+seBo9tk2+1Ab4+OErxY6MDBkt3QzDZ
            wq52+Qy/zTuf\nnp9K4QNVZd8JBUoxkK5D+PqpTwvMzzOn08wAVImURMokQXprxfoHpaFvFNLfqgBk\n7V3OaM3dYs
            sUfAA0S3fHHv7xxijIfW/F4EKGk7B1+WX1LIoka4OF3fRtktqlv0xV\nIDG1YqugiwEHL2cxVHmviqJOfP496JKzz9
            TXS6TMWbRThykQjXf8irOfQsAbjmuO\nFFp+FCK8XITKuS9tBinpKpsUZoLiZ3r+uAO3gVWutdsdrJChYP87+Aaj82
            PWr+tv\nfSNlAoGBAOynYVyFklx597Yg4jdVg6+TEMlQ8Ga4TK6Iba8NzGPt6qRq1UeRninF\ncw7jIVojtqdqzKnn
            m+d5Ri4tS5rjLJjTwyePpR5HU3mwlDCpaJIS0XUptNOwwqso\n9Y/a92iwzAMA1Z4s3q+ye2tinP0WZb1B7RxMjrBN
            Ouswnv3An7BFAoGBALt+eoI1\nNujkC/JXQVYgkkWtJJgu+d314qSate929cW8w37p/OevwcafOlocCvQPGOa7g6XP
            \nyCtw6CQtv2jbiZ2RddyvTP8kYg71o4MtND5SGiJ+Q2B2PmDbCcPZ5IZ5PyNru6Wj\nClX/bFVh0lszbpWLPKKwdJ
            whd+d6i3dJewUDAoGBALMW4eUmz5/tmNzanVpOjSrr\n1VoTvNgcxGhnPj9Itll1xlLpEBp8CP0EH7g9Lf8GRQkSjQ
            r0dftHBK1StcFR+DxN\nOb0SwiTAWtihTYyb4G6KyAWjBWHtjGXZzpZgg+CFytHXHjKC0ghrZFFDtRKNfWyg\nl8Jj
            cuZISENHY4+YsDJdAoGAfq9niGklGeYxleft4D+FbVlQE8y2qrrlPslmLC3I\nqDNvVcCxzPo20k/pKCDJIXH8EYWe
            I+1CD4OjxWsEyk8lodD8nAe+ZzRCQXWKKDNM\n0Cmi9LYthl27ceAbWtF+u7m1ChhcMaWDhjb2K9pP3MHi72vqsx1H
            3x2IXiJeO9ez\n/HcCgYEAvbcMG79y8Io4lm+c/emqnIPIL0fyrwo7SJ9qdojN63IV3YtQvct+V/Za\nOnLVizuPAy
            e0Bk2qbc4nSt9Jj+E3PrOrZCyEtdQHwT90WM5fzb5OOk6sIwMJaajn\nY6mMXL0VW0XYI6PhfFPdwKhi2nPP07VzN3
            02VWxTI3HeNT7Hg6A=\n-----END RSA PRIVATE KEY-----\n', 'passphrase': '', 'type':
            'LinuxCertificate'}], 'filter': {'exclusionMask': [], 'ignoreInaccessibleMachine': True,
            'osTypes': ['Debian', 'Ubuntu'], 'applications': [], 'customApplication': None,
            'platforms': ['MicrosoftHyperVandVmWareVSphere', 'Physical']}, 'notificationSettings':
            {'isEnabled': True, 'scheduleType': 'Weeks', 'scheduleTime': '05:00', 'weekSettings':
            {'scheduleDay': 'Monday'}, 'to': 'admin@mycompany.com', 'subject': 'Linux Discovery',
            'notifyOnTheFirstRun': False}, 'deploymentSettings': {'isEnabled': False,
            'backupPolicyUid': None, 'setReadOnlyAccess': True}, 'scheduleSettings': {'scheduleType':
            'NotScheduled', 'timeZone': None, 'dailyScheduleSettings': None,
            'monthlyScheduleSettings': None, 'periodicalScheduleSettings': None}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CreateLinuxNetworkBasedDiscoveryRuleResponse200 | ErrorResponse]
    """

    kwargs = _get_kwargs(
        body=body,
        select=select,
        x_request_id=x_request_id,
        x_client_version=x_client_version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: LinuxNetworkBasedDiscoveryRuleInput,
    select: str | Unset = UNSET,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Any | CreateLinuxNetworkBasedDiscoveryRuleResponse200 | ErrorResponse | None:
    r"""Create Network-Based Discovery Rule for Linux

     Creates a Linux network-based discovery rule.

    Args:
        select (str | Unset):
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):
        body (LinuxNetworkBasedDiscoveryRuleInput):  Example: {'name': 'Complex Linux Network
            Rule', 'masterAgentUid': 'da463bea-d186-4a14-b809-4aba366b03e8', 'networks':
            [{'networkName': 'netw', 'firstIp': '172.36.48.41', 'lastIp': '172.36.48.41',
            'trustOptions': {'trustOption': 'KnownList', 'knownHostList': 'valNet'}}], 'credentials':
            [{'username': 'root', 'password': 'Password1', 'priority': 0, 'description': 'Network-
            based rule for Linux computers', 'sshPort': 22, 'elevateAccountPrivileges': True,
            'addAccountToSudoersFile': True, 'useSuIfsudoFails': True, 'rootPassword': 'Password1',
            'sshPrivateKey': '-----BEGIN RSA PRIVATE KEY-----
            \nMIIEogIBAAKCAQEArVMvwKOymfth5E0wq38d7svfmLVsVAHtIJYMlJBTx6Y+R2+3\nDcAqVLZG9neFJU2ivudafb
            Znu1TykuM0sKRXRix+cpMUGevoY026m6lo0s7m3ft9\nF5oOrr1LefsSadI7MTRhCPrHBKt+G9taMhovnGHq/8JzUf
            lX2k1v7Sjy+zhJzpGW\nmJckhHZ+Jyd28JCdAWNiSEZgoEKGdLBL8/nkEm8Su4SRRKiTxRSbHtof+tUjIdoL\ntmdT
            9CiYM11eb46GMV8haaDEwpd0pL7iWZfXIo6ZZcKZ60JU70tYmz69JaYfVOLb\nasaI3ng22dzmt89Kk4C1i0ueVMH3
            WE7MvndpzwIBJQKCAQAODantBlqW3Qfv6pU+\nVmo19NrHMU34+Ty9c/Muo+seBo9tk2+1Ab4+OErxY6MDBkt3QzDZ
            wq52+Qy/zTuf\nnp9K4QNVZd8JBUoxkK5D+PqpTwvMzzOn08wAVImURMokQXprxfoHpaFvFNLfqgBk\n7V3OaM3dYs
            sUfAA0S3fHHv7xxijIfW/F4EKGk7B1+WX1LIoka4OF3fRtktqlv0xV\nIDG1YqugiwEHL2cxVHmviqJOfP496JKzz9
            TXS6TMWbRThykQjXf8irOfQsAbjmuO\nFFp+FCK8XITKuS9tBinpKpsUZoLiZ3r+uAO3gVWutdsdrJChYP87+Aaj82
            PWr+tv\nfSNlAoGBAOynYVyFklx597Yg4jdVg6+TEMlQ8Ga4TK6Iba8NzGPt6qRq1UeRninF\ncw7jIVojtqdqzKnn
            m+d5Ri4tS5rjLJjTwyePpR5HU3mwlDCpaJIS0XUptNOwwqso\n9Y/a92iwzAMA1Z4s3q+ye2tinP0WZb1B7RxMjrBN
            Ouswnv3An7BFAoGBALt+eoI1\nNujkC/JXQVYgkkWtJJgu+d314qSate929cW8w37p/OevwcafOlocCvQPGOa7g6XP
            \nyCtw6CQtv2jbiZ2RddyvTP8kYg71o4MtND5SGiJ+Q2B2PmDbCcPZ5IZ5PyNru6Wj\nClX/bFVh0lszbpWLPKKwdJ
            whd+d6i3dJewUDAoGBALMW4eUmz5/tmNzanVpOjSrr\n1VoTvNgcxGhnPj9Itll1xlLpEBp8CP0EH7g9Lf8GRQkSjQ
            r0dftHBK1StcFR+DxN\nOb0SwiTAWtihTYyb4G6KyAWjBWHtjGXZzpZgg+CFytHXHjKC0ghrZFFDtRKNfWyg\nl8Jj
            cuZISENHY4+YsDJdAoGAfq9niGklGeYxleft4D+FbVlQE8y2qrrlPslmLC3I\nqDNvVcCxzPo20k/pKCDJIXH8EYWe
            I+1CD4OjxWsEyk8lodD8nAe+ZzRCQXWKKDNM\n0Cmi9LYthl27ceAbWtF+u7m1ChhcMaWDhjb2K9pP3MHi72vqsx1H
            3x2IXiJeO9ez\n/HcCgYEAvbcMG79y8Io4lm+c/emqnIPIL0fyrwo7SJ9qdojN63IV3YtQvct+V/Za\nOnLVizuPAy
            e0Bk2qbc4nSt9Jj+E3PrOrZCyEtdQHwT90WM5fzb5OOk6sIwMJaajn\nY6mMXL0VW0XYI6PhfFPdwKhi2nPP07VzN3
            02VWxTI3HeNT7Hg6A=\n-----END RSA PRIVATE KEY-----\n', 'passphrase': '', 'type':
            'LinuxCertificate'}], 'filter': {'exclusionMask': [], 'ignoreInaccessibleMachine': True,
            'osTypes': ['Debian', 'Ubuntu'], 'applications': [], 'customApplication': None,
            'platforms': ['MicrosoftHyperVandVmWareVSphere', 'Physical']}, 'notificationSettings':
            {'isEnabled': True, 'scheduleType': 'Weeks', 'scheduleTime': '05:00', 'weekSettings':
            {'scheduleDay': 'Monday'}, 'to': 'admin@mycompany.com', 'subject': 'Linux Discovery',
            'notifyOnTheFirstRun': False}, 'deploymentSettings': {'isEnabled': False,
            'backupPolicyUid': None, 'setReadOnlyAccess': True}, 'scheduleSettings': {'scheduleType':
            'NotScheduled', 'timeZone': None, 'dailyScheduleSettings': None,
            'monthlyScheduleSettings': None, 'periodicalScheduleSettings': None}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CreateLinuxNetworkBasedDiscoveryRuleResponse200 | ErrorResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            select=select,
            x_request_id=x_request_id,
            x_client_version=x_client_version,
        )
    ).parsed
