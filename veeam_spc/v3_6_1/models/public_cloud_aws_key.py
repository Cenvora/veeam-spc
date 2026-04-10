from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PublicCloudAwsKey")


@_attrs_define
class PublicCloudAwsKey:
    """
    Attributes:
        key_pair_name (Union[Unset, str]): Name of a key pair.
    """

    key_pair_name: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        key_pair_name = self.key_pair_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if key_pair_name is not UNSET:
            field_dict["keyPairName"] = key_pair_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        key_pair_name = d.pop("keyPairName", UNSET)

        public_cloud_aws_key = cls(
            key_pair_name=key_pair_name,
        )

        public_cloud_aws_key.additional_properties = d
        return public_cloud_aws_key

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
