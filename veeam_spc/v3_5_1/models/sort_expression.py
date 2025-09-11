from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.collation import Collation
from ..models.sort_expression_direction import SortExpressionDirection
from ..types import UNSET, Unset

T = TypeVar("T", bound="SortExpression")


@_attrs_define
class SortExpression:
    """
    Attributes:
        property_ (str): Path to the required resource property.
        direction (SortExpressionDirection): Direction specifier. Default: SortExpressionDirection.ASCENDING.
        collation (Union[Unset, Collation]): Type of rules that determine how specified values are compared with
            resource property values.
    """

    property_: str
    direction: SortExpressionDirection = SortExpressionDirection.ASCENDING
    collation: Union[Unset, Collation] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        property_ = self.property_

        direction = self.direction.value

        collation: Union[Unset, str] = UNSET
        if not isinstance(self.collation, Unset):
            collation = self.collation.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "property": property_,
                "direction": direction,
            }
        )
        if collation is not UNSET:
            field_dict["collation"] = collation

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        property_ = d.pop("property")

        direction = SortExpressionDirection(d.pop("direction"))

        _collation = d.pop("collation", UNSET)
        collation: Union[Unset, Collation]
        if isinstance(_collation, Unset):
            collation = UNSET
        else:
            collation = Collation(_collation)

        sort_expression = cls(
            property_=property_,
            direction=direction,
            collation=collation,
        )

        sort_expression.additional_properties = d
        return sort_expression

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
