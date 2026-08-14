from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.deploy_schedule import DeploySchedule
    from ..models.vbr_deployment_configuration import VbrDeploymentConfiguration


T = TypeVar("T", bound="VbrScheduledDeploymentConfiguration")


@_attrs_define
class VbrScheduledDeploymentConfiguration:
    r"""
    Example:
        {'configuration': {'distribution': {'filePath':
            '\\\\tech.local\\tech\\VSPC\\VBR\\13\\Butler\\VeeamBackup&Replication_13.iso', 'userName': 'vspc\\admin',
            'password': 'Password1'}, 'usePredownloadedIso': False, 'answerXml': '<?xml version="1.0"
            encoding="utf-8"?>\r\n<unattendedInstallationConfiguration bundle="VBR" mode="upgrade">\r\n
            <properties>\r\n\r\n    <!--License agreements-->\r\n    <property name="ACCEPT_EULA" value="1" />\r\n
            <property name="ACCEPT_LICENSING_POLICY" value="1" />\r\n    <property name="ACCEPT_THIRDPARTY_LICENSES"
            value="1" />\r\n    <property name="ACCEPT_REQUIRED_SOFTWARE" value="1" />\r\n\r\n    <!--License file-->\r\n
            <property name="VBR_LICENSE_AUTOUPDATE" value="1" />\r\n\r\n    <!--Service account-->\r\n    <property
            name="VBR_SERVICE_PASSWORD" value="Password1" hidden="1" />\r\n\r\n    <!--Database configuration-->\r\n
            <property name="VBR_SQLSERVER_PASSWORD" value="Password1" hidden="1" />\r\n\r\n    <!--Automatic update
            settings-->\r\n    <property name="VBR_AUTO_UPGRADE" value="1" />\r\n\r\n
            </properties>\r\n</unattendedInstallationConfiguration>\r\n', 'allowAutoReboot': True, 'stopAllActivities':
            True, 'useManagementAgentCredentials': True, 'adminCredentials': {'username': 'vspc\\admin', 'password':
            'Password1'}}, 'schedule': {'dateTime': '2025-07-24T00:23:16.3525528-05:00'}}

    Attributes:
        configuration (VbrDeploymentConfiguration): If the `distribution` and `usePredownloadedIso` properties have the
            `null` value, the most recent version of Veeam Backup & Replication will be downloaded automatically. Example:
            {'distribution': {'filePath': '\\\\tech.local\\tech\\VSPC\\VBR\\13\\Butler\\VeeamBackup&Replication_13.iso',
            'userName': 'vspc1\\admin', 'password': 'Password1'}, 'usePredownloadedIso': False, 'answerXml': '<?xml
            version="1.0" encoding="utf-8"?>\r\n<unattendedInstallationConfiguration bundle="VBR" mode="upgrade">\r\n
            <properties>\r\n\r\n    <!--License agreements-->\r\n    <property name="ACCEPT_EULA" value="1" />\r\n
            <property name="ACCEPT_LICENSING_POLICY" value="1" />\r\n    <property name="ACCEPT_THIRDPARTY_LICENSES"
            value="1" />\r\n    <property name="ACCEPT_REQUIRED_SOFTWARE" value="1" />\r\n\r\n    <!--License file-->\r\n
            <!--property name="VBR_LICENSE_FILE" value="" /-->\r\n    <property name="VBR_LICENSE_AUTOUPDATE" value="1"
            />\r\n\r\n    <!--Service account-->\r\n    <!--property name="VBR_SERVICE_PASSWORD" value=""
            hidden="1"/-->\r\n\r\n    <!--Database configuration-->\r\n    <property name="VBR_SQLSERVER_PASSWORD"
            value="Password1" hidden="1"/>\r\n\r\n    <!--Automatic update settings-->\r\n    <property
            name="VBR_AUTO_UPGRADE" value="1" />\r\n\r\n  </properties>\r\n</unattendedInstallationConfiguration>\r\n',
            'allowAutoReboot': True, 'stopAllActivities': True, 'useManagementAgentCredentials': False, 'adminCredentials':
            {'username': 'vspc1\\admin', 'password': 'Password1'}}.
        schedule (DeploySchedule):
    """

    configuration: VbrDeploymentConfiguration
    schedule: DeploySchedule
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        configuration = self.configuration.to_dict()

        schedule = self.schedule.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "configuration": configuration,
                "schedule": schedule,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.deploy_schedule import DeploySchedule
        from ..models.vbr_deployment_configuration import VbrDeploymentConfiguration

        d = dict(src_dict)
        configuration = VbrDeploymentConfiguration.from_dict(d.pop("configuration"))

        schedule = DeploySchedule.from_dict(d.pop("schedule"))

        vbr_scheduled_deployment_configuration = cls(
            configuration=configuration,
            schedule=schedule,
        )

        vbr_scheduled_deployment_configuration.additional_properties = d
        return vbr_scheduled_deployment_configuration

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
