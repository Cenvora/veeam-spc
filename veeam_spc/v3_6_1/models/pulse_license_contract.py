import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="PulseLicenseContract")


@_attrs_define
class PulseLicenseContract:
    """
    Attributes:
        contract_id (Union[Unset, str]): ID assigned to a rental agreement contract.
        expiration_date (Union[Unset, datetime.datetime]): Date of rental agreement contract expiration.
        points_limit (Union[None, Unset, float]): Maximum number of license points that can be consumed according to
            rental agreement contract.
        automatic_extension_always_on (Union[Unset, bool]): Indicates whether rental agreement contract must be
            automatically updated.
    """

    contract_id: Union[Unset, str] = UNSET
    expiration_date: Union[Unset, datetime.datetime] = UNSET
    points_limit: Union[None, Unset, float] = UNSET
    automatic_extension_always_on: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        contract_id = self.contract_id

        expiration_date: Union[Unset, str] = UNSET
        if not isinstance(self.expiration_date, Unset):
            expiration_date = self.expiration_date.isoformat()

        points_limit: Union[None, Unset, float]
        if isinstance(self.points_limit, Unset):
            points_limit = UNSET
        else:
            points_limit = self.points_limit

        automatic_extension_always_on = self.automatic_extension_always_on

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if contract_id is not UNSET:
            field_dict["contractId"] = contract_id
        if expiration_date is not UNSET:
            field_dict["expirationDate"] = expiration_date
        if points_limit is not UNSET:
            field_dict["pointsLimit"] = points_limit
        if automatic_extension_always_on is not UNSET:
            field_dict["automaticExtensionAlwaysOn"] = automatic_extension_always_on

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        contract_id = d.pop("contractId", UNSET)

        _expiration_date = d.pop("expirationDate", UNSET)
        expiration_date: Union[Unset, datetime.datetime]
        if isinstance(_expiration_date, Unset):
            expiration_date = UNSET
        else:
            expiration_date = isoparse(_expiration_date)

        def _parse_points_limit(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        points_limit = _parse_points_limit(d.pop("pointsLimit", UNSET))

        automatic_extension_always_on = d.pop("automaticExtensionAlwaysOn", UNSET)

        pulse_license_contract = cls(
            contract_id=contract_id,
            expiration_date=expiration_date,
            points_limit=points_limit,
            automatic_extension_always_on=automatic_extension_always_on,
        )

        pulse_license_contract.additional_properties = d
        return pulse_license_contract

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
