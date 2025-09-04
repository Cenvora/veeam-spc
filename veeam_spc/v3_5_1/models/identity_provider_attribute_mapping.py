from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.identity_provider_attribute_mapping_attribute import IdentityProviderAttributeMappingAttribute
from ..types import UNSET, Unset

T = TypeVar("T", bound="IdentityProviderAttributeMapping")


@_attrs_define
class IdentityProviderAttributeMapping:
    """
    Attributes:
        claim_type (str): Mapping claim type.
        attribute (IdentityProviderAttributeMappingAttribute): User parameter to which a claim type is mapped.
        allow_aliases (Union[Unset, bool]): Indicates whether mapping claim name can be identified automatically.
            Default: True.
        default_value (Union[Unset, str]): Default attribute value.
    """

    claim_type: str
    attribute: IdentityProviderAttributeMappingAttribute
    allow_aliases: Union[Unset, bool] = True
    default_value: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        claim_type = self.claim_type

        attribute = self.attribute.value

        allow_aliases = self.allow_aliases

        default_value = self.default_value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "claimType": claim_type,
                "attribute": attribute,
            }
        )
        if allow_aliases is not UNSET:
            field_dict["allowAliases"] = allow_aliases
        if default_value is not UNSET:
            field_dict["defaultValue"] = default_value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        claim_type = d.pop("claimType")

        attribute = IdentityProviderAttributeMappingAttribute(d.pop("attribute"))

        allow_aliases = d.pop("allowAliases", UNSET)

        default_value = d.pop("defaultValue", UNSET)

        identity_provider_attribute_mapping = cls(
            claim_type=claim_type,
            attribute=attribute,
            allow_aliases=allow_aliases,
            default_value=default_value,
        )

        identity_provider_attribute_mapping.additional_properties = d
        return identity_provider_attribute_mapping

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
