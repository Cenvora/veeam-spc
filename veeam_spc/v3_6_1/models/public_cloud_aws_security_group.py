from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PublicCloudAwsSecurityGroup")


@_attrs_define
class PublicCloudAwsSecurityGroup:
    """
    Attributes:
        security_group_id (Union[Unset, str]): ID assigned to a security group.
        security_group_name (Union[Unset, str]): Name of a security group.
    """

    security_group_id: Union[Unset, str] = UNSET
    security_group_name: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        security_group_id = self.security_group_id

        security_group_name = self.security_group_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if security_group_id is not UNSET:
            field_dict["securityGroupId"] = security_group_id
        if security_group_name is not UNSET:
            field_dict["securityGroupName"] = security_group_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        security_group_id = d.pop("securityGroupId", UNSET)

        security_group_name = d.pop("securityGroupName", UNSET)

        public_cloud_aws_security_group = cls(
            security_group_id=security_group_id,
            security_group_name=security_group_name,
        )

        public_cloud_aws_security_group.additional_properties = d
        return public_cloud_aws_security_group

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
