from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.policy_settings_mfa_policy_status import PolicySettingsMfaPolicyStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="PolicySettings")


@_attrs_define
class PolicySettings:
    """
    Attributes:
        mfa_policy_status (Union[Unset, PolicySettingsMfaPolicyStatus]): Status of MFA configuration requirement for
            user. Default: PolicySettingsMfaPolicyStatus.DISABLED.
        enforce_mfa_policy (Union[Unset, bool]): Indicates whether MFA policy is applied to child organizations.
    """

    mfa_policy_status: Union[Unset, PolicySettingsMfaPolicyStatus] = PolicySettingsMfaPolicyStatus.DISABLED
    enforce_mfa_policy: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        mfa_policy_status: Union[Unset, str] = UNSET
        if not isinstance(self.mfa_policy_status, Unset):
            mfa_policy_status = self.mfa_policy_status.value

        enforce_mfa_policy = self.enforce_mfa_policy

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if mfa_policy_status is not UNSET:
            field_dict["mfaPolicyStatus"] = mfa_policy_status
        if enforce_mfa_policy is not UNSET:
            field_dict["enforceMfaPolicy"] = enforce_mfa_policy

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _mfa_policy_status = d.pop("mfaPolicyStatus", UNSET)
        mfa_policy_status: Union[Unset, PolicySettingsMfaPolicyStatus]
        if isinstance(_mfa_policy_status, Unset):
            mfa_policy_status = UNSET
        else:
            mfa_policy_status = PolicySettingsMfaPolicyStatus(_mfa_policy_status)

        enforce_mfa_policy = d.pop("enforceMfaPolicy", UNSET)

        policy_settings = cls(
            mfa_policy_status=mfa_policy_status,
            enforce_mfa_policy=enforce_mfa_policy,
        )

        policy_settings.additional_properties = d
        return policy_settings

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
