import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

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
        end_time (Union[None, Unset, datetime.datetime]): End date and time of a Veeam Backup for Public Clouds policy
            session
        failure_message (Union[None, Unset, str]): Message containing information on failed Veeam Backup for Public
            Clouds policy session.
        status (Union[Unset, PublicCloudPolicySessionStatusReadonly]): Status of a Veeam Backup for Public Clouds policy
            session.
    """

    end_time: Union[None, Unset, datetime.datetime] = UNSET
    failure_message: Union[None, Unset, str] = UNSET
    status: Union[Unset, PublicCloudPolicySessionStatusReadonly] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        end_time: Union[None, Unset, str]
        if isinstance(self.end_time, Unset):
            end_time = UNSET
        elif isinstance(self.end_time, datetime.datetime):
            end_time = self.end_time.isoformat()
        else:
            end_time = self.end_time

        failure_message: Union[None, Unset, str]
        if isinstance(self.failure_message, Unset):
            failure_message = UNSET
        else:
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

        def _parse_end_time(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                end_time_type_0 = isoparse(data)

                return end_time_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        end_time = _parse_end_time(d.pop("endTime", UNSET))

        def _parse_failure_message(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        failure_message = _parse_failure_message(d.pop("failureMessage", UNSET))

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
