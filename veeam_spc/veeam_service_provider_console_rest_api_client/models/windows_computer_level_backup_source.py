from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="WindowsComputerLevelBackupSource")


@_attrs_define
class WindowsComputerLevelBackupSource:
    """
    Attributes:
        include_usb_drives (bool): Indicates whether external USB drives must be included in the backup.
            > USB flash drives are not supported.
    """

    include_usb_drives: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        include_usb_drives = self.include_usb_drives

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "includeUsbDrives": include_usb_drives,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        include_usb_drives = d.pop("includeUsbDrives")

        windows_computer_level_backup_source = cls(
            include_usb_drives=include_usb_drives,
        )

        windows_computer_level_backup_source.additional_properties = d
        return windows_computer_level_backup_source

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
