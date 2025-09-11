from collections.abc import Mapping
from typing import Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GrantPublicCloudCredentialsForMigrationResult")


@_attrs_define
class GrantPublicCloudCredentialsForMigrationResult:
    """
    Attributes:
        account_uid (UUID): UID assigned to an account.
        success (bool): Indicates whether permissions are granted successfully.
        message (Union[Unset, str]):
    """

    account_uid: UUID
    success: bool
    message: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        account_uid = str(self.account_uid)

        success = self.success

        message = self.message

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "accountUid": account_uid,
                "success": success,
            }
        )
        if message is not UNSET:
            field_dict["message"] = message

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        account_uid = UUID(d.pop("accountUid"))

        success = d.pop("success")

        message = d.pop("message", UNSET)

        grant_public_cloud_credentials_for_migration_result = cls(
            account_uid=account_uid,
            success=success,
            message=message,
        )

        grant_public_cloud_credentials_for_migration_result.additional_properties = d
        return grant_public_cloud_credentials_for_migration_result

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
