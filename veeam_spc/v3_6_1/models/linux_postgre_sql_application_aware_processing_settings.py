from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.linux_postgre_sql_application_aware_processing_settings_auth_type import (
    LinuxPostgreSqlApplicationAwareProcessingSettingsAuthType,
)
from ..models.linux_postgre_sql_application_aware_processing_settings_processing_type import (
    LinuxPostgreSqlApplicationAwareProcessingSettingsProcessingType,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.linux_base_credentials import LinuxBaseCredentials


T = TypeVar("T", bound="LinuxPostgreSqlApplicationAwareProcessingSettings")


@_attrs_define
class LinuxPostgreSqlApplicationAwareProcessingSettings:
    """
    Attributes:
        processing_type (Union[Unset, LinuxPostgreSqlApplicationAwareProcessingSettingsProcessingType]): PostgreSQL
            database processing type. Default:
            LinuxPostgreSqlApplicationAwareProcessingSettingsProcessingType.DISABLEPROCESS.
        credentials (Union[Unset, LinuxBaseCredentials]):
        auth_type (Union[Unset, LinuxPostgreSqlApplicationAwareProcessingSettingsAuthType]): Type of credentials format.
            Default: LinuxPostgreSqlApplicationAwareProcessingSettingsAuthType.PSQLPASSWORD.
    """

    processing_type: Union[Unset, LinuxPostgreSqlApplicationAwareProcessingSettingsProcessingType] = (
        LinuxPostgreSqlApplicationAwareProcessingSettingsProcessingType.DISABLEPROCESS
    )
    credentials: Union[Unset, "LinuxBaseCredentials"] = UNSET
    auth_type: Union[Unset, LinuxPostgreSqlApplicationAwareProcessingSettingsAuthType] = (
        LinuxPostgreSqlApplicationAwareProcessingSettingsAuthType.PSQLPASSWORD
    )
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        processing_type: Union[Unset, str] = UNSET
        if not isinstance(self.processing_type, Unset):
            processing_type = self.processing_type.value

        credentials: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.credentials, Unset):
            credentials = self.credentials.to_dict()

        auth_type: Union[Unset, str] = UNSET
        if not isinstance(self.auth_type, Unset):
            auth_type = self.auth_type.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if processing_type is not UNSET:
            field_dict["processingType"] = processing_type
        if credentials is not UNSET:
            field_dict["credentials"] = credentials
        if auth_type is not UNSET:
            field_dict["authType"] = auth_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.linux_base_credentials import LinuxBaseCredentials

        d = dict(src_dict)
        _processing_type = d.pop("processingType", UNSET)
        processing_type: Union[Unset, LinuxPostgreSqlApplicationAwareProcessingSettingsProcessingType]
        if isinstance(_processing_type, Unset):
            processing_type = UNSET
        else:
            processing_type = LinuxPostgreSqlApplicationAwareProcessingSettingsProcessingType(_processing_type)

        _credentials = d.pop("credentials", UNSET)
        credentials: Union[Unset, LinuxBaseCredentials]
        if isinstance(_credentials, Unset):
            credentials = UNSET
        else:
            credentials = LinuxBaseCredentials.from_dict(_credentials)

        _auth_type = d.pop("authType", UNSET)
        auth_type: Union[Unset, LinuxPostgreSqlApplicationAwareProcessingSettingsAuthType]
        if isinstance(_auth_type, Unset):
            auth_type = UNSET
        else:
            auth_type = LinuxPostgreSqlApplicationAwareProcessingSettingsAuthType(_auth_type)

        linux_postgre_sql_application_aware_processing_settings = cls(
            processing_type=processing_type,
            credentials=credentials,
            auth_type=auth_type,
        )

        linux_postgre_sql_application_aware_processing_settings.additional_properties = d
        return linux_postgre_sql_application_aware_processing_settings

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
