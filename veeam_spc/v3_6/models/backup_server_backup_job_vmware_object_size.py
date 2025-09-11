from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.backup_server_vmware_object import BackupServerVmwareObject


T = TypeVar("T", bound="BackupServerBackupJobVmwareObjectSize")


@_attrs_define
class BackupServerBackupJobVmwareObjectSize:
    """VMware vSphere object and its size.

    Attributes:
        inventory_object (BackupServerVmwareObject): VMware vSphere object.
        size (Union[Unset, str]): Storage space used by the VMware vSphere object.
    """

    inventory_object: "BackupServerVmwareObject"
    size: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        inventory_object = self.inventory_object.to_dict()

        size = self.size

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "inventoryObject": inventory_object,
            }
        )
        if size is not UNSET:
            field_dict["size"] = size

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.backup_server_vmware_object import BackupServerVmwareObject

        d = dict(src_dict)
        inventory_object = BackupServerVmwareObject.from_dict(d.pop("inventoryObject"))

        size = d.pop("size", UNSET)

        backup_server_backup_job_vmware_object_size = cls(
            inventory_object=inventory_object,
            size=size,
        )

        backup_server_backup_job_vmware_object_size.additional_properties = d
        return backup_server_backup_job_vmware_object_size

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
