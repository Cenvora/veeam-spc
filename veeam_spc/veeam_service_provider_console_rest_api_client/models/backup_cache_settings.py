from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BackupCacheSettings")


@_attrs_define
class BackupCacheSettings:
    """
    Attributes:
        location (str): Path to the folder in which backup cache files must be stored.
        maximum_size_gb (Union[Unset, int]): Maximum size of the backup cache, in GB. Default: 10.
    """

    location: str
    maximum_size_gb: Union[Unset, int] = 10
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        location = self.location

        maximum_size_gb = self.maximum_size_gb

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "location": location,
            }
        )
        if maximum_size_gb is not UNSET:
            field_dict["maximumSizeGb"] = maximum_size_gb

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        location = d.pop("location")

        maximum_size_gb = d.pop("maximumSizeGb", UNSET)

        backup_cache_settings = cls(
            location=location,
            maximum_size_gb=maximum_size_gb,
        )

        backup_cache_settings.additional_properties = d
        return backup_cache_settings

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
