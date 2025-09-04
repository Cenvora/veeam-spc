import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.pulse_license_assign_status import PulseLicenseAssignStatus
from ..models.pulse_license_automatic_extension_status import PulseLicenseAutomaticExtensionStatus
from ..models.pulse_license_automatic_reporting_status import PulseLicenseAutomaticReportingStatus
from ..models.pulse_license_type import PulseLicenseType
from ..models.pulse_license_usage_type import PulseLicenseUsageType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pulse_license_workload import PulseLicenseWorkload


T = TypeVar("T", bound="PulseLicense")


@_attrs_define
class PulseLicense:
    """
    Attributes:
        instance_uid (UUID): UID assigned to a VCSP Pulse license.
        type_ (PulseLicenseType): Type of a VCSP Pulse license.
        assign_status (PulseLicenseAssignStatus): Status of VCSP Pulse license assignement.
        usage_type (PulseLicenseUsageType): Type of VCSP Pulse license usage.
        contract_id (str): ID assigned to a rental agreement contract.
        product_id (str): ID asigned to a Veeam product that requires a license.
        points (float): Number of license points.
        automatic_reporting_status (PulseLicenseAutomaticReportingStatus): Status of the automatic license reporting.
        workloads (list['PulseLicenseWorkload']): Array of licensed workloads.
        license_id (Union[Unset, UUID]): ID assigned to a VCSP Pulse license in SalesForce.
        created_by (Union[Unset, str]): Name of an organization that created VCSP Pulse license.
        description (Union[Unset, str]): Description of a VCSP Pulse license.
        expiration_date (Union[Unset, datetime.datetime]): Date of the VCSP Pulse license expiration.
        automatic_extension_status (Union[Unset, PulseLicenseAutomaticExtensionStatus]): Status of the VCSP Pulse
            license automatic update.
        assigned_company_uid (Union[Unset, UUID]): UID of a company to which a VCSP Pulse license is assigned.
        assigned_reseller_uid (Union[Unset, UUID]): UID of a reseller to which a VCSP Pulse license is assigned.
    """

    instance_uid: UUID
    type_: PulseLicenseType
    assign_status: PulseLicenseAssignStatus
    usage_type: PulseLicenseUsageType
    contract_id: str
    product_id: str
    points: float
    automatic_reporting_status: PulseLicenseAutomaticReportingStatus
    workloads: list["PulseLicenseWorkload"]
    license_id: Union[Unset, UUID] = UNSET
    created_by: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    expiration_date: Union[Unset, datetime.datetime] = UNSET
    automatic_extension_status: Union[Unset, PulseLicenseAutomaticExtensionStatus] = UNSET
    assigned_company_uid: Union[Unset, UUID] = UNSET
    assigned_reseller_uid: Union[Unset, UUID] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        instance_uid = str(self.instance_uid)

        type_ = self.type_.value

        assign_status = self.assign_status.value

        usage_type = self.usage_type.value

        contract_id = self.contract_id

        product_id = self.product_id

        points = self.points

        automatic_reporting_status = self.automatic_reporting_status.value

        workloads = []
        for workloads_item_data in self.workloads:
            workloads_item = workloads_item_data.to_dict()
            workloads.append(workloads_item)

        license_id: Union[Unset, str] = UNSET
        if not isinstance(self.license_id, Unset):
            license_id = str(self.license_id)

        created_by = self.created_by

        description = self.description

        expiration_date: Union[Unset, str] = UNSET
        if not isinstance(self.expiration_date, Unset):
            expiration_date = self.expiration_date.isoformat()

        automatic_extension_status: Union[Unset, str] = UNSET
        if not isinstance(self.automatic_extension_status, Unset):
            automatic_extension_status = self.automatic_extension_status.value

        assigned_company_uid: Union[Unset, str] = UNSET
        if not isinstance(self.assigned_company_uid, Unset):
            assigned_company_uid = str(self.assigned_company_uid)

        assigned_reseller_uid: Union[Unset, str] = UNSET
        if not isinstance(self.assigned_reseller_uid, Unset):
            assigned_reseller_uid = str(self.assigned_reseller_uid)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "instanceUid": instance_uid,
                "type": type_,
                "assignStatus": assign_status,
                "usageType": usage_type,
                "contractId": contract_id,
                "productId": product_id,
                "points": points,
                "automaticReportingStatus": automatic_reporting_status,
                "workloads": workloads,
            }
        )
        if license_id is not UNSET:
            field_dict["licenseId"] = license_id
        if created_by is not UNSET:
            field_dict["createdBy"] = created_by
        if description is not UNSET:
            field_dict["description"] = description
        if expiration_date is not UNSET:
            field_dict["expirationDate"] = expiration_date
        if automatic_extension_status is not UNSET:
            field_dict["automaticExtensionStatus"] = automatic_extension_status
        if assigned_company_uid is not UNSET:
            field_dict["assignedCompanyUid"] = assigned_company_uid
        if assigned_reseller_uid is not UNSET:
            field_dict["assignedResellerUid"] = assigned_reseller_uid

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.pulse_license_workload import PulseLicenseWorkload

        d = dict(src_dict)
        instance_uid = UUID(d.pop("instanceUid"))

        type_ = PulseLicenseType(d.pop("type"))

        assign_status = PulseLicenseAssignStatus(d.pop("assignStatus"))

        usage_type = PulseLicenseUsageType(d.pop("usageType"))

        contract_id = d.pop("contractId")

        product_id = d.pop("productId")

        points = d.pop("points")

        automatic_reporting_status = PulseLicenseAutomaticReportingStatus(d.pop("automaticReportingStatus"))

        workloads = []
        _workloads = d.pop("workloads")
        for workloads_item_data in _workloads:
            workloads_item = PulseLicenseWorkload.from_dict(workloads_item_data)

            workloads.append(workloads_item)

        _license_id = d.pop("licenseId", UNSET)
        license_id: Union[Unset, UUID]
        if isinstance(_license_id, Unset):
            license_id = UNSET
        else:
            license_id = UUID(_license_id)

        created_by = d.pop("createdBy", UNSET)

        description = d.pop("description", UNSET)

        _expiration_date = d.pop("expirationDate", UNSET)
        expiration_date: Union[Unset, datetime.datetime]
        if isinstance(_expiration_date, Unset):
            expiration_date = UNSET
        else:
            expiration_date = isoparse(_expiration_date)

        _automatic_extension_status = d.pop("automaticExtensionStatus", UNSET)
        automatic_extension_status: Union[Unset, PulseLicenseAutomaticExtensionStatus]
        if isinstance(_automatic_extension_status, Unset):
            automatic_extension_status = UNSET
        else:
            automatic_extension_status = PulseLicenseAutomaticExtensionStatus(_automatic_extension_status)

        _assigned_company_uid = d.pop("assignedCompanyUid", UNSET)
        assigned_company_uid: Union[Unset, UUID]
        if isinstance(_assigned_company_uid, Unset):
            assigned_company_uid = UNSET
        else:
            assigned_company_uid = UUID(_assigned_company_uid)

        _assigned_reseller_uid = d.pop("assignedResellerUid", UNSET)
        assigned_reseller_uid: Union[Unset, UUID]
        if isinstance(_assigned_reseller_uid, Unset):
            assigned_reseller_uid = UNSET
        else:
            assigned_reseller_uid = UUID(_assigned_reseller_uid)

        pulse_license = cls(
            instance_uid=instance_uid,
            type_=type_,
            assign_status=assign_status,
            usage_type=usage_type,
            contract_id=contract_id,
            product_id=product_id,
            points=points,
            automatic_reporting_status=automatic_reporting_status,
            workloads=workloads,
            license_id=license_id,
            created_by=created_by,
            description=description,
            expiration_date=expiration_date,
            automatic_extension_status=automatic_extension_status,
            assigned_company_uid=assigned_company_uid,
            assigned_reseller_uid=assigned_reseller_uid,
        )

        pulse_license.additional_properties = d
        return pulse_license

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
