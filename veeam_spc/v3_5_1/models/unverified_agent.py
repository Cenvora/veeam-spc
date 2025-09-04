import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.unverified_agent_platform_type import UnverifiedAgentPlatformType
from ..models.unverified_agent_status import UnverifiedAgentStatus
from ..models.unverified_agent_type import UnverifiedAgentType
from ..types import UNSET, Unset

T = TypeVar("T", bound="UnverifiedAgent")


@_attrs_define
class UnverifiedAgent:
    """
    Attributes:
        instance_uid (Union[Unset, UUID]): UID assigned to a management agent.
        organization_uid (Union[Unset, UUID]): UID assigned to an organization to which a management agent belongs.
        host_name (Union[Unset, str]): Name of a computer on which a management agent is deployed.
        registration_time (Union[Unset, datetime.datetime]): Time when a management agent was registered.
        tag (Union[Unset, str]): Additional information.
        reject_reason (Union[Unset, str]): Reason for management agent being unverified.
        type_ (Union[Unset, UnverifiedAgentType]): Role of a management agent.
        status (Union[Unset, UnverifiedAgentStatus]): Status of a management agent.
        status_message (Union[Unset, str]): Management agent status message.
        platform_type (Union[Unset, UnverifiedAgentPlatformType]): Platform type of an agent.
    """

    instance_uid: Union[Unset, UUID] = UNSET
    organization_uid: Union[Unset, UUID] = UNSET
    host_name: Union[Unset, str] = UNSET
    registration_time: Union[Unset, datetime.datetime] = UNSET
    tag: Union[Unset, str] = UNSET
    reject_reason: Union[Unset, str] = UNSET
    type_: Union[Unset, UnverifiedAgentType] = UNSET
    status: Union[Unset, UnverifiedAgentStatus] = UNSET
    status_message: Union[Unset, str] = UNSET
    platform_type: Union[Unset, UnverifiedAgentPlatformType] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        instance_uid: Union[Unset, str] = UNSET
        if not isinstance(self.instance_uid, Unset):
            instance_uid = str(self.instance_uid)

        organization_uid: Union[Unset, str] = UNSET
        if not isinstance(self.organization_uid, Unset):
            organization_uid = str(self.organization_uid)

        host_name = self.host_name

        registration_time: Union[Unset, str] = UNSET
        if not isinstance(self.registration_time, Unset):
            registration_time = self.registration_time.isoformat()

        tag = self.tag

        reject_reason = self.reject_reason

        type_: Union[Unset, str] = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        status_message = self.status_message

        platform_type: Union[Unset, str] = UNSET
        if not isinstance(self.platform_type, Unset):
            platform_type = self.platform_type.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if instance_uid is not UNSET:
            field_dict["instanceUid"] = instance_uid
        if organization_uid is not UNSET:
            field_dict["organizationUid"] = organization_uid
        if host_name is not UNSET:
            field_dict["hostName"] = host_name
        if registration_time is not UNSET:
            field_dict["registrationTime"] = registration_time
        if tag is not UNSET:
            field_dict["tag"] = tag
        if reject_reason is not UNSET:
            field_dict["rejectReason"] = reject_reason
        if type_ is not UNSET:
            field_dict["type"] = type_
        if status is not UNSET:
            field_dict["status"] = status
        if status_message is not UNSET:
            field_dict["statusMessage"] = status_message
        if platform_type is not UNSET:
            field_dict["platformType"] = platform_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _instance_uid = d.pop("instanceUid", UNSET)
        instance_uid: Union[Unset, UUID]
        if isinstance(_instance_uid, Unset):
            instance_uid = UNSET
        else:
            instance_uid = UUID(_instance_uid)

        _organization_uid = d.pop("organizationUid", UNSET)
        organization_uid: Union[Unset, UUID]
        if isinstance(_organization_uid, Unset):
            organization_uid = UNSET
        else:
            organization_uid = UUID(_organization_uid)

        host_name = d.pop("hostName", UNSET)

        _registration_time = d.pop("registrationTime", UNSET)
        registration_time: Union[Unset, datetime.datetime]
        if isinstance(_registration_time, Unset):
            registration_time = UNSET
        else:
            registration_time = isoparse(_registration_time)

        tag = d.pop("tag", UNSET)

        reject_reason = d.pop("rejectReason", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: Union[Unset, UnverifiedAgentType]
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = UnverifiedAgentType(_type_)

        _status = d.pop("status", UNSET)
        status: Union[Unset, UnverifiedAgentStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = UnverifiedAgentStatus(_status)

        status_message = d.pop("statusMessage", UNSET)

        _platform_type = d.pop("platformType", UNSET)
        platform_type: Union[Unset, UnverifiedAgentPlatformType]
        if isinstance(_platform_type, Unset):
            platform_type = UNSET
        else:
            platform_type = UnverifiedAgentPlatformType(_platform_type)

        unverified_agent = cls(
            instance_uid=instance_uid,
            organization_uid=organization_uid,
            host_name=host_name,
            registration_time=registration_time,
            tag=tag,
            reject_reason=reject_reason,
            type_=type_,
            status=status,
            status_message=status_message,
            platform_type=platform_type,
        )

        unverified_agent.additional_properties = d
        return unverified_agent

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
