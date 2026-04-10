from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

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
    Attributes:
        name (str): Name of an identity provider.
        display_name (str): Display name of an identity provider.
        configuration (Saml2Configuration): Represents the `<sustainsys.saml2>` element of SAML2 configuration. For
            details, see the [Sustainsys.Saml2 documentation](https://saml2.sustainsys.com/en/v2/config-elements/sustainsys-
            saml2.html).
        template (Union[Unset, IdentityProviderTemplate]): Identity provider template.
        type_ (Union[Unset, IdentityProviderType]): Type of an identity provider.
        configuration_completed (Union[Unset, bool]): Indicates whether the identity provider configuration is
            completed.
            >If configuration is not completed, an identity provider is not available on the authorization screen of the
            Veeam Service Provider Console web interface.
            >You can complete configuration by modifying this property using the PATCH operation.
            >If another identity provider is already enabled for an organization, this value cannot be modified.
             Default: False.
        enabled (Union[Unset, bool]): Indicates whether an identity provider is enabled. Default: True.
    """

    name: str
    display_name: str
    configuration: "Saml2Configuration"
    template: Union[Unset, IdentityProviderTemplate] = UNSET
    type_: Union[Unset, IdentityProviderType] = UNSET
    configuration_completed: Union[Unset, bool] = False
    enabled: Union[Unset, bool] = True
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        display_name = self.display_name

        configuration = self.configuration.to_dict()

        template: Union[Unset, str] = UNSET
        if not isinstance(self.template, Unset):
            template = self.template.value

        type_: Union[Unset, str] = UNSET
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
