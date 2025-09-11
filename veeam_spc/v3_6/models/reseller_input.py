from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

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
    Attributes:
        organization_input (OrganizationInput):
        owner_credentials (OwnerCredentials):
        description (Union[Unset, str]): Description of a reseller.
        pro_partner_id (Union[Unset, str]): ProPartner Portal ID assigned to a reseller.
        reseller_services (Union[Unset, ResellerServices]):
        is_rest_access_enabled (Union[Unset, bool]): Defines whether access to REST API is enabled for a reseller.
            Default: False.
    """

    organization_input: "OrganizationInput"
    owner_credentials: "OwnerCredentials"
    description: Union[Unset, str] = UNSET
    pro_partner_id: Union[Unset, str] = UNSET
    reseller_services: Union[Unset, "ResellerServices"] = UNSET
    is_rest_access_enabled: Union[Unset, bool] = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        organization_input = self.organization_input.to_dict()

        owner_credentials = self.owner_credentials.to_dict()

        description = self.description

        pro_partner_id = self.pro_partner_id

        reseller_services: Union[Unset, dict[str, Any]] = UNSET
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
        reseller_services: Union[Unset, ResellerServices]
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
