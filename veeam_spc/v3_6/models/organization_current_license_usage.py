from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.organization_current_license_usage_organization_type import (
    OrganizationCurrentLicenseUsageOrganizationType,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.server_current_license_usage import ServerCurrentLicenseUsage


T = TypeVar("T", bound="OrganizationCurrentLicenseUsage")


@_attrs_define
class OrganizationCurrentLicenseUsage:
    """
    Attributes:
        organization_uid (Union[Unset, UUID]): UID assigned to an organization.
        organization_type (Union[Unset, OrganizationCurrentLicenseUsageOrganizationType]): Type of an organization.
        provider_uid (Union[Unset, UUID]): UID assigned to a provider organization.
        servers (Union[Unset, list['ServerCurrentLicenseUsage']]): License usage by workloads for each server managing
            these workloads.
    """

    organization_uid: Union[Unset, UUID] = UNSET
    organization_type: Union[Unset, OrganizationCurrentLicenseUsageOrganizationType] = UNSET
    provider_uid: Union[Unset, UUID] = UNSET
    servers: Union[Unset, list["ServerCurrentLicenseUsage"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        organization_uid: Union[Unset, str] = UNSET
        if not isinstance(self.organization_uid, Unset):
            organization_uid = str(self.organization_uid)

        organization_type: Union[Unset, str] = UNSET
        if not isinstance(self.organization_type, Unset):
            organization_type = self.organization_type.value

        provider_uid: Union[Unset, str] = UNSET
        if not isinstance(self.provider_uid, Unset):
            provider_uid = str(self.provider_uid)

        servers: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.servers, Unset):
            servers = []
            for servers_item_data in self.servers:
                servers_item = servers_item_data.to_dict()
                servers.append(servers_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if organization_uid is not UNSET:
            field_dict["organizationUid"] = organization_uid
        if organization_type is not UNSET:
            field_dict["organizationType"] = organization_type
        if provider_uid is not UNSET:
            field_dict["providerUid"] = provider_uid
        if servers is not UNSET:
            field_dict["servers"] = servers

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.server_current_license_usage import ServerCurrentLicenseUsage

        d = dict(src_dict)
        _organization_uid = d.pop("organizationUid", UNSET)
        organization_uid: Union[Unset, UUID]
        if isinstance(_organization_uid, Unset):
            organization_uid = UNSET
        else:
            organization_uid = UUID(_organization_uid)

        _organization_type = d.pop("organizationType", UNSET)
        organization_type: Union[Unset, OrganizationCurrentLicenseUsageOrganizationType]
        if isinstance(_organization_type, Unset):
            organization_type = UNSET
        else:
            organization_type = OrganizationCurrentLicenseUsageOrganizationType(_organization_type)

        _provider_uid = d.pop("providerUid", UNSET)
        provider_uid: Union[Unset, UUID]
        if isinstance(_provider_uid, Unset):
            provider_uid = UNSET
        else:
            provider_uid = UUID(_provider_uid)

        servers = []
        _servers = d.pop("servers", UNSET)
        for servers_item_data in _servers or []:
            servers_item = ServerCurrentLicenseUsage.from_dict(servers_item_data)

            servers.append(servers_item)

        organization_current_license_usage = cls(
            organization_uid=organization_uid,
            organization_type=organization_type,
            provider_uid=provider_uid,
            servers=servers,
        )

        organization_current_license_usage.additional_properties = d
        return organization_current_license_usage

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
