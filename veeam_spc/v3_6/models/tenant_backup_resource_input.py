from collections.abc import Mapping
from typing import Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TenantBackupResourceInput")


@_attrs_define
class TenantBackupResourceInput:
    """
    Attributes:
        repository_uid (UUID): UID assigned to a cloud repository.
        cloud_repository_name (str): Name of a cloud backup repository.
        storage_quota (int): Amount of space allocated to a company on a cloud repository, in bytes.
        servers_quota (Union[Unset, int]): Maximum number of Veeam backup agents in the Server mode that a company is
            allowed to store on a cloud repository.
        is_servers_quota_unlimited (Union[Unset, bool]): Indicates whether a company is allowed to store an unlimited
            number of Veeam backup agents in the Server mode on a cloud repository. Default: True.
        workstations_quota (Union[Unset, int]): Maximum number of Veeam backup agents in the Workstation mode that a
            company is allowed to store on a cloud repository.
        is_workstations_quota_unlimited (Union[Unset, bool]): Indicates whether a company is allowed to store an
            unlimited number of Veeam backup agents in the Workstation mode on a cloud repository. Default: True.
        vms_quota (Union[Unset, int]): Maximum number of VMs that a company is allowed to store on a cloud repository.
        is_vms_quota_unlimited (Union[Unset, bool]): Indicates whether a company is allowed to store an unlimited number
            of VMs on a cloud repository. Default: True.
        is_wan_acceleration_enabled (Union[Unset, bool]): Indicates whether WAN acceleration is enabled. Default: False.
        wan_accelerator_uid (Union[Unset, UUID]): UID assigned to a WAN accelerator.
        is_default (Union[Unset, bool]): Defines whether a cloud repository is set by default. Default: False.
    """

    repository_uid: UUID
    cloud_repository_name: str
    storage_quota: int
    servers_quota: Union[Unset, int] = UNSET
    is_servers_quota_unlimited: Union[Unset, bool] = True
    workstations_quota: Union[Unset, int] = UNSET
    is_workstations_quota_unlimited: Union[Unset, bool] = True
    vms_quota: Union[Unset, int] = UNSET
    is_vms_quota_unlimited: Union[Unset, bool] = True
    is_wan_acceleration_enabled: Union[Unset, bool] = False
    wan_accelerator_uid: Union[Unset, UUID] = UNSET
    is_default: Union[Unset, bool] = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        repository_uid = str(self.repository_uid)

        cloud_repository_name = self.cloud_repository_name

        storage_quota = self.storage_quota

        servers_quota = self.servers_quota

        is_servers_quota_unlimited = self.is_servers_quota_unlimited

        workstations_quota = self.workstations_quota

        is_workstations_quota_unlimited = self.is_workstations_quota_unlimited

        vms_quota = self.vms_quota

        is_vms_quota_unlimited = self.is_vms_quota_unlimited

        is_wan_acceleration_enabled = self.is_wan_acceleration_enabled

        wan_accelerator_uid: Union[Unset, str] = UNSET
        if not isinstance(self.wan_accelerator_uid, Unset):
            wan_accelerator_uid = str(self.wan_accelerator_uid)

        is_default = self.is_default

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "repositoryUid": repository_uid,
                "cloudRepositoryName": cloud_repository_name,
                "storageQuota": storage_quota,
            }
        )
        if servers_quota is not UNSET:
            field_dict["serversQuota"] = servers_quota
        if is_servers_quota_unlimited is not UNSET:
            field_dict["isServersQuotaUnlimited"] = is_servers_quota_unlimited
        if workstations_quota is not UNSET:
            field_dict["workstationsQuota"] = workstations_quota
        if is_workstations_quota_unlimited is not UNSET:
            field_dict["isWorkstationsQuotaUnlimited"] = is_workstations_quota_unlimited
        if vms_quota is not UNSET:
            field_dict["vmsQuota"] = vms_quota
        if is_vms_quota_unlimited is not UNSET:
            field_dict["isVmsQuotaUnlimited"] = is_vms_quota_unlimited
        if is_wan_acceleration_enabled is not UNSET:
            field_dict["isWanAccelerationEnabled"] = is_wan_acceleration_enabled
        if wan_accelerator_uid is not UNSET:
            field_dict["wanAcceleratorUid"] = wan_accelerator_uid
        if is_default is not UNSET:
            field_dict["isDefault"] = is_default

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        repository_uid = UUID(d.pop("repositoryUid"))

        cloud_repository_name = d.pop("cloudRepositoryName")

        storage_quota = d.pop("storageQuota")

        servers_quota = d.pop("serversQuota", UNSET)

        is_servers_quota_unlimited = d.pop("isServersQuotaUnlimited", UNSET)

        workstations_quota = d.pop("workstationsQuota", UNSET)

        is_workstations_quota_unlimited = d.pop("isWorkstationsQuotaUnlimited", UNSET)

        vms_quota = d.pop("vmsQuota", UNSET)

        is_vms_quota_unlimited = d.pop("isVmsQuotaUnlimited", UNSET)

        is_wan_acceleration_enabled = d.pop("isWanAccelerationEnabled", UNSET)

        _wan_accelerator_uid = d.pop("wanAcceleratorUid", UNSET)
        wan_accelerator_uid: Union[Unset, UUID]
        if isinstance(_wan_accelerator_uid, Unset):
            wan_accelerator_uid = UNSET
        else:
            wan_accelerator_uid = UUID(_wan_accelerator_uid)

        is_default = d.pop("isDefault", UNSET)

        tenant_backup_resource_input = cls(
            repository_uid=repository_uid,
            cloud_repository_name=cloud_repository_name,
            storage_quota=storage_quota,
            servers_quota=servers_quota,
            is_servers_quota_unlimited=is_servers_quota_unlimited,
            workstations_quota=workstations_quota,
            is_workstations_quota_unlimited=is_workstations_quota_unlimited,
            vms_quota=vms_quota,
            is_vms_quota_unlimited=is_vms_quota_unlimited,
            is_wan_acceleration_enabled=is_wan_acceleration_enabled,
            wan_accelerator_uid=wan_accelerator_uid,
            is_default=is_default,
        )

        tenant_backup_resource_input.additional_properties = d
        return tenant_backup_resource_input

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
