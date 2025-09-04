from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.linux_oracle_archived_logs_truncation_config_truncation_mode import (
    LinuxOracleArchivedLogsTruncationConfigTruncationMode,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="LinuxOracleArchivedLogsTruncationConfig")


@_attrs_define
class LinuxOracleArchivedLogsTruncationConfig:
    """
    Attributes:
        truncation_mode (Union[Unset, LinuxOracleArchivedLogsTruncationConfigTruncationMode]): Archived log processing
            mode. Default: LinuxOracleArchivedLogsTruncationConfigTruncationMode.TRUNCATEDISABLED.
        size_gb (Union[Unset, int]): Maximum threshold for archived log file size, in GB. If an archived log file
            exceeds the limitation, it is deleted.
            > For the `TruncateBySize` archived log processing mode the property value must not be `0`.
             Default: 10.
        life_time_hours (Union[Unset, int]): Amount of time after which archived logs must be deleted, in hours.
            > For the `TruncateByAge` archived log processing mode the property value must not be `0`.
             Default: 24.
    """

    truncation_mode: Union[Unset, LinuxOracleArchivedLogsTruncationConfigTruncationMode] = (
        LinuxOracleArchivedLogsTruncationConfigTruncationMode.TRUNCATEDISABLED
    )
    size_gb: Union[Unset, int] = 10
    life_time_hours: Union[Unset, int] = 24
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        truncation_mode: Union[Unset, str] = UNSET
        if not isinstance(self.truncation_mode, Unset):
            truncation_mode = self.truncation_mode.value

        size_gb = self.size_gb

        life_time_hours = self.life_time_hours

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if truncation_mode is not UNSET:
            field_dict["truncationMode"] = truncation_mode
        if size_gb is not UNSET:
            field_dict["sizeGB"] = size_gb
        if life_time_hours is not UNSET:
            field_dict["lifeTimeHours"] = life_time_hours

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _truncation_mode = d.pop("truncationMode", UNSET)
        truncation_mode: Union[Unset, LinuxOracleArchivedLogsTruncationConfigTruncationMode]
        if isinstance(_truncation_mode, Unset):
            truncation_mode = UNSET
        else:
            truncation_mode = LinuxOracleArchivedLogsTruncationConfigTruncationMode(_truncation_mode)

        size_gb = d.pop("sizeGB", UNSET)

        life_time_hours = d.pop("lifeTimeHours", UNSET)

        linux_oracle_archived_logs_truncation_config = cls(
            truncation_mode=truncation_mode,
            size_gb=size_gb,
            life_time_hours=life_time_hours,
        )

        linux_oracle_archived_logs_truncation_config.additional_properties = d
        return linux_oracle_archived_logs_truncation_config

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
