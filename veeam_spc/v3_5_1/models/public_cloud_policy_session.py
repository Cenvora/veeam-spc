import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.public_cloud_policy_session_status_readonly import PublicCloudPolicySessionStatusReadonly
from ..types import UNSET, Unset

T = TypeVar("T", bound="PublicCloudPolicySession")


@_attrs_define
class PublicCloudPolicySession:
    """
    Attributes:
        end_time (Union[Unset, datetime.datetime]): End date and time of a Veeam Backup for Public Clouds policy session
        failure_message (Union[Unset, str]): Message containing information on failed Veeam Backup for Public Clouds
            policy session.
        status (Union[Unset, PublicCloudPolicySessionStatusReadonly]): Status of a Veeam Backup for Public Clouds policy
            session.
    """

    end_time: Union[Unset, datetime.datetime] = UNSET
    failure_message: Union[Unset, str] = UNSET
    status: Union[Unset, PublicCloudPolicySessionStatusReadonly] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        end_time: Union[Unset, str] = UNSET
        if not isinstance(self.end_time, Unset):
            end_time = self.end_time.isoformat()

        failure_message = self.failure_message

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if end_time is not UNSET:
            field_dict["endTime"] = end_time
        if failure_message is not UNSET:
            field_dict["failureMessage"] = failure_message
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _end_time = d.pop("endTime", UNSET)
        end_time: Union[Unset, datetime.datetime]
        if isinstance(_end_time, Unset):
            end_time = UNSET
        else:
            end_time = isoparse(_end_time)

        failure_message = d.pop("failureMessage", UNSET)

        _status = d.pop("status", UNSET)
        status: Union[Unset, PublicCloudPolicySessionStatusReadonly]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = PublicCloudPolicySessionStatusReadonly(_status)

        public_cloud_policy_session = cls(
            end_time=end_time,
            failure_message=failure_message,
            status=status,
        )

        public_cloud_policy_session.additional_properties = d
        return public_cloud_policy_session

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
