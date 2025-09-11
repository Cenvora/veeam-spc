from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.reseller_cloud_connect_quota_throttling_unit import ResellerCloudConnectQuotaThrottlingUnit
from ..types import UNSET, Unset

T = TypeVar("T", bound="ResellerCloudConnectQuota")


@_attrs_define
class ResellerCloudConnectQuota:
    """Veeam Cloud Connect resources provided to a reseller.
    > If you do not provide the `null` value for this property during reseller creation, you will not be able to change
    it to `null`.

        Attributes:
            data_transfer_out_quota (Union[Unset, int]): Maximum amount of data transfer out traffic available to a
                reseller, in bytes.
                > If quota is unlimited, the property value is `null`.
            insider_protection_quota (Union[Unset, int]): Number of days during which deleted backup files of reseller
                clients must be kept in the recycle bin by the service provider.
                > If quota is unlimited, the property value is `null`.
                 Default: 1.
            throttling_value (Union[Unset, int]): Maximum amount of incoming network traffic accepted from reseller clients.
                > If throttling is disabled, the property value is `null`.
                 Default: 1.
            throttling_unit (Union[Unset, ResellerCloudConnectQuotaThrottlingUnit]): Measurement units of the amount of
                incoming network traffic accepted from reseller clients. Default:
                ResellerCloudConnectQuotaThrottlingUnit.MBYTEPERSEC.
            max_concurrent_task (Union[Unset, int]): Maximum number of concurrent tasks that reseller clients can perform.
                > If concurrent tasks count is unlimited, the property value is `null`.
                 Default: 1.
            is_wan_acceleration_enabled (Union[Unset, bool]): Indicates whether WAN acceleration is enabled for replication
                jobs of reseller clients. Default: False.
    """

    data_transfer_out_quota: Union[Unset, int] = UNSET
    insider_protection_quota: Union[Unset, int] = 1
    throttling_value: Union[Unset, int] = 1
    throttling_unit: Union[Unset, ResellerCloudConnectQuotaThrottlingUnit] = (
        ResellerCloudConnectQuotaThrottlingUnit.MBYTEPERSEC
    )
    max_concurrent_task: Union[Unset, int] = 1
    is_wan_acceleration_enabled: Union[Unset, bool] = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data_transfer_out_quota = self.data_transfer_out_quota

        insider_protection_quota = self.insider_protection_quota

        throttling_value = self.throttling_value

        throttling_unit: Union[Unset, str] = UNSET
        if not isinstance(self.throttling_unit, Unset):
            throttling_unit = self.throttling_unit.value

        max_concurrent_task = self.max_concurrent_task

        is_wan_acceleration_enabled = self.is_wan_acceleration_enabled

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if data_transfer_out_quota is not UNSET:
            field_dict["dataTransferOutQuota"] = data_transfer_out_quota
        if insider_protection_quota is not UNSET:
            field_dict["insiderProtectionQuota"] = insider_protection_quota
        if throttling_value is not UNSET:
            field_dict["throttlingValue"] = throttling_value
        if throttling_unit is not UNSET:
            field_dict["throttlingUnit"] = throttling_unit
        if max_concurrent_task is not UNSET:
            field_dict["maxConcurrentTask"] = max_concurrent_task
        if is_wan_acceleration_enabled is not UNSET:
            field_dict["isWanAccelerationEnabled"] = is_wan_acceleration_enabled

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        data_transfer_out_quota = d.pop("dataTransferOutQuota", UNSET)

        insider_protection_quota = d.pop("insiderProtectionQuota", UNSET)

        throttling_value = d.pop("throttlingValue", UNSET)

        _throttling_unit = d.pop("throttlingUnit", UNSET)
        throttling_unit: Union[Unset, ResellerCloudConnectQuotaThrottlingUnit]
        if isinstance(_throttling_unit, Unset):
            throttling_unit = UNSET
        else:
            throttling_unit = ResellerCloudConnectQuotaThrottlingUnit(_throttling_unit)

        max_concurrent_task = d.pop("maxConcurrentTask", UNSET)

        is_wan_acceleration_enabled = d.pop("isWanAccelerationEnabled", UNSET)

        reseller_cloud_connect_quota = cls(
            data_transfer_out_quota=data_transfer_out_quota,
            insider_protection_quota=insider_protection_quota,
            throttling_value=throttling_value,
            throttling_unit=throttling_unit,
            max_concurrent_task=max_concurrent_task,
            is_wan_acceleration_enabled=is_wan_acceleration_enabled,
        )

        reseller_cloud_connect_quota.additional_properties = d
        return reseller_cloud_connect_quota

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
