from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.mac_common_credentials import MacCommonCredentials
    from ..models.mac_connection_settings import MacConnectionSettings


T = TypeVar("T", bound="MacBackupServerSettings")


@_attrs_define
class MacBackupServerSettings:
    """
    Attributes:
        connection (MacConnectionSettings):
        credentials (MacCommonCredentials):
        remote_repository_name (Union[None, Unset, str]): Name of a remote backup repository.
    """

    connection: "MacConnectionSettings"
    credentials: "MacCommonCredentials"
    remote_repository_name: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        connection = self.connection.to_dict()

        credentials = self.credentials.to_dict()

        remote_repository_name: Union[None, Unset, str]
        if isinstance(self.remote_repository_name, Unset):
            remote_repository_name = UNSET
        else:
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
        from ..models.mac_common_credentials import MacCommonCredentials
        from ..models.mac_connection_settings import MacConnectionSettings

        d = dict(src_dict)
        connection = MacConnectionSettings.from_dict(d.pop("connection"))

        credentials = MacCommonCredentials.from_dict(d.pop("credentials"))

        def _parse_remote_repository_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        remote_repository_name = _parse_remote_repository_name(d.pop("remoteRepositoryName", UNSET))

        mac_backup_server_settings = cls(
            connection=connection,
            credentials=credentials,
            remote_repository_name=remote_repository_name,
        )

        mac_backup_server_settings.additional_properties = d
        return mac_backup_server_settings

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
