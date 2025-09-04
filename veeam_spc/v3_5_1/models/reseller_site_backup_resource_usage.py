from collections.abc import Mapping
from typing import Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ResellerSiteBackupResourceUsage")


@_attrs_define
class ResellerSiteBackupResourceUsage:
    """
    Attributes:
        backup_resource_uid (Union[Unset, UUID]): UID assigned to a cloud backup resource.
        reseller_uid (Union[Unset, UUID]): UID assigned to a reseller.
        storage_quota (Union[Unset, int]): Amount of space allocated to a reseller, in bytes.
        used_storage_quota (Union[Unset, int]): Amount of space consumed by all companies of a reseller, in bytes.
        archive_tier_usage (Union[Unset, int]): Amount of archive tier space consumed by all companies of a reseller, in
            bytes.
        capacity_tier_usage (Union[Unset, int]): Amount of capacity tier space consumed by all company backups excluding
            backup copies, in bytes.
        performance_tier_usage (Union[Unset, int]): Amount of performance tier space consumed by all companies of a
            reseller, in bytes.
        server_backups (Union[Unset, int]): Number of server backups that a reseller stores on a cloud repository.
        workstation_backups (Union[Unset, int]): Number of workstation backups that a reseller stores on a cloud
            repository.
        vm_backups (Union[Unset, int]): Number of VM backups that a reseller stores on a cloud repository.
    """

    backup_resource_uid: Union[Unset, UUID] = UNSET
    reseller_uid: Union[Unset, UUID] = UNSET
    storage_quota: Union[Unset, int] = UNSET
    used_storage_quota: Union[Unset, int] = UNSET
    archive_tier_usage: Union[Unset, int] = UNSET
    capacity_tier_usage: Union[Unset, int] = UNSET
    performance_tier_usage: Union[Unset, int] = UNSET
    server_backups: Union[Unset, int] = UNSET
    workstation_backups: Union[Unset, int] = UNSET
    vm_backups: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        backup_resource_uid: Union[Unset, str] = UNSET
        if not isinstance(self.backup_resource_uid, Unset):
            backup_resource_uid = str(self.backup_resource_uid)

        reseller_uid: Union[Unset, str] = UNSET
        if not isinstance(self.reseller_uid, Unset):
            reseller_uid = str(self.reseller_uid)

        storage_quota = self.storage_quota

        used_storage_quota = self.used_storage_quota

        archive_tier_usage = self.archive_tier_usage

        capacity_tier_usage = self.capacity_tier_usage

        performance_tier_usage = self.performance_tier_usage

        server_backups = self.server_backups

        workstation_backups = self.workstation_backups

        vm_backups = self.vm_backups

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if backup_resource_uid is not UNSET:
            field_dict["backupResourceUid"] = backup_resource_uid
        if reseller_uid is not UNSET:
            field_dict["resellerUid"] = reseller_uid
        if storage_quota is not UNSET:
            field_dict["storageQuota"] = storage_quota
        if used_storage_quota is not UNSET:
            field_dict["usedStorageQuota"] = used_storage_quota
        if archive_tier_usage is not UNSET:
            field_dict["archiveTierUsage"] = archive_tier_usage
        if capacity_tier_usage is not UNSET:
            field_dict["capacityTierUsage"] = capacity_tier_usage
        if performance_tier_usage is not UNSET:
            field_dict["performanceTierUsage"] = performance_tier_usage
        if server_backups is not UNSET:
            field_dict["serverBackups"] = server_backups
        if workstation_backups is not UNSET:
            field_dict["workstationBackups"] = workstation_backups
        if vm_backups is not UNSET:
            field_dict["vmBackups"] = vm_backups

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _backup_resource_uid = d.pop("backupResourceUid", UNSET)
        backup_resource_uid: Union[Unset, UUID]
        if isinstance(_backup_resource_uid, Unset):
            backup_resource_uid = UNSET
        else:
            backup_resource_uid = UUID(_backup_resource_uid)

        _reseller_uid = d.pop("resellerUid", UNSET)
        reseller_uid: Union[Unset, UUID]
        if isinstance(_reseller_uid, Unset):
            reseller_uid = UNSET
        else:
            reseller_uid = UUID(_reseller_uid)

        storage_quota = d.pop("storageQuota", UNSET)

        used_storage_quota = d.pop("usedStorageQuota", UNSET)

        archive_tier_usage = d.pop("archiveTierUsage", UNSET)

        capacity_tier_usage = d.pop("capacityTierUsage", UNSET)

        performance_tier_usage = d.pop("performanceTierUsage", UNSET)

        server_backups = d.pop("serverBackups", UNSET)

        workstation_backups = d.pop("workstationBackups", UNSET)

        vm_backups = d.pop("vmBackups", UNSET)

        reseller_site_backup_resource_usage = cls(
            backup_resource_uid=backup_resource_uid,
            reseller_uid=reseller_uid,
            storage_quota=storage_quota,
            used_storage_quota=used_storage_quota,
            archive_tier_usage=archive_tier_usage,
            capacity_tier_usage=capacity_tier_usage,
            performance_tier_usage=performance_tier_usage,
            server_backups=server_backups,
            workstation_backups=workstation_backups,
            vm_backups=vm_backups,
        )

        reseller_site_backup_resource_usage.additional_properties = d
        return reseller_site_backup_resource_usage

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
