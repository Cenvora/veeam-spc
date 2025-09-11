from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.backup_server_job import BackupServerJob


T = TypeVar("T", bound="EmbeddedForBackupServerJobChildren")


@_attrs_define
class EmbeddedForBackupServerJobChildren:
    """Resource representation of the related Veeam Backup & Replication server job entity.

    Attributes:
        backup_server_job (Union[Unset, BackupServerJob]):  Example: {'instanceUid': 'EDEB5975-B409-49B5-8ECE-
            FFFECB13494F', 'name': 'Web server Backup to Cloud', 'backupServerUid': 'DF997BD3-4AE9-4841-8152-8FF5CC703EAB',
            'status': 'Success', 'type': 'BackupVm', 'lastRun': '2016-11-01T10:35:28.0000000-07:00', 'endTime':
            '2016-11-01T10:40:56.0000000-07:00', 'duration': 328, 'processingRate': 17, 'avgDuration': 328,
            'transferredData': 1052, 'bottleneck': 'Source', 'isEnabled': True, 'scheduleType': 'Periodically',
            'retentionLimit': 14, 'retentionLimitType': 'RestorePoints', 'isGfsOptionEnabled': True}.
    """

    backup_server_job: Union[Unset, "BackupServerJob"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        backup_server_job: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.backup_server_job, Unset):
            backup_server_job = self.backup_server_job.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if backup_server_job is not UNSET:
            field_dict["backupServerJob"] = backup_server_job

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.backup_server_job import BackupServerJob

        d = dict(src_dict)
        _backup_server_job = d.pop("backupServerJob", UNSET)
        backup_server_job: Union[Unset, BackupServerJob]
        if isinstance(_backup_server_job, Unset):
            backup_server_job = UNSET
        else:
            backup_server_job = BackupServerJob.from_dict(_backup_server_job)

        embedded_for_backup_server_job_children = cls(
            backup_server_job=backup_server_job,
        )

        embedded_for_backup_server_job_children.additional_properties = d
        return embedded_for_backup_server_job_children

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
