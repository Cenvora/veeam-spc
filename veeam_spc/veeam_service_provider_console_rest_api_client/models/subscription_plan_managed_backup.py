from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.subscription_plan_managed_backup_backup_used_space_units import (
    SubscriptionPlanManagedBackupBackupUsedSpaceUnits,
)
from ..models.subscription_plan_managed_backup_free_backup_used_space_units import (
    SubscriptionPlanManagedBackupFreeBackupUsedSpaceUnits,
)
from ..models.subscription_plan_managed_backup_repository_allocated_space_units import (
    SubscriptionPlanManagedBackupRepositoryAllocatedSpaceUnits,
)
from ..models.subscription_plan_managed_backup_repository_space_usage_algorithm import (
    SubscriptionPlanManagedBackupRepositorySpaceUsageAlgorithm,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="SubscriptionPlanManagedBackup")


@_attrs_define
class SubscriptionPlanManagedBackup:
    """
    Attributes:
        managed_service_price (Union[Unset, float]): Flat charge rate for provided management services, per month.
            Default: 0.0.
        monitored_service_price (Union[Unset, float]): Flat charge rate for provided monitoring services, per month.
            Default: 0.0.
        managed_vm_price (Union[Unset, float]): Charge rate for a managed VM, per month. Default: 0.0.
        managed_cdp_vm_price (Union[Unset, float]): Charge rate for a managed CDP VM, per month. Default: 0.0.
        managed_workstation_price (Union[Unset, float]): Charge rate for a managed workstation agent, per month.
            Default: 0.0.
        managed_server_agent_price (Union[Unset, float]): Charge rate for a managed server agent, per month. Default:
            0.0.
        free_managed_vms (Union[Unset, int]): Number of VMs that are managed for free. Default: 0.
        free_managed_cdp_vms (Union[Unset, int]): Number of CDP VMs that are managed for free. Default: 0.
        free_managed_workstations (Union[Unset, int]): Number of workstations that are managed for free. Default: 0.
        free_managed_server_agents (Union[Unset, int]): Number of server agents that are managed for free. Default: 0.
        windows_server_os_price (Union[Unset, float]): Extra charge rate for Microsoft Windows servers. Default: 0.0.
        windows_client_os_price (Union[Unset, float]): Extra charge rate for Microsoft Windows workstations. Default:
            0.0.
        linux_os_price (Union[Unset, float]): Extra charge rate for Linux computers. Default: 0.0.
        mac_os_price (Union[Unset, float]): Extra charge rate for Mac OS computers. Default: 0.0.
        backup_used_space_price (Union[Unset, float]): Charge rate for one GB or TB of backup repository space consumed
            by all non-cloud backups. Default: 0.0.
        backup_used_space_units (Union[Unset, SubscriptionPlanManagedBackupBackupUsedSpaceUnits]): Measurement units of
            backup repository space consumed by all non-cloud backups. Default:
            SubscriptionPlanManagedBackupBackupUsedSpaceUnits.GB.
        free_backup_used_space (Union[Unset, int]): Amount of backup repository space that can be consumed by all non-
            cloud backups for free.
            > Maximum value is `1048576` for GB and `1024` for TB.
        free_backup_used_space_units (Union[Unset, SubscriptionPlanManagedBackupFreeBackupUsedSpaceUnits]): Measurement
            units of backup repository space that can be consumed by all non-cloud backups for free. Default:
            SubscriptionPlanManagedBackupFreeBackupUsedSpaceUnits.GB.
        repository_space_usage_algorithm (Union[Unset, SubscriptionPlanManagedBackupRepositorySpaceUsageAlgorithm]):
            Type of charge rate for storage space on a repository. Default:
            SubscriptionPlanManagedBackupRepositorySpaceUsageAlgorithm.CONSUMED.
        repository_allocated_space_price (Union[Unset, float]): Charge rate for one GB or TB of allocated storage space
            on a repository. Default: 0.0.
        repository_allocated_space_units (Union[Unset, SubscriptionPlanManagedBackupRepositoryAllocatedSpaceUnits]):
            Measurement units of allocated storage space on a repository. Default:
            SubscriptionPlanManagedBackupRepositoryAllocatedSpaceUnits.GB.
        round_up_backup_used_space (Union[Unset, bool]): Indicates whether storage usage cost must be rounded up to a
            full data block cost when the consumed storage space does not match data block size. Default: False.
        backup_used_space_chunk_size (Union[Unset, int]): Size of a block of consumed storage space on a backup
            repository. Default: 1.
    """

    managed_service_price: Union[Unset, float] = 0.0
    monitored_service_price: Union[Unset, float] = 0.0
    managed_vm_price: Union[Unset, float] = 0.0
    managed_cdp_vm_price: Union[Unset, float] = 0.0
    managed_workstation_price: Union[Unset, float] = 0.0
    managed_server_agent_price: Union[Unset, float] = 0.0
    free_managed_vms: Union[Unset, int] = 0
    free_managed_cdp_vms: Union[Unset, int] = 0
    free_managed_workstations: Union[Unset, int] = 0
    free_managed_server_agents: Union[Unset, int] = 0
    windows_server_os_price: Union[Unset, float] = 0.0
    windows_client_os_price: Union[Unset, float] = 0.0
    linux_os_price: Union[Unset, float] = 0.0
    mac_os_price: Union[Unset, float] = 0.0
    backup_used_space_price: Union[Unset, float] = 0.0
    backup_used_space_units: Union[Unset, SubscriptionPlanManagedBackupBackupUsedSpaceUnits] = (
        SubscriptionPlanManagedBackupBackupUsedSpaceUnits.GB
    )
    free_backup_used_space: Union[Unset, int] = UNSET
    free_backup_used_space_units: Union[Unset, SubscriptionPlanManagedBackupFreeBackupUsedSpaceUnits] = (
        SubscriptionPlanManagedBackupFreeBackupUsedSpaceUnits.GB
    )
    repository_space_usage_algorithm: Union[Unset, SubscriptionPlanManagedBackupRepositorySpaceUsageAlgorithm] = (
        SubscriptionPlanManagedBackupRepositorySpaceUsageAlgorithm.CONSUMED
    )
    repository_allocated_space_price: Union[Unset, float] = 0.0
    repository_allocated_space_units: Union[Unset, SubscriptionPlanManagedBackupRepositoryAllocatedSpaceUnits] = (
        SubscriptionPlanManagedBackupRepositoryAllocatedSpaceUnits.GB
    )
    round_up_backup_used_space: Union[Unset, bool] = False
    backup_used_space_chunk_size: Union[Unset, int] = 1
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        managed_service_price = self.managed_service_price

        monitored_service_price = self.monitored_service_price

        managed_vm_price = self.managed_vm_price

        managed_cdp_vm_price = self.managed_cdp_vm_price

        managed_workstation_price = self.managed_workstation_price

        managed_server_agent_price = self.managed_server_agent_price

        free_managed_vms = self.free_managed_vms

        free_managed_cdp_vms = self.free_managed_cdp_vms

        free_managed_workstations = self.free_managed_workstations

        free_managed_server_agents = self.free_managed_server_agents

        windows_server_os_price = self.windows_server_os_price

        windows_client_os_price = self.windows_client_os_price

        linux_os_price = self.linux_os_price

        mac_os_price = self.mac_os_price

        backup_used_space_price = self.backup_used_space_price

        backup_used_space_units: Union[Unset, str] = UNSET
        if not isinstance(self.backup_used_space_units, Unset):
            backup_used_space_units = self.backup_used_space_units.value

        free_backup_used_space = self.free_backup_used_space

        free_backup_used_space_units: Union[Unset, str] = UNSET
        if not isinstance(self.free_backup_used_space_units, Unset):
            free_backup_used_space_units = self.free_backup_used_space_units.value

        repository_space_usage_algorithm: Union[Unset, str] = UNSET
        if not isinstance(self.repository_space_usage_algorithm, Unset):
            repository_space_usage_algorithm = self.repository_space_usage_algorithm.value

        repository_allocated_space_price = self.repository_allocated_space_price

        repository_allocated_space_units: Union[Unset, str] = UNSET
        if not isinstance(self.repository_allocated_space_units, Unset):
            repository_allocated_space_units = self.repository_allocated_space_units.value

        round_up_backup_used_space = self.round_up_backup_used_space

        backup_used_space_chunk_size = self.backup_used_space_chunk_size

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if managed_service_price is not UNSET:
            field_dict["managedServicePrice"] = managed_service_price
        if monitored_service_price is not UNSET:
            field_dict["monitoredServicePrice"] = monitored_service_price
        if managed_vm_price is not UNSET:
            field_dict["managedVmPrice"] = managed_vm_price
        if managed_cdp_vm_price is not UNSET:
            field_dict["managedCdpVmPrice"] = managed_cdp_vm_price
        if managed_workstation_price is not UNSET:
            field_dict["managedWorkstationPrice"] = managed_workstation_price
        if managed_server_agent_price is not UNSET:
            field_dict["managedServerAgentPrice"] = managed_server_agent_price
        if free_managed_vms is not UNSET:
            field_dict["freeManagedVms"] = free_managed_vms
        if free_managed_cdp_vms is not UNSET:
            field_dict["freeManagedCdpVms"] = free_managed_cdp_vms
        if free_managed_workstations is not UNSET:
            field_dict["freeManagedWorkstations"] = free_managed_workstations
        if free_managed_server_agents is not UNSET:
            field_dict["freeManagedServerAgents"] = free_managed_server_agents
        if windows_server_os_price is not UNSET:
            field_dict["windowsServerOsPrice"] = windows_server_os_price
        if windows_client_os_price is not UNSET:
            field_dict["windowsClientOsPrice"] = windows_client_os_price
        if linux_os_price is not UNSET:
            field_dict["linuxOsPrice"] = linux_os_price
        if mac_os_price is not UNSET:
            field_dict["macOsPrice"] = mac_os_price
        if backup_used_space_price is not UNSET:
            field_dict["backupUsedSpacePrice"] = backup_used_space_price
        if backup_used_space_units is not UNSET:
            field_dict["backupUsedSpaceUnits"] = backup_used_space_units
        if free_backup_used_space is not UNSET:
            field_dict["freeBackupUsedSpace"] = free_backup_used_space
        if free_backup_used_space_units is not UNSET:
            field_dict["freeBackupUsedSpaceUnits"] = free_backup_used_space_units
        if repository_space_usage_algorithm is not UNSET:
            field_dict["repositorySpaceUsageAlgorithm"] = repository_space_usage_algorithm
        if repository_allocated_space_price is not UNSET:
            field_dict["repositoryAllocatedSpacePrice"] = repository_allocated_space_price
        if repository_allocated_space_units is not UNSET:
            field_dict["repositoryAllocatedSpaceUnits"] = repository_allocated_space_units
        if round_up_backup_used_space is not UNSET:
            field_dict["roundUpBackupUsedSpace"] = round_up_backup_used_space
        if backup_used_space_chunk_size is not UNSET:
            field_dict["backupUsedSpaceChunkSize"] = backup_used_space_chunk_size

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        managed_service_price = d.pop("managedServicePrice", UNSET)

        monitored_service_price = d.pop("monitoredServicePrice", UNSET)

        managed_vm_price = d.pop("managedVmPrice", UNSET)

        managed_cdp_vm_price = d.pop("managedCdpVmPrice", UNSET)

        managed_workstation_price = d.pop("managedWorkstationPrice", UNSET)

        managed_server_agent_price = d.pop("managedServerAgentPrice", UNSET)

        free_managed_vms = d.pop("freeManagedVms", UNSET)

        free_managed_cdp_vms = d.pop("freeManagedCdpVms", UNSET)

        free_managed_workstations = d.pop("freeManagedWorkstations", UNSET)

        free_managed_server_agents = d.pop("freeManagedServerAgents", UNSET)

        windows_server_os_price = d.pop("windowsServerOsPrice", UNSET)

        windows_client_os_price = d.pop("windowsClientOsPrice", UNSET)

        linux_os_price = d.pop("linuxOsPrice", UNSET)

        mac_os_price = d.pop("macOsPrice", UNSET)

        backup_used_space_price = d.pop("backupUsedSpacePrice", UNSET)

        _backup_used_space_units = d.pop("backupUsedSpaceUnits", UNSET)
        backup_used_space_units: Union[Unset, SubscriptionPlanManagedBackupBackupUsedSpaceUnits]
        if isinstance(_backup_used_space_units, Unset):
            backup_used_space_units = UNSET
        else:
            backup_used_space_units = SubscriptionPlanManagedBackupBackupUsedSpaceUnits(_backup_used_space_units)

        free_backup_used_space = d.pop("freeBackupUsedSpace", UNSET)

        _free_backup_used_space_units = d.pop("freeBackupUsedSpaceUnits", UNSET)
        free_backup_used_space_units: Union[Unset, SubscriptionPlanManagedBackupFreeBackupUsedSpaceUnits]
        if isinstance(_free_backup_used_space_units, Unset):
            free_backup_used_space_units = UNSET
        else:
            free_backup_used_space_units = SubscriptionPlanManagedBackupFreeBackupUsedSpaceUnits(
                _free_backup_used_space_units
            )

        _repository_space_usage_algorithm = d.pop("repositorySpaceUsageAlgorithm", UNSET)
        repository_space_usage_algorithm: Union[Unset, SubscriptionPlanManagedBackupRepositorySpaceUsageAlgorithm]
        if isinstance(_repository_space_usage_algorithm, Unset):
            repository_space_usage_algorithm = UNSET
        else:
            repository_space_usage_algorithm = SubscriptionPlanManagedBackupRepositorySpaceUsageAlgorithm(
                _repository_space_usage_algorithm
            )

        repository_allocated_space_price = d.pop("repositoryAllocatedSpacePrice", UNSET)

        _repository_allocated_space_units = d.pop("repositoryAllocatedSpaceUnits", UNSET)
        repository_allocated_space_units: Union[Unset, SubscriptionPlanManagedBackupRepositoryAllocatedSpaceUnits]
        if isinstance(_repository_allocated_space_units, Unset):
            repository_allocated_space_units = UNSET
        else:
            repository_allocated_space_units = SubscriptionPlanManagedBackupRepositoryAllocatedSpaceUnits(
                _repository_allocated_space_units
            )

        round_up_backup_used_space = d.pop("roundUpBackupUsedSpace", UNSET)

        backup_used_space_chunk_size = d.pop("backupUsedSpaceChunkSize", UNSET)

        subscription_plan_managed_backup = cls(
            managed_service_price=managed_service_price,
            monitored_service_price=monitored_service_price,
            managed_vm_price=managed_vm_price,
            managed_cdp_vm_price=managed_cdp_vm_price,
            managed_workstation_price=managed_workstation_price,
            managed_server_agent_price=managed_server_agent_price,
            free_managed_vms=free_managed_vms,
            free_managed_cdp_vms=free_managed_cdp_vms,
            free_managed_workstations=free_managed_workstations,
            free_managed_server_agents=free_managed_server_agents,
            windows_server_os_price=windows_server_os_price,
            windows_client_os_price=windows_client_os_price,
            linux_os_price=linux_os_price,
            mac_os_price=mac_os_price,
            backup_used_space_price=backup_used_space_price,
            backup_used_space_units=backup_used_space_units,
            free_backup_used_space=free_backup_used_space,
            free_backup_used_space_units=free_backup_used_space_units,
            repository_space_usage_algorithm=repository_space_usage_algorithm,
            repository_allocated_space_price=repository_allocated_space_price,
            repository_allocated_space_units=repository_allocated_space_units,
            round_up_backup_used_space=round_up_backup_used_space,
            backup_used_space_chunk_size=backup_used_space_chunk_size,
        )

        subscription_plan_managed_backup.additional_properties = d
        return subscription_plan_managed_backup

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
