from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.active_alarm import ActiveAlarm
    from ..models.response_error import ResponseError
    from ..models.response_metadata import ResponseMetadata


T = TypeVar("T", bound="GetActiveAlarmResponse200")


@_attrs_define
class GetActiveAlarmResponse200:
    r"""
    Attributes:
        meta (Union[Unset, ResponseMetadata]):
        data (Union[Unset, ActiveAlarm]):  Example: {'instanceUid': '08b46982-1160-4804-bb12-6227b521972e',
            'alarmTemplateUid': '5cf175f4-d596-4636-bf8e-f166516418df', 'repeatCount': 3, 'object': {'instanceUid':
            'baf8d020-fb95-41ba-be4f-89b44dca4fcd', 'type': 'ObjectEntity', 'companyUid':
            '39f65b4c-a7d2-451e-936d-aeae418b53e1', 'locationUid': '5523b04d-077b-4526-a219-4533d6f23987',
            'managementAgentUid': 'd4b32a13-0b1b-4e7f-9050-309fa0eb7055', 'computerName': 'ws-5floor', 'objectName':
            'Premium repository'}, 'lastActivation': {'instanceUid': '86477f51-389e-49bb-9480-25dc9abc71d2', 'time':
            datetime.datetime(2020, 1, 13, 0, 20, 50, 520000, tzinfo=datetime.timezone(datetime.timedelta(seconds=3600),
            '+01:00')), 'status': 'Error', 'message': 'Free space (2.55%, 1.01 GB) is below the defined threshold
            (5%).\n\n', 'remark': '\n\n'}}.
        errors (Union[Unset, list['ResponseError']]):
    """

    meta: Union[Unset, "ResponseMetadata"] = UNSET
    data: Union[Unset, "ActiveAlarm"] = UNSET
    errors: Union[Unset, list["ResponseError"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        meta: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.meta, Unset):
            meta = self.meta.to_dict()

        data: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.data, Unset):
            data = self.data.to_dict()

        errors: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.errors, Unset):
            errors = []
            for errors_item_data in self.errors:
                errors_item = errors_item_data.to_dict()
                errors.append(errors_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if meta is not UNSET:
            field_dict["meta"] = meta
        if data is not UNSET:
            field_dict["data"] = data
        if errors is not UNSET:
            field_dict["errors"] = errors

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.active_alarm import ActiveAlarm
        from ..models.response_error import ResponseError
        from ..models.response_metadata import ResponseMetadata

        d = dict(src_dict)
        _meta = d.pop("meta", UNSET)
        meta: Union[Unset, ResponseMetadata]
        if isinstance(_meta, Unset):
            meta = UNSET
        else:
            meta = ResponseMetadata.from_dict(_meta)

        _data = d.pop("data", UNSET)
        data: Union[Unset, ActiveAlarm]
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = ActiveAlarm.from_dict(_data)

        errors = []
        _errors = d.pop("errors", UNSET)
        for errors_item_data in _errors or []:
            errors_item = ResponseError.from_dict(errors_item_data)

            errors.append(errors_item)

        get_active_alarm_response_200 = cls(
            meta=meta,
            data=data,
            errors=errors,
        )

        get_active_alarm_response_200.additional_properties = d
        return get_active_alarm_response_200

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
