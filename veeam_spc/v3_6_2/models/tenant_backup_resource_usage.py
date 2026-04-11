from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TenantBackupResourceUsage")


@_attrs_define
class TenantBackupResourceUsage:
    """
    Attributes:
        company_uid (None | Unset | UUID): UID assigned to a company.
        tenant_uid (UUID | Unset): UID assigned to a tenant.
        backup_resource_uid (UUID | Unset): UID assigned to a cloud backup resource.
        storage_quota (int | Unset): Amount of space allocated to a company, in bytes.
        used_storage_quota (int | Unset): Amount of space consumed by a company, in bytes.
        archive_tier_usage (int | None | Unset): Amount of archive tier space consumed by a company, in bytes.
        capacity_tier_usage (int | None | Unset): Amount of capacity tier space consumed by all company backups
            excluding backup copies, in bytes.
        performance_tier_usage (int | None | Unset): Amount of performance tier space consumed by a company, in bytes.
        server_backups (int | Unset): Number of server backups that a company stores on a cloud repository.
        workstation_backups (int | Unset): Number of workstation backups that a company stores on a cloud repository.
        vm_backups (int | Unset): Number of VM backups that a company stores on a cloud repository.
    """

    company_uid: None | Unset | UUID = UNSET
    tenant_uid: UUID | Unset = UNSET
    backup_resource_uid: UUID | Unset = UNSET
    storage_quota: int | Unset = UNSET
    used_storage_quota: int | Unset = UNSET
    archive_tier_usage: int | None | Unset = UNSET
    capacity_tier_usage: int | None | Unset = UNSET
    performance_tier_usage: int | None | Unset = UNSET
    server_backups: int | Unset = UNSET
    workstation_backups: int | Unset = UNSET
    vm_backups: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        company_uid: None | str | Unset
        if isinstance(self.company_uid, Unset):
            company_uid = UNSET
        elif isinstance(self.company_uid, UUID):
            company_uid = str(self.company_uid)
        else:
            company_uid = self.company_uid

        tenant_uid: str | Unset = UNSET
        if not isinstance(self.tenant_uid, Unset):
            tenant_uid = str(self.tenant_uid)

        backup_resource_uid: str | Unset = UNSET
        if not isinstance(self.backup_resource_uid, Unset):
            backup_resource_uid = str(self.backup_resource_uid)

        storage_quota = self.storage_quota

        used_storage_quota = self.used_storage_quota

        archive_tier_usage: int | None | Unset
        if isinstance(self.archive_tier_usage, Unset):
            archive_tier_usage = UNSET
        else:
            archive_tier_usage = self.archive_tier_usage

        capacity_tier_usage: int | None | Unset
        if isinstance(self.capacity_tier_usage, Unset):
            capacity_tier_usage = UNSET
        else:
            capacity_tier_usage = self.capacity_tier_usage

        performance_tier_usage: int | None | Unset
        if isinstance(self.performance_tier_usage, Unset):
            performance_tier_usage = UNSET
        else:
            performance_tier_usage = self.performance_tier_usage

        server_backups = self.server_backups

        workstation_backups = self.workstation_backups

        vm_backups = self.vm_backups

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if company_uid is not UNSET:
            field_dict["companyUid"] = company_uid
        if tenant_uid is not UNSET:
            field_dict["tenantUid"] = tenant_uid
        if backup_resource_uid is not UNSET:
            field_dict["backupResourceUid"] = backup_resource_uid
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

        def _parse_company_uid(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                company_uid_type_0 = UUID(data)

                return company_uid_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        company_uid = _parse_company_uid(d.pop("companyUid", UNSET))

        _tenant_uid = d.pop("tenantUid", UNSET)
        tenant_uid: UUID | Unset
        if isinstance(_tenant_uid, Unset):
            tenant_uid = UNSET
        else:
            tenant_uid = UUID(_tenant_uid)

        _backup_resource_uid = d.pop("backupResourceUid", UNSET)
        backup_resource_uid: UUID | Unset
        if isinstance(_backup_resource_uid, Unset):
            backup_resource_uid = UNSET
        else:
            backup_resource_uid = UUID(_backup_resource_uid)

        storage_quota = d.pop("storageQuota", UNSET)

        used_storage_quota = d.pop("usedStorageQuota", UNSET)

        def _parse_archive_tier_usage(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        archive_tier_usage = _parse_archive_tier_usage(d.pop("archiveTierUsage", UNSET))

        def _parse_capacity_tier_usage(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        capacity_tier_usage = _parse_capacity_tier_usage(d.pop("capacityTierUsage", UNSET))

        def _parse_performance_tier_usage(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        performance_tier_usage = _parse_performance_tier_usage(d.pop("performanceTierUsage", UNSET))

        server_backups = d.pop("serverBackups", UNSET)

        workstation_backups = d.pop("workstationBackups", UNSET)

        vm_backups = d.pop("vmBackups", UNSET)

        tenant_backup_resource_usage = cls(
            company_uid=company_uid,
            tenant_uid=tenant_uid,
            backup_resource_uid=backup_resource_uid,
            storage_quota=storage_quota,
            used_storage_quota=used_storage_quota,
            archive_tier_usage=archive_tier_usage,
            capacity_tier_usage=capacity_tier_usage,
            performance_tier_usage=performance_tier_usage,
            server_backups=server_backups,
            workstation_backups=workstation_backups,
            vm_backups=vm_backups,
        )

        tenant_backup_resource_usage.additional_properties = d
        return tenant_backup_resource_usage

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
