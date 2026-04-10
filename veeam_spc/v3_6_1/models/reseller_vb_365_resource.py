from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.reseller_vb_365_repository_resource import ResellerVb365RepositoryResource


T = TypeVar("T", bound="ResellerVb365Resource")


@_attrs_define
class ResellerVb365Resource:
    """
    Attributes:
        vb_365_server_uid (UUID): UID assigned to a Veeam Backup for Microsoft 365 server.
        friendly_name (str): Friendly name of a Veeam Backup for Microsoft 365 resource.
        reseller_uid (UUID): UID assigned to a reseller.
        vb_365_repositories (list['ResellerVb365RepositoryResource']): Array of Veeam Backup for Microsoft 365 backup
            repositories.
        instance_uid (Union[Unset, UUID]): UID assigned to a Veeam Backup for Microsoft 365 resource.
    """

    vb_365_server_uid: UUID
    friendly_name: str
    reseller_uid: UUID
    vb_365_repositories: list["ResellerVb365RepositoryResource"]
    instance_uid: Union[Unset, UUID] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        vb_365_server_uid = str(self.vb_365_server_uid)

        friendly_name = self.friendly_name

        reseller_uid = str(self.reseller_uid)

        vb_365_repositories = []
        for vb_365_repositories_item_data in self.vb_365_repositories:
            vb_365_repositories_item = vb_365_repositories_item_data.to_dict()
            vb_365_repositories.append(vb_365_repositories_item)

        instance_uid: Union[Unset, str] = UNSET
        if not isinstance(self.instance_uid, Unset):
            instance_uid = str(self.instance_uid)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "vb365ServerUid": vb_365_server_uid,
                "friendlyName": friendly_name,
                "resellerUid": reseller_uid,
                "vb365Repositories": vb_365_repositories,
            }
        )
        if instance_uid is not UNSET:
            field_dict["instanceUid"] = instance_uid

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.reseller_vb_365_repository_resource import ResellerVb365RepositoryResource

        d = dict(src_dict)
        vb_365_server_uid = UUID(d.pop("vb365ServerUid"))

        friendly_name = d.pop("friendlyName")

        reseller_uid = UUID(d.pop("resellerUid"))

        vb_365_repositories = []
        _vb_365_repositories = d.pop("vb365Repositories")
        for vb_365_repositories_item_data in _vb_365_repositories:
            vb_365_repositories_item = ResellerVb365RepositoryResource.from_dict(vb_365_repositories_item_data)

            vb_365_repositories.append(vb_365_repositories_item)

        _instance_uid = d.pop("instanceUid", UNSET)
        instance_uid: Union[Unset, UUID]
        if isinstance(_instance_uid, Unset):
            instance_uid = UNSET
        else:
            instance_uid = UUID(_instance_uid)

        reseller_vb_365_resource = cls(
            vb_365_server_uid=vb_365_server_uid,
            friendly_name=friendly_name,
            reseller_uid=reseller_uid,
            vb_365_repositories=vb_365_repositories,
            instance_uid=instance_uid,
        )

        reseller_vb_365_resource.additional_properties = d
        return reseller_vb_365_resource

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
