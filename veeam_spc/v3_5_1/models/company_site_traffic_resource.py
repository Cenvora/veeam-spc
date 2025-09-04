from collections.abc import Mapping
from typing import Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CompanySiteTrafficResource")


@_attrs_define
class CompanySiteTrafficResource:
    """
    Attributes:
        site_uid (Union[Unset, UUID]): UID assigned to a Veeam Cloud Connect site.
        data_transfer_out_quota (Union[Unset, int]): Maximum amount of data transfer out traffic available to a company,
            in bytes.
            > Minimum value is equal to 1 GB. <br>
            > If quota is unlimited, the property value is 0.'
        is_data_transfer_out_quota_unlimited (Union[Unset, bool]): Indicates whether the amount of data transfer out
            traffic available to a company is unlimited. Default: True.
    """

    site_uid: Union[Unset, UUID] = UNSET
    data_transfer_out_quota: Union[Unset, int] = UNSET
    is_data_transfer_out_quota_unlimited: Union[Unset, bool] = True
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        site_uid: Union[Unset, str] = UNSET
        if not isinstance(self.site_uid, Unset):
            site_uid = str(self.site_uid)

        data_transfer_out_quota = self.data_transfer_out_quota

        is_data_transfer_out_quota_unlimited = self.is_data_transfer_out_quota_unlimited

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if site_uid is not UNSET:
            field_dict["siteUid"] = site_uid
        if data_transfer_out_quota is not UNSET:
            field_dict["dataTransferOutQuota"] = data_transfer_out_quota
        if is_data_transfer_out_quota_unlimited is not UNSET:
            field_dict["isDataTransferOutQuotaUnlimited"] = is_data_transfer_out_quota_unlimited

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _site_uid = d.pop("siteUid", UNSET)
        site_uid: Union[Unset, UUID]
        if isinstance(_site_uid, Unset):
            site_uid = UNSET
        else:
            site_uid = UUID(_site_uid)

        data_transfer_out_quota = d.pop("dataTransferOutQuota", UNSET)

        is_data_transfer_out_quota_unlimited = d.pop("isDataTransferOutQuotaUnlimited", UNSET)

        company_site_traffic_resource = cls(
            site_uid=site_uid,
            data_transfer_out_quota=data_transfer_out_quota,
            is_data_transfer_out_quota_unlimited=is_data_transfer_out_quota_unlimited,
        )

        company_site_traffic_resource.additional_properties = d
        return company_site_traffic_resource

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
