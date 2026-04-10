from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.vdc_vault_data_center import VdcVaultDataCenter


T = TypeVar("T", bound="VdcVaultCountry")


@_attrs_define
class VdcVaultCountry:
    """
    Attributes:
        id (str | Unset): ID assigned to a country in Veeam Data Cloud Vault.
        name (str | Unset): Name of a country in Veeam Data Cloud Vault.
        data_centers (list[VdcVaultDataCenter] | Unset): Array of data centers assigned to a country in Veeam Data Cloud
            Vault.
    """

    id: str | Unset = UNSET
    name: str | Unset = UNSET
    data_centers: list[VdcVaultDataCenter] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        data_centers: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.data_centers, Unset):
            data_centers = []
            for data_centers_item_data in self.data_centers:
                data_centers_item = data_centers_item_data.to_dict()
                data_centers.append(data_centers_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if data_centers is not UNSET:
            field_dict["dataCenters"] = data_centers

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.vdc_vault_data_center import VdcVaultDataCenter

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        _data_centers = d.pop("dataCenters", UNSET)
        data_centers: list[VdcVaultDataCenter] | Unset = UNSET
        if _data_centers is not UNSET:
            data_centers = []
            for data_centers_item_data in _data_centers:
                data_centers_item = VdcVaultDataCenter.from_dict(data_centers_item_data)

                data_centers.append(data_centers_item)

        vdc_vault_country = cls(
            id=id,
            name=name,
            data_centers=data_centers,
        )

        vdc_vault_country.additional_properties = d
        return vdc_vault_country

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
