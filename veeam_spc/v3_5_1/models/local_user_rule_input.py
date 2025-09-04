from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.local_user_rule_mfa_policy_status import LocalUserRuleMfaPolicyStatus
from ..models.local_user_rule_role_type import LocalUserRuleRoleType
from ..models.local_user_rule_type_read_only import LocalUserRuleTypeReadOnly
from ..models.win_context_type import WinContextType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.local_user_rule_object import LocalUserRuleObject


T = TypeVar("T", bound="LocalUserRuleInput")


@_attrs_define
class LocalUserRuleInput:
    """
    Attributes:
        sid (str): SID of a user or group.
        name (str): Name of a user or group.
        context_type (WinContextType): Type of a location where an account is stored.
        scope (list['LocalUserRuleObject']): Array of services available to a user or group.
        type_ (LocalUserRuleTypeReadOnly): Type of a user or group.
        mfa_policy_status (LocalUserRuleMfaPolicyStatus): Status of MFA configuration requirement for a user or group.
        description (Union[Unset, str]): Description of a user or group.
        enabled (Union[Unset, bool]): Indicates whether a user or group is enabled. Default: True.
        role_type (Union[Unset, LocalUserRuleRoleType]): Role of a user or group users.
        has_access_to_provider (Union[Unset, bool]):
    """

    sid: str
    name: str
    context_type: WinContextType
    scope: list["LocalUserRuleObject"]
    type_: LocalUserRuleTypeReadOnly
    mfa_policy_status: LocalUserRuleMfaPolicyStatus
    description: Union[Unset, str] = UNSET
    enabled: Union[Unset, bool] = True
    role_type: Union[Unset, LocalUserRuleRoleType] = UNSET
    has_access_to_provider: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        sid = self.sid

        name = self.name

        context_type = self.context_type.value

        scope = []
        for scope_item_data in self.scope:
            scope_item = scope_item_data.to_dict()
            scope.append(scope_item)

        type_ = self.type_.value

        mfa_policy_status = self.mfa_policy_status.value

        description = self.description

        enabled = self.enabled

        role_type: Union[Unset, str] = UNSET
        if not isinstance(self.role_type, Unset):
            role_type = self.role_type.value

        has_access_to_provider = self.has_access_to_provider

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "sid": sid,
                "name": name,
                "contextType": context_type,
                "scope": scope,
                "type": type_,
                "mfaPolicyStatus": mfa_policy_status,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if role_type is not UNSET:
            field_dict["roleType"] = role_type
        if has_access_to_provider is not UNSET:
            field_dict["hasAccessToProvider"] = has_access_to_provider

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.local_user_rule_object import LocalUserRuleObject

        d = dict(src_dict)
        sid = d.pop("sid")

        name = d.pop("name")

        context_type = WinContextType(d.pop("contextType"))

        scope = []
        _scope = d.pop("scope")
        for scope_item_data in _scope:
            scope_item = LocalUserRuleObject.from_dict(scope_item_data)

            scope.append(scope_item)

        type_ = LocalUserRuleTypeReadOnly(d.pop("type"))

        mfa_policy_status = LocalUserRuleMfaPolicyStatus(d.pop("mfaPolicyStatus"))

        description = d.pop("description", UNSET)

        enabled = d.pop("enabled", UNSET)

        _role_type = d.pop("roleType", UNSET)
        role_type: Union[Unset, LocalUserRuleRoleType]
        if isinstance(_role_type, Unset):
            role_type = UNSET
        else:
            role_type = LocalUserRuleRoleType(_role_type)

        has_access_to_provider = d.pop("hasAccessToProvider", UNSET)

        local_user_rule_input = cls(
            sid=sid,
            name=name,
            context_type=context_type,
            scope=scope,
            type_=type_,
            mfa_policy_status=mfa_policy_status,
            description=description,
            enabled=enabled,
            role_type=role_type,
            has_access_to_provider=has_access_to_provider,
        )

        local_user_rule_input.additional_properties = d
        return local_user_rule_input

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
