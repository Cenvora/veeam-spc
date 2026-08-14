from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.create_saml_2_identity_provider_response_200 import CreateSaml2IdentityProviderResponse200
from ...models.error_response import ErrorResponse
from ...models.identity_provider_settings_input import IdentityProviderSettingsInput
from ...types import UNSET, Response, Unset


def _get_kwargs(
    organization_uid: UUID,
    *,
    body: IdentityProviderSettingsInput,
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
        "url": "/organizations/{organization_uid}/identityProviders/saml2".format(
            organization_uid=quote(str(organization_uid), safe=""),
        ),
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | CreateSaml2IdentityProviderResponse200 | ErrorResponse:
    if response.status_code == 200:
        response_200 = CreateSaml2IdentityProviderResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 202:
        response_202 = cast(Any, None)
        return response_202

    response_default = ErrorResponse.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | CreateSaml2IdentityProviderResponse200 | ErrorResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    organization_uid: UUID,
    *,
    client: AuthenticatedClient,
    body: IdentityProviderSettingsInput,
    select: str | Unset = UNSET,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Response[Any | CreateSaml2IdentityProviderResponse200 | ErrorResponse]:
    """Create SAML2 Identity Provider

     Creates a new SAML2 identity provider.
    > Before you create a new SAML2 identity provider for a company you must generate a company portal
    URL.

    Args:
        organization_uid (UUID):
        select (str | Unset):
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):
        body (IdentityProviderSettingsInput):  Example: {'name': 'MyCompany', 'displayName':
            'MyCompany', 'template': 'Keycloak', 'configuration': {'entityId': 'MyCompany_remove',
            'returnUrl': 'https://vspc1.tech.local:1280/Saml2/MyCompany/', 'modulePath':
            'Saml2/MyCompany/', 'authenticateRequestSigningBehavior': 'IfIdpWantAuthnRequestsSigned',
            'outboundSigningAlgorithm': 'RsaSha256', 'minIncomingSigningAlgorithm': 'RsaSha256',
            'validateCertificates': None, 'publicOrigin': None, 'requestedAuthnContext': {'classRef':
            'Password', 'comparison': 'Exact'}, 'metadata': {'cacheDuration': 'PT1H', 'validDuration':
            '7.12:00:00', 'wantAssertionsSigned': True, 'organization': {'name': 'MyCompany',
            'displayName': 'MyCompany', 'url': 'https://vspc1.tech.local:1280', 'language': 'en'},
            'contactPerson': {'type': 'Other', 'company': None, 'givenName': None, 'surname': None,
            'phoneNumber': None, 'email': ''}, 'requestedAttributes': [{'name': 'Minimal',
            'friendlyName': None, 'nameFormat': None, 'isRequired': None}]}, 'identityProviders':
            [{'entityId': 'http://keycloak.tech.local:8080/auth/realms/master', 'signOnUrl': None,
            'wantAuthnRequestsSigned': None, 'binding': None, 'allowUnsolicitedAuthnResponse': True,
            'loadMetadata': True, 'outboundSigningAlgorithm': None, 'metadataLocation':
            'http://keycloak.tech.local:8080/auth/realms/master/protocol/saml/descriptor'}],
            'serviceCertificates': [{'use': 'Both', 'status': 'Current', 'privateKeyContent': 'data:ap
            plication/x-
            pkcs12;base64,MIIdGhvdWdoaGFsZndheWJhc2lzYW55aGVyc2VsZmV5ZXNwb2tlbnB1c2h0cmlja3NhbGVwZXJzb
            25hbHdpbGRidXN5YnJlZXplYWRkaXRpb25zZW50cGFya2dvdGFsaWtlcmljaGVnZ2dhaW5hbW9uZ2FsdGhvdWdoYXJ
            lbWl4Y291bGRyZW1hcmthYmxlYnJlYWtmYXN0YnJlYXRoZWJyb2tlcGlua3Bvc3NpYmx5Y2FtZXNhZGRsZXZvd2Vsc
            mVhcnRyZWF0ZWR3aGVlbG9yZGVycnVsZXJ0b3VjaHN3ZWV0c2xvd2x5c3ViamVjdG9uZXJhaW5sYWtlbm9yaW52b2x
            2ZWRjb3VwbGViaWdnZXJwYXJ0aWNsZXNicmlkZ2V3YWl0dGhyb3VnaHNwZWNpZmljYmVuZGZ1cnRoZXJwdXNoYXZva
            WRqYXJmaW5pc2hzdW1vZmZpY2VtYXJrZXRtb3VzZXBvbnljb250aW51ZWRyZWNlbnRpY2VsYWNrYmFuZGFueWRlZXB
            seWRpZmZpY3VsdHRocm91Z2hwbGVudHlkYWlseWFueXdheXNvbHV0aW9ucmV0dXJuZGVwZW5kc2FuZGRvb3JhY3Jvc
            3NoYXZpbmdzb2xpZHBvbGljZW1hbmNhcnJ5ZXNzZW50aWFsdmFwb3JwYXJ0aWN1bGFybHloaWxsYXJ0ZG96ZW5idWZ
            mYWxvZHJpdmVyb3V0ZXB1bGxnaWFudGd1ZXNzY2FzZWhhcHBpbHlzdXJwcmlzZXNwbGl0bGlrZWx5c2hhbGxydXNoc
            HVwaWxwb3B1bGF0aW9ucmVjb2duaXplcHJvcGVydHlkZWVwZ3JlZW5raXRjaGVud2FzdGVpc2xhbmRtYW51ZmFjdHV
            yaW5nd2hpc3BlcmVkYmlydGhqdW5nbGVzdG9yeWNvbXBhcmVsZXR0ZXJzZXR0aW5nY2xlYXJ0aGV5dGhyb3d0aHJvd
            Wdob3V0cmVxdWlyZWNhcmVmdWxseW1vdmllcmluZ3NpbWlsYXJ0cmlja2Zsb2F0aW5nd2VyZXVuaW9ucnVubmluZ3J
            lY29nbml6ZXdoaXRlZGFuZ2Vyb3VzcGVyY2VudGNob29zZW1vc3RlbXB0eWFwcGxpZWRicmVhdGhlc2FuZ21hdGhlb
            WF0aWNzdW50aWxjaGVja3NpbGx5c3BlbnRtaW5kbGFkeXByaWRlY2Fubm90dG93YXJkcmVndWxhcnVuaW9uYWxvdWR
            oYWJpdHJpc2luZ2Nsb3RodGVycmlibGVhbHRob3VnaGRpbm5lcmdsYWRjbG90aGluZ2Rpc2hyZWNvcmRvZnRyYWZma
            WN0cm9vcHNodXJyaWVkZW52aXJvbm1lbnRob21lY2hhbmdpbmdmdWVsbGF0ZWNob3NlbnRoZW9yeW9sZGVyb2xkZXN
            0ZmlsbGZpbmFsbmV3c3BhcGVyd29ya2VydmljdG9yeWhvdGRpZmZlcmVudGdyZWF0YWR2ZW50dXJlY2VudHJhbGZhb
            W91c3BhcnRzdHJlZXRzb2Z0bHlib3JuZmlsbXdlYWx0aGFzbGVlcHBoeXNpY2FsbW91bnRhaW53ZXN0cmVmZXJidWZ
            mYWxvcmVkcmVwbGFjZWFibGVqdXN0Z3JlYXRseWZvbGxvd2FsaXZlaXJvbmV4cHJlc3Npb25wYWxlb2ZmZXJhcnRpY
            2xlZm9ydHllbGVwaGFudGZhcnRoZXJkcmF3bG93ZXJ1cGZyZXF1ZW50bHlraWRzYnJva2V0cmlja2VzcGVjaWFsbHl
            lbGV2ZW5yb2xsc2luZ3JlYWR5c2xpcHBlZG9yZ2FuaXplZGRvd25sZWFzdG5vd2Zpc2hkb2N0b3Jjb3B5Ym90aHJlc
            HJlc2VudHNvY2lldHlwb3dkZXJjcmVhbWx1Y2t5Y29udGluZW50bGlwc3N3aW1za2lsbGxpZmVtZWx0ZWRkcmlua3J
            hbmdlc3R1ZHlpbmdncmV3ZmFzdGVuZWRzaGFyZWNvbnRhaW5mYWlyaW52b2x2ZWR3b2xmb2JqZWN0bWlsZWJhZGx5c
            HJhY3RpY2FsaW50b2ZyZXF1ZW50bHl0b3dhcmRkZXRlcm1pbmVuZWFybHlqb3lpbmNvbWVkaWRhbGl2ZWNvbGxlZ2V
            jaG9vc2VsaXN0ZGlzY3Vzc2hvbGR1bmtub3duc2hvcnRicmVhdGhlYmFsYW5jZW1vc3RicmVlemVhY2NlcHRraWxsd
            2hpdGVwaHJhc2VhbmdsZWFjdHVhbGJyZWF0aGRvY3RvcnRvd25zY2VuZW1ldGZsYW1lc2hlcm9kcG9saWNlbWFuZm9
            yZWlnbm1hbm5lcmdyZWF0d2hpdGVvcGluaW9uc29sYXJiZWFyc21va2VyZWFybm9kZGVkcHJpbWl0aXZlc3RhcmVkY
            29tbXVuaXR5bWFkZWFkamVjdGl2ZWdpcmx3YW50c2FsbW9ubmVlZGxldG9mZWF0dXJleW91cmpvaW5ibG9vZHBhcnR
            wZXJiaWdnZXJub25lZm91Z2h0d2F2ZWdpZnRmYXJ0aGVyd2F5bWFraW5ncHJlc2VudHdob21hcnJvd3BsZWFzdXJlZ
            nJvZ2Jyb3duZmFjZXF1aWV0bHlza3lzdG9ybXRvZGF5cHJvY2Vzc3BhcmVudGVhZ2VycG9ldHJ5YnJlYWRzaG9ldG9
            vdGhlZWRyaW5rZ3JlZW5wYWxhY2Vwcm92aWRldXNlZnVsY2xvc2VyaGFzc3RhcnRtYW5jb2FjaGFmdGVybm9vbnBhZ
            2V0cmllZGZhc3RzdXJmYWNlYnJlYXRobWlycm9ydHJpYmVkcmVzc2JhcnBhcmFsbGVsc3BlZWR0aWV0d29waWdldmV
            uaW5nbGFpZGNhcnJ5YmVhdHRhc2t0ZWxldmlzaW9uc25vd29jY3Vyd2F0ZXJhcHByb3ByaWF0ZXN3ZWV0d29yZW9mZ
            mVyaGFpcmFtb25nZmFybWVybWFkYWdhaW5zdGRpZmZpY3VsdHl3b29kZW5wYXJ0eW9yZm91Z2h0bmFtZWZlbGxiZWN
            hbWVmaW5pc2htaXNzaW9uc29saWR0b29mb3J0eWxpZmV0b3dhcmRsdW5jaHNoYWxscHVyZXN0b21hY2hvbGRlc3RiY
            XNld2VsbHNvbHZlbGFiZWxmZWV0ZWFybGllcmFkZGl0aW9uYWxuZXh0cXVhcnRlcmVpZ2h0bmVhcmJ5bmV2ZXJjYXN
            0cmVhc29uaXJvbmRlYWxvcHBvc2l0ZWxpcHNyZW1hcmthYmxlcHJpemVuaWdodHN0aWxsZWlnaHRsb2didXN5ZWxsb
            3dvcGVucmlkaW5nc2ltcGxlbm9zZXN0b25lc3R1ZGVudGNvbnN0YW50bHlmb3JnZXRiZXR0ZXJncmVhdGhpc3Rvcnl
            yZWFsc2lkZXNjYXJyeWZpbGxrbm93bGVkZ2VzdHJvbmdlcmZhY3Rvcmdsb2JlZWF0ZW5taW5lcmFsc2d1bGZraW5kc
            m9zZWV4cHJlc3Npb25yZWFsaXplbG9va2ZyZWVkdXR5dG9uZ3VlZGVlcGRpc2hiYW5kcmVhcmNoYXJhY3RlcmlzdGl
            jaHVzYmFuZG1pbmVyYWxzcG9uZHBhaW5hcmVhZnJpZW5kY3JlYXRlZnJlc2hyb2NreWF0dGVtcHR5b3VuZ2NvbnZlc
            nNhdGlvbmtuZXd3aGljaHRocm93Z2lybGNhbm5vdGZsaWVzc291dGhqb3VybmV5aW5kZWVkY29tYmluZXNsZWVwZmV
            uY2VldmVudHBhdGhiaWxsbG9zZXdvb2xmb3JlaWduaW5kZXBlbmRlbnRiYWxsb29ud2l0aGlub25seXBsZWFzdXJlb
            WVhdGJpdHNjaWVudGlmaWNkb3dubG93aG90c2hvcnRlcnNsaWdodGx5YWxvbmdzaG91dG1ldGFscmVzdHNvbWV0aGl
            uZ2V4cGVyaWVuY2VzdWNoYXJteXdpbmdyZW1haW5raXRjaGVuc3RyYW5nZXJzb3V0aHJoeXRobXN1cnByaXNlY2hhc
            mFjdGVyaXN0aWNkaXN0YW5jZXZlcnliZWxvbmdicmVhdGhpbmdhbHJlYWR5YmVsaWV2ZWRoZWFyZHBvc3NpYmxlcG9
            saWNlc29vbmNvd3NhbmR3YXZlZG96ZW5wZW5yaXNlaGFwcHlzdGF0ZW1lbnRjbGltYnBlcnNvbmVhcm5tb29kYmVjb
            21pbmdlbmdpbmVuZWdhdGl2ZXNvbWVoYXNtaWxsc2xpZGV3aGVhdGJlZW5pdHNjYWtlb2xkZXJ2aWxsYWdlc2F2ZWR
            iZWFudGVsZXBob25lYmVpbmdiYWxsY2xvc2VycG9zc2libHljbGltYnN0cnVjdHVyZWZ1cnBhaXJmaWZ0aHNob3Jlc
            3VubGln', 'metadataPublishOverride': None}], 'compatibility':
            {'ignoreMissingInResponseTo': True, 'ignoreAuthenticationContextInResponse': None,
            'unpackEntitiesDescriptorInIdentityProviderMetadata': True}}, 'configurationCompleted':
            True, 'enabled': True}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CreateSaml2IdentityProviderResponse200 | ErrorResponse]
    """

    kwargs = _get_kwargs(
        organization_uid=organization_uid,
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
    organization_uid: UUID,
    *,
    client: AuthenticatedClient,
    body: IdentityProviderSettingsInput,
    select: str | Unset = UNSET,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Any | CreateSaml2IdentityProviderResponse200 | ErrorResponse | None:
    """Create SAML2 Identity Provider

     Creates a new SAML2 identity provider.
    > Before you create a new SAML2 identity provider for a company you must generate a company portal
    URL.

    Args:
        organization_uid (UUID):
        select (str | Unset):
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):
        body (IdentityProviderSettingsInput):  Example: {'name': 'MyCompany', 'displayName':
            'MyCompany', 'template': 'Keycloak', 'configuration': {'entityId': 'MyCompany_remove',
            'returnUrl': 'https://vspc1.tech.local:1280/Saml2/MyCompany/', 'modulePath':
            'Saml2/MyCompany/', 'authenticateRequestSigningBehavior': 'IfIdpWantAuthnRequestsSigned',
            'outboundSigningAlgorithm': 'RsaSha256', 'minIncomingSigningAlgorithm': 'RsaSha256',
            'validateCertificates': None, 'publicOrigin': None, 'requestedAuthnContext': {'classRef':
            'Password', 'comparison': 'Exact'}, 'metadata': {'cacheDuration': 'PT1H', 'validDuration':
            '7.12:00:00', 'wantAssertionsSigned': True, 'organization': {'name': 'MyCompany',
            'displayName': 'MyCompany', 'url': 'https://vspc1.tech.local:1280', 'language': 'en'},
            'contactPerson': {'type': 'Other', 'company': None, 'givenName': None, 'surname': None,
            'phoneNumber': None, 'email': ''}, 'requestedAttributes': [{'name': 'Minimal',
            'friendlyName': None, 'nameFormat': None, 'isRequired': None}]}, 'identityProviders':
            [{'entityId': 'http://keycloak.tech.local:8080/auth/realms/master', 'signOnUrl': None,
            'wantAuthnRequestsSigned': None, 'binding': None, 'allowUnsolicitedAuthnResponse': True,
            'loadMetadata': True, 'outboundSigningAlgorithm': None, 'metadataLocation':
            'http://keycloak.tech.local:8080/auth/realms/master/protocol/saml/descriptor'}],
            'serviceCertificates': [{'use': 'Both', 'status': 'Current', 'privateKeyContent': 'data:ap
            plication/x-
            pkcs12;base64,MIIdGhvdWdoaGFsZndheWJhc2lzYW55aGVyc2VsZmV5ZXNwb2tlbnB1c2h0cmlja3NhbGVwZXJzb
            25hbHdpbGRidXN5YnJlZXplYWRkaXRpb25zZW50cGFya2dvdGFsaWtlcmljaGVnZ2dhaW5hbW9uZ2FsdGhvdWdoYXJ
            lbWl4Y291bGRyZW1hcmthYmxlYnJlYWtmYXN0YnJlYXRoZWJyb2tlcGlua3Bvc3NpYmx5Y2FtZXNhZGRsZXZvd2Vsc
            mVhcnRyZWF0ZWR3aGVlbG9yZGVycnVsZXJ0b3VjaHN3ZWV0c2xvd2x5c3ViamVjdG9uZXJhaW5sYWtlbm9yaW52b2x
            2ZWRjb3VwbGViaWdnZXJwYXJ0aWNsZXNicmlkZ2V3YWl0dGhyb3VnaHNwZWNpZmljYmVuZGZ1cnRoZXJwdXNoYXZva
            WRqYXJmaW5pc2hzdW1vZmZpY2VtYXJrZXRtb3VzZXBvbnljb250aW51ZWRyZWNlbnRpY2VsYWNrYmFuZGFueWRlZXB
            seWRpZmZpY3VsdHRocm91Z2hwbGVudHlkYWlseWFueXdheXNvbHV0aW9ucmV0dXJuZGVwZW5kc2FuZGRvb3JhY3Jvc
            3NoYXZpbmdzb2xpZHBvbGljZW1hbmNhcnJ5ZXNzZW50aWFsdmFwb3JwYXJ0aWN1bGFybHloaWxsYXJ0ZG96ZW5idWZ
            mYWxvZHJpdmVyb3V0ZXB1bGxnaWFudGd1ZXNzY2FzZWhhcHBpbHlzdXJwcmlzZXNwbGl0bGlrZWx5c2hhbGxydXNoc
            HVwaWxwb3B1bGF0aW9ucmVjb2duaXplcHJvcGVydHlkZWVwZ3JlZW5raXRjaGVud2FzdGVpc2xhbmRtYW51ZmFjdHV
            yaW5nd2hpc3BlcmVkYmlydGhqdW5nbGVzdG9yeWNvbXBhcmVsZXR0ZXJzZXR0aW5nY2xlYXJ0aGV5dGhyb3d0aHJvd
            Wdob3V0cmVxdWlyZWNhcmVmdWxseW1vdmllcmluZ3NpbWlsYXJ0cmlja2Zsb2F0aW5nd2VyZXVuaW9ucnVubmluZ3J
            lY29nbml6ZXdoaXRlZGFuZ2Vyb3VzcGVyY2VudGNob29zZW1vc3RlbXB0eWFwcGxpZWRicmVhdGhlc2FuZ21hdGhlb
            WF0aWNzdW50aWxjaGVja3NpbGx5c3BlbnRtaW5kbGFkeXByaWRlY2Fubm90dG93YXJkcmVndWxhcnVuaW9uYWxvdWR
            oYWJpdHJpc2luZ2Nsb3RodGVycmlibGVhbHRob3VnaGRpbm5lcmdsYWRjbG90aGluZ2Rpc2hyZWNvcmRvZnRyYWZma
            WN0cm9vcHNodXJyaWVkZW52aXJvbm1lbnRob21lY2hhbmdpbmdmdWVsbGF0ZWNob3NlbnRoZW9yeW9sZGVyb2xkZXN
            0ZmlsbGZpbmFsbmV3c3BhcGVyd29ya2VydmljdG9yeWhvdGRpZmZlcmVudGdyZWF0YWR2ZW50dXJlY2VudHJhbGZhb
            W91c3BhcnRzdHJlZXRzb2Z0bHlib3JuZmlsbXdlYWx0aGFzbGVlcHBoeXNpY2FsbW91bnRhaW53ZXN0cmVmZXJidWZ
            mYWxvcmVkcmVwbGFjZWFibGVqdXN0Z3JlYXRseWZvbGxvd2FsaXZlaXJvbmV4cHJlc3Npb25wYWxlb2ZmZXJhcnRpY
            2xlZm9ydHllbGVwaGFudGZhcnRoZXJkcmF3bG93ZXJ1cGZyZXF1ZW50bHlraWRzYnJva2V0cmlja2VzcGVjaWFsbHl
            lbGV2ZW5yb2xsc2luZ3JlYWR5c2xpcHBlZG9yZ2FuaXplZGRvd25sZWFzdG5vd2Zpc2hkb2N0b3Jjb3B5Ym90aHJlc
            HJlc2VudHNvY2lldHlwb3dkZXJjcmVhbWx1Y2t5Y29udGluZW50bGlwc3N3aW1za2lsbGxpZmVtZWx0ZWRkcmlua3J
            hbmdlc3R1ZHlpbmdncmV3ZmFzdGVuZWRzaGFyZWNvbnRhaW5mYWlyaW52b2x2ZWR3b2xmb2JqZWN0bWlsZWJhZGx5c
            HJhY3RpY2FsaW50b2ZyZXF1ZW50bHl0b3dhcmRkZXRlcm1pbmVuZWFybHlqb3lpbmNvbWVkaWRhbGl2ZWNvbGxlZ2V
            jaG9vc2VsaXN0ZGlzY3Vzc2hvbGR1bmtub3duc2hvcnRicmVhdGhlYmFsYW5jZW1vc3RicmVlemVhY2NlcHRraWxsd
            2hpdGVwaHJhc2VhbmdsZWFjdHVhbGJyZWF0aGRvY3RvcnRvd25zY2VuZW1ldGZsYW1lc2hlcm9kcG9saWNlbWFuZm9
            yZWlnbm1hbm5lcmdyZWF0d2hpdGVvcGluaW9uc29sYXJiZWFyc21va2VyZWFybm9kZGVkcHJpbWl0aXZlc3RhcmVkY
            29tbXVuaXR5bWFkZWFkamVjdGl2ZWdpcmx3YW50c2FsbW9ubmVlZGxldG9mZWF0dXJleW91cmpvaW5ibG9vZHBhcnR
            wZXJiaWdnZXJub25lZm91Z2h0d2F2ZWdpZnRmYXJ0aGVyd2F5bWFraW5ncHJlc2VudHdob21hcnJvd3BsZWFzdXJlZ
            nJvZ2Jyb3duZmFjZXF1aWV0bHlza3lzdG9ybXRvZGF5cHJvY2Vzc3BhcmVudGVhZ2VycG9ldHJ5YnJlYWRzaG9ldG9
            vdGhlZWRyaW5rZ3JlZW5wYWxhY2Vwcm92aWRldXNlZnVsY2xvc2VyaGFzc3RhcnRtYW5jb2FjaGFmdGVybm9vbnBhZ
            2V0cmllZGZhc3RzdXJmYWNlYnJlYXRobWlycm9ydHJpYmVkcmVzc2JhcnBhcmFsbGVsc3BlZWR0aWV0d29waWdldmV
            uaW5nbGFpZGNhcnJ5YmVhdHRhc2t0ZWxldmlzaW9uc25vd29jY3Vyd2F0ZXJhcHByb3ByaWF0ZXN3ZWV0d29yZW9mZ
            mVyaGFpcmFtb25nZmFybWVybWFkYWdhaW5zdGRpZmZpY3VsdHl3b29kZW5wYXJ0eW9yZm91Z2h0bmFtZWZlbGxiZWN
            hbWVmaW5pc2htaXNzaW9uc29saWR0b29mb3J0eWxpZmV0b3dhcmRsdW5jaHNoYWxscHVyZXN0b21hY2hvbGRlc3RiY
            XNld2VsbHNvbHZlbGFiZWxmZWV0ZWFybGllcmFkZGl0aW9uYWxuZXh0cXVhcnRlcmVpZ2h0bmVhcmJ5bmV2ZXJjYXN
            0cmVhc29uaXJvbmRlYWxvcHBvc2l0ZWxpcHNyZW1hcmthYmxlcHJpemVuaWdodHN0aWxsZWlnaHRsb2didXN5ZWxsb
            3dvcGVucmlkaW5nc2ltcGxlbm9zZXN0b25lc3R1ZGVudGNvbnN0YW50bHlmb3JnZXRiZXR0ZXJncmVhdGhpc3Rvcnl
            yZWFsc2lkZXNjYXJyeWZpbGxrbm93bGVkZ2VzdHJvbmdlcmZhY3Rvcmdsb2JlZWF0ZW5taW5lcmFsc2d1bGZraW5kc
            m9zZWV4cHJlc3Npb25yZWFsaXplbG9va2ZyZWVkdXR5dG9uZ3VlZGVlcGRpc2hiYW5kcmVhcmNoYXJhY3RlcmlzdGl
            jaHVzYmFuZG1pbmVyYWxzcG9uZHBhaW5hcmVhZnJpZW5kY3JlYXRlZnJlc2hyb2NreWF0dGVtcHR5b3VuZ2NvbnZlc
            nNhdGlvbmtuZXd3aGljaHRocm93Z2lybGNhbm5vdGZsaWVzc291dGhqb3VybmV5aW5kZWVkY29tYmluZXNsZWVwZmV
            uY2VldmVudHBhdGhiaWxsbG9zZXdvb2xmb3JlaWduaW5kZXBlbmRlbnRiYWxsb29ud2l0aGlub25seXBsZWFzdXJlb
            WVhdGJpdHNjaWVudGlmaWNkb3dubG93aG90c2hvcnRlcnNsaWdodGx5YWxvbmdzaG91dG1ldGFscmVzdHNvbWV0aGl
            uZ2V4cGVyaWVuY2VzdWNoYXJteXdpbmdyZW1haW5raXRjaGVuc3RyYW5nZXJzb3V0aHJoeXRobXN1cnByaXNlY2hhc
            mFjdGVyaXN0aWNkaXN0YW5jZXZlcnliZWxvbmdicmVhdGhpbmdhbHJlYWR5YmVsaWV2ZWRoZWFyZHBvc3NpYmxlcG9
            saWNlc29vbmNvd3NhbmR3YXZlZG96ZW5wZW5yaXNlaGFwcHlzdGF0ZW1lbnRjbGltYnBlcnNvbmVhcm5tb29kYmVjb
            21pbmdlbmdpbmVuZWdhdGl2ZXNvbWVoYXNtaWxsc2xpZGV3aGVhdGJlZW5pdHNjYWtlb2xkZXJ2aWxsYWdlc2F2ZWR
            iZWFudGVsZXBob25lYmVpbmdiYWxsY2xvc2VycG9zc2libHljbGltYnN0cnVjdHVyZWZ1cnBhaXJmaWZ0aHNob3Jlc
            3VubGln', 'metadataPublishOverride': None}], 'compatibility':
            {'ignoreMissingInResponseTo': True, 'ignoreAuthenticationContextInResponse': None,
            'unpackEntitiesDescriptorInIdentityProviderMetadata': True}}, 'configurationCompleted':
            True, 'enabled': True}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CreateSaml2IdentityProviderResponse200 | ErrorResponse
    """

    return sync_detailed(
        organization_uid=organization_uid,
        client=client,
        body=body,
        select=select,
        x_request_id=x_request_id,
        x_client_version=x_client_version,
    ).parsed


async def asyncio_detailed(
    organization_uid: UUID,
    *,
    client: AuthenticatedClient,
    body: IdentityProviderSettingsInput,
    select: str | Unset = UNSET,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Response[Any | CreateSaml2IdentityProviderResponse200 | ErrorResponse]:
    """Create SAML2 Identity Provider

     Creates a new SAML2 identity provider.
    > Before you create a new SAML2 identity provider for a company you must generate a company portal
    URL.

    Args:
        organization_uid (UUID):
        select (str | Unset):
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):
        body (IdentityProviderSettingsInput):  Example: {'name': 'MyCompany', 'displayName':
            'MyCompany', 'template': 'Keycloak', 'configuration': {'entityId': 'MyCompany_remove',
            'returnUrl': 'https://vspc1.tech.local:1280/Saml2/MyCompany/', 'modulePath':
            'Saml2/MyCompany/', 'authenticateRequestSigningBehavior': 'IfIdpWantAuthnRequestsSigned',
            'outboundSigningAlgorithm': 'RsaSha256', 'minIncomingSigningAlgorithm': 'RsaSha256',
            'validateCertificates': None, 'publicOrigin': None, 'requestedAuthnContext': {'classRef':
            'Password', 'comparison': 'Exact'}, 'metadata': {'cacheDuration': 'PT1H', 'validDuration':
            '7.12:00:00', 'wantAssertionsSigned': True, 'organization': {'name': 'MyCompany',
            'displayName': 'MyCompany', 'url': 'https://vspc1.tech.local:1280', 'language': 'en'},
            'contactPerson': {'type': 'Other', 'company': None, 'givenName': None, 'surname': None,
            'phoneNumber': None, 'email': ''}, 'requestedAttributes': [{'name': 'Minimal',
            'friendlyName': None, 'nameFormat': None, 'isRequired': None}]}, 'identityProviders':
            [{'entityId': 'http://keycloak.tech.local:8080/auth/realms/master', 'signOnUrl': None,
            'wantAuthnRequestsSigned': None, 'binding': None, 'allowUnsolicitedAuthnResponse': True,
            'loadMetadata': True, 'outboundSigningAlgorithm': None, 'metadataLocation':
            'http://keycloak.tech.local:8080/auth/realms/master/protocol/saml/descriptor'}],
            'serviceCertificates': [{'use': 'Both', 'status': 'Current', 'privateKeyContent': 'data:ap
            plication/x-
            pkcs12;base64,MIIdGhvdWdoaGFsZndheWJhc2lzYW55aGVyc2VsZmV5ZXNwb2tlbnB1c2h0cmlja3NhbGVwZXJzb
            25hbHdpbGRidXN5YnJlZXplYWRkaXRpb25zZW50cGFya2dvdGFsaWtlcmljaGVnZ2dhaW5hbW9uZ2FsdGhvdWdoYXJ
            lbWl4Y291bGRyZW1hcmthYmxlYnJlYWtmYXN0YnJlYXRoZWJyb2tlcGlua3Bvc3NpYmx5Y2FtZXNhZGRsZXZvd2Vsc
            mVhcnRyZWF0ZWR3aGVlbG9yZGVycnVsZXJ0b3VjaHN3ZWV0c2xvd2x5c3ViamVjdG9uZXJhaW5sYWtlbm9yaW52b2x
            2ZWRjb3VwbGViaWdnZXJwYXJ0aWNsZXNicmlkZ2V3YWl0dGhyb3VnaHNwZWNpZmljYmVuZGZ1cnRoZXJwdXNoYXZva
            WRqYXJmaW5pc2hzdW1vZmZpY2VtYXJrZXRtb3VzZXBvbnljb250aW51ZWRyZWNlbnRpY2VsYWNrYmFuZGFueWRlZXB
            seWRpZmZpY3VsdHRocm91Z2hwbGVudHlkYWlseWFueXdheXNvbHV0aW9ucmV0dXJuZGVwZW5kc2FuZGRvb3JhY3Jvc
            3NoYXZpbmdzb2xpZHBvbGljZW1hbmNhcnJ5ZXNzZW50aWFsdmFwb3JwYXJ0aWN1bGFybHloaWxsYXJ0ZG96ZW5idWZ
            mYWxvZHJpdmVyb3V0ZXB1bGxnaWFudGd1ZXNzY2FzZWhhcHBpbHlzdXJwcmlzZXNwbGl0bGlrZWx5c2hhbGxydXNoc
            HVwaWxwb3B1bGF0aW9ucmVjb2duaXplcHJvcGVydHlkZWVwZ3JlZW5raXRjaGVud2FzdGVpc2xhbmRtYW51ZmFjdHV
            yaW5nd2hpc3BlcmVkYmlydGhqdW5nbGVzdG9yeWNvbXBhcmVsZXR0ZXJzZXR0aW5nY2xlYXJ0aGV5dGhyb3d0aHJvd
            Wdob3V0cmVxdWlyZWNhcmVmdWxseW1vdmllcmluZ3NpbWlsYXJ0cmlja2Zsb2F0aW5nd2VyZXVuaW9ucnVubmluZ3J
            lY29nbml6ZXdoaXRlZGFuZ2Vyb3VzcGVyY2VudGNob29zZW1vc3RlbXB0eWFwcGxpZWRicmVhdGhlc2FuZ21hdGhlb
            WF0aWNzdW50aWxjaGVja3NpbGx5c3BlbnRtaW5kbGFkeXByaWRlY2Fubm90dG93YXJkcmVndWxhcnVuaW9uYWxvdWR
            oYWJpdHJpc2luZ2Nsb3RodGVycmlibGVhbHRob3VnaGRpbm5lcmdsYWRjbG90aGluZ2Rpc2hyZWNvcmRvZnRyYWZma
            WN0cm9vcHNodXJyaWVkZW52aXJvbm1lbnRob21lY2hhbmdpbmdmdWVsbGF0ZWNob3NlbnRoZW9yeW9sZGVyb2xkZXN
            0ZmlsbGZpbmFsbmV3c3BhcGVyd29ya2VydmljdG9yeWhvdGRpZmZlcmVudGdyZWF0YWR2ZW50dXJlY2VudHJhbGZhb
            W91c3BhcnRzdHJlZXRzb2Z0bHlib3JuZmlsbXdlYWx0aGFzbGVlcHBoeXNpY2FsbW91bnRhaW53ZXN0cmVmZXJidWZ
            mYWxvcmVkcmVwbGFjZWFibGVqdXN0Z3JlYXRseWZvbGxvd2FsaXZlaXJvbmV4cHJlc3Npb25wYWxlb2ZmZXJhcnRpY
            2xlZm9ydHllbGVwaGFudGZhcnRoZXJkcmF3bG93ZXJ1cGZyZXF1ZW50bHlraWRzYnJva2V0cmlja2VzcGVjaWFsbHl
            lbGV2ZW5yb2xsc2luZ3JlYWR5c2xpcHBlZG9yZ2FuaXplZGRvd25sZWFzdG5vd2Zpc2hkb2N0b3Jjb3B5Ym90aHJlc
            HJlc2VudHNvY2lldHlwb3dkZXJjcmVhbWx1Y2t5Y29udGluZW50bGlwc3N3aW1za2lsbGxpZmVtZWx0ZWRkcmlua3J
            hbmdlc3R1ZHlpbmdncmV3ZmFzdGVuZWRzaGFyZWNvbnRhaW5mYWlyaW52b2x2ZWR3b2xmb2JqZWN0bWlsZWJhZGx5c
            HJhY3RpY2FsaW50b2ZyZXF1ZW50bHl0b3dhcmRkZXRlcm1pbmVuZWFybHlqb3lpbmNvbWVkaWRhbGl2ZWNvbGxlZ2V
            jaG9vc2VsaXN0ZGlzY3Vzc2hvbGR1bmtub3duc2hvcnRicmVhdGhlYmFsYW5jZW1vc3RicmVlemVhY2NlcHRraWxsd
            2hpdGVwaHJhc2VhbmdsZWFjdHVhbGJyZWF0aGRvY3RvcnRvd25zY2VuZW1ldGZsYW1lc2hlcm9kcG9saWNlbWFuZm9
            yZWlnbm1hbm5lcmdyZWF0d2hpdGVvcGluaW9uc29sYXJiZWFyc21va2VyZWFybm9kZGVkcHJpbWl0aXZlc3RhcmVkY
            29tbXVuaXR5bWFkZWFkamVjdGl2ZWdpcmx3YW50c2FsbW9ubmVlZGxldG9mZWF0dXJleW91cmpvaW5ibG9vZHBhcnR
            wZXJiaWdnZXJub25lZm91Z2h0d2F2ZWdpZnRmYXJ0aGVyd2F5bWFraW5ncHJlc2VudHdob21hcnJvd3BsZWFzdXJlZ
            nJvZ2Jyb3duZmFjZXF1aWV0bHlza3lzdG9ybXRvZGF5cHJvY2Vzc3BhcmVudGVhZ2VycG9ldHJ5YnJlYWRzaG9ldG9
            vdGhlZWRyaW5rZ3JlZW5wYWxhY2Vwcm92aWRldXNlZnVsY2xvc2VyaGFzc3RhcnRtYW5jb2FjaGFmdGVybm9vbnBhZ
            2V0cmllZGZhc3RzdXJmYWNlYnJlYXRobWlycm9ydHJpYmVkcmVzc2JhcnBhcmFsbGVsc3BlZWR0aWV0d29waWdldmV
            uaW5nbGFpZGNhcnJ5YmVhdHRhc2t0ZWxldmlzaW9uc25vd29jY3Vyd2F0ZXJhcHByb3ByaWF0ZXN3ZWV0d29yZW9mZ
            mVyaGFpcmFtb25nZmFybWVybWFkYWdhaW5zdGRpZmZpY3VsdHl3b29kZW5wYXJ0eW9yZm91Z2h0bmFtZWZlbGxiZWN
            hbWVmaW5pc2htaXNzaW9uc29saWR0b29mb3J0eWxpZmV0b3dhcmRsdW5jaHNoYWxscHVyZXN0b21hY2hvbGRlc3RiY
            XNld2VsbHNvbHZlbGFiZWxmZWV0ZWFybGllcmFkZGl0aW9uYWxuZXh0cXVhcnRlcmVpZ2h0bmVhcmJ5bmV2ZXJjYXN
            0cmVhc29uaXJvbmRlYWxvcHBvc2l0ZWxpcHNyZW1hcmthYmxlcHJpemVuaWdodHN0aWxsZWlnaHRsb2didXN5ZWxsb
            3dvcGVucmlkaW5nc2ltcGxlbm9zZXN0b25lc3R1ZGVudGNvbnN0YW50bHlmb3JnZXRiZXR0ZXJncmVhdGhpc3Rvcnl
            yZWFsc2lkZXNjYXJyeWZpbGxrbm93bGVkZ2VzdHJvbmdlcmZhY3Rvcmdsb2JlZWF0ZW5taW5lcmFsc2d1bGZraW5kc
            m9zZWV4cHJlc3Npb25yZWFsaXplbG9va2ZyZWVkdXR5dG9uZ3VlZGVlcGRpc2hiYW5kcmVhcmNoYXJhY3RlcmlzdGl
            jaHVzYmFuZG1pbmVyYWxzcG9uZHBhaW5hcmVhZnJpZW5kY3JlYXRlZnJlc2hyb2NreWF0dGVtcHR5b3VuZ2NvbnZlc
            nNhdGlvbmtuZXd3aGljaHRocm93Z2lybGNhbm5vdGZsaWVzc291dGhqb3VybmV5aW5kZWVkY29tYmluZXNsZWVwZmV
            uY2VldmVudHBhdGhiaWxsbG9zZXdvb2xmb3JlaWduaW5kZXBlbmRlbnRiYWxsb29ud2l0aGlub25seXBsZWFzdXJlb
            WVhdGJpdHNjaWVudGlmaWNkb3dubG93aG90c2hvcnRlcnNsaWdodGx5YWxvbmdzaG91dG1ldGFscmVzdHNvbWV0aGl
            uZ2V4cGVyaWVuY2VzdWNoYXJteXdpbmdyZW1haW5raXRjaGVuc3RyYW5nZXJzb3V0aHJoeXRobXN1cnByaXNlY2hhc
            mFjdGVyaXN0aWNkaXN0YW5jZXZlcnliZWxvbmdicmVhdGhpbmdhbHJlYWR5YmVsaWV2ZWRoZWFyZHBvc3NpYmxlcG9
            saWNlc29vbmNvd3NhbmR3YXZlZG96ZW5wZW5yaXNlaGFwcHlzdGF0ZW1lbnRjbGltYnBlcnNvbmVhcm5tb29kYmVjb
            21pbmdlbmdpbmVuZWdhdGl2ZXNvbWVoYXNtaWxsc2xpZGV3aGVhdGJlZW5pdHNjYWtlb2xkZXJ2aWxsYWdlc2F2ZWR
            iZWFudGVsZXBob25lYmVpbmdiYWxsY2xvc2VycG9zc2libHljbGltYnN0cnVjdHVyZWZ1cnBhaXJmaWZ0aHNob3Jlc
            3VubGln', 'metadataPublishOverride': None}], 'compatibility':
            {'ignoreMissingInResponseTo': True, 'ignoreAuthenticationContextInResponse': None,
            'unpackEntitiesDescriptorInIdentityProviderMetadata': True}}, 'configurationCompleted':
            True, 'enabled': True}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CreateSaml2IdentityProviderResponse200 | ErrorResponse]
    """

    kwargs = _get_kwargs(
        organization_uid=organization_uid,
        body=body,
        select=select,
        x_request_id=x_request_id,
        x_client_version=x_client_version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    organization_uid: UUID,
    *,
    client: AuthenticatedClient,
    body: IdentityProviderSettingsInput,
    select: str | Unset = UNSET,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Any | CreateSaml2IdentityProviderResponse200 | ErrorResponse | None:
    """Create SAML2 Identity Provider

     Creates a new SAML2 identity provider.
    > Before you create a new SAML2 identity provider for a company you must generate a company portal
    URL.

    Args:
        organization_uid (UUID):
        select (str | Unset):
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):
        body (IdentityProviderSettingsInput):  Example: {'name': 'MyCompany', 'displayName':
            'MyCompany', 'template': 'Keycloak', 'configuration': {'entityId': 'MyCompany_remove',
            'returnUrl': 'https://vspc1.tech.local:1280/Saml2/MyCompany/', 'modulePath':
            'Saml2/MyCompany/', 'authenticateRequestSigningBehavior': 'IfIdpWantAuthnRequestsSigned',
            'outboundSigningAlgorithm': 'RsaSha256', 'minIncomingSigningAlgorithm': 'RsaSha256',
            'validateCertificates': None, 'publicOrigin': None, 'requestedAuthnContext': {'classRef':
            'Password', 'comparison': 'Exact'}, 'metadata': {'cacheDuration': 'PT1H', 'validDuration':
            '7.12:00:00', 'wantAssertionsSigned': True, 'organization': {'name': 'MyCompany',
            'displayName': 'MyCompany', 'url': 'https://vspc1.tech.local:1280', 'language': 'en'},
            'contactPerson': {'type': 'Other', 'company': None, 'givenName': None, 'surname': None,
            'phoneNumber': None, 'email': ''}, 'requestedAttributes': [{'name': 'Minimal',
            'friendlyName': None, 'nameFormat': None, 'isRequired': None}]}, 'identityProviders':
            [{'entityId': 'http://keycloak.tech.local:8080/auth/realms/master', 'signOnUrl': None,
            'wantAuthnRequestsSigned': None, 'binding': None, 'allowUnsolicitedAuthnResponse': True,
            'loadMetadata': True, 'outboundSigningAlgorithm': None, 'metadataLocation':
            'http://keycloak.tech.local:8080/auth/realms/master/protocol/saml/descriptor'}],
            'serviceCertificates': [{'use': 'Both', 'status': 'Current', 'privateKeyContent': 'data:ap
            plication/x-
            pkcs12;base64,MIIdGhvdWdoaGFsZndheWJhc2lzYW55aGVyc2VsZmV5ZXNwb2tlbnB1c2h0cmlja3NhbGVwZXJzb
            25hbHdpbGRidXN5YnJlZXplYWRkaXRpb25zZW50cGFya2dvdGFsaWtlcmljaGVnZ2dhaW5hbW9uZ2FsdGhvdWdoYXJ
            lbWl4Y291bGRyZW1hcmthYmxlYnJlYWtmYXN0YnJlYXRoZWJyb2tlcGlua3Bvc3NpYmx5Y2FtZXNhZGRsZXZvd2Vsc
            mVhcnRyZWF0ZWR3aGVlbG9yZGVycnVsZXJ0b3VjaHN3ZWV0c2xvd2x5c3ViamVjdG9uZXJhaW5sYWtlbm9yaW52b2x
            2ZWRjb3VwbGViaWdnZXJwYXJ0aWNsZXNicmlkZ2V3YWl0dGhyb3VnaHNwZWNpZmljYmVuZGZ1cnRoZXJwdXNoYXZva
            WRqYXJmaW5pc2hzdW1vZmZpY2VtYXJrZXRtb3VzZXBvbnljb250aW51ZWRyZWNlbnRpY2VsYWNrYmFuZGFueWRlZXB
            seWRpZmZpY3VsdHRocm91Z2hwbGVudHlkYWlseWFueXdheXNvbHV0aW9ucmV0dXJuZGVwZW5kc2FuZGRvb3JhY3Jvc
            3NoYXZpbmdzb2xpZHBvbGljZW1hbmNhcnJ5ZXNzZW50aWFsdmFwb3JwYXJ0aWN1bGFybHloaWxsYXJ0ZG96ZW5idWZ
            mYWxvZHJpdmVyb3V0ZXB1bGxnaWFudGd1ZXNzY2FzZWhhcHBpbHlzdXJwcmlzZXNwbGl0bGlrZWx5c2hhbGxydXNoc
            HVwaWxwb3B1bGF0aW9ucmVjb2duaXplcHJvcGVydHlkZWVwZ3JlZW5raXRjaGVud2FzdGVpc2xhbmRtYW51ZmFjdHV
            yaW5nd2hpc3BlcmVkYmlydGhqdW5nbGVzdG9yeWNvbXBhcmVsZXR0ZXJzZXR0aW5nY2xlYXJ0aGV5dGhyb3d0aHJvd
            Wdob3V0cmVxdWlyZWNhcmVmdWxseW1vdmllcmluZ3NpbWlsYXJ0cmlja2Zsb2F0aW5nd2VyZXVuaW9ucnVubmluZ3J
            lY29nbml6ZXdoaXRlZGFuZ2Vyb3VzcGVyY2VudGNob29zZW1vc3RlbXB0eWFwcGxpZWRicmVhdGhlc2FuZ21hdGhlb
            WF0aWNzdW50aWxjaGVja3NpbGx5c3BlbnRtaW5kbGFkeXByaWRlY2Fubm90dG93YXJkcmVndWxhcnVuaW9uYWxvdWR
            oYWJpdHJpc2luZ2Nsb3RodGVycmlibGVhbHRob3VnaGRpbm5lcmdsYWRjbG90aGluZ2Rpc2hyZWNvcmRvZnRyYWZma
            WN0cm9vcHNodXJyaWVkZW52aXJvbm1lbnRob21lY2hhbmdpbmdmdWVsbGF0ZWNob3NlbnRoZW9yeW9sZGVyb2xkZXN
            0ZmlsbGZpbmFsbmV3c3BhcGVyd29ya2VydmljdG9yeWhvdGRpZmZlcmVudGdyZWF0YWR2ZW50dXJlY2VudHJhbGZhb
            W91c3BhcnRzdHJlZXRzb2Z0bHlib3JuZmlsbXdlYWx0aGFzbGVlcHBoeXNpY2FsbW91bnRhaW53ZXN0cmVmZXJidWZ
            mYWxvcmVkcmVwbGFjZWFibGVqdXN0Z3JlYXRseWZvbGxvd2FsaXZlaXJvbmV4cHJlc3Npb25wYWxlb2ZmZXJhcnRpY
            2xlZm9ydHllbGVwaGFudGZhcnRoZXJkcmF3bG93ZXJ1cGZyZXF1ZW50bHlraWRzYnJva2V0cmlja2VzcGVjaWFsbHl
            lbGV2ZW5yb2xsc2luZ3JlYWR5c2xpcHBlZG9yZ2FuaXplZGRvd25sZWFzdG5vd2Zpc2hkb2N0b3Jjb3B5Ym90aHJlc
            HJlc2VudHNvY2lldHlwb3dkZXJjcmVhbWx1Y2t5Y29udGluZW50bGlwc3N3aW1za2lsbGxpZmVtZWx0ZWRkcmlua3J
            hbmdlc3R1ZHlpbmdncmV3ZmFzdGVuZWRzaGFyZWNvbnRhaW5mYWlyaW52b2x2ZWR3b2xmb2JqZWN0bWlsZWJhZGx5c
            HJhY3RpY2FsaW50b2ZyZXF1ZW50bHl0b3dhcmRkZXRlcm1pbmVuZWFybHlqb3lpbmNvbWVkaWRhbGl2ZWNvbGxlZ2V
            jaG9vc2VsaXN0ZGlzY3Vzc2hvbGR1bmtub3duc2hvcnRicmVhdGhlYmFsYW5jZW1vc3RicmVlemVhY2NlcHRraWxsd
            2hpdGVwaHJhc2VhbmdsZWFjdHVhbGJyZWF0aGRvY3RvcnRvd25zY2VuZW1ldGZsYW1lc2hlcm9kcG9saWNlbWFuZm9
            yZWlnbm1hbm5lcmdyZWF0d2hpdGVvcGluaW9uc29sYXJiZWFyc21va2VyZWFybm9kZGVkcHJpbWl0aXZlc3RhcmVkY
            29tbXVuaXR5bWFkZWFkamVjdGl2ZWdpcmx3YW50c2FsbW9ubmVlZGxldG9mZWF0dXJleW91cmpvaW5ibG9vZHBhcnR
            wZXJiaWdnZXJub25lZm91Z2h0d2F2ZWdpZnRmYXJ0aGVyd2F5bWFraW5ncHJlc2VudHdob21hcnJvd3BsZWFzdXJlZ
            nJvZ2Jyb3duZmFjZXF1aWV0bHlza3lzdG9ybXRvZGF5cHJvY2Vzc3BhcmVudGVhZ2VycG9ldHJ5YnJlYWRzaG9ldG9
            vdGhlZWRyaW5rZ3JlZW5wYWxhY2Vwcm92aWRldXNlZnVsY2xvc2VyaGFzc3RhcnRtYW5jb2FjaGFmdGVybm9vbnBhZ
            2V0cmllZGZhc3RzdXJmYWNlYnJlYXRobWlycm9ydHJpYmVkcmVzc2JhcnBhcmFsbGVsc3BlZWR0aWV0d29waWdldmV
            uaW5nbGFpZGNhcnJ5YmVhdHRhc2t0ZWxldmlzaW9uc25vd29jY3Vyd2F0ZXJhcHByb3ByaWF0ZXN3ZWV0d29yZW9mZ
            mVyaGFpcmFtb25nZmFybWVybWFkYWdhaW5zdGRpZmZpY3VsdHl3b29kZW5wYXJ0eW9yZm91Z2h0bmFtZWZlbGxiZWN
            hbWVmaW5pc2htaXNzaW9uc29saWR0b29mb3J0eWxpZmV0b3dhcmRsdW5jaHNoYWxscHVyZXN0b21hY2hvbGRlc3RiY
            XNld2VsbHNvbHZlbGFiZWxmZWV0ZWFybGllcmFkZGl0aW9uYWxuZXh0cXVhcnRlcmVpZ2h0bmVhcmJ5bmV2ZXJjYXN
            0cmVhc29uaXJvbmRlYWxvcHBvc2l0ZWxpcHNyZW1hcmthYmxlcHJpemVuaWdodHN0aWxsZWlnaHRsb2didXN5ZWxsb
            3dvcGVucmlkaW5nc2ltcGxlbm9zZXN0b25lc3R1ZGVudGNvbnN0YW50bHlmb3JnZXRiZXR0ZXJncmVhdGhpc3Rvcnl
            yZWFsc2lkZXNjYXJyeWZpbGxrbm93bGVkZ2VzdHJvbmdlcmZhY3Rvcmdsb2JlZWF0ZW5taW5lcmFsc2d1bGZraW5kc
            m9zZWV4cHJlc3Npb25yZWFsaXplbG9va2ZyZWVkdXR5dG9uZ3VlZGVlcGRpc2hiYW5kcmVhcmNoYXJhY3RlcmlzdGl
            jaHVzYmFuZG1pbmVyYWxzcG9uZHBhaW5hcmVhZnJpZW5kY3JlYXRlZnJlc2hyb2NreWF0dGVtcHR5b3VuZ2NvbnZlc
            nNhdGlvbmtuZXd3aGljaHRocm93Z2lybGNhbm5vdGZsaWVzc291dGhqb3VybmV5aW5kZWVkY29tYmluZXNsZWVwZmV
            uY2VldmVudHBhdGhiaWxsbG9zZXdvb2xmb3JlaWduaW5kZXBlbmRlbnRiYWxsb29ud2l0aGlub25seXBsZWFzdXJlb
            WVhdGJpdHNjaWVudGlmaWNkb3dubG93aG90c2hvcnRlcnNsaWdodGx5YWxvbmdzaG91dG1ldGFscmVzdHNvbWV0aGl
            uZ2V4cGVyaWVuY2VzdWNoYXJteXdpbmdyZW1haW5raXRjaGVuc3RyYW5nZXJzb3V0aHJoeXRobXN1cnByaXNlY2hhc
            mFjdGVyaXN0aWNkaXN0YW5jZXZlcnliZWxvbmdicmVhdGhpbmdhbHJlYWR5YmVsaWV2ZWRoZWFyZHBvc3NpYmxlcG9
            saWNlc29vbmNvd3NhbmR3YXZlZG96ZW5wZW5yaXNlaGFwcHlzdGF0ZW1lbnRjbGltYnBlcnNvbmVhcm5tb29kYmVjb
            21pbmdlbmdpbmVuZWdhdGl2ZXNvbWVoYXNtaWxsc2xpZGV3aGVhdGJlZW5pdHNjYWtlb2xkZXJ2aWxsYWdlc2F2ZWR
            iZWFudGVsZXBob25lYmVpbmdiYWxsY2xvc2VycG9zc2libHljbGltYnN0cnVjdHVyZWZ1cnBhaXJmaWZ0aHNob3Jlc
            3VubGln', 'metadataPublishOverride': None}], 'compatibility':
            {'ignoreMissingInResponseTo': True, 'ignoreAuthenticationContextInResponse': None,
            'unpackEntitiesDescriptorInIdentityProviderMetadata': True}}, 'configurationCompleted':
            True, 'enabled': True}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CreateSaml2IdentityProviderResponse200 | ErrorResponse
    """

    return (
        await asyncio_detailed(
            organization_uid=organization_uid,
            client=client,
            body=body,
            select=select,
            x_request_id=x_request_id,
            x_client_version=x_client_version,
        )
    ).parsed
