from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.public_cloud_sql_account_status import PublicCloudSqlAccountStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="PublicCloudSqlAccount")


@_attrs_define
class PublicCloudSqlAccount:
    """
    Attributes:
        account_name (str): Name of a public cloud SQL account.
        account_id (str | Unset): ID assigned to a public cloud SQL account.
        user_name (None | str | Unset): User name.
        password (None | str | Unset): Password.
        description (None | str | Unset): Description of a public cloud SQL account.
        status (PublicCloudSqlAccountStatus | Unset): Status of a public cloud SQL account.
        appliance_uid (UUID | Unset): UID assigned to a Veeam Backup for Public Clouds appliance.
        site_uid (UUID | Unset): UID assigned to a Veeam Cloud Connect site.
        management_agent_uid (UUID | Unset): UID assigned to a management agent installed on a Veeam Backup for Public
            Clouds appliance server.
    """

    account_name: str
    account_id: str | Unset = UNSET
    user_name: None | str | Unset = UNSET
    password: None | str | Unset = UNSET
    description: None | str | Unset = UNSET
    status: PublicCloudSqlAccountStatus | Unset = UNSET
    appliance_uid: UUID | Unset = UNSET
    site_uid: UUID | Unset = UNSET
    management_agent_uid: UUID | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        account_name = self.account_name

        account_id = self.account_id

        user_name: None | str | Unset
        if isinstance(self.user_name, Unset):
            user_name = UNSET
        else:
            user_name = self.user_name

        password: None | str | Unset
        if isinstance(self.password, Unset):
            password = UNSET
        else:
            password = self.password

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        appliance_uid: str | Unset = UNSET
        if not isinstance(self.appliance_uid, Unset):
            appliance_uid = str(self.appliance_uid)

        site_uid: str | Unset = UNSET
        if not isinstance(self.site_uid, Unset):
            site_uid = str(self.site_uid)

        management_agent_uid: str | Unset = UNSET
        if not isinstance(self.management_agent_uid, Unset):
            management_agent_uid = str(self.management_agent_uid)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "accountName": account_name,
            }
        )
        if account_id is not UNSET:
            field_dict["accountId"] = account_id
        if user_name is not UNSET:
            field_dict["userName"] = user_name
        if password is not UNSET:
            field_dict["password"] = password
        if description is not UNSET:
            field_dict["description"] = description
        if status is not UNSET:
            field_dict["status"] = status
        if appliance_uid is not UNSET:
            field_dict["applianceUid"] = appliance_uid
        if site_uid is not UNSET:
            field_dict["siteUid"] = site_uid
        if management_agent_uid is not UNSET:
            field_dict["managementAgentUid"] = management_agent_uid

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        account_name = d.pop("accountName")

        account_id = d.pop("accountId", UNSET)

        def _parse_user_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        user_name = _parse_user_name(d.pop("userName", UNSET))

        def _parse_password(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        password = _parse_password(d.pop("password", UNSET))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        _status = d.pop("status", UNSET)
        status: PublicCloudSqlAccountStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = PublicCloudSqlAccountStatus(_status)

        _appliance_uid = d.pop("applianceUid", UNSET)
        appliance_uid: UUID | Unset
        if isinstance(_appliance_uid, Unset):
            appliance_uid = UNSET
        else:
            appliance_uid = UUID(_appliance_uid)

        _site_uid = d.pop("siteUid", UNSET)
        site_uid: UUID | Unset
        if isinstance(_site_uid, Unset):
            site_uid = UNSET
        else:
            site_uid = UUID(_site_uid)

        _management_agent_uid = d.pop("managementAgentUid", UNSET)
        management_agent_uid: UUID | Unset
        if isinstance(_management_agent_uid, Unset):
            management_agent_uid = UNSET
        else:
            management_agent_uid = UUID(_management_agent_uid)

        public_cloud_sql_account = cls(
            account_name=account_name,
            account_id=account_id,
            user_name=user_name,
            password=password,
            description=description,
            status=status,
            appliance_uid=appliance_uid,
            site_uid=site_uid,
            management_agent_uid=management_agent_uid,
        )

        public_cloud_sql_account.additional_properties = d
        return public_cloud_sql_account

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
