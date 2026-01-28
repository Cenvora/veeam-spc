from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.vb_365_backup_repository_daily_type import Vb365BackupRepositoryDailyType
from ..models.vb_365_backup_repository_monthly_day_number import Vb365BackupRepositoryMonthlyDayNumber
from ..models.vb_365_backup_repository_monthly_day_of_week import Vb365BackupRepositoryMonthlyDayOfWeek
from ..models.vb_365_backup_repository_retention_frequency_type import Vb365BackupRepositoryRetentionFrequencyType
from ..models.vb_365_backup_repository_retention_period_type import Vb365BackupRepositoryRetentionPeriodType
from ..models.vb_365_backup_repository_retention_type import Vb365BackupRepositoryRetentionType
from ..models.vb_365_backup_repository_yearly_retention_period import Vb365BackupRepositoryYearlyRetentionPeriod
from ..types import UNSET, Unset

T = TypeVar("T", bound="Vb365BackupRepository")


@_attrs_define
class Vb365BackupRepository:
    """
    Attributes:
        instance_uid (Union[Unset, UUID]): UID assigned to a backup repository.
        name (Union[Unset, str]): Name of a backup repository
        description (Union[Unset, str]): Description of a backup repository
        proxy_uid (Union[None, UUID, Unset]): UID assigned to a backup proxy.
        proxy_pool_uid (Union[None, UUID, Unset]): UID assigned to a backup proxy pool.
        path (Union[Unset, str]): Path to a folder that contains backup files.
        is_archive_repository (Union[Unset, bool]): Indicates whether a backup repository is used as an archive
            repository.
        is_available_for_backup_job (Union[Unset, bool]): Indicates whether a backup repository can be used to store
            backups.
        is_available_for_copy_job (Union[Unset, bool]): Indicates whether a backup repository can be used to store
            backup copies.
        is_object_storage_repository (Union[Unset, bool]): Indicates whether a backup repository is used as an object
            storage.
        object_storage_repository_uid (Union[None, UUID, Unset]): UID assigned to an object storage.
        object_storage_repository_cache_path (Union[Unset, str]): Path to the directory of the backup repository on a
            backup proxy server.
        object_storage_repository_encryption_enabled (Union[None, Unset, bool]): Indicates whether the object storage
            encryption is enabled.
        encryption_key_id (Union[None, UUID, Unset]): ID assigned to an encryption key.
        is_out_of_sync (Union[Unset, bool]): Indicates whether a backup proxy server must be synchronized with the
            object storage to get the same cache state.
        capacity_bytes (Union[None, Unset, int]): Storage capacity, in bytes.
        free_space_bytes (Union[None, Unset, int]): Amount of free disk space on a backup repository, in bytes.
        used_space_bytes (Union[None, Unset, int]): Amount of used disk space on a backup repository, in bytes.
        daily_retention_period (Union[None, Unset, int]): Retention period in days.
        monthly_retention_period (Union[None, Unset, int]): Retention period in months.
        daily_time (Union[Unset, str]): Time of the day when the daily clean-up must be performed.
        monthly_time (Union[Unset, str]):  Time of the day when the monthly clean-up must be performed.
        retention_type (Union[Unset, Vb365BackupRepositoryRetentionType]): Type of the retention policy.
        retention_period_type (Union[Unset, Vb365BackupRepositoryRetentionPeriodType]): Retention period type.
        yearly_retention_period (Union[Unset, Vb365BackupRepositoryYearlyRetentionPeriod]): Retention period in years.
        retention_frequency_type (Union[Unset, Vb365BackupRepositoryRetentionFrequencyType]): Clean-up schedule type.
        daily_type (Union[Unset, Vb365BackupRepositoryDailyType]): Days when the daily clean-up must be performed.
        monthly_day_number (Union[Unset, Vb365BackupRepositoryMonthlyDayNumber]): Ordinal number of the week when the
            monthly clean-up must be performed.
        monthly_day_of_week (Union[Unset, Vb365BackupRepositoryMonthlyDayOfWeek]): Day of the week when the monthly
            clean-up must be performed.
    """

    instance_uid: Union[Unset, UUID] = UNSET
    name: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    proxy_uid: Union[None, UUID, Unset] = UNSET
    proxy_pool_uid: Union[None, UUID, Unset] = UNSET
    path: Union[Unset, str] = UNSET
    is_archive_repository: Union[Unset, bool] = UNSET
    is_available_for_backup_job: Union[Unset, bool] = UNSET
    is_available_for_copy_job: Union[Unset, bool] = UNSET
    is_object_storage_repository: Union[Unset, bool] = UNSET
    object_storage_repository_uid: Union[None, UUID, Unset] = UNSET
    object_storage_repository_cache_path: Union[Unset, str] = UNSET
    object_storage_repository_encryption_enabled: Union[None, Unset, bool] = UNSET
    encryption_key_id: Union[None, UUID, Unset] = UNSET
    is_out_of_sync: Union[Unset, bool] = UNSET
    capacity_bytes: Union[None, Unset, int] = UNSET
    free_space_bytes: Union[None, Unset, int] = UNSET
    used_space_bytes: Union[None, Unset, int] = UNSET
    daily_retention_period: Union[None, Unset, int] = UNSET
    monthly_retention_period: Union[None, Unset, int] = UNSET
    daily_time: Union[Unset, str] = UNSET
    monthly_time: Union[Unset, str] = UNSET
    retention_type: Union[Unset, Vb365BackupRepositoryRetentionType] = UNSET
    retention_period_type: Union[Unset, Vb365BackupRepositoryRetentionPeriodType] = UNSET
    yearly_retention_period: Union[Unset, Vb365BackupRepositoryYearlyRetentionPeriod] = UNSET
    retention_frequency_type: Union[Unset, Vb365BackupRepositoryRetentionFrequencyType] = UNSET
    daily_type: Union[Unset, Vb365BackupRepositoryDailyType] = UNSET
    monthly_day_number: Union[Unset, Vb365BackupRepositoryMonthlyDayNumber] = UNSET
    monthly_day_of_week: Union[Unset, Vb365BackupRepositoryMonthlyDayOfWeek] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        instance_uid: Union[Unset, str] = UNSET
        if not isinstance(self.instance_uid, Unset):
            instance_uid = str(self.instance_uid)

        name = self.name

        description = self.description

        proxy_uid: Union[None, Unset, str]
        if isinstance(self.proxy_uid, Unset):
            proxy_uid = UNSET
        elif isinstance(self.proxy_uid, UUID):
            proxy_uid = str(self.proxy_uid)
        else:
            proxy_uid = self.proxy_uid

        proxy_pool_uid: Union[None, Unset, str]
        if isinstance(self.proxy_pool_uid, Unset):
            proxy_pool_uid = UNSET
        elif isinstance(self.proxy_pool_uid, UUID):
            proxy_pool_uid = str(self.proxy_pool_uid)
        else:
            proxy_pool_uid = self.proxy_pool_uid

        path = self.path

        is_archive_repository = self.is_archive_repository

        is_available_for_backup_job = self.is_available_for_backup_job

        is_available_for_copy_job = self.is_available_for_copy_job

        is_object_storage_repository = self.is_object_storage_repository

        object_storage_repository_uid: Union[None, Unset, str]
        if isinstance(self.object_storage_repository_uid, Unset):
            object_storage_repository_uid = UNSET
        elif isinstance(self.object_storage_repository_uid, UUID):
            object_storage_repository_uid = str(self.object_storage_repository_uid)
        else:
            object_storage_repository_uid = self.object_storage_repository_uid

        object_storage_repository_cache_path = self.object_storage_repository_cache_path

        object_storage_repository_encryption_enabled: Union[None, Unset, bool]
        if isinstance(self.object_storage_repository_encryption_enabled, Unset):
            object_storage_repository_encryption_enabled = UNSET
        else:
            object_storage_repository_encryption_enabled = self.object_storage_repository_encryption_enabled

        encryption_key_id: Union[None, Unset, str]
        if isinstance(self.encryption_key_id, Unset):
            encryption_key_id = UNSET
        elif isinstance(self.encryption_key_id, UUID):
            encryption_key_id = str(self.encryption_key_id)
        else:
            encryption_key_id = self.encryption_key_id

        is_out_of_sync = self.is_out_of_sync

        capacity_bytes: Union[None, Unset, int]
        if isinstance(self.capacity_bytes, Unset):
            capacity_bytes = UNSET
        else:
            capacity_bytes = self.capacity_bytes

        free_space_bytes: Union[None, Unset, int]
        if isinstance(self.free_space_bytes, Unset):
            free_space_bytes = UNSET
        else:
            free_space_bytes = self.free_space_bytes

        used_space_bytes: Union[None, Unset, int]
        if isinstance(self.used_space_bytes, Unset):
            used_space_bytes = UNSET
        else:
            used_space_bytes = self.used_space_bytes

        daily_retention_period: Union[None, Unset, int]
        if isinstance(self.daily_retention_period, Unset):
            daily_retention_period = UNSET
        else:
            daily_retention_period = self.daily_retention_period

        monthly_retention_period: Union[None, Unset, int]
        if isinstance(self.monthly_retention_period, Unset):
            monthly_retention_period = UNSET
        else:
            monthly_retention_period = self.monthly_retention_period

        daily_time = self.daily_time

        monthly_time = self.monthly_time

        retention_type: Union[Unset, str] = UNSET
        if not isinstance(self.retention_type, Unset):
            retention_type = self.retention_type.value

        retention_period_type: Union[Unset, str] = UNSET
        if not isinstance(self.retention_period_type, Unset):
            retention_period_type = self.retention_period_type.value

        yearly_retention_period: Union[Unset, str] = UNSET
        if not isinstance(self.yearly_retention_period, Unset):
            yearly_retention_period = self.yearly_retention_period.value

        retention_frequency_type: Union[Unset, str] = UNSET
        if not isinstance(self.retention_frequency_type, Unset):
            retention_frequency_type = self.retention_frequency_type.value

        daily_type: Union[Unset, str] = UNSET
        if not isinstance(self.daily_type, Unset):
            daily_type = self.daily_type.value

        monthly_day_number: Union[Unset, str] = UNSET
        if not isinstance(self.monthly_day_number, Unset):
            monthly_day_number = self.monthly_day_number.value

        monthly_day_of_week: Union[Unset, str] = UNSET
        if not isinstance(self.monthly_day_of_week, Unset):
            monthly_day_of_week = self.monthly_day_of_week.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if instance_uid is not UNSET:
            field_dict["instanceUid"] = instance_uid
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if proxy_uid is not UNSET:
            field_dict["proxyUid"] = proxy_uid
        if proxy_pool_uid is not UNSET:
            field_dict["proxyPoolUid"] = proxy_pool_uid
        if path is not UNSET:
            field_dict["path"] = path
        if is_archive_repository is not UNSET:
            field_dict["isArchiveRepository"] = is_archive_repository
        if is_available_for_backup_job is not UNSET:
            field_dict["isAvailableForBackupJob"] = is_available_for_backup_job
        if is_available_for_copy_job is not UNSET:
            field_dict["isAvailableForCopyJob"] = is_available_for_copy_job
        if is_object_storage_repository is not UNSET:
            field_dict["isObjectStorageRepository"] = is_object_storage_repository
        if object_storage_repository_uid is not UNSET:
            field_dict["objectStorageRepositoryUid"] = object_storage_repository_uid
        if object_storage_repository_cache_path is not UNSET:
            field_dict["objectStorageRepositoryCachePath"] = object_storage_repository_cache_path
        if object_storage_repository_encryption_enabled is not UNSET:
            field_dict["objectStorageRepositoryEncryptionEnabled"] = object_storage_repository_encryption_enabled
        if encryption_key_id is not UNSET:
            field_dict["encryptionKeyId"] = encryption_key_id
        if is_out_of_sync is not UNSET:
            field_dict["isOutOfSync"] = is_out_of_sync
        if capacity_bytes is not UNSET:
            field_dict["capacityBytes"] = capacity_bytes
        if free_space_bytes is not UNSET:
            field_dict["freeSpaceBytes"] = free_space_bytes
        if used_space_bytes is not UNSET:
            field_dict["usedSpaceBytes"] = used_space_bytes
        if daily_retention_period is not UNSET:
            field_dict["dailyRetentionPeriod"] = daily_retention_period
        if monthly_retention_period is not UNSET:
            field_dict["monthlyRetentionPeriod"] = monthly_retention_period
        if daily_time is not UNSET:
            field_dict["dailyTime"] = daily_time
        if monthly_time is not UNSET:
            field_dict["monthlyTime"] = monthly_time
        if retention_type is not UNSET:
            field_dict["retentionType"] = retention_type
        if retention_period_type is not UNSET:
            field_dict["retentionPeriodType"] = retention_period_type
        if yearly_retention_period is not UNSET:
            field_dict["yearlyRetentionPeriod"] = yearly_retention_period
        if retention_frequency_type is not UNSET:
            field_dict["retentionFrequencyType"] = retention_frequency_type
        if daily_type is not UNSET:
            field_dict["dailyType"] = daily_type
        if monthly_day_number is not UNSET:
            field_dict["monthlyDayNumber"] = monthly_day_number
        if monthly_day_of_week is not UNSET:
            field_dict["monthlyDayOfWeek"] = monthly_day_of_week

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _instance_uid = d.pop("instanceUid", UNSET)
        instance_uid: Union[Unset, UUID]
        if isinstance(_instance_uid, Unset):
            instance_uid = UNSET
        else:
            instance_uid = UUID(_instance_uid)

        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        def _parse_proxy_uid(data: object) -> Union[None, UUID, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                proxy_uid_type_0 = UUID(data)

                return proxy_uid_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID, Unset], data)

        proxy_uid = _parse_proxy_uid(d.pop("proxyUid", UNSET))

        def _parse_proxy_pool_uid(data: object) -> Union[None, UUID, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                proxy_pool_uid_type_0 = UUID(data)

                return proxy_pool_uid_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID, Unset], data)

        proxy_pool_uid = _parse_proxy_pool_uid(d.pop("proxyPoolUid", UNSET))

        path = d.pop("path", UNSET)

        is_archive_repository = d.pop("isArchiveRepository", UNSET)

        is_available_for_backup_job = d.pop("isAvailableForBackupJob", UNSET)

        is_available_for_copy_job = d.pop("isAvailableForCopyJob", UNSET)

        is_object_storage_repository = d.pop("isObjectStorageRepository", UNSET)

        def _parse_object_storage_repository_uid(data: object) -> Union[None, UUID, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                object_storage_repository_uid_type_0 = UUID(data)

                return object_storage_repository_uid_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID, Unset], data)

        object_storage_repository_uid = _parse_object_storage_repository_uid(d.pop("objectStorageRepositoryUid", UNSET))

        object_storage_repository_cache_path = d.pop("objectStorageRepositoryCachePath", UNSET)

        def _parse_object_storage_repository_encryption_enabled(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        object_storage_repository_encryption_enabled = _parse_object_storage_repository_encryption_enabled(
            d.pop("objectStorageRepositoryEncryptionEnabled", UNSET)
        )

        def _parse_encryption_key_id(data: object) -> Union[None, UUID, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                encryption_key_id_type_0 = UUID(data)

                return encryption_key_id_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID, Unset], data)

        encryption_key_id = _parse_encryption_key_id(d.pop("encryptionKeyId", UNSET))

        is_out_of_sync = d.pop("isOutOfSync", UNSET)

        def _parse_capacity_bytes(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        capacity_bytes = _parse_capacity_bytes(d.pop("capacityBytes", UNSET))

        def _parse_free_space_bytes(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        free_space_bytes = _parse_free_space_bytes(d.pop("freeSpaceBytes", UNSET))

        def _parse_used_space_bytes(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        used_space_bytes = _parse_used_space_bytes(d.pop("usedSpaceBytes", UNSET))

        def _parse_daily_retention_period(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        daily_retention_period = _parse_daily_retention_period(d.pop("dailyRetentionPeriod", UNSET))

        def _parse_monthly_retention_period(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        monthly_retention_period = _parse_monthly_retention_period(d.pop("monthlyRetentionPeriod", UNSET))

        daily_time = d.pop("dailyTime", UNSET)

        monthly_time = d.pop("monthlyTime", UNSET)

        _retention_type = d.pop("retentionType", UNSET)
        retention_type: Union[Unset, Vb365BackupRepositoryRetentionType]
        if isinstance(_retention_type, Unset):
            retention_type = UNSET
        else:
            retention_type = Vb365BackupRepositoryRetentionType(_retention_type)

        _retention_period_type = d.pop("retentionPeriodType", UNSET)
        retention_period_type: Union[Unset, Vb365BackupRepositoryRetentionPeriodType]
        if isinstance(_retention_period_type, Unset):
            retention_period_type = UNSET
        else:
            retention_period_type = Vb365BackupRepositoryRetentionPeriodType(_retention_period_type)

        _yearly_retention_period = d.pop("yearlyRetentionPeriod", UNSET)
        yearly_retention_period: Union[Unset, Vb365BackupRepositoryYearlyRetentionPeriod]
        if isinstance(_yearly_retention_period, Unset):
            yearly_retention_period = UNSET
        else:
            yearly_retention_period = Vb365BackupRepositoryYearlyRetentionPeriod(_yearly_retention_period)

        _retention_frequency_type = d.pop("retentionFrequencyType", UNSET)
        retention_frequency_type: Union[Unset, Vb365BackupRepositoryRetentionFrequencyType]
        if isinstance(_retention_frequency_type, Unset):
            retention_frequency_type = UNSET
        else:
            retention_frequency_type = Vb365BackupRepositoryRetentionFrequencyType(_retention_frequency_type)

        _daily_type = d.pop("dailyType", UNSET)
        daily_type: Union[Unset, Vb365BackupRepositoryDailyType]
        if isinstance(_daily_type, Unset):
            daily_type = UNSET
        else:
            daily_type = Vb365BackupRepositoryDailyType(_daily_type)

        _monthly_day_number = d.pop("monthlyDayNumber", UNSET)
        monthly_day_number: Union[Unset, Vb365BackupRepositoryMonthlyDayNumber]
        if isinstance(_monthly_day_number, Unset):
            monthly_day_number = UNSET
        else:
            monthly_day_number = Vb365BackupRepositoryMonthlyDayNumber(_monthly_day_number)

        _monthly_day_of_week = d.pop("monthlyDayOfWeek", UNSET)
        monthly_day_of_week: Union[Unset, Vb365BackupRepositoryMonthlyDayOfWeek]
        if isinstance(_monthly_day_of_week, Unset):
            monthly_day_of_week = UNSET
        else:
            monthly_day_of_week = Vb365BackupRepositoryMonthlyDayOfWeek(_monthly_day_of_week)

        vb_365_backup_repository = cls(
            instance_uid=instance_uid,
            name=name,
            description=description,
            proxy_uid=proxy_uid,
            proxy_pool_uid=proxy_pool_uid,
            path=path,
            is_archive_repository=is_archive_repository,
            is_available_for_backup_job=is_available_for_backup_job,
            is_available_for_copy_job=is_available_for_copy_job,
            is_object_storage_repository=is_object_storage_repository,
            object_storage_repository_uid=object_storage_repository_uid,
            object_storage_repository_cache_path=object_storage_repository_cache_path,
            object_storage_repository_encryption_enabled=object_storage_repository_encryption_enabled,
            encryption_key_id=encryption_key_id,
            is_out_of_sync=is_out_of_sync,
            capacity_bytes=capacity_bytes,
            free_space_bytes=free_space_bytes,
            used_space_bytes=used_space_bytes,
            daily_retention_period=daily_retention_period,
            monthly_retention_period=monthly_retention_period,
            daily_time=daily_time,
            monthly_time=monthly_time,
            retention_type=retention_type,
            retention_period_type=retention_period_type,
            yearly_retention_period=yearly_retention_period,
            retention_frequency_type=retention_frequency_type,
            daily_type=daily_type,
            monthly_day_number=monthly_day_number,
            monthly_day_of_week=monthly_day_of_week,
        )

        vb_365_backup_repository.additional_properties = d
        return vb_365_backup_repository

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
