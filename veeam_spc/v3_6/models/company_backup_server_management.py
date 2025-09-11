from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CompanyBackupServerManagement")


@_attrs_define
class CompanyBackupServerManagement:
    """Managed Veeam Backup & Replication server quota.

    Attributes:
        backup_server_quota (Union[Unset, int]): Number of Veeam Backup & Replication servers that a company is allowed
            to manage.
            > The `null` value indicates that the amount is unlimited.
    """

    backup_server_quota: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        backup_server_quota = self.backup_server_quota

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if backup_server_quota is not UNSET:
            field_dict["backupServerQuota"] = backup_server_quota

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        backup_server_quota = d.pop("backupServerQuota", UNSET)

        company_backup_server_management = cls(
            backup_server_quota=backup_server_quota,
        )

        company_backup_server_management.additional_properties = d
        return company_backup_server_management

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
