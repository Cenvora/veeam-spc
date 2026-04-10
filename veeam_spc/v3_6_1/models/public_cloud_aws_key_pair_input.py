from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PublicCloudAwsKeyPairInput")


@_attrs_define
class PublicCloudAwsKeyPairInput:
    """
    Attributes:
        connection_uid (UUID): UID assigned to an Amazon connection.
        name (str): Name of an EC2 key pair.
    """

    connection_uid: UUID
    name: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        connection_uid = str(self.connection_uid)

        name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "connectionUid": connection_uid,
                "name": name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        connection_uid = UUID(d.pop("connectionUid"))

        name = d.pop("name")

        public_cloud_aws_key_pair_input = cls(
            connection_uid=connection_uid,
            name=name,
        )

        public_cloud_aws_key_pair_input.additional_properties = d
        return public_cloud_aws_key_pair_input

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
