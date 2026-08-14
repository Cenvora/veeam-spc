from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.identity_provider_template import IdentityProviderTemplate
from ..models.identity_provider_type import IdentityProviderType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.saml_2_configuration import Saml2Configuration


T = TypeVar("T", bound="IdentityProviderSettingsInput")


@_attrs_define
class IdentityProviderSettingsInput:
    """
    Example:
        {'name': 'MyCompany', 'displayName': 'MyCompany', 'template': 'Keycloak', 'configuration': {'entityId':
            'MyCompany_remove', 'returnUrl': 'https://vspc1.tech.local:1280/Saml2/MyCompany/', 'modulePath':
            'Saml2/MyCompany/', 'authenticateRequestSigningBehavior': 'IfIdpWantAuthnRequestsSigned',
            'outboundSigningAlgorithm': 'RsaSha256', 'minIncomingSigningAlgorithm': 'RsaSha256', 'validateCertificates':
            None, 'publicOrigin': None, 'requestedAuthnContext': {'classRef': 'Password', 'comparison': 'Exact'},
            'metadata': {'cacheDuration': 'PT1H', 'validDuration': '7.12:00:00', 'wantAssertionsSigned': True,
            'organization': {'name': 'MyCompany', 'displayName': 'MyCompany', 'url': 'https://vspc1.tech.local:1280',
            'language': 'en'}, 'contactPerson': {'type': 'Other', 'company': None, 'givenName': None, 'surname': None,
            'phoneNumber': None, 'email': ''}, 'requestedAttributes': [{'name': 'Minimal', 'friendlyName': None,
            'nameFormat': None, 'isRequired': None}]}, 'identityProviders': [{'entityId':
            'http://keycloak.tech.local:8080/auth/realms/master', 'signOnUrl': None, 'wantAuthnRequestsSigned': None,
            'binding': None, 'allowUnsolicitedAuthnResponse': True, 'loadMetadata': True, 'outboundSigningAlgorithm': None,
            'metadataLocation': 'http://keycloak.tech.local:8080/auth/realms/master/protocol/saml/descriptor'}],
            'serviceCertificates': [{'use': 'Both', 'status': 'Current', 'privateKeyContent': 'data:application/x-
            pkcs12;base64,MIIdGhvdWdoaGFsZndheWJhc2lzYW55aGVyc2VsZmV5ZXNwb2tlbnB1c2h0cmlja3NhbGVwZXJzb25hbHdpbGRidXN5YnJlZXp
            lYWRkaXRpb25zZW50cGFya2dvdGFsaWtlcmljaGVnZ2dhaW5hbW9uZ2FsdGhvdWdoYXJlbWl4Y291bGRyZW1hcmthYmxlYnJlYWtmYXN0YnJlYXR
            oZWJyb2tlcGlua3Bvc3NpYmx5Y2FtZXNhZGRsZXZvd2VscmVhcnRyZWF0ZWR3aGVlbG9yZGVycnVsZXJ0b3VjaHN3ZWV0c2xvd2x5c3ViamVjdG9
            uZXJhaW5sYWtlbm9yaW52b2x2ZWRjb3VwbGViaWdnZXJwYXJ0aWNsZXNicmlkZ2V3YWl0dGhyb3VnaHNwZWNpZmljYmVuZGZ1cnRoZXJwdXNoYXZ
            vaWRqYXJmaW5pc2hzdW1vZmZpY2VtYXJrZXRtb3VzZXBvbnljb250aW51ZWRyZWNlbnRpY2VsYWNrYmFuZGFueWRlZXBseWRpZmZpY3VsdHRocm9
            1Z2hwbGVudHlkYWlseWFueXdheXNvbHV0aW9ucmV0dXJuZGVwZW5kc2FuZGRvb3JhY3Jvc3NoYXZpbmdzb2xpZHBvbGljZW1hbmNhcnJ5ZXNzZW5
            0aWFsdmFwb3JwYXJ0aWN1bGFybHloaWxsYXJ0ZG96ZW5idWZmYWxvZHJpdmVyb3V0ZXB1bGxnaWFudGd1ZXNzY2FzZWhhcHBpbHlzdXJwcmlzZXN
            wbGl0bGlrZWx5c2hhbGxydXNocHVwaWxwb3B1bGF0aW9ucmVjb2duaXplcHJvcGVydHlkZWVwZ3JlZW5raXRjaGVud2FzdGVpc2xhbmRtYW51ZmF
            jdHVyaW5nd2hpc3BlcmVkYmlydGhqdW5nbGVzdG9yeWNvbXBhcmVsZXR0ZXJzZXR0aW5nY2xlYXJ0aGV5dGhyb3d0aHJvdWdob3V0cmVxdWlyZWN
            hcmVmdWxseW1vdmllcmluZ3NpbWlsYXJ0cmlja2Zsb2F0aW5nd2VyZXVuaW9ucnVubmluZ3JlY29nbml6ZXdoaXRlZGFuZ2Vyb3VzcGVyY2VudGN
            ob29zZW1vc3RlbXB0eWFwcGxpZWRicmVhdGhlc2FuZ21hdGhlbWF0aWNzdW50aWxjaGVja3NpbGx5c3BlbnRtaW5kbGFkeXByaWRlY2Fubm90dG9
            3YXJkcmVndWxhcnVuaW9uYWxvdWRoYWJpdHJpc2luZ2Nsb3RodGVycmlibGVhbHRob3VnaGRpbm5lcmdsYWRjbG90aGluZ2Rpc2hyZWNvcmRvZnR
            yYWZmaWN0cm9vcHNodXJyaWVkZW52aXJvbm1lbnRob21lY2hhbmdpbmdmdWVsbGF0ZWNob3NlbnRoZW9yeW9sZGVyb2xkZXN0ZmlsbGZpbmFsbmV
            3c3BhcGVyd29ya2VydmljdG9yeWhvdGRpZmZlcmVudGdyZWF0YWR2ZW50dXJlY2VudHJhbGZhbW91c3BhcnRzdHJlZXRzb2Z0bHlib3JuZmlsbXd
            lYWx0aGFzbGVlcHBoeXNpY2FsbW91bnRhaW53ZXN0cmVmZXJidWZmYWxvcmVkcmVwbGFjZWFibGVqdXN0Z3JlYXRseWZvbGxvd2FsaXZlaXJvbmV
            4cHJlc3Npb25wYWxlb2ZmZXJhcnRpY2xlZm9ydHllbGVwaGFudGZhcnRoZXJkcmF3bG93ZXJ1cGZyZXF1ZW50bHlraWRzYnJva2V0cmlja2VzcGV
            jaWFsbHllbGV2ZW5yb2xsc2luZ3JlYWR5c2xpcHBlZG9yZ2FuaXplZGRvd25sZWFzdG5vd2Zpc2hkb2N0b3Jjb3B5Ym90aHJlcHJlc2VudHNvY2l
            ldHlwb3dkZXJjcmVhbWx1Y2t5Y29udGluZW50bGlwc3N3aW1za2lsbGxpZmVtZWx0ZWRkcmlua3Jhbmdlc3R1ZHlpbmdncmV3ZmFzdGVuZWRzaGF
            yZWNvbnRhaW5mYWlyaW52b2x2ZWR3b2xmb2JqZWN0bWlsZWJhZGx5cHJhY3RpY2FsaW50b2ZyZXF1ZW50bHl0b3dhcmRkZXRlcm1pbmVuZWFybHl
            qb3lpbmNvbWVkaWRhbGl2ZWNvbGxlZ2VjaG9vc2VsaXN0ZGlzY3Vzc2hvbGR1bmtub3duc2hvcnRicmVhdGhlYmFsYW5jZW1vc3RicmVlemVhY2N
            lcHRraWxsd2hpdGVwaHJhc2VhbmdsZWFjdHVhbGJyZWF0aGRvY3RvcnRvd25zY2VuZW1ldGZsYW1lc2hlcm9kcG9saWNlbWFuZm9yZWlnbm1hbm5
            lcmdyZWF0d2hpdGVvcGluaW9uc29sYXJiZWFyc21va2VyZWFybm9kZGVkcHJpbWl0aXZlc3RhcmVkY29tbXVuaXR5bWFkZWFkamVjdGl2ZWdpcmx
            3YW50c2FsbW9ubmVlZGxldG9mZWF0dXJleW91cmpvaW5ibG9vZHBhcnRwZXJiaWdnZXJub25lZm91Z2h0d2F2ZWdpZnRmYXJ0aGVyd2F5bWFraW5
            ncHJlc2VudHdob21hcnJvd3BsZWFzdXJlZnJvZ2Jyb3duZmFjZXF1aWV0bHlza3lzdG9ybXRvZGF5cHJvY2Vzc3BhcmVudGVhZ2VycG9ldHJ5YnJ
            lYWRzaG9ldG9vdGhlZWRyaW5rZ3JlZW5wYWxhY2Vwcm92aWRldXNlZnVsY2xvc2VyaGFzc3RhcnRtYW5jb2FjaGFmdGVybm9vbnBhZ2V0cmllZGZ
            hc3RzdXJmYWNlYnJlYXRobWlycm9ydHJpYmVkcmVzc2JhcnBhcmFsbGVsc3BlZWR0aWV0d29waWdldmVuaW5nbGFpZGNhcnJ5YmVhdHRhc2t0ZWx
            ldmlzaW9uc25vd29jY3Vyd2F0ZXJhcHByb3ByaWF0ZXN3ZWV0d29yZW9mZmVyaGFpcmFtb25nZmFybWVybWFkYWdhaW5zdGRpZmZpY3VsdHl3b29
            kZW5wYXJ0eW9yZm91Z2h0bmFtZWZlbGxiZWNhbWVmaW5pc2htaXNzaW9uc29saWR0b29mb3J0eWxpZmV0b3dhcmRsdW5jaHNoYWxscHVyZXN0b21
            hY2hvbGRlc3RiYXNld2VsbHNvbHZlbGFiZWxmZWV0ZWFybGllcmFkZGl0aW9uYWxuZXh0cXVhcnRlcmVpZ2h0bmVhcmJ5bmV2ZXJjYXN0cmVhc29
            uaXJvbmRlYWxvcHBvc2l0ZWxpcHNyZW1hcmthYmxlcHJpemVuaWdodHN0aWxsZWlnaHRsb2didXN5ZWxsb3dvcGVucmlkaW5nc2ltcGxlbm9zZXN
            0b25lc3R1ZGVudGNvbnN0YW50bHlmb3JnZXRiZXR0ZXJncmVhdGhpc3RvcnlyZWFsc2lkZXNjYXJyeWZpbGxrbm93bGVkZ2VzdHJvbmdlcmZhY3R
            vcmdsb2JlZWF0ZW5taW5lcmFsc2d1bGZraW5kcm9zZWV4cHJlc3Npb25yZWFsaXplbG9va2ZyZWVkdXR5dG9uZ3VlZGVlcGRpc2hiYW5kcmVhcmN
            oYXJhY3RlcmlzdGljaHVzYmFuZG1pbmVyYWxzcG9uZHBhaW5hcmVhZnJpZW5kY3JlYXRlZnJlc2hyb2NreWF0dGVtcHR5b3VuZ2NvbnZlcnNhdGl
            vbmtuZXd3aGljaHRocm93Z2lybGNhbm5vdGZsaWVzc291dGhqb3VybmV5aW5kZWVkY29tYmluZXNsZWVwZmVuY2VldmVudHBhdGhiaWxsbG9zZXd
            vb2xmb3JlaWduaW5kZXBlbmRlbnRiYWxsb29ud2l0aGlub25seXBsZWFzdXJlbWVhdGJpdHNjaWVudGlmaWNkb3dubG93aG90c2hvcnRlcnNsaWd
            odGx5YWxvbmdzaG91dG1ldGFscmVzdHNvbWV0aGluZ2V4cGVyaWVuY2VzdWNoYXJteXdpbmdyZW1haW5raXRjaGVuc3RyYW5nZXJzb3V0aHJoeXR
            obXN1cnByaXNlY2hhcmFjdGVyaXN0aWNkaXN0YW5jZXZlcnliZWxvbmdicmVhdGhpbmdhbHJlYWR5YmVsaWV2ZWRoZWFyZHBvc3NpYmxlcG9saWN
            lc29vbmNvd3NhbmR3YXZlZG96ZW5wZW5yaXNlaGFwcHlzdGF0ZW1lbnRjbGltYnBlcnNvbmVhcm5tb29kYmVjb21pbmdlbmdpbmVuZWdhdGl2ZXN
            vbWVoYXNtaWxsc2xpZGV3aGVhdGJlZW5pdHNjYWtlb2xkZXJ2aWxsYWdlc2F2ZWRiZWFudGVsZXBob25lYmVpbmdiYWxsY2xvc2VycG9zc2libHl
            jbGltYnN0cnVjdHVyZWZ1cnBhaXJmaWZ0aHNob3Jlc3VubGln', 'metadataPublishOverride': None}], 'compatibility':
            {'ignoreMissingInResponseTo': True, 'ignoreAuthenticationContextInResponse': None,
            'unpackEntitiesDescriptorInIdentityProviderMetadata': True}}, 'configurationCompleted': True, 'enabled': True}

    Attributes:
        name (str): Name of an identity provider.
        display_name (str): Display name of an identity provider.
        configuration (Saml2Configuration): Represents the `<sustainsys.saml2>` element of SAML2 configuration. For
            details, see the [Sustainsys.Saml2 documentation](https://saml2.sustainsys.com/en/v2/config-elements/sustainsys-
            saml2.html).
        template (IdentityProviderTemplate | Unset): Identity provider template.
        type_ (IdentityProviderType | Unset): Type of an identity provider.
        configuration_completed (bool | Unset): Indicates whether the identity provider configuration is completed.
            >If configuration is not completed, an identity provider is not available on the authorization screen of the
            Veeam Service Provider Console web interface.
            >You can complete configuration by modifying this property using the PATCH operation.
            >If another identity provider is already enabled for an organization, this value cannot be modified.
             Default: False.
        enabled (bool | Unset): Indicates whether an identity provider is enabled. Default: True.
    """

    name: str
    display_name: str
    configuration: Saml2Configuration
    template: IdentityProviderTemplate | Unset = UNSET
    type_: IdentityProviderType | Unset = UNSET
    configuration_completed: bool | Unset = False
    enabled: bool | Unset = True
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        display_name = self.display_name

        configuration = self.configuration.to_dict()

        template: str | Unset = UNSET
        if not isinstance(self.template, Unset):
            template = self.template.value

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        configuration_completed = self.configuration_completed

        enabled = self.enabled

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "displayName": display_name,
                "configuration": configuration,
            }
        )
        if template is not UNSET:
            field_dict["template"] = template
        if type_ is not UNSET:
            field_dict["type"] = type_
        if configuration_completed is not UNSET:
            field_dict["configurationCompleted"] = configuration_completed
        if enabled is not UNSET:
            field_dict["enabled"] = enabled

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.saml_2_configuration import Saml2Configuration

        d = dict(src_dict)
        name = d.pop("name")

        display_name = d.pop("displayName")

        configuration = Saml2Configuration.from_dict(d.pop("configuration"))

        _template = d.pop("template", UNSET)
        template: IdentityProviderTemplate | Unset
        if isinstance(_template, Unset):
            template = UNSET
        else:
            template = IdentityProviderTemplate(_template)

        _type_ = d.pop("type", UNSET)
        type_: IdentityProviderType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = IdentityProviderType(_type_)

        configuration_completed = d.pop("configurationCompleted", UNSET)

        enabled = d.pop("enabled", UNSET)

        identity_provider_settings_input = cls(
            name=name,
            display_name=display_name,
            configuration=configuration,
            template=template,
            type_=type_,
            configuration_completed=configuration_completed,
            enabled=enabled,
        )

        identity_provider_settings_input.additional_properties = d
        return identity_provider_settings_input

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
