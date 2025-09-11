from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="IdentityProviderCompanyTenantMappingParameters")


@_attrs_define
class IdentityProviderCompanyTenantMappingParameters:
    """Parameters required to create a mapping rule for users with `CompanyTenant` role.

    Attributes:
        site_name_source_claim_type (str): Claim containing a name of a Veeam Cloud Connect site.
        tenant_name_source_claim_type (str): Claim containing name of a tenant.
    """

    site_name_source_claim_type: str
    tenant_name_source_claim_type: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        site_name_source_claim_type = self.site_name_source_claim_type

        tenant_name_source_claim_type = self.tenant_name_source_claim_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "siteNameSourceClaimType": site_name_source_claim_type,
                "tenantNameSourceClaimType": tenant_name_source_claim_type,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        site_name_source_claim_type = d.pop("siteNameSourceClaimType")

        tenant_name_source_claim_type = d.pop("tenantNameSourceClaimType")

        identity_provider_company_tenant_mapping_parameters = cls(
            site_name_source_claim_type=site_name_source_claim_type,
            tenant_name_source_claim_type=tenant_name_source_claim_type,
        )

        identity_provider_company_tenant_mapping_parameters.additional_properties = d
        return identity_provider_company_tenant_mapping_parameters

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
