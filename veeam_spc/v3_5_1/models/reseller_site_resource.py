from collections.abc import Mapping
from typing import Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ResellerSiteResource")


@_attrs_define
class ResellerSiteResource:
    """
    Example:
        {'siteUid': '38AB1C08-B0DA-4D76-8995-5011DBE96E18', 'tenantsQuota': 20, 'isTenantsQuotaUnlimited': False}

    Attributes:
        site_uid (UUID): UID assigned to a Veeam Cloud Connect site.
        reseller_uid (Union[Unset, UUID]): UID assigned to a reseller.
        tenants_quota (Union[Unset, int]): Maximum number of companies that a reseller can manage on a Veeam Cloud
            Connect site. Default: 20.
        used_tenants_quota (Union[Unset, int]): Number of companies that a reseller manages on a site
        is_tenants_quota_unlimited (Union[Unset, bool]): Indicates whether a reseller has unlimited quota for managed
            companies. Default: False.
    """

    site_uid: UUID
    reseller_uid: Union[Unset, UUID] = UNSET
    tenants_quota: Union[Unset, int] = 20
    used_tenants_quota: Union[Unset, int] = UNSET
    is_tenants_quota_unlimited: Union[Unset, bool] = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        site_uid = str(self.site_uid)

        reseller_uid: Union[Unset, str] = UNSET
        if not isinstance(self.reseller_uid, Unset):
            reseller_uid = str(self.reseller_uid)

        tenants_quota = self.tenants_quota

        used_tenants_quota = self.used_tenants_quota

        is_tenants_quota_unlimited = self.is_tenants_quota_unlimited

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "siteUid": site_uid,
            }
        )
        if reseller_uid is not UNSET:
            field_dict["resellerUid"] = reseller_uid
        if tenants_quota is not UNSET:
            field_dict["tenantsQuota"] = tenants_quota
        if used_tenants_quota is not UNSET:
            field_dict["usedTenantsQuota"] = used_tenants_quota
        if is_tenants_quota_unlimited is not UNSET:
            field_dict["isTenantsQuotaUnlimited"] = is_tenants_quota_unlimited

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        site_uid = UUID(d.pop("siteUid"))

        _reseller_uid = d.pop("resellerUid", UNSET)
        reseller_uid: Union[Unset, UUID]
        if isinstance(_reseller_uid, Unset):
            reseller_uid = UNSET
        else:
            reseller_uid = UUID(_reseller_uid)

        tenants_quota = d.pop("tenantsQuota", UNSET)

        used_tenants_quota = d.pop("usedTenantsQuota", UNSET)

        is_tenants_quota_unlimited = d.pop("isTenantsQuotaUnlimited", UNSET)

        reseller_site_resource = cls(
            site_uid=site_uid,
            reseller_uid=reseller_uid,
            tenants_quota=tenants_quota,
            used_tenants_quota=used_tenants_quota,
            is_tenants_quota_unlimited=is_tenants_quota_unlimited,
        )

        reseller_site_resource.additional_properties = d
        return reseller_site_resource

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
