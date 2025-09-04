from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.user_mfa_policy_configuration_status import UserMfaPolicyConfigurationStatus
from ..models.user_mfa_policy_status import UserMfaPolicyStatus
from ..models.user_role import UserRole
from ..models.user_status import UserStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.credentials_info import CredentialsInfo
    from ..models.user_profile import UserProfile


T = TypeVar("T", bound="User")


@_attrs_define
class User:
    """
    Attributes:
        role (UserRole): User role.
        profile (UserProfile):  Example: {'firstName': 'Mark', 'lastName': 'Brown', 'title': 'Mr', 'status': 'Enabled',
            'email': 'mark.brown@delta.com', 'address': '90 West Broad St Columbus OH 43215', 'phone': '(524) 745-5371'}.
        instance_uid (Union[Unset, UUID]): UID assigned to a user.
        organization_uid (Union[Unset, UUID]): UID assigned to a user organization.
        user_name (Union[Unset, str]): User name.
        status (Union[Unset, UserStatus]): User status. Default: UserStatus.ENABLED.
        mfa_policy_status (Union[Unset, UserMfaPolicyStatus]): Status of MFA configuration requirement for user.
            Default: UserMfaPolicyStatus.DISABLED.
        mfa_policy_configuration_status (Union[Unset, UserMfaPolicyConfigurationStatus]): Status of user MFA policy
            configuration. Default: UserMfaPolicyConfigurationStatus.NOTCONFIGURED.
        credentials (Union[Unset, CredentialsInfo]):
    """

    role: UserRole
    profile: "UserProfile"
    instance_uid: Union[Unset, UUID] = UNSET
    organization_uid: Union[Unset, UUID] = UNSET
    user_name: Union[Unset, str] = UNSET
    status: Union[Unset, UserStatus] = UserStatus.ENABLED
    mfa_policy_status: Union[Unset, UserMfaPolicyStatus] = UserMfaPolicyStatus.DISABLED
    mfa_policy_configuration_status: Union[Unset, UserMfaPolicyConfigurationStatus] = (
        UserMfaPolicyConfigurationStatus.NOTCONFIGURED
    )
    credentials: Union[Unset, "CredentialsInfo"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        role = self.role.value

        profile = self.profile.to_dict()

        instance_uid: Union[Unset, str] = UNSET
        if not isinstance(self.instance_uid, Unset):
            instance_uid = str(self.instance_uid)

        organization_uid: Union[Unset, str] = UNSET
        if not isinstance(self.organization_uid, Unset):
            organization_uid = str(self.organization_uid)

        user_name = self.user_name

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        mfa_policy_status: Union[Unset, str] = UNSET
        if not isinstance(self.mfa_policy_status, Unset):
            mfa_policy_status = self.mfa_policy_status.value

        mfa_policy_configuration_status: Union[Unset, str] = UNSET
        if not isinstance(self.mfa_policy_configuration_status, Unset):
            mfa_policy_configuration_status = self.mfa_policy_configuration_status.value

        credentials: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.credentials, Unset):
            credentials = self.credentials.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "role": role,
                "profile": profile,
            }
        )
        if instance_uid is not UNSET:
            field_dict["instanceUid"] = instance_uid
        if organization_uid is not UNSET:
            field_dict["organizationUid"] = organization_uid
        if user_name is not UNSET:
            field_dict["userName"] = user_name
        if status is not UNSET:
            field_dict["status"] = status
        if mfa_policy_status is not UNSET:
            field_dict["mfaPolicyStatus"] = mfa_policy_status
        if mfa_policy_configuration_status is not UNSET:
            field_dict["mfaPolicyConfigurationStatus"] = mfa_policy_configuration_status
        if credentials is not UNSET:
            field_dict["credentials"] = credentials

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.credentials_info import CredentialsInfo
        from ..models.user_profile import UserProfile

        d = dict(src_dict)
        role = UserRole(d.pop("role"))

        profile = UserProfile.from_dict(d.pop("profile"))

        _instance_uid = d.pop("instanceUid", UNSET)
        instance_uid: Union[Unset, UUID]
        if isinstance(_instance_uid, Unset):
            instance_uid = UNSET
        else:
            instance_uid = UUID(_instance_uid)

        _organization_uid = d.pop("organizationUid", UNSET)
        organization_uid: Union[Unset, UUID]
        if isinstance(_organization_uid, Unset):
            organization_uid = UNSET
        else:
            organization_uid = UUID(_organization_uid)

        user_name = d.pop("userName", UNSET)

        _status = d.pop("status", UNSET)
        status: Union[Unset, UserStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = UserStatus(_status)

        _mfa_policy_status = d.pop("mfaPolicyStatus", UNSET)
        mfa_policy_status: Union[Unset, UserMfaPolicyStatus]
        if isinstance(_mfa_policy_status, Unset):
            mfa_policy_status = UNSET
        else:
            mfa_policy_status = UserMfaPolicyStatus(_mfa_policy_status)

        _mfa_policy_configuration_status = d.pop("mfaPolicyConfigurationStatus", UNSET)
        mfa_policy_configuration_status: Union[Unset, UserMfaPolicyConfigurationStatus]
        if isinstance(_mfa_policy_configuration_status, Unset):
            mfa_policy_configuration_status = UNSET
        else:
            mfa_policy_configuration_status = UserMfaPolicyConfigurationStatus(_mfa_policy_configuration_status)

        _credentials = d.pop("credentials", UNSET)
        credentials: Union[Unset, CredentialsInfo]
        if isinstance(_credentials, Unset):
            credentials = UNSET
        else:
            credentials = CredentialsInfo.from_dict(_credentials)

        user = cls(
            role=role,
            profile=profile,
            instance_uid=instance_uid,
            organization_uid=organization_uid,
            user_name=user_name,
            status=status,
            mfa_policy_status=mfa_policy_status,
            mfa_policy_configuration_status=mfa_policy_configuration_status,
            credentials=credentials,
        )

        user.additional_properties = d
        return user

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
