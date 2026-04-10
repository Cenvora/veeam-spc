from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.vb_365_job_session_log_log_type import Vb365JobSessionLogLogType
from ..types import UNSET, Unset

T = TypeVar("T", bound="Vb365JobSessionLog")


@_attrs_define
class Vb365JobSessionLog:
    """
    Attributes:
        message (Union[Unset, str]): The job session log details
        log_type (Union[Unset, Vb365JobSessionLogLogType]): The job session log type
    """

    message: Union[Unset, str] = UNSET
    log_type: Union[Unset, Vb365JobSessionLogLogType] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        message = self.message

        log_type: Union[Unset, str] = UNSET
        if not isinstance(self.log_type, Unset):
            log_type = self.log_type.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if message is not UNSET:
            field_dict["message"] = message
        if log_type is not UNSET:
            field_dict["logType"] = log_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        message = d.pop("message", UNSET)

        _log_type = d.pop("logType", UNSET)
        log_type: Union[Unset, Vb365JobSessionLogLogType]
        if isinstance(_log_type, Unset):
            log_type = UNSET
        else:
            log_type = Vb365JobSessionLogLogType(_log_type)

        vb_365_job_session_log = cls(
            message=message,
            log_type=log_type,
        )

        vb_365_job_session_log.additional_properties = d
        return vb_365_job_session_log

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
