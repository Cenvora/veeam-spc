from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.backup_server_backup_gfs_policy_settings_weekly import BackupServerBackupGFSPolicySettingsWeekly
    from ..models.backup_server_backup_job_gfs_policy_settings_monthly import (
        BackupServerBackupJobGFSPolicySettingsMonthly,
    )
    from ..models.backup_server_backup_job_gfs_policy_settings_yearly import (
        BackupServerBackupJobGFSPolicySettingsYearly,
    )


T = TypeVar("T", bound="BackupServerBackupJobGFSPolicySettings")


@_attrs_define
class BackupServerBackupJobGFSPolicySettings:
    """Long-term retention policy settings.

    Attributes:
        is_enabled (bool): Indicates whether the long-term retention policy is enabled.
        weekly (Union[Unset, BackupServerBackupGFSPolicySettingsWeekly]): Weekly long-term retention policy settings.
        monthly (Union[Unset, BackupServerBackupJobGFSPolicySettingsMonthly]): Monthly long-term retention policy.
        yearly (Union[Unset, BackupServerBackupJobGFSPolicySettingsYearly]): Yearly long-term retention policy.
    """

    is_enabled: bool
    weekly: Union[Unset, "BackupServerBackupGFSPolicySettingsWeekly"] = UNSET
    monthly: Union[Unset, "BackupServerBackupJobGFSPolicySettingsMonthly"] = UNSET
    yearly: Union[Unset, "BackupServerBackupJobGFSPolicySettingsYearly"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        is_enabled = self.is_enabled

        weekly: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.weekly, Unset):
            weekly = self.weekly.to_dict()

        monthly: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.monthly, Unset):
            monthly = self.monthly.to_dict()

        yearly: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.yearly, Unset):
            yearly = self.yearly.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "isEnabled": is_enabled,
            }
        )
        if weekly is not UNSET:
            field_dict["weekly"] = weekly
        if monthly is not UNSET:
            field_dict["monthly"] = monthly
        if yearly is not UNSET:
            field_dict["yearly"] = yearly

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.backup_server_backup_gfs_policy_settings_weekly import BackupServerBackupGFSPolicySettingsWeekly
        from ..models.backup_server_backup_job_gfs_policy_settings_monthly import (
            BackupServerBackupJobGFSPolicySettingsMonthly,
        )
        from ..models.backup_server_backup_job_gfs_policy_settings_yearly import (
            BackupServerBackupJobGFSPolicySettingsYearly,
        )

        d = dict(src_dict)
        is_enabled = d.pop("isEnabled")

        _weekly = d.pop("weekly", UNSET)
        weekly: Union[Unset, BackupServerBackupGFSPolicySettingsWeekly]
        if isinstance(_weekly, Unset):
            weekly = UNSET
        else:
            weekly = BackupServerBackupGFSPolicySettingsWeekly.from_dict(_weekly)

        _monthly = d.pop("monthly", UNSET)
        monthly: Union[Unset, BackupServerBackupJobGFSPolicySettingsMonthly]
        if isinstance(_monthly, Unset):
            monthly = UNSET
        else:
            monthly = BackupServerBackupJobGFSPolicySettingsMonthly.from_dict(_monthly)

        _yearly = d.pop("yearly", UNSET)
        yearly: Union[Unset, BackupServerBackupJobGFSPolicySettingsYearly]
        if isinstance(_yearly, Unset):
            yearly = UNSET
        else:
            yearly = BackupServerBackupJobGFSPolicySettingsYearly.from_dict(_yearly)

        backup_server_backup_job_gfs_policy_settings = cls(
            is_enabled=is_enabled,
            weekly=weekly,
            monthly=monthly,
            yearly=yearly,
        )

        backup_server_backup_job_gfs_policy_settings.additional_properties = d
        return backup_server_backup_job_gfs_policy_settings

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
