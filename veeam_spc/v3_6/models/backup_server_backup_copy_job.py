from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.backup_server_backup_copy_job_retention_policy_type import BackupServerBackupCopyJobRetentionPolicyType
from ..models.backup_server_backup_copy_job_rpo_options_unit import BackupServerBackupCopyJobRpoOptionsUnit
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.embedded_for_backup_server_job_children import EmbeddedForBackupServerJobChildren


T = TypeVar("T", bound="BackupServerBackupCopyJob")


@_attrs_define
class BackupServerBackupCopyJob:
    """
    Attributes:
        instance_uid (Union[Unset, UUID]): UID assigned to a job in Veeam Backup & Replication.
        unique_uid (Union[Unset, UUID]): UID assigned to a job in Veeam Service Provider Console.
        target_repository_uid (Union[Unset, UUID]): UID assigned to a target repository.
        target_wan_accelerator_uid (Union[Unset, UUID]): UID assigned to a target WAN accelerator.
        source_wan_accelerator_uid (Union[Unset, UUID]): UID assigned to a source WAN accelerator.
        weekly_restore_points_to_keep (Union[Unset, int]): Number of weeks during which the weekly backup must be stored
            on the target repository.
        monthly_restore_points_to_keep (Union[Unset, int]): Number of months during which the monthly backup must be
            stored on the target repository.
        yearly_restore_points_to_keep (Union[Unset, int]): Number of years during which the yearly backup must be stored
            on the target repository.
        retention_policy_type (Union[Unset, BackupServerBackupCopyJobRetentionPolicyType]): Type of a retention policy
            of a backup copy job.
        is_rpo_options_enabled (Union[Unset, bool]): Indicates whether a warning is enabled in case backup copy job
            fails to complete within the specified RPO interval.
        rpo_options_value (Union[Unset, int]): Desired RPO interval value.
        rpo_options_unit (Union[Unset, BackupServerBackupCopyJobRpoOptionsUnit]): Measurement units of a desired RPO
            interval value.
        field_embedded (Union[Unset, EmbeddedForBackupServerJobChildren]): Resource representation of the related Veeam
            Backup & Replication server job entity.
    """

    instance_uid: Union[Unset, UUID] = UNSET
    unique_uid: Union[Unset, UUID] = UNSET
    target_repository_uid: Union[Unset, UUID] = UNSET
    target_wan_accelerator_uid: Union[Unset, UUID] = UNSET
    source_wan_accelerator_uid: Union[Unset, UUID] = UNSET
    weekly_restore_points_to_keep: Union[Unset, int] = UNSET
    monthly_restore_points_to_keep: Union[Unset, int] = UNSET
    yearly_restore_points_to_keep: Union[Unset, int] = UNSET
    retention_policy_type: Union[Unset, BackupServerBackupCopyJobRetentionPolicyType] = UNSET
    is_rpo_options_enabled: Union[Unset, bool] = UNSET
    rpo_options_value: Union[Unset, int] = UNSET
    rpo_options_unit: Union[Unset, BackupServerBackupCopyJobRpoOptionsUnit] = UNSET
    field_embedded: Union[Unset, "EmbeddedForBackupServerJobChildren"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        instance_uid: Union[Unset, str] = UNSET
        if not isinstance(self.instance_uid, Unset):
            instance_uid = str(self.instance_uid)

        unique_uid: Union[Unset, str] = UNSET
        if not isinstance(self.unique_uid, Unset):
            unique_uid = str(self.unique_uid)

        target_repository_uid: Union[Unset, str] = UNSET
        if not isinstance(self.target_repository_uid, Unset):
            target_repository_uid = str(self.target_repository_uid)

        target_wan_accelerator_uid: Union[Unset, str] = UNSET
        if not isinstance(self.target_wan_accelerator_uid, Unset):
            target_wan_accelerator_uid = str(self.target_wan_accelerator_uid)

        source_wan_accelerator_uid: Union[Unset, str] = UNSET
        if not isinstance(self.source_wan_accelerator_uid, Unset):
            source_wan_accelerator_uid = str(self.source_wan_accelerator_uid)

        weekly_restore_points_to_keep = self.weekly_restore_points_to_keep

        monthly_restore_points_to_keep = self.monthly_restore_points_to_keep

        yearly_restore_points_to_keep = self.yearly_restore_points_to_keep

        retention_policy_type: Union[Unset, str] = UNSET
        if not isinstance(self.retention_policy_type, Unset):
            retention_policy_type = self.retention_policy_type.value

        is_rpo_options_enabled = self.is_rpo_options_enabled

        rpo_options_value = self.rpo_options_value

        rpo_options_unit: Union[Unset, str] = UNSET
        if not isinstance(self.rpo_options_unit, Unset):
            rpo_options_unit = self.rpo_options_unit.value

        field_embedded: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.field_embedded, Unset):
            field_embedded = self.field_embedded.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if instance_uid is not UNSET:
            field_dict["instanceUid"] = instance_uid
        if unique_uid is not UNSET:
            field_dict["uniqueUid"] = unique_uid
        if target_repository_uid is not UNSET:
            field_dict["targetRepositoryUid"] = target_repository_uid
        if target_wan_accelerator_uid is not UNSET:
            field_dict["targetWanAcceleratorUid"] = target_wan_accelerator_uid
        if source_wan_accelerator_uid is not UNSET:
            field_dict["sourceWanAcceleratorUid"] = source_wan_accelerator_uid
        if weekly_restore_points_to_keep is not UNSET:
            field_dict["weeklyRestorePointsToKeep"] = weekly_restore_points_to_keep
        if monthly_restore_points_to_keep is not UNSET:
            field_dict["monthlyRestorePointsToKeep"] = monthly_restore_points_to_keep
        if yearly_restore_points_to_keep is not UNSET:
            field_dict["yearlyRestorePointsToKeep"] = yearly_restore_points_to_keep
        if retention_policy_type is not UNSET:
            field_dict["retentionPolicyType"] = retention_policy_type
        if is_rpo_options_enabled is not UNSET:
            field_dict["isRpoOptionsEnabled"] = is_rpo_options_enabled
        if rpo_options_value is not UNSET:
            field_dict["rpoOptionsValue"] = rpo_options_value
        if rpo_options_unit is not UNSET:
            field_dict["rpoOptionsUnit"] = rpo_options_unit
        if field_embedded is not UNSET:
            field_dict["_embedded"] = field_embedded

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.embedded_for_backup_server_job_children import EmbeddedForBackupServerJobChildren

        d = dict(src_dict)
        _instance_uid = d.pop("instanceUid", UNSET)
        instance_uid: Union[Unset, UUID]
        if isinstance(_instance_uid, Unset):
            instance_uid = UNSET
        else:
            instance_uid = UUID(_instance_uid)

        _unique_uid = d.pop("uniqueUid", UNSET)
        unique_uid: Union[Unset, UUID]
        if isinstance(_unique_uid, Unset):
            unique_uid = UNSET
        else:
            unique_uid = UUID(_unique_uid)

        _target_repository_uid = d.pop("targetRepositoryUid", UNSET)
        target_repository_uid: Union[Unset, UUID]
        if isinstance(_target_repository_uid, Unset):
            target_repository_uid = UNSET
        else:
            target_repository_uid = UUID(_target_repository_uid)

        _target_wan_accelerator_uid = d.pop("targetWanAcceleratorUid", UNSET)
        target_wan_accelerator_uid: Union[Unset, UUID]
        if isinstance(_target_wan_accelerator_uid, Unset):
            target_wan_accelerator_uid = UNSET
        else:
            target_wan_accelerator_uid = UUID(_target_wan_accelerator_uid)

        _source_wan_accelerator_uid = d.pop("sourceWanAcceleratorUid", UNSET)
        source_wan_accelerator_uid: Union[Unset, UUID]
        if isinstance(_source_wan_accelerator_uid, Unset):
            source_wan_accelerator_uid = UNSET
        else:
            source_wan_accelerator_uid = UUID(_source_wan_accelerator_uid)

        weekly_restore_points_to_keep = d.pop("weeklyRestorePointsToKeep", UNSET)

        monthly_restore_points_to_keep = d.pop("monthlyRestorePointsToKeep", UNSET)

        yearly_restore_points_to_keep = d.pop("yearlyRestorePointsToKeep", UNSET)

        _retention_policy_type = d.pop("retentionPolicyType", UNSET)
        retention_policy_type: Union[Unset, BackupServerBackupCopyJobRetentionPolicyType]
        if isinstance(_retention_policy_type, Unset):
            retention_policy_type = UNSET
        else:
            retention_policy_type = BackupServerBackupCopyJobRetentionPolicyType(_retention_policy_type)

        is_rpo_options_enabled = d.pop("isRpoOptionsEnabled", UNSET)

        rpo_options_value = d.pop("rpoOptionsValue", UNSET)

        _rpo_options_unit = d.pop("rpoOptionsUnit", UNSET)
        rpo_options_unit: Union[Unset, BackupServerBackupCopyJobRpoOptionsUnit]
        if isinstance(_rpo_options_unit, Unset):
            rpo_options_unit = UNSET
        else:
            rpo_options_unit = BackupServerBackupCopyJobRpoOptionsUnit(_rpo_options_unit)

        _field_embedded = d.pop("_embedded", UNSET)
        field_embedded: Union[Unset, EmbeddedForBackupServerJobChildren]
        if isinstance(_field_embedded, Unset):
            field_embedded = UNSET
        else:
            field_embedded = EmbeddedForBackupServerJobChildren.from_dict(_field_embedded)

        backup_server_backup_copy_job = cls(
            instance_uid=instance_uid,
            unique_uid=unique_uid,
            target_repository_uid=target_repository_uid,
            target_wan_accelerator_uid=target_wan_accelerator_uid,
            source_wan_accelerator_uid=source_wan_accelerator_uid,
            weekly_restore_points_to_keep=weekly_restore_points_to_keep,
            monthly_restore_points_to_keep=monthly_restore_points_to_keep,
            yearly_restore_points_to_keep=yearly_restore_points_to_keep,
            retention_policy_type=retention_policy_type,
            is_rpo_options_enabled=is_rpo_options_enabled,
            rpo_options_value=rpo_options_value,
            rpo_options_unit=rpo_options_unit,
            field_embedded=field_embedded,
        )

        backup_server_backup_copy_job.additional_properties = d
        return backup_server_backup_copy_job

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
