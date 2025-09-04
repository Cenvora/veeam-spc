from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BackupServerNotificationVmAttributeSettings")


@_attrs_define
class BackupServerNotificationVmAttributeSettings:
    """VM attribute settings.

    Attributes:
        is_enabled (bool): Indicates whether information about successfully performed backup is written to a VM
            attribute.
        notes (Union[Unset, str]): Name of a VM attribute.
        append_to_existing_value (Union[Unset, bool]): Indicates whether information about successfully performed backup
            is appended to the existing value of the attribute added by the user. Default: True.
    """

    is_enabled: bool
    notes: Union[Unset, str] = UNSET
    append_to_existing_value: Union[Unset, bool] = True
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        is_enabled = self.is_enabled

        notes = self.notes

        append_to_existing_value = self.append_to_existing_value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "isEnabled": is_enabled,
            }
        )
        if notes is not UNSET:
            field_dict["notes"] = notes
        if append_to_existing_value is not UNSET:
            field_dict["appendToExistingValue"] = append_to_existing_value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        is_enabled = d.pop("isEnabled")

        notes = d.pop("notes", UNSET)

        append_to_existing_value = d.pop("appendToExistingValue", UNSET)

        backup_server_notification_vm_attribute_settings = cls(
            is_enabled=is_enabled,
            notes=notes,
            append_to_existing_value=append_to_existing_value,
        )

        backup_server_notification_vm_attribute_settings.additional_properties = d
        return backup_server_notification_vm_attribute_settings

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
