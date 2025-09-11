from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.o_auth_2_client_settings import OAuth2ClientSettings


T = TypeVar("T", bound="PrepareSmtpOAuth2SignInBody")


@_attrs_define
class PrepareSmtpOAuth2SignInBody:
    """
    Attributes:
        client_settings (OAuth2ClientSettings):
        redirect_url (str): Redirect URI. For details, see
            [RFC6749](https://datatracker.ietf.org/doc/html/rfc6749#section-3.1.2).
        state (Union[Unset, str]): Request state returned to a client. For details, see
            [RFC6749](https://datatracker.ietf.org/doc/html/rfc6749#section-4.1.1).
    """

    client_settings: "OAuth2ClientSettings"
    redirect_url: str
    state: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        client_settings = self.client_settings.to_dict()

        redirect_url = self.redirect_url

        state = self.state

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "clientSettings": client_settings,
                "redirectUrl": redirect_url,
            }
        )
        if state is not UNSET:
            field_dict["state"] = state

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.o_auth_2_client_settings import OAuth2ClientSettings

        d = dict(src_dict)
        client_settings = OAuth2ClientSettings.from_dict(d.pop("clientSettings"))

        redirect_url = d.pop("redirectUrl")

        state = d.pop("state", UNSET)

        prepare_smtp_o_auth_2_sign_in_body = cls(
            client_settings=client_settings,
            redirect_url=redirect_url,
            state=state,
        )

        prepare_smtp_o_auth_2_sign_in_body.additional_properties = d
        return prepare_smtp_o_auth_2_sign_in_body

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
