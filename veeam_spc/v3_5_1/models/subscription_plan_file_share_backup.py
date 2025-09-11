from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.subscription_plan_file_share_backup_file_share_archive_used_space_units import (
    SubscriptionPlanFileShareBackupFileShareArchiveUsedSpaceUnits,
)
from ..models.subscription_plan_file_share_backup_file_share_backup_used_space_units import (
    SubscriptionPlanFileShareBackupFileShareBackupUsedSpaceUnits,
)
from ..models.subscription_plan_file_share_backup_free_file_share_archive_used_space_units import (
    SubscriptionPlanFileShareBackupFreeFileShareArchiveUsedSpaceUnits,
)
from ..models.subscription_plan_file_share_backup_free_file_share_backup_used_space_units import (
    SubscriptionPlanFileShareBackupFreeFileShareBackupUsedSpaceUnits,
)
from ..models.subscription_plan_file_share_backup_free_source_amount_of_data_units import (
    SubscriptionPlanFileShareBackupFreeSourceAmountOfDataUnits,
)
from ..models.subscription_plan_file_share_backup_source_amount_of_data_units import (
    SubscriptionPlanFileShareBackupSourceAmountOfDataUnits,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="SubscriptionPlanFileShareBackup")


@_attrs_define
class SubscriptionPlanFileShareBackup:
    """
    Attributes:
        file_share_backup_used_space_price (Union[Unset, float]): Charge rate for one GB or TB of backup repository
            space consumed by file share backups. Default: 0.0.
        file_share_backup_used_space_units (Union[Unset, SubscriptionPlanFileShareBackupFileShareBackupUsedSpaceUnits]):
            Measurement units of backup repository space consumed by file share backups. Default:
            SubscriptionPlanFileShareBackupFileShareBackupUsedSpaceUnits.GB.
        free_file_share_backup_used_space (Union[Unset, int]): Amount of backup repository space that can be consumed by
            file share backups for free.
            > Maximum value is `1048576` for GB and `1024` for TB.
        free_file_share_backup_used_space_units (Union[Unset,
            SubscriptionPlanFileShareBackupFreeFileShareBackupUsedSpaceUnits]): Measurement units of backup repository space
            that can be consumed by file share backups for free. Default:
            SubscriptionPlanFileShareBackupFreeFileShareBackupUsedSpaceUnits.GB.
        file_share_archive_used_space_price (Union[Unset, float]): Charge rate for one GB or TB of archive repository
            space consumed by file share backups. Default: 0.0.
        file_share_archive_used_space_units (Union[Unset,
            SubscriptionPlanFileShareBackupFileShareArchiveUsedSpaceUnits]): Measurement units of archive repository space
            consumed by file share backups. Default: SubscriptionPlanFileShareBackupFileShareArchiveUsedSpaceUnits.GB.
        free_file_share_archive_used_space (Union[Unset, int]): Amount of archive repository space that can be consumed
            by file share backups for free.
            > Maximum value is `1048576` for GB and `1024` for TB.
        free_file_share_archive_used_space_units (Union[Unset,
            SubscriptionPlanFileShareBackupFreeFileShareArchiveUsedSpaceUnits]): Measurement units of archive repository
            space that can be consumed by file share backups for free. Default:
            SubscriptionPlanFileShareBackupFreeFileShareArchiveUsedSpaceUnits.GB.
        source_amount_of_data_price (Union[Unset, float]): Charge rate for one GB or TB of source data. Default: 0.0.
        source_amount_of_data_units (Union[Unset, SubscriptionPlanFileShareBackupSourceAmountOfDataUnits]): Measurement
            units of source data. Default: SubscriptionPlanFileShareBackupSourceAmountOfDataUnits.GB.
        free_source_amount_of_data (Union[Unset, int]): Amount of source data that is processed for free.
            > Maximum value is `1048576` for GB and `1024` for TB.
        free_source_amount_of_data_units (Union[Unset, SubscriptionPlanFileShareBackupFreeSourceAmountOfDataUnits]):
            Measurement units of source data that is processed for free. Default:
            SubscriptionPlanFileShareBackupFreeSourceAmountOfDataUnits.GB.
    """

    file_share_backup_used_space_price: Union[Unset, float] = 0.0
    file_share_backup_used_space_units: Union[Unset, SubscriptionPlanFileShareBackupFileShareBackupUsedSpaceUnits] = (
        SubscriptionPlanFileShareBackupFileShareBackupUsedSpaceUnits.GB
    )
    free_file_share_backup_used_space: Union[Unset, int] = UNSET
    free_file_share_backup_used_space_units: Union[
        Unset, SubscriptionPlanFileShareBackupFreeFileShareBackupUsedSpaceUnits
    ] = SubscriptionPlanFileShareBackupFreeFileShareBackupUsedSpaceUnits.GB
    file_share_archive_used_space_price: Union[Unset, float] = 0.0
    file_share_archive_used_space_units: Union[Unset, SubscriptionPlanFileShareBackupFileShareArchiveUsedSpaceUnits] = (
        SubscriptionPlanFileShareBackupFileShareArchiveUsedSpaceUnits.GB
    )
    free_file_share_archive_used_space: Union[Unset, int] = UNSET
    free_file_share_archive_used_space_units: Union[
        Unset, SubscriptionPlanFileShareBackupFreeFileShareArchiveUsedSpaceUnits
    ] = SubscriptionPlanFileShareBackupFreeFileShareArchiveUsedSpaceUnits.GB
    source_amount_of_data_price: Union[Unset, float] = 0.0
    source_amount_of_data_units: Union[Unset, SubscriptionPlanFileShareBackupSourceAmountOfDataUnits] = (
        SubscriptionPlanFileShareBackupSourceAmountOfDataUnits.GB
    )
    free_source_amount_of_data: Union[Unset, int] = UNSET
    free_source_amount_of_data_units: Union[Unset, SubscriptionPlanFileShareBackupFreeSourceAmountOfDataUnits] = (
        SubscriptionPlanFileShareBackupFreeSourceAmountOfDataUnits.GB
    )
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        file_share_backup_used_space_price = self.file_share_backup_used_space_price

        file_share_backup_used_space_units: Union[Unset, str] = UNSET
        if not isinstance(self.file_share_backup_used_space_units, Unset):
            file_share_backup_used_space_units = self.file_share_backup_used_space_units.value

        free_file_share_backup_used_space = self.free_file_share_backup_used_space

        free_file_share_backup_used_space_units: Union[Unset, str] = UNSET
        if not isinstance(self.free_file_share_backup_used_space_units, Unset):
            free_file_share_backup_used_space_units = self.free_file_share_backup_used_space_units.value

        file_share_archive_used_space_price = self.file_share_archive_used_space_price

        file_share_archive_used_space_units: Union[Unset, str] = UNSET
        if not isinstance(self.file_share_archive_used_space_units, Unset):
            file_share_archive_used_space_units = self.file_share_archive_used_space_units.value

        free_file_share_archive_used_space = self.free_file_share_archive_used_space

        free_file_share_archive_used_space_units: Union[Unset, str] = UNSET
        if not isinstance(self.free_file_share_archive_used_space_units, Unset):
            free_file_share_archive_used_space_units = self.free_file_share_archive_used_space_units.value

        source_amount_of_data_price = self.source_amount_of_data_price

        source_amount_of_data_units: Union[Unset, str] = UNSET
        if not isinstance(self.source_amount_of_data_units, Unset):
            source_amount_of_data_units = self.source_amount_of_data_units.value

        free_source_amount_of_data = self.free_source_amount_of_data

        free_source_amount_of_data_units: Union[Unset, str] = UNSET
        if not isinstance(self.free_source_amount_of_data_units, Unset):
            free_source_amount_of_data_units = self.free_source_amount_of_data_units.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if file_share_backup_used_space_price is not UNSET:
            field_dict["fileShareBackupUsedSpacePrice"] = file_share_backup_used_space_price
        if file_share_backup_used_space_units is not UNSET:
            field_dict["fileShareBackupUsedSpaceUnits"] = file_share_backup_used_space_units
        if free_file_share_backup_used_space is not UNSET:
            field_dict["freeFileShareBackupUsedSpace"] = free_file_share_backup_used_space
        if free_file_share_backup_used_space_units is not UNSET:
            field_dict["freeFileShareBackupUsedSpaceUnits"] = free_file_share_backup_used_space_units
        if file_share_archive_used_space_price is not UNSET:
            field_dict["fileShareArchiveUsedSpacePrice"] = file_share_archive_used_space_price
        if file_share_archive_used_space_units is not UNSET:
            field_dict["fileShareArchiveUsedSpaceUnits"] = file_share_archive_used_space_units
        if free_file_share_archive_used_space is not UNSET:
            field_dict["freeFileShareArchiveUsedSpace"] = free_file_share_archive_used_space
        if free_file_share_archive_used_space_units is not UNSET:
            field_dict["freeFileShareArchiveUsedSpaceUnits"] = free_file_share_archive_used_space_units
        if source_amount_of_data_price is not UNSET:
            field_dict["sourceAmountOfDataPrice"] = source_amount_of_data_price
        if source_amount_of_data_units is not UNSET:
            field_dict["sourceAmountOfDataUnits"] = source_amount_of_data_units
        if free_source_amount_of_data is not UNSET:
            field_dict["freeSourceAmountOfData"] = free_source_amount_of_data
        if free_source_amount_of_data_units is not UNSET:
            field_dict["freeSourceAmountOfDataUnits"] = free_source_amount_of_data_units

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        file_share_backup_used_space_price = d.pop("fileShareBackupUsedSpacePrice", UNSET)

        _file_share_backup_used_space_units = d.pop("fileShareBackupUsedSpaceUnits", UNSET)
        file_share_backup_used_space_units: Union[Unset, SubscriptionPlanFileShareBackupFileShareBackupUsedSpaceUnits]
        if isinstance(_file_share_backup_used_space_units, Unset):
            file_share_backup_used_space_units = UNSET
        else:
            file_share_backup_used_space_units = SubscriptionPlanFileShareBackupFileShareBackupUsedSpaceUnits(
                _file_share_backup_used_space_units
            )

        free_file_share_backup_used_space = d.pop("freeFileShareBackupUsedSpace", UNSET)

        _free_file_share_backup_used_space_units = d.pop("freeFileShareBackupUsedSpaceUnits", UNSET)
        free_file_share_backup_used_space_units: Union[
            Unset, SubscriptionPlanFileShareBackupFreeFileShareBackupUsedSpaceUnits
        ]
        if isinstance(_free_file_share_backup_used_space_units, Unset):
            free_file_share_backup_used_space_units = UNSET
        else:
            free_file_share_backup_used_space_units = SubscriptionPlanFileShareBackupFreeFileShareBackupUsedSpaceUnits(
                _free_file_share_backup_used_space_units
            )

        file_share_archive_used_space_price = d.pop("fileShareArchiveUsedSpacePrice", UNSET)

        _file_share_archive_used_space_units = d.pop("fileShareArchiveUsedSpaceUnits", UNSET)
        file_share_archive_used_space_units: Union[Unset, SubscriptionPlanFileShareBackupFileShareArchiveUsedSpaceUnits]
        if isinstance(_file_share_archive_used_space_units, Unset):
            file_share_archive_used_space_units = UNSET
        else:
            file_share_archive_used_space_units = SubscriptionPlanFileShareBackupFileShareArchiveUsedSpaceUnits(
                _file_share_archive_used_space_units
            )

        free_file_share_archive_used_space = d.pop("freeFileShareArchiveUsedSpace", UNSET)

        _free_file_share_archive_used_space_units = d.pop("freeFileShareArchiveUsedSpaceUnits", UNSET)
        free_file_share_archive_used_space_units: Union[
            Unset, SubscriptionPlanFileShareBackupFreeFileShareArchiveUsedSpaceUnits
        ]
        if isinstance(_free_file_share_archive_used_space_units, Unset):
            free_file_share_archive_used_space_units = UNSET
        else:
            free_file_share_archive_used_space_units = (
                SubscriptionPlanFileShareBackupFreeFileShareArchiveUsedSpaceUnits(
                    _free_file_share_archive_used_space_units
                )
            )

        source_amount_of_data_price = d.pop("sourceAmountOfDataPrice", UNSET)

        _source_amount_of_data_units = d.pop("sourceAmountOfDataUnits", UNSET)
        source_amount_of_data_units: Union[Unset, SubscriptionPlanFileShareBackupSourceAmountOfDataUnits]
        if isinstance(_source_amount_of_data_units, Unset):
            source_amount_of_data_units = UNSET
        else:
            source_amount_of_data_units = SubscriptionPlanFileShareBackupSourceAmountOfDataUnits(
                _source_amount_of_data_units
            )

        free_source_amount_of_data = d.pop("freeSourceAmountOfData", UNSET)

        _free_source_amount_of_data_units = d.pop("freeSourceAmountOfDataUnits", UNSET)
        free_source_amount_of_data_units: Union[Unset, SubscriptionPlanFileShareBackupFreeSourceAmountOfDataUnits]
        if isinstance(_free_source_amount_of_data_units, Unset):
            free_source_amount_of_data_units = UNSET
        else:
            free_source_amount_of_data_units = SubscriptionPlanFileShareBackupFreeSourceAmountOfDataUnits(
                _free_source_amount_of_data_units
            )

        subscription_plan_file_share_backup = cls(
            file_share_backup_used_space_price=file_share_backup_used_space_price,
            file_share_backup_used_space_units=file_share_backup_used_space_units,
            free_file_share_backup_used_space=free_file_share_backup_used_space,
            free_file_share_backup_used_space_units=free_file_share_backup_used_space_units,
            file_share_archive_used_space_price=file_share_archive_used_space_price,
            file_share_archive_used_space_units=file_share_archive_used_space_units,
            free_file_share_archive_used_space=free_file_share_archive_used_space,
            free_file_share_archive_used_space_units=free_file_share_archive_used_space_units,
            source_amount_of_data_price=source_amount_of_data_price,
            source_amount_of_data_units=source_amount_of_data_units,
            free_source_amount_of_data=free_source_amount_of_data,
            free_source_amount_of_data_units=free_source_amount_of_data_units,
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
