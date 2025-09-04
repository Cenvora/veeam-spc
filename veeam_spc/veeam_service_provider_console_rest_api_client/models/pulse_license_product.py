from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pulse_license_product_workload import PulseLicenseProductWorkload


T = TypeVar("T", bound="PulseLicenseProduct")


@_attrs_define
class PulseLicenseProduct:
    """
    Attributes:
        product_id (Union[Unset, str]): ID assigned to a licensed Veeam product.
        name (Union[Unset, str]): Name of a licensed Veeam product.
        edition (Union[Unset, str]): Edition of a licensed Veeam product.
        version (Union[Unset, str]): Version of a licensed Veeam product.
        workloads (Union[Unset, list['PulseLicenseProductWorkload']]): Array of Veeam product workloads included in the
            VCSP Pulse license.
    """

    product_id: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    edition: Union[Unset, str] = UNSET
    version: Union[Unset, str] = UNSET
    workloads: Union[Unset, list["PulseLicenseProductWorkload"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        product_id = self.product_id

        name = self.name

        edition = self.edition

        version = self.version

        workloads: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.workloads, Unset):
            workloads = []
            for workloads_item_data in self.workloads:
                workloads_item = workloads_item_data.to_dict()
                workloads.append(workloads_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if product_id is not UNSET:
            field_dict["productId"] = product_id
        if name is not UNSET:
            field_dict["name"] = name
        if edition is not UNSET:
            field_dict["edition"] = edition
        if version is not UNSET:
            field_dict["version"] = version
        if workloads is not UNSET:
            field_dict["workloads"] = workloads

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.pulse_license_product_workload import PulseLicenseProductWorkload

        d = dict(src_dict)
        product_id = d.pop("productId", UNSET)

        name = d.pop("name", UNSET)

        edition = d.pop("edition", UNSET)

        version = d.pop("version", UNSET)

        workloads = []
        _workloads = d.pop("workloads", UNSET)
        for workloads_item_data in _workloads or []:
            workloads_item = PulseLicenseProductWorkload.from_dict(workloads_item_data)

            workloads.append(workloads_item)

        pulse_license_product = cls(
            product_id=product_id,
            name=name,
            edition=edition,
            version=version,
            workloads=workloads,
        )

        pulse_license_product.additional_properties = d
        return pulse_license_product

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
