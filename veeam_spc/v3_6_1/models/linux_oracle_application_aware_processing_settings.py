from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.linux_oracle_application_aware_processing_settings_processing_type import (
    LinuxOracleApplicationAwareProcessingSettingsProcessingType,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.linux_base_credentials import LinuxBaseCredentials
    from ..models.linux_oracle_archived_logs_truncation_config import LinuxOracleArchivedLogsTruncationConfig


T = TypeVar("T", bound="LinuxOracleApplicationAwareProcessingSettings")


@_attrs_define
class LinuxOracleApplicationAwareProcessingSettings:
    """
    Attributes:
        processing_type (Union[Unset, LinuxOracleApplicationAwareProcessingSettingsProcessingType]): Processing type.
            Default: LinuxOracleApplicationAwareProcessingSettingsProcessingType.DISABLEPROCESS.
        credentials (Union[Unset, LinuxBaseCredentials]):
        truncation_config (Union[Unset, LinuxOracleArchivedLogsTruncationConfig]):
        use_oracle_credentials (Union[Unset, bool]): Indicates whether the Oracle account credentials must be used.
            Default: False.
    """

    processing_type: Union[Unset, LinuxOracleApplicationAwareProcessingSettingsProcessingType] = (
        LinuxOracleApplicationAwareProcessingSettingsProcessingType.DISABLEPROCESS
    )
    credentials: Union[Unset, "LinuxBaseCredentials"] = UNSET
    truncation_config: Union[Unset, "LinuxOracleArchivedLogsTruncationConfig"] = UNSET
    use_oracle_credentials: Union[Unset, bool] = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        processing_type: Union[Unset, str] = UNSET
        if not isinstance(self.processing_type, Unset):
            processing_type = self.processing_type.value

        credentials: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.credentials, Unset):
            credentials = self.credentials.to_dict()

        truncation_config: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.truncation_config, Unset):
            truncation_config = self.truncation_config.to_dict()

        use_oracle_credentials = self.use_oracle_credentials

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if processing_type is not UNSET:
            field_dict["processingType"] = processing_type
        if credentials is not UNSET:
            field_dict["credentials"] = credentials
        if truncation_config is not UNSET:
            field_dict["truncationConfig"] = truncation_config
        if use_oracle_credentials is not UNSET:
            field_dict["useOracleCredentials"] = use_oracle_credentials

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.linux_base_credentials import LinuxBaseCredentials
        from ..models.linux_oracle_archived_logs_truncation_config import LinuxOracleArchivedLogsTruncationConfig

        d = dict(src_dict)
        _processing_type = d.pop("processingType", UNSET)
        processing_type: Union[Unset, LinuxOracleApplicationAwareProcessingSettingsProcessingType]
        if isinstance(_processing_type, Unset):
            processing_type = UNSET
        else:
            processing_type = LinuxOracleApplicationAwareProcessingSettingsProcessingType(_processing_type)

        _credentials = d.pop("credentials", UNSET)
        credentials: Union[Unset, LinuxBaseCredentials]
        if isinstance(_credentials, Unset):
            credentials = UNSET
        else:
            credentials = LinuxBaseCredentials.from_dict(_credentials)

        _truncation_config = d.pop("truncationConfig", UNSET)
        truncation_config: Union[Unset, LinuxOracleArchivedLogsTruncationConfig]
        if isinstance(_truncation_config, Unset):
            truncation_config = UNSET
        else:
            truncation_config = LinuxOracleArchivedLogsTruncationConfig.from_dict(_truncation_config)

        use_oracle_credentials = d.pop("useOracleCredentials", UNSET)

        linux_oracle_application_aware_processing_settings = cls(
            processing_type=processing_type,
            credentials=credentials,
            truncation_config=truncation_config,
            use_oracle_credentials=use_oracle_credentials,
        )

        linux_oracle_application_aware_processing_settings.additional_properties = d
        return linux_oracle_application_aware_processing_settings

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
