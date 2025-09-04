from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.response_error import ResponseError
    from ..models.response_metadata import ResponseMetadata
    from ..models.windows_backup_agent_job import WindowsBackupAgentJob


T = TypeVar("T", bound="GetWindowsBackupAgentJobResponse200")


@_attrs_define
class GetWindowsBackupAgentJobResponse200:
    r"""
    Attributes:
        meta (Union[Unset, ResponseMetadata]):
        data (Union[Unset, WindowsBackupAgentJob]):  Example: {'backupAgentUid': 'CCEB5975-B409-49B5-8ECE-FFFECB13494F',
            'name': 'VAW job 2 Cloud', 'configUid': 'AF097BD3-4AE9-4841-8152-8FF5CC703EAB', 'status': 'Success',
            'operationMode': 'Server', 'backupMode': 'File', 'destination': '\\\\share\\backup\\test', 'restorePoints': 4,
            'lastRun': datetime.datetime(2018, 11, 1, 11, 35, tzinfo=datetime.timezone(datetime.timedelta(seconds=3600),
            '+01:00')), 'lastEndTime': datetime.datetime(2018, 11, 1, 11, 45,
            tzinfo=datetime.timezone(datetime.timedelta(seconds=3600), '+01:00')), 'lastDuration': 600, 'nextRun':
            datetime.datetime(2018, 12, 1, 11, 35, tzinfo=datetime.timezone(datetime.timedelta(seconds=3600), '+01:00')),
            'avgDuration': 575, 'targetType': 'Local', 'isEnabled': True, 'schedulingType': 'Periodically',
            'failureMessage': '', 'lastModifiedDate': datetime.datetime(2018, 11, 1, 11, 45,
            tzinfo=datetime.timezone(datetime.timedelta(seconds=3600), '+01:00')), 'lastModifiedBy': 'someuser',
            'backedUpSize': 12550788}.
        errors (Union[Unset, list['ResponseError']]):
    """

    meta: Union[Unset, "ResponseMetadata"] = UNSET
    data: Union[Unset, "WindowsBackupAgentJob"] = UNSET
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
        from ..models.response_error import ResponseError
        from ..models.response_metadata import ResponseMetadata
        from ..models.windows_backup_agent_job import WindowsBackupAgentJob

        d = dict(src_dict)
        _meta = d.pop("meta", UNSET)
        meta: Union[Unset, ResponseMetadata]
        if isinstance(_meta, Unset):
            meta = UNSET
        else:
            meta = ResponseMetadata.from_dict(_meta)

        _data = d.pop("data", UNSET)
        data: Union[Unset, WindowsBackupAgentJob]
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = WindowsBackupAgentJob.from_dict(_data)

        errors = []
        _errors = d.pop("errors", UNSET)
        for errors_item_data in _errors or []:
            errors_item = ResponseError.from_dict(errors_item_data)

            errors.append(errors_item)

        get_windows_backup_agent_job_response_200 = cls(
            meta=meta,
            data=data,
            errors=errors,
        )

        get_windows_backup_agent_job_response_200.additional_properties = d
        return get_windows_backup_agent_job_response_200

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
