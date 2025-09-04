from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.backup_job_operation_mode import BackupJobOperationMode
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.windows_backup_job_configuration import WindowsBackupJobConfiguration


T = TypeVar("T", bound="WindowsBackupPolicy")


@_attrs_define
class WindowsBackupPolicy:
    """
    Attributes:
        operation_mode (BackupJobOperationMode): Backup job operation mode.
        job_configuration (WindowsBackupJobConfiguration):
        instance_uid (Union[Unset, UUID]): UID assigned to a backup policy template.
        create_subtenants (Union[Unset, bool]): Indicates whether a subtenant must be created for each Veeam Agent for
            Microsoft Windows. Default: True.
        create_sub_folders (Union[Unset, bool]): Indicates whether a subfolder must be created for each Veeam backup
            agent on the shared folder. Default: False.
        unlimited_subtenant_quota (Union[Unset, bool]): Indicates whether a subtenant can consume unlimited amount of
            space on a repository. Default: False.
        repository_quota_gb (Union[None, Unset, int]): Maximum amount of space that a subtenant can consume on a
            repository.
            > If a subtenant can consume unlimited amount of space, the value of this property is ignored.
             Default: 100.
    """

    operation_mode: BackupJobOperationMode
    job_configuration: "WindowsBackupJobConfiguration"
    instance_uid: Union[Unset, UUID] = UNSET
    create_subtenants: Union[Unset, bool] = True
    create_sub_folders: Union[Unset, bool] = False
    unlimited_subtenant_quota: Union[Unset, bool] = False
    repository_quota_gb: Union[None, Unset, int] = 100
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        operation_mode = self.operation_mode.value

        job_configuration = self.job_configuration.to_dict()

        instance_uid: Union[Unset, str] = UNSET
        if not isinstance(self.instance_uid, Unset):
            instance_uid = str(self.instance_uid)

        create_subtenants = self.create_subtenants

        create_sub_folders = self.create_sub_folders

        unlimited_subtenant_quota = self.unlimited_subtenant_quota

        repository_quota_gb: Union[None, Unset, int]
        if isinstance(self.repository_quota_gb, Unset):
            repository_quota_gb = UNSET
        else:
            repository_quota_gb = self.repository_quota_gb

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "operationMode": operation_mode,
                "jobConfiguration": job_configuration,
            }
        )
        if instance_uid is not UNSET:
            field_dict["instanceUid"] = instance_uid
        if create_subtenants is not UNSET:
            field_dict["createSubtenants"] = create_subtenants
        if create_sub_folders is not UNSET:
            field_dict["createSubFolders"] = create_sub_folders
        if unlimited_subtenant_quota is not UNSET:
            field_dict["unlimitedSubtenantQuota"] = unlimited_subtenant_quota
        if repository_quota_gb is not UNSET:
            field_dict["repositoryQuotaGb"] = repository_quota_gb

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.windows_backup_job_configuration import WindowsBackupJobConfiguration

        d = dict(src_dict)
        operation_mode = BackupJobOperationMode(d.pop("operationMode"))

        job_configuration = WindowsBackupJobConfiguration.from_dict(d.pop("jobConfiguration"))

        _instance_uid = d.pop("instanceUid", UNSET)
        instance_uid: Union[Unset, UUID]
        if isinstance(_instance_uid, Unset):
            instance_uid = UNSET
        else:
            instance_uid = UUID(_instance_uid)

        create_subtenants = d.pop("createSubtenants", UNSET)

        create_sub_folders = d.pop("createSubFolders", UNSET)

        unlimited_subtenant_quota = d.pop("unlimitedSubtenantQuota", UNSET)

        def _parse_repository_quota_gb(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        repository_quota_gb = _parse_repository_quota_gb(d.pop("repositoryQuotaGb", UNSET))

        windows_backup_policy = cls(
            operation_mode=operation_mode,
            job_configuration=job_configuration,
            instance_uid=instance_uid,
            create_subtenants=create_subtenants,
            create_sub_folders=create_sub_folders,
            unlimited_subtenant_quota=unlimited_subtenant_quota,
            repository_quota_gb=repository_quota_gb,
        )

        windows_backup_policy.additional_properties = d
        return windows_backup_policy

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
