from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.linux_shared_folder_target_target_type import LinuxSharedFolderTargetTargetType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.linux_common_credentials import LinuxCommonCredentials


T = TypeVar("T", bound="LinuxSharedFolderTarget")


@_attrs_define
class LinuxSharedFolderTarget:
    """
    Attributes:
        target_type (LinuxSharedFolderTargetTargetType): Type of a network shared folder. Default:
            LinuxSharedFolderTargetTargetType.NFS.
        path (str): Path to a network shared folder.'
        credentials (Union[Unset, LinuxCommonCredentials]):
    """

    path: str
    target_type: LinuxSharedFolderTargetTargetType = LinuxSharedFolderTargetTargetType.NFS
    credentials: Union[Unset, "LinuxCommonCredentials"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        target_type = self.target_type.value

        path = self.path

        credentials: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.credentials, Unset):
            credentials = self.credentials.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "targetType": target_type,
                "path": path,
            }
        )
        if credentials is not UNSET:
            field_dict["credentials"] = credentials

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.linux_common_credentials import LinuxCommonCredentials

        d = dict(src_dict)
        target_type = LinuxSharedFolderTargetTargetType(d.pop("targetType"))

        path = d.pop("path")

        _credentials = d.pop("credentials", UNSET)
        credentials: Union[Unset, LinuxCommonCredentials]
        if isinstance(_credentials, Unset):
            credentials = UNSET
        else:
            credentials = LinuxCommonCredentials.from_dict(_credentials)

        linux_shared_folder_target = cls(
            target_type=target_type,
            path=path,
            credentials=credentials,
        )

        linux_shared_folder_target.additional_properties = d
        return linux_shared_folder_target

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
