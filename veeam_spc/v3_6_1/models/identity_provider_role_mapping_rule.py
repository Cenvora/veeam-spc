from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.identity_provider_role_mapping_rule_role import IdentityProviderRoleMappingRuleRole
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.identity_provider_attribute_mapping import IdentityProviderAttributeMapping
    from ..models.identity_provider_claim_match_rule import IdentityProviderClaimMatchRule
    from ..models.identity_provider_company_tenant_mapping_parameters_type_0 import (
        IdentityProviderCompanyTenantMappingParametersType0,
    )
    from ..models.identity_provider_role_mapping_rule_embedded import IdentityProviderRoleMappingRuleEmbedded


T = TypeVar("T", bound="IdentityProviderRoleMappingRule")


@_attrs_define
class IdentityProviderRoleMappingRule:
    """
    Example:
        {'name': 'Portal operators', 'desciption': 'Portal operators from ADFS', 'role': 'PortalOperator',
            'managedCompaniesUids': ['ab452a99-51bf-4a40-a1c4-df01506f56a3', 'd8ba8d10-f2fb-4592-8c41-184d0e1b03f1'],
            'organizationMappingSourceClaimType':
            'http://schemas.xmlsoap.org/ws/2005/05/identity/claims/ComanyNameAndAlias', 'additionalMappings': [{'claimType':
            'http://schemas.xmlsoap.org/ws/2005/05/identity/claims/emailaddress', 'operator': 'Contains', 'value':
            '@mycompany.com', 'matchCase': False}], 'attributeMappings': [{'claimType':
            'http://schemas.xmlsoap.org/ws/2005/05/identity/claims/firstName', 'allowAliases': True, 'attribute':
            'FirstName'}, {'claimType': 'http://schemas.xmlsoap.org/ws/2005/05/identity/claims/lastName', 'allowAliases':
            True, 'attribute': 'LastName'}, {'claimType': 'http://schemas.xmlsoap.org/ws/2005/05/identity/claims/name',
            'allowAliases': True, 'attribute': 'Name'}, {'claimType':
            'http://schemas.xmlsoap.org/ws/2005/05/identity/claims/address', 'allowAliases': True, 'attribute': 'Address'},
            {'claimType': 'http://schemas.xmlsoap.org/ws/2005/05/identity/claims/phone', 'allowAliases': True, 'attribute':
            'Phone'}], 'providerInfo': {'name': 'adfs', 'displayName': 'Microsoft Entra ID Federation Services', 'template':
            'ADFS', 'type': 'SAML2', 'organizationUid': '0242e3ca-1cc2-4d90-8285-0e7a9b375418', 'enabled': True}}

    Attributes:
        name (str): Name of a mapping rule. Each mapping rule configured for a single identity provider must have a
            unique name.
        role (IdentityProviderRoleMappingRuleRole): User role.
        organization_mapping_source_claim_type (str): Organization mapping claim type containing organization alias.
        instance_uid (Union[Unset, UUID]): UID assigned to a mapping rule.
        provider_name (Union[Unset, str]): Name of an identity provider.
        description (Union[None, Unset, str]): Mapping rule description.
        enabled (Union[Unset, bool]): Indicates whether a mapping rule is enabled. Default: True.
        managed_companies_uids (Union[None, Unset, list[UUID]]): Array of UIDs assigned to companies managed by a user.
            >Required for the `PortalOperator`, `PortalReadonlyOperator`, `ResellerOperator`, `ResellerUser`
            and `ResellerAdministrator` user roles.
        manage_all_companies (Union[Unset, bool]): Indicates whether a user must manage all available companies.
            Overrides values of the `managedCompaniesUids` property. Default: True.
        has_access_to_provider (Union[None, Unset, bool]): Indicates whether a user is permitted to view service
            provider organization resources.
            >Required for the `PortalOperator` and `PortalReadonlyOperator` user roles.
        locations_mapping_source_claim_type (Union[None, Unset, str]): Location mapping claim containing user locations
            in the following format: `Location1;Location2`.
            >This property can be specified for the `CompanyLocationUser`, `CompanyLocationAdministrator` and
            `CompanySubtenant` user roles. Otherwise a user is assigned to the first available company location.
        company_tenant_mapping_claims (Union['IdentityProviderCompanyTenantMappingParametersType0', None, Unset]):
            Parameters required to create a mapping rule for users with `CompanyTenant` role.
        additional_mappings (Union[None, Unset, list['IdentityProviderClaimMatchRule']]): Array of additional mappings
            required for rule selection.
        attribute_mappings (Union[None, Unset, list['IdentityProviderAttributeMapping']]): Array of mapping claims
            attributed to user parameters.
        field_embedded (Union[Unset, IdentityProviderRoleMappingRuleEmbedded]): Resource representation of the related
            identity provider entity.
    """

    name: str
    role: IdentityProviderRoleMappingRuleRole
    organization_mapping_source_claim_type: str
    instance_uid: Union[Unset, UUID] = UNSET
    provider_name: Union[Unset, str] = UNSET
    description: Union[None, Unset, str] = UNSET
    enabled: Union[Unset, bool] = True
    managed_companies_uids: Union[None, Unset, list[UUID]] = UNSET
    manage_all_companies: Union[Unset, bool] = True
    has_access_to_provider: Union[None, Unset, bool] = UNSET
    locations_mapping_source_claim_type: Union[None, Unset, str] = UNSET
    company_tenant_mapping_claims: Union["IdentityProviderCompanyTenantMappingParametersType0", None, Unset] = UNSET
    additional_mappings: Union[None, Unset, list["IdentityProviderClaimMatchRule"]] = UNSET
    attribute_mappings: Union[None, Unset, list["IdentityProviderAttributeMapping"]] = UNSET
    field_embedded: Union[Unset, "IdentityProviderRoleMappingRuleEmbedded"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.identity_provider_company_tenant_mapping_parameters_type_0 import (
            IdentityProviderCompanyTenantMappingParametersType0,
        )

        name = self.name

        role = self.role.value

        organization_mapping_source_claim_type = self.organization_mapping_source_claim_type

        instance_uid: Union[Unset, str] = UNSET
        if not isinstance(self.instance_uid, Unset):
            instance_uid = str(self.instance_uid)

        provider_name = self.provider_name

        description: Union[None, Unset, str]
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        enabled = self.enabled

        managed_companies_uids: Union[None, Unset, list[str]]
        if isinstance(self.managed_companies_uids, Unset):
            managed_companies_uids = UNSET
        elif isinstance(self.managed_companies_uids, list):
            managed_companies_uids = []
            for managed_companies_uids_type_0_item_data in self.managed_companies_uids:
                managed_companies_uids_type_0_item = str(managed_companies_uids_type_0_item_data)
                managed_companies_uids.append(managed_companies_uids_type_0_item)

        else:
            managed_companies_uids = self.managed_companies_uids

        manage_all_companies = self.manage_all_companies

        has_access_to_provider: Union[None, Unset, bool]
        if isinstance(self.has_access_to_provider, Unset):
            has_access_to_provider = UNSET
        else:
            has_access_to_provider = self.has_access_to_provider

        locations_mapping_source_claim_type: Union[None, Unset, str]
        if isinstance(self.locations_mapping_source_claim_type, Unset):
            locations_mapping_source_claim_type = UNSET
        else:
            locations_mapping_source_claim_type = self.locations_mapping_source_claim_type

        company_tenant_mapping_claims: Union[None, Unset, dict[str, Any]]
        if isinstance(self.company_tenant_mapping_claims, Unset):
            company_tenant_mapping_claims = UNSET
        elif isinstance(self.company_tenant_mapping_claims, IdentityProviderCompanyTenantMappingParametersType0):
            company_tenant_mapping_claims = self.company_tenant_mapping_claims.to_dict()
        else:
            company_tenant_mapping_claims = self.company_tenant_mapping_claims

        additional_mappings: Union[None, Unset, list[dict[str, Any]]]
        if isinstance(self.additional_mappings, Unset):
            additional_mappings = UNSET
        elif isinstance(self.additional_mappings, list):
            additional_mappings = []
            for additional_mappings_type_0_item_data in self.additional_mappings:
                additional_mappings_type_0_item = additional_mappings_type_0_item_data.to_dict()
                additional_mappings.append(additional_mappings_type_0_item)

        else:
            additional_mappings = self.additional_mappings

        attribute_mappings: Union[None, Unset, list[dict[str, Any]]]
        if isinstance(self.attribute_mappings, Unset):
            attribute_mappings = UNSET
        elif isinstance(self.attribute_mappings, list):
            attribute_mappings = []
            for attribute_mappings_type_0_item_data in self.attribute_mappings:
                attribute_mappings_type_0_item = attribute_mappings_type_0_item_data.to_dict()
                attribute_mappings.append(attribute_mappings_type_0_item)

        else:
            attribute_mappings = self.attribute_mappings

        field_embedded: Union[Unset, dict[str, Any]] = UNSET
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
        from ..models.identity_provider_company_tenant_mapping_parameters_type_0 import (
            IdentityProviderCompanyTenantMappingParametersType0,
        )
        from ..models.identity_provider_role_mapping_rule_embedded import IdentityProviderRoleMappingRuleEmbedded

        d = dict(src_dict)
        name = d.pop("name")

        role = IdentityProviderRoleMappingRuleRole(d.pop("role"))

        organization_mapping_source_claim_type = d.pop("organizationMappingSourceClaimType")

        _instance_uid = d.pop("instanceUid", UNSET)
        instance_uid: Union[Unset, UUID]
        if isinstance(_instance_uid, Unset):
            instance_uid = UNSET
        else:
            instance_uid = UUID(_instance_uid)

        provider_name = d.pop("providerName", UNSET)

        def _parse_description(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        description = _parse_description(d.pop("description", UNSET))

        enabled = d.pop("enabled", UNSET)

        def _parse_managed_companies_uids(data: object) -> Union[None, Unset, list[UUID]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                managed_companies_uids_type_0 = []
                _managed_companies_uids_type_0 = data
                for managed_companies_uids_type_0_item_data in _managed_companies_uids_type_0:
                    managed_companies_uids_type_0_item = UUID(managed_companies_uids_type_0_item_data)

                    managed_companies_uids_type_0.append(managed_companies_uids_type_0_item)

                return managed_companies_uids_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[UUID]], data)

        managed_companies_uids = _parse_managed_companies_uids(d.pop("managedCompaniesUids", UNSET))

        manage_all_companies = d.pop("manageAllCompanies", UNSET)

        def _parse_has_access_to_provider(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        has_access_to_provider = _parse_has_access_to_provider(d.pop("hasAccessToProvider", UNSET))

        def _parse_locations_mapping_source_claim_type(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        locations_mapping_source_claim_type = _parse_locations_mapping_source_claim_type(
            d.pop("locationsMappingSourceClaimType", UNSET)
        )

        def _parse_company_tenant_mapping_claims(
            data: object,
        ) -> Union["IdentityProviderCompanyTenantMappingParametersType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_identity_provider_company_tenant_mapping_parameters_type_0 = (
                    IdentityProviderCompanyTenantMappingParametersType0.from_dict(data)
                )

                return componentsschemas_identity_provider_company_tenant_mapping_parameters_type_0
            except:  # noqa: E722
                pass
            return cast(Union["IdentityProviderCompanyTenantMappingParametersType0", None, Unset], data)

        company_tenant_mapping_claims = _parse_company_tenant_mapping_claims(d.pop("companyTenantMappingClaims", UNSET))

        def _parse_additional_mappings(data: object) -> Union[None, Unset, list["IdentityProviderClaimMatchRule"]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                additional_mappings_type_0 = []
                _additional_mappings_type_0 = data
                for additional_mappings_type_0_item_data in _additional_mappings_type_0:
                    additional_mappings_type_0_item = IdentityProviderClaimMatchRule.from_dict(
                        additional_mappings_type_0_item_data
                    )

                    additional_mappings_type_0.append(additional_mappings_type_0_item)

                return additional_mappings_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list["IdentityProviderClaimMatchRule"]], data)

        additional_mappings = _parse_additional_mappings(d.pop("additionalMappings", UNSET))

        def _parse_attribute_mappings(data: object) -> Union[None, Unset, list["IdentityProviderAttributeMapping"]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                attribute_mappings_type_0 = []
                _attribute_mappings_type_0 = data
                for attribute_mappings_type_0_item_data in _attribute_mappings_type_0:
                    attribute_mappings_type_0_item = IdentityProviderAttributeMapping.from_dict(
                        attribute_mappings_type_0_item_data
                    )

                    attribute_mappings_type_0.append(attribute_mappings_type_0_item)

                return attribute_mappings_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list["IdentityProviderAttributeMapping"]], data)

        attribute_mappings = _parse_attribute_mappings(d.pop("attributeMappings", UNSET))

        _field_embedded = d.pop("_embedded", UNSET)
        field_embedded: Union[Unset, IdentityProviderRoleMappingRuleEmbedded]
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
