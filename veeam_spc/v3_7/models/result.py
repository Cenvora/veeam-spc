from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.e_action_result_status import EActionResultStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="Result")


@_attrs_define
class Result:
    """
    Attributes:
        status (EActionResultStatus | Unset):
        success (bool | Unset):
        message (str | Unset):
        object_name (str | Unset):
        object_id (str | Unset):
    """

    status: EActionResultStatus | Unset = UNSET
    success: bool | Unset = UNSET
    message: str | Unset = UNSET
    object_name: str | Unset = UNSET
    object_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        success = self.success

        message = self.message

        object_name = self.object_name

        object_id = self.object_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if status is not UNSET:
            field_dict["status"] = status
        if success is not UNSET:
            field_dict["success"] = success
        if message is not UNSET:
            field_dict["message"] = message
        if object_name is not UNSET:
            field_dict["objectName"] = object_name
        if object_id is not UNSET:
            field_dict["objectId"] = object_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _status = d.pop("status", UNSET)
        status: EActionResultStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = EActionResultStatus(_status)

        success = d.pop("success", UNSET)

        message = d.pop("message", UNSET)

        object_name = d.pop("objectName", UNSET)

        object_id = d.pop("objectId", UNSET)

        result = cls(
            status=status,
            success=success,
            message=message,
            object_name=object_name,
            object_id=object_id,
        )

        result.additional_properties = d
        return result

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
