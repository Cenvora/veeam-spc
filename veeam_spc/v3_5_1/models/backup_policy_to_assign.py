from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.backup_policy import BackupPolicy


T = TypeVar("T", bound="BackupPolicyToAssign")


@_attrs_define
class BackupPolicyToAssign:
    """
    Attributes:
        company_uid (Union[Unset, UUID]): UID assigned to an organization to whose agents a backup policy is assigned.
        backup_policies (Union[Unset, list['BackupPolicy']]): Array of backup policies available to assign.
    """

    company_uid: Union[Unset, UUID] = UNSET
    backup_policies: Union[Unset, list["BackupPolicy"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        company_uid: Union[Unset, str] = UNSET
        if not isinstance(self.company_uid, Unset):
            company_uid = str(self.company_uid)

        backup_policies: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.backup_policies, Unset):
            backup_policies = []
            for backup_policies_item_data in self.backup_policies:
                backup_policies_item = backup_policies_item_data.to_dict()
                backup_policies.append(backup_policies_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if company_uid is not UNSET:
            field_dict["companyUid"] = company_uid
        if backup_policies is not UNSET:
            field_dict["backupPolicies"] = backup_policies

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.backup_policy import BackupPolicy

        d = dict(src_dict)
        _company_uid = d.pop("companyUid", UNSET)
        company_uid: Union[Unset, UUID]
        if isinstance(_company_uid, Unset):
            company_uid = UNSET
        else:
            company_uid = UUID(_company_uid)

        backup_policies = []
        _backup_policies = d.pop("backupPolicies", UNSET)
        for backup_policies_item_data in _backup_policies or []:
            backup_policies_item = BackupPolicy.from_dict(backup_policies_item_data)

            backup_policies.append(backup_policies_item)

        backup_policy_to_assign = cls(
            company_uid=company_uid,
            backup_policies=backup_policies,
        )

        backup_policy_to_assign.additional_properties = d
        return backup_policy_to_assign

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
