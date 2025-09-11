from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.linux_common_credentials import LinuxCommonCredentials
    from ..models.linux_connection_settings import LinuxConnectionSettings


T = TypeVar("T", bound="LinuxBackupServerSettings")


@_attrs_define
class LinuxBackupServerSettings:
    """
    Attributes:
        connection (LinuxConnectionSettings):
        credentials (LinuxCommonCredentials):
        remote_repository_name (Union[Unset, str]): Name of a backup repository.
    """

    connection: "LinuxConnectionSettings"
    credentials: "LinuxCommonCredentials"
    remote_repository_name: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        connection = self.connection.to_dict()

        credentials = self.credentials.to_dict()

        remote_repository_name = self.remote_repository_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "connection": connection,
                "credentials": credentials,
            }
        )
        if remote_repository_name is not UNSET:
            field_dict["remoteRepositoryName"] = remote_repository_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.linux_common_credentials import LinuxCommonCredentials
        from ..models.linux_connection_settings import LinuxConnectionSettings

        d = dict(src_dict)
        connection = LinuxConnectionSettings.from_dict(d.pop("connection"))

        credentials = LinuxCommonCredentials.from_dict(d.pop("credentials"))

        remote_repository_name = d.pop("remoteRepositoryName", UNSET)

        linux_backup_server_settings = cls(
            connection=connection,
            credentials=credentials,
            remote_repository_name=remote_repository_name,
        )

        linux_backup_server_settings.additional_properties = d
        return linux_backup_server_settings

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
