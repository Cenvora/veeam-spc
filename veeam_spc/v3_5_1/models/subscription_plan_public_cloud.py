from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.subscription_plan_public_cloud_archive_used_space_units import (
    SubscriptionPlanPublicCloudArchiveUsedSpaceUnits,
)
from ..models.subscription_plan_public_cloud_backup_used_space_units import (
    SubscriptionPlanPublicCloudBackupUsedSpaceUnits,
)
from ..models.subscription_plan_public_cloud_free_archive_used_space_units import (
    SubscriptionPlanPublicCloudFreeArchiveUsedSpaceUnits,
)
from ..models.subscription_plan_public_cloud_free_backup_used_space_units import (
    SubscriptionPlanPublicCloudFreeBackupUsedSpaceUnits,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="SubscriptionPlanPublicCloud")


@_attrs_define
class SubscriptionPlanPublicCloud:
    """
    Attributes:
        cloud_vm_price (Union[Unset, float]): Charge rate for a managed cloud VM. Default: 0.0.
        free_cloud_vms (Union[Unset, int]): Number of cloud VMs that are managed for free. Default: 0.
        cloud_file_share_price (Union[Unset, float]): Charge rate for a managed cloud file share. Default: 0.0.
        free_cloud_file_shares (Union[Unset, int]): Number of cloud file shares that are managed for free. Default: 0.
        cloud_database_price (Union[Unset, float]): Charge rate for a managed cloud database. Default: 0.0.
        free_cloud_databases (Union[Unset, int]): Number of cloud databases that are managed for free. Default: 0.
        cloud_network_price (Union[Unset, float]): Charge rate for a managed cloud network. Default: 0.0.
        free_cloud_networks (Union[Unset, int]): Number of cloud networks that are managed for free. Default: 0.
        backup_used_space_price (Union[Unset, float]): Charge rate for one GB or TB of consumed space on backup
            repository. Default: 0.0.
        backup_used_space_units (Union[Unset, SubscriptionPlanPublicCloudBackupUsedSpaceUnits]): Measurement units of
            consumed space on backup repository. Default: SubscriptionPlanPublicCloudBackupUsedSpaceUnits.GB.
        free_backup_used_space (Union[Unset, int]): Amount of consumed space on backup repository that is processed for
            free.
            > Maximum value is `1048576` for GB and `1024` for TB.
        free_backup_used_space_units (Union[Unset, SubscriptionPlanPublicCloudFreeBackupUsedSpaceUnits]): Measurement
            units of consumed space on backup repository that is processed for free. Default:
            SubscriptionPlanPublicCloudFreeBackupUsedSpaceUnits.GB.
        archive_used_space_price (Union[Unset, float]): Charge rate for one GB or TB of consumed space on archive
            repository. Default: 0.0.
        archive_used_space_units (Union[Unset, SubscriptionPlanPublicCloudArchiveUsedSpaceUnits]): Measurement units of
            consumed space on archive repository. Default: SubscriptionPlanPublicCloudArchiveUsedSpaceUnits.GB.
        free_archive_used_space (Union[Unset, int]): Amount of consumed space on archive repository that is processed
            for free.
            > Maximum value is `1048576` for GB and `1024` for TB.
        free_archive_used_space_units (Union[Unset, SubscriptionPlanPublicCloudFreeArchiveUsedSpaceUnits]): Measurement
            units of consumed space on archive repository that is processed for free. Default:
            SubscriptionPlanPublicCloudFreeArchiveUsedSpaceUnits.GB.
    """

    cloud_vm_price: Union[Unset, float] = 0.0
    free_cloud_vms: Union[Unset, int] = 0
    cloud_file_share_price: Union[Unset, float] = 0.0
    free_cloud_file_shares: Union[Unset, int] = 0
    cloud_database_price: Union[Unset, float] = 0.0
    free_cloud_databases: Union[Unset, int] = 0
    cloud_network_price: Union[Unset, float] = 0.0
    free_cloud_networks: Union[Unset, int] = 0
    backup_used_space_price: Union[Unset, float] = 0.0
    backup_used_space_units: Union[Unset, SubscriptionPlanPublicCloudBackupUsedSpaceUnits] = (
        SubscriptionPlanPublicCloudBackupUsedSpaceUnits.GB
    )
    free_backup_used_space: Union[Unset, int] = UNSET
    free_backup_used_space_units: Union[Unset, SubscriptionPlanPublicCloudFreeBackupUsedSpaceUnits] = (
        SubscriptionPlanPublicCloudFreeBackupUsedSpaceUnits.GB
    )
    archive_used_space_price: Union[Unset, float] = 0.0
    archive_used_space_units: Union[Unset, SubscriptionPlanPublicCloudArchiveUsedSpaceUnits] = (
        SubscriptionPlanPublicCloudArchiveUsedSpaceUnits.GB
    )
    free_archive_used_space: Union[Unset, int] = UNSET
    free_archive_used_space_units: Union[Unset, SubscriptionPlanPublicCloudFreeArchiveUsedSpaceUnits] = (
        SubscriptionPlanPublicCloudFreeArchiveUsedSpaceUnits.GB
    )
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cloud_vm_price = self.cloud_vm_price

        free_cloud_vms = self.free_cloud_vms

        cloud_file_share_price = self.cloud_file_share_price

        free_cloud_file_shares = self.free_cloud_file_shares

        cloud_database_price = self.cloud_database_price

        free_cloud_databases = self.free_cloud_databases

        cloud_network_price = self.cloud_network_price

        free_cloud_networks = self.free_cloud_networks

        backup_used_space_price = self.backup_used_space_price

        backup_used_space_units: Union[Unset, str] = UNSET
        if not isinstance(self.backup_used_space_units, Unset):
            backup_used_space_units = self.backup_used_space_units.value

        free_backup_used_space = self.free_backup_used_space

        free_backup_used_space_units: Union[Unset, str] = UNSET
        if not isinstance(self.free_backup_used_space_units, Unset):
            free_backup_used_space_units = self.free_backup_used_space_units.value

        archive_used_space_price = self.archive_used_space_price

        archive_used_space_units: Union[Unset, str] = UNSET
        if not isinstance(self.archive_used_space_units, Unset):
            archive_used_space_units = self.archive_used_space_units.value

        free_archive_used_space = self.free_archive_used_space

        free_archive_used_space_units: Union[Unset, str] = UNSET
        if not isinstance(self.free_archive_used_space_units, Unset):
            free_archive_used_space_units = self.free_archive_used_space_units.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cloud_vm_price is not UNSET:
            field_dict["cloudVmPrice"] = cloud_vm_price
        if free_cloud_vms is not UNSET:
            field_dict["freeCloudVms"] = free_cloud_vms
        if cloud_file_share_price is not UNSET:
            field_dict["cloudFileSharePrice"] = cloud_file_share_price
        if free_cloud_file_shares is not UNSET:
            field_dict["freeCloudFileShares"] = free_cloud_file_shares
        if cloud_database_price is not UNSET:
            field_dict["cloudDatabasePrice"] = cloud_database_price
        if free_cloud_databases is not UNSET:
            field_dict["freeCloudDatabases"] = free_cloud_databases
        if cloud_network_price is not UNSET:
            field_dict["cloudNetworkPrice"] = cloud_network_price
        if free_cloud_networks is not UNSET:
            field_dict["freeCloudNetworks"] = free_cloud_networks
        if backup_used_space_price is not UNSET:
            field_dict["backupUsedSpacePrice"] = backup_used_space_price
        if backup_used_space_units is not UNSET:
            field_dict["backupUsedSpaceUnits"] = backup_used_space_units
        if free_backup_used_space is not UNSET:
            field_dict["freeBackupUsedSpace"] = free_backup_used_space
        if free_backup_used_space_units is not UNSET:
            field_dict["freeBackupUsedSpaceUnits"] = free_backup_used_space_units
        if archive_used_space_price is not UNSET:
            field_dict["archiveUsedSpacePrice"] = archive_used_space_price
        if archive_used_space_units is not UNSET:
            field_dict["archiveUsedSpaceUnits"] = archive_used_space_units
        if free_archive_used_space is not UNSET:
            field_dict["freeArchiveUsedSpace"] = free_archive_used_space
        if free_archive_used_space_units is not UNSET:
            field_dict["freeArchiveUsedSpaceUnits"] = free_archive_used_space_units

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        cloud_vm_price = d.pop("cloudVmPrice", UNSET)

        free_cloud_vms = d.pop("freeCloudVms", UNSET)

        cloud_file_share_price = d.pop("cloudFileSharePrice", UNSET)

        free_cloud_file_shares = d.pop("freeCloudFileShares", UNSET)

        cloud_database_price = d.pop("cloudDatabasePrice", UNSET)

        free_cloud_databases = d.pop("freeCloudDatabases", UNSET)

        cloud_network_price = d.pop("cloudNetworkPrice", UNSET)

        free_cloud_networks = d.pop("freeCloudNetworks", UNSET)

        backup_used_space_price = d.pop("backupUsedSpacePrice", UNSET)

        _backup_used_space_units = d.pop("backupUsedSpaceUnits", UNSET)
        backup_used_space_units: Union[Unset, SubscriptionPlanPublicCloudBackupUsedSpaceUnits]
        if isinstance(_backup_used_space_units, Unset):
            backup_used_space_units = UNSET
        else:
            backup_used_space_units = SubscriptionPlanPublicCloudBackupUsedSpaceUnits(_backup_used_space_units)

        free_backup_used_space = d.pop("freeBackupUsedSpace", UNSET)

        _free_backup_used_space_units = d.pop("freeBackupUsedSpaceUnits", UNSET)
        free_backup_used_space_units: Union[Unset, SubscriptionPlanPublicCloudFreeBackupUsedSpaceUnits]
        if isinstance(_free_backup_used_space_units, Unset):
            free_backup_used_space_units = UNSET
        else:
            free_backup_used_space_units = SubscriptionPlanPublicCloudFreeBackupUsedSpaceUnits(
                _free_backup_used_space_units
            )

        archive_used_space_price = d.pop("archiveUsedSpacePrice", UNSET)

        _archive_used_space_units = d.pop("archiveUsedSpaceUnits", UNSET)
        archive_used_space_units: Union[Unset, SubscriptionPlanPublicCloudArchiveUsedSpaceUnits]
        if isinstance(_archive_used_space_units, Unset):
            archive_used_space_units = UNSET
        else:
            archive_used_space_units = SubscriptionPlanPublicCloudArchiveUsedSpaceUnits(_archive_used_space_units)

        free_archive_used_space = d.pop("freeArchiveUsedSpace", UNSET)

        _free_archive_used_space_units = d.pop("freeArchiveUsedSpaceUnits", UNSET)
        free_archive_used_space_units: Union[Unset, SubscriptionPlanPublicCloudFreeArchiveUsedSpaceUnits]
        if isinstance(_free_archive_used_space_units, Unset):
            free_archive_used_space_units = UNSET
        else:
            free_archive_used_space_units = SubscriptionPlanPublicCloudFreeArchiveUsedSpaceUnits(
                _free_archive_used_space_units
            )

        subscription_plan_public_cloud = cls(
            cloud_vm_price=cloud_vm_price,
            free_cloud_vms=free_cloud_vms,
            cloud_file_share_price=cloud_file_share_price,
            free_cloud_file_shares=free_cloud_file_shares,
            cloud_database_price=cloud_database_price,
            free_cloud_databases=free_cloud_databases,
            cloud_network_price=cloud_network_price,
            free_cloud_networks=free_cloud_networks,
            backup_used_space_price=backup_used_space_price,
            backup_used_space_units=backup_used_space_units,
            free_backup_used_space=free_backup_used_space,
            free_backup_used_space_units=free_backup_used_space_units,
            archive_used_space_price=archive_used_space_price,
            archive_used_space_units=archive_used_space_units,
            free_archive_used_space=free_archive_used_space,
            free_archive_used_space_units=free_archive_used_space_units,
        )

        subscription_plan_public_cloud.additional_properties = d
        return subscription_plan_public_cloud

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
