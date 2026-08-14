from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.notification_settings_level import NotificationSettingsLevel
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.notification_alarms_settings import NotificationAlarmsSettings
    from ..models.notification_billing_settings import NotificationBillingSettings
    from ..models.notification_discovery_settings import NotificationDiscoverySettings
    from ..models.notification_license_settings import NotificationLicenseSettings
    from ..models.smtp_settings import SmtpSettings


T = TypeVar("T", bound="NotificationSettings")


@_attrs_define
class NotificationSettings:
    """
    Attributes:
        billing (NotificationBillingSettings):
        discovery (NotificationDiscoverySettings):
        alarms (NotificationAlarmsSettings):
        license_ (NotificationLicenseSettings):
        smtp (SmtpSettings | Unset):  Example: {'serverAddress': 'smtp://smtp1.tech.local:25', 'tlsMode': 'auto',
            'timeout': '00:05:00', 'passwordCredential': None, 'oAuth2Credential': None,
            'exclusivelyAcceptedCertificateHash': None}.
        level (NotificationSettingsLevel | Unset): Level of notifications. Default: NotificationSettingsLevel.DISABLED.
        default_sender_name (str | Unset): Name of a sender.
        default_from (str | Unset): Default email address from which notification messages must be sent.
    """

    billing: NotificationBillingSettings
    discovery: NotificationDiscoverySettings
    alarms: NotificationAlarmsSettings
    license_: NotificationLicenseSettings
    smtp: SmtpSettings | Unset = UNSET
    level: NotificationSettingsLevel | Unset = NotificationSettingsLevel.DISABLED
    default_sender_name: str | Unset = UNSET
    default_from: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        billing = self.billing.to_dict()

        discovery = self.discovery.to_dict()

        alarms = self.alarms.to_dict()

        license_ = self.license_.to_dict()

        smtp: dict[str, Any] | Unset = UNSET
        if not isinstance(self.smtp, Unset):
            smtp = self.smtp.to_dict()

        level: str | Unset = UNSET
        if not isinstance(self.level, Unset):
            level = self.level.value

        default_sender_name = self.default_sender_name

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
        if default_sender_name is not UNSET:
            field_dict["defaultSenderName"] = default_sender_name
        if default_from is not UNSET:
            field_dict["defaultFrom"] = default_from

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.notification_alarms_settings import NotificationAlarmsSettings
        from ..models.notification_billing_settings import NotificationBillingSettings
        from ..models.notification_discovery_settings import NotificationDiscoverySettings
        from ..models.notification_license_settings import NotificationLicenseSettings
        from ..models.smtp_settings import SmtpSettings

        d = dict(src_dict)
        billing = NotificationBillingSettings.from_dict(d.pop("billing"))

        discovery = NotificationDiscoverySettings.from_dict(d.pop("discovery"))

        alarms = NotificationAlarmsSettings.from_dict(d.pop("alarms"))

        license_ = NotificationLicenseSettings.from_dict(d.pop("license"))

        _smtp = d.pop("smtp", UNSET)
        smtp: SmtpSettings | Unset
        if isinstance(_smtp, Unset):
            smtp = UNSET
        else:
            smtp = SmtpSettings.from_dict(_smtp)

        _level = d.pop("level", UNSET)
        level: NotificationSettingsLevel | Unset
        if isinstance(_level, Unset):
            level = UNSET
        else:
            level = NotificationSettingsLevel(_level)

        default_sender_name = d.pop("defaultSenderName", UNSET)

        default_from = d.pop("defaultFrom", UNSET)

        notification_settings = cls(
            billing=billing,
            discovery=discovery,
            alarms=alarms,
            license_=license_,
            smtp=smtp,
            level=level,
            default_sender_name=default_sender_name,
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
