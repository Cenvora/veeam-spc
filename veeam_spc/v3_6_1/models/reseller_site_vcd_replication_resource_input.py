from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ResellerSiteVcdReplicationResourceInput")


@_attrs_define
class ResellerSiteVcdReplicationResourceInput:
    """
    Attributes:
        vcd_organization_uid (UUID): UID assigned to a VMware Cloud Director organization whose resources are allocated
            to a reseller.
    """

    vcd_organization_uid: UUID
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        vcd_organization_uid = str(self.vcd_organization_uid)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "vcdOrganizationUid": vcd_organization_uid,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        vcd_organization_uid = UUID(d.pop("vcdOrganizationUid"))

        reseller_site_vcd_replication_resource_input = cls(
            vcd_organization_uid=vcd_organization_uid,
        )

        reseller_site_vcd_replication_resource_input.additional_properties = d
        return reseller_site_vcd_replication_resource_input

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
