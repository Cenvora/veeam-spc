import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.malware_state import MalwareState
from ..models.protected_virtual_machine_backup_backup_type import ProtectedVirtualMachineBackupBackupType
from ..models.protected_virtual_machine_backup_target_type import ProtectedVirtualMachineBackupTargetType
from ..models.sobr_repository_tier import SobrRepositoryTier
from ..types import UNSET, Unset

T = TypeVar("T", bound="ProtectedVirtualMachineBackup")


@_attrs_define
class ProtectedVirtualMachineBackup:
    """
    Attributes:
        instance_uid (Union[Unset, UUID]): UID assigned to a backup chain.
        virtual_machine_uid (Union[Unset, UUID]): UID assigned to a virtual machine.
        job_uid (Union[Unset, UUID]): UID assigned to a backup job in Veeam Backup & Replication.
        backup_server_uid (Union[Unset, UUID]): UID assigned to a Veeam Backup & Replication server.
        backup_type (Union[Unset, ProtectedVirtualMachineBackupBackupType]): Backup job type.
        repository_uid (Union[Unset, UUID]): UID assigned to a repository on which the restore point resides.
        total_restore_point_size (Union[Unset, int]): Total size of all restore points, in bytes.
        latest_restore_point_size (Union[Unset, int]): Size of the latest restore point, in bytes.
        restore_points (Union[Unset, int]): Number of restore points.
        latest_restore_point_date (Union[Unset, datetime.datetime]): Date and time of the latest restore point creation.
        target_type (Union[Unset, ProtectedVirtualMachineBackupTargetType]): Type of a target repository.
        malware_state (Union[Unset, MalwareState]): Malware status.
        target_location_tier (Union[Unset, SobrRepositoryTier]): Tier of a target repository in case it is an extent of
            a scale-out backup repository.
            > For individual repositories, the value is `None`.
    """

    instance_uid: Union[Unset, UUID] = UNSET
    virtual_machine_uid: Union[Unset, UUID] = UNSET
    job_uid: Union[Unset, UUID] = UNSET
    backup_server_uid: Union[Unset, UUID] = UNSET
    backup_type: Union[Unset, ProtectedVirtualMachineBackupBackupType] = UNSET
    repository_uid: Union[Unset, UUID] = UNSET
    total_restore_point_size: Union[Unset, int] = UNSET
    latest_restore_point_size: Union[Unset, int] = UNSET
    restore_points: Union[Unset, int] = UNSET
    latest_restore_point_date: Union[Unset, datetime.datetime] = UNSET
    target_type: Union[Unset, ProtectedVirtualMachineBackupTargetType] = UNSET
    malware_state: Union[Unset, MalwareState] = UNSET
    target_location_tier: Union[Unset, SobrRepositoryTier] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        instance_uid: Union[Unset, str] = UNSET
        if not isinstance(self.instance_uid, Unset):
            instance_uid = str(self.instance_uid)

        virtual_machine_uid: Union[Unset, str] = UNSET
        if not isinstance(self.virtual_machine_uid, Unset):
            virtual_machine_uid = str(self.virtual_machine_uid)

        job_uid: Union[Unset, str] = UNSET
        if not isinstance(self.job_uid, Unset):
            job_uid = str(self.job_uid)

        backup_server_uid: Union[Unset, str] = UNSET
        if not isinstance(self.backup_server_uid, Unset):
            backup_server_uid = str(self.backup_server_uid)

        backup_type: Union[Unset, str] = UNSET
        if not isinstance(self.backup_type, Unset):
            backup_type = self.backup_type.value

        repository_uid: Union[Unset, str] = UNSET
        if not isinstance(self.repository_uid, Unset):
            repository_uid = str(self.repository_uid)

        total_restore_point_size = self.total_restore_point_size

        latest_restore_point_size = self.latest_restore_point_size

        restore_points = self.restore_points

        latest_restore_point_date: Union[Unset, str] = UNSET
        if not isinstance(self.latest_restore_point_date, Unset):
            latest_restore_point_date = self.latest_restore_point_date.isoformat()

        target_type: Union[Unset, str] = UNSET
        if not isinstance(self.target_type, Unset):
            target_type = self.target_type.value

        malware_state: Union[Unset, str] = UNSET
        if not isinstance(self.malware_state, Unset):
            malware_state = self.malware_state.value

        target_location_tier: Union[Unset, str] = UNSET
        if not isinstance(self.target_location_tier, Unset):
            target_location_tier = self.target_location_tier.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if instance_uid is not UNSET:
            field_dict["instanceUid"] = instance_uid
        if virtual_machine_uid is not UNSET:
            field_dict["virtualMachineUid"] = virtual_machine_uid
        if job_uid is not UNSET:
            field_dict["jobUid"] = job_uid
        if backup_server_uid is not UNSET:
            field_dict["backupServerUid"] = backup_server_uid
        if backup_type is not UNSET:
            field_dict["backupType"] = backup_type
        if repository_uid is not UNSET:
            field_dict["repositoryUid"] = repository_uid
        if total_restore_point_size is not UNSET:
            field_dict["totalRestorePointSize"] = total_restore_point_size
        if latest_restore_point_size is not UNSET:
            field_dict["latestRestorePointSize"] = latest_restore_point_size
        if restore_points is not UNSET:
            field_dict["restorePoints"] = restore_points
        if latest_restore_point_date is not UNSET:
            field_dict["latestRestorePointDate"] = latest_restore_point_date
        if target_type is not UNSET:
            field_dict["targetType"] = target_type
        if malware_state is not UNSET:
            field_dict["malwareState"] = malware_state
        if target_location_tier is not UNSET:
            field_dict["targetLocationTier"] = target_location_tier

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

        _virtual_machine_uid = d.pop("virtualMachineUid", UNSET)
        virtual_machine_uid: Union[Unset, UUID]
        if isinstance(_virtual_machine_uid, Unset):
            virtual_machine_uid = UNSET
        else:
            virtual_machine_uid = UUID(_virtual_machine_uid)

        _job_uid = d.pop("jobUid", UNSET)
        job_uid: Union[Unset, UUID]
        if isinstance(_job_uid, Unset):
            job_uid = UNSET
        else:
            job_uid = UUID(_job_uid)

        _backup_server_uid = d.pop("backupServerUid", UNSET)
        backup_server_uid: Union[Unset, UUID]
        if isinstance(_backup_server_uid, Unset):
            backup_server_uid = UNSET
        else:
            backup_server_uid = UUID(_backup_server_uid)

        _backup_type = d.pop("backupType", UNSET)
        backup_type: Union[Unset, ProtectedVirtualMachineBackupBackupType]
        if isinstance(_backup_type, Unset):
            backup_type = UNSET
        else:
            backup_type = ProtectedVirtualMachineBackupBackupType(_backup_type)

        _repository_uid = d.pop("repositoryUid", UNSET)
        repository_uid: Union[Unset, UUID]
        if isinstance(_repository_uid, Unset):
            repository_uid = UNSET
        else:
            repository_uid = UUID(_repository_uid)

        total_restore_point_size = d.pop("totalRestorePointSize", UNSET)

        latest_restore_point_size = d.pop("latestRestorePointSize", UNSET)

        restore_points = d.pop("restorePoints", UNSET)

        _latest_restore_point_date = d.pop("latestRestorePointDate", UNSET)
        latest_restore_point_date: Union[Unset, datetime.datetime]
        if isinstance(_latest_restore_point_date, Unset):
            latest_restore_point_date = UNSET
        else:
            latest_restore_point_date = isoparse(_latest_restore_point_date)

        _target_type = d.pop("targetType", UNSET)
        target_type: Union[Unset, ProtectedVirtualMachineBackupTargetType]
        if isinstance(_target_type, Unset):
            target_type = UNSET
        else:
            target_type = ProtectedVirtualMachineBackupTargetType(_target_type)

        _malware_state = d.pop("malwareState", UNSET)
        malware_state: Union[Unset, MalwareState]
        if isinstance(_malware_state, Unset):
            malware_state = UNSET
        else:
            malware_state = MalwareState(_malware_state)

        _target_location_tier = d.pop("targetLocationTier", UNSET)
        target_location_tier: Union[Unset, SobrRepositoryTier]
        if isinstance(_target_location_tier, Unset):
            target_location_tier = UNSET
        else:
            target_location_tier = SobrRepositoryTier(_target_location_tier)

        protected_virtual_machine_backup = cls(
            instance_uid=instance_uid,
            virtual_machine_uid=virtual_machine_uid,
            job_uid=job_uid,
            backup_server_uid=backup_server_uid,
            backup_type=backup_type,
            repository_uid=repository_uid,
            total_restore_point_size=total_restore_point_size,
            latest_restore_point_size=latest_restore_point_size,
            restore_points=restore_points,
            latest_restore_point_date=latest_restore_point_date,
            target_type=target_type,
            malware_state=malware_state,
            target_location_tier=target_location_tier,
        )

        protected_virtual_machine_backup.additional_properties = d
        return protected_virtual_machine_backup

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
