from collections.abc import Mapping
from typing import Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.o_auth_2_issue_token_body_grant_type import OAuth2IssueTokenBodyGrantType
from ..types import UNSET, Unset

T = TypeVar("T", bound="OAuth2IssueTokenBody")


@_attrs_define
class OAuth2IssueTokenBody:
    """
    Attributes:
        grant_type (OAuth2IssueTokenBodyGrantType): Grant type according to RFC 6749. Example: password.
        username (Union[Unset, str]): User name.
            > Used with the `password` grant type.
             Example: restv3vacadministrator.
        password (Union[Unset, str]): Password.
            > Used with the `password` grant type.
             Example: secretPassword.
        refresh_token (Union[Unset, str]): Refresh token.
            > Used with the `refresh_token` and `as` grant type.
        mfa_token (Union[Unset, str]): Multi-factor authentication token.
            > Used with the `mfa` grant type.
        mfa_code (Union[Unset, str]): Multi-factor authentication code.
            > Used with the `mfa` grant type.
        code (Union[Unset, str]): Authorization code.
            > Used with the `authorization_code` grant type.
        public_key (Union[Unset, str]): Public key encoded in the Base64 format.
            > Used with the `public_key` grant type.
        user_uid (Union[Unset, UUID]): UID assigned to a user whose account must be used for authentication.
            > Used with the `as` grant type.
        read_only (Union[Unset, bool]): Defines whether a read-only access token must be issued.
            > Used with any grant type.
    """

    grant_type: OAuth2IssueTokenBodyGrantType
    username: Union[Unset, str] = UNSET
    password: Union[Unset, str] = UNSET
    refresh_token: Union[Unset, str] = UNSET
    mfa_token: Union[Unset, str] = UNSET
    mfa_code: Union[Unset, str] = UNSET
    code: Union[Unset, str] = UNSET
    public_key: Union[Unset, str] = UNSET
    user_uid: Union[Unset, UUID] = UNSET
    read_only: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        grant_type = self.grant_type.value

        username = self.username

        password = self.password

        refresh_token = self.refresh_token

        mfa_token = self.mfa_token

        mfa_code = self.mfa_code

        code = self.code

        public_key = self.public_key

        user_uid: Union[Unset, str] = UNSET
        if not isinstance(self.user_uid, Unset):
            user_uid = str(self.user_uid)

        read_only = self.read_only

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "grant_type": grant_type,
            }
        )
        if username is not UNSET:
            field_dict["username"] = username
        if password is not UNSET:
            field_dict["password"] = password
        if refresh_token is not UNSET:
            field_dict["refresh_token"] = refresh_token
        if mfa_token is not UNSET:
            field_dict["mfa_token"] = mfa_token
        if mfa_code is not UNSET:
            field_dict["mfa_code"] = mfa_code
        if code is not UNSET:
            field_dict["code"] = code
        if public_key is not UNSET:
            field_dict["public_key"] = public_key
        if user_uid is not UNSET:
            field_dict["userUid"] = user_uid
        if read_only is not UNSET:
            field_dict["readOnly"] = read_only

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        grant_type = OAuth2IssueTokenBodyGrantType(d.pop("grant_type"))

        username = d.pop("username", UNSET)

        password = d.pop("password", UNSET)

        refresh_token = d.pop("refresh_token", UNSET)

        mfa_token = d.pop("mfa_token", UNSET)

        mfa_code = d.pop("mfa_code", UNSET)

        code = d.pop("code", UNSET)

        public_key = d.pop("public_key", UNSET)

        _user_uid = d.pop("userUid", UNSET)
        user_uid: Union[Unset, UUID]
        if isinstance(_user_uid, Unset):
            user_uid = UNSET
        else:
            user_uid = UUID(_user_uid)

        read_only = d.pop("readOnly", UNSET)

        o_auth_2_issue_token_body = cls(
            grant_type=grant_type,
            username=username,
            password=password,
            refresh_token=refresh_token,
            mfa_token=mfa_token,
            mfa_code=mfa_code,
            code=code,
            public_key=public_key,
            user_uid=user_uid,
            read_only=read_only,
        )

        o_auth_2_issue_token_body.additional_properties = d
        return o_auth_2_issue_token_body

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
