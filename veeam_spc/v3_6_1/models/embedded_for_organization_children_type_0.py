from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.organization import Organization


T = TypeVar("T", bound="EmbeddedForOrganizationChildrenType0")


@_attrs_define
class EmbeddedForOrganizationChildrenType0:
    """Resource representation of the related organization entity.

    Attributes:
        organization (Union[Unset, Organization]):
    """

    organization: Union[Unset, "Organization"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        organization: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.organization, Unset):
            organization = self.organization.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if organization is not UNSET:
            field_dict["organization"] = organization

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.organization import Organization

        d = dict(src_dict)
        _organization = d.pop("organization", UNSET)
        organization: Union[Unset, Organization]
        if isinstance(_organization, Unset):
            organization = UNSET
        else:
            organization = Organization.from_dict(_organization)

        embedded_for_organization_children_type_0 = cls(
            organization=organization,
        )

        embedded_for_organization_children_type_0.additional_properties = d
        return embedded_for_organization_children_type_0

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
