from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.linux_my_sql_application_aware_processing_settings_auth_type import (
    LinuxMySqlApplicationAwareProcessingSettingsAuthType,
)
from ..models.linux_my_sql_application_aware_processing_settings_processing_type import (
    LinuxMySqlApplicationAwareProcessingSettingsProcessingType,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.linux_base_credentials import LinuxBaseCredentials


T = TypeVar("T", bound="LinuxMySqlApplicationAwareProcessingSettings")


@_attrs_define
class LinuxMySqlApplicationAwareProcessingSettings:
    """
    Attributes:
        processing_type (Union[Unset, LinuxMySqlApplicationAwareProcessingSettingsProcessingType]): Transaction log
            processing mode. Default: LinuxMySqlApplicationAwareProcessingSettingsProcessingType.DISABLEPROCESS.
        credentials (Union[Unset, LinuxBaseCredentials]):
        auth_type (Union[Unset, LinuxMySqlApplicationAwareProcessingSettingsAuthType]): Type of credentials format.
            Default: LinuxMySqlApplicationAwareProcessingSettingsAuthType.MYSQLPASSWORD.
        password_file_path (Union[None, Unset, str]): Path to the password file.
    """

    processing_type: Union[Unset, LinuxMySqlApplicationAwareProcessingSettingsProcessingType] = (
        LinuxMySqlApplicationAwareProcessingSettingsProcessingType.DISABLEPROCESS
    )
    credentials: Union[Unset, "LinuxBaseCredentials"] = UNSET
    auth_type: Union[Unset, LinuxMySqlApplicationAwareProcessingSettingsAuthType] = (
        LinuxMySqlApplicationAwareProcessingSettingsAuthType.MYSQLPASSWORD
    )
    password_file_path: Union[None, Unset, str] = UNSET
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

        password_file_path: Union[None, Unset, str]
        if isinstance(self.password_file_path, Unset):
            password_file_path = UNSET
        else:
            password_file_path = self.password_file_path

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if processing_type is not UNSET:
            field_dict["processingType"] = processing_type
        if credentials is not UNSET:
            field_dict["credentials"] = credentials
        if auth_type is not UNSET:
            field_dict["authType"] = auth_type
        if password_file_path is not UNSET:
            field_dict["passwordFilePath"] = password_file_path

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.linux_base_credentials import LinuxBaseCredentials

        d = dict(src_dict)
        _processing_type = d.pop("processingType", UNSET)
        processing_type: Union[Unset, LinuxMySqlApplicationAwareProcessingSettingsProcessingType]
        if isinstance(_processing_type, Unset):
            processing_type = UNSET
        else:
            processing_type = LinuxMySqlApplicationAwareProcessingSettingsProcessingType(_processing_type)

        _credentials = d.pop("credentials", UNSET)
        credentials: Union[Unset, LinuxBaseCredentials]
        if isinstance(_credentials, Unset):
            credentials = UNSET
        else:
            credentials = LinuxBaseCredentials.from_dict(_credentials)

        _auth_type = d.pop("authType", UNSET)
        auth_type: Union[Unset, LinuxMySqlApplicationAwareProcessingSettingsAuthType]
        if isinstance(_auth_type, Unset):
            auth_type = UNSET
        else:
            auth_type = LinuxMySqlApplicationAwareProcessingSettingsAuthType(_auth_type)

        def _parse_password_file_path(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        password_file_path = _parse_password_file_path(d.pop("passwordFilePath", UNSET))

        linux_my_sql_application_aware_processing_settings = cls(
            processing_type=processing_type,
            credentials=credentials,
            auth_type=auth_type,
            password_file_path=password_file_path,
        )

        linux_my_sql_application_aware_processing_settings.additional_properties = d
        return linux_my_sql_application_aware_processing_settings

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
