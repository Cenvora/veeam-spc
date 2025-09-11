from collections.abc import Mapping
from typing import Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UserBackupResourceInput")


@_attrs_define
class UserBackupResourceInput:
    """
    Attributes:
        tenant_backup_resource_uid (UUID): UID assigned to a tenant backup resource.
        resource_friendly_name (str): Friendly name of a subtenant backup resource.
        site_uid (Union[Unset, UUID]): UID assigned to a Veeam Cloud Connect site.
            > You can provide the `null` value only if a single tenant is assigned to a company. Otherwise, the server will
            return an error.'
        description (Union[Unset, str]): Subtenant user description.
        vcd_user_id (Union[Unset, str]): UID assigned to a VMware Cloud Director organization user account.
        storage_quota (Union[Unset, int]): Subtenant quota, in bytes.
        is_storage_quota_unlimited (Union[Unset, bool]): Defines whether a subtenant has unlimited quota. Default: True.
    """

    tenant_backup_resource_uid: UUID
    resource_friendly_name: str
    site_uid: Union[Unset, UUID] = UNSET
    description: Union[Unset, str] = UNSET
    vcd_user_id: Union[Unset, str] = UNSET
    storage_quota: Union[Unset, int] = UNSET
    is_storage_quota_unlimited: Union[Unset, bool] = True
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        tenant_backup_resource_uid = str(self.tenant_backup_resource_uid)

        resource_friendly_name = self.resource_friendly_name

        site_uid: Union[Unset, str] = UNSET
        if not isinstance(self.site_uid, Unset):
            site_uid = str(self.site_uid)

        description = self.description

        vcd_user_id = self.vcd_user_id

        storage_quota = self.storage_quota

        is_storage_quota_unlimited = self.is_storage_quota_unlimited

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "tenantBackupResourceUid": tenant_backup_resource_uid,
                "resourceFriendlyName": resource_friendly_name,
            }
        )
        if site_uid is not UNSET:
            field_dict["siteUid"] = site_uid
        if description is not UNSET:
            field_dict["description"] = description
        if vcd_user_id is not UNSET:
            field_dict["vcdUserId"] = vcd_user_id
        if storage_quota is not UNSET:
            field_dict["storageQuota"] = storage_quota
        if is_storage_quota_unlimited is not UNSET:
            field_dict["isStorageQuotaUnlimited"] = is_storage_quota_unlimited

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        tenant_backup_resource_uid = UUID(d.pop("tenantBackupResourceUid"))

        resource_friendly_name = d.pop("resourceFriendlyName")

        _site_uid = d.pop("siteUid", UNSET)
        site_uid: Union[Unset, UUID]
        if isinstance(_site_uid, Unset):
            site_uid = UNSET
        else:
            site_uid = UUID(_site_uid)

        description = d.pop("description", UNSET)

        vcd_user_id = d.pop("vcdUserId", UNSET)

        storage_quota = d.pop("storageQuota", UNSET)

        is_storage_quota_unlimited = d.pop("isStorageQuotaUnlimited", UNSET)

        user_backup_resource_input = cls(
            tenant_backup_resource_uid=tenant_backup_resource_uid,
            resource_friendly_name=resource_friendly_name,
            site_uid=site_uid,
            description=description,
            vcd_user_id=vcd_user_id,
            storage_quota=storage_quota,
            is_storage_quota_unlimited=is_storage_quota_unlimited,
        )

        user_backup_resource_input.additional_properties = d
        return user_backup_resource_input

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
