import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.user_login_scopes_item import UserLoginScopesItem
from ..models.user_login_status import UserLoginStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="UserLogin")


@_attrs_define
class UserLogin:
    """
    Attributes:
        id (int): System ID assigned to a user identity.
        user_uid (UUID): UID assigned to a user.
        identity_provider_name (str): Name of an identity provider that manages user identity.
        description (str): Description of a user identity.
        is_read_access_only (bool): Indicates whether a user identity has the read-only access.
        status (UserLoginStatus): User identity status.
            > You can change status to `enabled` or `disabled` using the PATCH method.
        identifier_in_provider (str): Provided identity.
        user_name (Union[Unset, str]): User name.
        company_id (Union[Unset, UUID]): UID assigned to a user company.
        company_name (Union[Unset, str]): Name of a user company.
        scopes (Union[Unset, list[UserLoginScopesItem]]): Services that are available to the user identity.
        parameters (Union[Unset, str]): Parameters of a user identity.
        creation_date (Union[Unset, datetime.datetime]): Date and time of identity creation.
    """

    id: int
    user_uid: UUID
    identity_provider_name: str
    description: str
    is_read_access_only: bool
    status: UserLoginStatus
    identifier_in_provider: str
    user_name: Union[Unset, str] = UNSET
    company_id: Union[Unset, UUID] = UNSET
    company_name: Union[Unset, str] = UNSET
    scopes: Union[Unset, list[UserLoginScopesItem]] = UNSET
    parameters: Union[Unset, str] = UNSET
    creation_date: Union[Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        user_uid = str(self.user_uid)

        identity_provider_name = self.identity_provider_name

        description = self.description

        is_read_access_only = self.is_read_access_only

        status = self.status.value

        identifier_in_provider = self.identifier_in_provider

        user_name = self.user_name

        company_id: Union[Unset, str] = UNSET
        if not isinstance(self.company_id, Unset):
            company_id = str(self.company_id)

        company_name = self.company_name

        scopes: Union[Unset, list[str]] = UNSET
        if not isinstance(self.scopes, Unset):
            scopes = []
            for scopes_item_data in self.scopes:
                scopes_item = scopes_item_data.value
                scopes.append(scopes_item)

        parameters = self.parameters

        creation_date: Union[Unset, str] = UNSET
        if not isinstance(self.creation_date, Unset):
            creation_date = self.creation_date.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "userUid": user_uid,
                "identityProviderName": identity_provider_name,
                "description": description,
                "isReadAccessOnly": is_read_access_only,
                "status": status,
                "identifierInProvider": identifier_in_provider,
            }
        )
        if user_name is not UNSET:
            field_dict["userName"] = user_name
        if company_id is not UNSET:
            field_dict["companyId"] = company_id
        if company_name is not UNSET:
            field_dict["companyName"] = company_name
        if scopes is not UNSET:
            field_dict["scopes"] = scopes
        if parameters is not UNSET:
            field_dict["parameters"] = parameters
        if creation_date is not UNSET:
            field_dict["creationDate"] = creation_date

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        user_uid = UUID(d.pop("userUid"))

        identity_provider_name = d.pop("identityProviderName")

        description = d.pop("description")

        is_read_access_only = d.pop("isReadAccessOnly")

        status = UserLoginStatus(d.pop("status"))

        identifier_in_provider = d.pop("identifierInProvider")

        user_name = d.pop("userName", UNSET)

        _company_id = d.pop("companyId", UNSET)
        company_id: Union[Unset, UUID]
        if isinstance(_company_id, Unset):
            company_id = UNSET
        else:
            company_id = UUID(_company_id)

        company_name = d.pop("companyName", UNSET)

        scopes = []
        _scopes = d.pop("scopes", UNSET)
        for scopes_item_data in _scopes or []:
            scopes_item = UserLoginScopesItem(scopes_item_data)

            scopes.append(scopes_item)

        parameters = d.pop("parameters", UNSET)

        _creation_date = d.pop("creationDate", UNSET)
        creation_date: Union[Unset, datetime.datetime]
        if isinstance(_creation_date, Unset):
            creation_date = UNSET
        else:
            creation_date = isoparse(_creation_date)

        user_login = cls(
            id=id,
            user_uid=user_uid,
            identity_provider_name=identity_provider_name,
            description=description,
            is_read_access_only=is_read_access_only,
            status=status,
            identifier_in_provider=identifier_in_provider,
            user_name=user_name,
            company_id=company_id,
            company_name=company_name,
            scopes=scopes,
            parameters=parameters,
            creation_date=creation_date,
        )

        user_login.additional_properties = d
        return user_login

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
