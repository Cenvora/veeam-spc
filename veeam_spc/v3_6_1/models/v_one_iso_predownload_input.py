from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.v_one_iso_predownload_input_predownload_type import VOneIsoPredownloadInputPredownloadType
from ..types import UNSET, Unset

T = TypeVar("T", bound="VOneIsoPredownloadInput")


@_attrs_define
class VOneIsoPredownloadInput:
    """Setup file predownload configuration.

    Attributes:
        path (str): Path to a target folder.
        predownload_type (Union[Unset, VOneIsoPredownloadInputPredownloadType]): Veeam ONE distribution type.
    """

    path: str
    predownload_type: Union[Unset, VOneIsoPredownloadInputPredownloadType] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        path = self.path

        predownload_type: Union[Unset, str] = UNSET
        if not isinstance(self.predownload_type, Unset):
            predownload_type = self.predownload_type.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "path": path,
            }
        )
        if predownload_type is not UNSET:
            field_dict["predownloadType"] = predownload_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        path = d.pop("path")

        _predownload_type = d.pop("predownloadType", UNSET)
        predownload_type: Union[Unset, VOneIsoPredownloadInputPredownloadType]
        if isinstance(_predownload_type, Unset):
            predownload_type = UNSET
        else:
            predownload_type = VOneIsoPredownloadInputPredownloadType(_predownload_type)

        v_one_iso_predownload_input = cls(
            path=path,
            predownload_type=predownload_type,
        )

        v_one_iso_predownload_input.additional_properties = d
        return v_one_iso_predownload_input

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
