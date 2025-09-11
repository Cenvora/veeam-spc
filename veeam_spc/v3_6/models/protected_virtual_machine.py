import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.malware_state import MalwareState
from ..types import UNSET, Unset

T = TypeVar("T", bound="ProtectedVirtualMachine")


@_attrs_define
class ProtectedVirtualMachine:
    """
    Attributes:
        instance_uid (Union[Unset, UUID]): UID assigned to a protected VM.
        backup_server_uid (Union[Unset, UUID]): UID assigned to a backup server.
        organization_uid (Union[Unset, UUID]): UID assigned to an organization.
        name (Union[Unset, str]): VM hostname.
        hierarchy_ref (Union[Unset, str]): Reference ID of a VM.
        parent_host_ref (Union[Unset, str]): Reference ID assigned to a parent hypervisor.
        object_uid (Union[Unset, UUID]): UID assigned to a VM as a job object.
        ip_addresses (Union[Unset, list[str]]): IP addresses.
        provisioned_source_size (Union[Unset, int]): Total size of protected VM disks, in bytes.
        used_source_size (Union[Unset, int]): Used space on protected VM disks, in bytes.
        total_restore_point_size (Union[Unset, int]): Total size of all restore points, in bytes.
        latest_restore_point_size (Union[Unset, int]): Size of the latest restore point, in bytes.
        restore_points (Union[Unset, int]): Number of restore points.
        latest_restore_point_date (Union[Unset, datetime.datetime]): Date and time of the latest restore point creation.
        job_uid (Union[Unset, UUID]): UID assigned to a backup job that created the latest restore point.
        malware_state (Union[Unset, MalwareState]): Malware status.
        immutable (Union[Unset, bool]): Indicates whether a protected VM has any immutable restore points.
    """

    instance_uid: Union[Unset, UUID] = UNSET
    backup_server_uid: Union[Unset, UUID] = UNSET
    organization_uid: Union[Unset, UUID] = UNSET
    name: Union[Unset, str] = UNSET
    hierarchy_ref: Union[Unset, str] = UNSET
    parent_host_ref: Union[Unset, str] = UNSET
    object_uid: Union[Unset, UUID] = UNSET
    ip_addresses: Union[Unset, list[str]] = UNSET
    provisioned_source_size: Union[Unset, int] = UNSET
    used_source_size: Union[Unset, int] = UNSET
    total_restore_point_size: Union[Unset, int] = UNSET
    latest_restore_point_size: Union[Unset, int] = UNSET
    restore_points: Union[Unset, int] = UNSET
    latest_restore_point_date: Union[Unset, datetime.datetime] = UNSET
    job_uid: Union[Unset, UUID] = UNSET
    malware_state: Union[Unset, MalwareState] = UNSET
    immutable: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        instance_uid: Union[Unset, str] = UNSET
        if not isinstance(self.instance_uid, Unset):
            instance_uid = str(self.instance_uid)

        backup_server_uid: Union[Unset, str] = UNSET
        if not isinstance(self.backup_server_uid, Unset):
            backup_server_uid = str(self.backup_server_uid)

        organization_uid: Union[Unset, str] = UNSET
        if not isinstance(self.organization_uid, Unset):
            organization_uid = str(self.organization_uid)

        name = self.name

        hierarchy_ref = self.hierarchy_ref

        parent_host_ref = self.parent_host_ref

        object_uid: Union[Unset, str] = UNSET
        if not isinstance(self.object_uid, Unset):
            object_uid = str(self.object_uid)

        ip_addresses: Union[Unset, list[str]] = UNSET
        if not isinstance(self.ip_addresses, Unset):
            ip_addresses = self.ip_addresses

        provisioned_source_size = self.provisioned_source_size

        used_source_size = self.used_source_size

        total_restore_point_size = self.total_restore_point_size

        latest_restore_point_size = self.latest_restore_point_size

        restore_points = self.restore_points

        latest_restore_point_date: Union[Unset, str] = UNSET
        if not isinstance(self.latest_restore_point_date, Unset):
            latest_restore_point_date = self.latest_restore_point_date.isoformat()

        job_uid: Union[Unset, str] = UNSET
        if not isinstance(self.job_uid, Unset):
            job_uid = str(self.job_uid)

        malware_state: Union[Unset, str] = UNSET
        if not isinstance(self.malware_state, Unset):
            malware_state = self.malware_state.value

        immutable = self.immutable

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if instance_uid is not UNSET:
            field_dict["instanceUid"] = instance_uid
        if backup_server_uid is not UNSET:
            field_dict["backupServerUid"] = backup_server_uid
        if organization_uid is not UNSET:
            field_dict["organizationUid"] = organization_uid
        if name is not UNSET:
            field_dict["name"] = name
        if hierarchy_ref is not UNSET:
            field_dict["hierarchyRef"] = hierarchy_ref
        if parent_host_ref is not UNSET:
            field_dict["parentHostRef"] = parent_host_ref
        if object_uid is not UNSET:
            field_dict["objectUid"] = object_uid
        if ip_addresses is not UNSET:
            field_dict["ipAddresses"] = ip_addresses
        if provisioned_source_size is not UNSET:
            field_dict["provisionedSourceSize"] = provisioned_source_size
        if used_source_size is not UNSET:
            field_dict["usedSourceSize"] = used_source_size
        if total_restore_point_size is not UNSET:
            field_dict["totalRestorePointSize"] = total_restore_point_size
        if latest_restore_point_size is not UNSET:
            field_dict["latestRestorePointSize"] = latest_restore_point_size
        if restore_points is not UNSET:
            field_dict["restorePoints"] = restore_points
        if latest_restore_point_date is not UNSET:
            field_dict["latestRestorePointDate"] = latest_restore_point_date
        if job_uid is not UNSET:
            field_dict["jobUid"] = job_uid
        if malware_state is not UNSET:
            field_dict["malwareState"] = malware_state
        if immutable is not UNSET:
            field_dict["immutable"] = immutable

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

        _backup_server_uid = d.pop("backupServerUid", UNSET)
        backup_server_uid: Union[Unset, UUID]
        if isinstance(_backup_server_uid, Unset):
            backup_server_uid = UNSET
        else:
            backup_server_uid = UUID(_backup_server_uid)

        _organization_uid = d.pop("organizationUid", UNSET)
        organization_uid: Union[Unset, UUID]
        if isinstance(_organization_uid, Unset):
            organization_uid = UNSET
        else:
            organization_uid = UUID(_organization_uid)

        name = d.pop("name", UNSET)

        hierarchy_ref = d.pop("hierarchyRef", UNSET)

        parent_host_ref = d.pop("parentHostRef", UNSET)

        _object_uid = d.pop("objectUid", UNSET)
        object_uid: Union[Unset, UUID]
        if isinstance(_object_uid, Unset):
            object_uid = UNSET
        else:
            object_uid = UUID(_object_uid)

        ip_addresses = cast(list[str], d.pop("ipAddresses", UNSET))

        provisioned_source_size = d.pop("provisionedSourceSize", UNSET)

        used_source_size = d.pop("usedSourceSize", UNSET)

        total_restore_point_size = d.pop("totalRestorePointSize", UNSET)

        latest_restore_point_size = d.pop("latestRestorePointSize", UNSET)

        restore_points = d.pop("restorePoints", UNSET)

        _latest_restore_point_date = d.pop("latestRestorePointDate", UNSET)
        latest_restore_point_date: Union[Unset, datetime.datetime]
        if isinstance(_latest_restore_point_date, Unset):
            latest_restore_point_date = UNSET
        else:
            latest_restore_point_date = isoparse(_latest_restore_point_date)

        _job_uid = d.pop("jobUid", UNSET)
        job_uid: Union[Unset, UUID]
        if isinstance(_job_uid, Unset):
            job_uid = UNSET
        else:
            job_uid = UUID(_job_uid)

        _malware_state = d.pop("malwareState", UNSET)
        malware_state: Union[Unset, MalwareState]
        if isinstance(_malware_state, Unset):
            malware_state = UNSET
        else:
            malware_state = MalwareState(_malware_state)

        immutable = d.pop("immutable", UNSET)

        protected_virtual_machine = cls(
            instance_uid=instance_uid,
            backup_server_uid=backup_server_uid,
            organization_uid=organization_uid,
            name=name,
            hierarchy_ref=hierarchy_ref,
            parent_host_ref=parent_host_ref,
            object_uid=object_uid,
            ip_addresses=ip_addresses,
            provisioned_source_size=provisioned_source_size,
            used_source_size=used_source_size,
            total_restore_point_size=total_restore_point_size,
            latest_restore_point_size=latest_restore_point_size,
            restore_points=restore_points,
            latest_restore_point_date=latest_restore_point_date,
            job_uid=job_uid,
            malware_state=malware_state,
            immutable=immutable,
        )

        protected_virtual_machine.additional_properties = d
        return protected_virtual_machine

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
