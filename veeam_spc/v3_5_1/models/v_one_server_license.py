import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.v_one_server_license_status import VOneServerLicenseStatus
from ..models.v_one_server_license_type import VOneServerLicenseType
from ..models.v_one_server_license_unit_type import VOneServerLicenseUnitType
from ..types import UNSET, Unset

T = TypeVar("T", bound="VOneServerLicense")


@_attrs_define
class VOneServerLicense:
    """
    Attributes:
        auto_update_enabled (bool): Indicates whether license updates automatically.
        v_one_server_uid (Union[Unset, UUID]): UID assigned to a Veeam ONE server.
        company (Union[Unset, str]): Name of an organization to which a license is issued.
        email (Union[Unset, str]): Email address of an organization to which a license is issued.
        expiration_date (Union[Unset, datetime.datetime]): License expiration date and time.
        support_expiration_date (Union[Unset, datetime.datetime]): Support expiration date and time.
        license_id (Union[Unset, UUID]): License ID.
        support_id (Union[Unset, str]): License ID required to contact Veeam Support.
        status (Union[Unset, VOneServerLicenseStatus]): Current status of the license.
        status_message (Union[Unset, str]): Status message.
        units (Union[Unset, float]): Number of available license units.
        used_units (Union[Unset, float]): Number of used license units.
        unit_type (Union[Unset, VOneServerLicenseUnitType]): Type of license units.
        type_ (Union[Unset, VOneServerLicenseType]): Type of the license.
    """

    auto_update_enabled: bool
    v_one_server_uid: Union[Unset, UUID] = UNSET
    company: Union[Unset, str] = UNSET
    email: Union[Unset, str] = UNSET
    expiration_date: Union[Unset, datetime.datetime] = UNSET
    support_expiration_date: Union[Unset, datetime.datetime] = UNSET
    license_id: Union[Unset, UUID] = UNSET
    support_id: Union[Unset, str] = UNSET
    status: Union[Unset, VOneServerLicenseStatus] = UNSET
    status_message: Union[Unset, str] = UNSET
    units: Union[Unset, float] = UNSET
    used_units: Union[Unset, float] = UNSET
    unit_type: Union[Unset, VOneServerLicenseUnitType] = UNSET
    type_: Union[Unset, VOneServerLicenseType] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        auto_update_enabled = self.auto_update_enabled

        v_one_server_uid: Union[Unset, str] = UNSET
        if not isinstance(self.v_one_server_uid, Unset):
            v_one_server_uid = str(self.v_one_server_uid)

        company = self.company

        email = self.email

        expiration_date: Union[Unset, str] = UNSET
        if not isinstance(self.expiration_date, Unset):
            expiration_date = self.expiration_date.isoformat()

        support_expiration_date: Union[Unset, str] = UNSET
        if not isinstance(self.support_expiration_date, Unset):
            support_expiration_date = self.support_expiration_date.isoformat()

        license_id: Union[Unset, str] = UNSET
        if not isinstance(self.license_id, Unset):
            license_id = str(self.license_id)

        support_id = self.support_id

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        status_message = self.status_message

        units = self.units

        used_units = self.used_units

        unit_type: Union[Unset, str] = UNSET
        if not isinstance(self.unit_type, Unset):
            unit_type = self.unit_type.value

        type_: Union[Unset, str] = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "autoUpdateEnabled": auto_update_enabled,
            }
        )
        if v_one_server_uid is not UNSET:
            field_dict["vOneServerUid"] = v_one_server_uid
        if company is not UNSET:
            field_dict["company"] = company
        if email is not UNSET:
            field_dict["email"] = email
        if expiration_date is not UNSET:
            field_dict["expirationDate"] = expiration_date
        if support_expiration_date is not UNSET:
            field_dict["supportExpirationDate"] = support_expiration_date
        if license_id is not UNSET:
            field_dict["licenseId"] = license_id
        if support_id is not UNSET:
            field_dict["supportId"] = support_id
        if status is not UNSET:
            field_dict["status"] = status
        if status_message is not UNSET:
            field_dict["statusMessage"] = status_message
        if units is not UNSET:
            field_dict["units"] = units
        if used_units is not UNSET:
            field_dict["usedUnits"] = used_units
        if unit_type is not UNSET:
            field_dict["unitType"] = unit_type
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        auto_update_enabled = d.pop("autoUpdateEnabled")

        _v_one_server_uid = d.pop("vOneServerUid", UNSET)
        v_one_server_uid: Union[Unset, UUID]
        if isinstance(_v_one_server_uid, Unset):
            v_one_server_uid = UNSET
        else:
            v_one_server_uid = UUID(_v_one_server_uid)

        company = d.pop("company", UNSET)

        email = d.pop("email", UNSET)

        _expiration_date = d.pop("expirationDate", UNSET)
        expiration_date: Union[Unset, datetime.datetime]
        if isinstance(_expiration_date, Unset):
            expiration_date = UNSET
        else:
            expiration_date = isoparse(_expiration_date)

        _support_expiration_date = d.pop("supportExpirationDate", UNSET)
        support_expiration_date: Union[Unset, datetime.datetime]
        if isinstance(_support_expiration_date, Unset):
            support_expiration_date = UNSET
        else:
            support_expiration_date = isoparse(_support_expiration_date)

        _license_id = d.pop("licenseId", UNSET)
        license_id: Union[Unset, UUID]
        if isinstance(_license_id, Unset):
            license_id = UNSET
        else:
            license_id = UUID(_license_id)

        support_id = d.pop("supportId", UNSET)

        _status = d.pop("status", UNSET)
        status: Union[Unset, VOneServerLicenseStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = VOneServerLicenseStatus(_status)

        status_message = d.pop("statusMessage", UNSET)

        units = d.pop("units", UNSET)

        used_units = d.pop("usedUnits", UNSET)

        _unit_type = d.pop("unitType", UNSET)
        unit_type: Union[Unset, VOneServerLicenseUnitType]
        if isinstance(_unit_type, Unset):
            unit_type = UNSET
        else:
            unit_type = VOneServerLicenseUnitType(_unit_type)

        _type_ = d.pop("type", UNSET)
        type_: Union[Unset, VOneServerLicenseType]
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = VOneServerLicenseType(_type_)

        v_one_server_license = cls(
            auto_update_enabled=auto_update_enabled,
            v_one_server_uid=v_one_server_uid,
            company=company,
            email=email,
            expiration_date=expiration_date,
            support_expiration_date=support_expiration_date,
            license_id=license_id,
            support_id=support_id,
            status=status,
            status_message=status_message,
            units=units,
            used_units=used_units,
            unit_type=unit_type,
            type_=type_,
        )

        v_one_server_license.additional_properties = d
        return v_one_server_license

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
