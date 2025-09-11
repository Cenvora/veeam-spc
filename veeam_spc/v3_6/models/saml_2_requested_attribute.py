from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.saml_2_requested_attribute_name_format import Saml2RequestedAttributeNameFormat
from ..types import UNSET, Unset

T = TypeVar("T", bound="Saml2RequestedAttribute")


@_attrs_define
class Saml2RequestedAttribute:
    """
    Attributes:
        name (str): Unique name of an attribute.
        friendly_name (Union[Unset, str]): Friendy name of an attribute.
        name_format (Union[Unset, Saml2RequestedAttributeNameFormat]): Format of the `name` value.
        is_required (Union[Unset, bool]): Indicates whether an attribute is required by a service provider.
    """

    name: str
    friendly_name: Union[Unset, str] = UNSET
    name_format: Union[Unset, Saml2RequestedAttributeNameFormat] = UNSET
    is_required: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        friendly_name = self.friendly_name

        name_format: Union[Unset, str] = UNSET
        if not isinstance(self.name_format, Unset):
            name_format = self.name_format.value

        is_required = self.is_required

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if friendly_name is not UNSET:
            field_dict["friendlyName"] = friendly_name
        if name_format is not UNSET:
            field_dict["nameFormat"] = name_format
        if is_required is not UNSET:
            field_dict["isRequired"] = is_required

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        friendly_name = d.pop("friendlyName", UNSET)

        _name_format = d.pop("nameFormat", UNSET)
        name_format: Union[Unset, Saml2RequestedAttributeNameFormat]
        if isinstance(_name_format, Unset):
            name_format = UNSET
        else:
            name_format = Saml2RequestedAttributeNameFormat(_name_format)

        is_required = d.pop("isRequired", UNSET)

        saml_2_requested_attribute = cls(
            name=name,
            friendly_name=friendly_name,
            name_format=name_format,
            is_required=is_required,
        )

        saml_2_requested_attribute.additional_properties = d
        return saml_2_requested_attribute

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
