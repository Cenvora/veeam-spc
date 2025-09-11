from collections.abc import Mapping
from typing import Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ResellerVb365ResourceInput")


@_attrs_define
class ResellerVb365ResourceInput:
    """
    Attributes:
        vb_365_server_uid (UUID): UID assigned to a Veeam Backup for Microsoft 365 resource.
        friendly_name (str): Friendly name of a Veeam Backup for Microsoft 365 resource.
        vb_365_repositories_uids (Union[Unset, list[UUID]]): Array of UIDs assigned to Veeam Backup for Microsoft 365
            backup repositories.
    """

    vb_365_server_uid: UUID
    friendly_name: str
    vb_365_repositories_uids: Union[Unset, list[UUID]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        vb_365_server_uid = str(self.vb_365_server_uid)

        friendly_name = self.friendly_name

        vb_365_repositories_uids: Union[Unset, list[str]] = UNSET
        if not isinstance(self.vb_365_repositories_uids, Unset):
            vb_365_repositories_uids = []
            for vb_365_repositories_uids_item_data in self.vb_365_repositories_uids:
                vb_365_repositories_uids_item = str(vb_365_repositories_uids_item_data)
                vb_365_repositories_uids.append(vb_365_repositories_uids_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "vb365ServerUid": vb_365_server_uid,
                "friendlyName": friendly_name,
            }
        )
        if vb_365_repositories_uids is not UNSET:
            field_dict["vb365RepositoriesUids"] = vb_365_repositories_uids

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        vb_365_server_uid = UUID(d.pop("vb365ServerUid"))

        friendly_name = d.pop("friendlyName")

        vb_365_repositories_uids = []
        _vb_365_repositories_uids = d.pop("vb365RepositoriesUids", UNSET)
        for vb_365_repositories_uids_item_data in _vb_365_repositories_uids or []:
            vb_365_repositories_uids_item = UUID(vb_365_repositories_uids_item_data)

            vb_365_repositories_uids.append(vb_365_repositories_uids_item)

        reseller_vb_365_resource_input = cls(
            vb_365_server_uid=vb_365_server_uid,
            friendly_name=friendly_name,
            vb_365_repositories_uids=vb_365_repositories_uids,
        )

        reseller_vb_365_resource_input.additional_properties = d
        return reseller_vb_365_resource_input

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
