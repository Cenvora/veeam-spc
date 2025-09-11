from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.subscription_plan_vb_365_hosted_archive_storage_used_space_units import (
    SubscriptionPlanVb365HostedArchiveStorageUsedSpaceUnits,
)
from ..models.subscription_plan_vb_365_hosted_free_archive_storage_used_space_units import (
    SubscriptionPlanVb365HostedFreeArchiveStorageUsedSpaceUnits,
)
from ..models.subscription_plan_vb_365_hosted_free_standard_storage_used_space_units import (
    SubscriptionPlanVb365HostedFreeStandardStorageUsedSpaceUnits,
)
from ..models.subscription_plan_vb_365_hosted_repository_allocated_space_units import (
    SubscriptionPlanVb365HostedRepositoryAllocatedSpaceUnits,
)
from ..models.subscription_plan_vb_365_hosted_repository_space_usage_algorithm import (
    SubscriptionPlanVb365HostedRepositorySpaceUsageAlgorithm,
)
from ..models.subscription_plan_vb_365_hosted_standard_storage_used_space_units import (
    SubscriptionPlanVb365HostedStandardStorageUsedSpaceUnits,
)
from ..models.subscription_plan_vb_365_remote_archive_storage_used_space_units import (
    SubscriptionPlanVb365RemoteArchiveStorageUsedSpaceUnits,
)
from ..models.subscription_plan_vb_365_remote_free_archive_storage_used_space_units import (
    SubscriptionPlanVb365RemoteFreeArchiveStorageUsedSpaceUnits,
)
from ..models.subscription_plan_vb_365_remote_free_standard_storage_used_space_units import (
    SubscriptionPlanVb365RemoteFreeStandardStorageUsedSpaceUnits,
)
from ..models.subscription_plan_vb_365_remote_repository_allocated_space_units import (
    SubscriptionPlanVb365RemoteRepositoryAllocatedSpaceUnits,
)
from ..models.subscription_plan_vb_365_remote_repository_space_usage_algorithm import (
    SubscriptionPlanVb365RemoteRepositorySpaceUsageAlgorithm,
)
from ..models.subscription_plan_vb_365_remote_standard_storage_used_space_units import (
    SubscriptionPlanVb365RemoteStandardStorageUsedSpaceUnits,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="SubscriptionPlanVb365")


