from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.user_input_mfa_policy_status import UserInputMfaPolicyStatus
from ..models.user_input_role import UserInputRole
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.credentials import Credentials
    from ..models.user_backup_resource_input import UserBackupResourceInput
    from ..models.user_profile import UserProfile


T = TypeVar("T", bound="UserInput")


@_attrs_define
class UserInput:
    """
    Attributes:
        organization_uid (UUID): UID assigned to an organization.
        role (UserInputRole): User role in Veeam Service Provider Console.
        profile (UserProfile):  Example: {'firstName': 'Mark', 'lastName': 'Brown', 'title': 'Mr', 'status': 'Enabled',
            'email': 'mark.brown@delta.com', 'address': '90 West Broad St Columbus OH 43215', 'phone': '(524) 745-5371'}.
        credentials (Credentials):
        mfa_policy_status (Union[Unset, UserInputMfaPolicyStatus]): Status of MFA configuration requirement for user.
            Default: UserInputMfaPolicyStatus.DISABLED.
        backup_resource (Union[Unset, UserBackupResourceInput]):
    """

    organization_uid: UUID
    role: UserInputRole
    profile: "UserProfile"
    credentials: "Credentials"
    mfa_policy_status: Union[Unset, UserInputMfaPolicyStatus] = UserInputMfaPolicyStatus.DISABLED
    backup_resource: Union[Unset, "UserBackupResourceInput"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        organization_uid = str(self.organization_uid)

        role = self.role.value

        profile = self.profile.to_dict()

        credentials = self.credentials.to_dict()

        mfa_policy_status: Union[Unset, str] = UNSET
        if not isinstance(self.mfa_policy_status, Unset):
            mfa_policy_status = self.mfa_policy_status.value

        backup_resource: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.backup_resource, Unset):
            backup_resource = self.backup_resource.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "organizationUid": organization_uid,
                "role": role,
                "profile": profile,
                "credentials": credentials,
            }
        )
        if mfa_policy_status is not UNSET:
            field_dict["mfaPolicyStatus"] = mfa_policy_status
        if backup_resource is not UNSET:
            field_dict["backupResource"] = backup_resource

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.credentials import Credentials
        from ..models.user_backup_resource_input import UserBackupResourceInput
        from ..models.user_profile import UserProfile

        d = dict(src_dict)
        organization_uid = UUID(d.pop("organizationUid"))

        role = UserInputRole(d.pop("role"))

        profile = UserProfile.from_dict(d.pop("profile"))

        credentials = Credentials.from_dict(d.pop("credentials"))

        _mfa_policy_status = d.pop("mfaPolicyStatus", UNSET)
        mfa_policy_status: Union[Unset, UserInputMfaPolicyStatus]
        if isinstance(_mfa_policy_status, Unset):
            mfa_policy_status = UNSET
        else:
            mfa_policy_status = UserInputMfaPolicyStatus(_mfa_policy_status)

        _backup_resource = d.pop("backupResource", UNSET)
        backup_resource: Union[Unset, UserBackupResourceInput]
        if isinstance(_backup_resource, Unset):
            backup_resource = UNSET
        else:
            backup_resource = UserBackupResourceInput.from_dict(_backup_resource)

        user_input = cls(
            organization_uid=organization_uid,
            role=role,
            profile=profile,
            credentials=credentials,
            mfa_policy_status=mfa_policy_status,
            backup_resource=backup_resource,
        )

        user_input.additional_properties = d
        return user_input

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
