from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BackupHardwarePlanStorage")


@_attrs_define
class BackupHardwarePlanStorage:
    """
    Attributes:
        instance_uid (Union[Unset, UUID]): UID assigned to a hardware plan storage.
        name (Union[Unset, str]): Friendly name of a hardware plan storage.
        hardware_plan_uid (Union[Unset, UUID]): UID assigned to a hardware plan.
        quota (Union[None, Unset, int]): Amount of disk space provided to a tenant.
    """

    instance_uid: Union[Unset, UUID] = UNSET
    name: Union[Unset, str] = UNSET
    hardware_plan_uid: Union[Unset, UUID] = UNSET
    quota: Union[None, Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        instance_uid: Union[Unset, str] = UNSET
        if not isinstance(self.instance_uid, Unset):
            instance_uid = str(self.instance_uid)

        name = self.name

        hardware_plan_uid: Union[Unset, str] = UNSET
        if not isinstance(self.hardware_plan_uid, Unset):
            hardware_plan_uid = str(self.hardware_plan_uid)

        quota: Union[None, Unset, int]
        if isinstance(self.quota, Unset):
            quota = UNSET
        else:
            quota = self.quota

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if instance_uid is not UNSET:
            field_dict["instanceUid"] = instance_uid
        if name is not UNSET:
            field_dict["name"] = name
        if hardware_plan_uid is not UNSET:
            field_dict["hardwarePlanUid"] = hardware_plan_uid
        if quota is not UNSET:
            field_dict["quota"] = quota

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

        name = d.pop("name", UNSET)

        _hardware_plan_uid = d.pop("hardwarePlanUid", UNSET)
        hardware_plan_uid: Union[Unset, UUID]
        if isinstance(_hardware_plan_uid, Unset):
            hardware_plan_uid = UNSET
        else:
            hardware_plan_uid = UUID(_hardware_plan_uid)

        def _parse_quota(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        quota = _parse_quota(d.pop("quota", UNSET))

        backup_hardware_plan_storage = cls(
            instance_uid=instance_uid,
            name=name,
            hardware_plan_uid=hardware_plan_uid,
            quota=quota,
        )

        backup_hardware_plan_storage.additional_properties = d
        return backup_hardware_plan_storage

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
