from http import HTTPStatus
from typing import Any, cast
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.create_subscription_plan_response_200 import CreateSubscriptionPlanResponse200
from ...models.error_response import ErrorResponse
from ...models.subscription_plan import SubscriptionPlan
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: SubscriptionPlan,
    select: str | Unset = UNSET,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_request_id, Unset):
        headers["X-Request-id"] = x_request_id

    if not isinstance(x_client_version, Unset):
        headers["X-Client-Version"] = x_client_version

    params: dict[str, Any] = {}

    params["select"] = select

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/subscriptionPlans",
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | CreateSubscriptionPlanResponse200 | ErrorResponse:
    if response.status_code == 200:
        response_200 = CreateSubscriptionPlanResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 202:
        response_202 = cast(Any, None)
        return response_202

    response_default = ErrorResponse.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | CreateSubscriptionPlanResponse200 | ErrorResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: SubscriptionPlan,
    select: str | Unset = UNSET,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Response[Any | CreateSubscriptionPlanResponse200 | ErrorResponse]:
    """Create Subscription Plan

     Creates a subscription plan.

    Args:
        select (str | Unset):
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):
        body (SubscriptionPlan):  Example: {'name': 'Pittsburgh subscription plan', 'description':
            'Subscription plan for Pittsburgh clients', 'currency': 'USD', 'taxType': 'VAT',
            'taxPercent': 10, 'discountPercent': 12, 'managedBackup': {'managedServicePrice': 21,
            'monitoredServicePrice': 0, 'remoteManagedVmPrice': 0, 'remoteManagedCdpVmPrice': 0,
            'remoteManagedWorkstationPrice': 0, 'remoteManagedServerAgentPrice': 0,
            'remoteFreeManagedVms': 0, 'remoteFreeManagedCdpVms': 0, 'remoteFreeManagedWorkstations':
            0, 'remoteFreeManagedServerAgents': 0, 'remoteWindowsServerOsPrice': 0,
            'remoteWindowsClientOsPrice': 0, 'remoteLinuxOsPrice': 0, 'remoteMacOsPrice': 0,
            'remoteBackupUsedSpacePrice': 0, 'remoteBackupUsedSpaceUnits': 'GB',
            'remoteFreeBackupUsedSpace': None, 'remoteFreeBackupUsedSpaceUnits': 'GB',
            'remoteRepositorySpaceUsageAlgorithm': 'Consumed', 'remoteRepositoryAllocatedSpacePrice':
            0, 'remoteRepositoryAllocatedSpaceUnits': 'GB', 'remoteRoundUpBackupUsedSpace': False,
            'remoteBackupUsedSpaceChunkSize': 1, 'hostedManagedVmPrice': 0, 'hostedManagedCdpVmPrice':
            0, 'hostedManagedWorkstationPrice': 0, 'hostedManagedServerAgentPrice': 0,
            'hostedFreeManagedVms': 0, 'hostedFreeManagedCdpVms': 0, 'hostedFreeManagedWorkstations':
            0, 'hostedFreeManagedServerAgents': 0, 'hostedWindowsServerOsPrice': 0,
            'hostedWindowsClientOsPrice': 0, 'hostedLinuxOsPrice': 0, 'hostedMacOsPrice': 0,
            'hostedBackupUsedSpacePrice': 0, 'hostedBackupUsedSpaceUnits': 'GB',
            'hostedFreeBackupUsedSpace': None, 'hostedFreeBackupUsedSpaceUnits': 'GB',
            'hostedRepositorySpaceUsageAlgorithm': 'Consumed', 'hostedRepositoryAllocatedSpacePrice':
            0, 'hostedRepositoryAllocatedSpaceUnits': 'GB', 'hostedRoundUpBackupUsedSpace': False,
            'hostedBackupUsedSpaceChunkSize': 1, 'useRepositoryUsageByLabelHosted': True,
            'useRepositoryUsageByLabelRemote': False, 'repositoryUsageByLabel': {'hosted':
            [{'labelUid': '8f3c9d21-5b47-4e6a-9c12-7d8a0f4b1e63', 'price': 12, 'priceMeasure': 'TB',
            'freeOfCharge': 100, 'freeOfChargeMeasure': 'GB', 'chunkSize': 1, 'roundUpPerChunk': True,
            'enabled': True}], 'remote': []}}, 'publicCloud': {'remoteCloudVmPrice': 0,
            'remoteFreeCloudVms': 0, 'remoteCloudFileSharePrice': 0, 'remoteFreeCloudFileShares': 0,
            'remoteCloudDatabasePrice': 0, 'remoteFreeCloudDatabases': 0, 'remoteCloudNetworkPrice':
            0, 'remoteBackupUsedSpacePrice': 0, 'remoteBackupUsedSpaceUnits': 'GB',
            'remoteFreeBackupUsedSpace': None, 'remoteFreeBackupUsedSpaceUnits': 'GB',
            'remoteArchiveUsedSpacePrice': 0, 'remoteArchiveUsedSpaceUnits': 'GB',
            'remoteFreeArchiveUsedSpace': None, 'remoteFreeArchiveUsedSpaceUnits': 'GB',
            'hostedCloudVmPrice': 0, 'hostedFreeCloudVms': 0, 'hostedCloudFileSharePrice': 0,
            'hostedFreeCloudFileShares': 0, 'hostedCloudDatabasePrice': 0, 'hostedFreeCloudDatabases':
            0, 'hostedCloudNetworkPrice': 0, 'hostedBackupUsedSpacePrice': 0,
            'hostedBackupUsedSpaceUnits': 'GB', 'hostedFreeBackupUsedSpace': None,
            'hostedFreeBackupUsedSpaceUnits': 'GB', 'hostedArchiveUsedSpacePrice': 0,
            'hostedArchiveUsedSpaceUnits': 'GB', 'hostedFreeArchiveUsedSpace': None,
            'hostedFreeArchiveUsedSpaceUnits': 'GB'}, 'vb365': {'remoteSubscriptionUserPrice': 0,
            'remoteFreeSubscriptionUsers': 0, 'remoteEducationalUserPrice': 0,
            'remoteFreeEducationalUsers': 0, 'remoteRoundUpUsedSpace': False,
            'remoteStandardStorageUsedSpacePrice': 0, 'remoteStandardStorageUsedSpaceChunkSize': 1,
            'remoteStandardStorageUsedSpaceUnits': 'GB', 'remoteFreeStandardStorageUsedSpace': None,
            'remoteFreeStandardStorageUsedSpaceUnits': 'GB', 'remoteArchiveStorageUsedSpacePrice': 0,
            'remoteArchiveStorageUsedSpaceChunkSize': 1, 'remoteArchiveStorageUsedSpaceUnits': 'GB',
            'remoteFreeArchiveStorageUsedSpace': None, 'remoteFreeArchiveStorageUsedSpaceUnits': 'GB',
            'remoteRepositorySpaceUsageAlgorithm': 'Consumed', 'remoteRepositoryAllocatedSpacePrice':
            0, 'remoteRepositoryAllocatedSpaceUnits': 'GB', 'hostedSubscriptionUserPrice': 0,
            'hostedFreeSubscriptionUsers': 0, 'hostedEducationalUserPrice': 0,
            'hostedFreeEducationalUsers': 0, 'hostedRoundUpUsedSpace': False,
            'hostedStandardStorageUsedSpacePrice': 0, 'hostedStandardStorageUsedSpaceChunkSize': 1,
            'hostedStandardStorageUsedSpaceUnits': 'GB', 'hostedFreeStandardStorageUsedSpace': None,
            'hostedFreeStandardStorageUsedSpaceUnits': 'GB', 'hostedArchiveStorageUsedSpacePrice': 0,
            'hostedArchiveStorageUsedSpaceChunkSize': 1, 'hostedArchiveStorageUsedSpaceUnits': 'GB',
            'hostedFreeArchiveStorageUsedSpace': None, 'hostedFreeArchiveStorageUsedSpaceUnits': 'GB',
            'hostedRepositorySpaceUsageAlgorithm': 'Consumed', 'hostedRepositoryAllocatedSpacePrice':
            0, 'hostedRepositoryAllocatedSpaceUnits': 'GB'}, 'cloudReplication': {'replicatedVmPrice':
            10, 'cloudStorageConsumedSpacePrice': 10, 'cloudStorageConsumedSpaceUnits': 'TB',
            'freeCloudStorageConsumedSpace': None, 'freeCloudStorageConsumedSpaceUnits': 'GB',
            'computeResourcesPrice': 0, 'computeResourcesUnits': 'Hours', 'freeComputeResources': 1,
            'freeComputeResourcesUnits': 'Hours', 'replicationDataTransferOutPrice': 0,
            'replicationDataTransferOutUnits': 'GB'}, 'fileShareBackup':
            {'fileShareRemoteBackupUsedSpacePrice': 0, 'fileShareRemoteBackupUsedSpaceUnits': 'GB',
            'freeFileShareRemoteBackupUsedSpace': None, 'freeFileShareRemoteBackupUsedSpaceUnits':
            'GB', 'fileShareRemoteArchiveUsedSpacePrice': 0, 'fileShareRemoteArchiveUsedSpaceUnits':
            'GB', 'freeFileShareRemoteArchiveUsedSpace': None,
            'freeFileShareRemoteArchiveUsedSpaceUnits': 'GB', 'sourceRemoteAmountOfDataPrice': 0,
            'sourceRemoteAmountOfDataUnits': 'GB', 'freeSourceRemoteAmountOfData': None,
            'freeSourceRemoteAmountOfDataUnits': 'GB', 'fileShareHostedBackupUsedSpacePrice': 0,
            'fileShareHostedBackupUsedSpaceUnits': 'GB', 'freeFileShareHostedBackupUsedSpace': None,
            'freeFileShareHostedBackupUsedSpaceUnits': 'GB', 'fileShareHostedArchiveUsedSpacePrice':
            0, 'fileShareHostedArchiveUsedSpaceUnits': 'GB', 'freeFileShareHostedArchiveUsedSpace':
            None, 'freeFileShareHostedArchiveUsedSpaceUnits': 'GB', 'sourceHostedAmountOfDataPrice':
            0, 'sourceHostedAmountOfDataUnits': 'GB', 'freeSourceHostedAmountOfData': None,
            'freeSourceHostedAmountOfDataUnits': 'GB'}, 'cloudBackup': {'roundUpUsedSpace': False,
            'vmCloudBackupsPrice': 5, 'serverCloudBackupsPrice': 6, 'workstationCloudBackupsPrice': 7,
            'cloudRepositorySpaceUsageAlgorithm': 'Consumed', 'cloudRepositoryAllocatedSpacePrice': 0,
            'cloudRepositoryAllocatedSpaceUnits': 'GB', 'cloudRepositoryConsumedSpacePrice': 15,
            'cloudRepositoryConsumedSpaceChunkSize': 1, 'cloudRepositoryConsumedSpaceUnits': 'TB',
            'freeCloudRepositoryConsumedSpace': None, 'freeCloudRepositoryConsumedSpaceUnits': 'GB',
            'backupDataTransferOutPrice': 8, 'backupDataTransferOutUnits': 'GB',
            'insiderProtectionUsedSpacePrice': 0, 'insiderProtectionUsedSpaceUnits': 'GB',
            'performanceTierUsedSpacePrice': 0, 'performanceTierUsedSpaceChunkSize': 1,
            'performanceTierUsedSpaceUnits': 'GB', 'capacityTierUsedSpacePrice': 0,
            'capacityTierUsedSpaceChunkSize': 1, 'capacityTierUsedSpaceUnits': 'GB',
            'archiveTierUsedSpacePrice': 0, 'archiveTierUsedSpaceChunkSize': 1,
            'archiveTierUsedSpaceUnits': 'GB'}, 'licenses': {'vspcLicenses': {'workstationPrice': 0,
            'serverPrice': 0}, 'backupAndReplicationStandardEditionLicenses': {'vmPrice': 0,
            'workstationPrice': 0, 'serverPrice': 0, 'applicationPrice': 0, 'microsoftEntraIdPrice':
            0, 'fileSharePrice': 0, 'objectStoragePrice': 0, 'cloudVmPrice': 0, 'cloudFileSharePrice':
            0, 'cloudDatabasePrice': 0}, 'backupAndReplicationEnterpriseEditionLicenses': {'vmPrice':
            0, 'workstationPrice': 0, 'serverPrice': 0, 'applicationPrice': 0,
            'microsoftEntraIdPrice': 0, 'fileSharePrice': 0, 'objectStoragePrice': 0, 'cloudVmPrice':
            0, 'cloudFileSharePrice': 0, 'cloudDatabasePrice': 0},
            'backupAndReplicationEnterprisePlusEditionLicenses': {'vmPrice': 0, 'workstationPrice': 0,
            'serverPrice': 0, 'applicationPrice': 0, 'microsoftEntraIdPrice': 0, 'fileSharePrice': 0,
            'objectStoragePrice': 0, 'cloudVmPrice': 0, 'cloudFileSharePrice': 0,
            'cloudDatabasePrice': 0}, 'vdpFoundationPackageLicenses': {'vmPrice': 0,
            'workstationPrice': 0, 'serverPrice': 0, 'applicationPrice': 0, 'microsoftEntraIdPrice':
            0, 'fileSharePrice': 0, 'objectStoragePrice': 0, 'cloudVmPrice': 0, 'cloudFileSharePrice':
            0, 'cloudDatabasePrice': 0}, 'vdpAdvancedPackageLicenses': {'vmPrice': 0,
            'workstationPrice': 0, 'serverPrice': 0, 'applicationPrice': 0, 'microsoftEntraIdPrice':
            0, 'fileSharePrice': 0, 'objectStoragePrice': 0, 'cloudVmPrice': 0, 'cloudFileSharePrice':
            0, 'cloudDatabasePrice': 0}, 'vdpPremiumPackageLicenses': {'vmPrice': 0,
            'workstationPrice': 0, 'serverPrice': 0, 'applicationPrice': 0, 'microsoftEntraIdPrice':
            0, 'fileSharePrice': 0, 'objectStoragePrice': 0, 'cloudVmPrice': 0, 'cloudFileSharePrice':
            0, 'cloudDatabasePrice': 0}, 'cloudConnectLicenses': {'vmBackupPrice': 0,
            'vmReplicaPrice': 0, 'workstationBackupPrice': 0, 'serverBackupPrice': 0},
            'vb365Licenses': {'userPrice': 0}, 'veeamOneLicenses': {'monitoredObjectPrice': 0}},
            'externalPlugins': []}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CreateSubscriptionPlanResponse200 | ErrorResponse]
    """

    kwargs = _get_kwargs(
        body=body,
        select=select,
        x_request_id=x_request_id,
        x_client_version=x_client_version,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: SubscriptionPlan,
    select: str | Unset = UNSET,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Any | CreateSubscriptionPlanResponse200 | ErrorResponse | None:
    """Create Subscription Plan

     Creates a subscription plan.

    Args:
        select (str | Unset):
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):
        body (SubscriptionPlan):  Example: {'name': 'Pittsburgh subscription plan', 'description':
            'Subscription plan for Pittsburgh clients', 'currency': 'USD', 'taxType': 'VAT',
            'taxPercent': 10, 'discountPercent': 12, 'managedBackup': {'managedServicePrice': 21,
            'monitoredServicePrice': 0, 'remoteManagedVmPrice': 0, 'remoteManagedCdpVmPrice': 0,
            'remoteManagedWorkstationPrice': 0, 'remoteManagedServerAgentPrice': 0,
            'remoteFreeManagedVms': 0, 'remoteFreeManagedCdpVms': 0, 'remoteFreeManagedWorkstations':
            0, 'remoteFreeManagedServerAgents': 0, 'remoteWindowsServerOsPrice': 0,
            'remoteWindowsClientOsPrice': 0, 'remoteLinuxOsPrice': 0, 'remoteMacOsPrice': 0,
            'remoteBackupUsedSpacePrice': 0, 'remoteBackupUsedSpaceUnits': 'GB',
            'remoteFreeBackupUsedSpace': None, 'remoteFreeBackupUsedSpaceUnits': 'GB',
            'remoteRepositorySpaceUsageAlgorithm': 'Consumed', 'remoteRepositoryAllocatedSpacePrice':
            0, 'remoteRepositoryAllocatedSpaceUnits': 'GB', 'remoteRoundUpBackupUsedSpace': False,
            'remoteBackupUsedSpaceChunkSize': 1, 'hostedManagedVmPrice': 0, 'hostedManagedCdpVmPrice':
            0, 'hostedManagedWorkstationPrice': 0, 'hostedManagedServerAgentPrice': 0,
            'hostedFreeManagedVms': 0, 'hostedFreeManagedCdpVms': 0, 'hostedFreeManagedWorkstations':
            0, 'hostedFreeManagedServerAgents': 0, 'hostedWindowsServerOsPrice': 0,
            'hostedWindowsClientOsPrice': 0, 'hostedLinuxOsPrice': 0, 'hostedMacOsPrice': 0,
            'hostedBackupUsedSpacePrice': 0, 'hostedBackupUsedSpaceUnits': 'GB',
            'hostedFreeBackupUsedSpace': None, 'hostedFreeBackupUsedSpaceUnits': 'GB',
            'hostedRepositorySpaceUsageAlgorithm': 'Consumed', 'hostedRepositoryAllocatedSpacePrice':
            0, 'hostedRepositoryAllocatedSpaceUnits': 'GB', 'hostedRoundUpBackupUsedSpace': False,
            'hostedBackupUsedSpaceChunkSize': 1, 'useRepositoryUsageByLabelHosted': True,
            'useRepositoryUsageByLabelRemote': False, 'repositoryUsageByLabel': {'hosted':
            [{'labelUid': '8f3c9d21-5b47-4e6a-9c12-7d8a0f4b1e63', 'price': 12, 'priceMeasure': 'TB',
            'freeOfCharge': 100, 'freeOfChargeMeasure': 'GB', 'chunkSize': 1, 'roundUpPerChunk': True,
            'enabled': True}], 'remote': []}}, 'publicCloud': {'remoteCloudVmPrice': 0,
            'remoteFreeCloudVms': 0, 'remoteCloudFileSharePrice': 0, 'remoteFreeCloudFileShares': 0,
            'remoteCloudDatabasePrice': 0, 'remoteFreeCloudDatabases': 0, 'remoteCloudNetworkPrice':
            0, 'remoteBackupUsedSpacePrice': 0, 'remoteBackupUsedSpaceUnits': 'GB',
            'remoteFreeBackupUsedSpace': None, 'remoteFreeBackupUsedSpaceUnits': 'GB',
            'remoteArchiveUsedSpacePrice': 0, 'remoteArchiveUsedSpaceUnits': 'GB',
            'remoteFreeArchiveUsedSpace': None, 'remoteFreeArchiveUsedSpaceUnits': 'GB',
            'hostedCloudVmPrice': 0, 'hostedFreeCloudVms': 0, 'hostedCloudFileSharePrice': 0,
            'hostedFreeCloudFileShares': 0, 'hostedCloudDatabasePrice': 0, 'hostedFreeCloudDatabases':
            0, 'hostedCloudNetworkPrice': 0, 'hostedBackupUsedSpacePrice': 0,
            'hostedBackupUsedSpaceUnits': 'GB', 'hostedFreeBackupUsedSpace': None,
            'hostedFreeBackupUsedSpaceUnits': 'GB', 'hostedArchiveUsedSpacePrice': 0,
            'hostedArchiveUsedSpaceUnits': 'GB', 'hostedFreeArchiveUsedSpace': None,
            'hostedFreeArchiveUsedSpaceUnits': 'GB'}, 'vb365': {'remoteSubscriptionUserPrice': 0,
            'remoteFreeSubscriptionUsers': 0, 'remoteEducationalUserPrice': 0,
            'remoteFreeEducationalUsers': 0, 'remoteRoundUpUsedSpace': False,
            'remoteStandardStorageUsedSpacePrice': 0, 'remoteStandardStorageUsedSpaceChunkSize': 1,
            'remoteStandardStorageUsedSpaceUnits': 'GB', 'remoteFreeStandardStorageUsedSpace': None,
            'remoteFreeStandardStorageUsedSpaceUnits': 'GB', 'remoteArchiveStorageUsedSpacePrice': 0,
            'remoteArchiveStorageUsedSpaceChunkSize': 1, 'remoteArchiveStorageUsedSpaceUnits': 'GB',
            'remoteFreeArchiveStorageUsedSpace': None, 'remoteFreeArchiveStorageUsedSpaceUnits': 'GB',
            'remoteRepositorySpaceUsageAlgorithm': 'Consumed', 'remoteRepositoryAllocatedSpacePrice':
            0, 'remoteRepositoryAllocatedSpaceUnits': 'GB', 'hostedSubscriptionUserPrice': 0,
            'hostedFreeSubscriptionUsers': 0, 'hostedEducationalUserPrice': 0,
            'hostedFreeEducationalUsers': 0, 'hostedRoundUpUsedSpace': False,
            'hostedStandardStorageUsedSpacePrice': 0, 'hostedStandardStorageUsedSpaceChunkSize': 1,
            'hostedStandardStorageUsedSpaceUnits': 'GB', 'hostedFreeStandardStorageUsedSpace': None,
            'hostedFreeStandardStorageUsedSpaceUnits': 'GB', 'hostedArchiveStorageUsedSpacePrice': 0,
            'hostedArchiveStorageUsedSpaceChunkSize': 1, 'hostedArchiveStorageUsedSpaceUnits': 'GB',
            'hostedFreeArchiveStorageUsedSpace': None, 'hostedFreeArchiveStorageUsedSpaceUnits': 'GB',
            'hostedRepositorySpaceUsageAlgorithm': 'Consumed', 'hostedRepositoryAllocatedSpacePrice':
            0, 'hostedRepositoryAllocatedSpaceUnits': 'GB'}, 'cloudReplication': {'replicatedVmPrice':
            10, 'cloudStorageConsumedSpacePrice': 10, 'cloudStorageConsumedSpaceUnits': 'TB',
            'freeCloudStorageConsumedSpace': None, 'freeCloudStorageConsumedSpaceUnits': 'GB',
            'computeResourcesPrice': 0, 'computeResourcesUnits': 'Hours', 'freeComputeResources': 1,
            'freeComputeResourcesUnits': 'Hours', 'replicationDataTransferOutPrice': 0,
            'replicationDataTransferOutUnits': 'GB'}, 'fileShareBackup':
            {'fileShareRemoteBackupUsedSpacePrice': 0, 'fileShareRemoteBackupUsedSpaceUnits': 'GB',
            'freeFileShareRemoteBackupUsedSpace': None, 'freeFileShareRemoteBackupUsedSpaceUnits':
            'GB', 'fileShareRemoteArchiveUsedSpacePrice': 0, 'fileShareRemoteArchiveUsedSpaceUnits':
            'GB', 'freeFileShareRemoteArchiveUsedSpace': None,
            'freeFileShareRemoteArchiveUsedSpaceUnits': 'GB', 'sourceRemoteAmountOfDataPrice': 0,
            'sourceRemoteAmountOfDataUnits': 'GB', 'freeSourceRemoteAmountOfData': None,
            'freeSourceRemoteAmountOfDataUnits': 'GB', 'fileShareHostedBackupUsedSpacePrice': 0,
            'fileShareHostedBackupUsedSpaceUnits': 'GB', 'freeFileShareHostedBackupUsedSpace': None,
            'freeFileShareHostedBackupUsedSpaceUnits': 'GB', 'fileShareHostedArchiveUsedSpacePrice':
            0, 'fileShareHostedArchiveUsedSpaceUnits': 'GB', 'freeFileShareHostedArchiveUsedSpace':
            None, 'freeFileShareHostedArchiveUsedSpaceUnits': 'GB', 'sourceHostedAmountOfDataPrice':
            0, 'sourceHostedAmountOfDataUnits': 'GB', 'freeSourceHostedAmountOfData': None,
            'freeSourceHostedAmountOfDataUnits': 'GB'}, 'cloudBackup': {'roundUpUsedSpace': False,
            'vmCloudBackupsPrice': 5, 'serverCloudBackupsPrice': 6, 'workstationCloudBackupsPrice': 7,
            'cloudRepositorySpaceUsageAlgorithm': 'Consumed', 'cloudRepositoryAllocatedSpacePrice': 0,
            'cloudRepositoryAllocatedSpaceUnits': 'GB', 'cloudRepositoryConsumedSpacePrice': 15,
            'cloudRepositoryConsumedSpaceChunkSize': 1, 'cloudRepositoryConsumedSpaceUnits': 'TB',
            'freeCloudRepositoryConsumedSpace': None, 'freeCloudRepositoryConsumedSpaceUnits': 'GB',
            'backupDataTransferOutPrice': 8, 'backupDataTransferOutUnits': 'GB',
            'insiderProtectionUsedSpacePrice': 0, 'insiderProtectionUsedSpaceUnits': 'GB',
            'performanceTierUsedSpacePrice': 0, 'performanceTierUsedSpaceChunkSize': 1,
            'performanceTierUsedSpaceUnits': 'GB', 'capacityTierUsedSpacePrice': 0,
            'capacityTierUsedSpaceChunkSize': 1, 'capacityTierUsedSpaceUnits': 'GB',
            'archiveTierUsedSpacePrice': 0, 'archiveTierUsedSpaceChunkSize': 1,
            'archiveTierUsedSpaceUnits': 'GB'}, 'licenses': {'vspcLicenses': {'workstationPrice': 0,
            'serverPrice': 0}, 'backupAndReplicationStandardEditionLicenses': {'vmPrice': 0,
            'workstationPrice': 0, 'serverPrice': 0, 'applicationPrice': 0, 'microsoftEntraIdPrice':
            0, 'fileSharePrice': 0, 'objectStoragePrice': 0, 'cloudVmPrice': 0, 'cloudFileSharePrice':
            0, 'cloudDatabasePrice': 0}, 'backupAndReplicationEnterpriseEditionLicenses': {'vmPrice':
            0, 'workstationPrice': 0, 'serverPrice': 0, 'applicationPrice': 0,
            'microsoftEntraIdPrice': 0, 'fileSharePrice': 0, 'objectStoragePrice': 0, 'cloudVmPrice':
            0, 'cloudFileSharePrice': 0, 'cloudDatabasePrice': 0},
            'backupAndReplicationEnterprisePlusEditionLicenses': {'vmPrice': 0, 'workstationPrice': 0,
            'serverPrice': 0, 'applicationPrice': 0, 'microsoftEntraIdPrice': 0, 'fileSharePrice': 0,
            'objectStoragePrice': 0, 'cloudVmPrice': 0, 'cloudFileSharePrice': 0,
            'cloudDatabasePrice': 0}, 'vdpFoundationPackageLicenses': {'vmPrice': 0,
            'workstationPrice': 0, 'serverPrice': 0, 'applicationPrice': 0, 'microsoftEntraIdPrice':
            0, 'fileSharePrice': 0, 'objectStoragePrice': 0, 'cloudVmPrice': 0, 'cloudFileSharePrice':
            0, 'cloudDatabasePrice': 0}, 'vdpAdvancedPackageLicenses': {'vmPrice': 0,
            'workstationPrice': 0, 'serverPrice': 0, 'applicationPrice': 0, 'microsoftEntraIdPrice':
            0, 'fileSharePrice': 0, 'objectStoragePrice': 0, 'cloudVmPrice': 0, 'cloudFileSharePrice':
            0, 'cloudDatabasePrice': 0}, 'vdpPremiumPackageLicenses': {'vmPrice': 0,
            'workstationPrice': 0, 'serverPrice': 0, 'applicationPrice': 0, 'microsoftEntraIdPrice':
            0, 'fileSharePrice': 0, 'objectStoragePrice': 0, 'cloudVmPrice': 0, 'cloudFileSharePrice':
            0, 'cloudDatabasePrice': 0}, 'cloudConnectLicenses': {'vmBackupPrice': 0,
            'vmReplicaPrice': 0, 'workstationBackupPrice': 0, 'serverBackupPrice': 0},
            'vb365Licenses': {'userPrice': 0}, 'veeamOneLicenses': {'monitoredObjectPrice': 0}},
            'externalPlugins': []}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CreateSubscriptionPlanResponse200 | ErrorResponse
    """

    return sync_detailed(
        client=client,
        body=body,
        select=select,
        x_request_id=x_request_id,
        x_client_version=x_client_version,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: SubscriptionPlan,
    select: str | Unset = UNSET,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Response[Any | CreateSubscriptionPlanResponse200 | ErrorResponse]:
    """Create Subscription Plan

     Creates a subscription plan.

    Args:
        select (str | Unset):
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):
        body (SubscriptionPlan):  Example: {'name': 'Pittsburgh subscription plan', 'description':
            'Subscription plan for Pittsburgh clients', 'currency': 'USD', 'taxType': 'VAT',
            'taxPercent': 10, 'discountPercent': 12, 'managedBackup': {'managedServicePrice': 21,
            'monitoredServicePrice': 0, 'remoteManagedVmPrice': 0, 'remoteManagedCdpVmPrice': 0,
            'remoteManagedWorkstationPrice': 0, 'remoteManagedServerAgentPrice': 0,
            'remoteFreeManagedVms': 0, 'remoteFreeManagedCdpVms': 0, 'remoteFreeManagedWorkstations':
            0, 'remoteFreeManagedServerAgents': 0, 'remoteWindowsServerOsPrice': 0,
            'remoteWindowsClientOsPrice': 0, 'remoteLinuxOsPrice': 0, 'remoteMacOsPrice': 0,
            'remoteBackupUsedSpacePrice': 0, 'remoteBackupUsedSpaceUnits': 'GB',
            'remoteFreeBackupUsedSpace': None, 'remoteFreeBackupUsedSpaceUnits': 'GB',
            'remoteRepositorySpaceUsageAlgorithm': 'Consumed', 'remoteRepositoryAllocatedSpacePrice':
            0, 'remoteRepositoryAllocatedSpaceUnits': 'GB', 'remoteRoundUpBackupUsedSpace': False,
            'remoteBackupUsedSpaceChunkSize': 1, 'hostedManagedVmPrice': 0, 'hostedManagedCdpVmPrice':
            0, 'hostedManagedWorkstationPrice': 0, 'hostedManagedServerAgentPrice': 0,
            'hostedFreeManagedVms': 0, 'hostedFreeManagedCdpVms': 0, 'hostedFreeManagedWorkstations':
            0, 'hostedFreeManagedServerAgents': 0, 'hostedWindowsServerOsPrice': 0,
            'hostedWindowsClientOsPrice': 0, 'hostedLinuxOsPrice': 0, 'hostedMacOsPrice': 0,
            'hostedBackupUsedSpacePrice': 0, 'hostedBackupUsedSpaceUnits': 'GB',
            'hostedFreeBackupUsedSpace': None, 'hostedFreeBackupUsedSpaceUnits': 'GB',
            'hostedRepositorySpaceUsageAlgorithm': 'Consumed', 'hostedRepositoryAllocatedSpacePrice':
            0, 'hostedRepositoryAllocatedSpaceUnits': 'GB', 'hostedRoundUpBackupUsedSpace': False,
            'hostedBackupUsedSpaceChunkSize': 1, 'useRepositoryUsageByLabelHosted': True,
            'useRepositoryUsageByLabelRemote': False, 'repositoryUsageByLabel': {'hosted':
            [{'labelUid': '8f3c9d21-5b47-4e6a-9c12-7d8a0f4b1e63', 'price': 12, 'priceMeasure': 'TB',
            'freeOfCharge': 100, 'freeOfChargeMeasure': 'GB', 'chunkSize': 1, 'roundUpPerChunk': True,
            'enabled': True}], 'remote': []}}, 'publicCloud': {'remoteCloudVmPrice': 0,
            'remoteFreeCloudVms': 0, 'remoteCloudFileSharePrice': 0, 'remoteFreeCloudFileShares': 0,
            'remoteCloudDatabasePrice': 0, 'remoteFreeCloudDatabases': 0, 'remoteCloudNetworkPrice':
            0, 'remoteBackupUsedSpacePrice': 0, 'remoteBackupUsedSpaceUnits': 'GB',
            'remoteFreeBackupUsedSpace': None, 'remoteFreeBackupUsedSpaceUnits': 'GB',
            'remoteArchiveUsedSpacePrice': 0, 'remoteArchiveUsedSpaceUnits': 'GB',
            'remoteFreeArchiveUsedSpace': None, 'remoteFreeArchiveUsedSpaceUnits': 'GB',
            'hostedCloudVmPrice': 0, 'hostedFreeCloudVms': 0, 'hostedCloudFileSharePrice': 0,
            'hostedFreeCloudFileShares': 0, 'hostedCloudDatabasePrice': 0, 'hostedFreeCloudDatabases':
            0, 'hostedCloudNetworkPrice': 0, 'hostedBackupUsedSpacePrice': 0,
            'hostedBackupUsedSpaceUnits': 'GB', 'hostedFreeBackupUsedSpace': None,
            'hostedFreeBackupUsedSpaceUnits': 'GB', 'hostedArchiveUsedSpacePrice': 0,
            'hostedArchiveUsedSpaceUnits': 'GB', 'hostedFreeArchiveUsedSpace': None,
            'hostedFreeArchiveUsedSpaceUnits': 'GB'}, 'vb365': {'remoteSubscriptionUserPrice': 0,
            'remoteFreeSubscriptionUsers': 0, 'remoteEducationalUserPrice': 0,
            'remoteFreeEducationalUsers': 0, 'remoteRoundUpUsedSpace': False,
            'remoteStandardStorageUsedSpacePrice': 0, 'remoteStandardStorageUsedSpaceChunkSize': 1,
            'remoteStandardStorageUsedSpaceUnits': 'GB', 'remoteFreeStandardStorageUsedSpace': None,
            'remoteFreeStandardStorageUsedSpaceUnits': 'GB', 'remoteArchiveStorageUsedSpacePrice': 0,
            'remoteArchiveStorageUsedSpaceChunkSize': 1, 'remoteArchiveStorageUsedSpaceUnits': 'GB',
            'remoteFreeArchiveStorageUsedSpace': None, 'remoteFreeArchiveStorageUsedSpaceUnits': 'GB',
            'remoteRepositorySpaceUsageAlgorithm': 'Consumed', 'remoteRepositoryAllocatedSpacePrice':
            0, 'remoteRepositoryAllocatedSpaceUnits': 'GB', 'hostedSubscriptionUserPrice': 0,
            'hostedFreeSubscriptionUsers': 0, 'hostedEducationalUserPrice': 0,
            'hostedFreeEducationalUsers': 0, 'hostedRoundUpUsedSpace': False,
            'hostedStandardStorageUsedSpacePrice': 0, 'hostedStandardStorageUsedSpaceChunkSize': 1,
            'hostedStandardStorageUsedSpaceUnits': 'GB', 'hostedFreeStandardStorageUsedSpace': None,
            'hostedFreeStandardStorageUsedSpaceUnits': 'GB', 'hostedArchiveStorageUsedSpacePrice': 0,
            'hostedArchiveStorageUsedSpaceChunkSize': 1, 'hostedArchiveStorageUsedSpaceUnits': 'GB',
            'hostedFreeArchiveStorageUsedSpace': None, 'hostedFreeArchiveStorageUsedSpaceUnits': 'GB',
            'hostedRepositorySpaceUsageAlgorithm': 'Consumed', 'hostedRepositoryAllocatedSpacePrice':
            0, 'hostedRepositoryAllocatedSpaceUnits': 'GB'}, 'cloudReplication': {'replicatedVmPrice':
            10, 'cloudStorageConsumedSpacePrice': 10, 'cloudStorageConsumedSpaceUnits': 'TB',
            'freeCloudStorageConsumedSpace': None, 'freeCloudStorageConsumedSpaceUnits': 'GB',
            'computeResourcesPrice': 0, 'computeResourcesUnits': 'Hours', 'freeComputeResources': 1,
            'freeComputeResourcesUnits': 'Hours', 'replicationDataTransferOutPrice': 0,
            'replicationDataTransferOutUnits': 'GB'}, 'fileShareBackup':
            {'fileShareRemoteBackupUsedSpacePrice': 0, 'fileShareRemoteBackupUsedSpaceUnits': 'GB',
            'freeFileShareRemoteBackupUsedSpace': None, 'freeFileShareRemoteBackupUsedSpaceUnits':
            'GB', 'fileShareRemoteArchiveUsedSpacePrice': 0, 'fileShareRemoteArchiveUsedSpaceUnits':
            'GB', 'freeFileShareRemoteArchiveUsedSpace': None,
            'freeFileShareRemoteArchiveUsedSpaceUnits': 'GB', 'sourceRemoteAmountOfDataPrice': 0,
            'sourceRemoteAmountOfDataUnits': 'GB', 'freeSourceRemoteAmountOfData': None,
            'freeSourceRemoteAmountOfDataUnits': 'GB', 'fileShareHostedBackupUsedSpacePrice': 0,
            'fileShareHostedBackupUsedSpaceUnits': 'GB', 'freeFileShareHostedBackupUsedSpace': None,
            'freeFileShareHostedBackupUsedSpaceUnits': 'GB', 'fileShareHostedArchiveUsedSpacePrice':
            0, 'fileShareHostedArchiveUsedSpaceUnits': 'GB', 'freeFileShareHostedArchiveUsedSpace':
            None, 'freeFileShareHostedArchiveUsedSpaceUnits': 'GB', 'sourceHostedAmountOfDataPrice':
            0, 'sourceHostedAmountOfDataUnits': 'GB', 'freeSourceHostedAmountOfData': None,
            'freeSourceHostedAmountOfDataUnits': 'GB'}, 'cloudBackup': {'roundUpUsedSpace': False,
            'vmCloudBackupsPrice': 5, 'serverCloudBackupsPrice': 6, 'workstationCloudBackupsPrice': 7,
            'cloudRepositorySpaceUsageAlgorithm': 'Consumed', 'cloudRepositoryAllocatedSpacePrice': 0,
            'cloudRepositoryAllocatedSpaceUnits': 'GB', 'cloudRepositoryConsumedSpacePrice': 15,
            'cloudRepositoryConsumedSpaceChunkSize': 1, 'cloudRepositoryConsumedSpaceUnits': 'TB',
            'freeCloudRepositoryConsumedSpace': None, 'freeCloudRepositoryConsumedSpaceUnits': 'GB',
            'backupDataTransferOutPrice': 8, 'backupDataTransferOutUnits': 'GB',
            'insiderProtectionUsedSpacePrice': 0, 'insiderProtectionUsedSpaceUnits': 'GB',
            'performanceTierUsedSpacePrice': 0, 'performanceTierUsedSpaceChunkSize': 1,
            'performanceTierUsedSpaceUnits': 'GB', 'capacityTierUsedSpacePrice': 0,
            'capacityTierUsedSpaceChunkSize': 1, 'capacityTierUsedSpaceUnits': 'GB',
            'archiveTierUsedSpacePrice': 0, 'archiveTierUsedSpaceChunkSize': 1,
            'archiveTierUsedSpaceUnits': 'GB'}, 'licenses': {'vspcLicenses': {'workstationPrice': 0,
            'serverPrice': 0}, 'backupAndReplicationStandardEditionLicenses': {'vmPrice': 0,
            'workstationPrice': 0, 'serverPrice': 0, 'applicationPrice': 0, 'microsoftEntraIdPrice':
            0, 'fileSharePrice': 0, 'objectStoragePrice': 0, 'cloudVmPrice': 0, 'cloudFileSharePrice':
            0, 'cloudDatabasePrice': 0}, 'backupAndReplicationEnterpriseEditionLicenses': {'vmPrice':
            0, 'workstationPrice': 0, 'serverPrice': 0, 'applicationPrice': 0,
            'microsoftEntraIdPrice': 0, 'fileSharePrice': 0, 'objectStoragePrice': 0, 'cloudVmPrice':
            0, 'cloudFileSharePrice': 0, 'cloudDatabasePrice': 0},
            'backupAndReplicationEnterprisePlusEditionLicenses': {'vmPrice': 0, 'workstationPrice': 0,
            'serverPrice': 0, 'applicationPrice': 0, 'microsoftEntraIdPrice': 0, 'fileSharePrice': 0,
            'objectStoragePrice': 0, 'cloudVmPrice': 0, 'cloudFileSharePrice': 0,
            'cloudDatabasePrice': 0}, 'vdpFoundationPackageLicenses': {'vmPrice': 0,
            'workstationPrice': 0, 'serverPrice': 0, 'applicationPrice': 0, 'microsoftEntraIdPrice':
            0, 'fileSharePrice': 0, 'objectStoragePrice': 0, 'cloudVmPrice': 0, 'cloudFileSharePrice':
            0, 'cloudDatabasePrice': 0}, 'vdpAdvancedPackageLicenses': {'vmPrice': 0,
            'workstationPrice': 0, 'serverPrice': 0, 'applicationPrice': 0, 'microsoftEntraIdPrice':
            0, 'fileSharePrice': 0, 'objectStoragePrice': 0, 'cloudVmPrice': 0, 'cloudFileSharePrice':
            0, 'cloudDatabasePrice': 0}, 'vdpPremiumPackageLicenses': {'vmPrice': 0,
            'workstationPrice': 0, 'serverPrice': 0, 'applicationPrice': 0, 'microsoftEntraIdPrice':
            0, 'fileSharePrice': 0, 'objectStoragePrice': 0, 'cloudVmPrice': 0, 'cloudFileSharePrice':
            0, 'cloudDatabasePrice': 0}, 'cloudConnectLicenses': {'vmBackupPrice': 0,
            'vmReplicaPrice': 0, 'workstationBackupPrice': 0, 'serverBackupPrice': 0},
            'vb365Licenses': {'userPrice': 0}, 'veeamOneLicenses': {'monitoredObjectPrice': 0}},
            'externalPlugins': []}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CreateSubscriptionPlanResponse200 | ErrorResponse]
    """

    kwargs = _get_kwargs(
        body=body,
        select=select,
        x_request_id=x_request_id,
        x_client_version=x_client_version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: SubscriptionPlan,
    select: str | Unset = UNSET,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Any | CreateSubscriptionPlanResponse200 | ErrorResponse | None:
    """Create Subscription Plan

     Creates a subscription plan.

    Args:
        select (str | Unset):
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):
        body (SubscriptionPlan):  Example: {'name': 'Pittsburgh subscription plan', 'description':
            'Subscription plan for Pittsburgh clients', 'currency': 'USD', 'taxType': 'VAT',
            'taxPercent': 10, 'discountPercent': 12, 'managedBackup': {'managedServicePrice': 21,
            'monitoredServicePrice': 0, 'remoteManagedVmPrice': 0, 'remoteManagedCdpVmPrice': 0,
            'remoteManagedWorkstationPrice': 0, 'remoteManagedServerAgentPrice': 0,
            'remoteFreeManagedVms': 0, 'remoteFreeManagedCdpVms': 0, 'remoteFreeManagedWorkstations':
            0, 'remoteFreeManagedServerAgents': 0, 'remoteWindowsServerOsPrice': 0,
            'remoteWindowsClientOsPrice': 0, 'remoteLinuxOsPrice': 0, 'remoteMacOsPrice': 0,
            'remoteBackupUsedSpacePrice': 0, 'remoteBackupUsedSpaceUnits': 'GB',
            'remoteFreeBackupUsedSpace': None, 'remoteFreeBackupUsedSpaceUnits': 'GB',
            'remoteRepositorySpaceUsageAlgorithm': 'Consumed', 'remoteRepositoryAllocatedSpacePrice':
            0, 'remoteRepositoryAllocatedSpaceUnits': 'GB', 'remoteRoundUpBackupUsedSpace': False,
            'remoteBackupUsedSpaceChunkSize': 1, 'hostedManagedVmPrice': 0, 'hostedManagedCdpVmPrice':
            0, 'hostedManagedWorkstationPrice': 0, 'hostedManagedServerAgentPrice': 0,
            'hostedFreeManagedVms': 0, 'hostedFreeManagedCdpVms': 0, 'hostedFreeManagedWorkstations':
            0, 'hostedFreeManagedServerAgents': 0, 'hostedWindowsServerOsPrice': 0,
            'hostedWindowsClientOsPrice': 0, 'hostedLinuxOsPrice': 0, 'hostedMacOsPrice': 0,
            'hostedBackupUsedSpacePrice': 0, 'hostedBackupUsedSpaceUnits': 'GB',
            'hostedFreeBackupUsedSpace': None, 'hostedFreeBackupUsedSpaceUnits': 'GB',
            'hostedRepositorySpaceUsageAlgorithm': 'Consumed', 'hostedRepositoryAllocatedSpacePrice':
            0, 'hostedRepositoryAllocatedSpaceUnits': 'GB', 'hostedRoundUpBackupUsedSpace': False,
            'hostedBackupUsedSpaceChunkSize': 1, 'useRepositoryUsageByLabelHosted': True,
            'useRepositoryUsageByLabelRemote': False, 'repositoryUsageByLabel': {'hosted':
            [{'labelUid': '8f3c9d21-5b47-4e6a-9c12-7d8a0f4b1e63', 'price': 12, 'priceMeasure': 'TB',
            'freeOfCharge': 100, 'freeOfChargeMeasure': 'GB', 'chunkSize': 1, 'roundUpPerChunk': True,
            'enabled': True}], 'remote': []}}, 'publicCloud': {'remoteCloudVmPrice': 0,
            'remoteFreeCloudVms': 0, 'remoteCloudFileSharePrice': 0, 'remoteFreeCloudFileShares': 0,
            'remoteCloudDatabasePrice': 0, 'remoteFreeCloudDatabases': 0, 'remoteCloudNetworkPrice':
            0, 'remoteBackupUsedSpacePrice': 0, 'remoteBackupUsedSpaceUnits': 'GB',
            'remoteFreeBackupUsedSpace': None, 'remoteFreeBackupUsedSpaceUnits': 'GB',
            'remoteArchiveUsedSpacePrice': 0, 'remoteArchiveUsedSpaceUnits': 'GB',
            'remoteFreeArchiveUsedSpace': None, 'remoteFreeArchiveUsedSpaceUnits': 'GB',
            'hostedCloudVmPrice': 0, 'hostedFreeCloudVms': 0, 'hostedCloudFileSharePrice': 0,
            'hostedFreeCloudFileShares': 0, 'hostedCloudDatabasePrice': 0, 'hostedFreeCloudDatabases':
            0, 'hostedCloudNetworkPrice': 0, 'hostedBackupUsedSpacePrice': 0,
            'hostedBackupUsedSpaceUnits': 'GB', 'hostedFreeBackupUsedSpace': None,
            'hostedFreeBackupUsedSpaceUnits': 'GB', 'hostedArchiveUsedSpacePrice': 0,
            'hostedArchiveUsedSpaceUnits': 'GB', 'hostedFreeArchiveUsedSpace': None,
            'hostedFreeArchiveUsedSpaceUnits': 'GB'}, 'vb365': {'remoteSubscriptionUserPrice': 0,
            'remoteFreeSubscriptionUsers': 0, 'remoteEducationalUserPrice': 0,
            'remoteFreeEducationalUsers': 0, 'remoteRoundUpUsedSpace': False,
            'remoteStandardStorageUsedSpacePrice': 0, 'remoteStandardStorageUsedSpaceChunkSize': 1,
            'remoteStandardStorageUsedSpaceUnits': 'GB', 'remoteFreeStandardStorageUsedSpace': None,
            'remoteFreeStandardStorageUsedSpaceUnits': 'GB', 'remoteArchiveStorageUsedSpacePrice': 0,
            'remoteArchiveStorageUsedSpaceChunkSize': 1, 'remoteArchiveStorageUsedSpaceUnits': 'GB',
            'remoteFreeArchiveStorageUsedSpace': None, 'remoteFreeArchiveStorageUsedSpaceUnits': 'GB',
            'remoteRepositorySpaceUsageAlgorithm': 'Consumed', 'remoteRepositoryAllocatedSpacePrice':
            0, 'remoteRepositoryAllocatedSpaceUnits': 'GB', 'hostedSubscriptionUserPrice': 0,
            'hostedFreeSubscriptionUsers': 0, 'hostedEducationalUserPrice': 0,
            'hostedFreeEducationalUsers': 0, 'hostedRoundUpUsedSpace': False,
            'hostedStandardStorageUsedSpacePrice': 0, 'hostedStandardStorageUsedSpaceChunkSize': 1,
            'hostedStandardStorageUsedSpaceUnits': 'GB', 'hostedFreeStandardStorageUsedSpace': None,
            'hostedFreeStandardStorageUsedSpaceUnits': 'GB', 'hostedArchiveStorageUsedSpacePrice': 0,
            'hostedArchiveStorageUsedSpaceChunkSize': 1, 'hostedArchiveStorageUsedSpaceUnits': 'GB',
            'hostedFreeArchiveStorageUsedSpace': None, 'hostedFreeArchiveStorageUsedSpaceUnits': 'GB',
            'hostedRepositorySpaceUsageAlgorithm': 'Consumed', 'hostedRepositoryAllocatedSpacePrice':
            0, 'hostedRepositoryAllocatedSpaceUnits': 'GB'}, 'cloudReplication': {'replicatedVmPrice':
            10, 'cloudStorageConsumedSpacePrice': 10, 'cloudStorageConsumedSpaceUnits': 'TB',
            'freeCloudStorageConsumedSpace': None, 'freeCloudStorageConsumedSpaceUnits': 'GB',
            'computeResourcesPrice': 0, 'computeResourcesUnits': 'Hours', 'freeComputeResources': 1,
            'freeComputeResourcesUnits': 'Hours', 'replicationDataTransferOutPrice': 0,
            'replicationDataTransferOutUnits': 'GB'}, 'fileShareBackup':
            {'fileShareRemoteBackupUsedSpacePrice': 0, 'fileShareRemoteBackupUsedSpaceUnits': 'GB',
            'freeFileShareRemoteBackupUsedSpace': None, 'freeFileShareRemoteBackupUsedSpaceUnits':
            'GB', 'fileShareRemoteArchiveUsedSpacePrice': 0, 'fileShareRemoteArchiveUsedSpaceUnits':
            'GB', 'freeFileShareRemoteArchiveUsedSpace': None,
            'freeFileShareRemoteArchiveUsedSpaceUnits': 'GB', 'sourceRemoteAmountOfDataPrice': 0,
            'sourceRemoteAmountOfDataUnits': 'GB', 'freeSourceRemoteAmountOfData': None,
            'freeSourceRemoteAmountOfDataUnits': 'GB', 'fileShareHostedBackupUsedSpacePrice': 0,
            'fileShareHostedBackupUsedSpaceUnits': 'GB', 'freeFileShareHostedBackupUsedSpace': None,
            'freeFileShareHostedBackupUsedSpaceUnits': 'GB', 'fileShareHostedArchiveUsedSpacePrice':
            0, 'fileShareHostedArchiveUsedSpaceUnits': 'GB', 'freeFileShareHostedArchiveUsedSpace':
            None, 'freeFileShareHostedArchiveUsedSpaceUnits': 'GB', 'sourceHostedAmountOfDataPrice':
            0, 'sourceHostedAmountOfDataUnits': 'GB', 'freeSourceHostedAmountOfData': None,
            'freeSourceHostedAmountOfDataUnits': 'GB'}, 'cloudBackup': {'roundUpUsedSpace': False,
            'vmCloudBackupsPrice': 5, 'serverCloudBackupsPrice': 6, 'workstationCloudBackupsPrice': 7,
            'cloudRepositorySpaceUsageAlgorithm': 'Consumed', 'cloudRepositoryAllocatedSpacePrice': 0,
            'cloudRepositoryAllocatedSpaceUnits': 'GB', 'cloudRepositoryConsumedSpacePrice': 15,
            'cloudRepositoryConsumedSpaceChunkSize': 1, 'cloudRepositoryConsumedSpaceUnits': 'TB',
            'freeCloudRepositoryConsumedSpace': None, 'freeCloudRepositoryConsumedSpaceUnits': 'GB',
            'backupDataTransferOutPrice': 8, 'backupDataTransferOutUnits': 'GB',
            'insiderProtectionUsedSpacePrice': 0, 'insiderProtectionUsedSpaceUnits': 'GB',
            'performanceTierUsedSpacePrice': 0, 'performanceTierUsedSpaceChunkSize': 1,
            'performanceTierUsedSpaceUnits': 'GB', 'capacityTierUsedSpacePrice': 0,
            'capacityTierUsedSpaceChunkSize': 1, 'capacityTierUsedSpaceUnits': 'GB',
            'archiveTierUsedSpacePrice': 0, 'archiveTierUsedSpaceChunkSize': 1,
            'archiveTierUsedSpaceUnits': 'GB'}, 'licenses': {'vspcLicenses': {'workstationPrice': 0,
            'serverPrice': 0}, 'backupAndReplicationStandardEditionLicenses': {'vmPrice': 0,
            'workstationPrice': 0, 'serverPrice': 0, 'applicationPrice': 0, 'microsoftEntraIdPrice':
            0, 'fileSharePrice': 0, 'objectStoragePrice': 0, 'cloudVmPrice': 0, 'cloudFileSharePrice':
            0, 'cloudDatabasePrice': 0}, 'backupAndReplicationEnterpriseEditionLicenses': {'vmPrice':
            0, 'workstationPrice': 0, 'serverPrice': 0, 'applicationPrice': 0,
            'microsoftEntraIdPrice': 0, 'fileSharePrice': 0, 'objectStoragePrice': 0, 'cloudVmPrice':
            0, 'cloudFileSharePrice': 0, 'cloudDatabasePrice': 0},
            'backupAndReplicationEnterprisePlusEditionLicenses': {'vmPrice': 0, 'workstationPrice': 0,
            'serverPrice': 0, 'applicationPrice': 0, 'microsoftEntraIdPrice': 0, 'fileSharePrice': 0,
            'objectStoragePrice': 0, 'cloudVmPrice': 0, 'cloudFileSharePrice': 0,
            'cloudDatabasePrice': 0}, 'vdpFoundationPackageLicenses': {'vmPrice': 0,
            'workstationPrice': 0, 'serverPrice': 0, 'applicationPrice': 0, 'microsoftEntraIdPrice':
            0, 'fileSharePrice': 0, 'objectStoragePrice': 0, 'cloudVmPrice': 0, 'cloudFileSharePrice':
            0, 'cloudDatabasePrice': 0}, 'vdpAdvancedPackageLicenses': {'vmPrice': 0,
            'workstationPrice': 0, 'serverPrice': 0, 'applicationPrice': 0, 'microsoftEntraIdPrice':
            0, 'fileSharePrice': 0, 'objectStoragePrice': 0, 'cloudVmPrice': 0, 'cloudFileSharePrice':
            0, 'cloudDatabasePrice': 0}, 'vdpPremiumPackageLicenses': {'vmPrice': 0,
            'workstationPrice': 0, 'serverPrice': 0, 'applicationPrice': 0, 'microsoftEntraIdPrice':
            0, 'fileSharePrice': 0, 'objectStoragePrice': 0, 'cloudVmPrice': 0, 'cloudFileSharePrice':
            0, 'cloudDatabasePrice': 0}, 'cloudConnectLicenses': {'vmBackupPrice': 0,
            'vmReplicaPrice': 0, 'workstationBackupPrice': 0, 'serverBackupPrice': 0},
            'vb365Licenses': {'userPrice': 0}, 'veeamOneLicenses': {'monitoredObjectPrice': 0}},
            'externalPlugins': []}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CreateSubscriptionPlanResponse200 | ErrorResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            select=select,
            x_request_id=x_request_id,
            x_client_version=x_client_version,
        )
    ).parsed
