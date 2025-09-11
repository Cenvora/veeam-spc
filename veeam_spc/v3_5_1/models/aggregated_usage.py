from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.aggregated_usage_type import AggregatedUsageType
from ..types import UNSET, Unset

T = TypeVar("T", bound="AggregatedUsage")


@_attrs_define
class AggregatedUsage:
    """
    Attributes:
        value (Union[Unset, int]): Counter value.
        type_ (Union[Unset, AggregatedUsageType]): Counter type.
    """

    value: Union[Unset, int] = UNSET
    type_: Union[Unset, AggregatedUsageType] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        value = self.value

        type_: Union[Unset, str] = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if value is not UNSET:
            field_dict["value"] = value
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        value = d.pop("value", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: Union[Unset, AggregatedUsageType]
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = AggregatedUsageType(_type_)

        aggregated_usage = cls(
            value=value,
            type_=type_,
        )

        aggregated_usage.additional_properties = d
        return aggregated_usage

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
