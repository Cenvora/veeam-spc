from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.backup_server_email_notification_settings_type_0 import BackupServerEmailNotificationSettingsType0
    from ..models.backup_server_notification_vm_attribute_settings_type_0 import (
        BackupServerNotificationVmAttributeSettingsType0,
    )


T = TypeVar("T", bound="BackupServerBackupJobNotificationSettingsType0")


@_attrs_define
class BackupServerBackupJobNotificationSettingsType0:
    """Notification settings.

    Attributes:
        send_snmp_notifications (Union[Unset, bool]): Indicates whether SNMP notifications are enabled for a job.
            Default: False.
        email_notifications (Union['BackupServerEmailNotificationSettingsType0', None, Unset]): Email notification
            settings.
        vm_attribute (Union['BackupServerNotificationVmAttributeSettingsType0', None, Unset]): VM attribute settings.
    """

    send_snmp_notifications: Union[Unset, bool] = False
    email_notifications: Union["BackupServerEmailNotificationSettingsType0", None, Unset] = UNSET
    vm_attribute: Union["BackupServerNotificationVmAttributeSettingsType0", None, Unset] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.backup_server_email_notification_settings_type_0 import BackupServerEmailNotificationSettingsType0
        from ..models.backup_server_notification_vm_attribute_settings_type_0 import (
            BackupServerNotificationVmAttributeSettingsType0,
        )

        send_snmp_notifications = self.send_snmp_notifications

        email_notifications: Union[None, Unset, dict[str, Any]]
        if isinstance(self.email_notifications, Unset):
            email_notifications = UNSET
        elif isinstance(self.email_notifications, BackupServerEmailNotificationSettingsType0):
            email_notifications = self.email_notifications.to_dict()
        else:
            email_notifications = self.email_notifications

        vm_attribute: Union[None, Unset, dict[str, Any]]
        if isinstance(self.vm_attribute, Unset):
            vm_attribute = UNSET
        elif isinstance(self.vm_attribute, BackupServerNotificationVmAttributeSettingsType0):
            vm_attribute = self.vm_attribute.to_dict()
        else:
            vm_attribute = self.vm_attribute

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
        from ..models.backup_server_email_notification_settings_type_0 import BackupServerEmailNotificationSettingsType0
        from ..models.backup_server_notification_vm_attribute_settings_type_0 import (
            BackupServerNotificationVmAttributeSettingsType0,
        )

        d = dict(src_dict)
        send_snmp_notifications = d.pop("sendSNMPNotifications", UNSET)

        def _parse_email_notifications(
            data: object,
        ) -> Union["BackupServerEmailNotificationSettingsType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_backup_server_email_notification_settings_type_0 = (
                    BackupServerEmailNotificationSettingsType0.from_dict(data)
                )

                return componentsschemas_backup_server_email_notification_settings_type_0
            except:  # noqa: E722
                pass
            return cast(Union["BackupServerEmailNotificationSettingsType0", None, Unset], data)

        email_notifications = _parse_email_notifications(d.pop("emailNotifications", UNSET))

        def _parse_vm_attribute(data: object) -> Union["BackupServerNotificationVmAttributeSettingsType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_backup_server_notification_vm_attribute_settings_type_0 = (
                    BackupServerNotificationVmAttributeSettingsType0.from_dict(data)
                )

                return componentsschemas_backup_server_notification_vm_attribute_settings_type_0
            except:  # noqa: E722
                pass
            return cast(Union["BackupServerNotificationVmAttributeSettingsType0", None, Unset], data)

        vm_attribute = _parse_vm_attribute(d.pop("vmAttribute", UNSET))

        backup_server_backup_job_notification_settings_type_0 = cls(
            send_snmp_notifications=send_snmp_notifications,
            email_notifications=email_notifications,
            vm_attribute=vm_attribute,
        )

        backup_server_backup_job_notification_settings_type_0.additional_properties = d
        return backup_server_backup_job_notification_settings_type_0

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
