from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ResellerSiteBackupResource")


@_attrs_define
class ResellerSiteBackupResource:
    """
    Attributes:
        resource_friendly_name (str): Cloud repository friendly name configured for a reseller.
        instance_uid (UUID | Unset): UID assigned to a cloud backup resource.
        site_uid (UUID | Unset): UID assigned to a Veeam Cloud Connect site.
        reseller_uid (UUID | Unset): UID assigned to a reseller.
        repository_uid (UUID | Unset): UID assigned to a cloud backup repository.
        storage_quota (int | None | Unset): Amount of space allocated to a reseller, in bytes.
        is_storage_quota_unlimited (bool | Unset): Indicates whether the amount of space allocated to a reseller is
            unlimited. Default: True.
        servers_quota (int | None | Unset): Number of servers that a reseller can store on a cloud backup repository.
        is_servers_quota_unlimited (bool | Unset): Indicates whether the number of servers that a reseller can store on
            a cloud backup repository is unlimited. Default: True.
        workstations_quota (int | None | Unset): Number of workstations that a reseller can store on a cloud backup
            repository.
        is_workstations_quota_unlimited (bool | Unset): Indicates whether the number of workstations that a reseller can
            store on a cloud backup repository is unlimited. Default: True.
        vms_quota (int | None | Unset): Number of VMs that a reseller can store on a cloud backup repository.
        is_vms_quota_unlimited (bool | Unset): Indicates whether the number of VMs that a reseller can store on a cloud
            backup repository is unlimited. Default: True.
    """

    resource_friendly_name: str
    instance_uid: UUID | Unset = UNSET
    site_uid: UUID | Unset = UNSET
    reseller_uid: UUID | Unset = UNSET
    repository_uid: UUID | Unset = UNSET
    storage_quota: int | None | Unset = UNSET
    is_storage_quota_unlimited: bool | Unset = True
    servers_quota: int | None | Unset = UNSET
    is_servers_quota_unlimited: bool | Unset = True
    workstations_quota: int | None | Unset = UNSET
    is_workstations_quota_unlimited: bool | Unset = True
    vms_quota: int | None | Unset = UNSET
    is_vms_quota_unlimited: bool | Unset = True
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        resource_friendly_name = self.resource_friendly_name

        instance_uid: str | Unset = UNSET
        if not isinstance(self.instance_uid, Unset):
            instance_uid = str(self.instance_uid)

        site_uid: str | Unset = UNSET
        if not isinstance(self.site_uid, Unset):
            site_uid = str(self.site_uid)

        reseller_uid: str | Unset = UNSET
        if not isinstance(self.reseller_uid, Unset):
            reseller_uid = str(self.reseller_uid)

        repository_uid: str | Unset = UNSET
        if not isinstance(self.repository_uid, Unset):
            repository_uid = str(self.repository_uid)

        storage_quota: int | None | Unset
        if isinstance(self.storage_quota, Unset):
            storage_quota = UNSET
        else:
            storage_quota = self.storage_quota

        is_storage_quota_unlimited = self.is_storage_quota_unlimited

        servers_quota: int | None | Unset
        if isinstance(self.servers_quota, Unset):
            servers_quota = UNSET
        else:
            servers_quota = self.servers_quota

        is_servers_quota_unlimited = self.is_servers_quota_unlimited

        workstations_quota: int | None | Unset
        if isinstance(self.workstations_quota, Unset):
            workstations_quota = UNSET
        else:
            workstations_quota = self.workstations_quota

        is_workstations_quota_unlimited = self.is_workstations_quota_unlimited

        vms_quota: int | None | Unset
        if isinstance(self.vms_quota, Unset):
            vms_quota = UNSET
        else:
            vms_quota = self.vms_quota

        is_vms_quota_unlimited = self.is_vms_quota_unlimited

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "resourceFriendlyName": resource_friendly_name,
            }
        )
        if instance_uid is not UNSET:
            field_dict["instanceUid"] = instance_uid
        if site_uid is not UNSET:
            field_dict["siteUid"] = site_uid
        if reseller_uid is not UNSET:
            field_dict["resellerUid"] = reseller_uid
        if repository_uid is not UNSET:
            field_dict["repositoryUid"] = repository_uid
        if storage_quota is not UNSET:
            field_dict["storageQuota"] = storage_quota
        if is_storage_quota_unlimited is not UNSET:
            field_dict["isStorageQuotaUnlimited"] = is_storage_quota_unlimited
        if servers_quota is not UNSET:
            field_dict["serversQuota"] = servers_quota
        if is_servers_quota_unlimited is not UNSET:
            field_dict["isServersQuotaUnlimited"] = is_servers_quota_unlimited
        if workstations_quota is not UNSET:
            field_dict["workstationsQuota"] = workstations_quota
        if is_workstations_quota_unlimited is not UNSET:
            field_dict["isWorkstationsQuotaUnlimited"] = is_workstations_quota_unlimited
        if vms_quota is not UNSET:
            field_dict["vmsQuota"] = vms_quota
        if is_vms_quota_unlimited is not UNSET:
            field_dict["isVmsQuotaUnlimited"] = is_vms_quota_unlimited

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        resource_friendly_name = d.pop("resourceFriendlyName")

        _instance_uid = d.pop("instanceUid", UNSET)
        instance_uid: UUID | Unset
        if isinstance(_instance_uid, Unset):
            instance_uid = UNSET
        else:
            instance_uid = UUID(_instance_uid)

        _site_uid = d.pop("siteUid", UNSET)
        site_uid: UUID | Unset
        if isinstance(_site_uid, Unset):
            site_uid = UNSET
        else:
            site_uid = UUID(_site_uid)

        _reseller_uid = d.pop("resellerUid", UNSET)
        reseller_uid: UUID | Unset
        if isinstance(_reseller_uid, Unset):
            reseller_uid = UNSET
        else:
            reseller_uid = UUID(_reseller_uid)

        _repository_uid = d.pop("repositoryUid", UNSET)
        repository_uid: UUID | Unset
        if isinstance(_repository_uid, Unset):
            repository_uid = UNSET
        else:
            repository_uid = UUID(_repository_uid)

        def _parse_storage_quota(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        storage_quota = _parse_storage_quota(d.pop("storageQuota", UNSET))

        is_storage_quota_unlimited = d.pop("isStorageQuotaUnlimited", UNSET)

        def _parse_servers_quota(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        servers_quota = _parse_servers_quota(d.pop("serversQuota", UNSET))

        is_servers_quota_unlimited = d.pop("isServersQuotaUnlimited", UNSET)

        def _parse_workstations_quota(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        workstations_quota = _parse_workstations_quota(d.pop("workstationsQuota", UNSET))

        is_workstations_quota_unlimited = d.pop("isWorkstationsQuotaUnlimited", UNSET)

        def _parse_vms_quota(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        vms_quota = _parse_vms_quota(d.pop("vmsQuota", UNSET))

        is_vms_quota_unlimited = d.pop("isVmsQuotaUnlimited", UNSET)

        reseller_site_backup_resource = cls(
            resource_friendly_name=resource_friendly_name,
            instance_uid=instance_uid,
            site_uid=site_uid,
            reseller_uid=reseller_uid,
            repository_uid=repository_uid,
            storage_quota=storage_quota,
            is_storage_quota_unlimited=is_storage_quota_unlimited,
            servers_quota=servers_quota,
            is_servers_quota_unlimited=is_servers_quota_unlimited,
            workstations_quota=workstations_quota,
            is_workstations_quota_unlimited=is_workstations_quota_unlimited,
            vms_quota=vms_quota,
            is_vms_quota_unlimited=is_vms_quota_unlimited,
        )

        reseller_site_backup_resource.additional_properties = d
        return reseller_site_backup_resource

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
