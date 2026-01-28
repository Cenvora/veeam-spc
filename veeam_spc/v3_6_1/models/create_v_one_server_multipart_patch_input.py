from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.v_one_server_multipart_patch_file_input import VOneServerMultipartPatchFileInput


T = TypeVar("T", bound="CreateVOneServerMultipartPatchInput")


@_attrs_define
class CreateVOneServerMultipartPatchInput:
    """
    Attributes:
        files (list['VOneServerMultipartPatchFileInput']): Array of files included in a Veeam ONE server patch upload.
        stop_all_activities (bool): Indicates whether all Veeam ONE activities must be stopped before patch installation
            begins.
        reboot_automatically (bool): Indicates whether a Veeam ONE server must be rebooted after the patch installation
            is finished.
    """

    files: list["VOneServerMultipartPatchFileInput"]
    stop_all_activities: bool
    reboot_automatically: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        files = []
        for files_item_data in self.files:
            files_item = files_item_data.to_dict()
            files.append(files_item)

        stop_all_activities = self.stop_all_activities

        reboot_automatically = self.reboot_automatically

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "files": files,
                "stopAllActivities": stop_all_activities,
                "rebootAutomatically": reboot_automatically,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.v_one_server_multipart_patch_file_input import VOneServerMultipartPatchFileInput

        d = dict(src_dict)
        files = []
        _files = d.pop("files")
        for files_item_data in _files:
            files_item = VOneServerMultipartPatchFileInput.from_dict(files_item_data)

            files.append(files_item)

        stop_all_activities = d.pop("stopAllActivities")

        reboot_automatically = d.pop("rebootAutomatically")

        create_v_one_server_multipart_patch_input = cls(
            files=files,
            stop_all_activities=stop_all_activities,
            reboot_automatically=reboot_automatically,
        )

        create_v_one_server_multipart_patch_input.additional_properties = d
        return create_v_one_server_multipart_patch_input

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
