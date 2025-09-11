from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.subscription_plan_public_cloud_hosted_archive_used_space_units import (
    SubscriptionPlanPublicCloudHostedArchiveUsedSpaceUnits,
)
from ..models.subscription_plan_public_cloud_hosted_backup_used_space_units import (
    SubscriptionPlanPublicCloudHostedBackupUsedSpaceUnits,
)
from ..models.subscription_plan_public_cloud_hosted_free_archive_used_space_units import (
    SubscriptionPlanPublicCloudHostedFreeArchiveUsedSpaceUnits,
)
from ..models.subscription_plan_public_cloud_hosted_free_backup_used_space_units import (
    SubscriptionPlanPublicCloudHostedFreeBackupUsedSpaceUnits,
)
from ..models.subscription_plan_public_cloud_remote_archive_used_space_units import (
    SubscriptionPlanPublicCloudRemoteArchiveUsedSpaceUnits,
)
from ..models.subscription_plan_public_cloud_remote_backup_used_space_units import (
    SubscriptionPlanPublicCloudRemoteBackupUsedSpaceUnits,
)
from ..models.subscription_plan_public_cloud_remote_free_archive_used_space_units import (
    SubscriptionPlanPublicCloudRemoteFreeArchiveUsedSpaceUnits,
)
from ..models.subscription_plan_public_cloud_remote_free_backup_used_space_units import (
    SubscriptionPlanPublicCloudRemoteFreeBackupUsedSpaceUnits,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="SubscriptionPlanPublicCloud")


