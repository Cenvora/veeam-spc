from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CompanyHostedServices")


@_attrs_define
class CompanyHostedServices:
    """
    Attributes:
        is_vb_public_cloud_management_enabled (Union[Unset, bool]): Indicates whether a company is allowed to manage
            public cloud appliances. Default: False.
    """

    is_vb_public_cloud_management_enabled: Union[Unset, bool] = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        is_vb_public_cloud_management_enabled = self.is_vb_public_cloud_management_enabled

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if is_vb_public_cloud_management_enabled is not UNSET:
            field_dict["isVbPublicCloudManagementEnabled"] = is_vb_public_cloud_management_enabled

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        is_vb_public_cloud_management_enabled = d.pop("isVbPublicCloudManagementEnabled", UNSET)

        company_hosted_services = cls(
            is_vb_public_cloud_management_enabled=is_vb_public_cloud_management_enabled,
        )

        company_hosted_services.additional_properties = d
        return company_hosted_services

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
