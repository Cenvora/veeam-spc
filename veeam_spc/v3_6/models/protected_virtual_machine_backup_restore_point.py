import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.malware_state import MalwareState
from ..models.protected_virtual_machine_backup_restore_point_gfs_type_item import (
    ProtectedVirtualMachineBackupRestorePointGfsTypeItem,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="ProtectedVirtualMachineBackupRestorePoint")


@_attrs_define
class ProtectedVirtualMachineBackupRestorePoint:
    """
    Attributes:
        instance_uid (Union[Unset, UUID]): UID assigned to a restore point.
        backup_uid (Union[Unset, UUID]): UID assigned to a backup chain.
        virtual_machine_uid (Union[Unset, UUID]): UID assigned to a protected virtual machine.
        backup_server_uid (Union[Unset, UUID]): UID assigned to a Veeam Backup & Replication server.
        file_path (Union[Unset, str]): Path to a backup file location.
        gfs_type (Union[Unset, list[ProtectedVirtualMachineBackupRestorePointGfsTypeItem]]): Array of enabled GFS
            retention types.
        job_uid (Union[Unset, UUID]): UID assigned to a backup job.
        repository_uid (Union[Unset, UUID]): UID assigned to a repository on which the restore point resides.
        size (Union[Unset, int]): Size of a restore point, in bytes. Includes all virtual machines protected by the same
            backup job.
        provisioned_source_size (Union[Unset, int]): Total size of protected virtual machine disks, in bytes.
        used_source_size (Union[Unset, int]): Used space on protected virtual machine disks, in bytes.
        increment_raw_data_size (Union[Unset, int]): Size of backup increment, in bytes.
        cpu_cores (Union[Unset, int]): Number of vCPU cores of a cloud virtual machine.
        memory (Union[Unset, int]): Protected virtual machine memory, in bytes.
        backup_creation_time (Union[Unset, datetime.datetime]): Date and time when backup was created.
        file_creation_time (Union[Unset, datetime.datetime]): Date and time when a restore point was created.
        is_consistent (Union[Unset, bool]): Indicates whether a retore point has successfully passed a health check.
        malware_state (Union[Unset, MalwareState]): Malware status.
        immutable_till (Union[Unset, datetime.datetime]): Date and time when the latest immutable restore point was
            created.
    """

    instance_uid: Union[Unset, UUID] = UNSET
    backup_uid: Union[Unset, UUID] = UNSET
    virtual_machine_uid: Union[Unset, UUID] = UNSET
    backup_server_uid: Union[Unset, UUID] = UNSET
    file_path: Union[Unset, str] = UNSET
    gfs_type: Union[Unset, list[ProtectedVirtualMachineBackupRestorePointGfsTypeItem]] = UNSET
    job_uid: Union[Unset, UUID] = UNSET
    repository_uid: Union[Unset, UUID] = UNSET
    size: Union[Unset, int] = UNSET
    provisioned_source_size: Union[Unset, int] = UNSET
    used_source_size: Union[Unset, int] = UNSET
    increment_raw_data_size: Union[Unset, int] = UNSET
    cpu_cores: Union[Unset, int] = UNSET
    memory: Union[Unset, int] = UNSET
    backup_creation_time: Union[Unset, datetime.datetime] = UNSET
    file_creation_time: Union[Unset, datetime.datetime] = UNSET
    is_consistent: Union[Unset, bool] = UNSET
    malware_state: Union[Unset, MalwareState] = UNSET
    immutable_till: Union[Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        instance_uid: Union[Unset, str] = UNSET
        if not isinstance(self.instance_uid, Unset):
            instance_uid = str(self.instance_uid)

        backup_uid: Union[Unset, str] = UNSET
        if not isinstance(self.backup_uid, Unset):
            backup_uid = str(self.backup_uid)

        virtual_machine_uid: Union[Unset, str] = UNSET
        if not isinstance(self.virtual_machine_uid, Unset):
            virtual_machine_uid = str(self.virtual_machine_uid)

        backup_server_uid: Union[Unset, str] = UNSET
        if not isinstance(self.backup_server_uid, Unset):
            backup_server_uid = str(self.backup_server_uid)

        file_path = self.file_path

        gfs_type: Union[Unset, list[str]] = UNSET
        if not isinstance(self.gfs_type, Unset):
            gfs_type = []
            for gfs_type_item_data in self.gfs_type:
                gfs_type_item = gfs_type_item_data.value
                gfs_type.append(gfs_type_item)

        job_uid: Union[Unset, str] = UNSET
        if not isinstance(self.job_uid, Unset):
            job_uid = str(self.job_uid)

        repository_uid: Union[Unset, str] = UNSET
        if not isinstance(self.repository_uid, Unset):
            repository_uid = str(self.repository_uid)

        size = self.size

        provisioned_source_size = self.provisioned_source_size

        used_source_size = self.used_source_size

        increment_raw_data_size = self.increment_raw_data_size

        cpu_cores = self.cpu_cores

        memory = self.memory

        backup_creation_time: Union[Unset, str] = UNSET
        if not isinstance(self.backup_creation_time, Unset):
            backup_creation_time = self.backup_creation_time.isoformat()

        file_creation_time: Union[Unset, str] = UNSET
        if not isinstance(self.file_creation_time, Unset):
            file_creation_time = self.file_creation_time.isoformat()

        is_consistent = self.is_consistent

        malware_state: Union[Unset, str] = UNSET
        if not isinstance(self.malware_state, Unset):
            malware_state = self.malware_state.value

        immutable_till: Union[Unset, str] = UNSET
        if not isinstance(self.immutable_till, Unset):
            immutable_till = self.immutable_till.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if instance_uid is not UNSET:
            field_dict["instanceUid"] = instance_uid
        if backup_uid is not UNSET:
            field_dict["backupUid"] = backup_uid
        if virtual_machine_uid is not UNSET:
            field_dict["virtualMachineUid"] = virtual_machine_uid
        if backup_server_uid is not UNSET:
            field_dict["backupServerUid"] = backup_server_uid
        if file_path is not UNSET:
            field_dict["filePath"] = file_path
        if gfs_type is not UNSET:
            field_dict["gfsType"] = gfs_type
        if job_uid is not UNSET:
            field_dict["jobUid"] = job_uid
        if repository_uid is not UNSET:
            field_dict["repositoryUid"] = repository_uid
        if size is not UNSET:
            field_dict["size"] = size
        if provisioned_source_size is not UNSET:
            field_dict["provisionedSourceSize"] = provisioned_source_size
        if used_source_size is not UNSET:
            field_dict["usedSourceSize"] = used_source_size
        if increment_raw_data_size is not UNSET:
            field_dict["incrementRawDataSize"] = increment_raw_data_size
        if cpu_cores is not UNSET:
            field_dict["cpuCores"] = cpu_cores
        if memory is not UNSET:
            field_dict["memory"] = memory
        if backup_creation_time is not UNSET:
            field_dict["backupCreationTime"] = backup_creation_time
        if file_creation_time is not UNSET:
            field_dict["fileCreationTime"] = file_creation_time
        if is_consistent is not UNSET:
            field_dict["isConsistent"] = is_consistent
        if malware_state is not UNSET:
            field_dict["malwareState"] = malware_state
        if immutable_till is not UNSET:
            field_dict["immutableTill"] = immutable_till

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

        _backup_uid = d.pop("backupUid", UNSET)
        backup_uid: Union[Unset, UUID]
        if isinstance(_backup_uid, Unset):
            backup_uid = UNSET
        else:
            backup_uid = UUID(_backup_uid)

        _virtual_machine_uid = d.pop("virtualMachineUid", UNSET)
        virtual_machine_uid: Union[Unset, UUID]
        if isinstance(_virtual_machine_uid, Unset):
            virtual_machine_uid = UNSET
        else:
            virtual_machine_uid = UUID(_virtual_machine_uid)

        _backup_server_uid = d.pop("backupServerUid", UNSET)
        backup_server_uid: Union[Unset, UUID]
        if isinstance(_backup_server_uid, Unset):
            backup_server_uid = UNSET
        else:
            backup_server_uid = UUID(_backup_server_uid)

        file_path = d.pop("filePath", UNSET)

        gfs_type = []
        _gfs_type = d.pop("gfsType", UNSET)
        for gfs_type_item_data in _gfs_type or []:
            gfs_type_item = ProtectedVirtualMachineBackupRestorePointGfsTypeItem(gfs_type_item_data)

            gfs_type.append(gfs_type_item)

        _job_uid = d.pop("jobUid", UNSET)
        job_uid: Union[Unset, UUID]
        if isinstance(_job_uid, Unset):
            job_uid = UNSET
        else:
            job_uid = UUID(_job_uid)

        _repository_uid = d.pop("repositoryUid", UNSET)
        repository_uid: Union[Unset, UUID]
        if isinstance(_repository_uid, Unset):
            repository_uid = UNSET
        else:
            repository_uid = UUID(_repository_uid)

        size = d.pop("size", UNSET)

        provisioned_source_size = d.pop("provisionedSourceSize", UNSET)

        used_source_size = d.pop("usedSourceSize", UNSET)

        increment_raw_data_size = d.pop("incrementRawDataSize", UNSET)

        cpu_cores = d.pop("cpuCores", UNSET)

        memory = d.pop("memory", UNSET)

        _backup_creation_time = d.pop("backupCreationTime", UNSET)
        backup_creation_time: Union[Unset, datetime.datetime]
        if isinstance(_backup_creation_time, Unset):
            backup_creation_time = UNSET
        else:
            backup_creation_time = isoparse(_backup_creation_time)

        _file_creation_time = d.pop("fileCreationTime", UNSET)
        file_creation_time: Union[Unset, datetime.datetime]
        if isinstance(_file_creation_time, Unset):
            file_creation_time = UNSET
        else:
            file_creation_time = isoparse(_file_creation_time)

        is_consistent = d.pop("isConsistent", UNSET)

        _malware_state = d.pop("malwareState", UNSET)
        malware_state: Union[Unset, MalwareState]
        if isinstance(_malware_state, Unset):
            malware_state = UNSET
        else:
            malware_state = MalwareState(_malware_state)

        _immutable_till = d.pop("immutableTill", UNSET)
        immutable_till: Union[Unset, datetime.datetime]
        if isinstance(_immutable_till, Unset):
            immutable_till = UNSET
        else:
            immutable_till = isoparse(_immutable_till)

        protected_virtual_machine_backup_restore_point = cls(
            instance_uid=instance_uid,
            backup_uid=backup_uid,
            virtual_machine_uid=virtual_machine_uid,
            backup_server_uid=backup_server_uid,
            file_path=file_path,
            gfs_type=gfs_type,
            job_uid=job_uid,
            repository_uid=repository_uid,
            size=size,
            provisioned_source_size=provisioned_source_size,
            used_source_size=used_source_size,
            increment_raw_data_size=increment_raw_data_size,
            cpu_cores=cpu_cores,
            memory=memory,
            backup_creation_time=backup_creation_time,
            file_creation_time=file_creation_time,
            is_consistent=is_consistent,
            malware_state=malware_state,
            immutable_till=immutable_till,
        )

        protected_virtual_machine_backup_restore_point.additional_properties = d
        return protected_virtual_machine_backup_restore_point

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
