from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.local_user_rule_object_type import LocalUserRuleObjectType
from ..types import UNSET, Unset

T = TypeVar("T", bound="LocalUserRuleObject")


@_attrs_define
class LocalUserRuleObject:
    """
    Attributes:
        type_ (LocalUserRuleObjectType): Type of an account.
        object_uid (Union[None, UUID, Unset]): UID assigned to a Company/CloudConnectAgent. Reference is depended on
            type
    """

    type_: LocalUserRuleObjectType
    object_uid: Union[None, UUID, Unset] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        object_uid: Union[None, Unset, str]
        if isinstance(self.object_uid, Unset):
            object_uid = UNSET
        elif isinstance(self.object_uid, UUID):
            object_uid = str(self.object_uid)
        else:
            object_uid = self.object_uid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
            }
        )
        if object_uid is not UNSET:
            field_dict["objectUid"] = object_uid

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = LocalUserRuleObjectType(d.pop("type"))

        def _parse_object_uid(data: object) -> Union[None, UUID, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                object_uid_type_0 = UUID(data)

                return object_uid_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID, Unset], data)

        object_uid = _parse_object_uid(d.pop("objectUid", UNSET))

        local_user_rule_object = cls(
            type_=type_,
            object_uid=object_uid,
        )

        local_user_rule_object.additional_properties = d
        return local_user_rule_object

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
