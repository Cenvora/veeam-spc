from collections.abc import Mapping
from typing import Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PublicCloudSqlAccountAppliance")


@_attrs_define
class PublicCloudSqlAccountAppliance:
    """
    Attributes:
        appliance_uid (Union[Unset, UUID]): UID assigned to a Veeam Backup for Public Clouds appliance.
        appliance_name (Union[Unset, str]): Name of a Veeam Backup for Public Clouds appliance.
        site_uid (Union[Unset, UUID]): UID assigned to a Veeam Cloud Connect site.
        management_agent_uid (Union[Unset, UUID]): UID assigned to a management agent installed on a Veeam Backup for
            Public Clouds appliance server.
    """

    appliance_uid: Union[Unset, UUID] = UNSET
    appliance_name: Union[Unset, str] = UNSET
    site_uid: Union[Unset, UUID] = UNSET
    management_agent_uid: Union[Unset, UUID] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        appliance_uid: Union[Unset, str] = UNSET
        if not isinstance(self.appliance_uid, Unset):
            appliance_uid = str(self.appliance_uid)

        appliance_name = self.appliance_name

        site_uid: Union[Unset, str] = UNSET
        if not isinstance(self.site_uid, Unset):
            site_uid = str(self.site_uid)

        management_agent_uid: Union[Unset, str] = UNSET
        if not isinstance(self.management_agent_uid, Unset):
            management_agent_uid = str(self.management_agent_uid)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if appliance_uid is not UNSET:
            field_dict["applianceUid"] = appliance_uid
        if appliance_name is not UNSET:
            field_dict["applianceName"] = appliance_name
        if site_uid is not UNSET:
            field_dict["siteUid"] = site_uid
        if management_agent_uid is not UNSET:
            field_dict["managementAgentUid"] = management_agent_uid

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _appliance_uid = d.pop("applianceUid", UNSET)
        appliance_uid: Union[Unset, UUID]
        if isinstance(_appliance_uid, Unset):
            appliance_uid = UNSET
        else:
            appliance_uid = UUID(_appliance_uid)

        appliance_name = d.pop("applianceName", UNSET)

        _site_uid = d.pop("siteUid", UNSET)
        site_uid: Union[Unset, UUID]
        if isinstance(_site_uid, Unset):
            site_uid = UNSET
        else:
            site_uid = UUID(_site_uid)

        _management_agent_uid = d.pop("managementAgentUid", UNSET)
        management_agent_uid: Union[Unset, UUID]
        if isinstance(_management_agent_uid, Unset):
            management_agent_uid = UNSET
        else:
            management_agent_uid = UUID(_management_agent_uid)

        public_cloud_sql_account_appliance = cls(
            appliance_uid=appliance_uid,
            appliance_name=appliance_name,
            site_uid=site_uid,
            management_agent_uid=management_agent_uid,
        )

        public_cloud_sql_account_appliance.additional_properties = d
        return public_cloud_sql_account_appliance

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