@_attrs_define
class SubscriptionPlanPublicCloud:
    """
    Attributes:
        remote_cloud_vm_price (Union[Unset, float]): Charge rate for a managed remote public cloud VM. Default: 0.0.
        remote_free_cloud_vms (Union[Unset, int]): Number of remote public cloud VMs that are managed for free. Default:
            0.
        remote_cloud_file_share_price (Union[Unset, float]): Charge rate for a managed remote public cloud file share.
            Default: 0.0.
        remote_free_cloud_file_shares (Union[Unset, int]): Number of remote public cloud file shares that are managed
            for free. Default: 0.
        remote_cloud_database_price (Union[Unset, float]): Charge rate for a managed remote public cloud database.
            Default: 0.0.
        remote_free_cloud_databases (Union[Unset, int]): Number of remote public cloud databases that are managed for
            free. Default: 0.
        remote_cloud_network_price (Union[Unset, float]): Charge rate for a managed remote public cloud network.
            Default: 0.0.
        remote_backup_used_space_price (Union[Unset, float]): Charge rate for one GB or TB of consumed space on remote
            public cloud repository. Default: 0.0.
        remote_backup_used_space_units (Union[Unset, SubscriptionPlanPublicCloudRemoteBackupUsedSpaceUnits]):
            Measurement units of consumed space on remote public cloud repository. Default:
            SubscriptionPlanPublicCloudRemoteBackupUsedSpaceUnits.GB.
        remote_free_backup_used_space (Union[Unset, int]): Amount of consumed space on remote public cloud repository
            that is processed for free.
            > Maximum value is `1048576` for GB and `1024` for TB.
        remote_free_backup_used_space_units (Union[Unset, SubscriptionPlanPublicCloudRemoteFreeBackupUsedSpaceUnits]):
            Measurement units of consumed space on remote public cloud repository that is processed for free. Default:
            SubscriptionPlanPublicCloudRemoteFreeBackupUsedSpaceUnits.GB.
        remote_archive_used_space_price (Union[Unset, float]): Charge rate for one GB or TB of consumed space on remote
            archive public cloud repository. Default: 0.0.
        remote_archive_used_space_units (Union[Unset, SubscriptionPlanPublicCloudRemoteArchiveUsedSpaceUnits]):
            Measurement units of consumed space on remote archive public cloud repository. Default:
            SubscriptionPlanPublicCloudRemoteArchiveUsedSpaceUnits.GB.
        remote_free_archive_used_space (Union[Unset, int]): Amount of consumed space on remote archive public cloud
            repository that is processed for free.
            > Maximum value is `1048576` for GB and `1024` for TB.
        remote_free_archive_used_space_units (Union[Unset, SubscriptionPlanPublicCloudRemoteFreeArchiveUsedSpaceUnits]):
            Measurement units of consumed space on remote archive public cloud repository that is processed for free.
            Default: SubscriptionPlanPublicCloudRemoteFreeArchiveUsedSpaceUnits.GB.
        hosted_cloud_vm_price (Union[Unset, float]): Charge rate for a managed hosted public cloud VM. Default: 0.0.
        hosted_free_cloud_vms (Union[Unset, int]): Number of hosted public cloud VMs that are managed for free. Default:
            0.
        hosted_cloud_file_share_price (Union[Unset, float]): Charge rate for a managed hosted public cloud file share.
            Default: 0.0.
        hosted_free_cloud_file_shares (Union[Unset, int]): Number of hosted public cloud file shares that are managed
            for free. Default: 0.
        hosted_cloud_database_price (Union[Unset, float]): Charge rate for a managed hosted public cloud database.
            Default: 0.0.
        hosted_free_cloud_databases (Union[Unset, int]): Number of hosted public cloud databases that are managed for
            free. Default: 0.
        hosted_cloud_network_price (Union[Unset, float]): Charge rate for a managed hosted public cloud network.
            Default: 0.0.
        hosted_backup_used_space_price (Union[Unset, float]): Charge rate for one GB or TB of consumed space on a hosted
            public cloud repository. Default: 0.0.
        hosted_backup_used_space_units (Union[Unset, SubscriptionPlanPublicCloudHostedBackupUsedSpaceUnits]):
            Measurement units of consumed space on a hosted public cloud repository. Default:
            SubscriptionPlanPublicCloudHostedBackupUsedSpaceUnits.GB.
        hosted_free_backup_used_space (Union[Unset, int]): Amount of consumed space on a hosted public cloud repository
            that is processed for free.
            > Maximum value is `1048576` for GB and `1024` for TB.
        hosted_free_backup_used_space_units (Union[Unset, SubscriptionPlanPublicCloudHostedFreeBackupUsedSpaceUnits]):
            Measurement units of consumed space on hosted public cloud repository that is processed for free. Default:
            SubscriptionPlanPublicCloudHostedFreeBackupUsedSpaceUnits.GB.
        hosted_archive_used_space_price (Union[Unset, float]): Charge rate for one GB or TB of consumed space on a
            hosted public cloud archive repository. Default: 0.0.
        hosted_archive_used_space_units (Union[Unset, SubscriptionPlanPublicCloudHostedArchiveUsedSpaceUnits]):
            Measurement units of consumed space on a hosted public cloud archive repository. Default:
            SubscriptionPlanPublicCloudHostedArchiveUsedSpaceUnits.GB.
        hosted_free_archive_used_space (Union[Unset, int]): Amount of consumed space on a hosted public cloud archive
            repository that is processed for free.
            > Maximum value is `1048576` for GB and `1024` for TB.
        hosted_free_archive_used_space_units (Union[Unset, SubscriptionPlanPublicCloudHostedFreeArchiveUsedSpaceUnits]):
            Measurement units of consumed space on a hosted public cloud archive repository that is processed for free.
            Default: SubscriptionPlanPublicCloudHostedFreeArchiveUsedSpaceUnits.GB.
    """

    remote_cloud_vm_price: Union[Unset, float] = 0.0
    remote_free_cloud_vms: Union[Unset, int] = 0
    remote_cloud_file_share_price: Union[Unset, float] = 0.0
    remote_free_cloud_file_shares: Union[Unset, int] = 0
    remote_cloud_database_price: Union[Unset, float] = 0.0
    remote_free_cloud_databases: Union[Unset, int] = 0
    remote_cloud_network_price: Union[Unset, float] = 0.0
    remote_backup_used_space_price: Union[Unset, float] = 0.0
    remote_backup_used_space_units: Union[Unset, SubscriptionPlanPublicCloudRemoteBackupUsedSpaceUnits] = (
        SubscriptionPlanPublicCloudRemoteBackupUsedSpaceUnits.GB
    )
    remote_free_backup_used_space: Union[Unset, int] = UNSET
    remote_free_backup_used_space_units: Union[Unset, SubscriptionPlanPublicCloudRemoteFreeBackupUsedSpaceUnits] = (
        SubscriptionPlanPublicCloudRemoteFreeBackupUsedSpaceUnits.GB
    )
    remote_archive_used_space_price: Union[Unset, float] = 0.0
    remote_archive_used_space_units: Union[Unset, SubscriptionPlanPublicCloudRemoteArchiveUsedSpaceUnits] = (
        SubscriptionPlanPublicCloudRemoteArchiveUsedSpaceUnits.GB
    )
    remote_free_archive_used_space: Union[Unset, int] = UNSET
    remote_free_archive_used_space_units: Union[Unset, SubscriptionPlanPublicCloudRemoteFreeArchiveUsedSpaceUnits] = (
        SubscriptionPlanPublicCloudRemoteFreeArchiveUsedSpaceUnits.GB
    )
    hosted_cloud_vm_price: Union[Unset, float] = 0.0
    hosted_free_cloud_vms: Union[Unset, int] = 0
    hosted_cloud_file_share_price: Union[Unset, float] = 0.0
    hosted_free_cloud_file_shares: Union[Unset, int] = 0
    hosted_cloud_database_price: Union[Unset, float] = 0.0
    hosted_free_cloud_databases: Union[Unset, int] = 0
    hosted_cloud_network_price: Union[Unset, float] = 0.0
    hosted_backup_used_space_price: Union[Unset, float] = 0.0
    hosted_backup_used_space_units: Union[Unset, SubscriptionPlanPublicCloudHostedBackupUsedSpaceUnits] = (
        SubscriptionPlanPublicCloudHostedBackupUsedSpaceUnits.GB
    )
    hosted_free_backup_used_space: Union[Unset, int] = UNSET
    hosted_free_backup_used_space_units: Union[Unset, SubscriptionPlanPublicCloudHostedFreeBackupUsedSpaceUnits] = (
        SubscriptionPlanPublicCloudHostedFreeBackupUsedSpaceUnits.GB
    )
    hosted_archive_used_space_price: Union[Unset, float] = 0.0
    hosted_archive_used_space_units: Union[Unset, SubscriptionPlanPublicCloudHostedArchiveUsedSpaceUnits] = (
        SubscriptionPlanPublicCloudHostedArchiveUsedSpaceUnits.GB
    )
    hosted_free_archive_used_space: Union[Unset, int] = UNSET
    hosted_free_archive_used_space_units: Union[Unset, SubscriptionPlanPublicCloudHostedFreeArchiveUsedSpaceUnits] = (
        SubscriptionPlanPublicCloudHostedFreeArchiveUsedSpaceUnits.GB
    )
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        remote_cloud_vm_price = self.remote_cloud_vm_price

        remote_free_cloud_vms = self.remote_free_cloud_vms

        remote_cloud_file_share_price = self.remote_cloud_file_share_price

        remote_free_cloud_file_shares = self.remote_free_cloud_file_shares

        remote_cloud_database_price = self.remote_cloud_database_price

        remote_free_cloud_databases = self.remote_free_cloud_databases

        remote_cloud_network_price = self.remote_cloud_network_price

        remote_backup_used_space_price = self.remote_backup_used_space_price

        remote_backup_used_space_units: Union[Unset, str] = UNSET
        if not isinstance(self.remote_backup_used_space_units, Unset):
            remote_backup_used_space_units = self.remote_backup_used_space_units.value

        remote_free_backup_used_space = self.remote_free_backup_used_space

        remote_free_backup_used_space_units: Union[Unset, str] = UNSET
        if not isinstance(self.remote_free_backup_used_space_units, Unset):
            remote_free_backup_used_space_units = self.remote_free_backup_used_space_units.value

        remote_archive_used_space_price = self.remote_archive_used_space_price

        remote_archive_used_space_units: Union[Unset, str] = UNSET
        if not isinstance(self.remote_archive_used_space_units, Unset):
            remote_archive_used_space_units = self.remote_archive_used_space_units.value

        remote_free_archive_used_space = self.remote_free_archive_used_space

        remote_free_archive_used_space_units: Union[Unset, str] = UNSET
        if not isinstance(self.remote_free_archive_used_space_units, Unset):
            remote_free_archive_used_space_units = self.remote_free_archive_used_space_units.value

        hosted_cloud_vm_price = self.hosted_cloud_vm_price

        hosted_free_cloud_vms = self.hosted_free_cloud_vms

        hosted_cloud_file_share_price = self.hosted_cloud_file_share_price

        hosted_free_cloud_file_shares = self.hosted_free_cloud_file_shares

        hosted_cloud_database_price = self.hosted_cloud_database_price

        hosted_free_cloud_databases = self.hosted_free_cloud_databases

        hosted_cloud_network_price = self.hosted_cloud_network_price

        hosted_backup_used_space_price = self.hosted_backup_used_space_price

        hosted_backup_used_space_units: Union[Unset, str] = UNSET
        if not isinstance(self.hosted_backup_used_space_units, Unset):
            hosted_backup_used_space_units = self.hosted_backup_used_space_units.value

        hosted_free_backup_used_space = self.hosted_free_backup_used_space

        hosted_free_backup_used_space_units: Union[Unset, str] = UNSET
        if not isinstance(self.hosted_free_backup_used_space_units, Unset):
            hosted_free_backup_used_space_units = self.hosted_free_backup_used_space_units.value

        hosted_archive_used_space_price = self.hosted_archive_used_space_price

        hosted_archive_used_space_units: Union[Unset, str] = UNSET
        if not isinstance(self.hosted_archive_used_space_units, Unset):
            hosted_archive_used_space_units = self.hosted_archive_used_space_units.value

        hosted_free_archive_used_space = self.hosted_free_archive_used_space

        hosted_free_archive_used_space_units: Union[Unset, str] = UNSET
        if not isinstance(self.hosted_free_archive_used_space_units, Unset):
            hosted_free_archive_used_space_units = self.hosted_free_archive_used_space_units.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if remote_cloud_vm_price is not UNSET:
            field_dict["remoteCloudVmPrice"] = remote_cloud_vm_price
        if remote_free_cloud_vms is not UNSET:
            field_dict["remoteFreeCloudVms"] = remote_free_cloud_vms
        if remote_cloud_file_share_price is not UNSET:
            field_dict["remoteCloudFileSharePrice"] = remote_cloud_file_share_price
        if remote_free_cloud_file_shares is not UNSET:
            field_dict["remoteFreeCloudFileShares"] = remote_free_cloud_file_shares
        if remote_cloud_database_price is not UNSET:
            field_dict["remoteCloudDatabasePrice"] = remote_cloud_database_price
        if remote_free_cloud_databases is not UNSET:
            field_dict["remoteFreeCloudDatabases"] = remote_free_cloud_databases
        if remote_cloud_network_price is not UNSET:
            field_dict["remoteCloudNetworkPrice"] = remote_cloud_network_price
        if remote_backup_used_space_price is not UNSET:
            field_dict["remoteBackupUsedSpacePrice"] = remote_backup_used_space_price
        if remote_backup_used_space_units is not UNSET:
            field_dict["remoteBackupUsedSpaceUnits"] = remote_backup_used_space_units
        if remote_free_backup_used_space is not UNSET:
            field_dict["remoteFreeBackupUsedSpace"] = remote_free_backup_used_space
        if remote_free_backup_used_space_units is not UNSET:
            field_dict["remoteFreeBackupUsedSpaceUnits"] = remote_free_backup_used_space_units
        if remote_archive_used_space_price is not UNSET:
            field_dict["remoteArchiveUsedSpacePrice"] = remote_archive_used_space_price
        if remote_archive_used_space_units is not UNSET:
            field_dict["remoteArchiveUsedSpaceUnits"] = remote_archive_used_space_units
        if remote_free_archive_used_space is not UNSET:
            field_dict["remoteFreeArchiveUsedSpace"] = remote_free_archive_used_space
        if remote_free_archive_used_space_units is not UNSET:
            field_dict["remoteFreeArchiveUsedSpaceUnits"] = remote_free_archive_used_space_units
        if hosted_cloud_vm_price is not UNSET:
            field_dict["hostedCloudVmPrice"] = hosted_cloud_vm_price
        if hosted_free_cloud_vms is not UNSET:
            field_dict["hostedFreeCloudVms"] = hosted_free_cloud_vms
        if hosted_cloud_file_share_price is not UNSET:
            field_dict["hostedCloudFileSharePrice"] = hosted_cloud_file_share_price
        if hosted_free_cloud_file_shares is not UNSET:
            field_dict["hostedFreeCloudFileShares"] = hosted_free_cloud_file_shares
        if hosted_cloud_database_price is not UNSET:
            field_dict["hostedCloudDatabasePrice"] = hosted_cloud_database_price
        if hosted_free_cloud_databases is not UNSET:
            field_dict["hostedFreeCloudDatabases"] = hosted_free_cloud_databases
        if hosted_cloud_network_price is not UNSET:
            field_dict["hostedCloudNetworkPrice"] = hosted_cloud_network_price
        if hosted_backup_used_space_price is not UNSET:
            field_dict["hostedBackupUsedSpacePrice"] = hosted_backup_used_space_price
        if hosted_backup_used_space_units is not UNSET:
            field_dict["hostedBackupUsedSpaceUnits"] = hosted_backup_used_space_units
        if hosted_free_backup_used_space is not UNSET:
            field_dict["hostedFreeBackupUsedSpace"] = hosted_free_backup_used_space
        if hosted_free_backup_used_space_units is not UNSET:
            field_dict["hostedFreeBackupUsedSpaceUnits"] = hosted_free_backup_used_space_units
        if hosted_archive_used_space_price is not UNSET:
            field_dict["hostedArchiveUsedSpacePrice"] = hosted_archive_used_space_price
        if hosted_archive_used_space_units is not UNSET:
            field_dict["hostedArchiveUsedSpaceUnits"] = hosted_archive_used_space_units
        if hosted_free_archive_used_space is not UNSET:
            field_dict["hostedFreeArchiveUsedSpace"] = hosted_free_archive_used_space
        if hosted_free_archive_used_space_units is not UNSET:
            field_dict["hostedFreeArchiveUsedSpaceUnits"] = hosted_free_archive_used_space_units

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        remote_cloud_vm_price = d.pop("remoteCloudVmPrice", UNSET)

        remote_free_cloud_vms = d.pop("remoteFreeCloudVms", UNSET)

        remote_cloud_file_share_price = d.pop("remoteCloudFileSharePrice", UNSET)

        remote_free_cloud_file_shares = d.pop("remoteFreeCloudFileShares", UNSET)

        remote_cloud_database_price = d.pop("remoteCloudDatabasePrice", UNSET)

        remote_free_cloud_databases = d.pop("remoteFreeCloudDatabases", UNSET)

        remote_cloud_network_price = d.pop("remoteCloudNetworkPrice", UNSET)

        remote_backup_used_space_price = d.pop("remoteBackupUsedSpacePrice", UNSET)

        _remote_backup_used_space_units = d.pop("remoteBackupUsedSpaceUnits", UNSET)
        remote_backup_used_space_units: Union[Unset, SubscriptionPlanPublicCloudRemoteBackupUsedSpaceUnits]
        if isinstance(_remote_backup_used_space_units, Unset):
            remote_backup_used_space_units = UNSET
        else:
            remote_backup_used_space_units = SubscriptionPlanPublicCloudRemoteBackupUsedSpaceUnits(
                _remote_backup_used_space_units
            )

        remote_free_backup_used_space = d.pop("remoteFreeBackupUsedSpace", UNSET)

        _remote_free_backup_used_space_units = d.pop("remoteFreeBackupUsedSpaceUnits", UNSET)
        remote_free_backup_used_space_units: Union[Unset, SubscriptionPlanPublicCloudRemoteFreeBackupUsedSpaceUnits]
        if isinstance(_remote_free_backup_used_space_units, Unset):
            remote_free_backup_used_space_units = UNSET
        else:
            remote_free_backup_used_space_units = SubscriptionPlanPublicCloudRemoteFreeBackupUsedSpaceUnits(
                _remote_free_backup_used_space_units
            )

        remote_archive_used_space_price = d.pop("remoteArchiveUsedSpacePrice", UNSET)

        _remote_archive_used_space_units = d.pop("remoteArchiveUsedSpaceUnits", UNSET)
        remote_archive_used_space_units: Union[Unset, SubscriptionPlanPublicCloudRemoteArchiveUsedSpaceUnits]
        if isinstance(_remote_archive_used_space_units, Unset):
            remote_archive_used_space_units = UNSET
        else:
            remote_archive_used_space_units = SubscriptionPlanPublicCloudRemoteArchiveUsedSpaceUnits(
                _remote_archive_used_space_units
            )

        remote_free_archive_used_space = d.pop("remoteFreeArchiveUsedSpace", UNSET)

        _remote_free_archive_used_space_units = d.pop("remoteFreeArchiveUsedSpaceUnits", UNSET)
        remote_free_archive_used_space_units: Union[Unset, SubscriptionPlanPublicCloudRemoteFreeArchiveUsedSpaceUnits]
        if isinstance(_remote_free_archive_used_space_units, Unset):
            remote_free_archive_used_space_units = UNSET
        else:
            remote_free_archive_used_space_units = SubscriptionPlanPublicCloudRemoteFreeArchiveUsedSpaceUnits(
                _remote_free_archive_used_space_units
            )

        hosted_cloud_vm_price = d.pop("hostedCloudVmPrice", UNSET)

        hosted_free_cloud_vms = d.pop("hostedFreeCloudVms", UNSET)

        hosted_cloud_file_share_price = d.pop("hostedCloudFileSharePrice", UNSET)

        hosted_free_cloud_file_shares = d.pop("hostedFreeCloudFileShares", UNSET)

        hosted_cloud_database_price = d.pop("hostedCloudDatabasePrice", UNSET)

        hosted_free_cloud_databases = d.pop("hostedFreeCloudDatabases", UNSET)

        hosted_cloud_network_price = d.pop("hostedCloudNetworkPrice", UNSET)

        hosted_backup_used_space_price = d.pop("hostedBackupUsedSpacePrice", UNSET)

        _hosted_backup_used_space_units = d.pop("hostedBackupUsedSpaceUnits", UNSET)
        hosted_backup_used_space_units: Union[Unset, SubscriptionPlanPublicCloudHostedBackupUsedSpaceUnits]
        if isinstance(_hosted_backup_used_space_units, Unset):
            hosted_backup_used_space_units = UNSET
        else:
            hosted_backup_used_space_units = SubscriptionPlanPublicCloudHostedBackupUsedSpaceUnits(
                _hosted_backup_used_space_units
            )

        hosted_free_backup_used_space = d.pop("hostedFreeBackupUsedSpace", UNSET)

        _hosted_free_backup_used_space_units = d.pop("hostedFreeBackupUsedSpaceUnits", UNSET)
        hosted_free_backup_used_space_units: Union[Unset, SubscriptionPlanPublicCloudHostedFreeBackupUsedSpaceUnits]
        if isinstance(_hosted_free_backup_used_space_units, Unset):
            hosted_free_backup_used_space_units = UNSET
        else:
            hosted_free_backup_used_space_units = SubscriptionPlanPublicCloudHostedFreeBackupUsedSpaceUnits(
                _hosted_free_backup_used_space_units
            )

        hosted_archive_used_space_price = d.pop("hostedArchiveUsedSpacePrice", UNSET)

        _hosted_archive_used_space_units = d.pop("hostedArchiveUsedSpaceUnits", UNSET)
        hosted_archive_used_space_units: Union[Unset, SubscriptionPlanPublicCloudHostedArchiveUsedSpaceUnits]
        if isinstance(_hosted_archive_used_space_units, Unset):
            hosted_archive_used_space_units = UNSET
        else:
            hosted_archive_used_space_units = SubscriptionPlanPublicCloudHostedArchiveUsedSpaceUnits(
                _hosted_archive_used_space_units
            )

        hosted_free_archive_used_space = d.pop("hostedFreeArchiveUsedSpace", UNSET)

        _hosted_free_archive_used_space_units = d.pop("hostedFreeArchiveUsedSpaceUnits", UNSET)
        hosted_free_archive_used_space_units: Union[Unset, SubscriptionPlanPublicCloudHostedFreeArchiveUsedSpaceUnits]
        if isinstance(_hosted_free_archive_used_space_units, Unset):
            hosted_free_archive_used_space_units = UNSET
        else:
            hosted_free_archive_used_space_units = SubscriptionPlanPublicCloudHostedFreeArchiveUsedSpaceUnits(
                _hosted_free_archive_used_space_units
            )

        subscription_plan_public_cloud = cls(
            remote_cloud_vm_price=remote_cloud_vm_price,
            remote_free_cloud_vms=remote_free_cloud_vms,
            remote_cloud_file_share_price=remote_cloud_file_share_price,
            remote_free_cloud_file_shares=remote_free_cloud_file_shares,
            remote_cloud_database_price=remote_cloud_database_price,
            remote_free_cloud_databases=remote_free_cloud_databases,
            remote_cloud_network_price=remote_cloud_network_price,
            remote_backup_used_space_price=remote_backup_used_space_price,
            remote_backup_used_space_units=remote_backup_used_space_units,
            remote_free_backup_used_space=remote_free_backup_used_space,
            remote_free_backup_used_space_units=remote_free_backup_used_space_units,
            remote_archive_used_space_price=remote_archive_used_space_price,
            remote_archive_used_space_units=remote_archive_used_space_units,
            remote_free_archive_used_space=remote_free_archive_used_space,
            remote_free_archive_used_space_units=remote_free_archive_used_space_units,
            hosted_cloud_vm_price=hosted_cloud_vm_price,
            hosted_free_cloud_vms=hosted_free_cloud_vms,
            hosted_cloud_file_share_price=hosted_cloud_file_share_price,
            hosted_free_cloud_file_shares=hosted_free_cloud_file_shares,
            hosted_cloud_database_price=hosted_cloud_database_price,
            hosted_free_cloud_databases=hosted_free_cloud_databases,
            hosted_cloud_network_price=hosted_cloud_network_price,
            hosted_backup_used_space_price=hosted_backup_used_space_price,
            hosted_backup_used_space_units=hosted_backup_used_space_units,
            hosted_free_backup_used_space=hosted_free_backup_used_space,
            hosted_free_backup_used_space_units=hosted_free_backup_used_space_units,
            hosted_archive_used_space_price=hosted_archive_used_space_price,
            hosted_archive_used_space_units=hosted_archive_used_space_units,
            hosted_free_archive_used_space=hosted_free_archive_used_space,
            hosted_free_archive_used_space_units=hosted_free_archive_used_space_units,
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
