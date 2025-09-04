from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Vb365Microsoft365BasicAuthenticationCommonConnectionSettings")


@_attrs_define
class Vb365Microsoft365BasicAuthenticationCommonConnectionSettings:
    """
    Attributes:
        account (str): User name of an account.
        password (str): Password of an account.
        grant_admin_access (Union[Unset, bool]): Indicates whether the `ApplicationImpersonation` role is assigned to an
            account. This role is required to back up Microsoft Exchange Online mailboxes.
            To assign the ApplicationImpersonation role, make sure the account that you use is a member of the Organization
            Management group and has been granted the Role Management role in advance.
             Default: False.
        use_custom_veeam_aad_application (Union[Unset, bool]): Indicates whether Veeam Backup for Microsoft 365 must use
            Veeam Azure AD Application to connect to a Microsoft organization. Default: False.
    """

    account: str
    password: str
    grant_admin_access: Union[Unset, bool] = False
    use_custom_veeam_aad_application: Union[Unset, bool] = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        account = self.account

        password = self.password

        grant_admin_access = self.grant_admin_access

        use_custom_veeam_aad_application = self.use_custom_veeam_aad_application

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "account": account,
                "password": password,
            }
        )
        if grant_admin_access is not UNSET:
            field_dict["grantAdminAccess"] = grant_admin_access
        if use_custom_veeam_aad_application is not UNSET:
            field_dict["useCustomVeeamAADApplication"] = use_custom_veeam_aad_application

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        account = d.pop("account")

        password = d.pop("password")

        grant_admin_access = d.pop("grantAdminAccess", UNSET)

        use_custom_veeam_aad_application = d.pop("useCustomVeeamAADApplication", UNSET)

        vb_365_microsoft_365_basic_authentication_common_connection_settings = cls(
            account=account,
            password=password,
            grant_admin_access=grant_admin_access,
            use_custom_veeam_aad_application=use_custom_veeam_aad_application,
        )

        vb_365_microsoft_365_basic_authentication_common_connection_settings.additional_properties = d
        return vb_365_microsoft_365_basic_authentication_common_connection_settings

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
