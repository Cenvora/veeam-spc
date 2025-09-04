from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="VbrDeploymentDistributionSource")


@_attrs_define
class VbrDeploymentDistributionSource:
    """
    Attributes:
        file_path (str): Path to the Veeam Backup & Replication installation file.
        user_name (str): User name required to access the file.
        password (str): Password required to access the file.
    """

    file_path: str
    user_name: str
    password: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        file_path = self.file_path

        user_name = self.user_name

        password = self.password

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "filePath": file_path,
                "userName": user_name,
                "password": password,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        file_path = d.pop("filePath")

        user_name = d.pop("userName")

        password = d.pop("password")

        vbr_deployment_distribution_source = cls(
            file_path=file_path,
            user_name=user_name,
            password=password,
        )

        vbr_deployment_distribution_source.additional_properties = d
        return vbr_deployment_distribution_source

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
