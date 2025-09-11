from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.e_public_cloud_object_creating_state import EPublicCloudObjectCreatingState
from ..types import UNSET, Unset

T = TypeVar("T", bound="CreatingObjectInfo")


@_attrs_define
class CreatingObjectInfo:
    """Status of a repository creation.

    Attributes:
        state (Union[Unset, EPublicCloudObjectCreatingState]): Status of object creation.
        message (Union[Unset, str]): Status message.
    """

    state: Union[Unset, EPublicCloudObjectCreatingState] = UNSET
    message: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        state: Union[Unset, str] = UNSET
        if not isinstance(self.state, Unset):
            state = self.state.value

        message = self.message

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if state is not UNSET:
            field_dict["state"] = state
        if message is not UNSET:
            field_dict["message"] = message

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _state = d.pop("state", UNSET)
        state: Union[Unset, EPublicCloudObjectCreatingState]
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = EPublicCloudObjectCreatingState(_state)

        message = d.pop("message", UNSET)

        creating_object_info = cls(
            state=state,
            message=message,
        )

        creating_object_info.additional_properties = d
        return creating_object_info

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
