from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UserBackupResource")


@_attrs_define
class UserBackupResource:
    """
    Attributes:
        site_uid (UUID): UID assigned to a Veeam Cloud Connect site.
        company_site_backup_resource_uid (UUID): UID assigned to a company backup resource.
        resource_friendly_name (str): Friendly name of a subtenant backup resource.
        user_uid (Union[Unset, UUID]): UID assigned to a subtenant user in Veeam Service Provider Console.
        description (Union[None, Unset, str]): Subtenant user description.
        subtenant_uid (Union[Unset, UUID]): UID assigned to a subtenant user in Veeam Cloud Connect.
        vcd_user_id (Union[None, Unset, str]): UID assigned to a VMware Cloud Director organization user account.
        storage_quota (Union[None, Unset, int]): Subtenant quota, in bytes.
        storage_quota_usage (Union[None, Unset, int]): Amount of storage space used by a subtenant, in bytes.
        is_storage_quota_unlimited (Union[Unset, bool]): Indicates whether a subtenant has unlimited quota. Default:
            True.
    """

    site_uid: UUID
    company_site_backup_resource_uid: UUID
    resource_friendly_name: str
    user_uid: Union[Unset, UUID] = UNSET
    description: Union[None, Unset, str] = UNSET
    subtenant_uid: Union[Unset, UUID] = UNSET
    vcd_user_id: Union[None, Unset, str] = UNSET
    storage_quota: Union[None, Unset, int] = UNSET
    storage_quota_usage: Union[None, Unset, int] = UNSET
    is_storage_quota_unlimited: Union[Unset, bool] = True
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        site_uid = str(self.site_uid)

        company_site_backup_resource_uid = str(self.company_site_backup_resource_uid)

        resource_friendly_name = self.resource_friendly_name

        user_uid: Union[Unset, str] = UNSET
        if not isinstance(self.user_uid, Unset):
            user_uid = str(self.user_uid)

        description: Union[None, Unset, str]
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        subtenant_uid: Union[Unset, str] = UNSET
        if not isinstance(self.subtenant_uid, Unset):
            subtenant_uid = str(self.subtenant_uid)

        vcd_user_id: Union[None, Unset, str]
        if isinstance(self.vcd_user_id, Unset):
            vcd_user_id = UNSET
        else:
            vcd_user_id = self.vcd_user_id

        storage_quota: Union[None, Unset, int]
        if isinstance(self.storage_quota, Unset):
            storage_quota = UNSET
        else:
            storage_quota = self.storage_quota

        storage_quota_usage: Union[None, Unset, int]
        if isinstance(self.storage_quota_usage, Unset):
            storage_quota_usage = UNSET
        else:
            storage_quota_usage = self.storage_quota_usage

        is_storage_quota_unlimited = self.is_storage_quota_unlimited

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "siteUid": site_uid,
                "companySiteBackupResourceUid": company_site_backup_resource_uid,
                "resourceFriendlyName": resource_friendly_name,
            }
        )
        if user_uid is not UNSET:
            field_dict["userUid"] = user_uid
        if description is not UNSET:
            field_dict["description"] = description
        if subtenant_uid is not UNSET:
            field_dict["subtenantUid"] = subtenant_uid
        if vcd_user_id is not UNSET:
            field_dict["vcdUserId"] = vcd_user_id
        if storage_quota is not UNSET:
            field_dict["storageQuota"] = storage_quota
        if storage_quota_usage is not UNSET:
            field_dict["storageQuotaUsage"] = storage_quota_usage
        if is_storage_quota_unlimited is not UNSET:
            field_dict["isStorageQuotaUnlimited"] = is_storage_quota_unlimited

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        site_uid = UUID(d.pop("siteUid"))

        company_site_backup_resource_uid = UUID(d.pop("companySiteBackupResourceUid"))

        resource_friendly_name = d.pop("resourceFriendlyName")

        _user_uid = d.pop("userUid", UNSET)
        user_uid: Union[Unset, UUID]
        if isinstance(_user_uid, Unset):
            user_uid = UNSET
        else:
            user_uid = UUID(_user_uid)

        def _parse_description(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        description = _parse_description(d.pop("description", UNSET))

        _subtenant_uid = d.pop("subtenantUid", UNSET)
        subtenant_uid: Union[Unset, UUID]
        if isinstance(_subtenant_uid, Unset):
            subtenant_uid = UNSET
        else:
            subtenant_uid = UUID(_subtenant_uid)

        def _parse_vcd_user_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        vcd_user_id = _parse_vcd_user_id(d.pop("vcdUserId", UNSET))

        def _parse_storage_quota(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        storage_quota = _parse_storage_quota(d.pop("storageQuota", UNSET))

        def _parse_storage_quota_usage(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        storage_quota_usage = _parse_storage_quota_usage(d.pop("storageQuotaUsage", UNSET))

        is_storage_quota_unlimited = d.pop("isStorageQuotaUnlimited", UNSET)

        user_backup_resource = cls(
            site_uid=site_uid,
            company_site_backup_resource_uid=company_site_backup_resource_uid,
            resource_friendly_name=resource_friendly_name,
            user_uid=user_uid,
            description=description,
            subtenant_uid=subtenant_uid,
            vcd_user_id=vcd_user_id,
            storage_quota=storage_quota,
            storage_quota_usage=storage_quota_usage,
            is_storage_quota_unlimited=is_storage_quota_unlimited,
        )

        user_backup_resource.additional_properties = d
        return user_backup_resource

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
