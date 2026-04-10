from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TenantTrafficResource")


@_attrs_define
class TenantTrafficResource:
    """
    Attributes:
        site_uid (Union[Unset, UUID]): UID assigned to a Veeam Cloud Connect site.
        tenant_uid (Union[Unset, UUID]): UID assigned to a tenant.
        company_uid (Union[None, UUID, Unset]): UID of a company to which a tenant is assigned. Has the `null` value if
            no tenant is assigned.
        data_transfer_out_quota (Union[None, Unset, int]): Maximum amount of data transfer out traffic available to a
            tenant, in GB.
            > Minimum value is equal to 1 GB. <br>
            > Maximum value is equal to 976 TB. <br>
            > If quota is unlimited, the property value is `null`.'
        is_data_transfer_out_quota_unlimited (Union[Unset, bool]): Indicates whether the amount of data transfer out
            traffic available to a company is unlimited. Default: True.
    """

    site_uid: Union[Unset, UUID] = UNSET
    tenant_uid: Union[Unset, UUID] = UNSET
    company_uid: Union[None, UUID, Unset] = UNSET
    data_transfer_out_quota: Union[None, Unset, int] = UNSET
    is_data_transfer_out_quota_unlimited: Union[Unset, bool] = True
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        site_uid: Union[Unset, str] = UNSET
        if not isinstance(self.site_uid, Unset):
            site_uid = str(self.site_uid)

        tenant_uid: Union[Unset, str] = UNSET
        if not isinstance(self.tenant_uid, Unset):
            tenant_uid = str(self.tenant_uid)

        company_uid: Union[None, Unset, str]
        if isinstance(self.company_uid, Unset):
            company_uid = UNSET
        elif isinstance(self.company_uid, UUID):
            company_uid = str(self.company_uid)
        else:
            company_uid = self.company_uid

        data_transfer_out_quota: Union[None, Unset, int]
        if isinstance(self.data_transfer_out_quota, Unset):
            data_transfer_out_quota = UNSET
        else:
            data_transfer_out_quota = self.data_transfer_out_quota

        is_data_transfer_out_quota_unlimited = self.is_data_transfer_out_quota_unlimited

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if site_uid is not UNSET:
            field_dict["siteUid"] = site_uid
        if tenant_uid is not UNSET:
            field_dict["tenantUid"] = tenant_uid
        if company_uid is not UNSET:
            field_dict["companyUid"] = company_uid
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

        _tenant_uid = d.pop("tenantUid", UNSET)
        tenant_uid: Union[Unset, UUID]
        if isinstance(_tenant_uid, Unset):
            tenant_uid = UNSET
        else:
            tenant_uid = UUID(_tenant_uid)

        def _parse_company_uid(data: object) -> Union[None, UUID, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                company_uid_type_0 = UUID(data)

                return company_uid_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID, Unset], data)

        company_uid = _parse_company_uid(d.pop("companyUid", UNSET))

        def _parse_data_transfer_out_quota(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        data_transfer_out_quota = _parse_data_transfer_out_quota(d.pop("dataTransferOutQuota", UNSET))

        is_data_transfer_out_quota_unlimited = d.pop("isDataTransferOutQuotaUnlimited", UNSET)

        tenant_traffic_resource = cls(
            site_uid=site_uid,
            tenant_uid=tenant_uid,
            company_uid=company_uid,
            data_transfer_out_quota=data_transfer_out_quota,
            is_data_transfer_out_quota_unlimited=is_data_transfer_out_quota_unlimited,
        )

        tenant_traffic_resource.additional_properties = d
        return tenant_traffic_resource

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
