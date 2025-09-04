from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.backup_server_backup_job_exclusion_policy import BackupServerBackupJobExclusionPolicy
from ..types import UNSET, Unset

T = TypeVar("T", bound="BackupServerBackupJobBackupFSExclusionsType0")


@_attrs_define
class BackupServerBackupJobBackupFSExclusionsType0:
    """VM guest OS file exclusion.

    Attributes:
        exclusion_policy (BackupServerBackupJobExclusionPolicy): Exclusion type.
        items_list (Union[None, Unset, list[str]]): Array of included or excluded files and folders.
            >Full paths to files and folders, environmental variables and file masks with the asterisk (*) and question mark
            (?) characters can be used.
    """

    exclusion_policy: BackupServerBackupJobExclusionPolicy
    items_list: Union[None, Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        exclusion_policy = self.exclusion_policy.value

        items_list: Union[None, Unset, list[str]]
        if isinstance(self.items_list, Unset):
            items_list = UNSET
        elif isinstance(self.items_list, list):
            items_list = self.items_list

        else:
            items_list = self.items_list

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "exclusionPolicy": exclusion_policy,
            }
        )
        if items_list is not UNSET:
            field_dict["itemsList"] = items_list

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        exclusion_policy = BackupServerBackupJobExclusionPolicy(d.pop("exclusionPolicy"))

        def _parse_items_list(data: object) -> Union[None, Unset, list[str]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                items_list_type_0 = cast(list[str], data)

                return items_list_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[str]], data)

        items_list = _parse_items_list(d.pop("itemsList", UNSET))

        backup_server_backup_job_backup_fs_exclusions_type_0 = cls(
            exclusion_policy=exclusion_policy,
            items_list=items_list,
        )

        backup_server_backup_job_backup_fs_exclusions_type_0.additional_properties = d
        return backup_server_backup_job_backup_fs_exclusions_type_0

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
