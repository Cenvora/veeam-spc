from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.reseller_cloud_connect_quota_type_0_throttling_unit import ResellerCloudConnectQuotaType0ThrottlingUnit
from ..types import UNSET, Unset

T = TypeVar("T", bound="ResellerCloudConnectQuotaType0")


@_attrs_define
class ResellerCloudConnectQuotaType0:
    """Veeam Cloud Connect resources provided to a reseller.
    > If you do not provide the `null` value for this property during reseller creation, you will not be able to change
    it to `null`.

        Attributes:
            data_transfer_out_quota (Union[None, Unset, int]): Maximum amount of data transfer out traffic available to a
                reseller, in bytes.
                > If quota is unlimited, the property value is `null`.
            insider_protection_quota (Union[None, Unset, int]): Number of days during which deleted backup files of reseller
                clients must be kept in the recycle bin by the service provider.
                > If quota is unlimited, the property value is `null`.
                 Default: 1.
            throttling_value (Union[None, Unset, int]): Maximum amount of incoming network traffic accepted from reseller
                clients.
                > If throttling is disabled, the property value is `null`.
                 Default: 1.
            throttling_unit (Union[Unset, ResellerCloudConnectQuotaType0ThrottlingUnit]): Measurement units of the amount of
                incoming network traffic accepted from reseller clients. Default:
                ResellerCloudConnectQuotaType0ThrottlingUnit.MBYTEPERSEC.
            max_concurrent_task (Union[None, Unset, int]): Maximum number of concurrent tasks that reseller clients can
                perform.
                > If concurrent tasks count is unlimited, the property value is `null`.
                 Default: 1.
            is_wan_acceleration_enabled (Union[Unset, bool]): Indicates whether WAN acceleration is enabled for replication
                jobs of reseller clients. Default: False.
    """

    data_transfer_out_quota: Union[None, Unset, int] = UNSET
    insider_protection_quota: Union[None, Unset, int] = 1
    throttling_value: Union[None, Unset, int] = 1
    throttling_unit: Union[Unset, ResellerCloudConnectQuotaType0ThrottlingUnit] = (
        ResellerCloudConnectQuotaType0ThrottlingUnit.MBYTEPERSEC
    )
    max_concurrent_task: Union[None, Unset, int] = 1
    is_wan_acceleration_enabled: Union[Unset, bool] = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data_transfer_out_quota: Union[None, Unset, int]
        if isinstance(self.data_transfer_out_quota, Unset):
            data_transfer_out_quota = UNSET
        else:
            data_transfer_out_quota = self.data_transfer_out_quota

        insider_protection_quota: Union[None, Unset, int]
        if isinstance(self.insider_protection_quota, Unset):
            insider_protection_quota = UNSET
        else:
            insider_protection_quota = self.insider_protection_quota

        throttling_value: Union[None, Unset, int]
        if isinstance(self.throttling_value, Unset):
            throttling_value = UNSET
        else:
            throttling_value = self.throttling_value

        throttling_unit: Union[Unset, str] = UNSET
        if not isinstance(self.throttling_unit, Unset):
            throttling_unit = self.throttling_unit.value

        max_concurrent_task: Union[None, Unset, int]
        if isinstance(self.max_concurrent_task, Unset):
            max_concurrent_task = UNSET
        else:
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

        def _parse_data_transfer_out_quota(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        data_transfer_out_quota = _parse_data_transfer_out_quota(d.pop("dataTransferOutQuota", UNSET))

        def _parse_insider_protection_quota(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        insider_protection_quota = _parse_insider_protection_quota(d.pop("insiderProtectionQuota", UNSET))

        def _parse_throttling_value(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        throttling_value = _parse_throttling_value(d.pop("throttlingValue", UNSET))

        _throttling_unit = d.pop("throttlingUnit", UNSET)
        throttling_unit: Union[Unset, ResellerCloudConnectQuotaType0ThrottlingUnit]
        if isinstance(_throttling_unit, Unset):
            throttling_unit = UNSET
        else:
            throttling_unit = ResellerCloudConnectQuotaType0ThrottlingUnit(_throttling_unit)

        def _parse_max_concurrent_task(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        max_concurrent_task = _parse_max_concurrent_task(d.pop("maxConcurrentTask", UNSET))

        is_wan_acceleration_enabled = d.pop("isWanAccelerationEnabled", UNSET)

        reseller_cloud_connect_quota_type_0 = cls(
            data_transfer_out_quota=data_transfer_out_quota,
            insider_protection_quota=insider_protection_quota,
            throttling_value=throttling_value,
            throttling_unit=throttling_unit,
            max_concurrent_task=max_concurrent_task,
            is_wan_acceleration_enabled=is_wan_acceleration_enabled,
        )

        reseller_cloud_connect_quota_type_0.additional_properties = d
        return reseller_cloud_connect_quota_type_0

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
