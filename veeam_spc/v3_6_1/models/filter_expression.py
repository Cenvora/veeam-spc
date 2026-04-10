from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.collation import Collation
from ..models.filter_expression_operation import FilterExpressionOperation
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.filter_expression_value_type_0 import FilterExpressionValueType0


T = TypeVar("T", bound="FilterExpression")


@_attrs_define
class FilterExpression:
    """
    Attributes:
        operation (FilterExpressionOperation): Filter operation.
        property_ (Union[None, Unset, str]): Path to the required resource property.
        items (Union[None, Unset, list['FilterExpression']]): Inner expressions. Can be used only with `and`, `or` and
            `not` operation.
        collation (Union[Unset, Collation]): Type of rules that determine how specified values are compared with
            resource property values.
        value (Union['FilterExpressionValueType0', None, Unset]): Resource property value.
    """

    operation: FilterExpressionOperation
    property_: Union[None, Unset, str] = UNSET
    items: Union[None, Unset, list["FilterExpression"]] = UNSET
    collation: Union[Unset, Collation] = UNSET
    value: Union["FilterExpressionValueType0", None, Unset] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.filter_expression_value_type_0 import FilterExpressionValueType0

        operation = self.operation.value

        property_: Union[None, Unset, str]
        if isinstance(self.property_, Unset):
            property_ = UNSET
        else:
            property_ = self.property_

        items: Union[None, Unset, list[dict[str, Any]]]
        if isinstance(self.items, Unset):
            items = UNSET
        elif isinstance(self.items, list):
            items = []
            for items_type_0_item_data in self.items:
                items_type_0_item = items_type_0_item_data.to_dict()
                items.append(items_type_0_item)

        else:
            items = self.items

        collation: Union[Unset, str] = UNSET
        if not isinstance(self.collation, Unset):
            collation = self.collation.value

        value: Union[None, Unset, dict[str, Any]]
        if isinstance(self.value, Unset):
            value = UNSET
        elif isinstance(self.value, FilterExpressionValueType0):
            value = self.value.to_dict()
        else:
            value = self.value

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
        from ..models.filter_expression_value_type_0 import FilterExpressionValueType0

        d = dict(src_dict)
        operation = FilterExpressionOperation(d.pop("operation"))

        def _parse_property_(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        property_ = _parse_property_(d.pop("property", UNSET))

        def _parse_items(data: object) -> Union[None, Unset, list["FilterExpression"]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                items_type_0 = []
                _items_type_0 = data
                for items_type_0_item_data in _items_type_0:
                    items_type_0_item = FilterExpression.from_dict(items_type_0_item_data)

                    items_type_0.append(items_type_0_item)

                return items_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list["FilterExpression"]], data)

        items = _parse_items(d.pop("items", UNSET))

        _collation = d.pop("collation", UNSET)
        collation: Union[Unset, Collation]
        if isinstance(_collation, Unset):
            collation = UNSET
        else:
            collation = Collation(_collation)

        def _parse_value(data: object) -> Union["FilterExpressionValueType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                value_type_0 = FilterExpressionValueType0.from_dict(data)

                return value_type_0
            except:  # noqa: E722
                pass
            return cast(Union["FilterExpressionValueType0", None, Unset], data)

        value = _parse_value(d.pop("value", UNSET))

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
