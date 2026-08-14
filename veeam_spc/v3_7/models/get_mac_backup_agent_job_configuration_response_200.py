from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.mac_custom_job_configuration import MacCustomJobConfiguration
    from ..models.response_error import ResponseError
    from ..models.response_metadata import ResponseMetadata


T = TypeVar("T", bound="GetMacBackupAgentJobConfigurationResponse200")


@_attrs_define
class GetMacBackupAgentJobConfigurationResponse200:
    """
    Attributes:
        data (MacCustomJobConfiguration):  Example: {'name': 'ServerEntireCloud_Custom', 'description': 'Mac Policy',
            'operationMode': 'Server', 'cloudRepositoryConnectionSettings': {'backupResourceUid':
            '28428289-2557-41b5-a51d-95730a24f23a', 'username': 'admin', 'password': None}, 'jobConfiguration':
            {'backupSource': {'backupDirectlyFromLiveFileSystem': True, 'includeUsbDrives': False, 'includeDirectories':
            None, 'inclusionMasks': None, 'excludeDirectories': None, 'exclusionMasks': None,
            'personalFilesAdvancedSettings': {'inclusions': ['Desktop', 'Documents', 'Downloads', 'Video', 'Music',
            'Pictures', 'Favorites', 'ApplicationData', 'OtherFilesAndFolders', 'Library'], 'excludeNetworkAccount': True}},
            'backupTarget': {'targetType': 'CloudRepository', 'localPath': None, 'sharedFolder': None, 'backupRepository':
            None, 'enableDeletedFilesRetention': False, 'removeDeletedItemsDataAfter': 30}, 'backupStorage':
            {'compressionLevel': 'Optimal', 'blockSize': 'Local1Mb', 'encryptionEnabled': False, 'password': None,
            'passwordHint': None}, 'retentionSettings': {'restorePointsCount': None, 'retentionDays': 7},
            'scheduleSettings': {'scheduleType': 'Daily', 'dailyScheduleSettings': {'time': '00:30', 'dailyMode':
            'Everyday', 'specificDays': None}, 'monthlyScheduleSettings': None, 'periodicallyScheduleSettings': None,
            'activeFullSettings': None, 'retrySettings': {'enabled': False, 'retryTimes': 3, 'waitTimeoutMinutes': 10},
            'backupHealthCheckScheduleSettings': None, 'syntheticFullSettings': None}, 'gfsRetentionSettings': None}}.
        meta (ResponseMetadata | Unset):
        errors (list[ResponseError] | Unset):
    """

    data: MacCustomJobConfiguration
    meta: ResponseMetadata | Unset = UNSET
    errors: list[ResponseError] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data = self.data.to_dict()

        meta: dict[str, Any] | Unset = UNSET
        if not isinstance(self.meta, Unset):
            meta = self.meta.to_dict()

        errors: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.errors, Unset):
            errors = []
            for errors_item_data in self.errors:
                errors_item = errors_item_data.to_dict()
                errors.append(errors_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "data": data,
            }
        )
        if meta is not UNSET:
            field_dict["meta"] = meta
        if errors is not UNSET:
            field_dict["errors"] = errors

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.mac_custom_job_configuration import MacCustomJobConfiguration
        from ..models.response_error import ResponseError
        from ..models.response_metadata import ResponseMetadata

        d = dict(src_dict)
        data = MacCustomJobConfiguration.from_dict(d.pop("data"))

        _meta = d.pop("meta", UNSET)
        meta: ResponseMetadata | Unset
        if isinstance(_meta, Unset):
            meta = UNSET
        else:
            meta = ResponseMetadata.from_dict(_meta)

        _errors = d.pop("errors", UNSET)
        errors: list[ResponseError] | Unset = UNSET
        if _errors is not UNSET:
            errors = []
            for errors_item_data in _errors:
                errors_item = ResponseError.from_dict(errors_item_data)

                errors.append(errors_item)

        get_mac_backup_agent_job_configuration_response_200 = cls(
            data=data,
            meta=meta,
            errors=errors,
        )

        get_mac_backup_agent_job_configuration_response_200.additional_properties = d
        return get_mac_backup_agent_job_configuration_response_200

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
