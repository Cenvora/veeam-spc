from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.public_cloud_google_network_type import PublicCloudGoogleNetworkType
from ..types import UNSET, Unset

T = TypeVar("T", bound="PublicCloudGoogleNetworks")


@_attrs_define
class PublicCloudGoogleNetworks:
    """
    Attributes:
        network_id (Union[Unset, str]): ID assigned to a network.
        network_name (Union[Unset, str]): Name of a network.
        project_id (Union[Unset, str]): ID assigned to a project to which a network is added.
        network_type (Union[Unset, PublicCloudGoogleNetworkType]): Type of a network.
    """

    network_id: Union[Unset, str] = UNSET
    network_name: Union[Unset, str] = UNSET
    project_id: Union[Unset, str] = UNSET
    network_type: Union[Unset, PublicCloudGoogleNetworkType] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        network_id = self.network_id

        network_name = self.network_name

        project_id = self.project_id

        network_type: Union[Unset, str] = UNSET
        if not isinstance(self.network_type, Unset):
            network_type = self.network_type.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if network_id is not UNSET:
            field_dict["networkId"] = network_id
        if network_name is not UNSET:
            field_dict["networkName"] = network_name
        if project_id is not UNSET:
            field_dict["projectId"] = project_id
        if network_type is not UNSET:
            field_dict["networkType"] = network_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        network_id = d.pop("networkId", UNSET)

        network_name = d.pop("networkName", UNSET)

        project_id = d.pop("projectId", UNSET)

        _network_type = d.pop("networkType", UNSET)
        network_type: Union[Unset, PublicCloudGoogleNetworkType]
        if isinstance(_network_type, Unset):
            network_type = UNSET
        else:
            network_type = PublicCloudGoogleNetworkType(_network_type)

        public_cloud_google_networks = cls(
            network_id=network_id,
            network_name=network_name,
            project_id=project_id,
            network_type=network_type,
        )

        public_cloud_google_networks.additional_properties = d
        return public_cloud_google_networks

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
