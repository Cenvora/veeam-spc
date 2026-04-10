from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.backup_server_email_notification_type import BackupServerEmailNotificationType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.backup_server_email_custom_notification_type import BackupServerEmailCustomNotificationType


T = TypeVar("T", bound="BackupServerEmailNotificationSettings")


@_attrs_define
class BackupServerEmailNotificationSettings:
    """Email notification settings.

    Attributes:
        is_enabled (bool): Indicates whether email notifications are enabled.
        recipients (list[str] | Unset): Array of email addresses of notification recipients.
        notification_type (BackupServerEmailNotificationType | Unset): Type of email notification settings applied to a
            current job.
        custom_notification_settings (BackupServerEmailCustomNotificationType | Unset): Custom notification settings.
    """

    is_enabled: bool
    recipients: list[str] | Unset = UNSET
    notification_type: BackupServerEmailNotificationType | Unset = UNSET
    custom_notification_settings: BackupServerEmailCustomNotificationType | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        is_enabled = self.is_enabled

        recipients: list[str] | Unset = UNSET
        if not isinstance(self.recipients, Unset):
            recipients = self.recipients

        notification_type: str | Unset = UNSET
        if not isinstance(self.notification_type, Unset):
            notification_type = self.notification_type.value

        custom_notification_settings: dict[str, Any] | Unset = UNSET
        if not isinstance(self.custom_notification_settings, Unset):
            custom_notification_settings = self.custom_notification_settings.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "isEnabled": is_enabled,
            }
        )
        if recipients is not UNSET:
            field_dict["recipients"] = recipients
        if notification_type is not UNSET:
            field_dict["notificationType"] = notification_type
        if custom_notification_settings is not UNSET:
            field_dict["customNotificationSettings"] = custom_notification_settings

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.backup_server_email_custom_notification_type import BackupServerEmailCustomNotificationType

        d = dict(src_dict)
        is_enabled = d.pop("isEnabled")

        recipients = cast(list[str], d.pop("recipients", UNSET))

        _notification_type = d.pop("notificationType", UNSET)
        notification_type: BackupServerEmailNotificationType | Unset
        if isinstance(_notification_type, Unset):
            notification_type = UNSET
        else:
            notification_type = BackupServerEmailNotificationType(_notification_type)

        _custom_notification_settings = d.pop("customNotificationSettings", UNSET)
        custom_notification_settings: BackupServerEmailCustomNotificationType | Unset
        if isinstance(_custom_notification_settings, Unset):
            custom_notification_settings = UNSET
        else:
            custom_notification_settings = BackupServerEmailCustomNotificationType.from_dict(
                _custom_notification_settings
            )

        backup_server_email_notification_settings = cls(
            is_enabled=is_enabled,
            recipients=recipients,
            notification_type=notification_type,
            custom_notification_settings=custom_notification_settings,
        )

        backup_server_email_notification_settings.additional_properties = d
        return backup_server_email_notification_settings

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
