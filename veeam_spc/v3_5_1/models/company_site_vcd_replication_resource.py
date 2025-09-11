from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.company_site_vcd_replication_resource_data_center import CompanySiteVcdReplicationResourceDataCenter


T = TypeVar("T", bound="CompanySiteVcdReplicationResource")


@_attrs_define
class CompanySiteVcdReplicationResource:
    """
    Attributes:
        instance_uid (Union[Unset, UUID]): UID assigned to a VMware Cloud Director replication resource.
        company_uid (Union[Unset, UUID]): UID assigned to a company.
        site_uid (Union[Unset, UUID]): UID assigned to a Veeam Cloud Connect site.
        data_centers (Union[Unset, list['CompanySiteVcdReplicationResourceDataCenter']]): Array of datacenters
        is_failover_capabilities_enabled (Union[Unset, bool]): Indicates whether performing failover is available to a
            company. Default: False.
    """

    instance_uid: Union[Unset, UUID] = UNSET
    company_uid: Union[Unset, UUID] = UNSET
    site_uid: Union[Unset, UUID] = UNSET
    data_centers: Union[Unset, list["CompanySiteVcdReplicationResourceDataCenter"]] = UNSET
    is_failover_capabilities_enabled: Union[Unset, bool] = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        instance_uid: Union[Unset, str] = UNSET
        if not isinstance(self.instance_uid, Unset):
            instance_uid = str(self.instance_uid)

        company_uid: Union[Unset, str] = UNSET
        if not isinstance(self.company_uid, Unset):
            company_uid = str(self.company_uid)

        site_uid: Union[Unset, str] = UNSET
        if not isinstance(self.site_uid, Unset):
            site_uid = str(self.site_uid)

        data_centers: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.data_centers, Unset):
            data_centers = []
            for data_centers_item_data in self.data_centers:
                data_centers_item = data_centers_item_data.to_dict()
                data_centers.append(data_centers_item)

        is_failover_capabilities_enabled = self.is_failover_capabilities_enabled

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if instance_uid is not UNSET:
            field_dict["instanceUid"] = instance_uid
        if company_uid is not UNSET:
            field_dict["companyUid"] = company_uid
        if site_uid is not UNSET:
            field_dict["siteUid"] = site_uid
        if data_centers is not UNSET:
            field_dict["dataCenters"] = data_centers
        if is_failover_capabilities_enabled is not UNSET:
            field_dict["isFailoverCapabilitiesEnabled"] = is_failover_capabilities_enabled

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.company_site_vcd_replication_resource_data_center import (
            CompanySiteVcdReplicationResourceDataCenter,
        )

        d = dict(src_dict)
        _instance_uid = d.pop("instanceUid", UNSET)
        instance_uid: Union[Unset, UUID]
        if isinstance(_instance_uid, Unset):
            instance_uid = UNSET
        else:
            instance_uid = UUID(_instance_uid)

        _company_uid = d.pop("companyUid", UNSET)
        company_uid: Union[Unset, UUID]
        if isinstance(_company_uid, Unset):
            company_uid = UNSET
        else:
            company_uid = UUID(_company_uid)

        _site_uid = d.pop("siteUid", UNSET)
        site_uid: Union[Unset, UUID]
        if isinstance(_site_uid, Unset):
            site_uid = UNSET
        else:
            site_uid = UUID(_site_uid)

        data_centers = []
        _data_centers = d.pop("dataCenters", UNSET)
        for data_centers_item_data in _data_centers or []:
            data_centers_item = CompanySiteVcdReplicationResourceDataCenter.from_dict(data_centers_item_data)

            data_centers.append(data_centers_item)

        is_failover_capabilities_enabled = d.pop("isFailoverCapabilitiesEnabled", UNSET)

        company_site_vcd_replication_resource = cls(
            instance_uid=instance_uid,
            company_uid=company_uid,
            site_uid=site_uid,
            data_centers=data_centers,
            is_failover_capabilities_enabled=is_failover_capabilities_enabled,
        )

        company_site_vcd_replication_resource.additional_properties = d
        return company_site_vcd_replication_resource

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
