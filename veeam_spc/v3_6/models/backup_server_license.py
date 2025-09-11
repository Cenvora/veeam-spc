import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.backup_server_license_cloud_connect import BackupServerLicenseCloudConnect
from ..models.backup_server_license_packages_item import BackupServerLicensePackagesItem
from ..models.backup_server_license_section_types_item import BackupServerLicenseSectionTypesItem
from ..models.backup_server_license_status import BackupServerLicenseStatus
from ..models.backup_server_license_type import BackupServerLicenseType
from ..models.backup_server_license_unit_type import BackupServerLicenseUnitType
from ..types import UNSET, Unset

T = TypeVar("T", bound="BackupServerLicense")


@_attrs_define
class BackupServerLicense:
    """
    Example:
        {'backupServerUid': 'DF997BD3-4AE9-4841-8152-8FF5CC703EAB', 'contactPerson': 'John Smith', 'edition':
            'Enterprise Plus', 'company': 'Veeam', 'email': 'John.Smith@veeam.com', 'units': 1000, 'unitType': 'Instances',
            'usedUnits': 100, 'status': 'Valid', 'cloudConnect': 'Yes', 'autoUpdateEnabled': True, 'packages': ['Suite'],
            'type': 'Rental', 'supportIds': ['987412365'], 'licenseIds': ['514c45eb-9543-4799-8003-1e59385b774c'],
            'expirationDate': '2018-10-24T14:00:00.0000000-07:00', 'supportExpirationDate':
            '2018-10-24T14:00:00.0000000-07:00'}

    Attributes:
        auto_update_enabled (bool): Indicates whether license updates automatically.
        backup_server_uid (Union[Unset, UUID]): UID assigned to a backup server.
        edition (Union[Unset, str]): License edition.
        monitoring (Union[Unset, bool]): Monitoring status.
        packages (Union[Unset, list[BackupServerLicensePackagesItem]]): Product packages.
        company (Union[Unset, str]): Name of an organization to which a license is issued.
        email (Union[Unset, str]): Email address of an organization to which a license is issued.
        contact_person (Union[Unset, str]): [Legacy] Name of a contact person in an organization to which the license is
            issued.
        expiration_date (Union[Unset, datetime.datetime]): License expiration date and time.
        support_expiration_date (Union[Unset, datetime.datetime]): Support expiration date and time.
        license_ids (Union[Unset, list[UUID]]): License IDs.
        support_ids (Union[Unset, list[str]]): License IDs required to contact Veeam Support.
        section_types (Union[Unset, list[BackupServerLicenseSectionTypesItem]]): Type of licensed units.
        status (Union[Unset, BackupServerLicenseStatus]): Current status of the license.
        cloud_connect (Union[Unset, BackupServerLicenseCloudConnect]): Indicates whether Veeam Cloud Connect is included
            in a license.
        sockets (Union[Unset, float]): Number of licensed sockets.
        used_sockets (Union[Unset, float]): Number of used sockets.
        capacity (Union[Unset, float]): Available protected capacity for NAS backup.
        used_capacity (Union[Unset, float]): Consumed capacity for NAS backup.
        units (Union[Unset, float]): Number of available license units.
        used_units (Union[Unset, float]): Number of used license units.
        unit_type (Union[Unset, BackupServerLicenseUnitType]): Type of license units.
        type_ (Union[Unset, BackupServerLicenseType]): Type of the license.
    """

    auto_update_enabled: bool
    backup_server_uid: Union[Unset, UUID] = UNSET
    edition: Union[Unset, str] = UNSET
    monitoring: Union[Unset, bool] = UNSET
    packages: Union[Unset, list[BackupServerLicensePackagesItem]] = UNSET
    company: Union[Unset, str] = UNSET
    email: Union[Unset, str] = UNSET
    contact_person: Union[Unset, str] = UNSET
    expiration_date: Union[Unset, datetime.datetime] = UNSET
    support_expiration_date: Union[Unset, datetime.datetime] = UNSET
    license_ids: Union[Unset, list[UUID]] = UNSET
    support_ids: Union[Unset, list[str]] = UNSET
    section_types: Union[Unset, list[BackupServerLicenseSectionTypesItem]] = UNSET
    status: Union[Unset, BackupServerLicenseStatus] = UNSET
    cloud_connect: Union[Unset, BackupServerLicenseCloudConnect] = UNSET
    sockets: Union[Unset, float] = UNSET
    used_sockets: Union[Unset, float] = UNSET
    capacity: Union[Unset, float] = UNSET
    used_capacity: Union[Unset, float] = UNSET
    units: Union[Unset, float] = UNSET
    used_units: Union[Unset, float] = UNSET
    unit_type: Union[Unset, BackupServerLicenseUnitType] = UNSET
    type_: Union[Unset, BackupServerLicenseType] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        auto_update_enabled = self.auto_update_enabled

        backup_server_uid: Union[Unset, str] = UNSET
        if not isinstance(self.backup_server_uid, Unset):
            backup_server_uid = str(self.backup_server_uid)

        edition = self.edition

        monitoring = self.monitoring

        packages: Union[Unset, list[str]] = UNSET
        if not isinstance(self.packages, Unset):
            packages = []
            for packages_item_data in self.packages:
                packages_item = packages_item_data.value
                packages.append(packages_item)

        company = self.company

        email = self.email

        contact_person = self.contact_person

        expiration_date: Union[Unset, str] = UNSET
        if not isinstance(self.expiration_date, Unset):
            expiration_date = self.expiration_date.isoformat()

        support_expiration_date: Union[Unset, str] = UNSET
        if not isinstance(self.support_expiration_date, Unset):
            support_expiration_date = self.support_expiration_date.isoformat()

        license_ids: Union[Unset, list[str]] = UNSET
        if not isinstance(self.license_ids, Unset):
            license_ids = []
            for license_ids_item_data in self.license_ids:
                license_ids_item = str(license_ids_item_data)
                license_ids.append(license_ids_item)

        support_ids: Union[Unset, list[str]] = UNSET
        if not isinstance(self.support_ids, Unset):
            support_ids = self.support_ids

        section_types: Union[Unset, list[str]] = UNSET
        if not isinstance(self.section_types, Unset):
            section_types = []
            for section_types_item_data in self.section_types:
                section_types_item = section_types_item_data.value
                section_types.append(section_types_item)

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        cloud_connect: Union[Unset, str] = UNSET
        if not isinstance(self.cloud_connect, Unset):
            cloud_connect = self.cloud_connect.value

        sockets = self.sockets

        used_sockets = self.used_sockets

        capacity = self.capacity

        used_capacity = self.used_capacity

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
        if backup_server_uid is not UNSET:
            field_dict["backupServerUid"] = backup_server_uid
        if edition is not UNSET:
            field_dict["edition"] = edition
        if monitoring is not UNSET:
            field_dict["monitoring"] = monitoring
        if packages is not UNSET:
            field_dict["packages"] = packages
        if company is not UNSET:
            field_dict["company"] = company
        if email is not UNSET:
            field_dict["email"] = email
        if contact_person is not UNSET:
            field_dict["contactPerson"] = contact_person
        if expiration_date is not UNSET:
            field_dict["expirationDate"] = expiration_date
        if support_expiration_date is not UNSET:
            field_dict["supportExpirationDate"] = support_expiration_date
        if license_ids is not UNSET:
            field_dict["licenseIds"] = license_ids
        if support_ids is not UNSET:
            field_dict["supportIds"] = support_ids
        if section_types is not UNSET:
            field_dict["sectionTypes"] = section_types
        if status is not UNSET:
            field_dict["status"] = status
        if cloud_connect is not UNSET:
            field_dict["cloudConnect"] = cloud_connect
        if sockets is not UNSET:
            field_dict["sockets"] = sockets
        if used_sockets is not UNSET:
            field_dict["usedSockets"] = used_sockets
        if capacity is not UNSET:
            field_dict["capacity"] = capacity
        if used_capacity is not UNSET:
            field_dict["usedCapacity"] = used_capacity
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

        _backup_server_uid = d.pop("backupServerUid", UNSET)
        backup_server_uid: Union[Unset, UUID]
        if isinstance(_backup_server_uid, Unset):
            backup_server_uid = UNSET
        else:
            backup_server_uid = UUID(_backup_server_uid)

        edition = d.pop("edition", UNSET)

        monitoring = d.pop("monitoring", UNSET)

        packages = []
        _packages = d.pop("packages", UNSET)
        for packages_item_data in _packages or []:
            packages_item = BackupServerLicensePackagesItem(packages_item_data)

            packages.append(packages_item)

        company = d.pop("company", UNSET)

        email = d.pop("email", UNSET)

        contact_person = d.pop("contactPerson", UNSET)

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

        license_ids = []
        _license_ids = d.pop("licenseIds", UNSET)
        for license_ids_item_data in _license_ids or []:
            license_ids_item = UUID(license_ids_item_data)

            license_ids.append(license_ids_item)

        support_ids = cast(list[str], d.pop("supportIds", UNSET))

        section_types = []
        _section_types = d.pop("sectionTypes", UNSET)
        for section_types_item_data in _section_types or []:
            section_types_item = BackupServerLicenseSectionTypesItem(section_types_item_data)

            section_types.append(section_types_item)

        _status = d.pop("status", UNSET)
        status: Union[Unset, BackupServerLicenseStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = BackupServerLicenseStatus(_status)

        _cloud_connect = d.pop("cloudConnect", UNSET)
        cloud_connect: Union[Unset, BackupServerLicenseCloudConnect]
        if isinstance(_cloud_connect, Unset):
            cloud_connect = UNSET
        else:
            cloud_connect = BackupServerLicenseCloudConnect(_cloud_connect)

        sockets = d.pop("sockets", UNSET)

        used_sockets = d.pop("usedSockets", UNSET)

        capacity = d.pop("capacity", UNSET)

        used_capacity = d.pop("usedCapacity", UNSET)

        units = d.pop("units", UNSET)

        used_units = d.pop("usedUnits", UNSET)

        _unit_type = d.pop("unitType", UNSET)
        unit_type: Union[Unset, BackupServerLicenseUnitType]
        if isinstance(_unit_type, Unset):
            unit_type = UNSET
        else:
            unit_type = BackupServerLicenseUnitType(_unit_type)

        _type_ = d.pop("type", UNSET)
        type_: Union[Unset, BackupServerLicenseType]
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = BackupServerLicenseType(_type_)

        backup_server_license = cls(
            auto_update_enabled=auto_update_enabled,
            backup_server_uid=backup_server_uid,
            edition=edition,
            monitoring=monitoring,
            packages=packages,
            company=company,
            email=email,
            contact_person=contact_person,
            expiration_date=expiration_date,
            support_expiration_date=support_expiration_date,
            license_ids=license_ids,
            support_ids=support_ids,
            section_types=section_types,
            status=status,
            cloud_connect=cloud_connect,
            sockets=sockets,
            used_sockets=used_sockets,
            capacity=capacity,
            used_capacity=used_capacity,
            units=units,
            used_units=used_units,
            unit_type=unit_type,
            type_=type_,
        )

        backup_server_license.additional_properties = d
        return backup_server_license

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
