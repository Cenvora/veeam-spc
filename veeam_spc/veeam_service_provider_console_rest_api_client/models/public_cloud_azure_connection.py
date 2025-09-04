from collections.abc import Mapping
from typing import Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PublicCloudAzureConnection")


@_attrs_define
class PublicCloudAzureConnection:
    """
    Attributes:
        connection_uid (Union[Unset, UUID]): UID assigned to a Microsoft Azure connection.
    """

    connection_uid: Union[Unset, UUID] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        connection_uid: Union[Unset, str] = UNSET
        if not isinstance(self.connection_uid, Unset):
            connection_uid = str(self.connection_uid)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if connection_uid is not UNSET:
            field_dict["connectionUid"] = connection_uid

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _connection_uid = d.pop("connectionUid", UNSET)
        connection_uid: Union[Unset, UUID]
        if isinstance(_connection_uid, Unset):
            connection_uid = UNSET
        else:
            connection_uid = UUID(_connection_uid)

        public_cloud_azure_connection = cls(
            connection_uid=connection_uid,
        )

        public_cloud_azure_connection.additional_properties = d
        return public_cloud_azure_connection

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
