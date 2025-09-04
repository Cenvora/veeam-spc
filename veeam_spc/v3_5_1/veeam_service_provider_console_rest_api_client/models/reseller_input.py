from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.reseller_permissions_nullable_type_0_item import ResellerPermissionsNullableType0Item
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.organization_input import OrganizationInput
    from ..models.owner_credentials import OwnerCredentials
    from ..models.reseller_quota import ResellerQuota


T = TypeVar("T", bound="ResellerInput")


@_attrs_define
class ResellerInput:
    """
    Attributes:
        organization_input (OrganizationInput):
        quota (ResellerQuota):
        owner_credentials (OwnerCredentials):
        description (Union[None, Unset, str]): Description of a reseller.
        pro_partner_id (Union[None, Unset, str]): ProPartner Portal ID assigned to a reseller.
        permissions (Union[None, Unset, list[ResellerPermissionsNullableType0Item]]): Array of the Veeam Service
            Provider Console components that a reseller can access.
    """

    organization_input: "OrganizationInput"
    quota: "ResellerQuota"
    owner_credentials: "OwnerCredentials"
    description: Union[None, Unset, str] = UNSET
    pro_partner_id: Union[None, Unset, str] = UNSET
    permissions: Union[None, Unset, list[ResellerPermissionsNullableType0Item]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        organization_input = self.organization_input.to_dict()

        quota = self.quota.to_dict()

        owner_credentials = self.owner_credentials.to_dict()

        description: Union[None, Unset, str]
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        pro_partner_id: Union[None, Unset, str]
        if isinstance(self.pro_partner_id, Unset):
            pro_partner_id = UNSET
        else:
            pro_partner_id = self.pro_partner_id

        permissions: Union[None, Unset, list[str]]
        if isinstance(self.permissions, Unset):
            permissions = UNSET
        elif isinstance(self.permissions, list):
            permissions = []
            for componentsschemas_reseller_permissions_nullable_type_0_item_data in self.permissions:
                componentsschemas_reseller_permissions_nullable_type_0_item = (
                    componentsschemas_reseller_permissions_nullable_type_0_item_data.value
                )
                permissions.append(componentsschemas_reseller_permissions_nullable_type_0_item)

        else:
            permissions = self.permissions

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "organizationInput": organization_input,
                "quota": quota,
                "ownerCredentials": owner_credentials,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if pro_partner_id is not UNSET:
            field_dict["proPartnerId"] = pro_partner_id
        if permissions is not UNSET:
            field_dict["permissions"] = permissions

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.organization_input import OrganizationInput
        from ..models.owner_credentials import OwnerCredentials
        from ..models.reseller_quota import ResellerQuota

        d = dict(src_dict)
        organization_input = OrganizationInput.from_dict(d.pop("organizationInput"))

        quota = ResellerQuota.from_dict(d.pop("quota"))

        owner_credentials = OwnerCredentials.from_dict(d.pop("ownerCredentials"))

        def _parse_description(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_pro_partner_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        pro_partner_id = _parse_pro_partner_id(d.pop("proPartnerId", UNSET))

        def _parse_permissions(data: object) -> Union[None, Unset, list[ResellerPermissionsNullableType0Item]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                componentsschemas_reseller_permissions_nullable_type_0 = []
                _componentsschemas_reseller_permissions_nullable_type_0 = data
                for (
                    componentsschemas_reseller_permissions_nullable_type_0_item_data
                ) in _componentsschemas_reseller_permissions_nullable_type_0:
                    componentsschemas_reseller_permissions_nullable_type_0_item = ResellerPermissionsNullableType0Item(
                        componentsschemas_reseller_permissions_nullable_type_0_item_data
                    )

                    componentsschemas_reseller_permissions_nullable_type_0.append(
                        componentsschemas_reseller_permissions_nullable_type_0_item
                    )

                return componentsschemas_reseller_permissions_nullable_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[ResellerPermissionsNullableType0Item]], data)

        permissions = _parse_permissions(d.pop("permissions", UNSET))

        reseller_input = cls(
            organization_input=organization_input,
            quota=quota,
            owner_credentials=owner_credentials,
            description=description,
            pro_partner_id=pro_partner_id,
            permissions=permissions,
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
