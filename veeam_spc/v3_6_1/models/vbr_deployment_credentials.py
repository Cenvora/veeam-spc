from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="VbrDeploymentCredentials")


@_attrs_define
class VbrDeploymentCredentials:
    """
    Attributes:
        tenant_name (str): User name of a tenant account.
        tenant_password (str): Password of a tenant account.
    """

    tenant_name: str
    tenant_password: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        tenant_name = self.tenant_name

        tenant_password = self.tenant_password

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "tenantName": tenant_name,
                "tenantPassword": tenant_password,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        tenant_name = d.pop("tenantName")

        tenant_password = d.pop("tenantPassword")

        vbr_deployment_credentials = cls(
            tenant_name=tenant_name,
            tenant_password=tenant_password,
        )

        vbr_deployment_credentials.additional_properties = d
        return vbr_deployment_credentials

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
