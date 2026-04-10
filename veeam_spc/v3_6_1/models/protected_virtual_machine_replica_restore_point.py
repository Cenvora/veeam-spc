import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="ProtectedVirtualMachineReplicaRestorePoint")


@_attrs_define
class ProtectedVirtualMachineReplicaRestorePoint:
    """
    Attributes:
        instance_uid (Union[Unset, UUID]): UID assigned to a restore point.
        virtual_machine_uid (Union[Unset, UUID]): UID assigned to a virtual machine.
        backup_uid (Union[Unset, UUID]): UID assigned to a replication chain.
        job_uid (Union[None, UUID, Unset]): UID assigned to a replication job.
        hardware_plan_uid (Union[None, UUID, Unset]): UID assigned to a hardware plan.
        creation_date (Union[None, Unset, datetime.datetime]): Date and time when a restore point was created.
    """

    instance_uid: Union[Unset, UUID] = UNSET
    virtual_machine_uid: Union[Unset, UUID] = UNSET
    backup_uid: Union[Unset, UUID] = UNSET
    job_uid: Union[None, UUID, Unset] = UNSET
    hardware_plan_uid: Union[None, UUID, Unset] = UNSET
    creation_date: Union[None, Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        instance_uid: Union[Unset, str] = UNSET
        if not isinstance(self.instance_uid, Unset):
            instance_uid = str(self.instance_uid)

        virtual_machine_uid: Union[Unset, str] = UNSET
        if not isinstance(self.virtual_machine_uid, Unset):
            virtual_machine_uid = str(self.virtual_machine_uid)

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

        hardware_plan_uid: Union[None, Unset, str]
        if isinstance(self.hardware_plan_uid, Unset):
            hardware_plan_uid = UNSET
        elif isinstance(self.hardware_plan_uid, UUID):
            hardware_plan_uid = str(self.hardware_plan_uid)
        else:
            hardware_plan_uid = self.hardware_plan_uid

        creation_date: Union[None, Unset, str]
        if isinstance(self.creation_date, Unset):
            creation_date = UNSET
        elif isinstance(self.creation_date, datetime.datetime):
            creation_date = self.creation_date.isoformat()
        else:
            creation_date = self.creation_date

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if instance_uid is not UNSET:
            field_dict["instanceUid"] = instance_uid
        if virtual_machine_uid is not UNSET:
            field_dict["virtualMachineUid"] = virtual_machine_uid
        if backup_uid is not UNSET:
            field_dict["backupUid"] = backup_uid
        if job_uid is not UNSET:
            field_dict["jobUid"] = job_uid
        if hardware_plan_uid is not UNSET:
            field_dict["hardwarePlanUid"] = hardware_plan_uid
        if creation_date is not UNSET:
            field_dict["creationDate"] = creation_date

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

        def _parse_hardware_plan_uid(data: object) -> Union[None, UUID, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                hardware_plan_uid_type_0 = UUID(data)

                return hardware_plan_uid_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID, Unset], data)

        hardware_plan_uid = _parse_hardware_plan_uid(d.pop("hardwarePlanUid", UNSET))

        def _parse_creation_date(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                creation_date_type_0 = isoparse(data)

                return creation_date_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        creation_date = _parse_creation_date(d.pop("creationDate", UNSET))

        protected_virtual_machine_replica_restore_point = cls(
            instance_uid=instance_uid,
            virtual_machine_uid=virtual_machine_uid,
            backup_uid=backup_uid,
            job_uid=job_uid,
            hardware_plan_uid=hardware_plan_uid,
            creation_date=creation_date,
        )

        protected_virtual_machine_replica_restore_point.additional_properties = d
        return protected_virtual_machine_replica_restore_point

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
