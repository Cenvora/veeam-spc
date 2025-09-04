from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.notification_settings_level import NotificationSettingsLevel
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.notification_alarms_settings import NotificationAlarmsSettings
    from ..models.notification_billing_settings import NotificationBillingSettings
    from ..models.notification_discovery_settings import NotificationDiscoverySettings
    from ..models.notification_license_settings import NotificationLicenseSettings
    from ..models.smtp_settings_type_0 import SmtpSettingsType0


T = TypeVar("T", bound="NotificationSettings")


@_attrs_define
class NotificationSettings:
    """
    Attributes:
        billing (NotificationBillingSettings):
        discovery (NotificationDiscoverySettings):
        alarms (NotificationAlarmsSettings):
        license_ (NotificationLicenseSettings):
        smtp (Union['SmtpSettingsType0', None, Unset]):
        level (Union[Unset, NotificationSettingsLevel]): Level of notifications. Default:
            NotificationSettingsLevel.DISABLED.
        default_from (Union[None, Unset, str]): Default email address from which notification messages must be sent.
    """

    billing: "NotificationBillingSettings"
    discovery: "NotificationDiscoverySettings"
    alarms: "NotificationAlarmsSettings"
    license_: "NotificationLicenseSettings"
    smtp: Union["SmtpSettingsType0", None, Unset] = UNSET
    level: Union[Unset, NotificationSettingsLevel] = NotificationSettingsLevel.DISABLED
    default_from: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.smtp_settings_type_0 import SmtpSettingsType0

        billing = self.billing.to_dict()

        discovery = self.discovery.to_dict()

        alarms = self.alarms.to_dict()

        license_ = self.license_.to_dict()

        smtp: Union[None, Unset, dict[str, Any]]
        if isinstance(self.smtp, Unset):
            smtp = UNSET
        elif isinstance(self.smtp, SmtpSettingsType0):
            smtp = self.smtp.to_dict()
        else:
            smtp = self.smtp

        level: Union[Unset, str] = UNSET
        if not isinstance(self.level, Unset):
            level = self.level.value

        default_from: Union[None, Unset, str]
        if isinstance(self.default_from, Unset):
            default_from = UNSET
        else:
            default_from = self.default_from

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "billing": billing,
                "discovery": discovery,
                "alarms": alarms,
                "license": license_,
            }
        )
        if smtp is not UNSET:
            field_dict["smtp"] = smtp
        if level is not UNSET:
            field_dict["level"] = level
        if default_from is not UNSET:
            field_dict["defaultFrom"] = default_from

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.notification_alarms_settings import NotificationAlarmsSettings
        from ..models.notification_billing_settings import NotificationBillingSettings
        from ..models.notification_discovery_settings import NotificationDiscoverySettings
        from ..models.notification_license_settings import NotificationLicenseSettings
        from ..models.smtp_settings_type_0 import SmtpSettingsType0

        d = dict(src_dict)
        billing = NotificationBillingSettings.from_dict(d.pop("billing"))

        discovery = NotificationDiscoverySettings.from_dict(d.pop("discovery"))

        alarms = NotificationAlarmsSettings.from_dict(d.pop("alarms"))

        license_ = NotificationLicenseSettings.from_dict(d.pop("license"))

        def _parse_smtp(data: object) -> Union["SmtpSettingsType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_smtp_settings_type_0 = SmtpSettingsType0.from_dict(data)

                return componentsschemas_smtp_settings_type_0
            except:  # noqa: E722
                pass
            return cast(Union["SmtpSettingsType0", None, Unset], data)

        smtp = _parse_smtp(d.pop("smtp", UNSET))

        _level = d.pop("level", UNSET)
        level: Union[Unset, NotificationSettingsLevel]
        if isinstance(_level, Unset):
            level = UNSET
        else:
            level = NotificationSettingsLevel(_level)

        def _parse_default_from(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        default_from = _parse_default_from(d.pop("defaultFrom", UNSET))

        notification_settings = cls(
            billing=billing,
            discovery=discovery,
            alarms=alarms,
            license_=license_,
            smtp=smtp,
            level=level,
            default_from=default_from,
        )

        notification_settings.additional_properties = d
        return notification_settings

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
