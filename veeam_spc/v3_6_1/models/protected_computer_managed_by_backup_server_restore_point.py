import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.malware_state import MalwareState
from ..models.protected_computer_managed_by_backup_server_restore_point_target_type import (
    ProtectedComputerManagedByBackupServerRestorePointTargetType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="ProtectedComputerManagedByBackupServerRestorePoint")


@_attrs_define
class ProtectedComputerManagedByBackupServerRestorePoint:
    """
    Attributes:
        instance_uid (Union[Unset, UUID]): UID assigned to a restore point.
        backup_agent_uid (Union[Unset, UUID]): UID assigned to a Veeam backup agent.
        backup_uid (Union[Unset, UUID]): UID assigned to a backup chain.
        job_uid (Union[None, UUID, Unset]): UID assigned to a backup job that created the restore point.
        repository_uid (Union[Unset, UUID]): UID assigned to a target repository
        size (Union[Unset, int]): Size of the restore point, in bytes.
        provisioned_source_size (Union[Unset, int]): Total size of protected computer disks, in bytes.
        used_source_size (Union[None, Unset, int]): Used space on protected computer disks, in bytes.
        increment_raw_data_size (Union[Unset, int]): Size of the backup increment, in bytes.
        source_size (Union[Unset, int]): Size of protected data, in bytes.
        cpu_cores (Union[Unset, int]): Number of protected computer CPU cores.
        memory (Union[Unset, int]): Protected computer memory, in bytes.
        target_type (Union[Unset, ProtectedComputerManagedByBackupServerRestorePointTargetType]): Type of a target
            repository.
        backup_creation_time (Union[None, Unset, datetime.datetime]): Date and time when backup was created.
        file_creation_time (Union[None, Unset, datetime.datetime]): Date and time when a restore point was created.
        malware_state (Union[Unset, MalwareState]): Malware status.
    """

    instance_uid: Union[Unset, UUID] = UNSET
    backup_agent_uid: Union[Unset, UUID] = UNSET
    backup_uid: Union[Unset, UUID] = UNSET
    job_uid: Union[None, UUID, Unset] = UNSET
    repository_uid: Union[Unset, UUID] = UNSET
    size: Union[Unset, int] = UNSET
    provisioned_source_size: Union[Unset, int] = UNSET
    used_source_size: Union[None, Unset, int] = UNSET
    increment_raw_data_size: Union[Unset, int] = UNSET
    source_size: Union[Unset, int] = UNSET
    cpu_cores: Union[Unset, int] = UNSET
    memory: Union[Unset, int] = UNSET
    target_type: Union[Unset, ProtectedComputerManagedByBackupServerRestorePointTargetType] = UNSET
    backup_creation_time: Union[None, Unset, datetime.datetime] = UNSET
    file_creation_time: Union[None, Unset, datetime.datetime] = UNSET
    malware_state: Union[Unset, MalwareState] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        instance_uid: Union[Unset, str] = UNSET
        if not isinstance(self.instance_uid, Unset):
            instance_uid = str(self.instance_uid)

        backup_agent_uid: Union[Unset, str] = UNSET
        if not isinstance(self.backup_agent_uid, Unset):
            backup_agent_uid = str(self.backup_agent_uid)

        backup_uid: Union[Unset, str] = UNSET
        if not isinstance(self.backup_uid, Unset):
            backup_uid = str(self.backup_uid)

        job_uid: Union[None, Unset, str]
        if isinstance(self.job_uid, Unset):
            job_uid = UNSET
        elif isinstance(self.job_uid, UUID):
            job_uid = str(self.job_uid)
        else:
            job_uid = self.job_uid

        repository_uid: Union[Unset, str] = UNSET
        if not isinstance(self.repository_uid, Unset):
            repository_uid = str(self.repository_uid)

        size = self.size

        provisioned_source_size = self.provisioned_source_size

        used_source_size: Union[None, Unset, int]
        if isinstance(self.used_source_size, Unset):
            used_source_size = UNSET
        else:
            used_source_size = self.used_source_size

        increment_raw_data_size = self.increment_raw_data_size

        source_size = self.source_size

        cpu_cores = self.cpu_cores

        memory = self.memory

        target_type: Union[Unset, str] = UNSET
        if not isinstance(self.target_type, Unset):
            target_type = self.target_type.value

        backup_creation_time: Union[None, Unset, str]
        if isinstance(self.backup_creation_time, Unset):
            backup_creation_time = UNSET
        elif isinstance(self.backup_creation_time, datetime.datetime):
            backup_creation_time = self.backup_creation_time.isoformat()
        else:
            backup_creation_time = self.backup_creation_time

        file_creation_time: Union[None, Unset, str]
        if isinstance(self.file_creation_time, Unset):
            file_creation_time = UNSET
        elif isinstance(self.file_creation_time, datetime.datetime):
            file_creation_time = self.file_creation_time.isoformat()
        else:
            file_creation_time = self.file_creation_time

        malware_state: Union[Unset, str] = UNSET
        if not isinstance(self.malware_state, Unset):
            malware_state = self.malware_state.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if instance_uid is not UNSET:
            field_dict["instanceUid"] = instance_uid
        if backup_agent_uid is not UNSET:
            field_dict["backupAgentUid"] = backup_agent_uid
        if backup_uid is not UNSET:
            field_dict["backupUid"] = backup_uid
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
        if source_size is not UNSET:
            field_dict["sourceSize"] = source_size
        if cpu_cores is not UNSET:
            field_dict["cpuCores"] = cpu_cores
        if memory is not UNSET:
            field_dict["memory"] = memory
        if target_type is not UNSET:
            field_dict["targetType"] = target_type
        if backup_creation_time is not UNSET:
            field_dict["backupCreationTime"] = backup_creation_time
        if file_creation_time is not UNSET:
            field_dict["fileCreationTime"] = file_creation_time
        if malware_state is not UNSET:
            field_dict["malwareState"] = malware_state

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

        _backup_agent_uid = d.pop("backupAgentUid", UNSET)
        backup_agent_uid: Union[Unset, UUID]
        if isinstance(_backup_agent_uid, Unset):
            backup_agent_uid = UNSET
        else:
            backup_agent_uid = UUID(_backup_agent_uid)

        _backup_uid = d.pop("backupUid", UNSET)
        backup_uid: Union[Unset, UUID]
        if isinstance(_backup_uid, Unset):
            backup_uid = UNSET
        else:
            backup_uid = UUID(_backup_uid)

        def _parse_job_uid(data: object) -> Union[None, UUID, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                job_uid_type_0 = UUID(data)

                return job_uid_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID, Unset], data)

        job_uid = _parse_job_uid(d.pop("jobUid", UNSET))

        _repository_uid = d.pop("repositoryUid", UNSET)
        repository_uid: Union[Unset, UUID]
        if isinstance(_repository_uid, Unset):
            repository_uid = UNSET
        else:
            repository_uid = UUID(_repository_uid)

        size = d.pop("size", UNSET)

        provisioned_source_size = d.pop("provisionedSourceSize", UNSET)

        def _parse_used_source_size(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        used_source_size = _parse_used_source_size(d.pop("usedSourceSize", UNSET))

        increment_raw_data_size = d.pop("incrementRawDataSize", UNSET)

        source_size = d.pop("sourceSize", UNSET)

        cpu_cores = d.pop("cpuCores", UNSET)

        memory = d.pop("memory", UNSET)

        _target_type = d.pop("targetType", UNSET)
        target_type: Union[Unset, ProtectedComputerManagedByBackupServerRestorePointTargetType]
        if isinstance(_target_type, Unset):
            target_type = UNSET
        else:
            target_type = ProtectedComputerManagedByBackupServerRestorePointTargetType(_target_type)

        def _parse_backup_creation_time(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                backup_creation_time_type_0 = isoparse(data)

                return backup_creation_time_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        backup_creation_time = _parse_backup_creation_time(d.pop("backupCreationTime", UNSET))

        def _parse_file_creation_time(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                file_creation_time_type_0 = isoparse(data)

                return file_creation_time_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        file_creation_time = _parse_file_creation_time(d.pop("fileCreationTime", UNSET))

        _malware_state = d.pop("malwareState", UNSET)
        malware_state: Union[Unset, MalwareState]
        if isinstance(_malware_state, Unset):
            malware_state = UNSET
        else:
            malware_state = MalwareState(_malware_state)

        protected_computer_managed_by_backup_server_restore_point = cls(
            instance_uid=instance_uid,
            backup_agent_uid=backup_agent_uid,
            backup_uid=backup_uid,
            job_uid=job_uid,
            repository_uid=repository_uid,
            size=size,
            provisioned_source_size=provisioned_source_size,
            used_source_size=used_source_size,
            increment_raw_data_size=increment_raw_data_size,
            source_size=source_size,
            cpu_cores=cpu_cores,
            memory=memory,
            target_type=target_type,
            backup_creation_time=backup_creation_time,
            file_creation_time=file_creation_time,
            malware_state=malware_state,
        )

        protected_computer_managed_by_backup_server_restore_point.additional_properties = d
        return protected_computer_managed_by_backup_server_restore_point

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
