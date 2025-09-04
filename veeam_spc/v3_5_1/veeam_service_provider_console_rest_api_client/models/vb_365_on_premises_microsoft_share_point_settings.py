from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Vb365OnPremisesMicrosoftSharePointSettings")


@_attrs_define
class Vb365OnPremisesMicrosoftSharePointSettings:
    """
    Attributes:
        server_name (Union[Unset, str]): Microsoft SharePoint Online server EWS endpoint URL.
        server_port (Union[None, Unset, int]): Port that is used to access a Microsoft SharePoint Online server. Default
            port is 5985.
        grant_impersonation (Union[Unset, bool]): Indicates whether backup jobs can process all items within a Microsoft
            SharePoint Online organization.
        user_name (Union[Unset, str]): User name of an account that is used to access an on-premises Microsoft
            SharePoint Online organization.
        use_ssl (Union[Unset, bool]): Indicates whether Veeam Backup for Microsoft Office 365 uses a secure connection
            with Microsoft SharePoint organization server.
        skip_c_averification (Union[Unset, bool]): Indicates whether Certificate Authority verification check must not
            be performed.
        skip_common_name_verification (Union[Unset, bool]): Indicates whether Common Name verification check must not be
            performed.
        skip_revocation_check (Union[Unset, bool]): Indicates whether the check of certificate expiration against the
            certificate revocation list must not be performed.
    """

    server_name: Union[Unset, str] = UNSET
    server_port: Union[None, Unset, int] = UNSET
    grant_impersonation: Union[Unset, bool] = UNSET
    user_name: Union[Unset, str] = UNSET
    use_ssl: Union[Unset, bool] = UNSET
    skip_c_averification: Union[Unset, bool] = UNSET
    skip_common_name_verification: Union[Unset, bool] = UNSET
    skip_revocation_check: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        server_name = self.server_name

        server_port: Union[None, Unset, int]
        if isinstance(self.server_port, Unset):
            server_port = UNSET
        else:
            server_port = self.server_port

        grant_impersonation = self.grant_impersonation

        user_name = self.user_name

        use_ssl = self.use_ssl

        skip_c_averification = self.skip_c_averification

        skip_common_name_verification = self.skip_common_name_verification

        skip_revocation_check = self.skip_revocation_check

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if server_name is not UNSET:
            field_dict["serverName"] = server_name
        if server_port is not UNSET:
            field_dict["serverPort"] = server_port
        if grant_impersonation is not UNSET:
            field_dict["grantImpersonation"] = grant_impersonation
        if user_name is not UNSET:
            field_dict["userName"] = user_name
        if use_ssl is not UNSET:
            field_dict["useSSL"] = use_ssl
        if skip_c_averification is not UNSET:
            field_dict["skipCAverification"] = skip_c_averification
        if skip_common_name_verification is not UNSET:
            field_dict["skipCommonNameVerification"] = skip_common_name_verification
        if skip_revocation_check is not UNSET:
            field_dict["skipRevocationCheck"] = skip_revocation_check

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        server_name = d.pop("serverName", UNSET)

        def _parse_server_port(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        server_port = _parse_server_port(d.pop("serverPort", UNSET))

        grant_impersonation = d.pop("grantImpersonation", UNSET)

        user_name = d.pop("userName", UNSET)

        use_ssl = d.pop("useSSL", UNSET)

        skip_c_averification = d.pop("skipCAverification", UNSET)

        skip_common_name_verification = d.pop("skipCommonNameVerification", UNSET)

        skip_revocation_check = d.pop("skipRevocationCheck", UNSET)

        vb_365_on_premises_microsoft_share_point_settings = cls(
            server_name=server_name,
            server_port=server_port,
            grant_impersonation=grant_impersonation,
            user_name=user_name,
            use_ssl=use_ssl,
            skip_c_averification=skip_c_averification,
            skip_common_name_verification=skip_common_name_verification,
            skip_revocation_check=skip_revocation_check,
        )

        vb_365_on_premises_microsoft_share_point_settings.additional_properties = d
        return vb_365_on_premises_microsoft_share_point_settings

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
