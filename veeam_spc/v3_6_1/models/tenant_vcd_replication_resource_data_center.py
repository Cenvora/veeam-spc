from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TenantVcdReplicationResourceDataCenter")


@_attrs_define
class TenantVcdReplicationResourceDataCenter:
    """
    Attributes:
        data_center_uid (UUID): UID assigned to an organization VDC.
        is_wan_acceleration_enabled (Union[Unset, bool]): Indicates whether WAN acceleration is enabled. Default: False.
        wan_accelerator_uid (Union[None, UUID, Unset]): UID assigned to a WAN accelerator.
    """

    data_center_uid: UUID
    is_wan_acceleration_enabled: Union[Unset, bool] = False
    wan_accelerator_uid: Union[None, UUID, Unset] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data_center_uid = str(self.data_center_uid)

        is_wan_acceleration_enabled = self.is_wan_acceleration_enabled

        wan_accelerator_uid: Union[None, Unset, str]
        if isinstance(self.wan_accelerator_uid, Unset):
            wan_accelerator_uid = UNSET
        elif isinstance(self.wan_accelerator_uid, UUID):
            wan_accelerator_uid = str(self.wan_accelerator_uid)
        else:
            wan_accelerator_uid = self.wan_accelerator_uid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "dataCenterUid": data_center_uid,
            }
        )
        if is_wan_acceleration_enabled is not UNSET:
            field_dict["isWanAccelerationEnabled"] = is_wan_acceleration_enabled
        if wan_accelerator_uid is not UNSET:
            field_dict["wanAcceleratorUid"] = wan_accelerator_uid

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        data_center_uid = UUID(d.pop("dataCenterUid"))

        is_wan_acceleration_enabled = d.pop("isWanAccelerationEnabled", UNSET)

        def _parse_wan_accelerator_uid(data: object) -> Union[None, UUID, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                wan_accelerator_uid_type_0 = UUID(data)

                return wan_accelerator_uid_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID, Unset], data)

        wan_accelerator_uid = _parse_wan_accelerator_uid(d.pop("wanAcceleratorUid", UNSET))

        tenant_vcd_replication_resource_data_center = cls(
            data_center_uid=data_center_uid,
            is_wan_acceleration_enabled=is_wan_acceleration_enabled,
            wan_accelerator_uid=wan_accelerator_uid,
        )

        tenant_vcd_replication_resource_data_center.additional_properties = d
        return tenant_vcd_replication_resource_data_center

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
