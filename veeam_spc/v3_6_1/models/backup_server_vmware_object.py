from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.backup_server_vmware_inventory_type import BackupServerVmwareInventoryType
from ..types import UNSET, Unset

T = TypeVar("T", bound="BackupServerVmwareObject")


@_attrs_define
class BackupServerVmwareObject:
    """VMware vSphere object.

    Attributes:
        host_name (str): Name of a VMware vSphere server that hosts the object.
        name (str): Name of the VMware vSphere object.
        type_ (BackupServerVmwareInventoryType): Type of a VMware vSphere object.
        object_id (Union[None, Unset, str]): URN assigned to a VMware vSphere object.
    """

    host_name: str
    name: str
    type_: BackupServerVmwareInventoryType
    object_id: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        host_name = self.host_name

        name = self.name

        type_ = self.type_.value

        object_id: Union[None, Unset, str]
        if isinstance(self.object_id, Unset):
            object_id = UNSET
        else:
            object_id = self.object_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "hostName": host_name,
                "name": name,
                "type": type_,
            }
        )
        if object_id is not UNSET:
            field_dict["objectId"] = object_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        host_name = d.pop("hostName")

        name = d.pop("name")

        type_ = BackupServerVmwareInventoryType(d.pop("type"))

        def _parse_object_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        object_id = _parse_object_id(d.pop("objectId", UNSET))

        backup_server_vmware_object = cls(
            host_name=host_name,
            name=name,
            type_=type_,
            object_id=object_id,
        )

        backup_server_vmware_object.additional_properties = d
        return backup_server_vmware_object

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
