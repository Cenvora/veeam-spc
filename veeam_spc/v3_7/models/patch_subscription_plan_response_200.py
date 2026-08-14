from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.response_error import ResponseError
    from ..models.response_metadata import ResponseMetadata
    from ..models.subscription_plan import SubscriptionPlan


T = TypeVar("T", bound="PatchSubscriptionPlanResponse200")


@_attrs_define
class PatchSubscriptionPlanResponse200:
    """
    Attributes:
        data (SubscriptionPlan):  Example: {'name': 'Pittsburgh subscription plan', 'description': 'Subscription plan
            for Pittsburgh clients', 'currency': 'USD', 'taxType': 'VAT', 'taxPercent': 10, 'discountPercent': 12,
            'managedBackup': {'managedServicePrice': 21, 'monitoredServicePrice': 0, 'remoteManagedVmPrice': 0,
            'remoteManagedCdpVmPrice': 0, 'remoteManagedWorkstationPrice': 0, 'remoteManagedServerAgentPrice': 0,
            'remoteFreeManagedVms': 0, 'remoteFreeManagedCdpVms': 0, 'remoteFreeManagedWorkstations': 0,
            'remoteFreeManagedServerAgents': 0, 'remoteWindowsServerOsPrice': 0, 'remoteWindowsClientOsPrice': 0,
            'remoteLinuxOsPrice': 0, 'remoteMacOsPrice': 0, 'remoteBackupUsedSpacePrice': 0, 'remoteBackupUsedSpaceUnits':
            'GB', 'remoteFreeBackupUsedSpace': None, 'remoteFreeBackupUsedSpaceUnits': 'GB',
            'remoteRepositorySpaceUsageAlgorithm': 'Consumed', 'remoteRepositoryAllocatedSpacePrice': 0,
            'remoteRepositoryAllocatedSpaceUnits': 'GB', 'remoteRoundUpBackupUsedSpace': False,
            'remoteBackupUsedSpaceChunkSize': 1, 'hostedManagedVmPrice': 0, 'hostedManagedCdpVmPrice': 0,
            'hostedManagedWorkstationPrice': 0, 'hostedManagedServerAgentPrice': 0, 'hostedFreeManagedVms': 0,
            'hostedFreeManagedCdpVms': 0, 'hostedFreeManagedWorkstations': 0, 'hostedFreeManagedServerAgents': 0,
            'hostedWindowsServerOsPrice': 0, 'hostedWindowsClientOsPrice': 0, 'hostedLinuxOsPrice': 0, 'hostedMacOsPrice':
            0, 'hostedBackupUsedSpacePrice': 0, 'hostedBackupUsedSpaceUnits': 'GB', 'hostedFreeBackupUsedSpace': None,
            'hostedFreeBackupUsedSpaceUnits': 'GB', 'hostedRepositorySpaceUsageAlgorithm': 'Consumed',
            'hostedRepositoryAllocatedSpacePrice': 0, 'hostedRepositoryAllocatedSpaceUnits': 'GB',
            'hostedRoundUpBackupUsedSpace': False, 'hostedBackupUsedSpaceChunkSize': 1, 'useRepositoryUsageByLabelHosted':
            True, 'useRepositoryUsageByLabelRemote': False, 'repositoryUsageByLabel': {'hosted': [{'labelUid':
            '8f3c9d21-5b47-4e6a-9c12-7d8a0f4b1e63', 'price': 12, 'priceMeasure': 'TB', 'freeOfCharge': 100,
            'freeOfChargeMeasure': 'GB', 'chunkSize': 1, 'roundUpPerChunk': True, 'enabled': True}], 'remote': []}},
            'publicCloud': {'remoteCloudVmPrice': 0, 'remoteFreeCloudVms': 0, 'remoteCloudFileSharePrice': 0,
            'remoteFreeCloudFileShares': 0, 'remoteCloudDatabasePrice': 0, 'remoteFreeCloudDatabases': 0,
            'remoteCloudNetworkPrice': 0, 'remoteBackupUsedSpacePrice': 0, 'remoteBackupUsedSpaceUnits': 'GB',
            'remoteFreeBackupUsedSpace': None, 'remoteFreeBackupUsedSpaceUnits': 'GB', 'remoteArchiveUsedSpacePrice': 0,
            'remoteArchiveUsedSpaceUnits': 'GB', 'remoteFreeArchiveUsedSpace': None, 'remoteFreeArchiveUsedSpaceUnits':
            'GB', 'hostedCloudVmPrice': 0, 'hostedFreeCloudVms': 0, 'hostedCloudFileSharePrice': 0,
            'hostedFreeCloudFileShares': 0, 'hostedCloudDatabasePrice': 0, 'hostedFreeCloudDatabases': 0,
            'hostedCloudNetworkPrice': 0, 'hostedBackupUsedSpacePrice': 0, 'hostedBackupUsedSpaceUnits': 'GB',
            'hostedFreeBackupUsedSpace': None, 'hostedFreeBackupUsedSpaceUnits': 'GB', 'hostedArchiveUsedSpacePrice': 0,
            'hostedArchiveUsedSpaceUnits': 'GB', 'hostedFreeArchiveUsedSpace': None, 'hostedFreeArchiveUsedSpaceUnits':
            'GB'}, 'vb365': {'remoteSubscriptionUserPrice': 0, 'remoteFreeSubscriptionUsers': 0,
            'remoteEducationalUserPrice': 0, 'remoteFreeEducationalUsers': 0, 'remoteRoundUpUsedSpace': False,
            'remoteStandardStorageUsedSpacePrice': 0, 'remoteStandardStorageUsedSpaceChunkSize': 1,
            'remoteStandardStorageUsedSpaceUnits': 'GB', 'remoteFreeStandardStorageUsedSpace': None,
            'remoteFreeStandardStorageUsedSpaceUnits': 'GB', 'remoteArchiveStorageUsedSpacePrice': 0,
            'remoteArchiveStorageUsedSpaceChunkSize': 1, 'remoteArchiveStorageUsedSpaceUnits': 'GB',
            'remoteFreeArchiveStorageUsedSpace': None, 'remoteFreeArchiveStorageUsedSpaceUnits': 'GB',
            'remoteRepositorySpaceUsageAlgorithm': 'Consumed', 'remoteRepositoryAllocatedSpacePrice': 0,
            'remoteRepositoryAllocatedSpaceUnits': 'GB', 'hostedSubscriptionUserPrice': 0, 'hostedFreeSubscriptionUsers': 0,
            'hostedEducationalUserPrice': 0, 'hostedFreeEducationalUsers': 0, 'hostedRoundUpUsedSpace': False,
            'hostedStandardStorageUsedSpacePrice': 0, 'hostedStandardStorageUsedSpaceChunkSize': 1,
            'hostedStandardStorageUsedSpaceUnits': 'GB', 'hostedFreeStandardStorageUsedSpace': None,
            'hostedFreeStandardStorageUsedSpaceUnits': 'GB', 'hostedArchiveStorageUsedSpacePrice': 0,
            'hostedArchiveStorageUsedSpaceChunkSize': 1, 'hostedArchiveStorageUsedSpaceUnits': 'GB',
            'hostedFreeArchiveStorageUsedSpace': None, 'hostedFreeArchiveStorageUsedSpaceUnits': 'GB',
            'hostedRepositorySpaceUsageAlgorithm': 'Consumed', 'hostedRepositoryAllocatedSpacePrice': 0,
            'hostedRepositoryAllocatedSpaceUnits': 'GB'}, 'cloudReplication': {'replicatedVmPrice': 10,
            'cloudStorageConsumedSpacePrice': 10, 'cloudStorageConsumedSpaceUnits': 'TB', 'freeCloudStorageConsumedSpace':
            None, 'freeCloudStorageConsumedSpaceUnits': 'GB', 'computeResourcesPrice': 0, 'computeResourcesUnits': 'Hours',
            'freeComputeResources': 1, 'freeComputeResourcesUnits': 'Hours', 'replicationDataTransferOutPrice': 0,
            'replicationDataTransferOutUnits': 'GB'}, 'fileShareBackup': {'fileShareRemoteBackupUsedSpacePrice': 0,
            'fileShareRemoteBackupUsedSpaceUnits': 'GB', 'freeFileShareRemoteBackupUsedSpace': None,
            'freeFileShareRemoteBackupUsedSpaceUnits': 'GB', 'fileShareRemoteArchiveUsedSpacePrice': 0,
            'fileShareRemoteArchiveUsedSpaceUnits': 'GB', 'freeFileShareRemoteArchiveUsedSpace': None,
            'freeFileShareRemoteArchiveUsedSpaceUnits': 'GB', 'sourceRemoteAmountOfDataPrice': 0,
            'sourceRemoteAmountOfDataUnits': 'GB', 'freeSourceRemoteAmountOfData': None,
            'freeSourceRemoteAmountOfDataUnits': 'GB', 'fileShareHostedBackupUsedSpacePrice': 0,
            'fileShareHostedBackupUsedSpaceUnits': 'GB', 'freeFileShareHostedBackupUsedSpace': None,
            'freeFileShareHostedBackupUsedSpaceUnits': 'GB', 'fileShareHostedArchiveUsedSpacePrice': 0,
            'fileShareHostedArchiveUsedSpaceUnits': 'GB', 'freeFileShareHostedArchiveUsedSpace': None,
            'freeFileShareHostedArchiveUsedSpaceUnits': 'GB', 'sourceHostedAmountOfDataPrice': 0,
            'sourceHostedAmountOfDataUnits': 'GB', 'freeSourceHostedAmountOfData': None,
            'freeSourceHostedAmountOfDataUnits': 'GB'}, 'cloudBackup': {'roundUpUsedSpace': False, 'vmCloudBackupsPrice': 5,
            'serverCloudBackupsPrice': 6, 'workstationCloudBackupsPrice': 7, 'cloudRepositorySpaceUsageAlgorithm':
            'Consumed', 'cloudRepositoryAllocatedSpacePrice': 0, 'cloudRepositoryAllocatedSpaceUnits': 'GB',
            'cloudRepositoryConsumedSpacePrice': 15, 'cloudRepositoryConsumedSpaceChunkSize': 1,
            'cloudRepositoryConsumedSpaceUnits': 'TB', 'freeCloudRepositoryConsumedSpace': None,
            'freeCloudRepositoryConsumedSpaceUnits': 'GB', 'backupDataTransferOutPrice': 8, 'backupDataTransferOutUnits':
            'GB', 'insiderProtectionUsedSpacePrice': 0, 'insiderProtectionUsedSpaceUnits': 'GB',
            'performanceTierUsedSpacePrice': 0, 'performanceTierUsedSpaceChunkSize': 1, 'performanceTierUsedSpaceUnits':
            'GB', 'capacityTierUsedSpacePrice': 0, 'capacityTierUsedSpaceChunkSize': 1, 'capacityTierUsedSpaceUnits': 'GB',
            'archiveTierUsedSpacePrice': 0, 'archiveTierUsedSpaceChunkSize': 1, 'archiveTierUsedSpaceUnits': 'GB'},
            'licenses': {'vspcLicenses': {'workstationPrice': 0, 'serverPrice': 0},
            'backupAndReplicationStandardEditionLicenses': {'vmPrice': 0, 'workstationPrice': 0, 'serverPrice': 0,
            'applicationPrice': 0, 'microsoftEntraIdPrice': 0, 'fileSharePrice': 0, 'objectStoragePrice': 0, 'cloudVmPrice':
            0, 'cloudFileSharePrice': 0, 'cloudDatabasePrice': 0}, 'backupAndReplicationEnterpriseEditionLicenses':
            {'vmPrice': 0, 'workstationPrice': 0, 'serverPrice': 0, 'applicationPrice': 0, 'microsoftEntraIdPrice': 0,
            'fileSharePrice': 0, 'objectStoragePrice': 0, 'cloudVmPrice': 0, 'cloudFileSharePrice': 0, 'cloudDatabasePrice':
            0}, 'backupAndReplicationEnterprisePlusEditionLicenses': {'vmPrice': 0, 'workstationPrice': 0, 'serverPrice': 0,
            'applicationPrice': 0, 'microsoftEntraIdPrice': 0, 'fileSharePrice': 0, 'objectStoragePrice': 0, 'cloudVmPrice':
            0, 'cloudFileSharePrice': 0, 'cloudDatabasePrice': 0}, 'vdpFoundationPackageLicenses': {'vmPrice': 0,
            'workstationPrice': 0, 'serverPrice': 0, 'applicationPrice': 0, 'microsoftEntraIdPrice': 0, 'fileSharePrice': 0,
            'objectStoragePrice': 0, 'cloudVmPrice': 0, 'cloudFileSharePrice': 0, 'cloudDatabasePrice': 0},
            'vdpAdvancedPackageLicenses': {'vmPrice': 0, 'workstationPrice': 0, 'serverPrice': 0, 'applicationPrice': 0,
            'microsoftEntraIdPrice': 0, 'fileSharePrice': 0, 'objectStoragePrice': 0, 'cloudVmPrice': 0,
            'cloudFileSharePrice': 0, 'cloudDatabasePrice': 0}, 'vdpPremiumPackageLicenses': {'vmPrice': 0,
            'workstationPrice': 0, 'serverPrice': 0, 'applicationPrice': 0, 'microsoftEntraIdPrice': 0, 'fileSharePrice': 0,
            'objectStoragePrice': 0, 'cloudVmPrice': 0, 'cloudFileSharePrice': 0, 'cloudDatabasePrice': 0},
            'cloudConnectLicenses': {'vmBackupPrice': 0, 'vmReplicaPrice': 0, 'workstationBackupPrice': 0,
            'serverBackupPrice': 0}, 'vb365Licenses': {'userPrice': 0}, 'veeamOneLicenses': {'monitoredObjectPrice': 0}},
            'externalPlugins': []}.
        meta (ResponseMetadata | Unset):
        errors (list[ResponseError] | Unset):
    """

    data: SubscriptionPlan
    meta: ResponseMetadata | Unset = UNSET
    errors: list[ResponseError] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data = self.data.to_dict()

        meta: dict[str, Any] | Unset = UNSET
        if not isinstance(self.meta, Unset):
            meta = self.meta.to_dict()

        errors: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.errors, Unset):
            errors = []
            for errors_item_data in self.errors:
                errors_item = errors_item_data.to_dict()
                errors.append(errors_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "data": data,
            }
        )
        if meta is not UNSET:
            field_dict["meta"] = meta
        if errors is not UNSET:
            field_dict["errors"] = errors

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.response_error import ResponseError
        from ..models.response_metadata import ResponseMetadata
        from ..models.subscription_plan import SubscriptionPlan

        d = dict(src_dict)
        data = SubscriptionPlan.from_dict(d.pop("data"))

        _meta = d.pop("meta", UNSET)
        meta: ResponseMetadata | Unset
        if isinstance(_meta, Unset):
            meta = UNSET
        else:
            meta = ResponseMetadata.from_dict(_meta)

        _errors = d.pop("errors", UNSET)
        errors: list[ResponseError] | Unset = UNSET
        if _errors is not UNSET:
            errors = []
            for errors_item_data in _errors:
                errors_item = ResponseError.from_dict(errors_item_data)

                errors.append(errors_item)

        patch_subscription_plan_response_200 = cls(
            data=data,
            meta=meta,
            errors=errors,
        )

        patch_subscription_plan_response_200.additional_properties = d
        return patch_subscription_plan_response_200

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
