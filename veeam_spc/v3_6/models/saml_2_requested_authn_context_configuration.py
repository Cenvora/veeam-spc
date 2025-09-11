from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.saml_2_requested_authn_context_configuration_class_ref import (
    Saml2RequestedAuthnContextConfigurationClassRef,
)
from ..models.saml_2_requested_authn_context_configuration_comparison import (
    Saml2RequestedAuthnContextConfigurationComparison,
)

T = TypeVar("T", bound="Saml2RequestedAuthnContextConfiguration")


@_attrs_define
class Saml2RequestedAuthnContextConfiguration:
    """Configuration of the `<requestedAuthnContext>` element.

    Attributes:
        class_ref (Saml2RequestedAuthnContextConfigurationClassRef): Class reference for the requested authentication
            context.
        comparison (Saml2RequestedAuthnContextConfigurationComparison): Indicates how strictly the identity provider
            must match the requested AuthnContext.
    """

    class_ref: Saml2RequestedAuthnContextConfigurationClassRef
    comparison: Saml2RequestedAuthnContextConfigurationComparison
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        class_ref = self.class_ref.value

        comparison = self.comparison.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "classRef": class_ref,
                "comparison": comparison,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        class_ref = Saml2RequestedAuthnContextConfigurationClassRef(d.pop("classRef"))

        comparison = Saml2RequestedAuthnContextConfigurationComparison(d.pop("comparison"))

        saml_2_requested_authn_context_configuration = cls(
            class_ref=class_ref,
            comparison=comparison,
        )

        saml_2_requested_authn_context_configuration.additional_properties = d
        return saml_2_requested_authn_context_configuration

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
