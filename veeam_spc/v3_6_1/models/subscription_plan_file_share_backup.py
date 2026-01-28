from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.subscription_plan_file_share_backup_file_share_hosted_archive_used_space_units import (
    SubscriptionPlanFileShareBackupFileShareHostedArchiveUsedSpaceUnits,
)
from ..models.subscription_plan_file_share_backup_file_share_hosted_backup_used_space_units import (
    SubscriptionPlanFileShareBackupFileShareHostedBackupUsedSpaceUnits,
)
from ..models.subscription_plan_file_share_backup_file_share_remote_archive_used_space_units import (
    SubscriptionPlanFileShareBackupFileShareRemoteArchiveUsedSpaceUnits,
)
from ..models.subscription_plan_file_share_backup_file_share_remote_backup_used_space_units import (
    SubscriptionPlanFileShareBackupFileShareRemoteBackupUsedSpaceUnits,
)
from ..models.subscription_plan_file_share_backup_free_file_share_hosted_archive_used_space_units import (
    SubscriptionPlanFileShareBackupFreeFileShareHostedArchiveUsedSpaceUnits,
)
from ..models.subscription_plan_file_share_backup_free_file_share_hosted_backup_used_space_units import (
    SubscriptionPlanFileShareBackupFreeFileShareHostedBackupUsedSpaceUnits,
)
from ..models.subscription_plan_file_share_backup_free_file_share_remote_archive_used_space_units import (
    SubscriptionPlanFileShareBackupFreeFileShareRemoteArchiveUsedSpaceUnits,
)
from ..models.subscription_plan_file_share_backup_free_file_share_remote_backup_used_space_units import (
    SubscriptionPlanFileShareBackupFreeFileShareRemoteBackupUsedSpaceUnits,
)
from ..models.subscription_plan_file_share_backup_free_source_hosted_amount_of_data_units import (
    SubscriptionPlanFileShareBackupFreeSourceHostedAmountOfDataUnits,
)
from ..models.subscription_plan_file_share_backup_free_source_remote_amount_of_data_units import (
    SubscriptionPlanFileShareBackupFreeSourceRemoteAmountOfDataUnits,
)
from ..models.subscription_plan_file_share_backup_source_hosted_amount_of_data_units import (
    SubscriptionPlanFileShareBackupSourceHostedAmountOfDataUnits,
)
from ..models.subscription_plan_file_share_backup_source_remote_amount_of_data_units import (
    SubscriptionPlanFileShareBackupSourceRemoteAmountOfDataUnits,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="SubscriptionPlanFileShareBackup")


