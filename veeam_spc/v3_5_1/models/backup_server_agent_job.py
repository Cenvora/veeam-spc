from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.backup_server_agent_job_job_mode import BackupServerAgentJobJobMode
from ..models.backup_server_agent_job_license_type import BackupServerAgentJobLicenseType
from ..models.backup_server_agent_job_os_type import BackupServerAgentJobOsType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.backup_server_agent_job_source import BackupServerAgentJobSource
    from ..models.embedded_for_backup_server_job_children import EmbeddedForBackupServerJobChildren


T = TypeVar("T", bound="BackupServerAgentJob")


@_attrs_define
class BackupServerAgentJob:
    """
    Attributes:
        instance_uid (Union[Unset, UUID]): UID assigned to a job in Veeam Backup & Replication.
        unique_uid (Union[Unset, UUID]): UID assigned to a job in Veeam Service Provider Console.
        total_jobs_count (Union[Unset, int]): Number of job sessions.
        success_jobs_count (Union[Unset, int]): Number of successful job sessions.
        destination (Union[Unset, str]): Location of backup files.
        source (Union[Unset, BackupServerAgentJobSource]):
        job_mode (Union[Unset, BackupServerAgentJobJobMode]): Status of the latest job session
        os_type (Union[Unset, BackupServerAgentJobOsType]): Type of a protected computer operating system.
        license_type (Union[Unset, BackupServerAgentJobLicenseType]): License type of a backup job.
        field_embedded (Union[Unset, EmbeddedForBackupServerJobChildren]): Resource representation of the related Veeam
            Backup & Replication server job entity.
    """

    instance_uid: Union[Unset, UUID] = UNSET
    unique_uid: Union[Unset, UUID] = UNSET
    total_jobs_count: Union[Unset, int] = UNSET
    success_jobs_count: Union[Unset, int] = UNSET
    destination: Union[Unset, str] = UNSET
    source: Union[Unset, "BackupServerAgentJobSource"] = UNSET
    job_mode: Union[Unset, BackupServerAgentJobJobMode] = UNSET
    os_type: Union[Unset, BackupServerAgentJobOsType] = UNSET
    license_type: Union[Unset, BackupServerAgentJobLicenseType] = UNSET
    field_embedded: Union[Unset, "EmbeddedForBackupServerJobChildren"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        instance_uid: Union[Unset, str] = UNSET
        if not isinstance(self.instance_uid, Unset):
            instance_uid = str(self.instance_uid)

        unique_uid: Union[Unset, str] = UNSET
        if not isinstance(self.unique_uid, Unset):
            unique_uid = str(self.unique_uid)

        total_jobs_count = self.total_jobs_count

        success_jobs_count = self.success_jobs_count

        destination = self.destination

        source: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.source, Unset):
            source = self.source.to_dict()

        job_mode: Union[Unset, str] = UNSET
        if not isinstance(self.job_mode, Unset):
            job_mode = self.job_mode.value

        os_type: Union[Unset, str] = UNSET
        if not isinstance(self.os_type, Unset):
            os_type = self.os_type.value

        license_type: Union[Unset, str] = UNSET
        if not isinstance(self.license_type, Unset):
            license_type = self.license_type.value

        field_embedded: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.field_embedded, Unset):
            field_embedded = self.field_embedded.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if instance_uid is not UNSET:
            field_dict["instanceUid"] = instance_uid
        if unique_uid is not UNSET:
            field_dict["uniqueUid"] = unique_uid
        if total_jobs_count is not UNSET:
            field_dict["totalJobsCount"] = total_jobs_count
        if success_jobs_count is not UNSET:
            field_dict["successJobsCount"] = success_jobs_count
        if destination is not UNSET:
            field_dict["destination"] = destination
        if source is not UNSET:
            field_dict["source"] = source
        if job_mode is not UNSET:
            field_dict["jobMode"] = job_mode
        if os_type is not UNSET:
            field_dict["osType"] = os_type
        if license_type is not UNSET:
            field_dict["licenseType"] = license_type
        if field_embedded is not UNSET:
            field_dict["_embedded"] = field_embedded

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.backup_server_agent_job_source import BackupServerAgentJobSource
        from ..models.embedded_for_backup_server_job_children import EmbeddedForBackupServerJobChildren

        d = dict(src_dict)
        _instance_uid = d.pop("instanceUid", UNSET)
        instance_uid: Union[Unset, UUID]
        if isinstance(_instance_uid, Unset):
            instance_uid = UNSET
        else:
            instance_uid = UUID(_instance_uid)

        _unique_uid = d.pop("uniqueUid", UNSET)
        unique_uid: Union[Unset, UUID]
        if isinstance(_unique_uid, Unset):
            unique_uid = UNSET
        else:
            unique_uid = UUID(_unique_uid)

        total_jobs_count = d.pop("totalJobsCount", UNSET)

        success_jobs_count = d.pop("successJobsCount", UNSET)

        destination = d.pop("destination", UNSET)

        _source = d.pop("source", UNSET)
        source: Union[Unset, BackupServerAgentJobSource]
        if isinstance(_source, Unset):
            source = UNSET
        else:
            source = BackupServerAgentJobSource.from_dict(_source)

        _job_mode = d.pop("jobMode", UNSET)
        job_mode: Union[Unset, BackupServerAgentJobJobMode]
        if isinstance(_job_mode, Unset):
            job_mode = UNSET
        else:
            job_mode = BackupServerAgentJobJobMode(_job_mode)

        _os_type = d.pop("osType", UNSET)
        os_type: Union[Unset, BackupServerAgentJobOsType]
        if isinstance(_os_type, Unset):
            os_type = UNSET
        else:
            os_type = BackupServerAgentJobOsType(_os_type)

        _license_type = d.pop("licenseType", UNSET)
        license_type: Union[Unset, BackupServerAgentJobLicenseType]
        if isinstance(_license_type, Unset):
            license_type = UNSET
        else:
            license_type = BackupServerAgentJobLicenseType(_license_type)

        _field_embedded = d.pop("_embedded", UNSET)
        field_embedded: Union[Unset, EmbeddedForBackupServerJobChildren]
        if isinstance(_field_embedded, Unset):
            field_embedded = UNSET
        else:
            field_embedded = EmbeddedForBackupServerJobChildren.from_dict(_field_embedded)

        backup_server_agent_job = cls(
            instance_uid=instance_uid,
            unique_uid=unique_uid,
            total_jobs_count=total_jobs_count,
            success_jobs_count=success_jobs_count,
            destination=destination,
            source=source,
            job_mode=job_mode,
            os_type=os_type,
            license_type=license_type,
            field_embedded=field_embedded,
        )

        backup_server_agent_job.additional_properties = d
        return backup_server_agent_job

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
