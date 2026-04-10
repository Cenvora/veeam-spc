from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.policy_settings_mfa_policy_status import PolicySettingsMfaPolicyStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="PolicySettings")


@_attrs_define
class PolicySettings:
    """
    Attributes:
        rest_api_proxying_enabled (bool): Indicates whether REST API proxying is enabled.
        power_shell_sessions_enabled (bool): Indicates whether the remote PowerShell console is enabled.
        redirecting_to_vbr_wizard_enabled (bool): Indicates whether Veeam Backup & Replication proxying is enabled.
        redirecting_to_vbr_web_ui_enabled (bool): Indicates whether Veeam Backup & Replication Web UI proxying is
            enabled.
        mfa_policy_status (PolicySettingsMfaPolicyStatus | Unset): Status of MFA configuration requirement for user.
            Default: PolicySettingsMfaPolicyStatus.DISABLED.
        enforce_mfa_policy (bool | Unset): Indicates whether MFA policy is applied to child organizations.
        rest_api_proxying_enabled_by_manager (bool | Unset): Indicates whether REST API proxying is enabled by a parent
            organization.
        power_shell_sessions_enabled_by_manager (bool | Unset): Indicates whether the remote PowerShell console is
            enabled by parent organizations.
        redirecting_to_vbr_wizard_enabled_by_manager (bool | Unset): Indicates whether Veeam Backup & Replication wizard
            proxying is enabled by parent organizations.
        redirecting_to_vbr_web_ui_enabled_by_manager (bool | Unset): Indicates whether Veeam Backup & Replication Web UI
            proxying is enabled by parent organizations.
    """

    rest_api_proxying_enabled: bool
    power_shell_sessions_enabled: bool
    redirecting_to_vbr_wizard_enabled: bool
    redirecting_to_vbr_web_ui_enabled: bool
    mfa_policy_status: PolicySettingsMfaPolicyStatus | Unset = PolicySettingsMfaPolicyStatus.DISABLED
    enforce_mfa_policy: bool | Unset = UNSET
    rest_api_proxying_enabled_by_manager: bool | Unset = UNSET
    power_shell_sessions_enabled_by_manager: bool | Unset = UNSET
    redirecting_to_vbr_wizard_enabled_by_manager: bool | Unset = UNSET
    redirecting_to_vbr_web_ui_enabled_by_manager: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        rest_api_proxying_enabled = self.rest_api_proxying_enabled

        power_shell_sessions_enabled = self.power_shell_sessions_enabled

        redirecting_to_vbr_wizard_enabled = self.redirecting_to_vbr_wizard_enabled

        redirecting_to_vbr_web_ui_enabled = self.redirecting_to_vbr_web_ui_enabled

        mfa_policy_status: str | Unset = UNSET
        if not isinstance(self.mfa_policy_status, Unset):
            mfa_policy_status = self.mfa_policy_status.value

        enforce_mfa_policy = self.enforce_mfa_policy

        rest_api_proxying_enabled_by_manager = self.rest_api_proxying_enabled_by_manager

        power_shell_sessions_enabled_by_manager = self.power_shell_sessions_enabled_by_manager

        redirecting_to_vbr_wizard_enabled_by_manager = self.redirecting_to_vbr_wizard_enabled_by_manager

        redirecting_to_vbr_web_ui_enabled_by_manager = self.redirecting_to_vbr_web_ui_enabled_by_manager

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "restApiProxyingEnabled": rest_api_proxying_enabled,
                "powerShellSessionsEnabled": power_shell_sessions_enabled,
                "redirectingToVbrWizardEnabled": redirecting_to_vbr_wizard_enabled,
                "redirectingToVbrWebUIEnabled": redirecting_to_vbr_web_ui_enabled,
            }
        )
        if mfa_policy_status is not UNSET:
            field_dict["mfaPolicyStatus"] = mfa_policy_status
        if enforce_mfa_policy is not UNSET:
            field_dict["enforceMfaPolicy"] = enforce_mfa_policy
        if rest_api_proxying_enabled_by_manager is not UNSET:
            field_dict["restApiProxyingEnabledByManager"] = rest_api_proxying_enabled_by_manager
        if power_shell_sessions_enabled_by_manager is not UNSET:
            field_dict["powerShellSessionsEnabledByManager"] = power_shell_sessions_enabled_by_manager
        if redirecting_to_vbr_wizard_enabled_by_manager is not UNSET:
            field_dict["redirectingToVbrWizardEnabledByManager"] = redirecting_to_vbr_wizard_enabled_by_manager
        if redirecting_to_vbr_web_ui_enabled_by_manager is not UNSET:
            field_dict["redirectingToVbrWebUIEnabledByManager"] = redirecting_to_vbr_web_ui_enabled_by_manager

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        rest_api_proxying_enabled = d.pop("restApiProxyingEnabled")

        power_shell_sessions_enabled = d.pop("powerShellSessionsEnabled")

        redirecting_to_vbr_wizard_enabled = d.pop("redirectingToVbrWizardEnabled")

        redirecting_to_vbr_web_ui_enabled = d.pop("redirectingToVbrWebUIEnabled")

        _mfa_policy_status = d.pop("mfaPolicyStatus", UNSET)
        mfa_policy_status: PolicySettingsMfaPolicyStatus | Unset
        if isinstance(_mfa_policy_status, Unset):
            mfa_policy_status = UNSET
        else:
            mfa_policy_status = PolicySettingsMfaPolicyStatus(_mfa_policy_status)

        enforce_mfa_policy = d.pop("enforceMfaPolicy", UNSET)

        rest_api_proxying_enabled_by_manager = d.pop("restApiProxyingEnabledByManager", UNSET)

        power_shell_sessions_enabled_by_manager = d.pop("powerShellSessionsEnabledByManager", UNSET)

        redirecting_to_vbr_wizard_enabled_by_manager = d.pop("redirectingToVbrWizardEnabledByManager", UNSET)

        redirecting_to_vbr_web_ui_enabled_by_manager = d.pop("redirectingToVbrWebUIEnabledByManager", UNSET)

        policy_settings = cls(
            rest_api_proxying_enabled=rest_api_proxying_enabled,
            power_shell_sessions_enabled=power_shell_sessions_enabled,
            redirecting_to_vbr_wizard_enabled=redirecting_to_vbr_wizard_enabled,
            redirecting_to_vbr_web_ui_enabled=redirecting_to_vbr_web_ui_enabled,
            mfa_policy_status=mfa_policy_status,
            enforce_mfa_policy=enforce_mfa_policy,
            rest_api_proxying_enabled_by_manager=rest_api_proxying_enabled_by_manager,
            power_shell_sessions_enabled_by_manager=power_shell_sessions_enabled_by_manager,
            redirecting_to_vbr_wizard_enabled_by_manager=redirecting_to_vbr_wizard_enabled_by_manager,
            redirecting_to_vbr_web_ui_enabled_by_manager=redirecting_to_vbr_web_ui_enabled_by_manager,
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
