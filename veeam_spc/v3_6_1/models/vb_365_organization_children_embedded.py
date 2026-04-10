from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.vb_365_organization_base import Vb365OrganizationBase


T = TypeVar("T", bound="Vb365OrganizationChildrenEmbedded")


@_attrs_define
class Vb365OrganizationChildrenEmbedded:
    """
    Attributes:
        organization_base (Union[Unset, Vb365OrganizationBase]):
    """

    organization_base: Union[Unset, "Vb365OrganizationBase"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        organization_base: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.organization_base, Unset):
            organization_base = self.organization_base.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if organization_base is not UNSET:
            field_dict["organizationBase"] = organization_base

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.vb_365_organization_base import Vb365OrganizationBase

        d = dict(src_dict)
        _organization_base = d.pop("organizationBase", UNSET)
        organization_base: Union[Unset, Vb365OrganizationBase]
        if isinstance(_organization_base, Unset):
            organization_base = UNSET
        else:
            organization_base = Vb365OrganizationBase.from_dict(_organization_base)

        vb_365_organization_children_embedded = cls(
            organization_base=organization_base,
        )

        vb_365_organization_children_embedded.additional_properties = d
        return vb_365_organization_children_embedded

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
