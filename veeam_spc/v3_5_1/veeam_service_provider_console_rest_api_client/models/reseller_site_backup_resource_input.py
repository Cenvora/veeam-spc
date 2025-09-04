from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast
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
        storage_quota (Union[None, Unset, int]): Amount of space allocated to a reseller, in bytes.
        is_storage_quota_unlimited (Union[Unset, bool]): Indicates whether the amount of space allocated to a reseller
            is unlimited. Default: True.
        servers_quota (Union[None, Unset, int]): Number of servers that a reseller can store on a cloud backup
            repository.
        is_servers_quota_unlimited (Union[Unset, bool]): Indicates whether the number of servers that a reseller can
            store on a cloud backup repository is unlimited. Default: True.
        workstations_quota (Union[None, Unset, int]): Number of workstations that a reseller can store on a cloud backup
            repository.
        is_workstations_quota_unlimited (Union[Unset, bool]): Indicates whether the number of workstations that a
            reseller can store on a cloud backup repository is unlimited. Default: True.
        vms_quota (Union[None, Unset, int]): Number of VMs that a reseller can store on a cloud backup repository.
        is_vms_quota_unlimited (Union[Unset, bool]): Indicates whether the number of VMs that a reseller can store on a
            cloud backup repository is unlimited. Default: True.
    """

    repository_uid: UUID
    resource_friendly_name: str
    storage_quota: Union[None, Unset, int] = UNSET
    is_storage_quota_unlimited: Union[Unset, bool] = True
    servers_quota: Union[None, Unset, int] = UNSET
    is_servers_quota_unlimited: Union[Unset, bool] = True
    workstations_quota: Union[None, Unset, int] = UNSET
    is_workstations_quota_unlimited: Union[Unset, bool] = True
    vms_quota: Union[None, Unset, int] = UNSET
    is_vms_quota_unlimited: Union[Unset, bool] = True
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        repository_uid = str(self.repository_uid)

        resource_friendly_name = self.resource_friendly_name

        storage_quota: Union[None, Unset, int]
        if isinstance(self.storage_quota, Unset):
            storage_quota = UNSET
        else:
            storage_quota = self.storage_quota

        is_storage_quota_unlimited = self.is_storage_quota_unlimited

        servers_quota: Union[None, Unset, int]
        if isinstance(self.servers_quota, Unset):
            servers_quota = UNSET
        else:
            servers_quota = self.servers_quota

        is_servers_quota_unlimited = self.is_servers_quota_unlimited

        workstations_quota: Union[None, Unset, int]
        if isinstance(self.workstations_quota, Unset):
            workstations_quota = UNSET
        else:
            workstations_quota = self.workstations_quota

        is_workstations_quota_unlimited = self.is_workstations_quota_unlimited

        vms_quota: Union[None, Unset, int]
        if isinstance(self.vms_quota, Unset):
            vms_quota = UNSET
        else:
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

        def _parse_storage_quota(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        storage_quota = _parse_storage_quota(d.pop("storageQuota", UNSET))

        is_storage_quota_unlimited = d.pop("isStorageQuotaUnlimited", UNSET)

        def _parse_servers_quota(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        servers_quota = _parse_servers_quota(d.pop("serversQuota", UNSET))

        is_servers_quota_unlimited = d.pop("isServersQuotaUnlimited", UNSET)

        def _parse_workstations_quota(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        workstations_quota = _parse_workstations_quota(d.pop("workstationsQuota", UNSET))

        is_workstations_quota_unlimited = d.pop("isWorkstationsQuotaUnlimited", UNSET)

        def _parse_vms_quota(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        vms_quota = _parse_vms_quota(d.pop("vmsQuota", UNSET))

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
