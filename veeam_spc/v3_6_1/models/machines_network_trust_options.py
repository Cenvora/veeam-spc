from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.machines_network_trust_options_trust_option import MachinesNetworkTrustOptionsTrustOption
from ..types import UNSET, Unset

T = TypeVar("T", bound="MachinesNetworkTrustOptions")


@_attrs_define
class MachinesNetworkTrustOptions:
    """
    Attributes:
        trust_option (MachinesNetworkTrustOptionsTrustOption): Type of trusted computer selection.
        known_host_list (Union[None, Unset, str]): List of trusted computers required for the `KnownList` type of
            selection.
    """

    trust_option: MachinesNetworkTrustOptionsTrustOption
    known_host_list: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        trust_option = self.trust_option.value

        known_host_list: Union[None, Unset, str]
        if isinstance(self.known_host_list, Unset):
            known_host_list = UNSET
        else:
            known_host_list = self.known_host_list

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "trustOption": trust_option,
            }
        )
        if known_host_list is not UNSET:
            field_dict["knownHostList"] = known_host_list

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        trust_option = MachinesNetworkTrustOptionsTrustOption(d.pop("trustOption"))

        def _parse_known_host_list(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        known_host_list = _parse_known_host_list(d.pop("knownHostList", UNSET))

        machines_network_trust_options = cls(
            trust_option=trust_option,
            known_host_list=known_host_list,
        )

        machines_network_trust_options.additional_properties = d
        return machines_network_trust_options

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
