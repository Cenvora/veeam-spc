from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ValidatePublicCloudCredentialsForMigrationResult")


@_attrs_define
class ValidatePublicCloudCredentialsForMigrationResult:
    """
    Attributes:
        account_uid (UUID): UID assigned to an account.
        success (bool): Indicates whether validation is successful.
        insufficient_rights (list[str]): Array of permissions that an account lacks.
    """

    account_uid: UUID
    success: bool
    insufficient_rights: list[str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        account_uid = str(self.account_uid)

        success = self.success

        insufficient_rights = self.insufficient_rights

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "accountUid": account_uid,
                "success": success,
                "insufficientRights": insufficient_rights,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        account_uid = UUID(d.pop("accountUid"))

        success = d.pop("success")

        insufficient_rights = cast(list[str], d.pop("insufficientRights"))

        validate_public_cloud_credentials_for_migration_result = cls(
            account_uid=account_uid,
            success=success,
            insufficient_rights=insufficient_rights,
        )

        validate_public_cloud_credentials_for_migration_result.additional_properties = d
        return validate_public_cloud_credentials_for_migration_result

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
