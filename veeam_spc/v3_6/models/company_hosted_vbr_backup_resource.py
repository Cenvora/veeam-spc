from collections.abc import Mapping
from typing import Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CompanyHostedVbrBackupResource")


@_attrs_define
class CompanyHostedVbrBackupResource:
    """
    Attributes:
        repository_uid (UUID): UID assigned to a backup repository.
        instance_uid (Union[Unset, UUID]): UID assigned to a company hosted repository resource.
        company_uid (Union[Unset, UUID]): UID assigned to a company.
        hosted_resource_uid (Union[Unset, UUID]): UID assigned to a company hosted resource.
        storage_quota (Union[Unset, int]): Amount of space allocated to a company on a repository, in GB.
        is_storage_quota_unlimited (Union[Unset, bool]): Indicates whether a storage quota is unlimited. Default: True.
    """

    repository_uid: UUID
    instance_uid: Union[Unset, UUID] = UNSET
    company_uid: Union[Unset, UUID] = UNSET
    hosted_resource_uid: Union[Unset, UUID] = UNSET
    storage_quota: Union[Unset, int] = UNSET
    is_storage_quota_unlimited: Union[Unset, bool] = True
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        repository_uid = str(self.repository_uid)

        instance_uid: Union[Unset, str] = UNSET
        if not isinstance(self.instance_uid, Unset):
            instance_uid = str(self.instance_uid)

        company_uid: Union[Unset, str] = UNSET
        if not isinstance(self.company_uid, Unset):
            company_uid = str(self.company_uid)

        hosted_resource_uid: Union[Unset, str] = UNSET
        if not isinstance(self.hosted_resource_uid, Unset):
            hosted_resource_uid = str(self.hosted_resource_uid)

        storage_quota = self.storage_quota

        is_storage_quota_unlimited = self.is_storage_quota_unlimited

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "repositoryUid": repository_uid,
            }
        )
        if instance_uid is not UNSET:
            field_dict["instanceUid"] = instance_uid
        if company_uid is not UNSET:
            field_dict["companyUid"] = company_uid
        if hosted_resource_uid is not UNSET:
            field_dict["hostedResourceUid"] = hosted_resource_uid
        if storage_quota is not UNSET:
            field_dict["storageQuota"] = storage_quota
        if is_storage_quota_unlimited is not UNSET:
            field_dict["isStorageQuotaUnlimited"] = is_storage_quota_unlimited

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        repository_uid = UUID(d.pop("repositoryUid"))

        _instance_uid = d.pop("instanceUid", UNSET)
        instance_uid: Union[Unset, UUID]
        if isinstance(_instance_uid, Unset):
            instance_uid = UNSET
        else:
            instance_uid = UUID(_instance_uid)

        _company_uid = d.pop("companyUid", UNSET)
        company_uid: Union[Unset, UUID]
        if isinstance(_company_uid, Unset):
            company_uid = UNSET
        else:
            company_uid = UUID(_company_uid)

        _hosted_resource_uid = d.pop("hostedResourceUid", UNSET)
        hosted_resource_uid: Union[Unset, UUID]
        if isinstance(_hosted_resource_uid, Unset):
            hosted_resource_uid = UNSET
        else:
            hosted_resource_uid = UUID(_hosted_resource_uid)

        storage_quota = d.pop("storageQuota", UNSET)

        is_storage_quota_unlimited = d.pop("isStorageQuotaUnlimited", UNSET)

        company_hosted_vbr_backup_resource = cls(
            repository_uid=repository_uid,
            instance_uid=instance_uid,
            company_uid=company_uid,
            hosted_resource_uid=hosted_resource_uid,
            storage_quota=storage_quota,
            is_storage_quota_unlimited=is_storage_quota_unlimited,
        )

        company_hosted_vbr_backup_resource.additional_properties = d
        return company_hosted_vbr_backup_resource

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
