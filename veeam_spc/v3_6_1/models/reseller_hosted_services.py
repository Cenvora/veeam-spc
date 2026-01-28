from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ResellerHostedServices")


@_attrs_define
class ResellerHostedServices:
    """
    Attributes:
        backup_resources_enabled (Union[Unset, bool]): Indicates whether reseller companies can create jobs on a hosted
            Veeam Backup & Replication server.
             Default: False.
        vb_365_management_enabled (Union[Unset, bool]): Indicates whether reseller companies can use Microsoft 365
            resources.
             Default: False.
        vb_public_cloud_management_enabled (Union[Unset, bool]): Indicates whether integration with Veeam Backup for
            Public Clouds is available to a reseller. Default: False.
    """

    backup_resources_enabled: Union[Unset, bool] = False
    vb_365_management_enabled: Union[Unset, bool] = False
    vb_public_cloud_management_enabled: Union[Unset, bool] = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        backup_resources_enabled = self.backup_resources_enabled

        vb_365_management_enabled = self.vb_365_management_enabled

        vb_public_cloud_management_enabled = self.vb_public_cloud_management_enabled

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if backup_resources_enabled is not UNSET:
            field_dict["backupResourcesEnabled"] = backup_resources_enabled
        if vb_365_management_enabled is not UNSET:
            field_dict["vb365ManagementEnabled"] = vb_365_management_enabled
        if vb_public_cloud_management_enabled is not UNSET:
            field_dict["vbPublicCloudManagementEnabled"] = vb_public_cloud_management_enabled

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        backup_resources_enabled = d.pop("backupResourcesEnabled", UNSET)

        vb_365_management_enabled = d.pop("vb365ManagementEnabled", UNSET)

        vb_public_cloud_management_enabled = d.pop("vbPublicCloudManagementEnabled", UNSET)

        reseller_hosted_services = cls(
            backup_resources_enabled=backup_resources_enabled,
            vb_365_management_enabled=vb_365_management_enabled,
            vb_public_cloud_management_enabled=vb_public_cloud_management_enabled,
        )

        reseller_hosted_services.additional_properties = d
        return reseller_hosted_services

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
