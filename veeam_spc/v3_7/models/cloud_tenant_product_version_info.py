from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.cloud_tenant_product_version_info_product_type import CloudTenantProductVersionInfoProductType
from ..types import UNSET, Unset

T = TypeVar("T", bound="CloudTenantProductVersionInfo")


@_attrs_define
class CloudTenantProductVersionInfo:
    """
    Attributes:
        instance_uid (UUID | Unset): UID assigned to a Veeam product.
        product_type (CloudTenantProductVersionInfoProductType | Unset): Veeam product type.
        version (None | str | Unset): Version of a Veeam product.
        site_uid (UUID | Unset): UID assigned to a Veeam Cloud Connect site managing a tenant that uses a Veeam product.
        company_uid (UUID | Unset): UID assigned to a company associated with a tenant that uses a Veeam product.
        tenant_uid (UUID | Unset): UID assigned to a tenant that uses a Veeam product.
        is_version_info_available (bool | Unset): Indicates whether information on Veeam product version is available.
    """

    instance_uid: UUID | Unset = UNSET
    product_type: CloudTenantProductVersionInfoProductType | Unset = UNSET
    version: None | str | Unset = UNSET
    site_uid: UUID | Unset = UNSET
    company_uid: UUID | Unset = UNSET
    tenant_uid: UUID | Unset = UNSET
    is_version_info_available: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        instance_uid: str | Unset = UNSET
        if not isinstance(self.instance_uid, Unset):
            instance_uid = str(self.instance_uid)

        product_type: str | Unset = UNSET
        if not isinstance(self.product_type, Unset):
            product_type = self.product_type.value

        version: None | str | Unset
        if isinstance(self.version, Unset):
            version = UNSET
        else:
            version = self.version

        site_uid: str | Unset = UNSET
        if not isinstance(self.site_uid, Unset):
            site_uid = str(self.site_uid)

        company_uid: str | Unset = UNSET
        if not isinstance(self.company_uid, Unset):
            company_uid = str(self.company_uid)

        tenant_uid: str | Unset = UNSET
        if not isinstance(self.tenant_uid, Unset):
            tenant_uid = str(self.tenant_uid)

        is_version_info_available = self.is_version_info_available

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if instance_uid is not UNSET:
            field_dict["instanceUid"] = instance_uid
        if product_type is not UNSET:
            field_dict["productType"] = product_type
        if version is not UNSET:
            field_dict["version"] = version
        if site_uid is not UNSET:
            field_dict["siteUid"] = site_uid
        if company_uid is not UNSET:
            field_dict["companyUid"] = company_uid
        if tenant_uid is not UNSET:
            field_dict["tenantUid"] = tenant_uid
        if is_version_info_available is not UNSET:
            field_dict["isVersionInfoAvailable"] = is_version_info_available

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _instance_uid = d.pop("instanceUid", UNSET)
        instance_uid: UUID | Unset
        if isinstance(_instance_uid, Unset):
            instance_uid = UNSET
        else:
            instance_uid = UUID(_instance_uid)

        _product_type = d.pop("productType", UNSET)
        product_type: CloudTenantProductVersionInfoProductType | Unset
        if isinstance(_product_type, Unset):
            product_type = UNSET
        else:
            product_type = CloudTenantProductVersionInfoProductType(_product_type)

        def _parse_version(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        version = _parse_version(d.pop("version", UNSET))

        _site_uid = d.pop("siteUid", UNSET)
        site_uid: UUID | Unset
        if isinstance(_site_uid, Unset):
            site_uid = UNSET
        else:
            site_uid = UUID(_site_uid)

        _company_uid = d.pop("companyUid", UNSET)
        company_uid: UUID | Unset
        if isinstance(_company_uid, Unset):
            company_uid = UNSET
        else:
            company_uid = UUID(_company_uid)

        _tenant_uid = d.pop("tenantUid", UNSET)
        tenant_uid: UUID | Unset
        if isinstance(_tenant_uid, Unset):
            tenant_uid = UNSET
        else:
            tenant_uid = UUID(_tenant_uid)

        is_version_info_available = d.pop("isVersionInfoAvailable", UNSET)

        cloud_tenant_product_version_info = cls(
            instance_uid=instance_uid,
            product_type=product_type,
            version=version,
            site_uid=site_uid,
            company_uid=company_uid,
            tenant_uid=tenant_uid,
            is_version_info_available=is_version_info_available,
        )

        cloud_tenant_product_version_info.additional_properties = d
        return cloud_tenant_product_version_info

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
