from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.vb_365_server_license_status import Vb365ServerLicenseStatus
from ..models.vb_365_server_license_type import Vb365ServerLicenseType
from ..types import UNSET, Unset

T = TypeVar("T", bound="Vb365ServerLicense")


@_attrs_define
class Vb365ServerLicense:
    """
    Attributes:
        auto_update_enabled (bool): Indicates whether license updates automatically.
        vb_365_server_uid (UUID | Unset): UID assigned to a Veeam Backup for Microsoft 365 server.
        company (str | Unset): Name of an organization to which a license is issued.
        email (str | Unset): Email address of an organization to which a license is issued.
        expiration_date (datetime.datetime | None | Unset): License expiration date and time.
        support_expiration_date (datetime.datetime | None | Unset): Support expiration date and time.
        license_id (None | Unset | UUID): License ID.
        support_id (str | Unset): License ID required to contact Veeam Support.
        status (Vb365ServerLicenseStatus | Unset): Current status of the license.
        licensed_users (int | Unset): Number of licensed users.
        protected_users (int | Unset): Number of protected users.
        type_ (Vb365ServerLicenseType | Unset): Type of the license.
    """

    auto_update_enabled: bool
    vb_365_server_uid: UUID | Unset = UNSET
    company: str | Unset = UNSET
    email: str | Unset = UNSET
    expiration_date: datetime.datetime | None | Unset = UNSET
    support_expiration_date: datetime.datetime | None | Unset = UNSET
    license_id: None | Unset | UUID = UNSET
    support_id: str | Unset = UNSET
    status: Vb365ServerLicenseStatus | Unset = UNSET
    licensed_users: int | Unset = UNSET
    protected_users: int | Unset = UNSET
    type_: Vb365ServerLicenseType | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        auto_update_enabled = self.auto_update_enabled

        vb_365_server_uid: str | Unset = UNSET
        if not isinstance(self.vb_365_server_uid, Unset):
            vb_365_server_uid = str(self.vb_365_server_uid)

        company = self.company

        email = self.email

        expiration_date: None | str | Unset
        if isinstance(self.expiration_date, Unset):
            expiration_date = UNSET
        elif isinstance(self.expiration_date, datetime.datetime):
            expiration_date = self.expiration_date.isoformat()
        else:
            expiration_date = self.expiration_date

        support_expiration_date: None | str | Unset
        if isinstance(self.support_expiration_date, Unset):
            support_expiration_date = UNSET
        elif isinstance(self.support_expiration_date, datetime.datetime):
            support_expiration_date = self.support_expiration_date.isoformat()
        else:
            support_expiration_date = self.support_expiration_date

        license_id: None | str | Unset
        if isinstance(self.license_id, Unset):
            license_id = UNSET
        elif isinstance(self.license_id, UUID):
            license_id = str(self.license_id)
        else:
            license_id = self.license_id

        support_id = self.support_id

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        licensed_users = self.licensed_users

        protected_users = self.protected_users

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "autoUpdateEnabled": auto_update_enabled,
            }
        )
        if vb_365_server_uid is not UNSET:
            field_dict["vb365ServerUid"] = vb_365_server_uid
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
        if licensed_users is not UNSET:
            field_dict["licensedUsers"] = licensed_users
        if protected_users is not UNSET:
            field_dict["protectedUsers"] = protected_users
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        auto_update_enabled = d.pop("autoUpdateEnabled")

        _vb_365_server_uid = d.pop("vb365ServerUid", UNSET)
        vb_365_server_uid: UUID | Unset
        if isinstance(_vb_365_server_uid, Unset):
            vb_365_server_uid = UNSET
        else:
            vb_365_server_uid = UUID(_vb_365_server_uid)

        company = d.pop("company", UNSET)

        email = d.pop("email", UNSET)

        def _parse_expiration_date(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                expiration_date_type_0 = isoparse(data)

                return expiration_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        expiration_date = _parse_expiration_date(d.pop("expirationDate", UNSET))

        def _parse_support_expiration_date(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                support_expiration_date_type_0 = isoparse(data)

                return support_expiration_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        support_expiration_date = _parse_support_expiration_date(d.pop("supportExpirationDate", UNSET))

        def _parse_license_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                license_id_type_0 = UUID(data)

                return license_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        license_id = _parse_license_id(d.pop("licenseId", UNSET))

        support_id = d.pop("supportId", UNSET)

        _status = d.pop("status", UNSET)
        status: Vb365ServerLicenseStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = Vb365ServerLicenseStatus(_status)

        licensed_users = d.pop("licensedUsers", UNSET)

        protected_users = d.pop("protectedUsers", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: Vb365ServerLicenseType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = Vb365ServerLicenseType(_type_)

        vb_365_server_license = cls(
            auto_update_enabled=auto_update_enabled,
            vb_365_server_uid=vb_365_server_uid,
            company=company,
            email=email,
            expiration_date=expiration_date,
            support_expiration_date=support_expiration_date,
            license_id=license_id,
            support_id=support_id,
            status=status,
            licensed_users=licensed_users,
            protected_users=protected_users,
            type_=type_,
        )

        vb_365_server_license.additional_properties = d
        return vb_365_server_license

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
