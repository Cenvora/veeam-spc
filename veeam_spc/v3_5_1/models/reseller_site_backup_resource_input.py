from collections.abc import Mapping
from typing import Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ResellerSiteBackupResourceInput")


@_attrs_define
class ResellerSiteBackupResourceInput:
    """
    Attributes:
        repository_uid (UUID): UID assigned to a cloud backup repository.
        resource_friendly_name (str): Cloud repository friendly name configured for a reseller.
        storage_quota (Union[Unset, int]): Amount of space allocated to a reseller, in bytes.
        is_storage_quota_unlimited (Union[Unset, bool]): Indicates whether the amount of space allocated to a reseller
            is unlimited. Default: True.
        servers_quota (Union[Unset, int]): Number of servers that a reseller can store on a cloud backup repository.
        is_servers_quota_unlimited (Union[Unset, bool]): Indicates whether the number of servers that a reseller can
            store on a cloud backup repository is unlimited. Default: True.
        workstations_quota (Union[Unset, int]): Number of workstations that a reseller can store on a cloud backup
            repository.
        is_workstations_quota_unlimited (Union[Unset, bool]): Indicates whether the number of workstations that a
            reseller can store on a cloud backup repository is unlimited. Default: True.
        vms_quota (Union[Unset, int]): Number of VMs that a reseller can store on a cloud backup repository.
        is_vms_quota_unlimited (Union[Unset, bool]): Indicates whether the number of VMs that a reseller can store on a
            cloud backup repository is unlimited. Default: True.
    """

    repository_uid: UUID
    resource_friendly_name: str
    storage_quota: Union[Unset, int] = UNSET
    is_storage_quota_unlimited: Union[Unset, bool] = True
    servers_quota: Union[Unset, int] = UNSET
    is_servers_quota_unlimited: Union[Unset, bool] = True
    workstations_quota: Union[Unset, int] = UNSET
    is_workstations_quota_unlimited: Union[Unset, bool] = True
    vms_quota: Union[Unset, int] = UNSET
    is_vms_quota_unlimited: Union[Unset, bool] = True
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        repository_uid = str(self.repository_uid)

        resource_friendly_name = self.resource_friendly_name

        storage_quota = self.storage_quota

        is_storage_quota_unlimited = self.is_storage_quota_unlimited

        servers_quota = self.servers_quota

        is_servers_quota_unlimited = self.is_servers_quota_unlimited

        workstations_quota = self.workstations_quota

        is_workstations_quota_unlimited = self.is_workstations_quota_unlimited

        vms_quota = self.vms_quota

        is_vms_quota_unlimited = self.is_vms_quota_unlimited

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "repositoryUid": repository_uid,
                "resourceFriendlyName": resource_friendly_name,
            }
        )
        if storage_quota is not UNSET:
            field_dict["storageQuota"] = storage_quota
        if is_storage_quota_unlimited is not UNSET:
            field_dict["isStorageQuotaUnlimited"] = is_storage_quota_unlimited
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

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        repository_uid = UUID(d.pop("repositoryUid"))

        resource_friendly_name = d.pop("resourceFriendlyName")

        storage_quota = d.pop("storageQuota", UNSET)

        is_storage_quota_unlimited = d.pop("isStorageQuotaUnlimited", UNSET)

        servers_quota = d.pop("serversQuota", UNSET)

        is_servers_quota_unlimited = d.pop("isServersQuotaUnlimited", UNSET)

        workstations_quota = d.pop("workstationsQuota", UNSET)

        is_workstations_quota_unlimited = d.pop("isWorkstationsQuotaUnlimited", UNSET)

        vms_quota = d.pop("vmsQuota", UNSET)

        is_vms_quota_unlimited = d.pop("isVmsQuotaUnlimited", UNSET)

        reseller_site_backup_resource_input = cls(
            repository_uid=repository_uid,
            resource_friendly_name=resource_friendly_name,
            storage_quota=storage_quota,
            is_storage_quota_unlimited=is_storage_quota_unlimited,
            servers_quota=servers_quota,
            is_servers_quota_unlimited=is_servers_quota_unlimited,
            workstations_quota=workstations_quota,
            is_workstations_quota_unlimited=is_workstations_quota_unlimited,
            vms_quota=vms_quota,
            is_vms_quota_unlimited=is_vms_quota_unlimited,
        )

        reseller_site_backup_resource_input.additional_properties = d
        return reseller_site_backup_resource_input

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
