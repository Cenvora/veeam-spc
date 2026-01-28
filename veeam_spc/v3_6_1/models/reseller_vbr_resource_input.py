from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ResellerVbrResourceInput")


@_attrs_define
class ResellerVbrResourceInput:
    """
    Attributes:
        vbr_server_uid (UUID): UID assigned to a Veeam Backup & Replication server resource.
        friendly_name (str): Friendly name of a Veeam Backup & Replication server resource.
    """

    vbr_server_uid: UUID
    friendly_name: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        vbr_server_uid = str(self.vbr_server_uid)

        friendly_name = self.friendly_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "vbrServerUid": vbr_server_uid,
                "friendlyName": friendly_name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        vbr_server_uid = UUID(d.pop("vbrServerUid"))

        friendly_name = d.pop("friendlyName")

        reseller_vbr_resource_input = cls(
            vbr_server_uid=vbr_server_uid,
            friendly_name=friendly_name,
        )

        reseller_vbr_resource_input.additional_properties = d
        return reseller_vbr_resource_input

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
