from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.active_alarm_area import ActiveAlarmArea
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.alarm_activation import AlarmActivation
    from ..models.alarm_object import AlarmObject


T = TypeVar("T", bound="ActiveAlarm")


@_attrs_define
class ActiveAlarm:
    r"""
    Example:
        {'instanceUid': '08b46982-1160-4804-bb12-6227b521972e', 'alarmTemplateUid':
            '5cf175f4-d596-4636-bf8e-f166516418df', 'repeatCount': 3, 'object': {'instanceUid': 'baf8d020-fb95-41ba-
            be4f-89b44dca4fcd', 'type': 'ObjectEntity', 'companyUid': '39f65b4c-a7d2-451e-936d-aeae418b53e1', 'locationUid':
            '5523b04d-077b-4526-a219-4533d6f23987', 'managementAgentUid': 'd4b32a13-0b1b-4e7f-9050-309fa0eb7055',
            'computerName': 'ws-5floor', 'objectName': 'Premium repository'}, 'lastActivation': {'instanceUid':
            '86477f51-389e-49bb-9480-25dc9abc71d2', 'time': '2020-01-12T23:20:50.5200000+00:00', 'status': 'Error',
            'message': 'Free space (2.55%, 1.01 GB) is below the defined threshold (5%).\n', 'remark': '\n'}}

    Attributes:
        instance_uid (Union[Unset, UUID]): UID assigned to a triggered alarm.
        alarm_template_uid (Union[Unset, UUID]): UID assigned to an alarm template.
        repeat_count (Union[Unset, int]): Number of times that an alarm changed its status.
        object_ (Union[Unset, AlarmObject]):
        last_activation (Union[Unset, AlarmActivation]):
        area (Union[Unset, ActiveAlarmArea]): Alarm area.
    """

    instance_uid: Union[Unset, UUID] = UNSET
    alarm_template_uid: Union[Unset, UUID] = UNSET
    repeat_count: Union[Unset, int] = UNSET
    object_: Union[Unset, "AlarmObject"] = UNSET
    last_activation: Union[Unset, "AlarmActivation"] = UNSET
    area: Union[Unset, ActiveAlarmArea] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        instance_uid: Union[Unset, str] = UNSET
        if not isinstance(self.instance_uid, Unset):
            instance_uid = str(self.instance_uid)

        alarm_template_uid: Union[Unset, str] = UNSET
        if not isinstance(self.alarm_template_uid, Unset):
            alarm_template_uid = str(self.alarm_template_uid)

        repeat_count = self.repeat_count

        object_: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.object_, Unset):
            object_ = self.object_.to_dict()

        last_activation: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.last_activation, Unset):
            last_activation = self.last_activation.to_dict()

        area: Union[Unset, str] = UNSET
        if not isinstance(self.area, Unset):
            area = self.area.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if instance_uid is not UNSET:
            field_dict["instanceUid"] = instance_uid
        if alarm_template_uid is not UNSET:
            field_dict["alarmTemplateUid"] = alarm_template_uid
        if repeat_count is not UNSET:
            field_dict["repeatCount"] = repeat_count
        if object_ is not UNSET:
            field_dict["object"] = object_
        if last_activation is not UNSET:
            field_dict["lastActivation"] = last_activation
        if area is not UNSET:
            field_dict["area"] = area

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.alarm_activation import AlarmActivation
        from ..models.alarm_object import AlarmObject

        d = dict(src_dict)
        _instance_uid = d.pop("instanceUid", UNSET)
        instance_uid: Union[Unset, UUID]
        if isinstance(_instance_uid, Unset):
            instance_uid = UNSET
        else:
            instance_uid = UUID(_instance_uid)

        _alarm_template_uid = d.pop("alarmTemplateUid", UNSET)
        alarm_template_uid: Union[Unset, UUID]
        if isinstance(_alarm_template_uid, Unset):
            alarm_template_uid = UNSET
        else:
            alarm_template_uid = UUID(_alarm_template_uid)

        repeat_count = d.pop("repeatCount", UNSET)

        _object_ = d.pop("object", UNSET)
        object_: Union[Unset, AlarmObject]
        if isinstance(_object_, Unset):
            object_ = UNSET
        else:
            object_ = AlarmObject.from_dict(_object_)

        _last_activation = d.pop("lastActivation", UNSET)
        last_activation: Union[Unset, AlarmActivation]
        if isinstance(_last_activation, Unset):
            last_activation = UNSET
        else:
            last_activation = AlarmActivation.from_dict(_last_activation)

        _area = d.pop("area", UNSET)
        area: Union[Unset, ActiveAlarmArea]
        if isinstance(_area, Unset):
            area = UNSET
        else:
            area = ActiveAlarmArea(_area)

        active_alarm = cls(
            instance_uid=instance_uid,
            alarm_template_uid=alarm_template_uid,
            repeat_count=repeat_count,
            object_=object_,
            last_activation=last_activation,
            area=area,
        )

        active_alarm.additional_properties = d
        return active_alarm

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
