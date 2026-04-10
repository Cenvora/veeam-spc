from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.backup_server_backup_job_gfs_policy_settings_yearly_type_0_desired_time import (
    BackupServerBackupJobGFSPolicySettingsYearlyType0DesiredTime,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="BackupServerBackupJobGFSPolicySettingsYearlyType0")


@_attrs_define
class BackupServerBackupJobGFSPolicySettingsYearlyType0:
    """Yearly long-term retention policy.

    Attributes:
        is_enabled (bool): Indicates whether the yearly GFS retention policy is enabled.
        keep_for_number_of_years (Union[None, Unset, int]): Number of years during which restore points must be stored.
        desired_time (Union[Unset, BackupServerBackupJobGFSPolicySettingsYearlyType0DesiredTime]): Month when the yearly
            restore point must be created.
    """

    is_enabled: bool
    keep_for_number_of_years: Union[None, Unset, int] = UNSET
    desired_time: Union[Unset, BackupServerBackupJobGFSPolicySettingsYearlyType0DesiredTime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        is_enabled = self.is_enabled

        keep_for_number_of_years: Union[None, Unset, int]
        if isinstance(self.keep_for_number_of_years, Unset):
            keep_for_number_of_years = UNSET
        else:
            keep_for_number_of_years = self.keep_for_number_of_years

        desired_time: Union[Unset, str] = UNSET
        if not isinstance(self.desired_time, Unset):
            desired_time = self.desired_time.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "isEnabled": is_enabled,
            }
        )
        if keep_for_number_of_years is not UNSET:
            field_dict["keepForNumberOfYears"] = keep_for_number_of_years
        if desired_time is not UNSET:
            field_dict["desiredTime"] = desired_time

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        is_enabled = d.pop("isEnabled")

        def _parse_keep_for_number_of_years(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        keep_for_number_of_years = _parse_keep_for_number_of_years(d.pop("keepForNumberOfYears", UNSET))

        _desired_time = d.pop("desiredTime", UNSET)
        desired_time: Union[Unset, BackupServerBackupJobGFSPolicySettingsYearlyType0DesiredTime]
        if isinstance(_desired_time, Unset):
            desired_time = UNSET
        else:
            desired_time = BackupServerBackupJobGFSPolicySettingsYearlyType0DesiredTime(_desired_time)

        backup_server_backup_job_gfs_policy_settings_yearly_type_0 = cls(
            is_enabled=is_enabled,
            keep_for_number_of_years=keep_for_number_of_years,
            desired_time=desired_time,
        )

        backup_server_backup_job_gfs_policy_settings_yearly_type_0.additional_properties = d
        return backup_server_backup_job_gfs_policy_settings_yearly_type_0

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
