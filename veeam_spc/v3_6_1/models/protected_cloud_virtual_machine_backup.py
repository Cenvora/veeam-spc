import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.protected_cloud_virtual_machine_backup_backup_type import ProtectedCloudVirtualMachineBackupBackupType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ProtectedCloudVirtualMachineBackup")


@_attrs_define
class ProtectedCloudVirtualMachineBackup:
    """
    Attributes:
        cloud_virtual_machine_uid (Union[Unset, UUID]): UID assigned to a cloud VM.
        policy_uid (Union[None, UUID, Unset]): UID assigned to a backup policy.
        policy_name (Union[None, Unset, str]): Name of a backup policy.
        backup_type (Union[Unset, ProtectedCloudVirtualMachineBackupBackupType]): Backup policy type.
        destination (Union[Unset, str]): Location where backup chain resides.
        size (Union[Unset, int]): Total size of a backup chain, in bytes.
            > For the `Snapshot` and `ReplicaSnapshot` policy types, size of a cloud VM, in bytes.
        restore_points (Union[Unset, int]): Number of restore points.
        latest_restore_point_date (Union[None, Unset, datetime.datetime]): Time and date of the latest restore point
            creation.
    """

    cloud_virtual_machine_uid: Union[Unset, UUID] = UNSET
    policy_uid: Union[None, UUID, Unset] = UNSET
    policy_name: Union[None, Unset, str] = UNSET
    backup_type: Union[Unset, ProtectedCloudVirtualMachineBackupBackupType] = UNSET
    destination: Union[Unset, str] = UNSET
    size: Union[Unset, int] = UNSET
    restore_points: Union[Unset, int] = UNSET
    latest_restore_point_date: Union[None, Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cloud_virtual_machine_uid: Union[Unset, str] = UNSET
        if not isinstance(self.cloud_virtual_machine_uid, Unset):
            cloud_virtual_machine_uid = str(self.cloud_virtual_machine_uid)

        policy_uid: Union[None, Unset, str]
        if isinstance(self.policy_uid, Unset):
            policy_uid = UNSET
        elif isinstance(self.policy_uid, UUID):
            policy_uid = str(self.policy_uid)
        else:
            policy_uid = self.policy_uid

        policy_name: Union[None, Unset, str]
        if isinstance(self.policy_name, Unset):
            policy_name = UNSET
        else:
            policy_name = self.policy_name

        backup_type: Union[Unset, str] = UNSET
        if not isinstance(self.backup_type, Unset):
            backup_type = self.backup_type.value

        destination = self.destination

        size = self.size

        restore_points = self.restore_points

        latest_restore_point_date: Union[None, Unset, str]
        if isinstance(self.latest_restore_point_date, Unset):
            latest_restore_point_date = UNSET
        elif isinstance(self.latest_restore_point_date, datetime.datetime):
            latest_restore_point_date = self.latest_restore_point_date.isoformat()
        else:
            latest_restore_point_date = self.latest_restore_point_date

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cloud_virtual_machine_uid is not UNSET:
            field_dict["cloudVirtualMachineUid"] = cloud_virtual_machine_uid
        if policy_uid is not UNSET:
            field_dict["policyUid"] = policy_uid
        if policy_name is not UNSET:
            field_dict["policyName"] = policy_name
        if backup_type is not UNSET:
            field_dict["backupType"] = backup_type
        if destination is not UNSET:
            field_dict["destination"] = destination
        if size is not UNSET:
            field_dict["size"] = size
        if restore_points is not UNSET:
            field_dict["restorePoints"] = restore_points
        if latest_restore_point_date is not UNSET:
            field_dict["latestRestorePointDate"] = latest_restore_point_date

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _cloud_virtual_machine_uid = d.pop("cloudVirtualMachineUid", UNSET)
        cloud_virtual_machine_uid: Union[Unset, UUID]
        if isinstance(_cloud_virtual_machine_uid, Unset):
            cloud_virtual_machine_uid = UNSET
        else:
            cloud_virtual_machine_uid = UUID(_cloud_virtual_machine_uid)

        def _parse_policy_uid(data: object) -> Union[None, UUID, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                policy_uid_type_0 = UUID(data)

                return policy_uid_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID, Unset], data)

        policy_uid = _parse_policy_uid(d.pop("policyUid", UNSET))

        def _parse_policy_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        policy_name = _parse_policy_name(d.pop("policyName", UNSET))

        _backup_type = d.pop("backupType", UNSET)
        backup_type: Union[Unset, ProtectedCloudVirtualMachineBackupBackupType]
        if isinstance(_backup_type, Unset):
            backup_type = UNSET
        else:
            backup_type = ProtectedCloudVirtualMachineBackupBackupType(_backup_type)

        destination = d.pop("destination", UNSET)

        size = d.pop("size", UNSET)

        restore_points = d.pop("restorePoints", UNSET)

        def _parse_latest_restore_point_date(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                latest_restore_point_date_type_0 = isoparse(data)

                return latest_restore_point_date_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        latest_restore_point_date = _parse_latest_restore_point_date(d.pop("latestRestorePointDate", UNSET))

        protected_cloud_virtual_machine_backup = cls(
            cloud_virtual_machine_uid=cloud_virtual_machine_uid,
            policy_uid=policy_uid,
            policy_name=policy_name,
            backup_type=backup_type,
            destination=destination,
            size=size,
            restore_points=restore_points,
            latest_restore_point_date=latest_restore_point_date,
        )

        protected_cloud_virtual_machine_backup.additional_properties = d
        return protected_cloud_virtual_machine_backup

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
