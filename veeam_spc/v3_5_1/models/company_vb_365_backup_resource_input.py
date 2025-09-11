from collections.abc import Mapping
from typing import Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CompanyVb365BackupResourceInput")


@_attrs_define
class CompanyVb365BackupResourceInput:
    """
    Attributes:
        repository_uid (UUID): UID assigned to a backup repository.
        proxy_uid (Union[Unset, UUID]): UID assigned to a backup proxy.
        proxy_pool_uid (Union[Unset, UUID]): UID assigned to a backup proxy pool.
        users_quota (Union[Unset, int]): Maximum number of protected user accounts.
        is_users_quota_unlimited (Union[Unset, bool]): Indicates whether a number of protected user accounts is
            unlimited. Default: True.
        storage_quota (Union[Unset, int]): Amount of space that a company can use to store user account data, in bytes.
        is_storage_quota_unlimited (Union[Unset, bool]): Indicates whether a storage quota is unlimited. Default: True.
    """

    repository_uid: UUID
    proxy_uid: Union[Unset, UUID] = UNSET
    proxy_pool_uid: Union[Unset, UUID] = UNSET
    users_quota: Union[Unset, int] = UNSET
    is_users_quota_unlimited: Union[Unset, bool] = True
    storage_quota: Union[Unset, int] = UNSET
    is_storage_quota_unlimited: Union[Unset, bool] = True
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        repository_uid = str(self.repository_uid)

        proxy_uid: Union[Unset, str] = UNSET
        if not isinstance(self.proxy_uid, Unset):
            proxy_uid = str(self.proxy_uid)

        proxy_pool_uid: Union[Unset, str] = UNSET
        if not isinstance(self.proxy_pool_uid, Unset):
            proxy_pool_uid = str(self.proxy_pool_uid)

        users_quota = self.users_quota

        is_users_quota_unlimited = self.is_users_quota_unlimited

        storage_quota = self.storage_quota

        is_storage_quota_unlimited = self.is_storage_quota_unlimited

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "repositoryUid": repository_uid,
            }
        )
        if proxy_uid is not UNSET:
            field_dict["proxyUid"] = proxy_uid
        if proxy_pool_uid is not UNSET:
            field_dict["proxyPoolUid"] = proxy_pool_uid
        if users_quota is not UNSET:
            field_dict["usersQuota"] = users_quota
        if is_users_quota_unlimited is not UNSET:
            field_dict["isUsersQuotaUnlimited"] = is_users_quota_unlimited
        if storage_quota is not UNSET:
            field_dict["storageQuota"] = storage_quota
        if is_storage_quota_unlimited is not UNSET:
            field_dict["isStorageQuotaUnlimited"] = is_storage_quota_unlimited

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        repository_uid = UUID(d.pop("repositoryUid"))

        _proxy_uid = d.pop("proxyUid", UNSET)
        proxy_uid: Union[Unset, UUID]
        if isinstance(_proxy_uid, Unset):
            proxy_uid = UNSET
        else:
            proxy_uid = UUID(_proxy_uid)

        _proxy_pool_uid = d.pop("proxyPoolUid", UNSET)
        proxy_pool_uid: Union[Unset, UUID]
        if isinstance(_proxy_pool_uid, Unset):
            proxy_pool_uid = UNSET
        else:
            proxy_pool_uid = UUID(_proxy_pool_uid)

        users_quota = d.pop("usersQuota", UNSET)

        is_users_quota_unlimited = d.pop("isUsersQuotaUnlimited", UNSET)

        storage_quota = d.pop("storageQuota", UNSET)

        is_storage_quota_unlimited = d.pop("isStorageQuotaUnlimited", UNSET)

        company_vb_365_backup_resource_input = cls(
            repository_uid=repository_uid,
            proxy_uid=proxy_uid,
            proxy_pool_uid=proxy_pool_uid,
            users_quota=users_quota,
            is_users_quota_unlimited=is_users_quota_unlimited,
            storage_quota=storage_quota,
            is_storage_quota_unlimited=is_storage_quota_unlimited,
        )

        company_vb_365_backup_resource_input.additional_properties = d
        return company_vb_365_backup_resource_input

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
