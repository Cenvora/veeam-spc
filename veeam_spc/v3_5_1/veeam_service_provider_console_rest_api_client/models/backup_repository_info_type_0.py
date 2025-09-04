from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.backup_repository_info_type_0_status import BackupRepositoryInfoType0Status
from ..models.backup_repository_info_type_0_type import BackupRepositoryInfoType0Type
from ..types import UNSET, Unset

T = TypeVar("T", bound="BackupRepositoryInfoType0")


@_attrs_define
class BackupRepositoryInfoType0:
    """
    Attributes:
        parent_repository_uid (Union[None, UUID, Unset]): UID assigned to a scale-out backup repository which includes
            the backup repository as an extent.
        per_vm_backup_files (Union[None, Unset, bool]): Indicates whether the per-VM backup job option is enabled in the
            backup repository settings. VM backup files option in the repository settings is enabled. Displays if the per-VM
            backup job option is enabled or not in the backup repository settings.
        capacity (Union[None, Unset, int]): Total disk space of backup repository, in bytes.
        is_capacity_available (Union[Unset, bool]): Indicates whether information about total disk space is available.
        free_space (Union[None, Unset, int]): Free disk space of a backup repository, in bytes.
        is_free_space_available (Union[Unset, bool]): Indicates whether a backup repository has free space.
        used_space (Union[None, Unset, int]): Amount of used space on a backup repository, in bytes.
        is_used_space_available (Union[Unset, bool]): Indicates whether information about used space is available.
        backup_size (Union[None, Unset, int]): Total size of all restore points, in bytes.
        is_immutability_enabled (Union[None, Unset, bool]): Indicates whether immutability is enabled.
        immutability_interval (Union[None, Unset, int]): Duration of an immutability period, in seconds.
        type_ (Union[Unset, BackupRepositoryInfoType0Type]): Type of a backup repository.
        cloud_repository_uid (Union[None, UUID, Unset]): UID assigned to a backup repository if it is used as a cloud
            repository.
        path (Union[Unset, str]): Path to the folder where backup files are stored.
        host_name (Union[Unset, str]): Name of a computer that performs a role of a backup repository.
        host_uid (Union[None, UUID, Unset]): UID assigned to a computer that performs a role of a backup repository.
        is_out_of_date (Union[Unset, bool]): Indicates whether a backup repository service is outdated.
        status (Union[Unset, BackupRepositoryInfoType0Status]): Status of a backup repository.
        is_cloud (Union[Unset, bool]): Indicates whether a backup repository is used as a cloud repository.
    """

    parent_repository_uid: Union[None, UUID, Unset] = UNSET
    per_vm_backup_files: Union[None, Unset, bool] = UNSET
    capacity: Union[None, Unset, int] = UNSET
    is_capacity_available: Union[Unset, bool] = UNSET
    free_space: Union[None, Unset, int] = UNSET
    is_free_space_available: Union[Unset, bool] = UNSET
    used_space: Union[None, Unset, int] = UNSET
    is_used_space_available: Union[Unset, bool] = UNSET
    backup_size: Union[None, Unset, int] = UNSET
    is_immutability_enabled: Union[None, Unset, bool] = UNSET
    immutability_interval: Union[None, Unset, int] = UNSET
    type_: Union[Unset, BackupRepositoryInfoType0Type] = UNSET
    cloud_repository_uid: Union[None, UUID, Unset] = UNSET
    path: Union[Unset, str] = UNSET
    host_name: Union[Unset, str] = UNSET
    host_uid: Union[None, UUID, Unset] = UNSET
    is_out_of_date: Union[Unset, bool] = UNSET
    status: Union[Unset, BackupRepositoryInfoType0Status] = UNSET
    is_cloud: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        parent_repository_uid: Union[None, Unset, str]
        if isinstance(self.parent_repository_uid, Unset):
            parent_repository_uid = UNSET
        elif isinstance(self.parent_repository_uid, UUID):
            parent_repository_uid = str(self.parent_repository_uid)
        else:
            parent_repository_uid = self.parent_repository_uid

        per_vm_backup_files: Union[None, Unset, bool]
        if isinstance(self.per_vm_backup_files, Unset):
            per_vm_backup_files = UNSET
        else:
            per_vm_backup_files = self.per_vm_backup_files

        capacity: Union[None, Unset, int]
        if isinstance(self.capacity, Unset):
            capacity = UNSET
        else:
            capacity = self.capacity

        is_capacity_available = self.is_capacity_available

        free_space: Union[None, Unset, int]
        if isinstance(self.free_space, Unset):
            free_space = UNSET
        else:
            free_space = self.free_space

        is_free_space_available = self.is_free_space_available

        used_space: Union[None, Unset, int]
        if isinstance(self.used_space, Unset):
            used_space = UNSET
        else:
            used_space = self.used_space

        is_used_space_available = self.is_used_space_available

        backup_size: Union[None, Unset, int]
        if isinstance(self.backup_size, Unset):
            backup_size = UNSET
        else:
            backup_size = self.backup_size

        is_immutability_enabled: Union[None, Unset, bool]
        if isinstance(self.is_immutability_enabled, Unset):
            is_immutability_enabled = UNSET
        else:
            is_immutability_enabled = self.is_immutability_enabled

        immutability_interval: Union[None, Unset, int]
        if isinstance(self.immutability_interval, Unset):
            immutability_interval = UNSET
        else:
            immutability_interval = self.immutability_interval

        type_: Union[Unset, str] = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        cloud_repository_uid: Union[None, Unset, str]
        if isinstance(self.cloud_repository_uid, Unset):
            cloud_repository_uid = UNSET
        elif isinstance(self.cloud_repository_uid, UUID):
            cloud_repository_uid = str(self.cloud_repository_uid)
        else:
            cloud_repository_uid = self.cloud_repository_uid

        path = self.path

        host_name = self.host_name

        host_uid: Union[None, Unset, str]
        if isinstance(self.host_uid, Unset):
            host_uid = UNSET
        elif isinstance(self.host_uid, UUID):
            host_uid = str(self.host_uid)
        else:
            host_uid = self.host_uid

        is_out_of_date = self.is_out_of_date

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        is_cloud = self.is_cloud

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if parent_repository_uid is not UNSET:
            field_dict["parentRepositoryUid"] = parent_repository_uid
        if per_vm_backup_files is not UNSET:
            field_dict["perVMBackupFiles"] = per_vm_backup_files
        if capacity is not UNSET:
            field_dict["capacity"] = capacity
        if is_capacity_available is not UNSET:
            field_dict["isCapacityAvailable"] = is_capacity_available
        if free_space is not UNSET:
            field_dict["freeSpace"] = free_space
        if is_free_space_available is not UNSET:
            field_dict["isFreeSpaceAvailable"] = is_free_space_available
        if used_space is not UNSET:
            field_dict["usedSpace"] = used_space
        if is_used_space_available is not UNSET:
            field_dict["isUsedSpaceAvailable"] = is_used_space_available
        if backup_size is not UNSET:
            field_dict["backupSize"] = backup_size
        if is_immutability_enabled is not UNSET:
            field_dict["isImmutabilityEnabled"] = is_immutability_enabled
        if immutability_interval is not UNSET:
            field_dict["immutabilityInterval"] = immutability_interval
        if type_ is not UNSET:
            field_dict["type"] = type_
        if cloud_repository_uid is not UNSET:
            field_dict["cloudRepositoryUid"] = cloud_repository_uid
        if path is not UNSET:
            field_dict["path"] = path
        if host_name is not UNSET:
            field_dict["hostName"] = host_name
        if host_uid is not UNSET:
            field_dict["hostUid"] = host_uid
        if is_out_of_date is not UNSET:
            field_dict["isOutOfDate"] = is_out_of_date
        if status is not UNSET:
            field_dict["status"] = status
        if is_cloud is not UNSET:
            field_dict["isCloud"] = is_cloud

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_parent_repository_uid(data: object) -> Union[None, UUID, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                parent_repository_uid_type_0 = UUID(data)

                return parent_repository_uid_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID, Unset], data)

        parent_repository_uid = _parse_parent_repository_uid(d.pop("parentRepositoryUid", UNSET))

        def _parse_per_vm_backup_files(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        per_vm_backup_files = _parse_per_vm_backup_files(d.pop("perVMBackupFiles", UNSET))

        def _parse_capacity(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        capacity = _parse_capacity(d.pop("capacity", UNSET))

        is_capacity_available = d.pop("isCapacityAvailable", UNSET)

        def _parse_free_space(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        free_space = _parse_free_space(d.pop("freeSpace", UNSET))

        is_free_space_available = d.pop("isFreeSpaceAvailable", UNSET)

        def _parse_used_space(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        used_space = _parse_used_space(d.pop("usedSpace", UNSET))

        is_used_space_available = d.pop("isUsedSpaceAvailable", UNSET)

        def _parse_backup_size(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        backup_size = _parse_backup_size(d.pop("backupSize", UNSET))

        def _parse_is_immutability_enabled(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        is_immutability_enabled = _parse_is_immutability_enabled(d.pop("isImmutabilityEnabled", UNSET))

        def _parse_immutability_interval(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        immutability_interval = _parse_immutability_interval(d.pop("immutabilityInterval", UNSET))

        _type_ = d.pop("type", UNSET)
        type_: Union[Unset, BackupRepositoryInfoType0Type]
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = BackupRepositoryInfoType0Type(_type_)

        def _parse_cloud_repository_uid(data: object) -> Union[None, UUID, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                cloud_repository_uid_type_0 = UUID(data)

                return cloud_repository_uid_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID, Unset], data)

        cloud_repository_uid = _parse_cloud_repository_uid(d.pop("cloudRepositoryUid", UNSET))

        path = d.pop("path", UNSET)

        host_name = d.pop("hostName", UNSET)

        def _parse_host_uid(data: object) -> Union[None, UUID, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                host_uid_type_0 = UUID(data)

                return host_uid_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID, Unset], data)

        host_uid = _parse_host_uid(d.pop("hostUid", UNSET))

        is_out_of_date = d.pop("isOutOfDate", UNSET)

        _status = d.pop("status", UNSET)
        status: Union[Unset, BackupRepositoryInfoType0Status]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = BackupRepositoryInfoType0Status(_status)

        is_cloud = d.pop("isCloud", UNSET)

        backup_repository_info_type_0 = cls(
            parent_repository_uid=parent_repository_uid,
            per_vm_backup_files=per_vm_backup_files,
            capacity=capacity,
            is_capacity_available=is_capacity_available,
            free_space=free_space,
            is_free_space_available=is_free_space_available,
            used_space=used_space,
            is_used_space_available=is_used_space_available,
            backup_size=backup_size,
            is_immutability_enabled=is_immutability_enabled,
            immutability_interval=immutability_interval,
            type_=type_,
            cloud_repository_uid=cloud_repository_uid,
            path=path,
            host_name=host_name,
            host_uid=host_uid,
            is_out_of_date=is_out_of_date,
            status=status,
            is_cloud=is_cloud,
        )

        backup_repository_info_type_0.additional_properties = d
        return backup_repository_info_type_0

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
