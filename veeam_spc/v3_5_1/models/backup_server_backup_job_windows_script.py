from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BackupServerBackupJobWindowsScript")


@_attrs_define
class BackupServerBackupJobWindowsScript:
    """Paths to pre-freeze and post-thaw scripts for Microsoft Windows VMs.

    Attributes:
        pre_freeze_script (Union[Unset, str]): Path to a pre-freeze script.
        post_thaw_script (Union[Unset, str]): Path to a post-thaw script.
    """

    pre_freeze_script: Union[Unset, str] = UNSET
    post_thaw_script: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        pre_freeze_script = self.pre_freeze_script

        post_thaw_script = self.post_thaw_script

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if pre_freeze_script is not UNSET:
            field_dict["preFreezeScript"] = pre_freeze_script
        if post_thaw_script is not UNSET:
            field_dict["postThawScript"] = post_thaw_script

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        pre_freeze_script = d.pop("preFreezeScript", UNSET)

        post_thaw_script = d.pop("postThawScript", UNSET)

        backup_server_backup_job_windows_script = cls(
            pre_freeze_script=pre_freeze_script,
            post_thaw_script=post_thaw_script,
        )

        backup_server_backup_job_windows_script.additional_properties = d
        return backup_server_backup_job_windows_script

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
