from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.identity_provider_role_mapping_rule import IdentityProviderRoleMappingRule
    from ..models.response_error import ResponseError
    from ..models.response_metadata import ResponseMetadata


T = TypeVar("T", bound="CreateIdentityProviderRuleResponse200")


@_attrs_define
class CreateIdentityProviderRuleResponse200:
    """
    Attributes:
        meta (Union[Unset, ResponseMetadata]):
        data (Union[Unset, IdentityProviderRoleMappingRule]):  Example: {'name': 'Portal operators', 'desciption':
            'Portal operators from ADFS', 'role': 'PortalOperator', 'managedCompaniesUids':
            ['ab452a99-51bf-4a40-a1c4-df01506f56a3', 'd8ba8d10-f2fb-4592-8c41-184d0e1b03f1'],
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
            'ADFS', 'type': 'SAML2', 'organizationUid': '0242e3ca-1cc2-4d90-8285-0e7a9b375418', 'enabled': True}}.
        errors (Union[Unset, list['ResponseError']]):
    """

    meta: Union[Unset, "ResponseMetadata"] = UNSET
    data: Union[Unset, "IdentityProviderRoleMappingRule"] = UNSET
    errors: Union[Unset, list["ResponseError"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        meta: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.meta, Unset):
            meta = self.meta.to_dict()

        data: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.data, Unset):
            data = self.data.to_dict()

        errors: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.errors, Unset):
            errors = []
            for errors_item_data in self.errors:
                errors_item = errors_item_data.to_dict()
                errors.append(errors_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if meta is not UNSET:
            field_dict["meta"] = meta
        if data is not UNSET:
            field_dict["data"] = data
        if errors is not UNSET:
            field_dict["errors"] = errors

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.identity_provider_role_mapping_rule import IdentityProviderRoleMappingRule
        from ..models.response_error import ResponseError
        from ..models.response_metadata import ResponseMetadata

        d = dict(src_dict)
        _meta = d.pop("meta", UNSET)
        meta: Union[Unset, ResponseMetadata]
        if isinstance(_meta, Unset):
            meta = UNSET
        else:
            meta = ResponseMetadata.from_dict(_meta)

        _data = d.pop("data", UNSET)
        data: Union[Unset, IdentityProviderRoleMappingRule]
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = IdentityProviderRoleMappingRule.from_dict(_data)

        errors = []
        _errors = d.pop("errors", UNSET)
        for errors_item_data in _errors or []:
            errors_item = ResponseError.from_dict(errors_item_data)

            errors.append(errors_item)

        create_identity_provider_rule_response_200 = cls(
            meta=meta,
            data=data,
            errors=errors,
        )

        create_identity_provider_rule_response_200.additional_properties = d
        return create_identity_provider_rule_response_200

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
