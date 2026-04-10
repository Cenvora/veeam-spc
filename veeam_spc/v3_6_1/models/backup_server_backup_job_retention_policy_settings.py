from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.backup_server_backup_job_retention_policy_type import BackupServerBackupJobRetentionPolicyType
from ..types import UNSET, Unset

T = TypeVar("T", bound="BackupServerBackupJobRetentionPolicySettings")


@_attrs_define
class BackupServerBackupJobRetentionPolicySettings:
    """Retention policy settings.

    Attributes:
        type_ (Union[Unset, BackupServerBackupJobRetentionPolicyType]): Type of a retention policy.
        quantity (Union[Unset, int]): Number of restore points or days that must must be stored. Default: 7.
    """

    type_: Union[Unset, BackupServerBackupJobRetentionPolicyType] = UNSET
    quantity: Union[Unset, int] = 7
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_: Union[Unset, str] = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        quantity = self.quantity

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type_ is not UNSET:
            field_dict["type"] = type_
        if quantity is not UNSET:
            field_dict["quantity"] = quantity

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _type_ = d.pop("type", UNSET)
        type_: Union[Unset, BackupServerBackupJobRetentionPolicyType]
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = BackupServerBackupJobRetentionPolicyType(_type_)

        quantity = d.pop("quantity", UNSET)

        backup_server_backup_job_retention_policy_settings = cls(
            type_=type_,
            quantity=quantity,
        )

        backup_server_backup_job_retention_policy_settings.additional_properties = d
        return backup_server_backup_job_retention_policy_settings

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
