from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CompanyBackupAgentsManagement")


@_attrs_define
class CompanyBackupAgentsManagement:
    """Number of Veeam backup agents that a company is allowed to manage.

    Attributes:
        is_hard_quota_enabled (bool | Unset): Indicates whether Veeam backup agent management quota is a hard quota. The
            `true` value enables a license consumption check during Veeam backup agent registration. Default: False.
        workstation_agents_quota (int | Unset): Maximum number of Veeam backup agents in the Workstation mode that a
            company is allowed to manage.
            > The `null` value indicates that the number is unlimited.
        server_agents_quota (int | Unset): Maximum number of Veeam backup agents in the Server mode that a company is
            allowed to manage.
            > The `null` value indicates that the number is unlimited.
    """

    is_hard_quota_enabled: bool | Unset = False
    workstation_agents_quota: int | Unset = UNSET
    server_agents_quota: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        is_hard_quota_enabled = self.is_hard_quota_enabled

        workstation_agents_quota = self.workstation_agents_quota

        server_agents_quota = self.server_agents_quota

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if is_hard_quota_enabled is not UNSET:
            field_dict["isHardQuotaEnabled"] = is_hard_quota_enabled
        if workstation_agents_quota is not UNSET:
            field_dict["workstationAgentsQuota"] = workstation_agents_quota
        if server_agents_quota is not UNSET:
            field_dict["serverAgentsQuota"] = server_agents_quota

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        is_hard_quota_enabled = d.pop("isHardQuotaEnabled", UNSET)

        workstation_agents_quota = d.pop("workstationAgentsQuota", UNSET)

        server_agents_quota = d.pop("serverAgentsQuota", UNSET)

        company_backup_agents_management = cls(
            is_hard_quota_enabled=is_hard_quota_enabled,
            workstation_agents_quota=workstation_agents_quota,
            server_agents_quota=server_agents_quota,
        )

        company_backup_agents_management.additional_properties = d
        return company_backup_agents_management

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
