from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.user_profile_title import UserProfileTitle
from ..types import UNSET, Unset

T = TypeVar("T", bound="UserProfile")


@_attrs_define
class UserProfile:
    """
    Example:
        {'firstName': 'Mark', 'lastName': 'Brown', 'title': 'Mr', 'status': 'Enabled', 'email': 'mark.brown@delta.com',
            'address': '90 West Broad St Columbus OH 43215', 'phone': '(524) 745-5371'}

    Attributes:
        first_name (Union[Unset, str]): User first name.
        last_name (Union[Unset, str]): User last name.
        title (Union[Unset, UserProfileTitle]): User title. Default: UserProfileTitle.UNKNOWN.
        email (Union[Unset, str]): User email address.
        address (Union[Unset, str]): Address of a user or user organization.
        phone (Union[Unset, str]): Telephone number of a user or user organization.
    """

    first_name: Union[Unset, str] = UNSET
    last_name: Union[Unset, str] = UNSET
    title: Union[Unset, UserProfileTitle] = UserProfileTitle.UNKNOWN
    email: Union[Unset, str] = UNSET
    address: Union[Unset, str] = UNSET
    phone: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        first_name = self.first_name

        last_name = self.last_name

        title: Union[Unset, str] = UNSET
        if not isinstance(self.title, Unset):
            title = self.title.value

        email = self.email

        address = self.address

        phone = self.phone

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if first_name is not UNSET:
            field_dict["firstName"] = first_name
        if last_name is not UNSET:
            field_dict["lastName"] = last_name
        if title is not UNSET:
            field_dict["title"] = title
        if email is not UNSET:
            field_dict["email"] = email
        if address is not UNSET:
            field_dict["address"] = address
        if phone is not UNSET:
            field_dict["phone"] = phone

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        first_name = d.pop("firstName", UNSET)

        last_name = d.pop("lastName", UNSET)

        _title = d.pop("title", UNSET)
        title: Union[Unset, UserProfileTitle]
        if isinstance(_title, Unset):
            title = UNSET
        else:
            title = UserProfileTitle(_title)

        email = d.pop("email", UNSET)

        address = d.pop("address", UNSET)

        phone = d.pop("phone", UNSET)

        user_profile = cls(
            first_name=first_name,
            last_name=last_name,
            title=title,
            email=email,
            address=address,
            phone=phone,
        )

        user_profile.additional_properties = d
        return user_profile

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
