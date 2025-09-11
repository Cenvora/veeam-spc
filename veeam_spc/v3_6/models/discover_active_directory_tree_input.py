from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.discovery_rule_credentials import DiscoveryRuleCredentials


T = TypeVar("T", bound="DiscoverActiveDirectoryTreeInput")


@_attrs_define
class DiscoverActiveDirectoryTreeInput:
    """
    Attributes:
        discovery_rule_uid (Union[Unset, UUID]): UID assigned to a discovery rule.
        service_account (Union[Unset, DiscoveryRuleCredentials]):
    """

    discovery_rule_uid: Union[Unset, UUID] = UNSET
    service_account: Union[Unset, "DiscoveryRuleCredentials"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        discovery_rule_uid: Union[Unset, str] = UNSET
        if not isinstance(self.discovery_rule_uid, Unset):
            discovery_rule_uid = str(self.discovery_rule_uid)

        service_account: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.service_account, Unset):
            service_account = self.service_account.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if discovery_rule_uid is not UNSET:
            field_dict["discoveryRuleUid"] = discovery_rule_uid
        if service_account is not UNSET:
            field_dict["serviceAccount"] = service_account

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.discovery_rule_credentials import DiscoveryRuleCredentials

        d = dict(src_dict)
        _discovery_rule_uid = d.pop("discoveryRuleUid", UNSET)
        discovery_rule_uid: Union[Unset, UUID]
        if isinstance(_discovery_rule_uid, Unset):
            discovery_rule_uid = UNSET
        else:
            discovery_rule_uid = UUID(_discovery_rule_uid)

        _service_account = d.pop("serviceAccount", UNSET)
        service_account: Union[Unset, DiscoveryRuleCredentials]
        if isinstance(_service_account, Unset):
            service_account = UNSET
        else:
            service_account = DiscoveryRuleCredentials.from_dict(_service_account)

        discover_active_directory_tree_input = cls(
            discovery_rule_uid=discovery_rule_uid,
            service_account=service_account,
        )

        discover_active_directory_tree_input.additional_properties = d
        return discover_active_directory_tree_input

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
