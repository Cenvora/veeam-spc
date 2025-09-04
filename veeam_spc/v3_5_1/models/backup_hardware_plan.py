from collections.abc import Mapping
from typing import Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BackupHardwarePlan")


@_attrs_define
class BackupHardwarePlan:
    """
    Example:
        {'instanceUid': '8db62bf7-581b-437b-b640-76212ff40b3a', 'name': 'Silver Hardware Plan', 'backupServerUid':
            'DF997BD3-4AE9-4841-8152-8FF5CC703EAB', 'CpuQuota': 7770, 'MemoryQuota': 7368000, 'NetworkQuota': 3}

    Attributes:
        instance_uid (Union[Unset, UUID]): UID assigned to a hardware plan.
        name (Union[Unset, str]): Name of a hardware plan.
        backup_server_uid (Union[Unset, UUID]): UID assigned to a Veeam Backup & Replication server on which a hardware
            plan is configured.
        cpu_quota (Union[Unset, int]): Maximum CPU resources that VM replicas can utilize, in MHz.
        is_cpu_quota_unlimited (Union[Unset, bool]): Indicates whether CPU resources that VM replicas can utilize are
            unlimited.
        memory_quota (Union[Unset, int]): Maximum RAM resources that VM replicas can utilize, in bytes.
        is_memory_quota_unlimited (Union[Unset, bool]): Indicates whether RAM resources that VM replicas can utilize are
            unlimited.
        network_with_internet_quota (Union[Unset, int]): Number of IP networks with internet access that are available
            to tenant VM replicas.
        network_without_internet_quota (Union[Unset, int]): Number of IP networks without internet access that are
            available to tenant VM replicas.
    """

    instance_uid: Union[Unset, UUID] = UNSET
    name: Union[Unset, str] = UNSET
    backup_server_uid: Union[Unset, UUID] = UNSET
    cpu_quota: Union[Unset, int] = UNSET
    is_cpu_quota_unlimited: Union[Unset, bool] = UNSET
    memory_quota: Union[Unset, int] = UNSET
    is_memory_quota_unlimited: Union[Unset, bool] = UNSET
    network_with_internet_quota: Union[Unset, int] = UNSET
    network_without_internet_quota: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        instance_uid: Union[Unset, str] = UNSET
        if not isinstance(self.instance_uid, Unset):
            instance_uid = str(self.instance_uid)

        name = self.name

        backup_server_uid: Union[Unset, str] = UNSET
        if not isinstance(self.backup_server_uid, Unset):
            backup_server_uid = str(self.backup_server_uid)

        cpu_quota = self.cpu_quota

        is_cpu_quota_unlimited = self.is_cpu_quota_unlimited

        memory_quota = self.memory_quota

        is_memory_quota_unlimited = self.is_memory_quota_unlimited

        network_with_internet_quota = self.network_with_internet_quota

        network_without_internet_quota = self.network_without_internet_quota

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if instance_uid is not UNSET:
            field_dict["instanceUid"] = instance_uid
        if name is not UNSET:
            field_dict["name"] = name
        if backup_server_uid is not UNSET:
            field_dict["backupServerUid"] = backup_server_uid
        if cpu_quota is not UNSET:
            field_dict["cpuQuota"] = cpu_quota
        if is_cpu_quota_unlimited is not UNSET:
            field_dict["isCpuQuotaUnlimited"] = is_cpu_quota_unlimited
        if memory_quota is not UNSET:
            field_dict["memoryQuota"] = memory_quota
        if is_memory_quota_unlimited is not UNSET:
            field_dict["isMemoryQuotaUnlimited"] = is_memory_quota_unlimited
        if network_with_internet_quota is not UNSET:
            field_dict["networkWithInternetQuota"] = network_with_internet_quota
        if network_without_internet_quota is not UNSET:
            field_dict["networkWithoutInternetQuota"] = network_without_internet_quota

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

        _backup_server_uid = d.pop("backupServerUid", UNSET)
        backup_server_uid: Union[Unset, UUID]
        if isinstance(_backup_server_uid, Unset):
            backup_server_uid = UNSET
        else:
            backup_server_uid = UUID(_backup_server_uid)

        cpu_quota = d.pop("cpuQuota", UNSET)

        is_cpu_quota_unlimited = d.pop("isCpuQuotaUnlimited", UNSET)

        memory_quota = d.pop("memoryQuota", UNSET)

        is_memory_quota_unlimited = d.pop("isMemoryQuotaUnlimited", UNSET)

        network_with_internet_quota = d.pop("networkWithInternetQuota", UNSET)

        network_without_internet_quota = d.pop("networkWithoutInternetQuota", UNSET)

        backup_hardware_plan = cls(
            instance_uid=instance_uid,
            name=name,
            backup_server_uid=backup_server_uid,
            cpu_quota=cpu_quota,
            is_cpu_quota_unlimited=is_cpu_quota_unlimited,
            memory_quota=memory_quota,
            is_memory_quota_unlimited=is_memory_quota_unlimited,
            network_with_internet_quota=network_with_internet_quota,
            network_without_internet_quota=network_without_internet_quota,
        )

        backup_hardware_plan.additional_properties = d
        return backup_hardware_plan

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
