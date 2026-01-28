from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast
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
        site_uid (Union[None, UUID, Unset]): UID assigned to a Veeam Cloud Connect site.
            > You can provide the `null` value only if a single tenant is assigned to a company. Otherwise, the server will
            return an error.'
        description (Union[None, Unset, str]): Subtenant user description.
        vcd_user_id (Union[None, Unset, str]): UID assigned to a VMware Cloud Director organization user account.
        storage_quota (Union[None, Unset, int]): Subtenant quota, in bytes.
        is_storage_quota_unlimited (Union[Unset, bool]): Defines whether a subtenant has unlimited quota. Default: True.
    """

    tenant_backup_resource_uid: UUID
    resource_friendly_name: str
    site_uid: Union[None, UUID, Unset] = UNSET
    description: Union[None, Unset, str] = UNSET
    vcd_user_id: Union[None, Unset, str] = UNSET
    storage_quota: Union[None, Unset, int] = UNSET
    is_storage_quota_unlimited: Union[Unset, bool] = True
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        tenant_backup_resource_uid = str(self.tenant_backup_resource_uid)

        resource_friendly_name = self.resource_friendly_name

        site_uid: Union[None, Unset, str]
        if isinstance(self.site_uid, Unset):
            site_uid = UNSET
        elif isinstance(self.site_uid, UUID):
            site_uid = str(self.site_uid)
        else:
            site_uid = self.site_uid

        description: Union[None, Unset, str]
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        vcd_user_id: Union[None, Unset, str]
        if isinstance(self.vcd_user_id, Unset):
            vcd_user_id = UNSET
        else:
            vcd_user_id = self.vcd_user_id

        storage_quota: Union[None, Unset, int]
        if isinstance(self.storage_quota, Unset):
            storage_quota = UNSET
        else:
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

        def _parse_site_uid(data: object) -> Union[None, UUID, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                site_uid_type_0 = UUID(data)

                return site_uid_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID, Unset], data)

        site_uid = _parse_site_uid(d.pop("siteUid", UNSET))

        def _parse_description(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_vcd_user_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        vcd_user_id = _parse_vcd_user_id(d.pop("vcdUserId", UNSET))

        def _parse_storage_quota(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        storage_quota = _parse_storage_quota(d.pop("storageQuota", UNSET))

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
