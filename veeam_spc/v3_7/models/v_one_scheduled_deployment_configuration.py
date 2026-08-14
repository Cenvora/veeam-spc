from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.deploy_schedule import DeploySchedule
    from ..models.v_one_deployment_configuration import VOneDeploymentConfiguration


T = TypeVar("T", bound="VOneScheduledDeploymentConfiguration")


@_attrs_define
class VOneScheduledDeploymentConfiguration:
    r"""
    Example:
        {'configuration': {'distribution': {'filePath':
            '\\\\tech.local\\tech\\VSPC\\VBR\\13\\Butler\\VeeamONE_13.0.0.5457_20250723.iso', 'userName': 'vspc\\admin',
            'password': 'Password1'}, 'usePredownloadedIso': None, 'answerXml': '<?xml version="1.0"
            encoding="utf-8"?>\r\n<unattendedInstallationConfiguration bundle="Vo" mode="upgrade" version="1.0">\r\n
            <properties>\r\n\r\n    <!--License agreements-->\r\n    <property name="ACCEPT_EULA" value="1" />\r\n
            <property name="ACCEPT_LICENSING_POLICY" value="1" />\r\n    <property name="ACCEPT_THIRDPARTY_LICENSES"
            value="1" />\r\n    <property name="ACCEPT_REQUIRED_SOFTWARE" value="1" />\r\n\r\n    <!--License file-->\r\n
            <property name="VO_LICENSE_FILE" value="" />\r\n    <property name="VO_LICENSE_AUTOUPDATE" value="1" />\r\n\r\n
            <!--Service account-->\r\n    <property name="VO_SERVICE_USER" value="vspc\\administrator" />\r\n    <property
            name="VO_SERVICE_PASSWORD" value="Password1" hidden="1" />\r\n\r\n    <!--Database configuration-->\r\n
            <property name="VO_SQLSERVER_USERNAME" value="" />\r\n    <property name="VO_SQLSERVER_PASSWORD" value=""
            hidden="1"/>\r\n\r\n    <!--Ports configuration-->\r\n    <property name="VO_MONITORING_SERVICE_PORT"
            value="2714" />\r\n    <property name="VO_REPORTING_SERVICE_PORT" value="2742" />\r\n    <property
            name="VO_INTERNAL_WEB_API_PORT" value="2741"  />\r\n    <!--Certificate configuration-->\r\n    <property
            name="VO_CERTIFICATE_THUMBPRINT" value="" />\r\n\r\n    <!--Server connection-->\r\n    <property
            name="VO_CONNECTION_SERVER_NAME" value="" />\r\n    <property name="VO_CONNECTION_WEB_API_PORT" value="" />\r\n
            <property name="VO_CONNECTION_USER" value="" />\r\n    <property name="VO_CONNECTION_PASSWORD" value=""
            hidden="1" />\r\n\r\n', 'allowAutoReboot': True, 'stopAllActivities': None, 'useManagementAgentCredentials':
            None, 'adminCredentials': {'username': 'vspc\\administrator', 'password': 'Password1'}}, 'schedule':
            {'dateTime': '2025-08-03T11:52:23.637Z'}}

    Attributes:
        configuration (VOneDeploymentConfiguration): Deployment configuration.
            > If the `distribution` and `usePredownloadedIso` properties have the `null` value, the most recent version of
            Veeam ONE will be downloaded automatically.
             Example: {'distribution': {'filePath':
            '\\\\tech.local\\tech\\VSPC\\VBR\\13\\Butler\\VeeamONE_13.0.0.5457_20250723.iso', 'userName': 'vspc\\admin',
            'password': 'Password1'}, 'usePredownloadedIso': None, 'answerXml': '<?xml version="1.0"
            encoding="utf-8"?>\r\n<unattendedInstallationConfiguration bundle="Vo" mode="upgrade" version="1.0">\r\n
            <properties>\r\n\r\n    <!--License agreements-->\r\n    <property name="ACCEPT_EULA" value="1" />\r\n
            <property name="ACCEPT_LICENSING_POLICY" value="1" />\r\n    <property name="ACCEPT_THIRDPARTY_LICENSES"
            value="1" />\r\n    <property name="ACCEPT_REQUIRED_SOFTWARE" value="1" />\r\n\r\n    <!--License file-->\r\n
            <property name="VO_LICENSE_FILE" value="" />\r\n    <property name="VO_LICENSE_AUTOUPDATE" value="1" />\r\n\r\n
            <!--Service account-->\r\n    <property name="VO_SERVICE_USER" value="vspc\\administrator" />\r\n    <property
            name="VO_SERVICE_PASSWORD" value="Password1" hidden="1" />\r\n\r\n    <!--Database configuration-->\r\n
            <property name="VO_SQLSERVER_USERNAME" value="" />\r\n    <property name="VO_SQLSERVER_PASSWORD" value=""
            hidden="1"/>\r\n\r\n    <!--Ports configuration-->\r\n    <property name="VO_MONITORING_SERVICE_PORT"
            value="2714" />\r\n    <property name="VO_REPORTING_SERVICE_PORT" value="2742" />\r\n    <property
            name="VO_INTERNAL_WEB_API_PORT" value="2741"  />\r\n    <!--Certificate configuration-->\r\n    <property
            name="VO_CERTIFICATE_THUMBPRINT" value="" />\r\n\r\n    <!--Server connection-->\r\n    <property
            name="VO_CONNECTION_SERVER_NAME" value="" />\r\n    <property name="VO_CONNECTION_WEB_API_PORT" value="" />\r\n
            <property name="VO_CONNECTION_USER" value="" />\r\n    <property name="VO_CONNECTION_PASSWORD" value=""
            hidden="1" />\r\n\r\n', 'allowAutoReboot': True, 'stopAllActivities': None, 'useManagementAgentCredentials':
            None, 'adminCredentials': {'username': 'vspc\\administrator', 'password': 'Password1'}}.
        schedule (DeploySchedule):
    """

    configuration: VOneDeploymentConfiguration
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
        from ..models.v_one_deployment_configuration import VOneDeploymentConfiguration

        d = dict(src_dict)
        configuration = VOneDeploymentConfiguration.from_dict(d.pop("configuration"))

        schedule = DeploySchedule.from_dict(d.pop("schedule"))

        v_one_scheduled_deployment_configuration = cls(
            configuration=configuration,
            schedule=schedule,
        )

        v_one_scheduled_deployment_configuration.additional_properties = d
        return v_one_scheduled_deployment_configuration

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
