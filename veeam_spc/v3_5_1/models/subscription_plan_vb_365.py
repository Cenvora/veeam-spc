from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.subscription_plan_vb_365_archive_storage_used_space_units import (
    SubscriptionPlanVb365ArchiveStorageUsedSpaceUnits,
)
from ..models.subscription_plan_vb_365_free_archive_storage_used_space_units import (
    SubscriptionPlanVb365FreeArchiveStorageUsedSpaceUnits,
)
from ..models.subscription_plan_vb_365_free_standard_storage_used_space_units import (
    SubscriptionPlanVb365FreeStandardStorageUsedSpaceUnits,
)
from ..models.subscription_plan_vb_365_repository_allocated_space_units import (
    SubscriptionPlanVb365RepositoryAllocatedSpaceUnits,
)
from ..models.subscription_plan_vb_365_repository_space_usage_algorithm import (
    SubscriptionPlanVb365RepositorySpaceUsageAlgorithm,
)
from ..models.subscription_plan_vb_365_standard_storage_used_space_units import (
    SubscriptionPlanVb365StandardStorageUsedSpaceUnits,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="SubscriptionPlanVb365")


@_attrs_define
class SubscriptionPlanVb365:
    """
    Attributes:
        subscription_user_price (Union[Unset, float]): Charge rate for a protected Microsoft 365 subscription user.
            Default: 0.0.
        free_subscription_users (Union[Unset, int]): Number of Microsoft 365 subscription user that are managed for
            free. Default: 0.
        educational_user_price (Union[Unset, float]): Charge rate for a protected Microsoft 365 educational subscription
            user. Default: 0.0.
        free_educational_users (Union[Unset, int]): Number of Microsoft 365 educational subscription users that are
            managed for free. Default: 0.
        round_up_used_space (Union[Unset, bool]): Indicates whether storage usage cost must be rounded up to a full data
            block cost when the consumed storage space does not match data block size. Default: False.
        standard_storage_used_space_price (Union[Unset, float]): Charge rate for a block of stored Microsoft 365 backup
            data. Default: 0.0.
        standard_storage_used_space_chunk_size (Union[Unset, int]): Size of a stored Microsoft 365 backup data block.
            Default: 1.
        standard_storage_used_space_units (Union[Unset, SubscriptionPlanVb365StandardStorageUsedSpaceUnits]):
            Measurement units of stored Microsoft 365 backup data block size. Default:
            SubscriptionPlanVb365StandardStorageUsedSpaceUnits.GB.
        free_standard_storage_used_space (Union[Unset, int]): Amount of disk space consumed by Microsoft 365 backups
            that is processed for free.
            > Maximum value is `1048576` for GB and `1024` for TB.
        free_standard_storage_used_space_units (Union[Unset, SubscriptionPlanVb365FreeStandardStorageUsedSpaceUnits]):
            Measurement units of disk space consumed by Microsoft 365 backups that is processed for free. Default:
            SubscriptionPlanVb365FreeStandardStorageUsedSpaceUnits.GB.
        archive_storage_used_space_price (Union[Unset, float]): Charge rate for a block of Microsoft 365 backup copy
            data stored in an archive repository. Default: 0.0.
        archive_storage_used_space_chunk_size (Union[Unset, int]): Size of a data block of Microsoft 365 backup copies
            storedin an archive repository. Default: 1.
        archive_storage_used_space_units (Union[Unset, SubscriptionPlanVb365ArchiveStorageUsedSpaceUnits]): Measurement
            units of Microsoft 365 backup copy data blocks. Default: SubscriptionPlanVb365ArchiveStorageUsedSpaceUnits.GB.
        free_archive_storage_used_space (Union[Unset, int]): Amount of archive repository disk space consumed by
            Microsoft 365 backup copies that is processed for free.
            > Maximum value is `1048576` for GB and `1024` for TB.
        free_archive_storage_used_space_units (Union[Unset, SubscriptionPlanVb365FreeArchiveStorageUsedSpaceUnits]):
            Measurement units of archive repository disk space consumed by Microsoft 365 backup copies that is processed for
            free. Default: SubscriptionPlanVb365FreeArchiveStorageUsedSpaceUnits.GB.
        repository_space_usage_algorithm (Union[Unset, SubscriptionPlanVb365RepositorySpaceUsageAlgorithm]): Type of
            charge rate for storage space on a repository. Default:
            SubscriptionPlanVb365RepositorySpaceUsageAlgorithm.CONSUMED.
        repository_allocated_space_price (Union[Unset, float]): Charge rate for one GB or TB of allocated storage space
            on a repository. Default: 0.0.
        repository_allocated_space_units (Union[Unset, SubscriptionPlanVb365RepositoryAllocatedSpaceUnits]): Measurement
            units of allocated storage space on a repository. Default:
            SubscriptionPlanVb365RepositoryAllocatedSpaceUnits.GB.
    """

    subscription_user_price: Union[Unset, float] = 0.0
    free_subscription_users: Union[Unset, int] = 0
    educational_user_price: Union[Unset, float] = 0.0
    free_educational_users: Union[Unset, int] = 0
    round_up_used_space: Union[Unset, bool] = False
    standard_storage_used_space_price: Union[Unset, float] = 0.0
    standard_storage_used_space_chunk_size: Union[Unset, int] = 1
    standard_storage_used_space_units: Union[Unset, SubscriptionPlanVb365StandardStorageUsedSpaceUnits] = (
        SubscriptionPlanVb365StandardStorageUsedSpaceUnits.GB
    )
    free_standard_storage_used_space: Union[Unset, int] = UNSET
    free_standard_storage_used_space_units: Union[Unset, SubscriptionPlanVb365FreeStandardStorageUsedSpaceUnits] = (
        SubscriptionPlanVb365FreeStandardStorageUsedSpaceUnits.GB
    )
    archive_storage_used_space_price: Union[Unset, float] = 0.0
    archive_storage_used_space_chunk_size: Union[Unset, int] = 1
    archive_storage_used_space_units: Union[Unset, SubscriptionPlanVb365ArchiveStorageUsedSpaceUnits] = (
        SubscriptionPlanVb365ArchiveStorageUsedSpaceUnits.GB
    )
    free_archive_storage_used_space: Union[Unset, int] = UNSET
    free_archive_storage_used_space_units: Union[Unset, SubscriptionPlanVb365FreeArchiveStorageUsedSpaceUnits] = (
        SubscriptionPlanVb365FreeArchiveStorageUsedSpaceUnits.GB
    )
    repository_space_usage_algorithm: Union[Unset, SubscriptionPlanVb365RepositorySpaceUsageAlgorithm] = (
        SubscriptionPlanVb365RepositorySpaceUsageAlgorithm.CONSUMED
    )
    repository_allocated_space_price: Union[Unset, float] = 0.0
    repository_allocated_space_units: Union[Unset, SubscriptionPlanVb365RepositoryAllocatedSpaceUnits] = (
        SubscriptionPlanVb365RepositoryAllocatedSpaceUnits.GB
    )
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        subscription_user_price = self.subscription_user_price

        free_subscription_users = self.free_subscription_users

        educational_user_price = self.educational_user_price

        free_educational_users = self.free_educational_users

        round_up_used_space = self.round_up_used_space

        standard_storage_used_space_price = self.standard_storage_used_space_price

        standard_storage_used_space_chunk_size = self.standard_storage_used_space_chunk_size

        standard_storage_used_space_units: Union[Unset, str] = UNSET
        if not isinstance(self.standard_storage_used_space_units, Unset):
            standard_storage_used_space_units = self.standard_storage_used_space_units.value

        free_standard_storage_used_space = self.free_standard_storage_used_space

        free_standard_storage_used_space_units: Union[Unset, str] = UNSET
        if not isinstance(self.free_standard_storage_used_space_units, Unset):
            free_standard_storage_used_space_units = self.free_standard_storage_used_space_units.value

        archive_storage_used_space_price = self.archive_storage_used_space_price

        archive_storage_used_space_chunk_size = self.archive_storage_used_space_chunk_size

        archive_storage_used_space_units: Union[Unset, str] = UNSET
        if not isinstance(self.archive_storage_used_space_units, Unset):
            archive_storage_used_space_units = self.archive_storage_used_space_units.value

        free_archive_storage_used_space = self.free_archive_storage_used_space

        free_archive_storage_used_space_units: Union[Unset, str] = UNSET
        if not isinstance(self.free_archive_storage_used_space_units, Unset):
            free_archive_storage_used_space_units = self.free_archive_storage_used_space_units.value

        repository_space_usage_algorithm: Union[Unset, str] = UNSET
        if not isinstance(self.repository_space_usage_algorithm, Unset):
            repository_space_usage_algorithm = self.repository_space_usage_algorithm.value

        repository_allocated_space_price = self.repository_allocated_space_price

        repository_allocated_space_units: Union[Unset, str] = UNSET
        if not isinstance(self.repository_allocated_space_units, Unset):
            repository_allocated_space_units = self.repository_allocated_space_units.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if subscription_user_price is not UNSET:
            field_dict["subscriptionUserPrice"] = subscription_user_price
        if free_subscription_users is not UNSET:
            field_dict["freeSubscriptionUsers"] = free_subscription_users
        if educational_user_price is not UNSET:
            field_dict["educationalUserPrice"] = educational_user_price
        if free_educational_users is not UNSET:
            field_dict["freeEducationalUsers"] = free_educational_users
        if round_up_used_space is not UNSET:
            field_dict["roundUpUsedSpace"] = round_up_used_space
        if standard_storage_used_space_price is not UNSET:
            field_dict["standardStorageUsedSpacePrice"] = standard_storage_used_space_price
        if standard_storage_used_space_chunk_size is not UNSET:
            field_dict["standardStorageUsedSpaceChunkSize"] = standard_storage_used_space_chunk_size
        if standard_storage_used_space_units is not UNSET:
            field_dict["standardStorageUsedSpaceUnits"] = standard_storage_used_space_units
        if free_standard_storage_used_space is not UNSET:
            field_dict["freeStandardStorageUsedSpace"] = free_standard_storage_used_space
        if free_standard_storage_used_space_units is not UNSET:
            field_dict["freeStandardStorageUsedSpaceUnits"] = free_standard_storage_used_space_units
        if archive_storage_used_space_price is not UNSET:
            field_dict["archiveStorageUsedSpacePrice"] = archive_storage_used_space_price
        if archive_storage_used_space_chunk_size is not UNSET:
            field_dict["archiveStorageUsedSpaceChunkSize"] = archive_storage_used_space_chunk_size
        if archive_storage_used_space_units is not UNSET:
            field_dict["archiveStorageUsedSpaceUnits"] = archive_storage_used_space_units
        if free_archive_storage_used_space is not UNSET:
            field_dict["freeArchiveStorageUsedSpace"] = free_archive_storage_used_space
        if free_archive_storage_used_space_units is not UNSET:
            field_dict["freeArchiveStorageUsedSpaceUnits"] = free_archive_storage_used_space_units
        if repository_space_usage_algorithm is not UNSET:
            field_dict["repositorySpaceUsageAlgorithm"] = repository_space_usage_algorithm
        if repository_allocated_space_price is not UNSET:
            field_dict["repositoryAllocatedSpacePrice"] = repository_allocated_space_price
        if repository_allocated_space_units is not UNSET:
            field_dict["repositoryAllocatedSpaceUnits"] = repository_allocated_space_units

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        subscription_user_price = d.pop("subscriptionUserPrice", UNSET)

        free_subscription_users = d.pop("freeSubscriptionUsers", UNSET)

        educational_user_price = d.pop("educationalUserPrice", UNSET)

        free_educational_users = d.pop("freeEducationalUsers", UNSET)

        round_up_used_space = d.pop("roundUpUsedSpace", UNSET)

        standard_storage_used_space_price = d.pop("standardStorageUsedSpacePrice", UNSET)

        standard_storage_used_space_chunk_size = d.pop("standardStorageUsedSpaceChunkSize", UNSET)

        _standard_storage_used_space_units = d.pop("standardStorageUsedSpaceUnits", UNSET)
        standard_storage_used_space_units: Union[Unset, SubscriptionPlanVb365StandardStorageUsedSpaceUnits]
        if isinstance(_standard_storage_used_space_units, Unset):
            standard_storage_used_space_units = UNSET
        else:
            standard_storage_used_space_units = SubscriptionPlanVb365StandardStorageUsedSpaceUnits(
                _standard_storage_used_space_units
            )

        free_standard_storage_used_space = d.pop("freeStandardStorageUsedSpace", UNSET)

        _free_standard_storage_used_space_units = d.pop("freeStandardStorageUsedSpaceUnits", UNSET)
        free_standard_storage_used_space_units: Union[Unset, SubscriptionPlanVb365FreeStandardStorageUsedSpaceUnits]
        if isinstance(_free_standard_storage_used_space_units, Unset):
            free_standard_storage_used_space_units = UNSET
        else:
            free_standard_storage_used_space_units = SubscriptionPlanVb365FreeStandardStorageUsedSpaceUnits(
                _free_standard_storage_used_space_units
            )

        archive_storage_used_space_price = d.pop("archiveStorageUsedSpacePrice", UNSET)

        archive_storage_used_space_chunk_size = d.pop("archiveStorageUsedSpaceChunkSize", UNSET)

        _archive_storage_used_space_units = d.pop("archiveStorageUsedSpaceUnits", UNSET)
        archive_storage_used_space_units: Union[Unset, SubscriptionPlanVb365ArchiveStorageUsedSpaceUnits]
        if isinstance(_archive_storage_used_space_units, Unset):
            archive_storage_used_space_units = UNSET
        else:
            archive_storage_used_space_units = SubscriptionPlanVb365ArchiveStorageUsedSpaceUnits(
                _archive_storage_used_space_units
            )

        free_archive_storage_used_space = d.pop("freeArchiveStorageUsedSpace", UNSET)

        _free_archive_storage_used_space_units = d.pop("freeArchiveStorageUsedSpaceUnits", UNSET)
        free_archive_storage_used_space_units: Union[Unset, SubscriptionPlanVb365FreeArchiveStorageUsedSpaceUnits]
        if isinstance(_free_archive_storage_used_space_units, Unset):
            free_archive_storage_used_space_units = UNSET
        else:
            free_archive_storage_used_space_units = SubscriptionPlanVb365FreeArchiveStorageUsedSpaceUnits(
                _free_archive_storage_used_space_units
            )

        _repository_space_usage_algorithm = d.pop("repositorySpaceUsageAlgorithm", UNSET)
        repository_space_usage_algorithm: Union[Unset, SubscriptionPlanVb365RepositorySpaceUsageAlgorithm]
        if isinstance(_repository_space_usage_algorithm, Unset):
            repository_space_usage_algorithm = UNSET
        else:
            repository_space_usage_algorithm = SubscriptionPlanVb365RepositorySpaceUsageAlgorithm(
                _repository_space_usage_algorithm
            )

        repository_allocated_space_price = d.pop("repositoryAllocatedSpacePrice", UNSET)

        _repository_allocated_space_units = d.pop("repositoryAllocatedSpaceUnits", UNSET)
        repository_allocated_space_units: Union[Unset, SubscriptionPlanVb365RepositoryAllocatedSpaceUnits]
        if isinstance(_repository_allocated_space_units, Unset):
            repository_allocated_space_units = UNSET
        else:
            repository_allocated_space_units = SubscriptionPlanVb365RepositoryAllocatedSpaceUnits(
                _repository_allocated_space_units
            )

        subscription_plan_vb_365 = cls(
            subscription_user_price=subscription_user_price,
            free_subscription_users=free_subscription_users,
            educational_user_price=educational_user_price,
            free_educational_users=free_educational_users,
            round_up_used_space=round_up_used_space,
            standard_storage_used_space_price=standard_storage_used_space_price,
            standard_storage_used_space_chunk_size=standard_storage_used_space_chunk_size,
            standard_storage_used_space_units=standard_storage_used_space_units,
            free_standard_storage_used_space=free_standard_storage_used_space,
            free_standard_storage_used_space_units=free_standard_storage_used_space_units,
            archive_storage_used_space_price=archive_storage_used_space_price,
            archive_storage_used_space_chunk_size=archive_storage_used_space_chunk_size,
            archive_storage_used_space_units=archive_storage_used_space_units,
            free_archive_storage_used_space=free_archive_storage_used_space,
            free_archive_storage_used_space_units=free_archive_storage_used_space_units,
            repository_space_usage_algorithm=repository_space_usage_algorithm,
            repository_allocated_space_price=repository_allocated_space_price,
            repository_allocated_space_units=repository_allocated_space_units,
        )

        subscription_plan_vb_365.additional_properties = d
        return subscription_plan_vb_365

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
