from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.tenant_vcd_replication_resource_data_center import TenantVcdReplicationResourceDataCenter


T = TypeVar("T", bound="TenantVcdReplicationResource")


@_attrs_define
class TenantVcdReplicationResource:
    """
    Attributes:
        instance_uid (UUID | Unset): UID assigned to a VMware Cloud Director replication resource.
        tenant_uid (UUID | Unset): UID assigned to a tenant.
        company_uid (None | Unset | UUID): UID assigned to a company.
        site_uid (UUID | Unset): UID assigned to a Veeam Cloud Connect site.
        data_centers (list[TenantVcdReplicationResourceDataCenter] | Unset): Array of datacenters
        is_failover_capabilities_enabled (bool | Unset): Indicates whether performing failover is available to a
            company. Default: False.
    """

    instance_uid: UUID | Unset = UNSET
    tenant_uid: UUID | Unset = UNSET
    company_uid: None | Unset | UUID = UNSET
    site_uid: UUID | Unset = UNSET
    data_centers: list[TenantVcdReplicationResourceDataCenter] | Unset = UNSET
    is_failover_capabilities_enabled: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        instance_uid: str | Unset = UNSET
        if not isinstance(self.instance_uid, Unset):
            instance_uid = str(self.instance_uid)

        tenant_uid: str | Unset = UNSET
        if not isinstance(self.tenant_uid, Unset):
            tenant_uid = str(self.tenant_uid)

        company_uid: None | str | Unset
        if isinstance(self.company_uid, Unset):
            company_uid = UNSET
        elif isinstance(self.company_uid, UUID):
            company_uid = str(self.company_uid)
        else:
            company_uid = self.company_uid

        site_uid: str | Unset = UNSET
        if not isinstance(self.site_uid, Unset):
            site_uid = str(self.site_uid)

        data_centers: list[dict[str, Any]] | Unset = UNSET
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
        if tenant_uid is not UNSET:
            field_dict["tenantUid"] = tenant_uid
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
        from ..models.tenant_vcd_replication_resource_data_center import TenantVcdReplicationResourceDataCenter

        d = dict(src_dict)
        _instance_uid = d.pop("instanceUid", UNSET)
        instance_uid: UUID | Unset
        if isinstance(_instance_uid, Unset):
            instance_uid = UNSET
        else:
            instance_uid = UUID(_instance_uid)

        _tenant_uid = d.pop("tenantUid", UNSET)
        tenant_uid: UUID | Unset
        if isinstance(_tenant_uid, Unset):
            tenant_uid = UNSET
        else:
            tenant_uid = UUID(_tenant_uid)

        def _parse_company_uid(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                company_uid_type_0 = UUID(data)

                return company_uid_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        company_uid = _parse_company_uid(d.pop("companyUid", UNSET))

        _site_uid = d.pop("siteUid", UNSET)
        site_uid: UUID | Unset
        if isinstance(_site_uid, Unset):
            site_uid = UNSET
        else:
            site_uid = UUID(_site_uid)

        _data_centers = d.pop("dataCenters", UNSET)
        data_centers: list[TenantVcdReplicationResourceDataCenter] | Unset = UNSET
        if _data_centers is not UNSET:
            data_centers = []
            for data_centers_item_data in _data_centers:
                data_centers_item = TenantVcdReplicationResourceDataCenter.from_dict(data_centers_item_data)

                data_centers.append(data_centers_item)

        is_failover_capabilities_enabled = d.pop("isFailoverCapabilitiesEnabled", UNSET)

        tenant_vcd_replication_resource = cls(
            instance_uid=instance_uid,
            tenant_uid=tenant_uid,
            company_uid=company_uid,
            site_uid=site_uid,
            data_centers=data_centers,
            is_failover_capabilities_enabled=is_failover_capabilities_enabled,
        )

        tenant_vcd_replication_resource.additional_properties = d
        return tenant_vcd_replication_resource

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
