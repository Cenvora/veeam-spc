from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CompanyBackupServerManagementType0")


@_attrs_define
class CompanyBackupServerManagementType0:
    """Managed Veeam Backup & Replication server quota.

    Attributes:
        backup_server_quota (Union[None, Unset, int]): Number of Veeam Backup & Replication servers that a company is
            allowed to manage.
            > The `null` value indicates that the amount is unlimited.
    """

    backup_server_quota: Union[None, Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        backup_server_quota: Union[None, Unset, int]
        if isinstance(self.backup_server_quota, Unset):
            backup_server_quota = UNSET
        else:
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

        def _parse_backup_server_quota(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        backup_server_quota = _parse_backup_server_quota(d.pop("backupServerQuota", UNSET))

        company_backup_server_management_type_0 = cls(
            backup_server_quota=backup_server_quota,
        )

        company_backup_server_management_type_0.additional_properties = d
        return company_backup_server_management_type_0

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
