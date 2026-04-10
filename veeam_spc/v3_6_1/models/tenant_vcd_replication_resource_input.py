from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.tenant_vcd_replication_resource_data_center import TenantVcdReplicationResourceDataCenter


T = TypeVar("T", bound="TenantVcdReplicationResourceInput")


@_attrs_define
class TenantVcdReplicationResourceInput:
    """
    Attributes:
        data_centers (Union[Unset, list['TenantVcdReplicationResourceDataCenter']]): Array of organization VDCs.
        is_failover_capabilities_enabled (Union[Unset, bool]): Indicates whether performing failover is available to a
            company. Default: False.
    """

    data_centers: Union[Unset, list["TenantVcdReplicationResourceDataCenter"]] = UNSET
    is_failover_capabilities_enabled: Union[Unset, bool] = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
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
        if data_centers is not UNSET:
            field_dict["dataCenters"] = data_centers
        if is_failover_capabilities_enabled is not UNSET:
            field_dict["isFailoverCapabilitiesEnabled"] = is_failover_capabilities_enabled

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.tenant_vcd_replication_resource_data_center import TenantVcdReplicationResourceDataCenter

        d = dict(src_dict)
        data_centers = []
        _data_centers = d.pop("dataCenters", UNSET)
        for data_centers_item_data in _data_centers or []:
            data_centers_item = TenantVcdReplicationResourceDataCenter.from_dict(data_centers_item_data)

            data_centers.append(data_centers_item)

        is_failover_capabilities_enabled = d.pop("isFailoverCapabilitiesEnabled", UNSET)

        tenant_vcd_replication_resource_input = cls(
            data_centers=data_centers,
            is_failover_capabilities_enabled=is_failover_capabilities_enabled,
        )

        tenant_vcd_replication_resource_input.additional_properties = d
        return tenant_vcd_replication_resource_input

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
