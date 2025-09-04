from collections.abc import Mapping
from typing import Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Vb365JobItemTeam")


@_attrs_define
class Vb365JobItemTeam:
    """
    Attributes:
        id (UUID): ID assigned to a team.
        display_name (str): Display name of a team.
        mail (str): Email address of a team.
        description (Union[Unset, str]): Description of a team. Default: ''.
    """

    id: UUID
    display_name: str
    mail: str
    description: Union[Unset, str] = ""
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        display_name = self.display_name

        mail = self.mail

        description = self.description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "displayName": display_name,
                "mail": mail,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))

        display_name = d.pop("displayName")

        mail = d.pop("mail")

        description = d.pop("description", UNSET)

        vb_365_job_item_team = cls(
            id=id,
            display_name=display_name,
            mail=mail,
            description=description,
        )

        vb_365_job_item_team.additional_properties = d
        return vb_365_job_item_team

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
