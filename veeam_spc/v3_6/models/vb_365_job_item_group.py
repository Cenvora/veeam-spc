from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.vb_365_job_item_group_group_type import Vb365JobItemGroupGroupType
from ..models.vb_365_job_item_group_location_type import Vb365JobItemGroupLocationType
from ..types import UNSET, Unset

T = TypeVar("T", bound="Vb365JobItemGroup")


@_attrs_define
class Vb365JobItemGroup:
    """
    Attributes:
        id (str): ID assigned to an organization group.
        group_type (Vb365JobItemGroupGroupType): Type of an organization group.
        name (str): Name of an organization group.
        display_name (str): Display name of an organization group.
        on_premises_sid (Union[Unset, str]): SID assigned to an on-premises organization group.
        location_type (Union[Unset, Vb365JobItemGroupLocationType]): Type of an organization group location.
        managed_by (Union[Unset, str]): Name of a user that manages an organization group.
        site (Union[Unset, str]): URL of an organization group site.
    """

    id: str
    group_type: Vb365JobItemGroupGroupType
    name: str
    display_name: str
    on_premises_sid: Union[Unset, str] = UNSET
    location_type: Union[Unset, Vb365JobItemGroupLocationType] = UNSET
    managed_by: Union[Unset, str] = UNSET
    site: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        group_type = self.group_type.value

        name = self.name

        display_name = self.display_name

        on_premises_sid = self.on_premises_sid

        location_type: Union[Unset, str] = UNSET
        if not isinstance(self.location_type, Unset):
            location_type = self.location_type.value

        managed_by = self.managed_by

        site = self.site

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "groupType": group_type,
                "name": name,
                "displayName": display_name,
            }
        )
        if on_premises_sid is not UNSET:
            field_dict["onPremisesSid"] = on_premises_sid
        if location_type is not UNSET:
            field_dict["locationType"] = location_type
        if managed_by is not UNSET:
            field_dict["managedBy"] = managed_by
        if site is not UNSET:
            field_dict["site"] = site

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        group_type = Vb365JobItemGroupGroupType(d.pop("groupType"))

        name = d.pop("name")

        display_name = d.pop("displayName")

        on_premises_sid = d.pop("onPremisesSid", UNSET)

        _location_type = d.pop("locationType", UNSET)
        location_type: Union[Unset, Vb365JobItemGroupLocationType]
        if isinstance(_location_type, Unset):
            location_type = UNSET
        else:
            location_type = Vb365JobItemGroupLocationType(_location_type)

        managed_by = d.pop("managedBy", UNSET)

        site = d.pop("site", UNSET)

        vb_365_job_item_group = cls(
            id=id,
            group_type=group_type,
            name=name,
            display_name=display_name,
            on_premises_sid=on_premises_sid,
            location_type=location_type,
            managed_by=managed_by,
            site=site,
        )

        vb_365_job_item_group.additional_properties = d
        return vb_365_job_item_group

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
