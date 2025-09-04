from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.backup_server_public_cloud_appliance_platform_input import BackupServerPublicCloudAppliancePlatformInput

T = TypeVar("T", bound="CreatePublicCloudMultipartPatchInput")


@_attrs_define
class CreatePublicCloudMultipartPatchInput:
    """
    Attributes:
        file_name (str): Name of a patch file.
        platform (BackupServerPublicCloudAppliancePlatformInput): Platform of a Veeam Backup for Public Clouds
            appliance.
        file_size (int): Size of a patch file, in bytes.
    """

    file_name: str
    platform: BackupServerPublicCloudAppliancePlatformInput
    file_size: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        file_name = self.file_name

        platform = self.platform.value

        file_size = self.file_size

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "fileName": file_name,
                "platform": platform,
                "fileSize": file_size,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        file_name = d.pop("fileName")

        platform = BackupServerPublicCloudAppliancePlatformInput(d.pop("platform"))

        file_size = d.pop("fileSize")

        create_public_cloud_multipart_patch_input = cls(
            file_name=file_name,
            platform=platform,
            file_size=file_size,
        )

        create_public_cloud_multipart_patch_input.additional_properties = d
        return create_public_cloud_multipart_patch_input

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
