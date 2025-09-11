import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.pulse_license_input_type import PulseLicenseInputType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pulse_license_workload_input import PulseLicenseWorkloadInput


T = TypeVar("T", bound="PulseLicenseInput")


@_attrs_define
class PulseLicenseInput:
    """
    Attributes:
        product_id (str): ID asigned to a Veeam product that requires a license.
        contract_id (str): ID assigned to a rental agreement contract.
        expiration_date (datetime.datetime): Date of the VCSP Pulse license expiration.
        workloads (list['PulseLicenseWorkloadInput']): Array of workloads that must be licensed.
        description (Union[Unset, str]): Description of a VCSP Pulse license.
        type_ (Union[Unset, PulseLicenseInputType]): Type of a VCSP Pulse license. Default:
            PulseLicenseInputType.RENTAL.
        is_automatic_reporting_enabled (Union[Unset, bool]): Defines whether automatic license reporting is enabled.
            Default: False.
    """

    product_id: str
    contract_id: str
    expiration_date: datetime.datetime
    workloads: list["PulseLicenseWorkloadInput"]
    description: Union[Unset, str] = UNSET
    type_: Union[Unset, PulseLicenseInputType] = PulseLicenseInputType.RENTAL
    is_automatic_reporting_enabled: Union[Unset, bool] = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        product_id = self.product_id

        contract_id = self.contract_id

        expiration_date = self.expiration_date.isoformat()

        workloads = []
        for workloads_item_data in self.workloads:
            workloads_item = workloads_item_data.to_dict()
            workloads.append(workloads_item)

        description = self.description

        type_: Union[Unset, str] = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        is_automatic_reporting_enabled = self.is_automatic_reporting_enabled

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "productId": product_id,
                "contractId": contract_id,
                "expirationDate": expiration_date,
                "workloads": workloads,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if type_ is not UNSET:
            field_dict["type"] = type_
        if is_automatic_reporting_enabled is not UNSET:
            field_dict["isAutomaticReportingEnabled"] = is_automatic_reporting_enabled

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.pulse_license_workload_input import PulseLicenseWorkloadInput

        d = dict(src_dict)
        product_id = d.pop("productId")

        contract_id = d.pop("contractId")

        expiration_date = isoparse(d.pop("expirationDate"))

        workloads = []
        _workloads = d.pop("workloads")
        for workloads_item_data in _workloads:
            workloads_item = PulseLicenseWorkloadInput.from_dict(workloads_item_data)

            workloads.append(workloads_item)

        description = d.pop("description", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: Union[Unset, PulseLicenseInputType]
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = PulseLicenseInputType(_type_)

        is_automatic_reporting_enabled = d.pop("isAutomaticReportingEnabled", UNSET)

        pulse_license_input = cls(
            product_id=product_id,
            contract_id=contract_id,
            expiration_date=expiration_date,
            workloads=workloads,
            description=description,
            type_=type_,
            is_automatic_reporting_enabled=is_automatic_reporting_enabled,
        )

        pulse_license_input.additional_properties = d
        return pulse_license_input

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
