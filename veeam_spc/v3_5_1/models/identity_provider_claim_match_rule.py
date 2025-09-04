from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.identity_provider_claim_match_rule_operator import IdentityProviderClaimMatchRuleOperator

T = TypeVar("T", bound="IdentityProviderClaimMatchRule")


@_attrs_define
class IdentityProviderClaimMatchRule:
    """
    Attributes:
        claim_type (str): Mapping claim type.
        operator (IdentityProviderClaimMatchRuleOperator): Logical operator.
        value (str): Mapping claim value.
        match_case (bool): Indicates whether value comparison must be case sensitive.
    """

    claim_type: str
    operator: IdentityProviderClaimMatchRuleOperator
    value: str
    match_case: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        claim_type = self.claim_type

        operator = self.operator.value

        value = self.value

        match_case = self.match_case

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "claimType": claim_type,
                "operator": operator,
                "value": value,
                "matchCase": match_case,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        claim_type = d.pop("claimType")

        operator = IdentityProviderClaimMatchRuleOperator(d.pop("operator"))

        value = d.pop("value")

        match_case = d.pop("matchCase")

        identity_provider_claim_match_rule = cls(
            claim_type=claim_type,
            operator=operator,
            value=value,
            match_case=match_case,
        )

        identity_provider_claim_match_rule.additional_properties = d
        return identity_provider_claim_match_rule

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
