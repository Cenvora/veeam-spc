from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Vb365BackupWindowSettings")


@_attrs_define
class Vb365BackupWindowSettings:
    """
    Attributes:
        backup_window (list[bool]): Defines an hourly scheme for the backup window. The scheduling scheme consists of
            168 boolean elements.
            These elements can be logically divided into 7 groups by 24. Each group represents a day of the week starting
            from Sunday.
            Each element represents a backup hours: `true` — backup is allowed, `false` — backup is not allowed.
        minute_offset (Union[Unset, int]): Number of minutes that must be skipped after specified job starting time.
    """

    backup_window: list[bool]
    minute_offset: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        backup_window = self.backup_window

        minute_offset = self.minute_offset

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "backupWindow": backup_window,
            }
        )
        if minute_offset is not UNSET:
            field_dict["minuteOffset"] = minute_offset

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        backup_window = cast(list[bool], d.pop("backupWindow"))

        minute_offset = d.pop("minuteOffset", UNSET)

        vb_365_backup_window_settings = cls(
            backup_window=backup_window,
            minute_offset=minute_offset,
        )

        vb_365_backup_window_settings.additional_properties = d
        return vb_365_backup_window_settings

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
