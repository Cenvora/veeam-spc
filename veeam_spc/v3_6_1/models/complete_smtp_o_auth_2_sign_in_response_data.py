from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.o_auth_2_credential import OAuth2Credential


T = TypeVar("T", bound="CompleteSmtpOAuth2SignInResponseData")


@_attrs_define
class CompleteSmtpOAuth2SignInResponseData:
    """
    Attributes:
        credential (Union[Unset, OAuth2Credential]):
    """

    credential: Union[Unset, "OAuth2Credential"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        credential: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.credential, Unset):
            credential = self.credential.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if credential is not UNSET:
            field_dict["credential"] = credential

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.o_auth_2_credential import OAuth2Credential

        d = dict(src_dict)
        _credential = d.pop("credential", UNSET)
        credential: Union[Unset, OAuth2Credential]
        if isinstance(_credential, Unset):
            credential = UNSET
        else:
            credential = OAuth2Credential.from_dict(_credential)

        complete_smtp_o_auth_2_sign_in_response_data = cls(
            credential=credential,
        )

        complete_smtp_o_auth_2_sign_in_response_data.additional_properties = d
        return complete_smtp_o_auth_2_sign_in_response_data

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
