from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.plugin_user_login_data_formats import PluginUserLoginDataFormats
    from ..models.plugin_user_login_data_service_time_zone import PluginUserLoginDataServiceTimeZone
    from ..models.user import User


T = TypeVar("T", bound="PluginUserLoginData")


@_attrs_define
class PluginUserLoginData:
    """
    Attributes:
        logged (Union[Unset, bool]): Indicates whether user account is logged in.
        user (Union[Unset, User]):
        service_time_zone (Union[Unset, PluginUserLoginDataServiceTimeZone]):
        version (Union[Unset, str]): Plugin version.
        session_expiration_time (Union[Unset, int]): Session expiration time, in seconds.
        token_prolongation_period (Union[Unset, int]): Token prolongation period, in seconds.
        formats (Union[Unset, PluginUserLoginDataFormats]):
        color_scheme (Union[Unset, str]): Color scheme of Veeam Service Provider Console Administrator Portal.
        portal_name (Union[Unset, str]): Name of Veeam Service Provider Console Administrator Portal.
    """

    logged: Union[Unset, bool] = UNSET
    user: Union[Unset, "User"] = UNSET
    service_time_zone: Union[Unset, "PluginUserLoginDataServiceTimeZone"] = UNSET
    version: Union[Unset, str] = UNSET
    session_expiration_time: Union[Unset, int] = UNSET
    token_prolongation_period: Union[Unset, int] = UNSET
    formats: Union[Unset, "PluginUserLoginDataFormats"] = UNSET
    color_scheme: Union[Unset, str] = UNSET
    portal_name: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        logged = self.logged

        user: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.user, Unset):
            user = self.user.to_dict()

        service_time_zone: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.service_time_zone, Unset):
            service_time_zone = self.service_time_zone.to_dict()

        version = self.version

        session_expiration_time = self.session_expiration_time

        token_prolongation_period = self.token_prolongation_period

        formats: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.formats, Unset):
            formats = self.formats.to_dict()

        color_scheme = self.color_scheme

        portal_name = self.portal_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if logged is not UNSET:
            field_dict["logged"] = logged
        if user is not UNSET:
            field_dict["user"] = user
        if service_time_zone is not UNSET:
            field_dict["serviceTimeZone"] = service_time_zone
        if version is not UNSET:
            field_dict["version"] = version
        if session_expiration_time is not UNSET:
            field_dict["sessionExpirationTime"] = session_expiration_time
        if token_prolongation_period is not UNSET:
            field_dict["tokenProlongationPeriod"] = token_prolongation_period
        if formats is not UNSET:
            field_dict["formats"] = formats
        if color_scheme is not UNSET:
            field_dict["colorScheme"] = color_scheme
        if portal_name is not UNSET:
            field_dict["portalName"] = portal_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.plugin_user_login_data_formats import PluginUserLoginDataFormats
        from ..models.plugin_user_login_data_service_time_zone import PluginUserLoginDataServiceTimeZone
        from ..models.user import User

        d = dict(src_dict)
        logged = d.pop("logged", UNSET)

        _user = d.pop("user", UNSET)
        user: Union[Unset, User]
        if isinstance(_user, Unset):
            user = UNSET
        else:
            user = User.from_dict(_user)

        _service_time_zone = d.pop("serviceTimeZone", UNSET)
        service_time_zone: Union[Unset, PluginUserLoginDataServiceTimeZone]
        if isinstance(_service_time_zone, Unset):
            service_time_zone = UNSET
        else:
            service_time_zone = PluginUserLoginDataServiceTimeZone.from_dict(_service_time_zone)

        version = d.pop("version", UNSET)

        session_expiration_time = d.pop("sessionExpirationTime", UNSET)

        token_prolongation_period = d.pop("tokenProlongationPeriod", UNSET)

        _formats = d.pop("formats", UNSET)
        formats: Union[Unset, PluginUserLoginDataFormats]
        if isinstance(_formats, Unset):
            formats = UNSET
        else:
            formats = PluginUserLoginDataFormats.from_dict(_formats)

        color_scheme = d.pop("colorScheme", UNSET)

        portal_name = d.pop("portalName", UNSET)

        plugin_user_login_data = cls(
            logged=logged,
            user=user,
            service_time_zone=service_time_zone,
            version=version,
            session_expiration_time=session_expiration_time,
            token_prolongation_period=token_prolongation_period,
            formats=formats,
            color_scheme=color_scheme,
            portal_name=portal_name,
        )

        plugin_user_login_data.additional_properties = d
        return plugin_user_login_data

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
