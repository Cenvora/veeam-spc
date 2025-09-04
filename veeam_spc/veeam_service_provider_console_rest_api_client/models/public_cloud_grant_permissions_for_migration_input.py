from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PublicCloudGrantPermissionsForMigrationInput")


@_attrs_define
class PublicCloudGrantPermissionsForMigrationInput:
    """
    Attributes:
        access_key (str): AWS access key.
        secret_key (str): AWS access secret key.
    """

    access_key: str
    secret_key: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        access_key = self.access_key

        secret_key = self.secret_key

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "accessKey": access_key,
                "secretKey": secret_key,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        access_key = d.pop("accessKey")

        secret_key = d.pop("secretKey")

        public_cloud_grant_permissions_for_migration_input = cls(
            access_key=access_key,
            secret_key=secret_key,
        )

        public_cloud_grant_permissions_for_migration_input.additional_properties = d
        return public_cloud_grant_permissions_for_migration_input

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
