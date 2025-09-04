import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.console_license_cloud_connect import ConsoleLicenseCloudConnect
from ..models.console_license_last_update_status import ConsoleLicenseLastUpdateStatus
from ..models.console_license_package import ConsoleLicensePackage
from ..models.console_license_status import ConsoleLicenseStatus
from ..models.console_license_type import ConsoleLicenseType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ConsoleLicense")


@_attrs_define
class ConsoleLicense:
    """
    Example:
        {'licenseId': '514c45eb-9543-4799-8003-1e59385b774c', 'contactPerson': 'John Smith', 'edition': 'Enterprise
            Plus', 'package': 'Suite', 'licenseeCompany': 'Veeam', 'licenseeEmail': 'John.Smith@veeam.com',
            'licenseeAdministratorEmail': 'Adam.Jang@veeam.com', 'instances': 1000, 'status': 'Valid', 'type': 'Rental',
            'cloudConnect': 'Yes', 'supportId': 987412365, 'expirationDate': datetime.datetime(2018, 10, 24, 23, 0,
            tzinfo=datetime.timezone(datetime.timedelta(seconds=7200), '+02:00')), 'supportExpirationDate':
            datetime.datetime(2018, 10, 24, 23, 0, tzinfo=datetime.timezone(datetime.timedelta(seconds=7200), '+02:00')),
            'lastUpdateDate': datetime.datetime(2019, 10, 24, 23, 0,
            tzinfo=datetime.timezone(datetime.timedelta(seconds=7200), '+02:00')), 'lastUpdateMessage': '',
            'lastUpdateState': 'Unknown'}

    Attributes:
        license_id (Union[Unset, str]): License ID.
        edition (Union[Unset, str]): License edition.
        package (Union[Unset, ConsoleLicensePackage]): Product packages.
        licensee_company (Union[Unset, str]): Name of an organization to which a license is issued.
        licensee_email (Union[Unset, str]): Email address of a contact person in an organization.
        licensee_administrator_email (Union[Unset, str]): Email address of a license administrator in a company.
        contact_person (Union[Unset, str]): [Legacy] Name of a contact person in an organization to which the license is
            issued.
        expiration_date (Union[Unset, datetime.datetime]): License expiration date and time.
        support_expiration_date (Union[Unset, datetime.datetime]): Support expiration date and time.
        support_id (Union[Unset, str]): Support ID required for contacting Veeam Support.
        status (Union[Unset, ConsoleLicenseStatus]): Current status of the license.
        status_message (Union[Unset, str]): Description of a license status.
        cloud_connect (Union[Unset, ConsoleLicenseCloudConnect]): Indicates whether a license includes Veeam Cloud
            Connect.
        instances (Union[Unset, float]): Total number of available instances.
        type_ (Union[Unset, ConsoleLicenseType]): Type of a license.
        last_update_date (Union[Unset, datetime.datetime]): Date and time when license was last updated.
        last_update_message (Union[Unset, str]): Message to the last license update.
        last_update_status (Union[Unset, ConsoleLicenseLastUpdateStatus]): Status of the last license update.
    """

    license_id: Union[Unset, str] = UNSET
    edition: Union[Unset, str] = UNSET
    package: Union[Unset, ConsoleLicensePackage] = UNSET
    licensee_company: Union[Unset, str] = UNSET
    licensee_email: Union[Unset, str] = UNSET
    licensee_administrator_email: Union[Unset, str] = UNSET
    contact_person: Union[Unset, str] = UNSET
    expiration_date: Union[Unset, datetime.datetime] = UNSET
    support_expiration_date: Union[Unset, datetime.datetime] = UNSET
    support_id: Union[Unset, str] = UNSET
    status: Union[Unset, ConsoleLicenseStatus] = UNSET
    status_message: Union[Unset, str] = UNSET
    cloud_connect: Union[Unset, ConsoleLicenseCloudConnect] = UNSET
    instances: Union[Unset, float] = UNSET
    type_: Union[Unset, ConsoleLicenseType] = UNSET
    last_update_date: Union[Unset, datetime.datetime] = UNSET
    last_update_message: Union[Unset, str] = UNSET
    last_update_status: Union[Unset, ConsoleLicenseLastUpdateStatus] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        license_id = self.license_id

        edition = self.edition

        package: Union[Unset, str] = UNSET
        if not isinstance(self.package, Unset):
            package = self.package.value

        licensee_company = self.licensee_company

        licensee_email = self.licensee_email

        licensee_administrator_email = self.licensee_administrator_email

        contact_person = self.contact_person

        expiration_date: Union[Unset, str] = UNSET
        if not isinstance(self.expiration_date, Unset):
            expiration_date = self.expiration_date.isoformat()

        support_expiration_date: Union[Unset, str] = UNSET
        if not isinstance(self.support_expiration_date, Unset):
            support_expiration_date = self.support_expiration_date.isoformat()

        support_id = self.support_id

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        status_message = self.status_message

        cloud_connect: Union[Unset, str] = UNSET
        if not isinstance(self.cloud_connect, Unset):
            cloud_connect = self.cloud_connect.value

        instances = self.instances

        type_: Union[Unset, str] = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        last_update_date: Union[Unset, str] = UNSET
        if not isinstance(self.last_update_date, Unset):
            last_update_date = self.last_update_date.isoformat()

        last_update_message = self.last_update_message

        last_update_status: Union[Unset, str] = UNSET
        if not isinstance(self.last_update_status, Unset):
            last_update_status = self.last_update_status.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if license_id is not UNSET:
            field_dict["licenseId"] = license_id
        if edition is not UNSET:
            field_dict["edition"] = edition
        if package is not UNSET:
            field_dict["package"] = package
        if licensee_company is not UNSET:
            field_dict["licenseeCompany"] = licensee_company
        if licensee_email is not UNSET:
            field_dict["licenseeEmail"] = licensee_email
        if licensee_administrator_email is not UNSET:
            field_dict["licenseeAdministratorEmail"] = licensee_administrator_email
        if contact_person is not UNSET:
            field_dict["contactPerson"] = contact_person
        if expiration_date is not UNSET:
            field_dict["expirationDate"] = expiration_date
        if support_expiration_date is not UNSET:
            field_dict["supportExpirationDate"] = support_expiration_date
        if support_id is not UNSET:
            field_dict["supportId"] = support_id
        if status is not UNSET:
            field_dict["status"] = status
        if status_message is not UNSET:
            field_dict["statusMessage"] = status_message
        if cloud_connect is not UNSET:
            field_dict["cloudConnect"] = cloud_connect
        if instances is not UNSET:
            field_dict["instances"] = instances
        if type_ is not UNSET:
            field_dict["type"] = type_
        if last_update_date is not UNSET:
            field_dict["lastUpdateDate"] = last_update_date
        if last_update_message is not UNSET:
            field_dict["lastUpdateMessage"] = last_update_message
        if last_update_status is not UNSET:
            field_dict["lastUpdateStatus"] = last_update_status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        license_id = d.pop("licenseId", UNSET)

        edition = d.pop("edition", UNSET)

        _package = d.pop("package", UNSET)
        package: Union[Unset, ConsoleLicensePackage]
        if isinstance(_package, Unset):
            package = UNSET
        else:
            package = ConsoleLicensePackage(_package)

        licensee_company = d.pop("licenseeCompany", UNSET)

        licensee_email = d.pop("licenseeEmail", UNSET)

        licensee_administrator_email = d.pop("licenseeAdministratorEmail", UNSET)

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

        support_id = d.pop("supportId", UNSET)

        _status = d.pop("status", UNSET)
        status: Union[Unset, ConsoleLicenseStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = ConsoleLicenseStatus(_status)

        status_message = d.pop("statusMessage", UNSET)

        _cloud_connect = d.pop("cloudConnect", UNSET)
        cloud_connect: Union[Unset, ConsoleLicenseCloudConnect]
        if isinstance(_cloud_connect, Unset):
            cloud_connect = UNSET
        else:
            cloud_connect = ConsoleLicenseCloudConnect(_cloud_connect)

        instances = d.pop("instances", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: Union[Unset, ConsoleLicenseType]
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = ConsoleLicenseType(_type_)

        _last_update_date = d.pop("lastUpdateDate", UNSET)
        last_update_date: Union[Unset, datetime.datetime]
        if isinstance(_last_update_date, Unset):
            last_update_date = UNSET
        else:
            last_update_date = isoparse(_last_update_date)

        last_update_message = d.pop("lastUpdateMessage", UNSET)

        _last_update_status = d.pop("lastUpdateStatus", UNSET)
        last_update_status: Union[Unset, ConsoleLicenseLastUpdateStatus]
        if isinstance(_last_update_status, Unset):
            last_update_status = UNSET
        else:
            last_update_status = ConsoleLicenseLastUpdateStatus(_last_update_status)

        console_license = cls(
            license_id=license_id,
            edition=edition,
            package=package,
            licensee_company=licensee_company,
            licensee_email=licensee_email,
            licensee_administrator_email=licensee_administrator_email,
            contact_person=contact_person,
            expiration_date=expiration_date,
            support_expiration_date=support_expiration_date,
            support_id=support_id,
            status=status,
            status_message=status_message,
            cloud_connect=cloud_connect,
            instances=instances,
            type_=type_,
            last_update_date=last_update_date,
            last_update_message=last_update_message,
            last_update_status=last_update_status,
        )

        console_license.additional_properties = d
        return console_license

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
