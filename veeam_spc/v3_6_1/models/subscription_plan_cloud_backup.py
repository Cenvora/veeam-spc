from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.subscription_plan_cloud_backup_archive_tier_used_space_units import (
    SubscriptionPlanCloudBackupArchiveTierUsedSpaceUnits,
)
from ..models.subscription_plan_cloud_backup_backup_data_transfer_out_units import (
    SubscriptionPlanCloudBackupBackupDataTransferOutUnits,
)
from ..models.subscription_plan_cloud_backup_capacity_tier_used_space_units import (
    SubscriptionPlanCloudBackupCapacityTierUsedSpaceUnits,
)
from ..models.subscription_plan_cloud_backup_cloud_repository_allocated_space_units import (
    SubscriptionPlanCloudBackupCloudRepositoryAllocatedSpaceUnits,
)
from ..models.subscription_plan_cloud_backup_cloud_repository_consumed_space_units import (
    SubscriptionPlanCloudBackupCloudRepositoryConsumedSpaceUnits,
)
from ..models.subscription_plan_cloud_backup_cloud_repository_space_usage_algorithm import (
    SubscriptionPlanCloudBackupCloudRepositorySpaceUsageAlgorithm,
)
from ..models.subscription_plan_cloud_backup_free_cloud_repository_consumed_space_units import (
    SubscriptionPlanCloudBackupFreeCloudRepositoryConsumedSpaceUnits,
)
from ..models.subscription_plan_cloud_backup_insider_protection_used_space_units import (
    SubscriptionPlanCloudBackupInsiderProtectionUsedSpaceUnits,
)
from ..models.subscription_plan_cloud_backup_performance_tier_used_space_units import (
    SubscriptionPlanCloudBackupPerformanceTierUsedSpaceUnits,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="SubscriptionPlanCloudBackup")


