from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.local_user_rule_mfa_policy_status import LocalUserRuleMfaPolicyStatus
from ..models.local_user_rule_role_type import LocalUserRuleRoleType
from ..models.local_user_rule_type import LocalUserRuleType
from ..models.win_context_type import WinContextType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.local_user_rule_object import LocalUserRuleObject


T = TypeVar("T", bound="LocalUserRule")


@_attrs_define
class LocalUserRule:
    """
    Attributes:
        name (str): Name of a user or group.
        role_type (LocalUserRuleRoleType): Role of a user or group users.
        context_type (WinContextType): Type of a location where an account is stored.
        scope (list['LocalUserRuleObject']): Array of services available to a user or group.
        type_ (LocalUserRuleType): Type of a user or group.
        mfa_policy_status (LocalUserRuleMfaPolicyStatus): Status of MFA configuration requirement for a user or group.
        instance_uid (Union[Unset, UUID]): UID assigned to a user or group.
        sid (Union[Unset, str]): SID assigned to a user or group.
        description (Union[None, Unset, str]): Description of a user or group.
        enabled (Union[Unset, bool]): Indicates whether a user or group is enabled. Default: True.
        has_access_to_provider (Union[None, Unset, bool]):
    """

    name: str
    role_type: LocalUserRuleRoleType
    context_type: WinContextType
    scope: list["LocalUserRuleObject"]
    type_: LocalUserRuleType
    mfa_policy_status: LocalUserRuleMfaPolicyStatus
    instance_uid: Union[Unset, UUID] = UNSET
    sid: Union[Unset, str] = UNSET
    description: Union[None, Unset, str] = UNSET
    enabled: Union[Unset, bool] = True
    has_access_to_provider: Union[None, Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        role_type = self.role_type.value

        context_type = self.context_type.value

        scope = []
        for scope_item_data in self.scope:
            scope_item = scope_item_data.to_dict()
            scope.append(scope_item)

        type_ = self.type_.value

        mfa_policy_status = self.mfa_policy_status.value

        instance_uid: Union[Unset, str] = UNSET
        if not isinstance(self.instance_uid, Unset):
            instance_uid = str(self.instance_uid)

        sid = self.sid

        description: Union[None, Unset, str]
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        enabled = self.enabled

        has_access_to_provider: Union[None, Unset, bool]
        if isinstance(self.has_access_to_provider, Unset):
            has_access_to_provider = UNSET
        else:
            has_access_to_provider = self.has_access_to_provider

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "roleType": role_type,
                "contextType": context_type,
                "scope": scope,
                "type": type_,
                "mfaPolicyStatus": mfa_policy_status,
            }
        )
        if instance_uid is not UNSET:
            field_dict["instanceUid"] = instance_uid
        if sid is not UNSET:
            field_dict["sid"] = sid
        if description is not UNSET:
            field_dict["description"] = description
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if has_access_to_provider is not UNSET:
            field_dict["hasAccessToProvider"] = has_access_to_provider

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.local_user_rule_object import LocalUserRuleObject

        d = dict(src_dict)
        name = d.pop("name")

        role_type = LocalUserRuleRoleType(d.pop("roleType"))

        context_type = WinContextType(d.pop("contextType"))

        scope = []
        _scope = d.pop("scope")
        for scope_item_data in _scope:
            scope_item = LocalUserRuleObject.from_dict(scope_item_data)

            scope.append(scope_item)

        type_ = LocalUserRuleType(d.pop("type"))

        mfa_policy_status = LocalUserRuleMfaPolicyStatus(d.pop("mfaPolicyStatus"))

        _instance_uid = d.pop("instanceUid", UNSET)
        instance_uid: Union[Unset, UUID]
        if isinstance(_instance_uid, Unset):
            instance_uid = UNSET
        else:
            instance_uid = UUID(_instance_uid)

        sid = d.pop("sid", UNSET)

        def _parse_description(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        description = _parse_description(d.pop("description", UNSET))

        enabled = d.pop("enabled", UNSET)

        def _parse_has_access_to_provider(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        has_access_to_provider = _parse_has_access_to_provider(d.pop("hasAccessToProvider", UNSET))

        local_user_rule = cls(
            name=name,
            role_type=role_type,
            context_type=context_type,
            scope=scope,
            type_=type_,
            mfa_policy_status=mfa_policy_status,
            instance_uid=instance_uid,
            sid=sid,
            description=description,
            enabled=enabled,
            has_access_to_provider=has_access_to_provider,
        )

        local_user_rule.additional_properties = d
        return local_user_rule

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