@_attrs_define
class SubscriptionPlanFileShareBackup:
    """
    Attributes:
        file_share_remote_backup_used_space_price (Union[Unset, float]): Charge rate for one GB or TB of backup
            repository space consumed by file share backups. Default: 0.0.
        file_share_remote_backup_used_space_units (Union[Unset,
            SubscriptionPlanFileShareBackupFileShareRemoteBackupUsedSpaceUnits]): Measurement units of backup repository
            space consumed by file share backups. Default:
            SubscriptionPlanFileShareBackupFileShareRemoteBackupUsedSpaceUnits.GB.
        free_file_share_remote_backup_used_space (Union[None, Unset, int]): Amount of backup repository space that can
            be consumed by file share backups for free.
            > Maximum value is `1048576` for GB and `1024` for TB.
        free_file_share_remote_backup_used_space_units (Union[Unset,
            SubscriptionPlanFileShareBackupFreeFileShareRemoteBackupUsedSpaceUnits]): Measurement units of backup repository
            space that can be consumed by file share backups for free. Default:
            SubscriptionPlanFileShareBackupFreeFileShareRemoteBackupUsedSpaceUnits.GB.
        file_share_remote_archive_used_space_price (Union[Unset, float]): Charge rate for one GB or TB of archive
            repository space consumed by file share backups. Default: 0.0.
        file_share_remote_archive_used_space_units (Union[Unset,
            SubscriptionPlanFileShareBackupFileShareRemoteArchiveUsedSpaceUnits]): Measurement units of archive repository
            space consumed by file share backups. Default:
            SubscriptionPlanFileShareBackupFileShareRemoteArchiveUsedSpaceUnits.GB.
        free_file_share_remote_archive_used_space (Union[None, Unset, int]): Amount of archive repository space that can
            be consumed by file share backups for free.
            > Maximum value is `1048576` for GB and `1024` for TB.
        free_file_share_remote_archive_used_space_units (Union[Unset,
            SubscriptionPlanFileShareBackupFreeFileShareRemoteArchiveUsedSpaceUnits]): Measurement units of archive
            repository space that can be consumed by file share backups for free. Default:
            SubscriptionPlanFileShareBackupFreeFileShareRemoteArchiveUsedSpaceUnits.GB.
        source_remote_amount_of_data_price (Union[Unset, float]): Charge rate for one GB or TB of source data. Default:
            0.0.
        source_remote_amount_of_data_units (Union[Unset, SubscriptionPlanFileShareBackupSourceRemoteAmountOfDataUnits]):
            Measurement units of source data. Default: SubscriptionPlanFileShareBackupSourceRemoteAmountOfDataUnits.GB.
        free_source_remote_amount_of_data (Union[None, Unset, int]): Amount of source data that is processed for free.
            > Maximum value is `1048576` for GB and `1024` for TB.
        free_source_remote_amount_of_data_units (Union[Unset,
            SubscriptionPlanFileShareBackupFreeSourceRemoteAmountOfDataUnits]): Measurement units of source data that is
            processed for free. Default: SubscriptionPlanFileShareBackupFreeSourceRemoteAmountOfDataUnits.GB.
        file_share_hosted_backup_used_space_price (Union[Unset, float]): Charge rate for one GB or TB of backup
            repository space consumed by file share backups. Default: 0.0.
        file_share_hosted_backup_used_space_units (Union[Unset,
            SubscriptionPlanFileShareBackupFileShareHostedBackupUsedSpaceUnits]): Measurement units of backup repository
            space consumed by file share backups. Default:
            SubscriptionPlanFileShareBackupFileShareHostedBackupUsedSpaceUnits.GB.
        free_file_share_hosted_backup_used_space (Union[None, Unset, int]): Amount of backup repository space that can
            be consumed by file share backups for free.
            > Maximum value is `1048576` for GB and `1024` for TB.
        free_file_share_hosted_backup_used_space_units (Union[Unset,
            SubscriptionPlanFileShareBackupFreeFileShareHostedBackupUsedSpaceUnits]): Measurement units of backup repository
            space that can be consumed by file share backups for free. Default:
            SubscriptionPlanFileShareBackupFreeFileShareHostedBackupUsedSpaceUnits.GB.
        file_share_hosted_archive_used_space_price (Union[Unset, float]): Charge rate for one GB or TB of archive
            repository space consumed by file share backups. Default: 0.0.
        file_share_hosted_archive_used_space_units (Union[Unset,
            SubscriptionPlanFileShareBackupFileShareHostedArchiveUsedSpaceUnits]): Measurement units of archive repository
            space consumed by file share backups. Default:
            SubscriptionPlanFileShareBackupFileShareHostedArchiveUsedSpaceUnits.GB.
        free_file_share_hosted_archive_used_space (Union[None, Unset, int]): Amount of archive repository space that can
            be consumed by file share backups for free.
            > Maximum value is `1048576` for GB and `1024` for TB.
        free_file_share_hosted_archive_used_space_units (Union[Unset,
            SubscriptionPlanFileShareBackupFreeFileShareHostedArchiveUsedSpaceUnits]): Measurement units of archive
            repository space that can be consumed by file share backups for free. Default:
            SubscriptionPlanFileShareBackupFreeFileShareHostedArchiveUsedSpaceUnits.GB.
        source_hosted_amount_of_data_price (Union[Unset, float]): Charge rate for one GB or TB of source data. Default:
            0.0.
        source_hosted_amount_of_data_units (Union[Unset, SubscriptionPlanFileShareBackupSourceHostedAmountOfDataUnits]):
            Measurement units of source data. Default: SubscriptionPlanFileShareBackupSourceHostedAmountOfDataUnits.GB.
        free_source_hosted_amount_of_data (Union[None, Unset, int]): Amount of source data that is processed for free.
            > Maximum value is `1048576` for GB and `1024` for TB.
        free_source_hosted_amount_of_data_units (Union[Unset,
            SubscriptionPlanFileShareBackupFreeSourceHostedAmountOfDataUnits]): Measurement units of source data that is
            processed for free. Default: SubscriptionPlanFileShareBackupFreeSourceHostedAmountOfDataUnits.GB.
    """

    file_share_remote_backup_used_space_price: Union[Unset, float] = 0.0
    file_share_remote_backup_used_space_units: Union[
        Unset, SubscriptionPlanFileShareBackupFileShareRemoteBackupUsedSpaceUnits
    ] = SubscriptionPlanFileShareBackupFileShareRemoteBackupUsedSpaceUnits.GB
    free_file_share_remote_backup_used_space: Union[None, Unset, int] = UNSET
    free_file_share_remote_backup_used_space_units: Union[
        Unset, SubscriptionPlanFileShareBackupFreeFileShareRemoteBackupUsedSpaceUnits
    ] = SubscriptionPlanFileShareBackupFreeFileShareRemoteBackupUsedSpaceUnits.GB
    file_share_remote_archive_used_space_price: Union[Unset, float] = 0.0
    file_share_remote_archive_used_space_units: Union[
        Unset, SubscriptionPlanFileShareBackupFileShareRemoteArchiveUsedSpaceUnits
    ] = SubscriptionPlanFileShareBackupFileShareRemoteArchiveUsedSpaceUnits.GB
    free_file_share_remote_archive_used_space: Union[None, Unset, int] = UNSET
    free_file_share_remote_archive_used_space_units: Union[
        Unset, SubscriptionPlanFileShareBackupFreeFileShareRemoteArchiveUsedSpaceUnits
    ] = SubscriptionPlanFileShareBackupFreeFileShareRemoteArchiveUsedSpaceUnits.GB
    source_remote_amount_of_data_price: Union[Unset, float] = 0.0
    source_remote_amount_of_data_units: Union[Unset, SubscriptionPlanFileShareBackupSourceRemoteAmountOfDataUnits] = (
        SubscriptionPlanFileShareBackupSourceRemoteAmountOfDataUnits.GB
    )
    free_source_remote_amount_of_data: Union[None, Unset, int] = UNSET
    free_source_remote_amount_of_data_units: Union[
        Unset, SubscriptionPlanFileShareBackupFreeSourceRemoteAmountOfDataUnits
    ] = SubscriptionPlanFileShareBackupFreeSourceRemoteAmountOfDataUnits.GB
    file_share_hosted_backup_used_space_price: Union[Unset, float] = 0.0
    file_share_hosted_backup_used_space_units: Union[
        Unset, SubscriptionPlanFileShareBackupFileShareHostedBackupUsedSpaceUnits
    ] = SubscriptionPlanFileShareBackupFileShareHostedBackupUsedSpaceUnits.GB
    free_file_share_hosted_backup_used_space: Union[None, Unset, int] = UNSET
    free_file_share_hosted_backup_used_space_units: Union[
        Unset, SubscriptionPlanFileShareBackupFreeFileShareHostedBackupUsedSpaceUnits
    ] = SubscriptionPlanFileShareBackupFreeFileShareHostedBackupUsedSpaceUnits.GB
    file_share_hosted_archive_used_space_price: Union[Unset, float] = 0.0
    file_share_hosted_archive_used_space_units: Union[
        Unset, SubscriptionPlanFileShareBackupFileShareHostedArchiveUsedSpaceUnits
    ] = SubscriptionPlanFileShareBackupFileShareHostedArchiveUsedSpaceUnits.GB
    free_file_share_hosted_archive_used_space: Union[None, Unset, int] = UNSET
    free_file_share_hosted_archive_used_space_units: Union[
        Unset, SubscriptionPlanFileShareBackupFreeFileShareHostedArchiveUsedSpaceUnits
    ] = SubscriptionPlanFileShareBackupFreeFileShareHostedArchiveUsedSpaceUnits.GB
    source_hosted_amount_of_data_price: Union[Unset, float] = 0.0
    source_hosted_amount_of_data_units: Union[Unset, SubscriptionPlanFileShareBackupSourceHostedAmountOfDataUnits] = (
        SubscriptionPlanFileShareBackupSourceHostedAmountOfDataUnits.GB
    )
    free_source_hosted_amount_of_data: Union[None, Unset, int] = UNSET
    free_source_hosted_amount_of_data_units: Union[
        Unset, SubscriptionPlanFileShareBackupFreeSourceHostedAmountOfDataUnits
    ] = SubscriptionPlanFileShareBackupFreeSourceHostedAmountOfDataUnits.GB
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        file_share_remote_backup_used_space_price = self.file_share_remote_backup_used_space_price

        file_share_remote_backup_used_space_units: Union[Unset, str] = UNSET
        if not isinstance(self.file_share_remote_backup_used_space_units, Unset):
            file_share_remote_backup_used_space_units = self.file_share_remote_backup_used_space_units.value

        free_file_share_remote_backup_used_space: Union[None, Unset, int]
        if isinstance(self.free_file_share_remote_backup_used_space, Unset):
            free_file_share_remote_backup_used_space = UNSET
        else:
            free_file_share_remote_backup_used_space = self.free_file_share_remote_backup_used_space

        free_file_share_remote_backup_used_space_units: Union[Unset, str] = UNSET
        if not isinstance(self.free_file_share_remote_backup_used_space_units, Unset):
            free_file_share_remote_backup_used_space_units = self.free_file_share_remote_backup_used_space_units.value

        file_share_remote_archive_used_space_price = self.file_share_remote_archive_used_space_price

        file_share_remote_archive_used_space_units: Union[Unset, str] = UNSET
        if not isinstance(self.file_share_remote_archive_used_space_units, Unset):
            file_share_remote_archive_used_space_units = self.file_share_remote_archive_used_space_units.value

        free_file_share_remote_archive_used_space: Union[None, Unset, int]
        if isinstance(self.free_file_share_remote_archive_used_space, Unset):
            free_file_share_remote_archive_used_space = UNSET
        else:
            free_file_share_remote_archive_used_space = self.free_file_share_remote_archive_used_space

        free_file_share_remote_archive_used_space_units: Union[Unset, str] = UNSET
        if not isinstance(self.free_file_share_remote_archive_used_space_units, Unset):
            free_file_share_remote_archive_used_space_units = self.free_file_share_remote_archive_used_space_units.value

        source_remote_amount_of_data_price = self.source_remote_amount_of_data_price

        source_remote_amount_of_data_units: Union[Unset, str] = UNSET
        if not isinstance(self.source_remote_amount_of_data_units, Unset):
            source_remote_amount_of_data_units = self.source_remote_amount_of_data_units.value

        free_source_remote_amount_of_data: Union[None, Unset, int]
        if isinstance(self.free_source_remote_amount_of_data, Unset):
            free_source_remote_amount_of_data = UNSET
        else:
            free_source_remote_amount_of_data = self.free_source_remote_amount_of_data

        free_source_remote_amount_of_data_units: Union[Unset, str] = UNSET
        if not isinstance(self.free_source_remote_amount_of_data_units, Unset):
            free_source_remote_amount_of_data_units = self.free_source_remote_amount_of_data_units.value

        file_share_hosted_backup_used_space_price = self.file_share_hosted_backup_used_space_price

        file_share_hosted_backup_used_space_units: Union[Unset, str] = UNSET
        if not isinstance(self.file_share_hosted_backup_used_space_units, Unset):
            file_share_hosted_backup_used_space_units = self.file_share_hosted_backup_used_space_units.value

        free_file_share_hosted_backup_used_space: Union[None, Unset, int]
        if isinstance(self.free_file_share_hosted_backup_used_space, Unset):
            free_file_share_hosted_backup_used_space = UNSET
        else:
            free_file_share_hosted_backup_used_space = self.free_file_share_hosted_backup_used_space

        free_file_share_hosted_backup_used_space_units: Union[Unset, str] = UNSET
        if not isinstance(self.free_file_share_hosted_backup_used_space_units, Unset):
            free_file_share_hosted_backup_used_space_units = self.free_file_share_hosted_backup_used_space_units.value

        file_share_hosted_archive_used_space_price = self.file_share_hosted_archive_used_space_price

        file_share_hosted_archive_used_space_units: Union[Unset, str] = UNSET
        if not isinstance(self.file_share_hosted_archive_used_space_units, Unset):
            file_share_hosted_archive_used_space_units = self.file_share_hosted_archive_used_space_units.value

        free_file_share_hosted_archive_used_space: Union[None, Unset, int]
        if isinstance(self.free_file_share_hosted_archive_used_space, Unset):
            free_file_share_hosted_archive_used_space = UNSET
        else:
            free_file_share_hosted_archive_used_space = self.free_file_share_hosted_archive_used_space

        free_file_share_hosted_archive_used_space_units: Union[Unset, str] = UNSET
        if not isinstance(self.free_file_share_hosted_archive_used_space_units, Unset):
            free_file_share_hosted_archive_used_space_units = self.free_file_share_hosted_archive_used_space_units.value

        source_hosted_amount_of_data_price = self.source_hosted_amount_of_data_price

        source_hosted_amount_of_data_units: Union[Unset, str] = UNSET
        if not isinstance(self.source_hosted_amount_of_data_units, Unset):
            source_hosted_amount_of_data_units = self.source_hosted_amount_of_data_units.value

        free_source_hosted_amount_of_data: Union[None, Unset, int]
        if isinstance(self.free_source_hosted_amount_of_data, Unset):
            free_source_hosted_amount_of_data = UNSET
        else:
            free_source_hosted_amount_of_data = self.free_source_hosted_amount_of_data

        free_source_hosted_amount_of_data_units: Union[Unset, str] = UNSET
        if not isinstance(self.free_source_hosted_amount_of_data_units, Unset):
            free_source_hosted_amount_of_data_units = self.free_source_hosted_amount_of_data_units.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if file_share_remote_backup_used_space_price is not UNSET:
            field_dict["fileShareRemoteBackupUsedSpacePrice"] = file_share_remote_backup_used_space_price
        if file_share_remote_backup_used_space_units is not UNSET:
            field_dict["fileShareRemoteBackupUsedSpaceUnits"] = file_share_remote_backup_used_space_units
        if free_file_share_remote_backup_used_space is not UNSET:
            field_dict["freeFileShareRemoteBackupUsedSpace"] = free_file_share_remote_backup_used_space
        if free_file_share_remote_backup_used_space_units is not UNSET:
            field_dict["freeFileShareRemoteBackupUsedSpaceUnits"] = free_file_share_remote_backup_used_space_units
        if file_share_remote_archive_used_space_price is not UNSET:
            field_dict["fileShareRemoteArchiveUsedSpacePrice"] = file_share_remote_archive_used_space_price
        if file_share_remote_archive_used_space_units is not UNSET:
            field_dict["fileShareRemoteArchiveUsedSpaceUnits"] = file_share_remote_archive_used_space_units
        if free_file_share_remote_archive_used_space is not UNSET:
            field_dict["freeFileShareRemoteArchiveUsedSpace"] = free_file_share_remote_archive_used_space
        if free_file_share_remote_archive_used_space_units is not UNSET:
            field_dict["freeFileShareRemoteArchiveUsedSpaceUnits"] = free_file_share_remote_archive_used_space_units
        if source_remote_amount_of_data_price is not UNSET:
            field_dict["sourceRemoteAmountOfDataPrice"] = source_remote_amount_of_data_price
        if source_remote_amount_of_data_units is not UNSET:
            field_dict["sourceRemoteAmountOfDataUnits"] = source_remote_amount_of_data_units
        if free_source_remote_amount_of_data is not UNSET:
            field_dict["freeSourceRemoteAmountOfData"] = free_source_remote_amount_of_data
        if free_source_remote_amount_of_data_units is not UNSET:
            field_dict["freeSourceRemoteAmountOfDataUnits"] = free_source_remote_amount_of_data_units
        if file_share_hosted_backup_used_space_price is not UNSET:
            field_dict["fileShareHostedBackupUsedSpacePrice"] = file_share_hosted_backup_used_space_price
        if file_share_hosted_backup_used_space_units is not UNSET:
            field_dict["fileShareHostedBackupUsedSpaceUnits"] = file_share_hosted_backup_used_space_units
        if free_file_share_hosted_backup_used_space is not UNSET:
            field_dict["freeFileShareHostedBackupUsedSpace"] = free_file_share_hosted_backup_used_space
        if free_file_share_hosted_backup_used_space_units is not UNSET:
            field_dict["freeFileShareHostedBackupUsedSpaceUnits"] = free_file_share_hosted_backup_used_space_units
        if file_share_hosted_archive_used_space_price is not UNSET:
            field_dict["fileShareHostedArchiveUsedSpacePrice"] = file_share_hosted_archive_used_space_price
        if file_share_hosted_archive_used_space_units is not UNSET:
            field_dict["fileShareHostedArchiveUsedSpaceUnits"] = file_share_hosted_archive_used_space_units
        if free_file_share_hosted_archive_used_space is not UNSET:
            field_dict["freeFileShareHostedArchiveUsedSpace"] = free_file_share_hosted_archive_used_space
        if free_file_share_hosted_archive_used_space_units is not UNSET:
            field_dict["freeFileShareHostedArchiveUsedSpaceUnits"] = free_file_share_hosted_archive_used_space_units
        if source_hosted_amount_of_data_price is not UNSET:
            field_dict["sourceHostedAmountOfDataPrice"] = source_hosted_amount_of_data_price
        if source_hosted_amount_of_data_units is not UNSET:
            field_dict["sourceHostedAmountOfDataUnits"] = source_hosted_amount_of_data_units
        if free_source_hosted_amount_of_data is not UNSET:
            field_dict["freeSourceHostedAmountOfData"] = free_source_hosted_amount_of_data
        if free_source_hosted_amount_of_data_units is not UNSET:
            field_dict["freeSourceHostedAmountOfDataUnits"] = free_source_hosted_amount_of_data_units

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        file_share_remote_backup_used_space_price = d.pop("fileShareRemoteBackupUsedSpacePrice", UNSET)

        _file_share_remote_backup_used_space_units = d.pop("fileShareRemoteBackupUsedSpaceUnits", UNSET)
        file_share_remote_backup_used_space_units: Union[
            Unset, SubscriptionPlanFileShareBackupFileShareRemoteBackupUsedSpaceUnits
        ]
        if isinstance(_file_share_remote_backup_used_space_units, Unset):
            file_share_remote_backup_used_space_units = UNSET
        else:
            file_share_remote_backup_used_space_units = (
                SubscriptionPlanFileShareBackupFileShareRemoteBackupUsedSpaceUnits(
                    _file_share_remote_backup_used_space_units
                )
            )

        def _parse_free_file_share_remote_backup_used_space(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        free_file_share_remote_backup_used_space = _parse_free_file_share_remote_backup_used_space(
            d.pop("freeFileShareRemoteBackupUsedSpace", UNSET)
        )

        _free_file_share_remote_backup_used_space_units = d.pop("freeFileShareRemoteBackupUsedSpaceUnits", UNSET)
        free_file_share_remote_backup_used_space_units: Union[
            Unset, SubscriptionPlanFileShareBackupFreeFileShareRemoteBackupUsedSpaceUnits
        ]
        if isinstance(_free_file_share_remote_backup_used_space_units, Unset):
            free_file_share_remote_backup_used_space_units = UNSET
        else:
            free_file_share_remote_backup_used_space_units = (
                SubscriptionPlanFileShareBackupFreeFileShareRemoteBackupUsedSpaceUnits(
                    _free_file_share_remote_backup_used_space_units
                )
            )

        file_share_remote_archive_used_space_price = d.pop("fileShareRemoteArchiveUsedSpacePrice", UNSET)

        _file_share_remote_archive_used_space_units = d.pop("fileShareRemoteArchiveUsedSpaceUnits", UNSET)
        file_share_remote_archive_used_space_units: Union[
            Unset, SubscriptionPlanFileShareBackupFileShareRemoteArchiveUsedSpaceUnits
        ]
        if isinstance(_file_share_remote_archive_used_space_units, Unset):
            file_share_remote_archive_used_space_units = UNSET
        else:
            file_share_remote_archive_used_space_units = (
                SubscriptionPlanFileShareBackupFileShareRemoteArchiveUsedSpaceUnits(
                    _file_share_remote_archive_used_space_units
                )
            )

        def _parse_free_file_share_remote_archive_used_space(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        free_file_share_remote_archive_used_space = _parse_free_file_share_remote_archive_used_space(
            d.pop("freeFileShareRemoteArchiveUsedSpace", UNSET)
        )

        _free_file_share_remote_archive_used_space_units = d.pop("freeFileShareRemoteArchiveUsedSpaceUnits", UNSET)
        free_file_share_remote_archive_used_space_units: Union[
            Unset, SubscriptionPlanFileShareBackupFreeFileShareRemoteArchiveUsedSpaceUnits
        ]
        if isinstance(_free_file_share_remote_archive_used_space_units, Unset):
            free_file_share_remote_archive_used_space_units = UNSET
        else:
            free_file_share_remote_archive_used_space_units = (
                SubscriptionPlanFileShareBackupFreeFileShareRemoteArchiveUsedSpaceUnits(
                    _free_file_share_remote_archive_used_space_units
                )
            )

        source_remote_amount_of_data_price = d.pop("sourceRemoteAmountOfDataPrice", UNSET)

        _source_remote_amount_of_data_units = d.pop("sourceRemoteAmountOfDataUnits", UNSET)
        source_remote_amount_of_data_units: Union[Unset, SubscriptionPlanFileShareBackupSourceRemoteAmountOfDataUnits]
        if isinstance(_source_remote_amount_of_data_units, Unset):
            source_remote_amount_of_data_units = UNSET
        else:
            source_remote_amount_of_data_units = SubscriptionPlanFileShareBackupSourceRemoteAmountOfDataUnits(
                _source_remote_amount_of_data_units
            )

        def _parse_free_source_remote_amount_of_data(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        free_source_remote_amount_of_data = _parse_free_source_remote_amount_of_data(
            d.pop("freeSourceRemoteAmountOfData", UNSET)
        )

        _free_source_remote_amount_of_data_units = d.pop("freeSourceRemoteAmountOfDataUnits", UNSET)
        free_source_remote_amount_of_data_units: Union[
            Unset, SubscriptionPlanFileShareBackupFreeSourceRemoteAmountOfDataUnits
        ]
        if isinstance(_free_source_remote_amount_of_data_units, Unset):
            free_source_remote_amount_of_data_units = UNSET
        else:
            free_source_remote_amount_of_data_units = SubscriptionPlanFileShareBackupFreeSourceRemoteAmountOfDataUnits(
                _free_source_remote_amount_of_data_units
            )

        file_share_hosted_backup_used_space_price = d.pop("fileShareHostedBackupUsedSpacePrice", UNSET)

        _file_share_hosted_backup_used_space_units = d.pop("fileShareHostedBackupUsedSpaceUnits", UNSET)
        file_share_hosted_backup_used_space_units: Union[
            Unset, SubscriptionPlanFileShareBackupFileShareHostedBackupUsedSpaceUnits
        ]
        if isinstance(_file_share_hosted_backup_used_space_units, Unset):
            file_share_hosted_backup_used_space_units = UNSET
        else:
            file_share_hosted_backup_used_space_units = (
                SubscriptionPlanFileShareBackupFileShareHostedBackupUsedSpaceUnits(
                    _file_share_hosted_backup_used_space_units
                )
            )

        def _parse_free_file_share_hosted_backup_used_space(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        free_file_share_hosted_backup_used_space = _parse_free_file_share_hosted_backup_used_space(
            d.pop("freeFileShareHostedBackupUsedSpace", UNSET)
        )

        _free_file_share_hosted_backup_used_space_units = d.pop("freeFileShareHostedBackupUsedSpaceUnits", UNSET)
        free_file_share_hosted_backup_used_space_units: Union[
            Unset, SubscriptionPlanFileShareBackupFreeFileShareHostedBackupUsedSpaceUnits
        ]
        if isinstance(_free_file_share_hosted_backup_used_space_units, Unset):
            free_file_share_hosted_backup_used_space_units = UNSET
        else:
            free_file_share_hosted_backup_used_space_units = (
                SubscriptionPlanFileShareBackupFreeFileShareHostedBackupUsedSpaceUnits(
                    _free_file_share_hosted_backup_used_space_units
                )
            )

        file_share_hosted_archive_used_space_price = d.pop("fileShareHostedArchiveUsedSpacePrice", UNSET)

        _file_share_hosted_archive_used_space_units = d.pop("fileShareHostedArchiveUsedSpaceUnits", UNSET)
        file_share_hosted_archive_used_space_units: Union[
            Unset, SubscriptionPlanFileShareBackupFileShareHostedArchiveUsedSpaceUnits
        ]
        if isinstance(_file_share_hosted_archive_used_space_units, Unset):
            file_share_hosted_archive_used_space_units = UNSET
        else:
            file_share_hosted_archive_used_space_units = (
                SubscriptionPlanFileShareBackupFileShareHostedArchiveUsedSpaceUnits(
                    _file_share_hosted_archive_used_space_units
                )
            )

        def _parse_free_file_share_hosted_archive_used_space(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        free_file_share_hosted_archive_used_space = _parse_free_file_share_hosted_archive_used_space(
            d.pop("freeFileShareHostedArchiveUsedSpace", UNSET)
        )

        _free_file_share_hosted_archive_used_space_units = d.pop("freeFileShareHostedArchiveUsedSpaceUnits", UNSET)
        free_file_share_hosted_archive_used_space_units: Union[
            Unset, SubscriptionPlanFileShareBackupFreeFileShareHostedArchiveUsedSpaceUnits
        ]
        if isinstance(_free_file_share_hosted_archive_used_space_units, Unset):
            free_file_share_hosted_archive_used_space_units = UNSET
        else:
            free_file_share_hosted_archive_used_space_units = (
                SubscriptionPlanFileShareBackupFreeFileShareHostedArchiveUsedSpaceUnits(
                    _free_file_share_hosted_archive_used_space_units
                )
            )

        source_hosted_amount_of_data_price = d.pop("sourceHostedAmountOfDataPrice", UNSET)

        _source_hosted_amount_of_data_units = d.pop("sourceHostedAmountOfDataUnits", UNSET)
        source_hosted_amount_of_data_units: Union[Unset, SubscriptionPlanFileShareBackupSourceHostedAmountOfDataUnits]
        if isinstance(_source_hosted_amount_of_data_units, Unset):
            source_hosted_amount_of_data_units = UNSET
        else:
            source_hosted_amount_of_data_units = SubscriptionPlanFileShareBackupSourceHostedAmountOfDataUnits(
                _source_hosted_amount_of_data_units
            )

        def _parse_free_source_hosted_amount_of_data(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        free_source_hosted_amount_of_data = _parse_free_source_hosted_amount_of_data(
            d.pop("freeSourceHostedAmountOfData", UNSET)
        )

        _free_source_hosted_amount_of_data_units = d.pop("freeSourceHostedAmountOfDataUnits", UNSET)
        free_source_hosted_amount_of_data_units: Union[
            Unset, SubscriptionPlanFileShareBackupFreeSourceHostedAmountOfDataUnits
        ]
        if isinstance(_free_source_hosted_amount_of_data_units, Unset):
            free_source_hosted_amount_of_data_units = UNSET
        else:
            free_source_hosted_amount_of_data_units = SubscriptionPlanFileShareBackupFreeSourceHostedAmountOfDataUnits(
                _free_source_hosted_amount_of_data_units
            )

        subscription_plan_file_share_backup = cls(
            file_share_remote_backup_used_space_price=file_share_remote_backup_used_space_price,
            file_share_remote_backup_used_space_units=file_share_remote_backup_used_space_units,
            free_file_share_remote_backup_used_space=free_file_share_remote_backup_used_space,
            free_file_share_remote_backup_used_space_units=free_file_share_remote_backup_used_space_units,
            file_share_remote_archive_used_space_price=file_share_remote_archive_used_space_price,
            file_share_remote_archive_used_space_units=file_share_remote_archive_used_space_units,
            free_file_share_remote_archive_used_space=free_file_share_remote_archive_used_space,
            free_file_share_remote_archive_used_space_units=free_file_share_remote_archive_used_space_units,
            source_remote_amount_of_data_price=source_remote_amount_of_data_price,
            source_remote_amount_of_data_units=source_remote_amount_of_data_units,
            free_source_remote_amount_of_data=free_source_remote_amount_of_data,
            free_source_remote_amount_of_data_units=free_source_remote_amount_of_data_units,
            file_share_hosted_backup_used_space_price=file_share_hosted_backup_used_space_price,
            file_share_hosted_backup_used_space_units=file_share_hosted_backup_used_space_units,
            free_file_share_hosted_backup_used_space=free_file_share_hosted_backup_used_space,
            free_file_share_hosted_backup_used_space_units=free_file_share_hosted_backup_used_space_units,
            file_share_hosted_archive_used_space_price=file_share_hosted_archive_used_space_price,
            file_share_hosted_archive_used_space_units=file_share_hosted_archive_used_space_units,
            free_file_share_hosted_archive_used_space=free_file_share_hosted_archive_used_space,
            free_file_share_hosted_archive_used_space_units=free_file_share_hosted_archive_used_space_units,
            source_hosted_amount_of_data_price=source_hosted_amount_of_data_price,
            source_hosted_amount_of_data_units=source_hosted_amount_of_data_units,
            free_source_hosted_amount_of_data=free_source_hosted_amount_of_data,
            free_source_hosted_amount_of_data_units=free_source_hosted_amount_of_data_units,
        )

        subscription_plan_file_share_backup.additional_properties = d
        return subscription_plan_file_share_backup

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
