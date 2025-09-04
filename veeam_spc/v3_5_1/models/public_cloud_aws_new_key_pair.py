from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PublicCloudAwsNewKeyPair")


@_attrs_define
class PublicCloudAwsNewKeyPair:
    """
    Attributes:
        key_pair_name (str): Name of a key pair.
        private_key (str): Private key.
        file_name (str): Name of a file containing key.
    """

    key_pair_name: str
    private_key: str
    file_name: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        key_pair_name = self.key_pair_name

        private_key = self.private_key

        file_name = self.file_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "keyPairName": key_pair_name,
                "privateKey": private_key,
                "fileName": file_name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        key_pair_name = d.pop("keyPairName")

        private_key = d.pop("privateKey")

        file_name = d.pop("fileName")

        public_cloud_aws_new_key_pair = cls(
            key_pair_name=key_pair_name,
            private_key=private_key,
            file_name=file_name,
        )

        public_cloud_aws_new_key_pair.additional_properties = d
        return public_cloud_aws_new_key_pair

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