@_attrs_define
class SubscriptionPlanCloudBackup:
    """
    Attributes:
        round_up_used_space (Union[Unset, bool]): Indicates whether storage usage cost must be rounded up to a full data
            block cost when the consumed storage space does not match data block size. Default: False.
        vm_cloud_backups_price (Union[Unset, float]): Charge rate for storing one VM in backup on a cloud repository,
            per month. Default: 0.0.
        server_cloud_backups_price (Union[Unset, float]): Charge rate for storing backup data of one server computer on
            a cloud repository, per month. Default: 0.0.
        workstation_cloud_backups_price (Union[Unset, float]): Charge rate for storing backup data for one workstation
            computer on a cloud repository, per month. Default: 0.0.
        cloud_repository_space_usage_algorithm (Union[Unset,
            SubscriptionPlanCloudBackupCloudRepositorySpaceUsageAlgorithm]): Type of charge rate for storage space on a
            cloud repository. Default: SubscriptionPlanCloudBackupCloudRepositorySpaceUsageAlgorithm.CONSUMED.
        cloud_repository_allocated_space_price (Union[Unset, float]): Charge rate for one GB or TB of allocated storage
            space on a cloud repository. Default: 0.0.
        cloud_repository_allocated_space_units (Union[Unset,
            SubscriptionPlanCloudBackupCloudRepositoryAllocatedSpaceUnits]): Measurement units of allocated storage space on
            a cloud repository. Default: SubscriptionPlanCloudBackupCloudRepositoryAllocatedSpaceUnits.GB.
        cloud_repository_consumed_space_price (Union[Unset, float]): Charge rate for a block of consumed storage space
            on a cloud repository. Default: 0.0.
        cloud_repository_consumed_space_chunk_size (Union[Unset, int]): Size of a block of consumed storage space on a
            cloud repository. Default: 1.
        cloud_repository_consumed_space_units (Union[Unset,
            SubscriptionPlanCloudBackupCloudRepositoryConsumedSpaceUnits]): Measurement units of consumed storage space on a
            cloud repository. Default: SubscriptionPlanCloudBackupCloudRepositoryConsumedSpaceUnits.TB.
        free_cloud_repository_consumed_space (Union[None, Unset, int]): Amount of storage space that can be consumed by
            backup files for free.
            > Maximum value is `1048576` for GB and `1024` for TB.
        free_cloud_repository_consumed_space_units (Union[Unset,
            SubscriptionPlanCloudBackupFreeCloudRepositoryConsumedSpaceUnits]): Measurement units of storage space that can
            be consumed by backup files for free. Default:
            SubscriptionPlanCloudBackupFreeCloudRepositoryConsumedSpaceUnits.GB.
        backup_data_transfer_out_price (Union[Unset, float]): Charge rate for one GB or TB of data downloaded from a
            cloud repository Default: 0.0.
        backup_data_transfer_out_units (Union[Unset, SubscriptionPlanCloudBackupBackupDataTransferOutUnits]):
            Measurement units of data downloaded from a cloud repository. Default:
            SubscriptionPlanCloudBackupBackupDataTransferOutUnits.GB.
        insider_protection_used_space_price (Union[Unset, float]): Charge rate for cloud repository space that is
            consumed by deleted backup files. Default: 0.0.
        insider_protection_used_space_units (Union[Unset, SubscriptionPlanCloudBackupInsiderProtectionUsedSpaceUnits]):
            Measurement units of cloud repository space that is consumed by deleted backup files. Default:
            SubscriptionPlanCloudBackupInsiderProtectionUsedSpaceUnits.GB.
        performance_tier_used_space_price (Union[Unset, float]): Charge rate for a block of consumed performance tier
            space. Default: 0.0.
        performance_tier_used_space_chunk_size (Union[Unset, int]): Size of a consumed performance tier space block.
            Default: 1.
        performance_tier_used_space_units (Union[Unset, SubscriptionPlanCloudBackupPerformanceTierUsedSpaceUnits]):
            Measurement units of blocks of consumed performance tier space. Default:
            SubscriptionPlanCloudBackupPerformanceTierUsedSpaceUnits.GB.
        capacity_tier_used_space_price (Union[Unset, float]): Charge rate for a block of consumed capacity tier space.
            Default: 0.0.
        capacity_tier_used_space_chunk_size (Union[Unset, int]): Size of a consumed capacity tier space block. Default:
            1.
        capacity_tier_used_space_units (Union[Unset, SubscriptionPlanCloudBackupCapacityTierUsedSpaceUnits]):
            Measurement units of consumed capacity tier space. Default:
            SubscriptionPlanCloudBackupCapacityTierUsedSpaceUnits.GB.
        archive_tier_used_space_price (Union[Unset, float]): Charge rate for a block of consumed archive tier space.
            Default: 0.0.
        archive_tier_used_space_chunk_size (Union[Unset, int]): Size of a consumed archive tier space block. Default: 1.
        archive_tier_used_space_units (Union[Unset, SubscriptionPlanCloudBackupArchiveTierUsedSpaceUnits]): Measurement
            units of consumed archive tier space. Default: SubscriptionPlanCloudBackupArchiveTierUsedSpaceUnits.GB.
    """

    round_up_used_space: Union[Unset, bool] = False
    vm_cloud_backups_price: Union[Unset, float] = 0.0
    server_cloud_backups_price: Union[Unset, float] = 0.0
    workstation_cloud_backups_price: Union[Unset, float] = 0.0
    cloud_repository_space_usage_algorithm: Union[
        Unset, SubscriptionPlanCloudBackupCloudRepositorySpaceUsageAlgorithm
    ] = SubscriptionPlanCloudBackupCloudRepositorySpaceUsageAlgorithm.CONSUMED
    cloud_repository_allocated_space_price: Union[Unset, float] = 0.0
    cloud_repository_allocated_space_units: Union[
        Unset, SubscriptionPlanCloudBackupCloudRepositoryAllocatedSpaceUnits
    ] = SubscriptionPlanCloudBackupCloudRepositoryAllocatedSpaceUnits.GB
    cloud_repository_consumed_space_price: Union[Unset, float] = 0.0
    cloud_repository_consumed_space_chunk_size: Union[Unset, int] = 1
    cloud_repository_consumed_space_units: Union[
        Unset, SubscriptionPlanCloudBackupCloudRepositoryConsumedSpaceUnits
    ] = SubscriptionPlanCloudBackupCloudRepositoryConsumedSpaceUnits.TB
    free_cloud_repository_consumed_space: Union[None, Unset, int] = UNSET
    free_cloud_repository_consumed_space_units: Union[
        Unset, SubscriptionPlanCloudBackupFreeCloudRepositoryConsumedSpaceUnits
    ] = SubscriptionPlanCloudBackupFreeCloudRepositoryConsumedSpaceUnits.GB
    backup_data_transfer_out_price: Union[Unset, float] = 0.0
    backup_data_transfer_out_units: Union[Unset, SubscriptionPlanCloudBackupBackupDataTransferOutUnits] = (
        SubscriptionPlanCloudBackupBackupDataTransferOutUnits.GB
    )
    insider_protection_used_space_price: Union[Unset, float] = 0.0
    insider_protection_used_space_units: Union[Unset, SubscriptionPlanCloudBackupInsiderProtectionUsedSpaceUnits] = (
        SubscriptionPlanCloudBackupInsiderProtectionUsedSpaceUnits.GB
    )
    performance_tier_used_space_price: Union[Unset, float] = 0.0
    performance_tier_used_space_chunk_size: Union[Unset, int] = 1
    performance_tier_used_space_units: Union[Unset, SubscriptionPlanCloudBackupPerformanceTierUsedSpaceUnits] = (
        SubscriptionPlanCloudBackupPerformanceTierUsedSpaceUnits.GB
    )
    capacity_tier_used_space_price: Union[Unset, float] = 0.0
    capacity_tier_used_space_chunk_size: Union[Unset, int] = 1
    capacity_tier_used_space_units: Union[Unset, SubscriptionPlanCloudBackupCapacityTierUsedSpaceUnits] = (
        SubscriptionPlanCloudBackupCapacityTierUsedSpaceUnits.GB
    )
    archive_tier_used_space_price: Union[Unset, float] = 0.0
    archive_tier_used_space_chunk_size: Union[Unset, int] = 1
    archive_tier_used_space_units: Union[Unset, SubscriptionPlanCloudBackupArchiveTierUsedSpaceUnits] = (
        SubscriptionPlanCloudBackupArchiveTierUsedSpaceUnits.GB
    )
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        round_up_used_space = self.round_up_used_space

        vm_cloud_backups_price = self.vm_cloud_backups_price

        server_cloud_backups_price = self.server_cloud_backups_price

        workstation_cloud_backups_price = self.workstation_cloud_backups_price

        cloud_repository_space_usage_algorithm: Union[Unset, str] = UNSET
        if not isinstance(self.cloud_repository_space_usage_algorithm, Unset):
            cloud_repository_space_usage_algorithm = self.cloud_repository_space_usage_algorithm.value

        cloud_repository_allocated_space_price = self.cloud_repository_allocated_space_price

        cloud_repository_allocated_space_units: Union[Unset, str] = UNSET
        if not isinstance(self.cloud_repository_allocated_space_units, Unset):
            cloud_repository_allocated_space_units = self.cloud_repository_allocated_space_units.value

        cloud_repository_consumed_space_price = self.cloud_repository_consumed_space_price

        cloud_repository_consumed_space_chunk_size = self.cloud_repository_consumed_space_chunk_size

        cloud_repository_consumed_space_units: Union[Unset, str] = UNSET
        if not isinstance(self.cloud_repository_consumed_space_units, Unset):
            cloud_repository_consumed_space_units = self.cloud_repository_consumed_space_units.value

        free_cloud_repository_consumed_space: Union[None, Unset, int]
        if isinstance(self.free_cloud_repository_consumed_space, Unset):
            free_cloud_repository_consumed_space = UNSET
        else:
            free_cloud_repository_consumed_space = self.free_cloud_repository_consumed_space

        free_cloud_repository_consumed_space_units: Union[Unset, str] = UNSET
        if not isinstance(self.free_cloud_repository_consumed_space_units, Unset):
            free_cloud_repository_consumed_space_units = self.free_cloud_repository_consumed_space_units.value

        backup_data_transfer_out_price = self.backup_data_transfer_out_price

        backup_data_transfer_out_units: Union[Unset, str] = UNSET
        if not isinstance(self.backup_data_transfer_out_units, Unset):
            backup_data_transfer_out_units = self.backup_data_transfer_out_units.value

        insider_protection_used_space_price = self.insider_protection_used_space_price

        insider_protection_used_space_units: Union[Unset, str] = UNSET
        if not isinstance(self.insider_protection_used_space_units, Unset):
            insider_protection_used_space_units = self.insider_protection_used_space_units.value

        performance_tier_used_space_price = self.performance_tier_used_space_price

        performance_tier_used_space_chunk_size = self.performance_tier_used_space_chunk_size

        performance_tier_used_space_units: Union[Unset, str] = UNSET
        if not isinstance(self.performance_tier_used_space_units, Unset):
            performance_tier_used_space_units = self.performance_tier_used_space_units.value

        capacity_tier_used_space_price = self.capacity_tier_used_space_price

        capacity_tier_used_space_chunk_size = self.capacity_tier_used_space_chunk_size

        capacity_tier_used_space_units: Union[Unset, str] = UNSET
        if not isinstance(self.capacity_tier_used_space_units, Unset):
            capacity_tier_used_space_units = self.capacity_tier_used_space_units.value

        archive_tier_used_space_price = self.archive_tier_used_space_price

        archive_tier_used_space_chunk_size = self.archive_tier_used_space_chunk_size

        archive_tier_used_space_units: Union[Unset, str] = UNSET
        if not isinstance(self.archive_tier_used_space_units, Unset):
            archive_tier_used_space_units = self.archive_tier_used_space_units.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if round_up_used_space is not UNSET:
            field_dict["roundUpUsedSpace"] = round_up_used_space
        if vm_cloud_backups_price is not UNSET:
            field_dict["vmCloudBackupsPrice"] = vm_cloud_backups_price
        if server_cloud_backups_price is not UNSET:
            field_dict["serverCloudBackupsPrice"] = server_cloud_backups_price
        if workstation_cloud_backups_price is not UNSET:
            field_dict["workstationCloudBackupsPrice"] = workstation_cloud_backups_price
        if cloud_repository_space_usage_algorithm is not UNSET:
            field_dict["cloudRepositorySpaceUsageAlgorithm"] = cloud_repository_space_usage_algorithm
        if cloud_repository_allocated_space_price is not UNSET:
            field_dict["cloudRepositoryAllocatedSpacePrice"] = cloud_repository_allocated_space_price
        if cloud_repository_allocated_space_units is not UNSET:
            field_dict["cloudRepositoryAllocatedSpaceUnits"] = cloud_repository_allocated_space_units
        if cloud_repository_consumed_space_price is not UNSET:
            field_dict["cloudRepositoryConsumedSpacePrice"] = cloud_repository_consumed_space_price
        if cloud_repository_consumed_space_chunk_size is not UNSET:
            field_dict["cloudRepositoryConsumedSpaceChunkSize"] = cloud_repository_consumed_space_chunk_size
        if cloud_repository_consumed_space_units is not UNSET:
            field_dict["cloudRepositoryConsumedSpaceUnits"] = cloud_repository_consumed_space_units
        if free_cloud_repository_consumed_space is not UNSET:
            field_dict["freeCloudRepositoryConsumedSpace"] = free_cloud_repository_consumed_space
        if free_cloud_repository_consumed_space_units is not UNSET:
            field_dict["freeCloudRepositoryConsumedSpaceUnits"] = free_cloud_repository_consumed_space_units
        if backup_data_transfer_out_price is not UNSET:
            field_dict["backupDataTransferOutPrice"] = backup_data_transfer_out_price
        if backup_data_transfer_out_units is not UNSET:
            field_dict["backupDataTransferOutUnits"] = backup_data_transfer_out_units
        if insider_protection_used_space_price is not UNSET:
            field_dict["insiderProtectionUsedSpacePrice"] = insider_protection_used_space_price
        if insider_protection_used_space_units is not UNSET:
            field_dict["insiderProtectionUsedSpaceUnits"] = insider_protection_used_space_units
        if performance_tier_used_space_price is not UNSET:
            field_dict["performanceTierUsedSpacePrice"] = performance_tier_used_space_price
        if performance_tier_used_space_chunk_size is not UNSET:
            field_dict["performanceTierUsedSpaceChunkSize"] = performance_tier_used_space_chunk_size
        if performance_tier_used_space_units is not UNSET:
            field_dict["performanceTierUsedSpaceUnits"] = performance_tier_used_space_units
        if capacity_tier_used_space_price is not UNSET:
            field_dict["capacityTierUsedSpacePrice"] = capacity_tier_used_space_price
        if capacity_tier_used_space_chunk_size is not UNSET:
            field_dict["capacityTierUsedSpaceChunkSize"] = capacity_tier_used_space_chunk_size
        if capacity_tier_used_space_units is not UNSET:
            field_dict["capacityTierUsedSpaceUnits"] = capacity_tier_used_space_units
        if archive_tier_used_space_price is not UNSET:
            field_dict["archiveTierUsedSpacePrice"] = archive_tier_used_space_price
        if archive_tier_used_space_chunk_size is not UNSET:
            field_dict["archiveTierUsedSpaceChunkSize"] = archive_tier_used_space_chunk_size
        if archive_tier_used_space_units is not UNSET:
            field_dict["archiveTierUsedSpaceUnits"] = archive_tier_used_space_units

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        round_up_used_space = d.pop("roundUpUsedSpace", UNSET)

        vm_cloud_backups_price = d.pop("vmCloudBackupsPrice", UNSET)

        server_cloud_backups_price = d.pop("serverCloudBackupsPrice", UNSET)

        workstation_cloud_backups_price = d.pop("workstationCloudBackupsPrice", UNSET)

        _cloud_repository_space_usage_algorithm = d.pop("cloudRepositorySpaceUsageAlgorithm", UNSET)
        cloud_repository_space_usage_algorithm: Union[
            Unset, SubscriptionPlanCloudBackupCloudRepositorySpaceUsageAlgorithm
        ]
        if isinstance(_cloud_repository_space_usage_algorithm, Unset):
            cloud_repository_space_usage_algorithm = UNSET
        else:
            cloud_repository_space_usage_algorithm = SubscriptionPlanCloudBackupCloudRepositorySpaceUsageAlgorithm(
                _cloud_repository_space_usage_algorithm
            )

        cloud_repository_allocated_space_price = d.pop("cloudRepositoryAllocatedSpacePrice", UNSET)

        _cloud_repository_allocated_space_units = d.pop("cloudRepositoryAllocatedSpaceUnits", UNSET)
        cloud_repository_allocated_space_units: Union[
            Unset, SubscriptionPlanCloudBackupCloudRepositoryAllocatedSpaceUnits
        ]
        if isinstance(_cloud_repository_allocated_space_units, Unset):
            cloud_repository_allocated_space_units = UNSET
        else:
            cloud_repository_allocated_space_units = SubscriptionPlanCloudBackupCloudRepositoryAllocatedSpaceUnits(
                _cloud_repository_allocated_space_units
            )

        cloud_repository_consumed_space_price = d.pop("cloudRepositoryConsumedSpacePrice", UNSET)

        cloud_repository_consumed_space_chunk_size = d.pop("cloudRepositoryConsumedSpaceChunkSize", UNSET)

        _cloud_repository_consumed_space_units = d.pop("cloudRepositoryConsumedSpaceUnits", UNSET)
        cloud_repository_consumed_space_units: Union[
            Unset, SubscriptionPlanCloudBackupCloudRepositoryConsumedSpaceUnits
        ]
        if isinstance(_cloud_repository_consumed_space_units, Unset):
            cloud_repository_consumed_space_units = UNSET
        else:
            cloud_repository_consumed_space_units = SubscriptionPlanCloudBackupCloudRepositoryConsumedSpaceUnits(
                _cloud_repository_consumed_space_units
            )

        def _parse_free_cloud_repository_consumed_space(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        free_cloud_repository_consumed_space = _parse_free_cloud_repository_consumed_space(
            d.pop("freeCloudRepositoryConsumedSpace", UNSET)
        )

        _free_cloud_repository_consumed_space_units = d.pop("freeCloudRepositoryConsumedSpaceUnits", UNSET)
        free_cloud_repository_consumed_space_units: Union[
            Unset, SubscriptionPlanCloudBackupFreeCloudRepositoryConsumedSpaceUnits
        ]
        if isinstance(_free_cloud_repository_consumed_space_units, Unset):
            free_cloud_repository_consumed_space_units = UNSET
        else:
            free_cloud_repository_consumed_space_units = (
                SubscriptionPlanCloudBackupFreeCloudRepositoryConsumedSpaceUnits(
                    _free_cloud_repository_consumed_space_units
                )
            )

        backup_data_transfer_out_price = d.pop("backupDataTransferOutPrice", UNSET)

        _backup_data_transfer_out_units = d.pop("backupDataTransferOutUnits", UNSET)
        backup_data_transfer_out_units: Union[Unset, SubscriptionPlanCloudBackupBackupDataTransferOutUnits]
        if isinstance(_backup_data_transfer_out_units, Unset):
            backup_data_transfer_out_units = UNSET
        else:
            backup_data_transfer_out_units = SubscriptionPlanCloudBackupBackupDataTransferOutUnits(
                _backup_data_transfer_out_units
            )

        insider_protection_used_space_price = d.pop("insiderProtectionUsedSpacePrice", UNSET)

        _insider_protection_used_space_units = d.pop("insiderProtectionUsedSpaceUnits", UNSET)
        insider_protection_used_space_units: Union[Unset, SubscriptionPlanCloudBackupInsiderProtectionUsedSpaceUnits]
        if isinstance(_insider_protection_used_space_units, Unset):
            insider_protection_used_space_units = UNSET
        else:
            insider_protection_used_space_units = SubscriptionPlanCloudBackupInsiderProtectionUsedSpaceUnits(
                _insider_protection_used_space_units
            )

        performance_tier_used_space_price = d.pop("performanceTierUsedSpacePrice", UNSET)

        performance_tier_used_space_chunk_size = d.pop("performanceTierUsedSpaceChunkSize", UNSET)

        _performance_tier_used_space_units = d.pop("performanceTierUsedSpaceUnits", UNSET)
        performance_tier_used_space_units: Union[Unset, SubscriptionPlanCloudBackupPerformanceTierUsedSpaceUnits]
        if isinstance(_performance_tier_used_space_units, Unset):
            performance_tier_used_space_units = UNSET
        else:
            performance_tier_used_space_units = SubscriptionPlanCloudBackupPerformanceTierUsedSpaceUnits(
                _performance_tier_used_space_units
            )

        capacity_tier_used_space_price = d.pop("capacityTierUsedSpacePrice", UNSET)

        capacity_tier_used_space_chunk_size = d.pop("capacityTierUsedSpaceChunkSize", UNSET)

        _capacity_tier_used_space_units = d.pop("capacityTierUsedSpaceUnits", UNSET)
        capacity_tier_used_space_units: Union[Unset, SubscriptionPlanCloudBackupCapacityTierUsedSpaceUnits]
        if isinstance(_capacity_tier_used_space_units, Unset):
            capacity_tier_used_space_units = UNSET
        else:
            capacity_tier_used_space_units = SubscriptionPlanCloudBackupCapacityTierUsedSpaceUnits(
                _capacity_tier_used_space_units
            )

        archive_tier_used_space_price = d.pop("archiveTierUsedSpacePrice", UNSET)

        archive_tier_used_space_chunk_size = d.pop("archiveTierUsedSpaceChunkSize", UNSET)

        _archive_tier_used_space_units = d.pop("archiveTierUsedSpaceUnits", UNSET)
        archive_tier_used_space_units: Union[Unset, SubscriptionPlanCloudBackupArchiveTierUsedSpaceUnits]
        if isinstance(_archive_tier_used_space_units, Unset):
            archive_tier_used_space_units = UNSET
        else:
            archive_tier_used_space_units = SubscriptionPlanCloudBackupArchiveTierUsedSpaceUnits(
                _archive_tier_used_space_units
            )

        subscription_plan_cloud_backup = cls(
            round_up_used_space=round_up_used_space,
            vm_cloud_backups_price=vm_cloud_backups_price,
            server_cloud_backups_price=server_cloud_backups_price,
            workstation_cloud_backups_price=workstation_cloud_backups_price,
            cloud_repository_space_usage_algorithm=cloud_repository_space_usage_algorithm,
            cloud_repository_allocated_space_price=cloud_repository_allocated_space_price,
            cloud_repository_allocated_space_units=cloud_repository_allocated_space_units,
            cloud_repository_consumed_space_price=cloud_repository_consumed_space_price,
            cloud_repository_consumed_space_chunk_size=cloud_repository_consumed_space_chunk_size,
            cloud_repository_consumed_space_units=cloud_repository_consumed_space_units,
            free_cloud_repository_consumed_space=free_cloud_repository_consumed_space,
            free_cloud_repository_consumed_space_units=free_cloud_repository_consumed_space_units,
            backup_data_transfer_out_price=backup_data_transfer_out_price,
            backup_data_transfer_out_units=backup_data_transfer_out_units,
            insider_protection_used_space_price=insider_protection_used_space_price,
            insider_protection_used_space_units=insider_protection_used_space_units,
            performance_tier_used_space_price=performance_tier_used_space_price,
            performance_tier_used_space_chunk_size=performance_tier_used_space_chunk_size,
            performance_tier_used_space_units=performance_tier_used_space_units,
            capacity_tier_used_space_price=capacity_tier_used_space_price,
            capacity_tier_used_space_chunk_size=capacity_tier_used_space_chunk_size,
            capacity_tier_used_space_units=capacity_tier_used_space_units,
            archive_tier_used_space_price=archive_tier_used_space_price,
            archive_tier_used_space_chunk_size=archive_tier_used_space_chunk_size,
            archive_tier_used_space_units=archive_tier_used_space_units,
        )

        subscription_plan_cloud_backup.additional_properties = d
        return subscription_plan_cloud_backup

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
