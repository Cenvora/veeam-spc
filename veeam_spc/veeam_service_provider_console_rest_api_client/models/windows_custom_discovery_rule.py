from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.embedded_for_windows_discovery_rule_children import EmbeddedForWindowsDiscoveryRuleChildren


T = TypeVar("T", bound="WindowsCustomDiscoveryRule")


@_attrs_define
class WindowsCustomDiscoveryRule:
    """
    Attributes:
        hosts (list[str]): Array of IP addresses or DNS names of computers on which Veeam backup agent is deployed.
        instance_uid (Union[Unset, UUID]): UID assigned to a custom discovery rule.
        field_embedded (Union[Unset, EmbeddedForWindowsDiscoveryRuleChildren]): Resource representation of the related
            Windows discovery rule entity.
    """

    hosts: list[str]
    instance_uid: Union[Unset, UUID] = UNSET
    field_embedded: Union[Unset, "EmbeddedForWindowsDiscoveryRuleChildren"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        hosts = self.hosts

        instance_uid: Union[Unset, str] = UNSET
        if not isinstance(self.instance_uid, Unset):
            instance_uid = str(self.instance_uid)

        field_embedded: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.field_embedded, Unset):
            field_embedded = self.field_embedded.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "hosts": hosts,
            }
        )
        if instance_uid is not UNSET:
            field_dict["instanceUid"] = instance_uid
        if field_embedded is not UNSET:
            field_dict["_embedded"] = field_embedded

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.embedded_for_windows_discovery_rule_children import EmbeddedForWindowsDiscoveryRuleChildren

        d = dict(src_dict)
        hosts = cast(list[str], d.pop("hosts"))

        _instance_uid = d.pop("instanceUid", UNSET)
        instance_uid: Union[Unset, UUID]
        if isinstance(_instance_uid, Unset):
            instance_uid = UNSET
        else:
            instance_uid = UUID(_instance_uid)

        _field_embedded = d.pop("_embedded", UNSET)
        field_embedded: Union[Unset, EmbeddedForWindowsDiscoveryRuleChildren]
        if isinstance(_field_embedded, Unset):
            field_embedded = UNSET
        else:
            field_embedded = EmbeddedForWindowsDiscoveryRuleChildren.from_dict(_field_embedded)

        windows_custom_discovery_rule = cls(
            hosts=hosts,
            instance_uid=instance_uid,
            field_embedded=field_embedded,
        )

        windows_custom_discovery_rule.additional_properties = d
        return windows_custom_discovery_rule

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
