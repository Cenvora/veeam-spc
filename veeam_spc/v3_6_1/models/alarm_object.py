from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.alarm_object_type import AlarmObjectType
from ..types import UNSET, Unset

T = TypeVar("T", bound="AlarmObject")


@_attrs_define
class AlarmObject:
    """
    Attributes:
        instance_uid (Union[Unset, UUID]): UID assigned to an object for which an alarm was triggered.
        type_ (Union[Unset, AlarmObjectType]): Object type.
        organization_uid (Union[Unset, UUID]): UID assigned to a organization for which an alarm was triggered.
        location_uid (Union[None, UUID, Unset]): UID assigned to a location for which an alarm was triggered.
        management_agent_uid (Union[None, UUID, Unset]): UID assigned to a managed agent that is installed on an alarm
            object.
        computer_name (Union[Unset, str]): Name of a computer for which an alarm was triggered.
        object_uid (Union[None, UUID, Unset]): UID assigned to an alarm object.
        object_name (Union[None, Unset, str]): Name of an alarm object.
    """

    instance_uid: Union[Unset, UUID] = UNSET
    type_: Union[Unset, AlarmObjectType] = UNSET
    organization_uid: Union[Unset, UUID] = UNSET
    location_uid: Union[None, UUID, Unset] = UNSET
    management_agent_uid: Union[None, UUID, Unset] = UNSET
    computer_name: Union[Unset, str] = UNSET
    object_uid: Union[None, UUID, Unset] = UNSET
    object_name: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        instance_uid: Union[Unset, str] = UNSET
        if not isinstance(self.instance_uid, Unset):
            instance_uid = str(self.instance_uid)

        type_: Union[Unset, str] = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        organization_uid: Union[Unset, str] = UNSET
        if not isinstance(self.organization_uid, Unset):
            organization_uid = str(self.organization_uid)

        location_uid: Union[None, Unset, str]
        if isinstance(self.location_uid, Unset):
            location_uid = UNSET
        elif isinstance(self.location_uid, UUID):
            location_uid = str(self.location_uid)
        else:
            location_uid = self.location_uid

        management_agent_uid: Union[None, Unset, str]
        if isinstance(self.management_agent_uid, Unset):
            management_agent_uid = UNSET
        elif isinstance(self.management_agent_uid, UUID):
            management_agent_uid = str(self.management_agent_uid)
        else:
            management_agent_uid = self.management_agent_uid

        computer_name = self.computer_name

        object_uid: Union[None, Unset, str]
        if isinstance(self.object_uid, Unset):
            object_uid = UNSET
        elif isinstance(self.object_uid, UUID):
            object_uid = str(self.object_uid)
        else:
            object_uid = self.object_uid

        object_name: Union[None, Unset, str]
        if isinstance(self.object_name, Unset):
            object_name = UNSET
        else:
            object_name = self.object_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if instance_uid is not UNSET:
            field_dict["instanceUid"] = instance_uid
        if type_ is not UNSET:
            field_dict["type"] = type_
        if organization_uid is not UNSET:
            field_dict["organizationUid"] = organization_uid
        if location_uid is not UNSET:
            field_dict["locationUid"] = location_uid
        if management_agent_uid is not UNSET:
            field_dict["managementAgentUid"] = management_agent_uid
        if computer_name is not UNSET:
            field_dict["computerName"] = computer_name
        if object_uid is not UNSET:
            field_dict["objectUid"] = object_uid
        if object_name is not UNSET:
            field_dict["objectName"] = object_name

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

        _type_ = d.pop("type", UNSET)
        type_: Union[Unset, AlarmObjectType]
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = AlarmObjectType(_type_)

        _organization_uid = d.pop("organizationUid", UNSET)
        organization_uid: Union[Unset, UUID]
        if isinstance(_organization_uid, Unset):
            organization_uid = UNSET
        else:
            organization_uid = UUID(_organization_uid)

        def _parse_location_uid(data: object) -> Union[None, UUID, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                location_uid_type_0 = UUID(data)

                return location_uid_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID, Unset], data)

        location_uid = _parse_location_uid(d.pop("locationUid", UNSET))

        def _parse_management_agent_uid(data: object) -> Union[None, UUID, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                management_agent_uid_type_0 = UUID(data)

                return management_agent_uid_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID, Unset], data)

        management_agent_uid = _parse_management_agent_uid(d.pop("managementAgentUid", UNSET))

        computer_name = d.pop("computerName", UNSET)

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

        def _parse_object_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        object_name = _parse_object_name(d.pop("objectName", UNSET))

        alarm_object = cls(
            instance_uid=instance_uid,
            type_=type_,
            organization_uid=organization_uid,
            location_uid=location_uid,
            management_agent_uid=management_agent_uid,
            computer_name=computer_name,
            object_uid=object_uid,
            object_name=object_name,
        )

        alarm_object.additional_properties = d
        return alarm_object

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
