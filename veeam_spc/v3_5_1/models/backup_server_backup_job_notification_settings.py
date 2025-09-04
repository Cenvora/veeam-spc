from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.backup_server_email_notification_settings import BackupServerEmailNotificationSettings
    from ..models.backup_server_notification_vm_attribute_settings import BackupServerNotificationVmAttributeSettings


T = TypeVar("T", bound="BackupServerBackupJobNotificationSettings")


@_attrs_define
class BackupServerBackupJobNotificationSettings:
    """Notification settings.

    Attributes:
        send_snmp_notifications (Union[Unset, bool]): Indicates whether SNMP notifications are enabled for a job.
            Default: False.
        email_notifications (Union[Unset, BackupServerEmailNotificationSettings]): Email notification settings.
        vm_attribute (Union[Unset, BackupServerNotificationVmAttributeSettings]): VM attribute settings.
    """

    send_snmp_notifications: Union[Unset, bool] = False
    email_notifications: Union[Unset, "BackupServerEmailNotificationSettings"] = UNSET
    vm_attribute: Union[Unset, "BackupServerNotificationVmAttributeSettings"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        send_snmp_notifications = self.send_snmp_notifications

        email_notifications: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.email_notifications, Unset):
            email_notifications = self.email_notifications.to_dict()

        vm_attribute: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.vm_attribute, Unset):
            vm_attribute = self.vm_attribute.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if send_snmp_notifications is not UNSET:
            field_dict["sendSNMPNotifications"] = send_snmp_notifications
        if email_notifications is not UNSET:
            field_dict["emailNotifications"] = email_notifications
        if vm_attribute is not UNSET:
            field_dict["vmAttribute"] = vm_attribute

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.backup_server_email_notification_settings import BackupServerEmailNotificationSettings
        from ..models.backup_server_notification_vm_attribute_settings import (
            BackupServerNotificationVmAttributeSettings,
        )

        d = dict(src_dict)
        send_snmp_notifications = d.pop("sendSNMPNotifications", UNSET)

        _email_notifications = d.pop("emailNotifications", UNSET)
        email_notifications: Union[Unset, BackupServerEmailNotificationSettings]
        if isinstance(_email_notifications, Unset):
            email_notifications = UNSET
        else:
            email_notifications = BackupServerEmailNotificationSettings.from_dict(_email_notifications)

        _vm_attribute = d.pop("vmAttribute", UNSET)
        vm_attribute: Union[Unset, BackupServerNotificationVmAttributeSettings]
        if isinstance(_vm_attribute, Unset):
            vm_attribute = UNSET
        else:
            vm_attribute = BackupServerNotificationVmAttributeSettings.from_dict(_vm_attribute)

        backup_server_backup_job_notification_settings = cls(
            send_snmp_notifications=send_snmp_notifications,
            email_notifications=email_notifications,
            vm_attribute=vm_attribute,
        )

        backup_server_backup_job_notification_settings.additional_properties = d
        return backup_server_backup_job_notification_settings

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
