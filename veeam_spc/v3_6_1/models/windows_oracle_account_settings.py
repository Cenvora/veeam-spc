from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.windows_oracle_account_settings_account_type import WindowsOracleAccountSettingsAccountType
from ..types import UNSET, Unset

T = TypeVar("T", bound="WindowsOracleAccountSettings")


@_attrs_define
class WindowsOracleAccountSettings:
    """
    Attributes:
        username (str): User name.
        account_type (Union[Unset, WindowsOracleAccountSettingsAccountType]): Type of the account used to access Oracle
            database. Default: WindowsOracleAccountSettingsAccountType.WINDOWS.
        password (Union[None, Unset, str]): Password.
    """

    username: str
    account_type: Union[Unset, WindowsOracleAccountSettingsAccountType] = (
        WindowsOracleAccountSettingsAccountType.WINDOWS
    )
    password: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        username = self.username

        account_type: Union[Unset, str] = UNSET
        if not isinstance(self.account_type, Unset):
            account_type = self.account_type.value

        password: Union[None, Unset, str]
        if isinstance(self.password, Unset):
            password = UNSET
        else:
            password = self.password

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "username": username,
            }
        )
        if account_type is not UNSET:
            field_dict["accountType"] = account_type
        if password is not UNSET:
            field_dict["password"] = password

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        username = d.pop("username")

        _account_type = d.pop("accountType", UNSET)
        account_type: Union[Unset, WindowsOracleAccountSettingsAccountType]
        if isinstance(_account_type, Unset):
            account_type = UNSET
        else:
            account_type = WindowsOracleAccountSettingsAccountType(_account_type)

        def _parse_password(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        password = _parse_password(d.pop("password", UNSET))

        windows_oracle_account_settings = cls(
            username=username,
            account_type=account_type,
            password=password,
        )

        windows_oracle_account_settings.additional_properties = d
        return windows_oracle_account_settings

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
