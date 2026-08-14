from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.organization_input import OrganizationInput
    from ..models.owner_credentials import OwnerCredentials
    from ..models.reseller_services import ResellerServices


T = TypeVar("T", bound="ResellerInput")


@_attrs_define
class ResellerInput:
    """
    Example:
        {'description': None, 'proPartnerId': None, 'organizationInput': {'name': 'Atrium Solutions', 'alias': 'atrium',
            'taxId': '34598', 'legalName': 'Atrium Solutions LLC', 'email': 'd.baker@atriumsol.com', 'phone':
            '606-932-3427', 'country': 1, 'state': 38, 'countryName': 'USA', 'regionName': None, 'city': 'South Shore',
            'street': '464 Hinkle Deegan Lake Road', 'locationAdmin0Code': 'us', 'locationAdmin1Code': 'us-ma',
            'locationAdmin2Code': None, 'notes': 'Basic configuration', 'zipCode': '41175', 'domain': 'atriumsol.com',
            'website': 'www.atriumsol.com', 'veeamTenantId': '11', 'companyId': None}, 'resellerServices':
            {'hostedServices': {'backupResourcesEnabled': False, 'vb365ManagementEnabled': False,
            'vbPublicCloudManagementEnabled': False}, 'remoteServices': {'backupAgentsManagement':
            {'workstationAgentsQuota': None, 'serverAgentsQuota': None}, 'vb365ManagementEnabled': False,
            'backupServersManagementEnabled': False, 'vbPublicCloudManagementEnabled': False}, 'cloudConnectQuota': None,
            'cloudConnectManagementEnabled': False, 'isFileLevelRestoreEnabled': False}, 'ownerCredentials': {'userName':
            'ResVcdExternalOwner', 'password': 'Password1'}, 'isRestAccessEnabled': True}

    Attributes:
        organization_input (OrganizationInput):
        owner_credentials (OwnerCredentials):
        description (str | Unset): Description of a reseller.
        pro_partner_id (str | Unset): ProPartner Portal ID assigned to a reseller.
        reseller_services (ResellerServices | Unset):
        is_rest_access_enabled (bool | Unset): Defines whether access to REST API is enabled for a reseller. Default:
            False.
    """

    organization_input: OrganizationInput
    owner_credentials: OwnerCredentials
    description: str | Unset = UNSET
    pro_partner_id: str | Unset = UNSET
    reseller_services: ResellerServices | Unset = UNSET
    is_rest_access_enabled: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        organization_input = self.organization_input.to_dict()

        owner_credentials = self.owner_credentials.to_dict()

        description = self.description

        pro_partner_id = self.pro_partner_id

        reseller_services: dict[str, Any] | Unset = UNSET
        if not isinstance(self.reseller_services, Unset):
            reseller_services = self.reseller_services.to_dict()

        is_rest_access_enabled = self.is_rest_access_enabled

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "organizationInput": organization_input,
                "ownerCredentials": owner_credentials,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if pro_partner_id is not UNSET:
            field_dict["proPartnerId"] = pro_partner_id
        if reseller_services is not UNSET:
            field_dict["resellerServices"] = reseller_services
        if is_rest_access_enabled is not UNSET:
            field_dict["isRestAccessEnabled"] = is_rest_access_enabled

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.organization_input import OrganizationInput
        from ..models.owner_credentials import OwnerCredentials
        from ..models.reseller_services import ResellerServices

        d = dict(src_dict)
        organization_input = OrganizationInput.from_dict(d.pop("organizationInput"))

        owner_credentials = OwnerCredentials.from_dict(d.pop("ownerCredentials"))

        description = d.pop("description", UNSET)

        pro_partner_id = d.pop("proPartnerId", UNSET)

        _reseller_services = d.pop("resellerServices", UNSET)
        reseller_services: ResellerServices | Unset
        if isinstance(_reseller_services, Unset):
            reseller_services = UNSET
        else:
            reseller_services = ResellerServices.from_dict(_reseller_services)

        is_rest_access_enabled = d.pop("isRestAccessEnabled", UNSET)

        reseller_input = cls(
            organization_input=organization_input,
            owner_credentials=owner_credentials,
            description=description,
            pro_partner_id=pro_partner_id,
            reseller_services=reseller_services,
            is_rest_access_enabled=is_rest_access_enabled,
        )

        reseller_input.additional_properties = d
        return reseller_input

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
