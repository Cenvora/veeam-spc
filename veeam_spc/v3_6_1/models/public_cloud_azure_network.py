from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.public_cloud_azure_subnet import PublicCloudAzureSubnet


T = TypeVar("T", bound="PublicCloudAzureNetwork")


@_attrs_define
class PublicCloudAzureNetwork:
    """
    Attributes:
        network_id (Union[Unset, str]): ID assigned to a network.
        network_name (Union[Unset, str]): Name of a network.
        subnets (Union[Unset, list['PublicCloudAzureSubnet']]): Array of subnets.
    """

    network_id: Union[Unset, str] = UNSET
    network_name: Union[Unset, str] = UNSET
    subnets: Union[Unset, list["PublicCloudAzureSubnet"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        network_id = self.network_id

        network_name = self.network_name

        subnets: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.subnets, Unset):
            subnets = []
            for subnets_item_data in self.subnets:
                subnets_item = subnets_item_data.to_dict()
                subnets.append(subnets_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if network_id is not UNSET:
            field_dict["networkId"] = network_id
        if network_name is not UNSET:
            field_dict["networkName"] = network_name
        if subnets is not UNSET:
            field_dict["subnets"] = subnets

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.public_cloud_azure_subnet import PublicCloudAzureSubnet

        d = dict(src_dict)
        network_id = d.pop("networkId", UNSET)

        network_name = d.pop("networkName", UNSET)

        subnets = []
        _subnets = d.pop("subnets", UNSET)
        for subnets_item_data in _subnets or []:
            subnets_item = PublicCloudAzureSubnet.from_dict(subnets_item_data)

            subnets.append(subnets_item)

        public_cloud_azure_network = cls(
            network_id=network_id,
            network_name=network_name,
            subnets=subnets,
        )

        public_cloud_azure_network.additional_properties = d
        return public_cloud_azure_network

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
