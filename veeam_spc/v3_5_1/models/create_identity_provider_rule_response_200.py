from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.identity_provider_role_mapping_rule import IdentityProviderRoleMappingRule
    from ..models.response_error import ResponseError
    from ..models.response_metadata_type_0 import ResponseMetadataType0


T = TypeVar("T", bound="CreateIdentityProviderRuleResponse200")


@_attrs_define
class CreateIdentityProviderRuleResponse200:
    """
    Attributes:
        meta (Union['ResponseMetadataType0', None, Unset]):
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
        errors (Union[None, Unset, list['ResponseError']]):
    """

    meta: Union["ResponseMetadataType0", None, Unset] = UNSET
    data: Union[Unset, "IdentityProviderRoleMappingRule"] = UNSET
    errors: Union[None, Unset, list["ResponseError"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.response_metadata_type_0 import ResponseMetadataType0

        meta: Union[None, Unset, dict[str, Any]]
        if isinstance(self.meta, Unset):
            meta = UNSET
        elif isinstance(self.meta, ResponseMetadataType0):
            meta = self.meta.to_dict()
        else:
            meta = self.meta

        data: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.data, Unset):
            data = self.data.to_dict()

        errors: Union[None, Unset, list[dict[str, Any]]]
        if isinstance(self.errors, Unset):
            errors = UNSET
        elif isinstance(self.errors, list):
            errors = []
            for errors_type_0_item_data in self.errors:
                errors_type_0_item = errors_type_0_item_data.to_dict()
                errors.append(errors_type_0_item)

        else:
            errors = self.errors

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
        from ..models.response_metadata_type_0 import ResponseMetadataType0

        d = dict(src_dict)

        def _parse_meta(data: object) -> Union["ResponseMetadataType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_response_metadata_type_0 = ResponseMetadataType0.from_dict(data)

                return componentsschemas_response_metadata_type_0
            except:  # noqa: E722
                pass
            return cast(Union["ResponseMetadataType0", None, Unset], data)

        meta = _parse_meta(d.pop("meta", UNSET))

        _data = d.pop("data", UNSET)
        data: Union[Unset, IdentityProviderRoleMappingRule]
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = IdentityProviderRoleMappingRule.from_dict(_data)

        def _parse_errors(data: object) -> Union[None, Unset, list["ResponseError"]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                errors_type_0 = []
                _errors_type_0 = data
                for errors_type_0_item_data in _errors_type_0:
                    errors_type_0_item = ResponseError.from_dict(errors_type_0_item_data)

                    errors_type_0.append(errors_type_0_item)

                return errors_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list["ResponseError"]], data)

        errors = _parse_errors(d.pop("errors", UNSET))

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
