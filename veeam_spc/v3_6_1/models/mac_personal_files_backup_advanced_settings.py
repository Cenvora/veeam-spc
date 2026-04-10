from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.mac_personal_files_backup_advanced_settings_inclusions_item import (
    MacPersonalFilesBackupAdvancedSettingsInclusionsItem,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="MacPersonalFilesBackupAdvancedSettings")


@_attrs_define
class MacPersonalFilesBackupAdvancedSettings:
    """
    Attributes:
        inclusions (list[MacPersonalFilesBackupAdvancedSettingsInclusionsItem]): Profile folders that must be included
            in the backup scope.
        exclude_network_account (Union[Unset, bool]): Exclude roaming user profiles from backup. Default: False.
    """

    inclusions: list[MacPersonalFilesBackupAdvancedSettingsInclusionsItem]
    exclude_network_account: Union[Unset, bool] = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        inclusions = []
        for inclusions_item_data in self.inclusions:
            inclusions_item = inclusions_item_data.value
            inclusions.append(inclusions_item)

        exclude_network_account = self.exclude_network_account

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "inclusions": inclusions,
            }
        )
        if exclude_network_account is not UNSET:
            field_dict["excludeNetworkAccount"] = exclude_network_account

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        inclusions = []
        _inclusions = d.pop("inclusions")
        for inclusions_item_data in _inclusions:
            inclusions_item = MacPersonalFilesBackupAdvancedSettingsInclusionsItem(inclusions_item_data)

            inclusions.append(inclusions_item)

        exclude_network_account = d.pop("excludeNetworkAccount", UNSET)

        mac_personal_files_backup_advanced_settings = cls(
            inclusions=inclusions,
            exclude_network_account=exclude_network_account,
        )

        mac_personal_files_backup_advanced_settings.additional_properties = d
        return mac_personal_files_backup_advanced_settings

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
