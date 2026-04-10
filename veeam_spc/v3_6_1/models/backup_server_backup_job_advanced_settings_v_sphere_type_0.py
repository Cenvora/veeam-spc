from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.backup_server_v_sphere_changed_block_tracking_settings_type_0 import (
        BackupServerVSphereChangedBlockTrackingSettingsType0,
    )


T = TypeVar("T", bound="BackupServerBackupJobAdvancedSettingsVSphereType0")


@_attrs_define
class BackupServerBackupJobAdvancedSettingsVSphereType0:
    """VMware vSphere settings.

    Attributes:
        enable_vm_ware_tools_quiescence (Union[Unset, bool]): Indicates whether VMware Tools quiescence is enabled for
            freezing the VM file system and application data. Default: False.
        changed_block_tracking (Union['BackupServerVSphereChangedBlockTrackingSettingsType0', None, Unset]): Changed
            block tracking settings.
    """

    enable_vm_ware_tools_quiescence: Union[Unset, bool] = False
    changed_block_tracking: Union["BackupServerVSphereChangedBlockTrackingSettingsType0", None, Unset] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.backup_server_v_sphere_changed_block_tracking_settings_type_0 import (
            BackupServerVSphereChangedBlockTrackingSettingsType0,
        )

        enable_vm_ware_tools_quiescence = self.enable_vm_ware_tools_quiescence

        changed_block_tracking: Union[None, Unset, dict[str, Any]]
        if isinstance(self.changed_block_tracking, Unset):
            changed_block_tracking = UNSET
        elif isinstance(self.changed_block_tracking, BackupServerVSphereChangedBlockTrackingSettingsType0):
            changed_block_tracking = self.changed_block_tracking.to_dict()
        else:
            changed_block_tracking = self.changed_block_tracking

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if enable_vm_ware_tools_quiescence is not UNSET:
            field_dict["enableVMWareToolsQuiescence"] = enable_vm_ware_tools_quiescence
        if changed_block_tracking is not UNSET:
            field_dict["changedBlockTracking"] = changed_block_tracking

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.backup_server_v_sphere_changed_block_tracking_settings_type_0 import (
            BackupServerVSphereChangedBlockTrackingSettingsType0,
        )

        d = dict(src_dict)
        enable_vm_ware_tools_quiescence = d.pop("enableVMWareToolsQuiescence", UNSET)

        def _parse_changed_block_tracking(
            data: object,
        ) -> Union["BackupServerVSphereChangedBlockTrackingSettingsType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_backup_server_v_sphere_changed_block_tracking_settings_type_0 = (
                    BackupServerVSphereChangedBlockTrackingSettingsType0.from_dict(data)
                )

                return componentsschemas_backup_server_v_sphere_changed_block_tracking_settings_type_0
            except:  # noqa: E722
                pass
            return cast(Union["BackupServerVSphereChangedBlockTrackingSettingsType0", None, Unset], data)

        changed_block_tracking = _parse_changed_block_tracking(d.pop("changedBlockTracking", UNSET))

        backup_server_backup_job_advanced_settings_v_sphere_type_0 = cls(
            enable_vm_ware_tools_quiescence=enable_vm_ware_tools_quiescence,
            changed_block_tracking=changed_block_tracking,
        )

        backup_server_backup_job_advanced_settings_v_sphere_type_0.additional_properties = d
        return backup_server_backup_job_advanced_settings_v_sphere_type_0

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
