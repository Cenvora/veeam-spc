from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.subscription_plan_cloud_replication_cloud_storage_consumed_space_units import (
    SubscriptionPlanCloudReplicationCloudStorageConsumedSpaceUnits,
)
from ..models.subscription_plan_cloud_replication_compute_resources_units import (
    SubscriptionPlanCloudReplicationComputeResourcesUnits,
)
from ..models.subscription_plan_cloud_replication_free_cloud_storage_consumed_space_units import (
    SubscriptionPlanCloudReplicationFreeCloudStorageConsumedSpaceUnits,
)
from ..models.subscription_plan_cloud_replication_free_compute_resources_units import (
    SubscriptionPlanCloudReplicationFreeComputeResourcesUnits,
)
from ..models.subscription_plan_cloud_replication_replication_data_transfer_out_units import (
    SubscriptionPlanCloudReplicationReplicationDataTransferOutUnits,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="SubscriptionPlanCloudReplication")


@_attrs_define
class SubscriptionPlanCloudReplication:
    """
    Attributes:
        replicated_vm_price (Union[Unset, float]): Charge rate for one VM replica registered on a cloud host, per month.
            Default: 0.0.
        cloud_storage_consumed_space_price (Union[Unset, float]): Charge rate for one GB or TB of cloud storage space
            consumed by VM replica files. Default: 0.0.
        cloud_storage_consumed_space_units (Union[Unset,
            SubscriptionPlanCloudReplicationCloudStorageConsumedSpaceUnits]): Measurement units of cloud storage space
            consumed by VM replica files. Default: SubscriptionPlanCloudReplicationCloudStorageConsumedSpaceUnits.TB.
        free_cloud_storage_consumed_space (Union[None, Unset, int]): Amount of cloud storage space that can be consumed
            by VM replicas for free.
            > Maximum value is `1048576` for GB and `1024` for TB.
        free_cloud_storage_consumed_space_units (Union[Unset,
            SubscriptionPlanCloudReplicationFreeCloudStorageConsumedSpaceUnits]): Measurement units of cloud storage space
            that can be consumed by VM replicas for free. Default:
            SubscriptionPlanCloudReplicationFreeCloudStorageConsumedSpaceUnits.GB.
        compute_resources_price (Union[Unset, float]): Charge rate for a CPU and memory resources usage by a VM on a
            cloud host. Default: 0.0.
        compute_resources_units (Union[Unset, SubscriptionPlanCloudReplicationComputeResourcesUnits]): Measurement units
            of time period of CPU and memory resources usage by a VM on a cloud host Default:
            SubscriptionPlanCloudReplicationComputeResourcesUnits.HOURS.
        free_compute_resources (Union[Unset, int]): Amount of time during which VM replicas can consume compute
            resources on a cloud host for free. Default: 0.
        free_compute_resources_units (Union[Unset, SubscriptionPlanCloudReplicationFreeComputeResourcesUnits]):
            Measurement units of time during which VM replicas can consume compute resources on a cloud host for free.
            Default: SubscriptionPlanCloudReplicationFreeComputeResourcesUnits.MINUTES.
        replication_data_transfer_out_price (Union[Unset, float]): Charge rate for one GB or TB of VM replica data
            downloaded from cloud storage. Default: 0.0.
        replication_data_transfer_out_units (Union[Unset,
            SubscriptionPlanCloudReplicationReplicationDataTransferOutUnits]): Measurement units of VM replica data
            downloaded from cloud storage. Default: SubscriptionPlanCloudReplicationReplicationDataTransferOutUnits.GB.
    """

    replicated_vm_price: Union[Unset, float] = 0.0
    cloud_storage_consumed_space_price: Union[Unset, float] = 0.0
    cloud_storage_consumed_space_units: Union[Unset, SubscriptionPlanCloudReplicationCloudStorageConsumedSpaceUnits] = (
        SubscriptionPlanCloudReplicationCloudStorageConsumedSpaceUnits.TB
    )
    free_cloud_storage_consumed_space: Union[None, Unset, int] = UNSET
    free_cloud_storage_consumed_space_units: Union[
        Unset, SubscriptionPlanCloudReplicationFreeCloudStorageConsumedSpaceUnits
    ] = SubscriptionPlanCloudReplicationFreeCloudStorageConsumedSpaceUnits.GB
    compute_resources_price: Union[Unset, float] = 0.0
    compute_resources_units: Union[Unset, SubscriptionPlanCloudReplicationComputeResourcesUnits] = (
        SubscriptionPlanCloudReplicationComputeResourcesUnits.HOURS
    )
    free_compute_resources: Union[Unset, int] = 0
    free_compute_resources_units: Union[Unset, SubscriptionPlanCloudReplicationFreeComputeResourcesUnits] = (
        SubscriptionPlanCloudReplicationFreeComputeResourcesUnits.MINUTES
    )
    replication_data_transfer_out_price: Union[Unset, float] = 0.0
    replication_data_transfer_out_units: Union[
        Unset, SubscriptionPlanCloudReplicationReplicationDataTransferOutUnits
    ] = SubscriptionPlanCloudReplicationReplicationDataTransferOutUnits.GB
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        replicated_vm_price = self.replicated_vm_price

        cloud_storage_consumed_space_price = self.cloud_storage_consumed_space_price

        cloud_storage_consumed_space_units: Union[Unset, str] = UNSET
        if not isinstance(self.cloud_storage_consumed_space_units, Unset):
            cloud_storage_consumed_space_units = self.cloud_storage_consumed_space_units.value

        free_cloud_storage_consumed_space: Union[None, Unset, int]
        if isinstance(self.free_cloud_storage_consumed_space, Unset):
            free_cloud_storage_consumed_space = UNSET
        else:
            free_cloud_storage_consumed_space = self.free_cloud_storage_consumed_space

        free_cloud_storage_consumed_space_units: Union[Unset, str] = UNSET
        if not isinstance(self.free_cloud_storage_consumed_space_units, Unset):
            free_cloud_storage_consumed_space_units = self.free_cloud_storage_consumed_space_units.value

        compute_resources_price = self.compute_resources_price

        compute_resources_units: Union[Unset, str] = UNSET
        if not isinstance(self.compute_resources_units, Unset):
            compute_resources_units = self.compute_resources_units.value

        free_compute_resources = self.free_compute_resources

        free_compute_resources_units: Union[Unset, str] = UNSET
        if not isinstance(self.free_compute_resources_units, Unset):
            free_compute_resources_units = self.free_compute_resources_units.value

        replication_data_transfer_out_price = self.replication_data_transfer_out_price

        replication_data_transfer_out_units: Union[Unset, str] = UNSET
        if not isinstance(self.replication_data_transfer_out_units, Unset):
            replication_data_transfer_out_units = self.replication_data_transfer_out_units.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if replicated_vm_price is not UNSET:
            field_dict["replicatedVmPrice"] = replicated_vm_price
        if cloud_storage_consumed_space_price is not UNSET:
            field_dict["cloudStorageConsumedSpacePrice"] = cloud_storage_consumed_space_price
        if cloud_storage_consumed_space_units is not UNSET:
            field_dict["cloudStorageConsumedSpaceUnits"] = cloud_storage_consumed_space_units
        if free_cloud_storage_consumed_space is not UNSET:
            field_dict["freeCloudStorageConsumedSpace"] = free_cloud_storage_consumed_space
        if free_cloud_storage_consumed_space_units is not UNSET:
            field_dict["freeCloudStorageConsumedSpaceUnits"] = free_cloud_storage_consumed_space_units
        if compute_resources_price is not UNSET:
            field_dict["computeResourcesPrice"] = compute_resources_price
        if compute_resources_units is not UNSET:
            field_dict["computeResourcesUnits"] = compute_resources_units
        if free_compute_resources is not UNSET:
            field_dict["freeComputeResources"] = free_compute_resources
        if free_compute_resources_units is not UNSET:
            field_dict["freeComputeResourcesUnits"] = free_compute_resources_units
        if replication_data_transfer_out_price is not UNSET:
            field_dict["replicationDataTransferOutPrice"] = replication_data_transfer_out_price
        if replication_data_transfer_out_units is not UNSET:
            field_dict["replicationDataTransferOutUnits"] = replication_data_transfer_out_units

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        replicated_vm_price = d.pop("replicatedVmPrice", UNSET)

        cloud_storage_consumed_space_price = d.pop("cloudStorageConsumedSpacePrice", UNSET)

        _cloud_storage_consumed_space_units = d.pop("cloudStorageConsumedSpaceUnits", UNSET)
        cloud_storage_consumed_space_units: Union[Unset, SubscriptionPlanCloudReplicationCloudStorageConsumedSpaceUnits]
        if isinstance(_cloud_storage_consumed_space_units, Unset):
            cloud_storage_consumed_space_units = UNSET
        else:
            cloud_storage_consumed_space_units = SubscriptionPlanCloudReplicationCloudStorageConsumedSpaceUnits(
                _cloud_storage_consumed_space_units
            )

        def _parse_free_cloud_storage_consumed_space(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        free_cloud_storage_consumed_space = _parse_free_cloud_storage_consumed_space(
            d.pop("freeCloudStorageConsumedSpace", UNSET)
        )

        _free_cloud_storage_consumed_space_units = d.pop("freeCloudStorageConsumedSpaceUnits", UNSET)
        free_cloud_storage_consumed_space_units: Union[
            Unset, SubscriptionPlanCloudReplicationFreeCloudStorageConsumedSpaceUnits
        ]
        if isinstance(_free_cloud_storage_consumed_space_units, Unset):
            free_cloud_storage_consumed_space_units = UNSET
        else:
            free_cloud_storage_consumed_space_units = (
                SubscriptionPlanCloudReplicationFreeCloudStorageConsumedSpaceUnits(
                    _free_cloud_storage_consumed_space_units
                )
            )

        compute_resources_price = d.pop("computeResourcesPrice", UNSET)

        _compute_resources_units = d.pop("computeResourcesUnits", UNSET)
        compute_resources_units: Union[Unset, SubscriptionPlanCloudReplicationComputeResourcesUnits]
        if isinstance(_compute_resources_units, Unset):
            compute_resources_units = UNSET
        else:
            compute_resources_units = SubscriptionPlanCloudReplicationComputeResourcesUnits(_compute_resources_units)

        free_compute_resources = d.pop("freeComputeResources", UNSET)

        _free_compute_resources_units = d.pop("freeComputeResourcesUnits", UNSET)
        free_compute_resources_units: Union[Unset, SubscriptionPlanCloudReplicationFreeComputeResourcesUnits]
        if isinstance(_free_compute_resources_units, Unset):
            free_compute_resources_units = UNSET
        else:
            free_compute_resources_units = SubscriptionPlanCloudReplicationFreeComputeResourcesUnits(
                _free_compute_resources_units
            )

        replication_data_transfer_out_price = d.pop("replicationDataTransferOutPrice", UNSET)

        _replication_data_transfer_out_units = d.pop("replicationDataTransferOutUnits", UNSET)
        replication_data_transfer_out_units: Union[
            Unset, SubscriptionPlanCloudReplicationReplicationDataTransferOutUnits
        ]
        if isinstance(_replication_data_transfer_out_units, Unset):
            replication_data_transfer_out_units = UNSET
        else:
            replication_data_transfer_out_units = SubscriptionPlanCloudReplicationReplicationDataTransferOutUnits(
                _replication_data_transfer_out_units
            )

        subscription_plan_cloud_replication = cls(
            replicated_vm_price=replicated_vm_price,
            cloud_storage_consumed_space_price=cloud_storage_consumed_space_price,
            cloud_storage_consumed_space_units=cloud_storage_consumed_space_units,
            free_cloud_storage_consumed_space=free_cloud_storage_consumed_space,
            free_cloud_storage_consumed_space_units=free_cloud_storage_consumed_space_units,
            compute_resources_price=compute_resources_price,
            compute_resources_units=compute_resources_units,
            free_compute_resources=free_compute_resources,
            free_compute_resources_units=free_compute_resources_units,
            replication_data_transfer_out_price=replication_data_transfer_out_price,
            replication_data_transfer_out_units=replication_data_transfer_out_units,
        )

        subscription_plan_cloud_replication.additional_properties = d
        return subscription_plan_cloud_replication

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
