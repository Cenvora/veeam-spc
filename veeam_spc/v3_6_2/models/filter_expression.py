from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.collation import Collation
from ..models.filter_expression_operation import FilterExpressionOperation
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.filter_expression_value import FilterExpressionValue


T = TypeVar("T", bound="FilterExpression")


@_attrs_define
class FilterExpression:
    """
    Attributes:
        operation (FilterExpressionOperation): Filter operation.
        property_ (str | Unset): Path to the required resource property.
        items (list[FilterExpression] | Unset): Inner expressions. Can be used only with `and`, `or` and `not`
            operation.
        collation (Collation | Unset): Type of rules that determine how specified values are compared with resource
            property values.
        value (FilterExpressionValue | Unset): Resource property value.
    """

    operation: FilterExpressionOperation
    property_: str | Unset = UNSET
    items: list[FilterExpression] | Unset = UNSET
    collation: Collation | Unset = UNSET
    value: FilterExpressionValue | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        operation = self.operation.value

        property_ = self.property_

        items: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.items, Unset):
            items = []
            for items_item_data in self.items:
                items_item = items_item_data.to_dict()
                items.append(items_item)

        collation: str | Unset = UNSET
        if not isinstance(self.collation, Unset):
            collation = self.collation.value

        value: dict[str, Any] | Unset = UNSET
        if not isinstance(self.value, Unset):
            value = self.value.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "operation": operation,
            }
        )
        if property_ is not UNSET:
            field_dict["property"] = property_
        if items is not UNSET:
            field_dict["items"] = items
        if collation is not UNSET:
            field_dict["collation"] = collation
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.filter_expression_value import FilterExpressionValue

        d = dict(src_dict)
        operation = FilterExpressionOperation(d.pop("operation"))

        property_ = d.pop("property", UNSET)

        _items = d.pop("items", UNSET)
        items: list[FilterExpression] | Unset = UNSET
        if _items is not UNSET:
            items = []
            for items_item_data in _items:
                items_item = FilterExpression.from_dict(items_item_data)

                items.append(items_item)

        _collation = d.pop("collation", UNSET)
        collation: Collation | Unset
        if isinstance(_collation, Unset):
            collation = UNSET
        else:
            collation = Collation(_collation)

        _value = d.pop("value", UNSET)
        value: FilterExpressionValue | Unset
        if isinstance(_value, Unset):
            value = UNSET
        else:
            value = FilterExpressionValue.from_dict(_value)

        filter_expression = cls(
            operation=operation,
            property_=property_,
            items=items,
            collation=collation,
            value=value,
        )

        filter_expression.additional_properties = d
        return filter_expression

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
