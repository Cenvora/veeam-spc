from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BackupServerVSphereChangedBlockTrackingSettingsType0")


@_attrs_define
class BackupServerVSphereChangedBlockTrackingSettingsType0:
    """Changed block tracking settings.

    Attributes:
        is_enabled (Union[Unset, bool]): Indicates whether CBT is enabled. Default: True.
        enable_cbt_automatically (Union[Unset, bool]): Indicates whether CBT is enabled for all processed VMs even if
            CBT is disabled in VM configuration.
            >CBT is used for VMs with virtual hardware version 7 or later.
            >VMs must not have existing snapshots.
             Default: True.
        reset_cbt_on_active_full (Union[Unset, bool]): Indicates whether CBT is reset before creating active full
            backups. Default: True.
    """

    is_enabled: Union[Unset, bool] = True
    enable_cbt_automatically: Union[Unset, bool] = True
    reset_cbt_on_active_full: Union[Unset, bool] = True
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        is_enabled = self.is_enabled

        enable_cbt_automatically = self.enable_cbt_automatically

        reset_cbt_on_active_full = self.reset_cbt_on_active_full

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if is_enabled is not UNSET:
            field_dict["isEnabled"] = is_enabled
        if enable_cbt_automatically is not UNSET:
            field_dict["enableCbtAutomatically"] = enable_cbt_automatically
        if reset_cbt_on_active_full is not UNSET:
            field_dict["resetCbtOnActiveFull"] = reset_cbt_on_active_full

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        is_enabled = d.pop("isEnabled", UNSET)

        enable_cbt_automatically = d.pop("enableCbtAutomatically", UNSET)

        reset_cbt_on_active_full = d.pop("resetCbtOnActiveFull", UNSET)

        backup_server_v_sphere_changed_block_tracking_settings_type_0 = cls(
            is_enabled=is_enabled,
            enable_cbt_automatically=enable_cbt_automatically,
            reset_cbt_on_active_full=reset_cbt_on_active_full,
        )

        backup_server_v_sphere_changed_block_tracking_settings_type_0.additional_properties = d
        return backup_server_v_sphere_changed_block_tracking_settings_type_0

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
