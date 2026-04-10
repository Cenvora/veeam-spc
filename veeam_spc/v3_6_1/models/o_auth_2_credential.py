import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

if TYPE_CHECKING:
    from ..models.o_auth_2_client_settings import OAuth2ClientSettings


T = TypeVar("T", bound="OAuth2Credential")


@_attrs_define
class OAuth2Credential:
    """
    Attributes:
        client_settings (OAuth2ClientSettings):
        user_id (Union[None, str]): User ID required to access the server.
        access_token (str): Access token.
        access_token_expiration (datetime.datetime): Date and time of the token expiration.
        refresh_token (str): Resfresh token.
    """

    client_settings: "OAuth2ClientSettings"
    user_id: Union[None, str]
    access_token: str
    access_token_expiration: datetime.datetime
    refresh_token: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        client_settings = self.client_settings.to_dict()

        user_id: Union[None, str]
        user_id = self.user_id

        access_token = self.access_token

        access_token_expiration = self.access_token_expiration.isoformat()

        refresh_token = self.refresh_token

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "clientSettings": client_settings,
                "userId": user_id,
                "accessToken": access_token,
                "accessTokenExpiration": access_token_expiration,
                "refreshToken": refresh_token,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.o_auth_2_client_settings import OAuth2ClientSettings

        d = dict(src_dict)
        client_settings = OAuth2ClientSettings.from_dict(d.pop("clientSettings"))

        def _parse_user_id(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        user_id = _parse_user_id(d.pop("userId"))

        access_token = d.pop("accessToken")

        access_token_expiration = isoparse(d.pop("accessTokenExpiration"))

        refresh_token = d.pop("refreshToken")

        o_auth_2_credential = cls(
            client_settings=client_settings,
            user_id=user_id,
            access_token=access_token,
            access_token_expiration=access_token_expiration,
            refresh_token=refresh_token,
        )

        o_auth_2_credential.additional_properties = d
        return o_auth_2_credential

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
