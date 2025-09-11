from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="VbrPatchConfiguration")


@_attrs_define
class VbrPatchConfiguration:
    """
    Attributes:
        allow_auto_reboot (Union[Unset, bool]): Indicates whether a server must be automatically rebooted after the
            installation is complete.
        stop_all_activities (Union[Unset, bool]): Indicates whether all other tasks must be stopped during installation.
    """

    allow_auto_reboot: Union[Unset, bool] = UNSET
    stop_all_activities: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        allow_auto_reboot = self.allow_auto_reboot

        stop_all_activities = self.stop_all_activities

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if allow_auto_reboot is not UNSET:
            field_dict["allowAutoReboot"] = allow_auto_reboot
        if stop_all_activities is not UNSET:
            field_dict["stopAllActivities"] = stop_all_activities

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        allow_auto_reboot = d.pop("allowAutoReboot", UNSET)

        stop_all_activities = d.pop("stopAllActivities", UNSET)

        vbr_patch_configuration = cls(
            allow_auto_reboot=allow_auto_reboot,
            stop_all_activities=stop_all_activities,
        )

        vbr_patch_configuration.additional_properties = d
        return vbr_patch_configuration

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
