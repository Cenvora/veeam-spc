from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.vb_365_job_item_user_location_type import Vb365JobItemUserLocationType
from ..models.vb_365_job_item_user_user_type import Vb365JobItemUserUserType
from ..types import UNSET, Unset

T = TypeVar("T", bound="Vb365JobItemUser")


@_attrs_define
class Vb365JobItemUser:
    """
    Attributes:
        id (str): ID assigned to a user.
        name (str): Name of a user.
        display_name (str): Display name of a user.
        on_premises_sid (Union[None, Unset, str]): SID assigned to a user of an on-premises organization.
        office_name (Union[Unset, str]): Microsoft 365 Online name of an organization to which a user belongs.
        user_type (Union[Unset, Vb365JobItemUserUserType]): Type of a user.
        location_type (Union[Unset, Vb365JobItemUserLocationType]): Type of a user location.
    """

    id: str
    name: str
    display_name: str
    on_premises_sid: Union[None, Unset, str] = UNSET
    office_name: Union[Unset, str] = UNSET
    user_type: Union[Unset, Vb365JobItemUserUserType] = UNSET
    location_type: Union[Unset, Vb365JobItemUserLocationType] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        display_name = self.display_name

        on_premises_sid: Union[None, Unset, str]
        if isinstance(self.on_premises_sid, Unset):
            on_premises_sid = UNSET
        else:
            on_premises_sid = self.on_premises_sid

        office_name = self.office_name

        user_type: Union[Unset, str] = UNSET
        if not isinstance(self.user_type, Unset):
            user_type = self.user_type.value

        location_type: Union[Unset, str] = UNSET
        if not isinstance(self.location_type, Unset):
            location_type = self.location_type.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "displayName": display_name,
            }
        )
        if on_premises_sid is not UNSET:
            field_dict["onPremisesSid"] = on_premises_sid
        if office_name is not UNSET:
            field_dict["officeName"] = office_name
        if user_type is not UNSET:
            field_dict["userType"] = user_type
        if location_type is not UNSET:
            field_dict["locationType"] = location_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        display_name = d.pop("displayName")

        def _parse_on_premises_sid(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        on_premises_sid = _parse_on_premises_sid(d.pop("onPremisesSid", UNSET))

        office_name = d.pop("officeName", UNSET)

        _user_type = d.pop("userType", UNSET)
        user_type: Union[Unset, Vb365JobItemUserUserType]
        if isinstance(_user_type, Unset):
            user_type = UNSET
        else:
            user_type = Vb365JobItemUserUserType(_user_type)

        _location_type = d.pop("locationType", UNSET)
        location_type: Union[Unset, Vb365JobItemUserLocationType]
        if isinstance(_location_type, Unset):
            location_type = UNSET
        else:
            location_type = Vb365JobItemUserLocationType(_location_type)

        vb_365_job_item_user = cls(
            id=id,
            name=name,
            display_name=display_name,
            on_premises_sid=on_premises_sid,
            office_name=office_name,
            user_type=user_type,
            location_type=location_type,
        )

        vb_365_job_item_user.additional_properties = d
        return vb_365_job_item_user

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
