from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
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
        username (None | str | Unset): User name.
            > Used with the `password` grant type.
             Example: restv3vacadministrator.
        password (None | str | Unset): Password.
            > Used with the `password` grant type.
             Example: secretPassword.
        refresh_token (None | str | Unset): Refresh token.
            > Used with the `refresh_token` and `as` grant type.
        mfa_token (None | str | Unset): Multi-factor authentication token.
            > Used with the `mfa` grant type.
        mfa_code (None | str | Unset): Multi-factor authentication code.
            > Used with the `mfa` grant type.
        code (None | str | Unset): Authorization code.
            > Used with the `authorization_code` grant type.
        public_key (None | str | Unset): Public key encoded in the Base64 format.
            > Used with the `public_key` grant type.
        user_uid (None | Unset | UUID): UID assigned to a user whose account must be used for authentication.
            > Used with the `as` grant type.
        read_only (bool | None | Unset): Defines whether a read-only access token must be issued.
            > Used with any grant type.
    """

    grant_type: OAuth2IssueTokenBodyGrantType
    username: None | str | Unset = UNSET
    password: None | str | Unset = UNSET
    refresh_token: None | str | Unset = UNSET
    mfa_token: None | str | Unset = UNSET
    mfa_code: None | str | Unset = UNSET
    code: None | str | Unset = UNSET
    public_key: None | str | Unset = UNSET
    user_uid: None | Unset | UUID = UNSET
    read_only: bool | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        grant_type = self.grant_type.value

        username: None | str | Unset
        if isinstance(self.username, Unset):
            username = UNSET
        else:
            username = self.username

        password: None | str | Unset
        if isinstance(self.password, Unset):
            password = UNSET
        else:
            password = self.password

        refresh_token: None | str | Unset
        if isinstance(self.refresh_token, Unset):
            refresh_token = UNSET
        else:
            refresh_token = self.refresh_token

        mfa_token: None | str | Unset
        if isinstance(self.mfa_token, Unset):
            mfa_token = UNSET
        else:
            mfa_token = self.mfa_token

        mfa_code: None | str | Unset
        if isinstance(self.mfa_code, Unset):
            mfa_code = UNSET
        else:
            mfa_code = self.mfa_code

        code: None | str | Unset
        if isinstance(self.code, Unset):
            code = UNSET
        else:
            code = self.code

        public_key: None | str | Unset
        if isinstance(self.public_key, Unset):
            public_key = UNSET
        else:
            public_key = self.public_key

        user_uid: None | str | Unset
        if isinstance(self.user_uid, Unset):
            user_uid = UNSET
        elif isinstance(self.user_uid, UUID):
            user_uid = str(self.user_uid)
        else:
            user_uid = self.user_uid

        read_only: bool | None | Unset
        if isinstance(self.read_only, Unset):
            read_only = UNSET
        else:
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

        def _parse_username(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        username = _parse_username(d.pop("username", UNSET))

        def _parse_password(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        password = _parse_password(d.pop("password", UNSET))

        def _parse_refresh_token(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        refresh_token = _parse_refresh_token(d.pop("refresh_token", UNSET))

        def _parse_mfa_token(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        mfa_token = _parse_mfa_token(d.pop("mfa_token", UNSET))

        def _parse_mfa_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        mfa_code = _parse_mfa_code(d.pop("mfa_code", UNSET))

        def _parse_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        code = _parse_code(d.pop("code", UNSET))

        def _parse_public_key(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        public_key = _parse_public_key(d.pop("public_key", UNSET))

        def _parse_user_uid(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                user_uid_type_0 = UUID(data)

                return user_uid_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        user_uid = _parse_user_uid(d.pop("userUid", UNSET))

        def _parse_read_only(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        read_only = _parse_read_only(d.pop("readOnly", UNSET))

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
