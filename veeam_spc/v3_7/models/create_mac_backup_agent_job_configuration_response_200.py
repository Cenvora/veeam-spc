from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.mac_custom_job_configuration import MacCustomJobConfiguration
    from ..models.response_error import ResponseError
    from ..models.response_metadata_type_0 import ResponseMetadataType0


T = TypeVar("T", bound="CreateMacBackupAgentJobConfigurationResponse200")


@_attrs_define
class CreateMacBackupAgentJobConfigurationResponse200:
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
        meta (None | ResponseMetadataType0 | Unset):
        errors (list[ResponseError] | None | Unset):
    """

    data: MacCustomJobConfiguration
    meta: None | ResponseMetadataType0 | Unset = UNSET
    errors: list[ResponseError] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.response_metadata_type_0 import ResponseMetadataType0

        data = self.data.to_dict()

        meta: dict[str, Any] | None | Unset
        if isinstance(self.meta, Unset):
            meta = UNSET
        elif isinstance(self.meta, ResponseMetadataType0):
            meta = self.meta.to_dict()
        else:
            meta = self.meta

        errors: list[dict[str, Any]] | None | Unset
        if isinstance(self.errors, Unset):
            errors = UNSET
        elif isinstance(self.errors, list):
            errors = []
            for errors_type_0_item_data in self.errors:
                errors_type_0_item = errors_type_0_item_data.to_dict()
                errors.append(errors_type_0_item)

        else:
            errors = self.errors

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
        from ..models.response_metadata_type_0 import ResponseMetadataType0

        d = dict(src_dict)
        data = MacCustomJobConfiguration.from_dict(d.pop("data"))

        def _parse_meta(data: object) -> None | ResponseMetadataType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_response_metadata_type_0 = ResponseMetadataType0.from_dict(data)

                return componentsschemas_response_metadata_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | ResponseMetadataType0 | Unset, data)

        meta = _parse_meta(d.pop("meta", UNSET))

        def _parse_errors(data: object) -> list[ResponseError] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                errors_type_0 = []
                _errors_type_0 = data
                for errors_type_0_item_data in _errors_type_0:
                    errors_type_0_item = ResponseError.from_dict(errors_type_0_item_data)

                    errors_type_0.append(errors_type_0_item)

                return errors_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ResponseError] | None | Unset, data)

        errors = _parse_errors(d.pop("errors", UNSET))

        create_mac_backup_agent_job_configuration_response_200 = cls(
            data=data,
            meta=meta,
            errors=errors,
        )

        create_mac_backup_agent_job_configuration_response_200.additional_properties = d
        return create_mac_backup_agent_job_configuration_response_200

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
