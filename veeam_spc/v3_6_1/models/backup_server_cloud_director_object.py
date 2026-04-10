from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.backup_server_cloud_director_inventory_type import BackupServerCloudDirectorInventoryType
from ..types import UNSET, Unset

T = TypeVar("T", bound="BackupServerCloudDirectorObject")


@_attrs_define
class BackupServerCloudDirectorObject:
    """VMware Cloud Director object.

    Attributes:
        host_name (str): Name of a VMware Cloud Director server that manages an object.
        name (str): Name of an object.
        type_ (BackupServerCloudDirectorInventoryType): Type of a VMware Cloud Director object.
        object_id (Union[None, Unset, str]): URN of an object.
        size (Union[None, Unset, str]): Size of an object.
        vcd_organization_name (Union[None, Unset, str]): Name of a VMware Cloud Director organization.
        vcd_organization_uid (Union[None, UUID, Unset]): UID assigned to a VMware Cloud Director server.
    """

    host_name: str
    name: str
    type_: BackupServerCloudDirectorInventoryType
    object_id: Union[None, Unset, str] = UNSET
    size: Union[None, Unset, str] = UNSET
    vcd_organization_name: Union[None, Unset, str] = UNSET
    vcd_organization_uid: Union[None, UUID, Unset] = UNSET
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

        size: Union[None, Unset, str]
        if isinstance(self.size, Unset):
            size = UNSET
        else:
            size = self.size

        vcd_organization_name: Union[None, Unset, str]
        if isinstance(self.vcd_organization_name, Unset):
            vcd_organization_name = UNSET
        else:
            vcd_organization_name = self.vcd_organization_name

        vcd_organization_uid: Union[None, Unset, str]
        if isinstance(self.vcd_organization_uid, Unset):
            vcd_organization_uid = UNSET
        elif isinstance(self.vcd_organization_uid, UUID):
            vcd_organization_uid = str(self.vcd_organization_uid)
        else:
            vcd_organization_uid = self.vcd_organization_uid

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
        if size is not UNSET:
            field_dict["size"] = size
        if vcd_organization_name is not UNSET:
            field_dict["vcdOrganizationName"] = vcd_organization_name
        if vcd_organization_uid is not UNSET:
            field_dict["vcdOrganizationUid"] = vcd_organization_uid

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        host_name = d.pop("hostName")

        name = d.pop("name")

        type_ = BackupServerCloudDirectorInventoryType(d.pop("type"))

        def _parse_object_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        object_id = _parse_object_id(d.pop("objectId", UNSET))

        def _parse_size(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        size = _parse_size(d.pop("size", UNSET))

        def _parse_vcd_organization_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        vcd_organization_name = _parse_vcd_organization_name(d.pop("vcdOrganizationName", UNSET))

        def _parse_vcd_organization_uid(data: object) -> Union[None, UUID, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                vcd_organization_uid_type_0 = UUID(data)

                return vcd_organization_uid_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID, Unset], data)

        vcd_organization_uid = _parse_vcd_organization_uid(d.pop("vcdOrganizationUid", UNSET))

        backup_server_cloud_director_object = cls(
            host_name=host_name,
            name=name,
            type_=type_,
            object_id=object_id,
            size=size,
            vcd_organization_name=vcd_organization_name,
            vcd_organization_uid=vcd_organization_uid,
        )

        backup_server_cloud_director_object.additional_properties = d
        return backup_server_cloud_director_object

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
