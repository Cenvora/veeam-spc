from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ResellerSiteWanAcceleratorResourceInput")


@_attrs_define
class ResellerSiteWanAcceleratorResourceInput:
    """
    Attributes:
        wan_accelerator_uid (UUID): UID assigned to a cloud backup repository.
    """

    wan_accelerator_uid: UUID
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        wan_accelerator_uid = str(self.wan_accelerator_uid)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "wanAcceleratorUid": wan_accelerator_uid,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        wan_accelerator_uid = UUID(d.pop("wanAcceleratorUid"))

        reseller_site_wan_accelerator_resource_input = cls(
            wan_accelerator_uid=wan_accelerator_uid,
        )

        reseller_site_wan_accelerator_resource_input.additional_properties = d
        return reseller_site_wan_accelerator_resource_input

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
