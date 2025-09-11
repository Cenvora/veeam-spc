from collections.abc import Mapping
from typing import Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ResellerVbrResource")


@_attrs_define
class ResellerVbrResource:
    """
    Attributes:
        vbr_server_uid (UUID): UID assigned to a Veeam Backup & Replication server server.
        friendly_name (str): Friendly name of a Veeam Backup & Replication server resource.
        reseller_uid (UUID): UID assigned to a reseller.
        instance_uid (Union[Unset, UUID]): UID assigned to a Veeam Backup & Replication server resource.
    """

    vbr_server_uid: UUID
    friendly_name: str
    reseller_uid: UUID
    instance_uid: Union[Unset, UUID] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        vbr_server_uid = str(self.vbr_server_uid)

        friendly_name = self.friendly_name

        reseller_uid = str(self.reseller_uid)

        instance_uid: Union[Unset, str] = UNSET
        if not isinstance(self.instance_uid, Unset):
            instance_uid = str(self.instance_uid)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "vbrServerUid": vbr_server_uid,
                "friendlyName": friendly_name,
                "resellerUid": reseller_uid,
            }
        )
        if instance_uid is not UNSET:
            field_dict["instanceUid"] = instance_uid

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        vbr_server_uid = UUID(d.pop("vbrServerUid"))

        friendly_name = d.pop("friendlyName")

        reseller_uid = UUID(d.pop("resellerUid"))

        _instance_uid = d.pop("instanceUid", UNSET)
        instance_uid: Union[Unset, UUID]
        if isinstance(_instance_uid, Unset):
            instance_uid = UNSET
        else:
            instance_uid = UUID(_instance_uid)

        reseller_vbr_resource = cls(
            vbr_server_uid=vbr_server_uid,
            friendly_name=friendly_name,
            reseller_uid=reseller_uid,
            instance_uid=instance_uid,
        )

        reseller_vbr_resource.additional_properties = d
        return reseller_vbr_resource

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
