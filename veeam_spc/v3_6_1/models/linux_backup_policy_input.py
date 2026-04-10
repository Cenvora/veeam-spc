from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.backup_job_operation_mode import BackupJobOperationMode
from ..models.backup_policy_access_mode import BackupPolicyAccessMode
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.linux_backup_job_configuration import LinuxBackupJobConfiguration


T = TypeVar("T", bound="LinuxBackupPolicyInput")


@_attrs_define
class LinuxBackupPolicyInput:
    """
    Attributes:
        name (str): Backup policy name.
        operation_mode (BackupJobOperationMode): Backup job operation mode.
        access_mode (BackupPolicyAccessMode): Backup policy access mode.
        job_configuration (LinuxBackupJobConfiguration):
        description (Union[Unset, str]): Backup policy description. Default: ''.
        create_subtenants (Union[Unset, bool]): Defines whether a subtenant must be created for each Veeam Agent for
            Linux.
            > Available if a cloud repository is selected as backup destination.
             Default: True.
        unlimited_subtenant_quota (Union[Unset, bool]): Defines whether a subtenant can consume unlimited amount of
            space on a repository.
            > Available if a cloud repository is selected as backup destination.
             Default: False.
        repository_quota_gb (Union[None, Unset, int]): Maximum amount of space that a subtenant can consume on a
            repository.
            > If a subtenant can consume unlimited amount of space, the value of this property is ignored. <br>
            > Available if a cloud repository is selected as backup destination.
             Default: 100.
    """

    name: str
    operation_mode: BackupJobOperationMode
    access_mode: BackupPolicyAccessMode
    job_configuration: "LinuxBackupJobConfiguration"
    description: Union[Unset, str] = ""
    create_subtenants: Union[Unset, bool] = True
    unlimited_subtenant_quota: Union[Unset, bool] = False
    repository_quota_gb: Union[None, Unset, int] = 100
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        operation_mode = self.operation_mode.value

        access_mode = self.access_mode.value

        job_configuration = self.job_configuration.to_dict()

        description = self.description

        create_subtenants = self.create_subtenants

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
                "name": name,
                "operationMode": operation_mode,
                "accessMode": access_mode,
                "jobConfiguration": job_configuration,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if create_subtenants is not UNSET:
            field_dict["createSubtenants"] = create_subtenants
        if unlimited_subtenant_quota is not UNSET:
            field_dict["unlimitedSubtenantQuota"] = unlimited_subtenant_quota
        if repository_quota_gb is not UNSET:
            field_dict["repositoryQuotaGB"] = repository_quota_gb

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.linux_backup_job_configuration import LinuxBackupJobConfiguration

        d = dict(src_dict)
        name = d.pop("name")

        operation_mode = BackupJobOperationMode(d.pop("operationMode"))

        access_mode = BackupPolicyAccessMode(d.pop("accessMode"))

        job_configuration = LinuxBackupJobConfiguration.from_dict(d.pop("jobConfiguration"))

        description = d.pop("description", UNSET)

        create_subtenants = d.pop("createSubtenants", UNSET)

        unlimited_subtenant_quota = d.pop("unlimitedSubtenantQuota", UNSET)

        def _parse_repository_quota_gb(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        repository_quota_gb = _parse_repository_quota_gb(d.pop("repositoryQuotaGB", UNSET))

        linux_backup_policy_input = cls(
            name=name,
            operation_mode=operation_mode,
            access_mode=access_mode,
            job_configuration=job_configuration,
            description=description,
            create_subtenants=create_subtenants,
            unlimited_subtenant_quota=unlimited_subtenant_quota,
            repository_quota_gb=repository_quota_gb,
        )

        linux_backup_policy_input.additional_properties = d
        return linux_backup_policy_input

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
