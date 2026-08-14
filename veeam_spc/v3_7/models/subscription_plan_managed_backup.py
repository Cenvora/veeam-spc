from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.subscription_plan_managed_backup_hosted_backup_used_space_units import (
    SubscriptionPlanManagedBackupHostedBackupUsedSpaceUnits,
)
from ..models.subscription_plan_managed_backup_hosted_free_backup_used_space_units import (
    SubscriptionPlanManagedBackupHostedFreeBackupUsedSpaceUnits,
)
from ..models.subscription_plan_managed_backup_hosted_repository_allocated_space_units import (
    SubscriptionPlanManagedBackupHostedRepositoryAllocatedSpaceUnits,
)
from ..models.subscription_plan_managed_backup_hosted_repository_space_usage_algorithm import (
    SubscriptionPlanManagedBackupHostedRepositorySpaceUsageAlgorithm,
)
from ..models.subscription_plan_managed_backup_remote_backup_used_space_units import (
    SubscriptionPlanManagedBackupRemoteBackupUsedSpaceUnits,
)
from ..models.subscription_plan_managed_backup_remote_free_backup_used_space_units import (
    SubscriptionPlanManagedBackupRemoteFreeBackupUsedSpaceUnits,
)
from ..models.subscription_plan_managed_backup_remote_repository_allocated_space_units import (
    SubscriptionPlanManagedBackupRemoteRepositoryAllocatedSpaceUnits,
)
from ..models.subscription_plan_managed_backup_remote_repository_space_usage_algorithm import (
    SubscriptionPlanManagedBackupRemoteRepositorySpaceUsageAlgorithm,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.subscription_plan_repository_usage_by_label import SubscriptionPlanRepositoryUsageByLabel


T = TypeVar("T", bound="SubscriptionPlanManagedBackup")


@_attrs_define
class SubscriptionPlanManagedBackup:
    """
    Attributes:
        managed_service_price (float | Unset): Flat charge rate for provided management services, per month. Default:
            0.0.
        monitored_service_price (float | Unset): Flat charge rate for provided monitoring services, per month. Default:
            0.0.
        remote_managed_vm_price (float | Unset): Charge rate for a managed remote VM, per month. Default: 0.0.
        remote_managed_cdp_vm_price (float | Unset): Charge rate for a managed remote CDP VM, per month. Default: 0.0.
        remote_managed_workstation_price (float | Unset): Charge rate for a managed remote workstation agent, per month.
            Default: 0.0.
        remote_managed_server_agent_price (float | Unset): Charge rate for a managed remote server agent, per month.
            Default: 0.0.
        remote_free_managed_vms (int | Unset): Number of remote VMs that are managed for free. Default: 0.
        remote_free_managed_cdp_vms (int | Unset): Number of remote CDP VMs that are managed for free. Default: 0.
        remote_free_managed_workstations (int | Unset): Number of remote workstations that are managed for free.
            Default: 0.
        remote_free_managed_server_agents (int | Unset): Number of remote server agents that are managed for free.
            Default: 0.
        remote_windows_server_os_price (float | Unset): Extra charge rate for remote Microsoft Windows servers. Default:
            0.0.
        remote_windows_client_os_price (float | Unset): Extra charge rate for remote Microsoft Windows workstations.
            Default: 0.0.
        remote_linux_os_price (float | Unset): Extra charge rate for remote Linux computers. Default: 0.0.
        remote_mac_os_price (float | Unset): Extra charge rate for remote Mac OS computers. Default: 0.0.
        remote_backup_used_space_price (float | Unset): Charge rate for one GB or TB of backup repository space consumed
            by all remote non-cloud backups. Default: 0.0.
        remote_backup_used_space_units (SubscriptionPlanManagedBackupRemoteBackupUsedSpaceUnits | Unset): Measurement
            units of backup repository space consumed by all remote non-cloud backups. Default:
            SubscriptionPlanManagedBackupRemoteBackupUsedSpaceUnits.GB.
        remote_free_backup_used_space (int | Unset): Amount of backup repository space that can be consumed by all
            remote non-cloud backups for free.
            > Maximum value is `1048576` for GB and `1024` for TB.
        remote_free_backup_used_space_units (SubscriptionPlanManagedBackupRemoteFreeBackupUsedSpaceUnits | Unset):
            Measurement units of backup repository space that can be consumed by all remote non-cloud backups for free.
            Default: SubscriptionPlanManagedBackupRemoteFreeBackupUsedSpaceUnits.GB.
        remote_repository_space_usage_algorithm (SubscriptionPlanManagedBackupRemoteRepositorySpaceUsageAlgorithm |
            Unset): Type of charge rate for repository storage space. Default:
            SubscriptionPlanManagedBackupRemoteRepositorySpaceUsageAlgorithm.CONSUMED.
        remote_repository_allocated_space_price (float | Unset): Charge rate for one GB or TB of storage space allocated
            to a remote Veeam Backup & Replication server. Default: 0.0.
        remote_repository_allocated_space_units (SubscriptionPlanManagedBackupRemoteRepositoryAllocatedSpaceUnits |
            Unset): Measurement units of storage space allocated to a remote Veeam Backup & Replication server. Default:
            SubscriptionPlanManagedBackupRemoteRepositoryAllocatedSpaceUnits.GB.
        remote_round_up_backup_used_space (bool | Unset): Indicates whether cost of storage used by remoste services
            must be rounded up to a full data block cost when the consumed storage space does not match data block size.
            Default: False.
        remote_backup_used_space_chunk_size (int | Unset): Size of a block of consumed storage space allocated to a
            remote Veeam Backup & Replication server. Default: 1.
        hosted_managed_vm_price (float | Unset): Charge rate for a managed hosted VM, per month. Default: 0.0.
        hosted_managed_cdp_vm_price (float | Unset): Charge rate for a managed hosted CDP VM, per month. Default: 0.0.
        hosted_managed_workstation_price (float | Unset): Charge rate for a managed hosted workstation agent, per month.
            Default: 0.0.
        hosted_managed_server_agent_price (float | Unset): Charge rate for a managed hosted server agent, per month.
            Default: 0.0.
        hosted_free_managed_vms (int | Unset): Number of hosted VMs that are managed for free. Default: 0.
        hosted_free_managed_cdp_vms (int | Unset): Number of hosted CDP VMs that are managed for free. Default: 0.
        hosted_free_managed_workstations (int | Unset): Number of hosted workstations that are managed for free.
            Default: 0.
        hosted_free_managed_server_agents (int | Unset): Number of hosted server agents that are managed for free.
            Default: 0.
        hosted_windows_server_os_price (float | Unset): Extra charge rate for hosted Microsoft Windows servers. Default:
            0.0.
        hosted_windows_client_os_price (float | Unset): Extra charge rate for hosted Microsoft Windows workstations.
            Default: 0.0.
        hosted_linux_os_price (float | Unset): Extra charge rate for hosted Linux computers. Default: 0.0.
        hosted_mac_os_price (float | Unset): Extra charge rate for hosted Mac OS computers. Default: 0.0.
        hosted_backup_used_space_price (float | Unset): Charge rate for one GB or TB of backup repository space consumed
            by all hosted non-cloud backups. Default: 0.0.
        hosted_backup_used_space_units (SubscriptionPlanManagedBackupHostedBackupUsedSpaceUnits | Unset): Measurement
            units of backup repository space consumed by all hosted non-cloud backups. Default:
            SubscriptionPlanManagedBackupHostedBackupUsedSpaceUnits.GB.
        hosted_free_backup_used_space (int | Unset): Amount of backup repository space that can be consumed by all non-
            cloud backups for free.
            > Maximum value is `1048576` for GB and `1024` for TB.
        hosted_free_backup_used_space_units (SubscriptionPlanManagedBackupHostedFreeBackupUsedSpaceUnits | Unset):
            Measurement units of backup repository space that can be consumed by all hosted non-cloud backups for free.
            Default: SubscriptionPlanManagedBackupHostedFreeBackupUsedSpaceUnits.GB.
        hosted_repository_space_usage_algorithm (SubscriptionPlanManagedBackupHostedRepositorySpaceUsageAlgorithm |
            Unset): Type of charge rate for repository storage space. Default:
            SubscriptionPlanManagedBackupHostedRepositorySpaceUsageAlgorithm.CONSUMED.
        hosted_repository_allocated_space_price (float | Unset): Charge rate for one GB or TB of repository storage
            space allocated to a hosted Veeam Backup & Replication server. Default: 0.0.
        hosted_repository_allocated_space_units (SubscriptionPlanManagedBackupHostedRepositoryAllocatedSpaceUnits |
            Unset): Measurement units of repository storage space allocated to a hosted Veeam Backup & Replication server.
            Default: SubscriptionPlanManagedBackupHostedRepositoryAllocatedSpaceUnits.GB.
        hosted_round_up_backup_used_space (bool | Unset): Indicates whether cost of storage used by hosted services must
            be rounded up to a full data block cost when the consumed storage space does not match data block size. Default:
            False.
        hosted_backup_used_space_chunk_size (int | Unset): Size of a block of repository storage space consumed by a
            hosted Veeam Backup & Replication server. Default: 1.
        use_repository_usage_by_label_hosted (bool | Unset): Enables per-label pricing for hosted backup repositories
            using `repositoryUsageByLabel.hosted` entries. Requires `hostedRepositorySpaceUsageAlgorithm` to be `Consumed`;
            repositories without an assigned label fall back to the Consumed-mode fields as an "Unspecified" bucket.
            Default: False.
        use_repository_usage_by_label_remote (bool | Unset): Enables per-label pricing for remote backup repositories
            using `repositoryUsageByLabel.remote` entries. Requires `remoteRepositorySpaceUsageAlgorithm` to be `Consumed`;
            repositories without an assigned label fall back to the Consumed-mode fields as an "Unspecified" bucket.
            Default: False.
        repository_usage_by_label (SubscriptionPlanRepositoryUsageByLabel | Unset):
    """

    managed_service_price: float | Unset = 0.0
    monitored_service_price: float | Unset = 0.0
    remote_managed_vm_price: float | Unset = 0.0
    remote_managed_cdp_vm_price: float | Unset = 0.0
    remote_managed_workstation_price: float | Unset = 0.0
    remote_managed_server_agent_price: float | Unset = 0.0
    remote_free_managed_vms: int | Unset = 0
    remote_free_managed_cdp_vms: int | Unset = 0
    remote_free_managed_workstations: int | Unset = 0
    remote_free_managed_server_agents: int | Unset = 0
    remote_windows_server_os_price: float | Unset = 0.0
    remote_windows_client_os_price: float | Unset = 0.0
    remote_linux_os_price: float | Unset = 0.0
    remote_mac_os_price: float | Unset = 0.0
    remote_backup_used_space_price: float | Unset = 0.0
    remote_backup_used_space_units: SubscriptionPlanManagedBackupRemoteBackupUsedSpaceUnits | Unset = (
        SubscriptionPlanManagedBackupRemoteBackupUsedSpaceUnits.GB
    )
    remote_free_backup_used_space: int | Unset = UNSET
    remote_free_backup_used_space_units: SubscriptionPlanManagedBackupRemoteFreeBackupUsedSpaceUnits | Unset = (
        SubscriptionPlanManagedBackupRemoteFreeBackupUsedSpaceUnits.GB
    )
    remote_repository_space_usage_algorithm: (
        SubscriptionPlanManagedBackupRemoteRepositorySpaceUsageAlgorithm | Unset
    ) = SubscriptionPlanManagedBackupRemoteRepositorySpaceUsageAlgorithm.CONSUMED
    remote_repository_allocated_space_price: float | Unset = 0.0
    remote_repository_allocated_space_units: (
        SubscriptionPlanManagedBackupRemoteRepositoryAllocatedSpaceUnits | Unset
    ) = SubscriptionPlanManagedBackupRemoteRepositoryAllocatedSpaceUnits.GB
    remote_round_up_backup_used_space: bool | Unset = False
    remote_backup_used_space_chunk_size: int | Unset = 1
    hosted_managed_vm_price: float | Unset = 0.0
    hosted_managed_cdp_vm_price: float | Unset = 0.0
    hosted_managed_workstation_price: float | Unset = 0.0
    hosted_managed_server_agent_price: float | Unset = 0.0
    hosted_free_managed_vms: int | Unset = 0
    hosted_free_managed_cdp_vms: int | Unset = 0
    hosted_free_managed_workstations: int | Unset = 0
    hosted_free_managed_server_agents: int | Unset = 0
    hosted_windows_server_os_price: float | Unset = 0.0
    hosted_windows_client_os_price: float | Unset = 0.0
    hosted_linux_os_price: float | Unset = 0.0
    hosted_mac_os_price: float | Unset = 0.0
    hosted_backup_used_space_price: float | Unset = 0.0
    hosted_backup_used_space_units: SubscriptionPlanManagedBackupHostedBackupUsedSpaceUnits | Unset = (
        SubscriptionPlanManagedBackupHostedBackupUsedSpaceUnits.GB
    )
    hosted_free_backup_used_space: int | Unset = UNSET
    hosted_free_backup_used_space_units: SubscriptionPlanManagedBackupHostedFreeBackupUsedSpaceUnits | Unset = (
        SubscriptionPlanManagedBackupHostedFreeBackupUsedSpaceUnits.GB
    )
    hosted_repository_space_usage_algorithm: (
        SubscriptionPlanManagedBackupHostedRepositorySpaceUsageAlgorithm | Unset
    ) = SubscriptionPlanManagedBackupHostedRepositorySpaceUsageAlgorithm.CONSUMED
    hosted_repository_allocated_space_price: float | Unset = 0.0
    hosted_repository_allocated_space_units: (
        SubscriptionPlanManagedBackupHostedRepositoryAllocatedSpaceUnits | Unset
    ) = SubscriptionPlanManagedBackupHostedRepositoryAllocatedSpaceUnits.GB
    hosted_round_up_backup_used_space: bool | Unset = False
    hosted_backup_used_space_chunk_size: int | Unset = 1
    use_repository_usage_by_label_hosted: bool | Unset = False
    use_repository_usage_by_label_remote: bool | Unset = False
    repository_usage_by_label: SubscriptionPlanRepositoryUsageByLabel | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        managed_service_price = self.managed_service_price

        monitored_service_price = self.monitored_service_price

        remote_managed_vm_price = self.remote_managed_vm_price

        remote_managed_cdp_vm_price = self.remote_managed_cdp_vm_price

        remote_managed_workstation_price = self.remote_managed_workstation_price

        remote_managed_server_agent_price = self.remote_managed_server_agent_price

        remote_free_managed_vms = self.remote_free_managed_vms

        remote_free_managed_cdp_vms = self.remote_free_managed_cdp_vms

        remote_free_managed_workstations = self.remote_free_managed_workstations

        remote_free_managed_server_agents = self.remote_free_managed_server_agents

        remote_windows_server_os_price = self.remote_windows_server_os_price

        remote_windows_client_os_price = self.remote_windows_client_os_price

        remote_linux_os_price = self.remote_linux_os_price

        remote_mac_os_price = self.remote_mac_os_price

        remote_backup_used_space_price = self.remote_backup_used_space_price

        remote_backup_used_space_units: str | Unset = UNSET
        if not isinstance(self.remote_backup_used_space_units, Unset):
            remote_backup_used_space_units = self.remote_backup_used_space_units.value

        remote_free_backup_used_space = self.remote_free_backup_used_space

        remote_free_backup_used_space_units: str | Unset = UNSET
        if not isinstance(self.remote_free_backup_used_space_units, Unset):
            remote_free_backup_used_space_units = self.remote_free_backup_used_space_units.value

        remote_repository_space_usage_algorithm: str | Unset = UNSET
        if not isinstance(self.remote_repository_space_usage_algorithm, Unset):
            remote_repository_space_usage_algorithm = self.remote_repository_space_usage_algorithm.value

        remote_repository_allocated_space_price = self.remote_repository_allocated_space_price

        remote_repository_allocated_space_units: str | Unset = UNSET
        if not isinstance(self.remote_repository_allocated_space_units, Unset):
            remote_repository_allocated_space_units = self.remote_repository_allocated_space_units.value

        remote_round_up_backup_used_space = self.remote_round_up_backup_used_space

        remote_backup_used_space_chunk_size = self.remote_backup_used_space_chunk_size

        hosted_managed_vm_price = self.hosted_managed_vm_price

        hosted_managed_cdp_vm_price = self.hosted_managed_cdp_vm_price

        hosted_managed_workstation_price = self.hosted_managed_workstation_price

        hosted_managed_server_agent_price = self.hosted_managed_server_agent_price

        hosted_free_managed_vms = self.hosted_free_managed_vms

        hosted_free_managed_cdp_vms = self.hosted_free_managed_cdp_vms

        hosted_free_managed_workstations = self.hosted_free_managed_workstations

        hosted_free_managed_server_agents = self.hosted_free_managed_server_agents

        hosted_windows_server_os_price = self.hosted_windows_server_os_price

        hosted_windows_client_os_price = self.hosted_windows_client_os_price

        hosted_linux_os_price = self.hosted_linux_os_price

        hosted_mac_os_price = self.hosted_mac_os_price

        hosted_backup_used_space_price = self.hosted_backup_used_space_price

        hosted_backup_used_space_units: str | Unset = UNSET
        if not isinstance(self.hosted_backup_used_space_units, Unset):
            hosted_backup_used_space_units = self.hosted_backup_used_space_units.value

        hosted_free_backup_used_space = self.hosted_free_backup_used_space

        hosted_free_backup_used_space_units: str | Unset = UNSET
        if not isinstance(self.hosted_free_backup_used_space_units, Unset):
            hosted_free_backup_used_space_units = self.hosted_free_backup_used_space_units.value

        hosted_repository_space_usage_algorithm: str | Unset = UNSET
        if not isinstance(self.hosted_repository_space_usage_algorithm, Unset):
            hosted_repository_space_usage_algorithm = self.hosted_repository_space_usage_algorithm.value

        hosted_repository_allocated_space_price = self.hosted_repository_allocated_space_price

        hosted_repository_allocated_space_units: str | Unset = UNSET
        if not isinstance(self.hosted_repository_allocated_space_units, Unset):
            hosted_repository_allocated_space_units = self.hosted_repository_allocated_space_units.value

        hosted_round_up_backup_used_space = self.hosted_round_up_backup_used_space

        hosted_backup_used_space_chunk_size = self.hosted_backup_used_space_chunk_size

        use_repository_usage_by_label_hosted = self.use_repository_usage_by_label_hosted

        use_repository_usage_by_label_remote = self.use_repository_usage_by_label_remote

        repository_usage_by_label: dict[str, Any] | Unset = UNSET
        if not isinstance(self.repository_usage_by_label, Unset):
            repository_usage_by_label = self.repository_usage_by_label.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if managed_service_price is not UNSET:
            field_dict["managedServicePrice"] = managed_service_price
        if monitored_service_price is not UNSET:
            field_dict["monitoredServicePrice"] = monitored_service_price
        if remote_managed_vm_price is not UNSET:
            field_dict["remoteManagedVmPrice"] = remote_managed_vm_price
        if remote_managed_cdp_vm_price is not UNSET:
            field_dict["remoteManagedCdpVmPrice"] = remote_managed_cdp_vm_price
        if remote_managed_workstation_price is not UNSET:
            field_dict["remoteManagedWorkstationPrice"] = remote_managed_workstation_price
        if remote_managed_server_agent_price is not UNSET:
            field_dict["remoteManagedServerAgentPrice"] = remote_managed_server_agent_price
        if remote_free_managed_vms is not UNSET:
            field_dict["remoteFreeManagedVms"] = remote_free_managed_vms
        if remote_free_managed_cdp_vms is not UNSET:
            field_dict["remoteFreeManagedCdpVms"] = remote_free_managed_cdp_vms
        if remote_free_managed_workstations is not UNSET:
            field_dict["remoteFreeManagedWorkstations"] = remote_free_managed_workstations
        if remote_free_managed_server_agents is not UNSET:
            field_dict["remoteFreeManagedServerAgents"] = remote_free_managed_server_agents
        if remote_windows_server_os_price is not UNSET:
            field_dict["remoteWindowsServerOsPrice"] = remote_windows_server_os_price
        if remote_windows_client_os_price is not UNSET:
            field_dict["remoteWindowsClientOsPrice"] = remote_windows_client_os_price
        if remote_linux_os_price is not UNSET:
            field_dict["remoteLinuxOsPrice"] = remote_linux_os_price
        if remote_mac_os_price is not UNSET:
            field_dict["remoteMacOsPrice"] = remote_mac_os_price
        if remote_backup_used_space_price is not UNSET:
            field_dict["remoteBackupUsedSpacePrice"] = remote_backup_used_space_price
        if remote_backup_used_space_units is not UNSET:
            field_dict["remoteBackupUsedSpaceUnits"] = remote_backup_used_space_units
        if remote_free_backup_used_space is not UNSET:
            field_dict["remoteFreeBackupUsedSpace"] = remote_free_backup_used_space
        if remote_free_backup_used_space_units is not UNSET:
            field_dict["remoteFreeBackupUsedSpaceUnits"] = remote_free_backup_used_space_units
        if remote_repository_space_usage_algorithm is not UNSET:
            field_dict["remoteRepositorySpaceUsageAlgorithm"] = remote_repository_space_usage_algorithm
        if remote_repository_allocated_space_price is not UNSET:
            field_dict["remoteRepositoryAllocatedSpacePrice"] = remote_repository_allocated_space_price
        if remote_repository_allocated_space_units is not UNSET:
            field_dict["remoteRepositoryAllocatedSpaceUnits"] = remote_repository_allocated_space_units
        if remote_round_up_backup_used_space is not UNSET:
            field_dict["remoteRoundUpBackupUsedSpace"] = remote_round_up_backup_used_space
        if remote_backup_used_space_chunk_size is not UNSET:
            field_dict["remoteBackupUsedSpaceChunkSize"] = remote_backup_used_space_chunk_size
        if hosted_managed_vm_price is not UNSET:
            field_dict["hostedManagedVmPrice"] = hosted_managed_vm_price
        if hosted_managed_cdp_vm_price is not UNSET:
            field_dict["hostedManagedCdpVmPrice"] = hosted_managed_cdp_vm_price
        if hosted_managed_workstation_price is not UNSET:
            field_dict["hostedManagedWorkstationPrice"] = hosted_managed_workstation_price
        if hosted_managed_server_agent_price is not UNSET:
            field_dict["hostedManagedServerAgentPrice"] = hosted_managed_server_agent_price
        if hosted_free_managed_vms is not UNSET:
            field_dict["hostedFreeManagedVms"] = hosted_free_managed_vms
        if hosted_free_managed_cdp_vms is not UNSET:
            field_dict["hostedFreeManagedCdpVms"] = hosted_free_managed_cdp_vms
        if hosted_free_managed_workstations is not UNSET:
            field_dict["hostedFreeManagedWorkstations"] = hosted_free_managed_workstations
        if hosted_free_managed_server_agents is not UNSET:
            field_dict["hostedFreeManagedServerAgents"] = hosted_free_managed_server_agents
        if hosted_windows_server_os_price is not UNSET:
            field_dict["hostedWindowsServerOsPrice"] = hosted_windows_server_os_price
        if hosted_windows_client_os_price is not UNSET:
            field_dict["hostedWindowsClientOsPrice"] = hosted_windows_client_os_price
        if hosted_linux_os_price is not UNSET:
            field_dict["hostedLinuxOsPrice"] = hosted_linux_os_price
        if hosted_mac_os_price is not UNSET:
            field_dict["hostedMacOsPrice"] = hosted_mac_os_price
        if hosted_backup_used_space_price is not UNSET:
            field_dict["hostedBackupUsedSpacePrice"] = hosted_backup_used_space_price
        if hosted_backup_used_space_units is not UNSET:
            field_dict["hostedBackupUsedSpaceUnits"] = hosted_backup_used_space_units
        if hosted_free_backup_used_space is not UNSET:
            field_dict["hostedFreeBackupUsedSpace"] = hosted_free_backup_used_space
        if hosted_free_backup_used_space_units is not UNSET:
            field_dict["hostedFreeBackupUsedSpaceUnits"] = hosted_free_backup_used_space_units
        if hosted_repository_space_usage_algorithm is not UNSET:
            field_dict["hostedRepositorySpaceUsageAlgorithm"] = hosted_repository_space_usage_algorithm
        if hosted_repository_allocated_space_price is not UNSET:
            field_dict["hostedRepositoryAllocatedSpacePrice"] = hosted_repository_allocated_space_price
        if hosted_repository_allocated_space_units is not UNSET:
            field_dict["hostedRepositoryAllocatedSpaceUnits"] = hosted_repository_allocated_space_units
        if hosted_round_up_backup_used_space is not UNSET:
            field_dict["hostedRoundUpBackupUsedSpace"] = hosted_round_up_backup_used_space
        if hosted_backup_used_space_chunk_size is not UNSET:
            field_dict["hostedBackupUsedSpaceChunkSize"] = hosted_backup_used_space_chunk_size
        if use_repository_usage_by_label_hosted is not UNSET:
            field_dict["useRepositoryUsageByLabelHosted"] = use_repository_usage_by_label_hosted
        if use_repository_usage_by_label_remote is not UNSET:
            field_dict["useRepositoryUsageByLabelRemote"] = use_repository_usage_by_label_remote
        if repository_usage_by_label is not UNSET:
            field_dict["repositoryUsageByLabel"] = repository_usage_by_label

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.subscription_plan_repository_usage_by_label import SubscriptionPlanRepositoryUsageByLabel

        d = dict(src_dict)
        managed_service_price = d.pop("managedServicePrice", UNSET)

        monitored_service_price = d.pop("monitoredServicePrice", UNSET)

        remote_managed_vm_price = d.pop("remoteManagedVmPrice", UNSET)

        remote_managed_cdp_vm_price = d.pop("remoteManagedCdpVmPrice", UNSET)

        remote_managed_workstation_price = d.pop("remoteManagedWorkstationPrice", UNSET)

        remote_managed_server_agent_price = d.pop("remoteManagedServerAgentPrice", UNSET)

        remote_free_managed_vms = d.pop("remoteFreeManagedVms", UNSET)

        remote_free_managed_cdp_vms = d.pop("remoteFreeManagedCdpVms", UNSET)

        remote_free_managed_workstations = d.pop("remoteFreeManagedWorkstations", UNSET)

        remote_free_managed_server_agents = d.pop("remoteFreeManagedServerAgents", UNSET)

        remote_windows_server_os_price = d.pop("remoteWindowsServerOsPrice", UNSET)

        remote_windows_client_os_price = d.pop("remoteWindowsClientOsPrice", UNSET)

        remote_linux_os_price = d.pop("remoteLinuxOsPrice", UNSET)

        remote_mac_os_price = d.pop("remoteMacOsPrice", UNSET)

        remote_backup_used_space_price = d.pop("remoteBackupUsedSpacePrice", UNSET)

        _remote_backup_used_space_units = d.pop("remoteBackupUsedSpaceUnits", UNSET)
        remote_backup_used_space_units: SubscriptionPlanManagedBackupRemoteBackupUsedSpaceUnits | Unset
        if isinstance(_remote_backup_used_space_units, Unset):
            remote_backup_used_space_units = UNSET
        else:
            remote_backup_used_space_units = SubscriptionPlanManagedBackupRemoteBackupUsedSpaceUnits(
                _remote_backup_used_space_units
            )

        remote_free_backup_used_space = d.pop("remoteFreeBackupUsedSpace", UNSET)

        _remote_free_backup_used_space_units = d.pop("remoteFreeBackupUsedSpaceUnits", UNSET)
        remote_free_backup_used_space_units: SubscriptionPlanManagedBackupRemoteFreeBackupUsedSpaceUnits | Unset
        if isinstance(_remote_free_backup_used_space_units, Unset):
            remote_free_backup_used_space_units = UNSET
        else:
            remote_free_backup_used_space_units = SubscriptionPlanManagedBackupRemoteFreeBackupUsedSpaceUnits(
                _remote_free_backup_used_space_units
            )

        _remote_repository_space_usage_algorithm = d.pop("remoteRepositorySpaceUsageAlgorithm", UNSET)
        remote_repository_space_usage_algorithm: (
            SubscriptionPlanManagedBackupRemoteRepositorySpaceUsageAlgorithm | Unset
        )
        if isinstance(_remote_repository_space_usage_algorithm, Unset):
            remote_repository_space_usage_algorithm = UNSET
        else:
            remote_repository_space_usage_algorithm = SubscriptionPlanManagedBackupRemoteRepositorySpaceUsageAlgorithm(
                _remote_repository_space_usage_algorithm
            )

        remote_repository_allocated_space_price = d.pop("remoteRepositoryAllocatedSpacePrice", UNSET)

        _remote_repository_allocated_space_units = d.pop("remoteRepositoryAllocatedSpaceUnits", UNSET)
        remote_repository_allocated_space_units: (
            SubscriptionPlanManagedBackupRemoteRepositoryAllocatedSpaceUnits | Unset
        )
        if isinstance(_remote_repository_allocated_space_units, Unset):
            remote_repository_allocated_space_units = UNSET
        else:
            remote_repository_allocated_space_units = SubscriptionPlanManagedBackupRemoteRepositoryAllocatedSpaceUnits(
                _remote_repository_allocated_space_units
            )

        remote_round_up_backup_used_space = d.pop("remoteRoundUpBackupUsedSpace", UNSET)

        remote_backup_used_space_chunk_size = d.pop("remoteBackupUsedSpaceChunkSize", UNSET)

        hosted_managed_vm_price = d.pop("hostedManagedVmPrice", UNSET)

        hosted_managed_cdp_vm_price = d.pop("hostedManagedCdpVmPrice", UNSET)

        hosted_managed_workstation_price = d.pop("hostedManagedWorkstationPrice", UNSET)

        hosted_managed_server_agent_price = d.pop("hostedManagedServerAgentPrice", UNSET)

        hosted_free_managed_vms = d.pop("hostedFreeManagedVms", UNSET)

        hosted_free_managed_cdp_vms = d.pop("hostedFreeManagedCdpVms", UNSET)

        hosted_free_managed_workstations = d.pop("hostedFreeManagedWorkstations", UNSET)

        hosted_free_managed_server_agents = d.pop("hostedFreeManagedServerAgents", UNSET)

        hosted_windows_server_os_price = d.pop("hostedWindowsServerOsPrice", UNSET)

        hosted_windows_client_os_price = d.pop("hostedWindowsClientOsPrice", UNSET)

        hosted_linux_os_price = d.pop("hostedLinuxOsPrice", UNSET)

        hosted_mac_os_price = d.pop("hostedMacOsPrice", UNSET)

        hosted_backup_used_space_price = d.pop("hostedBackupUsedSpacePrice", UNSET)

        _hosted_backup_used_space_units = d.pop("hostedBackupUsedSpaceUnits", UNSET)
        hosted_backup_used_space_units: SubscriptionPlanManagedBackupHostedBackupUsedSpaceUnits | Unset
        if isinstance(_hosted_backup_used_space_units, Unset):
            hosted_backup_used_space_units = UNSET
        else:
            hosted_backup_used_space_units = SubscriptionPlanManagedBackupHostedBackupUsedSpaceUnits(
                _hosted_backup_used_space_units
            )

        hosted_free_backup_used_space = d.pop("hostedFreeBackupUsedSpace", UNSET)

        _hosted_free_backup_used_space_units = d.pop("hostedFreeBackupUsedSpaceUnits", UNSET)
        hosted_free_backup_used_space_units: SubscriptionPlanManagedBackupHostedFreeBackupUsedSpaceUnits | Unset
        if isinstance(_hosted_free_backup_used_space_units, Unset):
            hosted_free_backup_used_space_units = UNSET
        else:
            hosted_free_backup_used_space_units = SubscriptionPlanManagedBackupHostedFreeBackupUsedSpaceUnits(
                _hosted_free_backup_used_space_units
            )

        _hosted_repository_space_usage_algorithm = d.pop("hostedRepositorySpaceUsageAlgorithm", UNSET)
        hosted_repository_space_usage_algorithm: (
            SubscriptionPlanManagedBackupHostedRepositorySpaceUsageAlgorithm | Unset
        )
        if isinstance(_hosted_repository_space_usage_algorithm, Unset):
            hosted_repository_space_usage_algorithm = UNSET
        else:
            hosted_repository_space_usage_algorithm = SubscriptionPlanManagedBackupHostedRepositorySpaceUsageAlgorithm(
                _hosted_repository_space_usage_algorithm
            )

        hosted_repository_allocated_space_price = d.pop("hostedRepositoryAllocatedSpacePrice", UNSET)

        _hosted_repository_allocated_space_units = d.pop("hostedRepositoryAllocatedSpaceUnits", UNSET)
        hosted_repository_allocated_space_units: (
            SubscriptionPlanManagedBackupHostedRepositoryAllocatedSpaceUnits | Unset
        )
        if isinstance(_hosted_repository_allocated_space_units, Unset):
            hosted_repository_allocated_space_units = UNSET
        else:
            hosted_repository_allocated_space_units = SubscriptionPlanManagedBackupHostedRepositoryAllocatedSpaceUnits(
                _hosted_repository_allocated_space_units
            )

        hosted_round_up_backup_used_space = d.pop("hostedRoundUpBackupUsedSpace", UNSET)

        hosted_backup_used_space_chunk_size = d.pop("hostedBackupUsedSpaceChunkSize", UNSET)

        use_repository_usage_by_label_hosted = d.pop("useRepositoryUsageByLabelHosted", UNSET)

        use_repository_usage_by_label_remote = d.pop("useRepositoryUsageByLabelRemote", UNSET)

        _repository_usage_by_label = d.pop("repositoryUsageByLabel", UNSET)
        repository_usage_by_label: SubscriptionPlanRepositoryUsageByLabel | Unset
        if isinstance(_repository_usage_by_label, Unset):
            repository_usage_by_label = UNSET
        else:
            repository_usage_by_label = SubscriptionPlanRepositoryUsageByLabel.from_dict(_repository_usage_by_label)

        subscription_plan_managed_backup = cls(
            managed_service_price=managed_service_price,
            monitored_service_price=monitored_service_price,
            remote_managed_vm_price=remote_managed_vm_price,
            remote_managed_cdp_vm_price=remote_managed_cdp_vm_price,
            remote_managed_workstation_price=remote_managed_workstation_price,
            remote_managed_server_agent_price=remote_managed_server_agent_price,
            remote_free_managed_vms=remote_free_managed_vms,
            remote_free_managed_cdp_vms=remote_free_managed_cdp_vms,
            remote_free_managed_workstations=remote_free_managed_workstations,
            remote_free_managed_server_agents=remote_free_managed_server_agents,
            remote_windows_server_os_price=remote_windows_server_os_price,
            remote_windows_client_os_price=remote_windows_client_os_price,
            remote_linux_os_price=remote_linux_os_price,
            remote_mac_os_price=remote_mac_os_price,
            remote_backup_used_space_price=remote_backup_used_space_price,
            remote_backup_used_space_units=remote_backup_used_space_units,
            remote_free_backup_used_space=remote_free_backup_used_space,
            remote_free_backup_used_space_units=remote_free_backup_used_space_units,
            remote_repository_space_usage_algorithm=remote_repository_space_usage_algorithm,
            remote_repository_allocated_space_price=remote_repository_allocated_space_price,
            remote_repository_allocated_space_units=remote_repository_allocated_space_units,
            remote_round_up_backup_used_space=remote_round_up_backup_used_space,
            remote_backup_used_space_chunk_size=remote_backup_used_space_chunk_size,
            hosted_managed_vm_price=hosted_managed_vm_price,
            hosted_managed_cdp_vm_price=hosted_managed_cdp_vm_price,
            hosted_managed_workstation_price=hosted_managed_workstation_price,
            hosted_managed_server_agent_price=hosted_managed_server_agent_price,
            hosted_free_managed_vms=hosted_free_managed_vms,
            hosted_free_managed_cdp_vms=hosted_free_managed_cdp_vms,
            hosted_free_managed_workstations=hosted_free_managed_workstations,
            hosted_free_managed_server_agents=hosted_free_managed_server_agents,
            hosted_windows_server_os_price=hosted_windows_server_os_price,
            hosted_windows_client_os_price=hosted_windows_client_os_price,
            hosted_linux_os_price=hosted_linux_os_price,
            hosted_mac_os_price=hosted_mac_os_price,
            hosted_backup_used_space_price=hosted_backup_used_space_price,
            hosted_backup_used_space_units=hosted_backup_used_space_units,
            hosted_free_backup_used_space=hosted_free_backup_used_space,
            hosted_free_backup_used_space_units=hosted_free_backup_used_space_units,
            hosted_repository_space_usage_algorithm=hosted_repository_space_usage_algorithm,
            hosted_repository_allocated_space_price=hosted_repository_allocated_space_price,
            hosted_repository_allocated_space_units=hosted_repository_allocated_space_units,
            hosted_round_up_backup_used_space=hosted_round_up_backup_used_space,
            hosted_backup_used_space_chunk_size=hosted_backup_used_space_chunk_size,
            use_repository_usage_by_label_hosted=use_repository_usage_by_label_hosted,
            use_repository_usage_by_label_remote=use_repository_usage_by_label_remote,
            repository_usage_by_label=repository_usage_by_label,
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
