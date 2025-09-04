from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PublicCloudAwsDataCenter")


@_attrs_define
class PublicCloudAwsDataCenter:
    """
    Attributes:
        data_center_id (Union[Unset, str]): ID assigned to an AWS datacenter.
        data_center_name (Union[Unset, str]): Name of an AWS datacenter.
    """

    data_center_id: Union[Unset, str] = UNSET
    data_center_name: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data_center_id = self.data_center_id

        data_center_name = self.data_center_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if data_center_id is not UNSET:
            field_dict["dataCenterId"] = data_center_id
        if data_center_name is not UNSET:
            field_dict["dataCenterName"] = data_center_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        data_center_id = d.pop("dataCenterId", UNSET)

        data_center_name = d.pop("dataCenterName", UNSET)

        public_cloud_aws_data_center = cls(
            data_center_id=data_center_id,
            data_center_name=data_center_name,
        )

        public_cloud_aws_data_center.additional_properties = d
        return public_cloud_aws_data_center

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
