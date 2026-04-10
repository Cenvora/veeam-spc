from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.public_cloud_sql_account_database_type import PublicCloudSqlAccountDatabaseType
from ..types import UNSET, Unset

T = TypeVar("T", bound="NewPublicCloudSqlAccount")


@_attrs_define
class NewPublicCloudSqlAccount:
    """
    Attributes:
        account_name (str): Name of a public cloud SQL account.
        database_type (PublicCloudSqlAccountDatabaseType): Type of a public cloud SQL database.
        user_name (Union[None, str]): User name.
        password (Union[None, str]): Password.
        appliance_uid (UUID): UID assigned to a Veeam Backup for Public Clouds appliance.
        description (Union[None, Unset, str]): Description of a public cloud SQL account.
    """

    account_name: str
    database_type: PublicCloudSqlAccountDatabaseType
    user_name: Union[None, str]
    password: Union[None, str]
    appliance_uid: UUID
    description: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        account_name = self.account_name

        database_type = self.database_type.value

        user_name: Union[None, str]
        user_name = self.user_name

        password: Union[None, str]
        password = self.password

        appliance_uid = str(self.appliance_uid)

        description: Union[None, Unset, str]
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "accountName": account_name,
                "databaseType": database_type,
                "userName": user_name,
                "password": password,
                "applianceUid": appliance_uid,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        account_name = d.pop("accountName")

        database_type = PublicCloudSqlAccountDatabaseType(d.pop("databaseType"))

        def _parse_user_name(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        user_name = _parse_user_name(d.pop("userName"))

        def _parse_password(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        password = _parse_password(d.pop("password"))

        appliance_uid = UUID(d.pop("applianceUid"))

        def _parse_description(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        description = _parse_description(d.pop("description", UNSET))

        new_public_cloud_sql_account = cls(
            account_name=account_name,
            database_type=database_type,
            user_name=user_name,
            password=password,
            appliance_uid=appliance_uid,
            description=description,
        )

        new_public_cloud_sql_account.additional_properties = d
        return new_public_cloud_sql_account

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
