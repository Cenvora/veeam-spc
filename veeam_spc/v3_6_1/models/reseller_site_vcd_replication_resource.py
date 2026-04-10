from collections.abc import Mapping
from typing import Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ResellerSiteVcdReplicationResource")


@_attrs_define
class ResellerSiteVcdReplicationResource:
    """
    Attributes:
        vcd_organization_uid (UUID): UID assigned to a VMware Cloud Director organization whose resources are allocated
            to a reseller.
        instance_uid (Union[Unset, UUID]): UID assigned to a reseller VMware Cloud Director replication resource.
        site_uid (Union[Unset, UUID]): UID assigned to a Veeam Cloud Connect site.
        reseller_uid (Union[Unset, UUID]): UID assigned to a reseller.
    """

    vcd_organization_uid: UUID
    instance_uid: Union[Unset, UUID] = UNSET
    site_uid: Union[Unset, UUID] = UNSET
    reseller_uid: Union[Unset, UUID] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        vcd_organization_uid = str(self.vcd_organization_uid)

        instance_uid: Union[Unset, str] = UNSET
        if not isinstance(self.instance_uid, Unset):
            instance_uid = str(self.instance_uid)

        site_uid: Union[Unset, str] = UNSET
        if not isinstance(self.site_uid, Unset):
            site_uid = str(self.site_uid)

        reseller_uid: Union[Unset, str] = UNSET
        if not isinstance(self.reseller_uid, Unset):
            reseller_uid = str(self.reseller_uid)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "vcdOrganizationUid": vcd_organization_uid,
            }
        )
        if instance_uid is not UNSET:
            field_dict["instanceUid"] = instance_uid
        if site_uid is not UNSET:
            field_dict["siteUid"] = site_uid
        if reseller_uid is not UNSET:
            field_dict["resellerUid"] = reseller_uid

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        vcd_organization_uid = UUID(d.pop("vcdOrganizationUid"))

        _instance_uid = d.pop("instanceUid", UNSET)
        instance_uid: Union[Unset, UUID]
        if isinstance(_instance_uid, Unset):
            instance_uid = UNSET
        else:
            instance_uid = UUID(_instance_uid)

        _site_uid = d.pop("siteUid", UNSET)
        site_uid: Union[Unset, UUID]
        if isinstance(_site_uid, Unset):
            site_uid = UNSET
        else:
            site_uid = UUID(_site_uid)

        _reseller_uid = d.pop("resellerUid", UNSET)
        reseller_uid: Union[Unset, UUID]
        if isinstance(_reseller_uid, Unset):
            reseller_uid = UNSET
        else:
            reseller_uid = UUID(_reseller_uid)

        reseller_site_vcd_replication_resource = cls(
            vcd_organization_uid=vcd_organization_uid,
            instance_uid=instance_uid,
            site_uid=site_uid,
            reseller_uid=reseller_uid,
        )

        reseller_site_vcd_replication_resource.additional_properties = d
        return reseller_site_vcd_replication_resource

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
