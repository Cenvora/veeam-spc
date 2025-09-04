from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CompanySiteBackupResource")


@_attrs_define
class CompanySiteBackupResource:
    """
    Attributes:
        cloud_repository_name (str): Name of a cloud backup repository.
        storage_quota (int): Amount of space allocated to a company on a cloud repository, in bytes.
        instance_uid (Union[Unset, UUID]): UID assigned to a site backup resource allocated to a company.
        company_uid (Union[Unset, UUID]): UID assigned to a company.
        site_uid (Union[Unset, UUID]): UID assigned to a Veeam Cloud Connect site.
        repository_uid (Union[Unset, UUID]): UID assigned to a cloud repository.
        used_space (Union[None, Unset, int]): Amount of used space on a cloud repository, in bytes.
        servers_quota (Union[None, Unset, int]): Maximum number of Veeam backup agents in the Server mode that a company
            is allowed to store on a cloud repository.
        is_servers_quota_unlimited (Union[Unset, bool]): Indicates whether a company is allowed to store an unlimited
            number of Veeam backup agents in the Server mode on a cloud repository. Default: True.
        workstations_quota (Union[None, Unset, int]): Maximum number of Veeam backup agents in the Workstation mode that
            a company is allowed to store on a cloud repository.
        is_workstations_quota_unlimited (Union[Unset, bool]): Indicates whether a company is allowed to store an
            unlimited number of Veeam backup agents in the Workstation mode on a cloud repository. Default: True.
        vms_quota (Union[None, Unset, int]): Maximum number of VMs that a company is allowed to store on a cloud
            repository.
        is_vms_quota_unlimited (Union[Unset, bool]): Indicates whether a company is allowed to store an unlimited number
            of VMs on a cloud repository. Default: True.
        is_wan_acceleration_enabled (Union[Unset, bool]): Indicates whether WAN acceleration is enabled. Default: False.
        wan_accelerator_uid (Union[None, UUID, Unset]): UID assigned to a WAN accelerator.
        is_default (Union[Unset, bool]): Indicates whether the repository is used by default. Default: False.
    """

    cloud_repository_name: str
    storage_quota: int
    instance_uid: Union[Unset, UUID] = UNSET
    company_uid: Union[Unset, UUID] = UNSET
    site_uid: Union[Unset, UUID] = UNSET
    repository_uid: Union[Unset, UUID] = UNSET
    used_space: Union[None, Unset, int] = UNSET
    servers_quota: Union[None, Unset, int] = UNSET
    is_servers_quota_unlimited: Union[Unset, bool] = True
    workstations_quota: Union[None, Unset, int] = UNSET
    is_workstations_quota_unlimited: Union[Unset, bool] = True
    vms_quota: Union[None, Unset, int] = UNSET
    is_vms_quota_unlimited: Union[Unset, bool] = True
    is_wan_acceleration_enabled: Union[Unset, bool] = False
    wan_accelerator_uid: Union[None, UUID, Unset] = UNSET
    is_default: Union[Unset, bool] = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cloud_repository_name = self.cloud_repository_name

        storage_quota = self.storage_quota

        instance_uid: Union[Unset, str] = UNSET
        if not isinstance(self.instance_uid, Unset):
            instance_uid = str(self.instance_uid)

        company_uid: Union[Unset, str] = UNSET
        if not isinstance(self.company_uid, Unset):
            company_uid = str(self.company_uid)

        site_uid: Union[Unset, str] = UNSET
        if not isinstance(self.site_uid, Unset):
            site_uid = str(self.site_uid)

        repository_uid: Union[Unset, str] = UNSET
        if not isinstance(self.repository_uid, Unset):
            repository_uid = str(self.repository_uid)

        used_space: Union[None, Unset, int]
        if isinstance(self.used_space, Unset):
            used_space = UNSET
        else:
            used_space = self.used_space

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

        is_wan_acceleration_enabled = self.is_wan_acceleration_enabled

        wan_accelerator_uid: Union[None, Unset, str]
        if isinstance(self.wan_accelerator_uid, Unset):
            wan_accelerator_uid = UNSET
        elif isinstance(self.wan_accelerator_uid, UUID):
            wan_accelerator_uid = str(self.wan_accelerator_uid)
        else:
            wan_accelerator_uid = self.wan_accelerator_uid

        is_default = self.is_default

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "cloudRepositoryName": cloud_repository_name,
                "storageQuota": storage_quota,
            }
        )
        if instance_uid is not UNSET:
            field_dict["instanceUid"] = instance_uid
        if company_uid is not UNSET:
            field_dict["companyUid"] = company_uid
        if site_uid is not UNSET:
            field_dict["siteUid"] = site_uid
        if repository_uid is not UNSET:
            field_dict["repositoryUid"] = repository_uid
        if used_space is not UNSET:
            field_dict["usedSpace"] = used_space
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
        cloud_repository_name = d.pop("cloudRepositoryName")

        storage_quota = d.pop("storageQuota")

        _instance_uid = d.pop("instanceUid", UNSET)
        instance_uid: Union[Unset, UUID]
        if isinstance(_instance_uid, Unset):
            instance_uid = UNSET
        else:
            instance_uid = UUID(_instance_uid)

        _company_uid = d.pop("companyUid", UNSET)
        company_uid: Union[Unset, UUID]
        if isinstance(_company_uid, Unset):
            company_uid = UNSET
        else:
            company_uid = UUID(_company_uid)

        _site_uid = d.pop("siteUid", UNSET)
        site_uid: Union[Unset, UUID]
        if isinstance(_site_uid, Unset):
            site_uid = UNSET
        else:
            site_uid = UUID(_site_uid)

        _repository_uid = d.pop("repositoryUid", UNSET)
        repository_uid: Union[Unset, UUID]
        if isinstance(_repository_uid, Unset):
            repository_uid = UNSET
        else:
            repository_uid = UUID(_repository_uid)

        def _parse_used_space(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        used_space = _parse_used_space(d.pop("usedSpace", UNSET))

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

        is_wan_acceleration_enabled = d.pop("isWanAccelerationEnabled", UNSET)

        def _parse_wan_accelerator_uid(data: object) -> Union[None, UUID, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                wan_accelerator_uid_type_0 = UUID(data)

                return wan_accelerator_uid_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID, Unset], data)

        wan_accelerator_uid = _parse_wan_accelerator_uid(d.pop("wanAcceleratorUid", UNSET))

        is_default = d.pop("isDefault", UNSET)

        company_site_backup_resource = cls(
            cloud_repository_name=cloud_repository_name,
            storage_quota=storage_quota,
            instance_uid=instance_uid,
            company_uid=company_uid,
            site_uid=site_uid,
            repository_uid=repository_uid,
            used_space=used_space,
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

        company_site_backup_resource.additional_properties = d
        return company_site_backup_resource

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
