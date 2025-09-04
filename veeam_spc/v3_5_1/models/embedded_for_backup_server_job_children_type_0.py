from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.backup_server_job import BackupServerJob


T = TypeVar("T", bound="EmbeddedForBackupServerJobChildrenType0")


@_attrs_define
class EmbeddedForBackupServerJobChildrenType0:
    """Resource representation of the related Veeam Backup & Replication server job entity.

    Attributes:
        backup_server_job (Union[Unset, BackupServerJob]):  Example: {'instanceUid': 'EDEB5975-B409-49B5-8ECE-
            FFFECB13494F', 'name': 'Web server Backup to Cloud', 'backupServerUid': 'DF997BD3-4AE9-4841-8152-8FF5CC703EAB',
            'status': 'Success', 'type': 'BackupVm', 'lastRun': datetime.datetime(2016, 11, 1, 18, 35, 28,
            tzinfo=datetime.timezone(datetime.timedelta(seconds=3600), '+01:00')), 'endTime': datetime.datetime(2016, 11, 1,
            18, 40, 56, tzinfo=datetime.timezone(datetime.timedelta(seconds=3600), '+01:00')), 'duration': 328,
            'processingRate': 17, 'avgDuration': 328, 'transferredData': 1052, 'bottleneck': 'Source', 'isEnabled': True,
            'scheduleType': 'Periodically', 'retentionLimit': 14, 'retentionLimitType': 'RestorePoints',
            'isGfsOptionEnabled': True}.
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

        embedded_for_backup_server_job_children_type_0 = cls(
            backup_server_job=backup_server_job,
        )

        embedded_for_backup_server_job_children_type_0.additional_properties = d
        return embedded_for_backup_server_job_children_type_0

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
