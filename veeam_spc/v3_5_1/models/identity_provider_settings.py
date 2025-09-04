from collections.abc import Mapping
from typing import Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.identity_provider_template import IdentityProviderTemplate
from ..models.identity_provider_type import IdentityProviderType
from ..types import UNSET, Unset

T = TypeVar("T", bound="IdentityProviderSettings")


@_attrs_define
class IdentityProviderSettings:
    r"""
    Example:
        {'name': 'myadfs', 'displayName': 'Microsoft Entra ID Federation Services', 'template': 'ADFS', 'type': 'SAML2',
            'configurationValidationSucceeded': True, 'errorMessage': None, 'configuration': '<identityProvider>\n  <saml2
            entityId="http://vac.myserver.com/Saml2/myadfs/" returnUrl="http://vac.myserver.com/Saml2/myadfs/">\n
            <federations>\n      <add
            metadataLocation="https://adfs.mydomain.com/federationmetadata/2007-06/federationmetadata.xml"\n
            allowUnsolicitedAuthnResponse="true" />\n    </federations>\n  </saml2>\n</identityProvider>\n', 'rulesCount':
            1, 'configurationCompleted': True, 'enabled': True}

    Attributes:
        name (str): Name of an identity provider.
        display_name (str): Display name of an identity provider.
        configuration (str): Identity provider type configuration.
            > For the `SAML` identity provider type use the
            [Sustainsys.Saml2](https://saml2.sustainsys.com/en/v2/configuration.html#sustainsys-saml2-section)
            configuration.
        template (Union[Unset, IdentityProviderTemplate]): Identity provider template.
        type_ (Union[Unset, IdentityProviderType]): Type of an identity provider.
        configuration_validation_succeeded (Union[Unset, bool]): Indicates whether an identity provider successfully
            passed validation procedure.
            > If the value is `false`, an identity provider is not functional.
        error_message (Union[Unset, str]): Error message.
            > If identity provider validation fails, the property value is not `null`.
        rules_count (Union[Unset, int]): Number of mapping rules configured for a service provider.
        configuration_completed (Union[Unset, bool]): Indicates whether the identity provider configuration is
            completed.
            >If configuration is not completed, an identity provider is not available on the authorization screen of the
            Veeam Service Provider Console web interface.
            >You can complete configuration by modifying this property using the PATCH operation.
            >If another identity provider is already enabled for an organization, this value cannot be modified.
             Default: False.
        enabled (Union[Unset, bool]): Indicates whether an identity provider is enabled. Default: True.
        organization_uid (Union[Unset, UUID]): UID assigned to an organization.
    """

    name: str
    display_name: str
    configuration: str
    template: Union[Unset, IdentityProviderTemplate] = UNSET
    type_: Union[Unset, IdentityProviderType] = UNSET
    configuration_validation_succeeded: Union[Unset, bool] = UNSET
    error_message: Union[Unset, str] = UNSET
    rules_count: Union[Unset, int] = UNSET
    configuration_completed: Union[Unset, bool] = False
    enabled: Union[Unset, bool] = True
    organization_uid: Union[Unset, UUID] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        display_name = self.display_name

        configuration = self.configuration

        template: Union[Unset, str] = UNSET
        if not isinstance(self.template, Unset):
            template = self.template.value

        type_: Union[Unset, str] = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        configuration_validation_succeeded = self.configuration_validation_succeeded

        error_message = self.error_message

        rules_count = self.rules_count

        configuration_completed = self.configuration_completed

        enabled = self.enabled

        organization_uid: Union[Unset, str] = UNSET
        if not isinstance(self.organization_uid, Unset):
            organization_uid = str(self.organization_uid)

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
        if configuration_validation_succeeded is not UNSET:
            field_dict["configurationValidationSucceeded"] = configuration_validation_succeeded
        if error_message is not UNSET:
            field_dict["errorMessage"] = error_message
        if rules_count is not UNSET:
            field_dict["rulesCount"] = rules_count
        if configuration_completed is not UNSET:
            field_dict["configurationCompleted"] = configuration_completed
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if organization_uid is not UNSET:
            field_dict["organizationUid"] = organization_uid

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        display_name = d.pop("displayName")

        configuration = d.pop("configuration")

        _template = d.pop("template", UNSET)
        template: Union[Unset, IdentityProviderTemplate]
        if isinstance(_template, Unset):
            template = UNSET
        else:
            template = IdentityProviderTemplate(_template)

        _type_ = d.pop("type", UNSET)
        type_: Union[Unset, IdentityProviderType]
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = IdentityProviderType(_type_)

        configuration_validation_succeeded = d.pop("configurationValidationSucceeded", UNSET)

        error_message = d.pop("errorMessage", UNSET)

        rules_count = d.pop("rulesCount", UNSET)

        configuration_completed = d.pop("configurationCompleted", UNSET)

        enabled = d.pop("enabled", UNSET)

        _organization_uid = d.pop("organizationUid", UNSET)
        organization_uid: Union[Unset, UUID]
        if isinstance(_organization_uid, Unset):
            organization_uid = UNSET
        else:
            organization_uid = UUID(_organization_uid)

        identity_provider_settings = cls(
            name=name,
            display_name=display_name,
            configuration=configuration,
            template=template,
            type_=type_,
            configuration_validation_succeeded=configuration_validation_succeeded,
            error_message=error_message,
            rules_count=rules_count,
            configuration_completed=configuration_completed,
            enabled=enabled,
            organization_uid=organization_uid,
        )

        identity_provider_settings.additional_properties = d
        return identity_provider_settings

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
