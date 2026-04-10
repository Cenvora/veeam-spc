from collections.abc import Mapping
from typing import Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.measure_category import MeasureCategory
from ..types import UNSET, Unset

T = TypeVar("T", bound="PluginCharge")


@_attrs_define
class PluginCharge:
    """
    Attributes:
        plugin_id (Union[Unset, UUID]): ID assigned to a plugin.
        charge_uid (Union[Unset, UUID]): UID assigned to an external plugin charge rate.
        display_name (Union[Unset, str]): Name of an external plugin charge rate.
        category_id (Union[Unset, str]): ID assigned to a external plugin charge rate category.
        category_display_name (Union[Unset, str]): Name of an external plugin charge rate category.
        measure_category (Union[Unset, MeasureCategory]): Measurement unit category.
    """

    plugin_id: Union[Unset, UUID] = UNSET
    charge_uid: Union[Unset, UUID] = UNSET
    display_name: Union[Unset, str] = UNSET
    category_id: Union[Unset, str] = UNSET
    category_display_name: Union[Unset, str] = UNSET
    measure_category: Union[Unset, MeasureCategory] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        plugin_id: Union[Unset, str] = UNSET
        if not isinstance(self.plugin_id, Unset):
            plugin_id = str(self.plugin_id)

        charge_uid: Union[Unset, str] = UNSET
        if not isinstance(self.charge_uid, Unset):
            charge_uid = str(self.charge_uid)

        display_name = self.display_name

        category_id = self.category_id

        category_display_name = self.category_display_name

        measure_category: Union[Unset, str] = UNSET
        if not isinstance(self.measure_category, Unset):
            measure_category = self.measure_category.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if plugin_id is not UNSET:
            field_dict["pluginId"] = plugin_id
        if charge_uid is not UNSET:
            field_dict["chargeUid"] = charge_uid
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if category_id is not UNSET:
            field_dict["categoryId"] = category_id
        if category_display_name is not UNSET:
            field_dict["categoryDisplayName"] = category_display_name
        if measure_category is not UNSET:
            field_dict["measureCategory"] = measure_category

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _plugin_id = d.pop("pluginId", UNSET)
        plugin_id: Union[Unset, UUID]
        if isinstance(_plugin_id, Unset):
            plugin_id = UNSET
        else:
            plugin_id = UUID(_plugin_id)

        _charge_uid = d.pop("chargeUid", UNSET)
        charge_uid: Union[Unset, UUID]
        if isinstance(_charge_uid, Unset):
            charge_uid = UNSET
        else:
            charge_uid = UUID(_charge_uid)

        display_name = d.pop("displayName", UNSET)

        category_id = d.pop("categoryId", UNSET)

        category_display_name = d.pop("categoryDisplayName", UNSET)

        _measure_category = d.pop("measureCategory", UNSET)
        measure_category: Union[Unset, MeasureCategory]
        if isinstance(_measure_category, Unset):
            measure_category = UNSET
        else:
            measure_category = MeasureCategory(_measure_category)

        plugin_charge = cls(
            plugin_id=plugin_id,
            charge_uid=charge_uid,
            display_name=display_name,
            category_id=category_id,
            category_display_name=category_display_name,
            measure_category=measure_category,
        )

        plugin_charge.additional_properties = d
        return plugin_charge

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
