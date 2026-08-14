from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.identity_provider_role_mapping_rule_role import IdentityProviderRoleMappingRuleRole
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.identity_provider_attribute_mapping import IdentityProviderAttributeMapping
    from ..models.identity_provider_claim_match_rule import IdentityProviderClaimMatchRule
    from ..models.identity_provider_company_tenant_mapping_parameters import (
        IdentityProviderCompanyTenantMappingParameters,
    )
    from ..models.identity_provider_role_mapping_rule_embedded import IdentityProviderRoleMappingRuleEmbedded


T = TypeVar("T", bound="IdentityProviderRoleMappingRule")


@_attrs_define
class IdentityProviderRoleMappingRule:
    """
    Example:
        {'name': 'PortalOperator', 'description': 'Portal Operator Keycloak', 'role': 'PortalOperator', 'enabled': True,
            'managedCompaniesUids': None, 'manageAllCompanies': True, 'hasAccessToProvider': True,
            'organizationMappingSourceClaimType': 'Company', 'locationsMappingSourceClaimType': None,
            'companyTenantMappingClaims': None, 'additionalMappings': None, 'attributeMappings': None, '_embedded': None}

    Attributes:
        name (str): Name of a mapping rule. Each mapping rule configured for a single identity provider must have a
            unique name.
        role (IdentityProviderRoleMappingRuleRole): User role.
        organization_mapping_source_claim_type (str): Organization mapping claim type containing organization alias.
        instance_uid (UUID | Unset): UID assigned to a mapping rule.
        provider_name (str | Unset): Name of an identity provider.
        description (str | Unset): Mapping rule description.
        enabled (bool | Unset): Indicates whether a mapping rule is enabled. Default: True.
        managed_companies_uids (list[UUID] | Unset): Array of UIDs assigned to companies managed by a user.
            >Required for the `PortalOperator`, `PortalReadonlyOperator`, `ResellerOperator`, `ResellerUser`
            and `ResellerAdministrator` user roles.
        manage_all_companies (bool | Unset): Indicates whether a user must manage all available companies. Overrides
            values of the `managedCompaniesUids` property. Default: True.
        has_access_to_provider (bool | Unset): Indicates whether a user is permitted to view service provider
            organization resources.
            >Required for the `PortalOperator` and `PortalReadonlyOperator` user roles.
        locations_mapping_source_claim_type (str | Unset): Location mapping claim containing user locations in the
            following format: `Location1;Location2`.
            >This property can be specified for the `CompanyLocationUser`, `CompanyLocationAdministrator` and
            `CompanySubtenant` user roles. Otherwise a user is assigned to the first available company location.
        company_tenant_mapping_claims (IdentityProviderCompanyTenantMappingParameters | Unset): Parameters required to
            create a mapping rule for users with `CompanyTenant` role.
        additional_mappings (list[IdentityProviderClaimMatchRule] | Unset): Array of additional mappings required for
            rule selection.
        attribute_mappings (list[IdentityProviderAttributeMapping] | Unset): Array of mapping claims attributed to user
            parameters.
        field_embedded (IdentityProviderRoleMappingRuleEmbedded | Unset): Resource representation of the related
            identity provider entity.
    """

    name: str
    role: IdentityProviderRoleMappingRuleRole
    organization_mapping_source_claim_type: str
    instance_uid: UUID | Unset = UNSET
    provider_name: str | Unset = UNSET
    description: str | Unset = UNSET
    enabled: bool | Unset = True
    managed_companies_uids: list[UUID] | Unset = UNSET
    manage_all_companies: bool | Unset = True
    has_access_to_provider: bool | Unset = UNSET
    locations_mapping_source_claim_type: str | Unset = UNSET
    company_tenant_mapping_claims: IdentityProviderCompanyTenantMappingParameters | Unset = UNSET
    additional_mappings: list[IdentityProviderClaimMatchRule] | Unset = UNSET
    attribute_mappings: list[IdentityProviderAttributeMapping] | Unset = UNSET
    field_embedded: IdentityProviderRoleMappingRuleEmbedded | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        role = self.role.value

        organization_mapping_source_claim_type = self.organization_mapping_source_claim_type

        instance_uid: str | Unset = UNSET
        if not isinstance(self.instance_uid, Unset):
            instance_uid = str(self.instance_uid)

        provider_name = self.provider_name

        description = self.description

        enabled = self.enabled

        managed_companies_uids: list[str] | Unset = UNSET
        if not isinstance(self.managed_companies_uids, Unset):
            managed_companies_uids = []
            for managed_companies_uids_item_data in self.managed_companies_uids:
                managed_companies_uids_item = str(managed_companies_uids_item_data)
                managed_companies_uids.append(managed_companies_uids_item)

        manage_all_companies = self.manage_all_companies

        has_access_to_provider = self.has_access_to_provider

        locations_mapping_source_claim_type = self.locations_mapping_source_claim_type

        company_tenant_mapping_claims: dict[str, Any] | Unset = UNSET
        if not isinstance(self.company_tenant_mapping_claims, Unset):
            company_tenant_mapping_claims = self.company_tenant_mapping_claims.to_dict()

        additional_mappings: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.additional_mappings, Unset):
            additional_mappings = []
            for additional_mappings_item_data in self.additional_mappings:
                additional_mappings_item = additional_mappings_item_data.to_dict()
                additional_mappings.append(additional_mappings_item)

        attribute_mappings: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.attribute_mappings, Unset):
            attribute_mappings = []
            for attribute_mappings_item_data in self.attribute_mappings:
                attribute_mappings_item = attribute_mappings_item_data.to_dict()
                attribute_mappings.append(attribute_mappings_item)

        field_embedded: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_embedded, Unset):
            field_embedded = self.field_embedded.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "role": role,
                "organizationMappingSourceClaimType": organization_mapping_source_claim_type,
            }
        )
        if instance_uid is not UNSET:
            field_dict["instanceUid"] = instance_uid
        if provider_name is not UNSET:
            field_dict["providerName"] = provider_name
        if description is not UNSET:
            field_dict["description"] = description
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if managed_companies_uids is not UNSET:
            field_dict["managedCompaniesUids"] = managed_companies_uids
        if manage_all_companies is not UNSET:
            field_dict["manageAllCompanies"] = manage_all_companies
        if has_access_to_provider is not UNSET:
            field_dict["hasAccessToProvider"] = has_access_to_provider
        if locations_mapping_source_claim_type is not UNSET:
            field_dict["locationsMappingSourceClaimType"] = locations_mapping_source_claim_type
        if company_tenant_mapping_claims is not UNSET:
            field_dict["companyTenantMappingClaims"] = company_tenant_mapping_claims
        if additional_mappings is not UNSET:
            field_dict["additionalMappings"] = additional_mappings
        if attribute_mappings is not UNSET:
            field_dict["attributeMappings"] = attribute_mappings
        if field_embedded is not UNSET:
            field_dict["_embedded"] = field_embedded

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.identity_provider_attribute_mapping import IdentityProviderAttributeMapping
        from ..models.identity_provider_claim_match_rule import IdentityProviderClaimMatchRule
        from ..models.identity_provider_company_tenant_mapping_parameters import (
            IdentityProviderCompanyTenantMappingParameters,
        )
        from ..models.identity_provider_role_mapping_rule_embedded import IdentityProviderRoleMappingRuleEmbedded

        d = dict(src_dict)
        name = d.pop("name")

        role = IdentityProviderRoleMappingRuleRole(d.pop("role"))

        organization_mapping_source_claim_type = d.pop("organizationMappingSourceClaimType")

        _instance_uid = d.pop("instanceUid", UNSET)
        instance_uid: UUID | Unset
        if isinstance(_instance_uid, Unset):
            instance_uid = UNSET
        else:
            instance_uid = UUID(_instance_uid)

        provider_name = d.pop("providerName", UNSET)

        description = d.pop("description", UNSET)

        enabled = d.pop("enabled", UNSET)

        _managed_companies_uids = d.pop("managedCompaniesUids", UNSET)
        managed_companies_uids: list[UUID] | Unset = UNSET
        if _managed_companies_uids is not UNSET:
            managed_companies_uids = []
            for managed_companies_uids_item_data in _managed_companies_uids:
                managed_companies_uids_item = UUID(managed_companies_uids_item_data)

                managed_companies_uids.append(managed_companies_uids_item)

        manage_all_companies = d.pop("manageAllCompanies", UNSET)

        has_access_to_provider = d.pop("hasAccessToProvider", UNSET)

        locations_mapping_source_claim_type = d.pop("locationsMappingSourceClaimType", UNSET)

        _company_tenant_mapping_claims = d.pop("companyTenantMappingClaims", UNSET)
        company_tenant_mapping_claims: IdentityProviderCompanyTenantMappingParameters | Unset
        if isinstance(_company_tenant_mapping_claims, Unset):
            company_tenant_mapping_claims = UNSET
        else:
            company_tenant_mapping_claims = IdentityProviderCompanyTenantMappingParameters.from_dict(
                _company_tenant_mapping_claims
            )

        _additional_mappings = d.pop("additionalMappings", UNSET)
        additional_mappings: list[IdentityProviderClaimMatchRule] | Unset = UNSET
        if _additional_mappings is not UNSET:
            additional_mappings = []
            for additional_mappings_item_data in _additional_mappings:
                additional_mappings_item = IdentityProviderClaimMatchRule.from_dict(additional_mappings_item_data)

                additional_mappings.append(additional_mappings_item)

        _attribute_mappings = d.pop("attributeMappings", UNSET)
        attribute_mappings: list[IdentityProviderAttributeMapping] | Unset = UNSET
        if _attribute_mappings is not UNSET:
            attribute_mappings = []
            for attribute_mappings_item_data in _attribute_mappings:
                attribute_mappings_item = IdentityProviderAttributeMapping.from_dict(attribute_mappings_item_data)

                attribute_mappings.append(attribute_mappings_item)

        _field_embedded = d.pop("_embedded", UNSET)
        field_embedded: IdentityProviderRoleMappingRuleEmbedded | Unset
        if isinstance(_field_embedded, Unset):
            field_embedded = UNSET
        else:
            field_embedded = IdentityProviderRoleMappingRuleEmbedded.from_dict(_field_embedded)

        identity_provider_role_mapping_rule = cls(
            name=name,
            role=role,
            organization_mapping_source_claim_type=organization_mapping_source_claim_type,
            instance_uid=instance_uid,
            provider_name=provider_name,
            description=description,
            enabled=enabled,
            managed_companies_uids=managed_companies_uids,
            manage_all_companies=manage_all_companies,
            has_access_to_provider=has_access_to_provider,
            locations_mapping_source_claim_type=locations_mapping_source_claim_type,
            company_tenant_mapping_claims=company_tenant_mapping_claims,
            additional_mappings=additional_mappings,
            attribute_mappings=attribute_mappings,
            field_embedded=field_embedded,
        )

        identity_provider_role_mapping_rule.additional_properties = d
        return identity_provider_role_mapping_rule

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
