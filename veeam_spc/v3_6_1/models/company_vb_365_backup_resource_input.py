from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast
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
        proxy_uid (Union[None, UUID, Unset]): UID assigned to a backup proxy.
        proxy_pool_uid (Union[None, UUID, Unset]): UID assigned to a backup proxy pool.
        users_quota (Union[None, Unset, int]): Maximum number of protected user accounts.
        is_users_quota_unlimited (Union[Unset, bool]): Indicates whether a number of protected user accounts is
            unlimited. Default: True.
        storage_quota (Union[None, Unset, int]): Maximum amount of Veeam Backup for Microsoft 365 repository storage
            space that a company is allowed to use, in GB.
        is_storage_quota_unlimited (Union[Unset, bool]): Indicates whether a storage quota is unlimited. Default: True.
    """

    repository_uid: UUID
    proxy_uid: Union[None, UUID, Unset] = UNSET
    proxy_pool_uid: Union[None, UUID, Unset] = UNSET
    users_quota: Union[None, Unset, int] = UNSET
    is_users_quota_unlimited: Union[Unset, bool] = True
    storage_quota: Union[None, Unset, int] = UNSET
    is_storage_quota_unlimited: Union[Unset, bool] = True
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        repository_uid = str(self.repository_uid)

        proxy_uid: Union[None, Unset, str]
        if isinstance(self.proxy_uid, Unset):
            proxy_uid = UNSET
        elif isinstance(self.proxy_uid, UUID):
            proxy_uid = str(self.proxy_uid)
        else:
            proxy_uid = self.proxy_uid

        proxy_pool_uid: Union[None, Unset, str]
        if isinstance(self.proxy_pool_uid, Unset):
            proxy_pool_uid = UNSET
        elif isinstance(self.proxy_pool_uid, UUID):
            proxy_pool_uid = str(self.proxy_pool_uid)
        else:
            proxy_pool_uid = self.proxy_pool_uid

        users_quota: Union[None, Unset, int]
        if isinstance(self.users_quota, Unset):
            users_quota = UNSET
        else:
            users_quota = self.users_quota

        is_users_quota_unlimited = self.is_users_quota_unlimited

        storage_quota: Union[None, Unset, int]
        if isinstance(self.storage_quota, Unset):
            storage_quota = UNSET
        else:
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

        def _parse_proxy_uid(data: object) -> Union[None, UUID, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                proxy_uid_type_0 = UUID(data)

                return proxy_uid_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID, Unset], data)

        proxy_uid = _parse_proxy_uid(d.pop("proxyUid", UNSET))

        def _parse_proxy_pool_uid(data: object) -> Union[None, UUID, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                proxy_pool_uid_type_0 = UUID(data)

                return proxy_pool_uid_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID, Unset], data)

        proxy_pool_uid = _parse_proxy_pool_uid(d.pop("proxyPoolUid", UNSET))

        def _parse_users_quota(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        users_quota = _parse_users_quota(d.pop("usersQuota", UNSET))

        is_users_quota_unlimited = d.pop("isUsersQuotaUnlimited", UNSET)

        def _parse_storage_quota(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        storage_quota = _parse_storage_quota(d.pop("storageQuota", UNSET))

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