@_attrs_define
class SubscriptionPlanVb365:
    """
    Attributes:
        remote_subscription_user_price (Union[Unset, float]): Charge rate for a protected remote Microsoft 365
            subscription user. Default: 0.0.
        remote_free_subscription_users (Union[Unset, int]): Number of remote Microsoft 365 subscription users that are
            managed for free. Default: 0.
        remote_educational_user_price (Union[Unset, float]): Charge rate for a protected remote Microsoft 365
            educational subscription user. Default: 0.0.
        remote_free_educational_users (Union[Unset, int]): Number of remote Microsoft 365 educational subscription users
            that are managed for free. Default: 0.
        remote_round_up_used_space (Union[Unset, bool]): Indicates whether cost of storage used by remote services must
            be rounded up to a full data block cost when the consumed storage space does not match data block size. Default:
            False.
        remote_standard_storage_used_space_price (Union[Unset, float]): Charge rate for a block of stored Microsoft 365
            backup data. Default: 0.0.
        remote_standard_storage_used_space_chunk_size (Union[Unset, int]): Size of a stored Microsoft 365 backup data
            block. Default: 1.
        remote_standard_storage_used_space_units (Union[Unset,
            SubscriptionPlanVb365RemoteStandardStorageUsedSpaceUnits]): Measurement units of stored Microsoft 365 backup
            data block size. Default: SubscriptionPlanVb365RemoteStandardStorageUsedSpaceUnits.GB.
        remote_free_standard_storage_used_space (Union[Unset, int]): Amount of disk space consumed by remote Microsoft
            365 backups that is processed for free.
            > Maximum value is `1048576` for GB and `1024` for TB.
        remote_free_standard_storage_used_space_units (Union[Unset,
            SubscriptionPlanVb365RemoteFreeStandardStorageUsedSpaceUnits]): Measurement units of disk space consumed by
            remote Microsoft 365 backups that is processed for free. Default:
            SubscriptionPlanVb365RemoteFreeStandardStorageUsedSpaceUnits.GB.
        remote_archive_storage_used_space_price (Union[Unset, float]): Charge rate for a block of Microsoft 365 backup
            copy data stored in a remote archive repository. Default: 0.0.
        remote_archive_storage_used_space_chunk_size (Union[Unset, int]): Size of a data block of Microsoft 365 backup
            copies stored in a hosted archive repository. Default: 1.
        remote_archive_storage_used_space_units (Union[Unset, SubscriptionPlanVb365RemoteArchiveStorageUsedSpaceUnits]):
            Measurement units of Microsoft 365 backup copy data blocks. Default:
            SubscriptionPlanVb365RemoteArchiveStorageUsedSpaceUnits.GB.
        remote_free_archive_storage_used_space (Union[Unset, int]): Amount of remote archive repository disk space
            consumed by Microsoft 365 backup copies that is processed for free.
            > Maximum value is `1048576` for GB and `1024` for TB.
        remote_free_archive_storage_used_space_units (Union[Unset,
            SubscriptionPlanVb365RemoteFreeArchiveStorageUsedSpaceUnits]): Measurement units of remote archive repository
            disk space consumed by Microsoft 365 backup copies that is processed for free. Default:
            SubscriptionPlanVb365RemoteFreeArchiveStorageUsedSpaceUnits.GB.
        remote_repository_space_usage_algorithm (Union[Unset,
            SubscriptionPlanVb365RemoteRepositorySpaceUsageAlgorithm]): Type of remote repository storage space usage.
            Default: SubscriptionPlanVb365RemoteRepositorySpaceUsageAlgorithm.CONSUMED.
        remote_repository_allocated_space_price (Union[Unset, float]): Charge rate for one GB or TB of allocated storage
            space on a remote repository. Default: 0.0.
        remote_repository_allocated_space_units (Union[Unset,
            SubscriptionPlanVb365RemoteRepositoryAllocatedSpaceUnits]): Measurement units of allocated storage space on a
            remote repository. Default: SubscriptionPlanVb365RemoteRepositoryAllocatedSpaceUnits.GB.
        hosted_subscription_user_price (Union[Unset, float]):  Charge rate for a protected hosted Microsoft 365
            subscription user. Default: 0.0.
        hosted_free_subscription_users (Union[Unset, int]): Number of hosted Microsoft 365 subscription user that are
            managed for free. Default: 0.
        hosted_educational_user_price (Union[Unset, float]): Charge rate for a protected hosted Microsoft 365
            educational subscription user. Default: 0.0.
        hosted_free_educational_users (Union[Unset, int]): Number of hosted Microsoft 365 educational subscription users
            that are managed for free. Default: 0.
        hosted_round_up_used_space (Union[Unset, bool]): Indicates whether cost of storage used by hosted services must
            be rounded up to a full data block cost when the consumed storage space does not match data block size. Default:
            False.
        hosted_standard_storage_used_space_price (Union[Unset, float]): Charge rate for a block of stored hosted
            Microsoft 365 backup data. Default: 0.0.
        hosted_standard_storage_used_space_chunk_size (Union[Unset, int]): Size of a stored hosted Microsoft 365 backup
            data block. Default: 1.
        hosted_standard_storage_used_space_units (Union[Unset,
            SubscriptionPlanVb365HostedStandardStorageUsedSpaceUnits]): Measurement units of stored hosted Microsoft 365
            backup data block size. Default: SubscriptionPlanVb365HostedStandardStorageUsedSpaceUnits.GB.
        hosted_free_standard_storage_used_space (Union[Unset, int]): Amount of disk space consumed by hosted Microsoft
            365 backups that is processed for free.
            > Maximum value is `1048576` for GB and `1024` for TB.
        hosted_free_standard_storage_used_space_units (Union[Unset,
            SubscriptionPlanVb365HostedFreeStandardStorageUsedSpaceUnits]): Measurement units of disk space consumed by
            hosted Microsoft 365 backups that is processed for free. Default:
            SubscriptionPlanVb365HostedFreeStandardStorageUsedSpaceUnits.GB.
        hosted_archive_storage_used_space_price (Union[Unset, float]): Charge rate for a block of Microsoft 365 backup
            copy data stored in a hosted archive repository. Default: 0.0.
        hosted_archive_storage_used_space_chunk_size (Union[Unset, int]): Size of a data block of Microsoft 365 backup
            copies stored in a hosted archive repository. Default: 1.
        hosted_archive_storage_used_space_units (Union[Unset, SubscriptionPlanVb365HostedArchiveStorageUsedSpaceUnits]):
            Measurement units of Microsoft 365 backup copy data stored in a hosted archive repository. Default:
            SubscriptionPlanVb365HostedArchiveStorageUsedSpaceUnits.GB.
        hosted_free_archive_storage_used_space (Union[Unset, int]): Amount of hosted archive repository disk space
            consumed by Microsoft 365 backup copies that is processed for free.
            > Maximum value is `1048576` for GB and `1024` for TB.
        hosted_free_archive_storage_used_space_units (Union[Unset,
            SubscriptionPlanVb365HostedFreeArchiveStorageUsedSpaceUnits]): Measurement units of hosted archive repository
            disk space consumed by Microsoft 365 backup copies that is processed for free. Default:
            SubscriptionPlanVb365HostedFreeArchiveStorageUsedSpaceUnits.GB.
        hosted_repository_space_usage_algorithm (Union[Unset,
            SubscriptionPlanVb365HostedRepositorySpaceUsageAlgorithm]): Type of charge rate for storage space on a hosted
            repository. Default: SubscriptionPlanVb365HostedRepositorySpaceUsageAlgorithm.CONSUMED.
        hosted_repository_allocated_space_price (Union[Unset, float]): Charge rate for one GB or TB of allocated storage
            space on a hosted repository. Default: 0.0.
        hosted_repository_allocated_space_units (Union[Unset,
            SubscriptionPlanVb365HostedRepositoryAllocatedSpaceUnits]): Measurement units of allocated storage space on a
            hosted repository. Default: SubscriptionPlanVb365HostedRepositoryAllocatedSpaceUnits.GB.
    """

    remote_subscription_user_price: Union[Unset, float] = 0.0
    remote_free_subscription_users: Union[Unset, int] = 0
    remote_educational_user_price: Union[Unset, float] = 0.0
    remote_free_educational_users: Union[Unset, int] = 0
    remote_round_up_used_space: Union[Unset, bool] = False
    remote_standard_storage_used_space_price: Union[Unset, float] = 0.0
    remote_standard_storage_used_space_chunk_size: Union[Unset, int] = 1
    remote_standard_storage_used_space_units: Union[Unset, SubscriptionPlanVb365RemoteStandardStorageUsedSpaceUnits] = (
        SubscriptionPlanVb365RemoteStandardStorageUsedSpaceUnits.GB
    )
    remote_free_standard_storage_used_space: Union[Unset, int] = UNSET
    remote_free_standard_storage_used_space_units: Union[
        Unset, SubscriptionPlanVb365RemoteFreeStandardStorageUsedSpaceUnits
    ] = SubscriptionPlanVb365RemoteFreeStandardStorageUsedSpaceUnits.GB
    remote_archive_storage_used_space_price: Union[Unset, float] = 0.0
    remote_archive_storage_used_space_chunk_size: Union[Unset, int] = 1
    remote_archive_storage_used_space_units: Union[Unset, SubscriptionPlanVb365RemoteArchiveStorageUsedSpaceUnits] = (
        SubscriptionPlanVb365RemoteArchiveStorageUsedSpaceUnits.GB
    )
    remote_free_archive_storage_used_space: Union[Unset, int] = UNSET
    remote_free_archive_storage_used_space_units: Union[
        Unset, SubscriptionPlanVb365RemoteFreeArchiveStorageUsedSpaceUnits
    ] = SubscriptionPlanVb365RemoteFreeArchiveStorageUsedSpaceUnits.GB
    remote_repository_space_usage_algorithm: Union[Unset, SubscriptionPlanVb365RemoteRepositorySpaceUsageAlgorithm] = (
        SubscriptionPlanVb365RemoteRepositorySpaceUsageAlgorithm.CONSUMED
    )
    remote_repository_allocated_space_price: Union[Unset, float] = 0.0
    remote_repository_allocated_space_units: Union[Unset, SubscriptionPlanVb365RemoteRepositoryAllocatedSpaceUnits] = (
        SubscriptionPlanVb365RemoteRepositoryAllocatedSpaceUnits.GB
    )
    hosted_subscription_user_price: Union[Unset, float] = 0.0
    hosted_free_subscription_users: Union[Unset, int] = 0
    hosted_educational_user_price: Union[Unset, float] = 0.0
    hosted_free_educational_users: Union[Unset, int] = 0
    hosted_round_up_used_space: Union[Unset, bool] = False
    hosted_standard_storage_used_space_price: Union[Unset, float] = 0.0
    hosted_standard_storage_used_space_chunk_size: Union[Unset, int] = 1
    hosted_standard_storage_used_space_units: Union[Unset, SubscriptionPlanVb365HostedStandardStorageUsedSpaceUnits] = (
        SubscriptionPlanVb365HostedStandardStorageUsedSpaceUnits.GB
    )
    hosted_free_standard_storage_used_space: Union[Unset, int] = UNSET
    hosted_free_standard_storage_used_space_units: Union[
        Unset, SubscriptionPlanVb365HostedFreeStandardStorageUsedSpaceUnits
    ] = SubscriptionPlanVb365HostedFreeStandardStorageUsedSpaceUnits.GB
    hosted_archive_storage_used_space_price: Union[Unset, float] = 0.0
    hosted_archive_storage_used_space_chunk_size: Union[Unset, int] = 1
    hosted_archive_storage_used_space_units: Union[Unset, SubscriptionPlanVb365HostedArchiveStorageUsedSpaceUnits] = (
        SubscriptionPlanVb365HostedArchiveStorageUsedSpaceUnits.GB
    )
    hosted_free_archive_storage_used_space: Union[Unset, int] = UNSET
    hosted_free_archive_storage_used_space_units: Union[
        Unset, SubscriptionPlanVb365HostedFreeArchiveStorageUsedSpaceUnits
    ] = SubscriptionPlanVb365HostedFreeArchiveStorageUsedSpaceUnits.GB
    hosted_repository_space_usage_algorithm: Union[Unset, SubscriptionPlanVb365HostedRepositorySpaceUsageAlgorithm] = (
        SubscriptionPlanVb365HostedRepositorySpaceUsageAlgorithm.CONSUMED
    )
    hosted_repository_allocated_space_price: Union[Unset, float] = 0.0
    hosted_repository_allocated_space_units: Union[Unset, SubscriptionPlanVb365HostedRepositoryAllocatedSpaceUnits] = (
        SubscriptionPlanVb365HostedRepositoryAllocatedSpaceUnits.GB
    )
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        remote_subscription_user_price = self.remote_subscription_user_price

        remote_free_subscription_users = self.remote_free_subscription_users

        remote_educational_user_price = self.remote_educational_user_price

        remote_free_educational_users = self.remote_free_educational_users

        remote_round_up_used_space = self.remote_round_up_used_space

        remote_standard_storage_used_space_price = self.remote_standard_storage_used_space_price

        remote_standard_storage_used_space_chunk_size = self.remote_standard_storage_used_space_chunk_size

        remote_standard_storage_used_space_units: Union[Unset, str] = UNSET
        if not isinstance(self.remote_standard_storage_used_space_units, Unset):
            remote_standard_storage_used_space_units = self.remote_standard_storage_used_space_units.value

        remote_free_standard_storage_used_space = self.remote_free_standard_storage_used_space

        remote_free_standard_storage_used_space_units: Union[Unset, str] = UNSET
        if not isinstance(self.remote_free_standard_storage_used_space_units, Unset):
            remote_free_standard_storage_used_space_units = self.remote_free_standard_storage_used_space_units.value

        remote_archive_storage_used_space_price = self.remote_archive_storage_used_space_price

        remote_archive_storage_used_space_chunk_size = self.remote_archive_storage_used_space_chunk_size

        remote_archive_storage_used_space_units: Union[Unset, str] = UNSET
        if not isinstance(self.remote_archive_storage_used_space_units, Unset):
            remote_archive_storage_used_space_units = self.remote_archive_storage_used_space_units.value

        remote_free_archive_storage_used_space = self.remote_free_archive_storage_used_space

        remote_free_archive_storage_used_space_units: Union[Unset, str] = UNSET
        if not isinstance(self.remote_free_archive_storage_used_space_units, Unset):
            remote_free_archive_storage_used_space_units = self.remote_free_archive_storage_used_space_units.value

        remote_repository_space_usage_algorithm: Union[Unset, str] = UNSET
        if not isinstance(self.remote_repository_space_usage_algorithm, Unset):
            remote_repository_space_usage_algorithm = self.remote_repository_space_usage_algorithm.value

        remote_repository_allocated_space_price = self.remote_repository_allocated_space_price

        remote_repository_allocated_space_units: Union[Unset, str] = UNSET
        if not isinstance(self.remote_repository_allocated_space_units, Unset):
            remote_repository_allocated_space_units = self.remote_repository_allocated_space_units.value

        hosted_subscription_user_price = self.hosted_subscription_user_price

        hosted_free_subscription_users = self.hosted_free_subscription_users

        hosted_educational_user_price = self.hosted_educational_user_price

        hosted_free_educational_users = self.hosted_free_educational_users

        hosted_round_up_used_space = self.hosted_round_up_used_space

        hosted_standard_storage_used_space_price = self.hosted_standard_storage_used_space_price

        hosted_standard_storage_used_space_chunk_size = self.hosted_standard_storage_used_space_chunk_size

        hosted_standard_storage_used_space_units: Union[Unset, str] = UNSET
        if not isinstance(self.hosted_standard_storage_used_space_units, Unset):
            hosted_standard_storage_used_space_units = self.hosted_standard_storage_used_space_units.value

        hosted_free_standard_storage_used_space = self.hosted_free_standard_storage_used_space

        hosted_free_standard_storage_used_space_units: Union[Unset, str] = UNSET
        if not isinstance(self.hosted_free_standard_storage_used_space_units, Unset):
            hosted_free_standard_storage_used_space_units = self.hosted_free_standard_storage_used_space_units.value

        hosted_archive_storage_used_space_price = self.hosted_archive_storage_used_space_price

        hosted_archive_storage_used_space_chunk_size = self.hosted_archive_storage_used_space_chunk_size

        hosted_archive_storage_used_space_units: Union[Unset, str] = UNSET
        if not isinstance(self.hosted_archive_storage_used_space_units, Unset):
            hosted_archive_storage_used_space_units = self.hosted_archive_storage_used_space_units.value

        hosted_free_archive_storage_used_space = self.hosted_free_archive_storage_used_space

        hosted_free_archive_storage_used_space_units: Union[Unset, str] = UNSET
        if not isinstance(self.hosted_free_archive_storage_used_space_units, Unset):
            hosted_free_archive_storage_used_space_units = self.hosted_free_archive_storage_used_space_units.value

        hosted_repository_space_usage_algorithm: Union[Unset, str] = UNSET
        if not isinstance(self.hosted_repository_space_usage_algorithm, Unset):
            hosted_repository_space_usage_algorithm = self.hosted_repository_space_usage_algorithm.value

        hosted_repository_allocated_space_price = self.hosted_repository_allocated_space_price

        hosted_repository_allocated_space_units: Union[Unset, str] = UNSET
        if not isinstance(self.hosted_repository_allocated_space_units, Unset):
            hosted_repository_allocated_space_units = self.hosted_repository_allocated_space_units.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if remote_subscription_user_price is not UNSET:
            field_dict["remoteSubscriptionUserPrice"] = remote_subscription_user_price
        if remote_free_subscription_users is not UNSET:
            field_dict["remoteFreeSubscriptionUsers"] = remote_free_subscription_users
        if remote_educational_user_price is not UNSET:
            field_dict["remoteEducationalUserPrice"] = remote_educational_user_price
        if remote_free_educational_users is not UNSET:
            field_dict["remoteFreeEducationalUsers"] = remote_free_educational_users
        if remote_round_up_used_space is not UNSET:
            field_dict["remoteRoundUpUsedSpace"] = remote_round_up_used_space
        if remote_standard_storage_used_space_price is not UNSET:
            field_dict["remoteStandardStorageUsedSpacePrice"] = remote_standard_storage_used_space_price
        if remote_standard_storage_used_space_chunk_size is not UNSET:
            field_dict["remoteStandardStorageUsedSpaceChunkSize"] = remote_standard_storage_used_space_chunk_size
        if remote_standard_storage_used_space_units is not UNSET:
            field_dict["remoteStandardStorageUsedSpaceUnits"] = remote_standard_storage_used_space_units
        if remote_free_standard_storage_used_space is not UNSET:
            field_dict["remoteFreeStandardStorageUsedSpace"] = remote_free_standard_storage_used_space
        if remote_free_standard_storage_used_space_units is not UNSET:
            field_dict["remoteFreeStandardStorageUsedSpaceUnits"] = remote_free_standard_storage_used_space_units
        if remote_archive_storage_used_space_price is not UNSET:
            field_dict["remoteArchiveStorageUsedSpacePrice"] = remote_archive_storage_used_space_price
        if remote_archive_storage_used_space_chunk_size is not UNSET:
            field_dict["remoteArchiveStorageUsedSpaceChunkSize"] = remote_archive_storage_used_space_chunk_size
        if remote_archive_storage_used_space_units is not UNSET:
            field_dict["remoteArchiveStorageUsedSpaceUnits"] = remote_archive_storage_used_space_units
        if remote_free_archive_storage_used_space is not UNSET:
            field_dict["remoteFreeArchiveStorageUsedSpace"] = remote_free_archive_storage_used_space
        if remote_free_archive_storage_used_space_units is not UNSET:
            field_dict["remoteFreeArchiveStorageUsedSpaceUnits"] = remote_free_archive_storage_used_space_units
        if remote_repository_space_usage_algorithm is not UNSET:
            field_dict["remoteRepositorySpaceUsageAlgorithm"] = remote_repository_space_usage_algorithm
        if remote_repository_allocated_space_price is not UNSET:
            field_dict["remoteRepositoryAllocatedSpacePrice"] = remote_repository_allocated_space_price
        if remote_repository_allocated_space_units is not UNSET:
            field_dict["remoteRepositoryAllocatedSpaceUnits"] = remote_repository_allocated_space_units
        if hosted_subscription_user_price is not UNSET:
            field_dict["hostedSubscriptionUserPrice"] = hosted_subscription_user_price
        if hosted_free_subscription_users is not UNSET:
            field_dict["hostedFreeSubscriptionUsers"] = hosted_free_subscription_users
        if hosted_educational_user_price is not UNSET:
            field_dict["hostedEducationalUserPrice"] = hosted_educational_user_price
        if hosted_free_educational_users is not UNSET:
            field_dict["hostedFreeEducationalUsers"] = hosted_free_educational_users
        if hosted_round_up_used_space is not UNSET:
            field_dict["hostedRoundUpUsedSpace"] = hosted_round_up_used_space
        if hosted_standard_storage_used_space_price is not UNSET:
            field_dict["hostedStandardStorageUsedSpacePrice"] = hosted_standard_storage_used_space_price
        if hosted_standard_storage_used_space_chunk_size is not UNSET:
            field_dict["hostedStandardStorageUsedSpaceChunkSize"] = hosted_standard_storage_used_space_chunk_size
        if hosted_standard_storage_used_space_units is not UNSET:
            field_dict["hostedStandardStorageUsedSpaceUnits"] = hosted_standard_storage_used_space_units
        if hosted_free_standard_storage_used_space is not UNSET:
            field_dict["hostedFreeStandardStorageUsedSpace"] = hosted_free_standard_storage_used_space
        if hosted_free_standard_storage_used_space_units is not UNSET:
            field_dict["hostedFreeStandardStorageUsedSpaceUnits"] = hosted_free_standard_storage_used_space_units
        if hosted_archive_storage_used_space_price is not UNSET:
            field_dict["hostedArchiveStorageUsedSpacePrice"] = hosted_archive_storage_used_space_price
        if hosted_archive_storage_used_space_chunk_size is not UNSET:
            field_dict["hostedArchiveStorageUsedSpaceChunkSize"] = hosted_archive_storage_used_space_chunk_size
        if hosted_archive_storage_used_space_units is not UNSET:
            field_dict["hostedArchiveStorageUsedSpaceUnits"] = hosted_archive_storage_used_space_units
        if hosted_free_archive_storage_used_space is not UNSET:
            field_dict["hostedFreeArchiveStorageUsedSpace"] = hosted_free_archive_storage_used_space
        if hosted_free_archive_storage_used_space_units is not UNSET:
            field_dict["hostedFreeArchiveStorageUsedSpaceUnits"] = hosted_free_archive_storage_used_space_units
        if hosted_repository_space_usage_algorithm is not UNSET:
            field_dict["hostedRepositorySpaceUsageAlgorithm"] = hosted_repository_space_usage_algorithm
        if hosted_repository_allocated_space_price is not UNSET:
            field_dict["hostedRepositoryAllocatedSpacePrice"] = hosted_repository_allocated_space_price
        if hosted_repository_allocated_space_units is not UNSET:
            field_dict["hostedRepositoryAllocatedSpaceUnits"] = hosted_repository_allocated_space_units

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        remote_subscription_user_price = d.pop("remoteSubscriptionUserPrice", UNSET)

        remote_free_subscription_users = d.pop("remoteFreeSubscriptionUsers", UNSET)

        remote_educational_user_price = d.pop("remoteEducationalUserPrice", UNSET)

        remote_free_educational_users = d.pop("remoteFreeEducationalUsers", UNSET)

        remote_round_up_used_space = d.pop("remoteRoundUpUsedSpace", UNSET)

        remote_standard_storage_used_space_price = d.pop("remoteStandardStorageUsedSpacePrice", UNSET)

        remote_standard_storage_used_space_chunk_size = d.pop("remoteStandardStorageUsedSpaceChunkSize", UNSET)

        _remote_standard_storage_used_space_units = d.pop("remoteStandardStorageUsedSpaceUnits", UNSET)
        remote_standard_storage_used_space_units: Union[Unset, SubscriptionPlanVb365RemoteStandardStorageUsedSpaceUnits]
        if isinstance(_remote_standard_storage_used_space_units, Unset):
            remote_standard_storage_used_space_units = UNSET
        else:
            remote_standard_storage_used_space_units = SubscriptionPlanVb365RemoteStandardStorageUsedSpaceUnits(
                _remote_standard_storage_used_space_units
            )

        remote_free_standard_storage_used_space = d.pop("remoteFreeStandardStorageUsedSpace", UNSET)

        _remote_free_standard_storage_used_space_units = d.pop("remoteFreeStandardStorageUsedSpaceUnits", UNSET)
        remote_free_standard_storage_used_space_units: Union[
            Unset, SubscriptionPlanVb365RemoteFreeStandardStorageUsedSpaceUnits
        ]
        if isinstance(_remote_free_standard_storage_used_space_units, Unset):
            remote_free_standard_storage_used_space_units = UNSET
        else:
            remote_free_standard_storage_used_space_units = (
                SubscriptionPlanVb365RemoteFreeStandardStorageUsedSpaceUnits(
                    _remote_free_standard_storage_used_space_units
                )
            )

        remote_archive_storage_used_space_price = d.pop("remoteArchiveStorageUsedSpacePrice", UNSET)

        remote_archive_storage_used_space_chunk_size = d.pop("remoteArchiveStorageUsedSpaceChunkSize", UNSET)

        _remote_archive_storage_used_space_units = d.pop("remoteArchiveStorageUsedSpaceUnits", UNSET)
        remote_archive_storage_used_space_units: Union[Unset, SubscriptionPlanVb365RemoteArchiveStorageUsedSpaceUnits]
        if isinstance(_remote_archive_storage_used_space_units, Unset):
            remote_archive_storage_used_space_units = UNSET
        else:
            remote_archive_storage_used_space_units = SubscriptionPlanVb365RemoteArchiveStorageUsedSpaceUnits(
                _remote_archive_storage_used_space_units
            )

        remote_free_archive_storage_used_space = d.pop("remoteFreeArchiveStorageUsedSpace", UNSET)

        _remote_free_archive_storage_used_space_units = d.pop("remoteFreeArchiveStorageUsedSpaceUnits", UNSET)
        remote_free_archive_storage_used_space_units: Union[
            Unset, SubscriptionPlanVb365RemoteFreeArchiveStorageUsedSpaceUnits
        ]
        if isinstance(_remote_free_archive_storage_used_space_units, Unset):
            remote_free_archive_storage_used_space_units = UNSET
        else:
            remote_free_archive_storage_used_space_units = SubscriptionPlanVb365RemoteFreeArchiveStorageUsedSpaceUnits(
                _remote_free_archive_storage_used_space_units
            )

        _remote_repository_space_usage_algorithm = d.pop("remoteRepositorySpaceUsageAlgorithm", UNSET)
        remote_repository_space_usage_algorithm: Union[Unset, SubscriptionPlanVb365RemoteRepositorySpaceUsageAlgorithm]
        if isinstance(_remote_repository_space_usage_algorithm, Unset):
            remote_repository_space_usage_algorithm = UNSET
        else:
            remote_repository_space_usage_algorithm = SubscriptionPlanVb365RemoteRepositorySpaceUsageAlgorithm(
                _remote_repository_space_usage_algorithm
            )

        remote_repository_allocated_space_price = d.pop("remoteRepositoryAllocatedSpacePrice", UNSET)

        _remote_repository_allocated_space_units = d.pop("remoteRepositoryAllocatedSpaceUnits", UNSET)
        remote_repository_allocated_space_units: Union[Unset, SubscriptionPlanVb365RemoteRepositoryAllocatedSpaceUnits]
        if isinstance(_remote_repository_allocated_space_units, Unset):
            remote_repository_allocated_space_units = UNSET
        else:
            remote_repository_allocated_space_units = SubscriptionPlanVb365RemoteRepositoryAllocatedSpaceUnits(
                _remote_repository_allocated_space_units
            )

        hosted_subscription_user_price = d.pop("hostedSubscriptionUserPrice", UNSET)

        hosted_free_subscription_users = d.pop("hostedFreeSubscriptionUsers", UNSET)

        hosted_educational_user_price = d.pop("hostedEducationalUserPrice", UNSET)

        hosted_free_educational_users = d.pop("hostedFreeEducationalUsers", UNSET)

        hosted_round_up_used_space = d.pop("hostedRoundUpUsedSpace", UNSET)

        hosted_standard_storage_used_space_price = d.pop("hostedStandardStorageUsedSpacePrice", UNSET)

        hosted_standard_storage_used_space_chunk_size = d.pop("hostedStandardStorageUsedSpaceChunkSize", UNSET)

        _hosted_standard_storage_used_space_units = d.pop("hostedStandardStorageUsedSpaceUnits", UNSET)
        hosted_standard_storage_used_space_units: Union[Unset, SubscriptionPlanVb365HostedStandardStorageUsedSpaceUnits]
        if isinstance(_hosted_standard_storage_used_space_units, Unset):
            hosted_standard_storage_used_space_units = UNSET
        else:
            hosted_standard_storage_used_space_units = SubscriptionPlanVb365HostedStandardStorageUsedSpaceUnits(
                _hosted_standard_storage_used_space_units
            )

        hosted_free_standard_storage_used_space = d.pop("hostedFreeStandardStorageUsedSpace", UNSET)

        _hosted_free_standard_storage_used_space_units = d.pop("hostedFreeStandardStorageUsedSpaceUnits", UNSET)
        hosted_free_standard_storage_used_space_units: Union[
            Unset, SubscriptionPlanVb365HostedFreeStandardStorageUsedSpaceUnits
        ]
        if isinstance(_hosted_free_standard_storage_used_space_units, Unset):
            hosted_free_standard_storage_used_space_units = UNSET
        else:
            hosted_free_standard_storage_used_space_units = (
                SubscriptionPlanVb365HostedFreeStandardStorageUsedSpaceUnits(
                    _hosted_free_standard_storage_used_space_units
                )
            )

        hosted_archive_storage_used_space_price = d.pop("hostedArchiveStorageUsedSpacePrice", UNSET)

        hosted_archive_storage_used_space_chunk_size = d.pop("hostedArchiveStorageUsedSpaceChunkSize", UNSET)

        _hosted_archive_storage_used_space_units = d.pop("hostedArchiveStorageUsedSpaceUnits", UNSET)
        hosted_archive_storage_used_space_units: Union[Unset, SubscriptionPlanVb365HostedArchiveStorageUsedSpaceUnits]
        if isinstance(_hosted_archive_storage_used_space_units, Unset):
            hosted_archive_storage_used_space_units = UNSET
        else:
            hosted_archive_storage_used_space_units = SubscriptionPlanVb365HostedArchiveStorageUsedSpaceUnits(
                _hosted_archive_storage_used_space_units
            )

        hosted_free_archive_storage_used_space = d.pop("hostedFreeArchiveStorageUsedSpace", UNSET)

        _hosted_free_archive_storage_used_space_units = d.pop("hostedFreeArchiveStorageUsedSpaceUnits", UNSET)
        hosted_free_archive_storage_used_space_units: Union[
            Unset, SubscriptionPlanVb365HostedFreeArchiveStorageUsedSpaceUnits
        ]
        if isinstance(_hosted_free_archive_storage_used_space_units, Unset):
            hosted_free_archive_storage_used_space_units = UNSET
        else:
            hosted_free_archive_storage_used_space_units = SubscriptionPlanVb365HostedFreeArchiveStorageUsedSpaceUnits(
                _hosted_free_archive_storage_used_space_units
            )

        _hosted_repository_space_usage_algorithm = d.pop("hostedRepositorySpaceUsageAlgorithm", UNSET)
        hosted_repository_space_usage_algorithm: Union[Unset, SubscriptionPlanVb365HostedRepositorySpaceUsageAlgorithm]
        if isinstance(_hosted_repository_space_usage_algorithm, Unset):
            hosted_repository_space_usage_algorithm = UNSET
        else:
            hosted_repository_space_usage_algorithm = SubscriptionPlanVb365HostedRepositorySpaceUsageAlgorithm(
                _hosted_repository_space_usage_algorithm
            )

        hosted_repository_allocated_space_price = d.pop("hostedRepositoryAllocatedSpacePrice", UNSET)

        _hosted_repository_allocated_space_units = d.pop("hostedRepositoryAllocatedSpaceUnits", UNSET)
        hosted_repository_allocated_space_units: Union[Unset, SubscriptionPlanVb365HostedRepositoryAllocatedSpaceUnits]
        if isinstance(_hosted_repository_allocated_space_units, Unset):
            hosted_repository_allocated_space_units = UNSET
        else:
            hosted_repository_allocated_space_units = SubscriptionPlanVb365HostedRepositoryAllocatedSpaceUnits(
                _hosted_repository_allocated_space_units
            )

        subscription_plan_vb_365 = cls(
            remote_subscription_user_price=remote_subscription_user_price,
            remote_free_subscription_users=remote_free_subscription_users,
            remote_educational_user_price=remote_educational_user_price,
            remote_free_educational_users=remote_free_educational_users,
            remote_round_up_used_space=remote_round_up_used_space,
            remote_standard_storage_used_space_price=remote_standard_storage_used_space_price,
            remote_standard_storage_used_space_chunk_size=remote_standard_storage_used_space_chunk_size,
            remote_standard_storage_used_space_units=remote_standard_storage_used_space_units,
            remote_free_standard_storage_used_space=remote_free_standard_storage_used_space,
            remote_free_standard_storage_used_space_units=remote_free_standard_storage_used_space_units,
            remote_archive_storage_used_space_price=remote_archive_storage_used_space_price,
            remote_archive_storage_used_space_chunk_size=remote_archive_storage_used_space_chunk_size,
            remote_archive_storage_used_space_units=remote_archive_storage_used_space_units,
            remote_free_archive_storage_used_space=remote_free_archive_storage_used_space,
            remote_free_archive_storage_used_space_units=remote_free_archive_storage_used_space_units,
            remote_repository_space_usage_algorithm=remote_repository_space_usage_algorithm,
            remote_repository_allocated_space_price=remote_repository_allocated_space_price,
            remote_repository_allocated_space_units=remote_repository_allocated_space_units,
            hosted_subscription_user_price=hosted_subscription_user_price,
            hosted_free_subscription_users=hosted_free_subscription_users,
            hosted_educational_user_price=hosted_educational_user_price,
            hosted_free_educational_users=hosted_free_educational_users,
            hosted_round_up_used_space=hosted_round_up_used_space,
            hosted_standard_storage_used_space_price=hosted_standard_storage_used_space_price,
            hosted_standard_storage_used_space_chunk_size=hosted_standard_storage_used_space_chunk_size,
            hosted_standard_storage_used_space_units=hosted_standard_storage_used_space_units,
            hosted_free_standard_storage_used_space=hosted_free_standard_storage_used_space,
            hosted_free_standard_storage_used_space_units=hosted_free_standard_storage_used_space_units,
            hosted_archive_storage_used_space_price=hosted_archive_storage_used_space_price,
            hosted_archive_storage_used_space_chunk_size=hosted_archive_storage_used_space_chunk_size,
            hosted_archive_storage_used_space_units=hosted_archive_storage_used_space_units,
            hosted_free_archive_storage_used_space=hosted_free_archive_storage_used_space,
            hosted_free_archive_storage_used_space_units=hosted_free_archive_storage_used_space_units,
            hosted_repository_space_usage_algorithm=hosted_repository_space_usage_algorithm,
            hosted_repository_allocated_space_price=hosted_repository_allocated_space_price,
            hosted_repository_allocated_space_units=hosted_repository_allocated_space_units,
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
