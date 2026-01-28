from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ResellerBackupAgentsManagement")


@_attrs_define
class ResellerBackupAgentsManagement:
    """
    Attributes:
        workstation_agents_quota (Union[None, Unset, int]): Maximum number of Veeam backup agents in the Workstation
            mode that a reseller is allowed to manage.
            > The `null` value indicates that the number is unlimited.
        server_agents_quota (Union[None, Unset, int]): Maximum number of Veeam backup agents in the Server mode that a
            reseller is allowed to manage.
            > The `null` value indicates that the number is unlimited.
    """

    workstation_agents_quota: Union[None, Unset, int] = UNSET
    server_agents_quota: Union[None, Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        workstation_agents_quota: Union[None, Unset, int]
        if isinstance(self.workstation_agents_quota, Unset):
            workstation_agents_quota = UNSET
        else:
            workstation_agents_quota = self.workstation_agents_quota

        server_agents_quota: Union[None, Unset, int]
        if isinstance(self.server_agents_quota, Unset):
            server_agents_quota = UNSET
        else:
            server_agents_quota = self.server_agents_quota

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if workstation_agents_quota is not UNSET:
            field_dict["workstationAgentsQuota"] = workstation_agents_quota
        if server_agents_quota is not UNSET:
            field_dict["serverAgentsQuota"] = server_agents_quota

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_workstation_agents_quota(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        workstation_agents_quota = _parse_workstation_agents_quota(d.pop("workstationAgentsQuota", UNSET))

        def _parse_server_agents_quota(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        server_agents_quota = _parse_server_agents_quota(d.pop("serverAgentsQuota", UNSET))

        reseller_backup_agents_management = cls(
            workstation_agents_quota=workstation_agents_quota,
            server_agents_quota=server_agents_quota,
        )

        reseller_backup_agents_management.additional_properties = d
        return reseller_backup_agents_management

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
