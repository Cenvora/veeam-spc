from collections.abc import Mapping
from typing import Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.reseller_quota_throttling_unit import ResellerQuotaThrottlingUnit
from ..types import UNSET, Unset

T = TypeVar("T", bound="ResellerQuota")


@_attrs_define
class ResellerQuota:
    """
    Attributes:
        reseller_uid (Union[Unset, UUID]): UID assigned to a reseller.
        servers_quota (Union[Unset, int]): Maximum number of client servers that a reseller can manage.
            > If quota is unlimited, the property value is 0.
        is_servers_quota_unlimited (Union[Unset, bool]): Indicates whether a reseller can manage an unlimited number of
            company servers. Default: True.
        workstations_quota (Union[Unset, int]): Maximum number of client workstations that a reseller can manage.
            > If quota is unlimited, the property value is 0.
        is_workstations_quota_unlimited (Union[Unset, bool]): Indicates whether a reseller can manage an unlimited
            number of company workstations. Default: True.
        data_transfer_out_quota (Union[Unset, int]): Maximum amount of data transfer out traffic available to a
            reseller, in bytes.
            > If quota is unlimited, the property value is 0.'
        is_data_transfer_out_quota_unlimited (Union[Unset, bool]): Indicates whether the amount of data transfer out
            traffic available to a reseller is unlimited. Default: True.
        insider_protection_quota (Union[Unset, int]): Number of days during which deleted backup files of reseller
            clients must be kept in the recycle bin by the service provider. Default: 0.
        is_wan_acceleration_enabled (Union[Unset, bool]): Indicates whether WAN acceleration is enabled for replication
            jobs of reseller clients. Default: False.
        is_file_level_restore_enabled (Union[Unset, bool]): Indicates whether file-level restore is available to
            reseller clients. Default: False.
        is_throttling_enabled (Union[Unset, bool]): Indicates whether incoming network traffic accepted from reseller
            clients is limited. Default: False.
        throttling_value (Union[Unset, int]): Maximum amount of incoming network traffic accepted from reseller clients.
            Default: 1.
        throttling_unit (Union[Unset, ResellerQuotaThrottlingUnit]): Measurement units of the amount of incoming network
            traffic accepted from reseller clients. Default: ResellerQuotaThrottlingUnit.MBYTEPERSEC.
        is_bandwidth_unlimited (Union[Unset, bool]): Indicates whether a number of concurrent tasks performed by
            reseller clients is limited. Default: True.
        max_concurrent_task (Union[Unset, int]): Maximum number of concurrent tasks that reseller clients can perform.
            Default: 1.
        is_vb_public_cloud_management_enabled (Union[Unset, bool]): Indicates whether integration with Veeam products
            for public cloud protection is available to users. Default: True.
    """

    reseller_uid: Union[Unset, UUID] = UNSET
    servers_quota: Union[Unset, int] = UNSET
    is_servers_quota_unlimited: Union[Unset, bool] = True
    workstations_quota: Union[Unset, int] = UNSET
    is_workstations_quota_unlimited: Union[Unset, bool] = True
    data_transfer_out_quota: Union[Unset, int] = UNSET
    is_data_transfer_out_quota_unlimited: Union[Unset, bool] = True
    insider_protection_quota: Union[Unset, int] = 0
    is_wan_acceleration_enabled: Union[Unset, bool] = False
    is_file_level_restore_enabled: Union[Unset, bool] = False
    is_throttling_enabled: Union[Unset, bool] = False
    throttling_value: Union[Unset, int] = 1
    throttling_unit: Union[Unset, ResellerQuotaThrottlingUnit] = ResellerQuotaThrottlingUnit.MBYTEPERSEC
    is_bandwidth_unlimited: Union[Unset, bool] = True
    max_concurrent_task: Union[Unset, int] = 1
    is_vb_public_cloud_management_enabled: Union[Unset, bool] = True
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        reseller_uid: Union[Unset, str] = UNSET
        if not isinstance(self.reseller_uid, Unset):
            reseller_uid = str(self.reseller_uid)

        servers_quota = self.servers_quota

        is_servers_quota_unlimited = self.is_servers_quota_unlimited

        workstations_quota = self.workstations_quota

        is_workstations_quota_unlimited = self.is_workstations_quota_unlimited

        data_transfer_out_quota = self.data_transfer_out_quota

        is_data_transfer_out_quota_unlimited = self.is_data_transfer_out_quota_unlimited

        insider_protection_quota = self.insider_protection_quota

        is_wan_acceleration_enabled = self.is_wan_acceleration_enabled

        is_file_level_restore_enabled = self.is_file_level_restore_enabled

        is_throttling_enabled = self.is_throttling_enabled

        throttling_value = self.throttling_value

        throttling_unit: Union[Unset, str] = UNSET
        if not isinstance(self.throttling_unit, Unset):
            throttling_unit = self.throttling_unit.value

        is_bandwidth_unlimited = self.is_bandwidth_unlimited

        max_concurrent_task = self.max_concurrent_task

        is_vb_public_cloud_management_enabled = self.is_vb_public_cloud_management_enabled

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if reseller_uid is not UNSET:
            field_dict["resellerUid"] = reseller_uid
        if servers_quota is not UNSET:
            field_dict["serversQuota"] = servers_quota
        if is_servers_quota_unlimited is not UNSET:
            field_dict["isServersQuotaUnlimited"] = is_servers_quota_unlimited
        if workstations_quota is not UNSET:
            field_dict["workstationsQuota"] = workstations_quota
        if is_workstations_quota_unlimited is not UNSET:
            field_dict["isWorkstationsQuotaUnlimited"] = is_workstations_quota_unlimited
        if data_transfer_out_quota is not UNSET:
            field_dict["dataTransferOutQuota"] = data_transfer_out_quota
        if is_data_transfer_out_quota_unlimited is not UNSET:
            field_dict["isDataTransferOutQuotaUnlimited"] = is_data_transfer_out_quota_unlimited
        if insider_protection_quota is not UNSET:
            field_dict["insiderProtectionQuota"] = insider_protection_quota
        if is_wan_acceleration_enabled is not UNSET:
            field_dict["isWanAccelerationEnabled"] = is_wan_acceleration_enabled
        if is_file_level_restore_enabled is not UNSET:
            field_dict["isFileLevelRestoreEnabled"] = is_file_level_restore_enabled
        if is_throttling_enabled is not UNSET:
            field_dict["isThrottlingEnabled"] = is_throttling_enabled
        if throttling_value is not UNSET:
            field_dict["throttlingValue"] = throttling_value
        if throttling_unit is not UNSET:
            field_dict["throttlingUnit"] = throttling_unit
        if is_bandwidth_unlimited is not UNSET:
            field_dict["isBandwidthUnlimited"] = is_bandwidth_unlimited
        if max_concurrent_task is not UNSET:
            field_dict["maxConcurrentTask"] = max_concurrent_task
        if is_vb_public_cloud_management_enabled is not UNSET:
            field_dict["isVbPublicCloudManagementEnabled"] = is_vb_public_cloud_management_enabled

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _reseller_uid = d.pop("resellerUid", UNSET)
        reseller_uid: Union[Unset, UUID]
        if isinstance(_reseller_uid, Unset):
            reseller_uid = UNSET
        else:
            reseller_uid = UUID(_reseller_uid)

        servers_quota = d.pop("serversQuota", UNSET)

        is_servers_quota_unlimited = d.pop("isServersQuotaUnlimited", UNSET)

        workstations_quota = d.pop("workstationsQuota", UNSET)

        is_workstations_quota_unlimited = d.pop("isWorkstationsQuotaUnlimited", UNSET)

        data_transfer_out_quota = d.pop("dataTransferOutQuota", UNSET)

        is_data_transfer_out_quota_unlimited = d.pop("isDataTransferOutQuotaUnlimited", UNSET)

        insider_protection_quota = d.pop("insiderProtectionQuota", UNSET)

        is_wan_acceleration_enabled = d.pop("isWanAccelerationEnabled", UNSET)

        is_file_level_restore_enabled = d.pop("isFileLevelRestoreEnabled", UNSET)

        is_throttling_enabled = d.pop("isThrottlingEnabled", UNSET)

        throttling_value = d.pop("throttlingValue", UNSET)

        _throttling_unit = d.pop("throttlingUnit", UNSET)
        throttling_unit: Union[Unset, ResellerQuotaThrottlingUnit]
        if isinstance(_throttling_unit, Unset):
            throttling_unit = UNSET
        else:
            throttling_unit = ResellerQuotaThrottlingUnit(_throttling_unit)

        is_bandwidth_unlimited = d.pop("isBandwidthUnlimited", UNSET)

        max_concurrent_task = d.pop("maxConcurrentTask", UNSET)

        is_vb_public_cloud_management_enabled = d.pop("isVbPublicCloudManagementEnabled", UNSET)

        reseller_quota = cls(
            reseller_uid=reseller_uid,
            servers_quota=servers_quota,
            is_servers_quota_unlimited=is_servers_quota_unlimited,
            workstations_quota=workstations_quota,
            is_workstations_quota_unlimited=is_workstations_quota_unlimited,
            data_transfer_out_quota=data_transfer_out_quota,
            is_data_transfer_out_quota_unlimited=is_data_transfer_out_quota_unlimited,
            insider_protection_quota=insider_protection_quota,
            is_wan_acceleration_enabled=is_wan_acceleration_enabled,
            is_file_level_restore_enabled=is_file_level_restore_enabled,
            is_throttling_enabled=is_throttling_enabled,
            throttling_value=throttling_value,
            throttling_unit=throttling_unit,
            is_bandwidth_unlimited=is_bandwidth_unlimited,
            max_concurrent_task=max_concurrent_task,
            is_vb_public_cloud_management_enabled=is_vb_public_cloud_management_enabled,
        )

        reseller_quota.additional_properties = d
        return reseller_quota

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
