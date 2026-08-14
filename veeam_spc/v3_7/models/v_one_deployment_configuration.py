from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.management_agent_credentials import ManagementAgentCredentials
    from ..models.v_one_deployment_distribution_source import VOneDeploymentDistributionSource


T = TypeVar("T", bound="VOneDeploymentConfiguration")


@_attrs_define
class VOneDeploymentConfiguration:
    r"""Deployment configuration.
    > If the `distribution` and `usePredownloadedIso` properties have the `null` value, the most recent version of Veeam
    ONE will be downloaded automatically.

        Example:
            {'distribution': {'filePath': '\\\\tech.local\\tech\\VSPC\\VBR\\13\\Butler\\VeeamONE_13.0.0.5457_20250723.iso',
                'userName': 'vspc\\admin', 'password': 'Password1'}, 'usePredownloadedIso': None, 'answerXml': '<?xml
                version="1.0" encoding="utf-8"?>\r\n<unattendedInstallationConfiguration bundle="Vo" mode="upgrade"
                version="1.0">\r\n  <properties>\r\n\r\n    <!--License agreements-->\r\n    <property name="ACCEPT_EULA"
                value="1" />\r\n    <property name="ACCEPT_LICENSING_POLICY" value="1" />\r\n    <property
                name="ACCEPT_THIRDPARTY_LICENSES" value="1" />\r\n    <property name="ACCEPT_REQUIRED_SOFTWARE" value="1"
                />\r\n\r\n    <!--License file-->\r\n    <property name="VO_LICENSE_FILE" value="" />\r\n    <property
                name="VO_LICENSE_AUTOUPDATE" value="1" />\r\n\r\n    <!--Service account-->\r\n    <property
                name="VO_SERVICE_USER" value="vspc\\administrator" />\r\n    <property name="VO_SERVICE_PASSWORD"
                value="Password1" hidden="1" />\r\n\r\n    <!--Database configuration-->\r\n    <property
                name="VO_SQLSERVER_USERNAME" value="" />\r\n    <property name="VO_SQLSERVER_PASSWORD" value=""
                hidden="1"/>\r\n\r\n    <!--Ports configuration-->\r\n    <property name="VO_MONITORING_SERVICE_PORT"
                value="2714" />\r\n    <property name="VO_REPORTING_SERVICE_PORT" value="2742" />\r\n    <property
                name="VO_INTERNAL_WEB_API_PORT" value="2741"  />\r\n    <!--Certificate configuration-->\r\n    <property
                name="VO_CERTIFICATE_THUMBPRINT" value="" />\r\n\r\n    <!--Server connection-->\r\n    <property
                name="VO_CONNECTION_SERVER_NAME" value="" />\r\n    <property name="VO_CONNECTION_WEB_API_PORT" value="" />\r\n
                <property name="VO_CONNECTION_USER" value="" />\r\n    <property name="VO_CONNECTION_PASSWORD" value=""
                hidden="1" />\r\n\r\n', 'allowAutoReboot': True, 'stopAllActivities': None, 'useManagementAgentCredentials':
                None, 'adminCredentials': {'username': 'vspc\\administrator', 'password': 'Password1'}}

        Attributes:
            answer_xml (str): XML string containing installation parameters.
            distribution (VOneDeploymentDistributionSource | Unset):
            use_predownloaded_iso (bool | Unset): Indicates whether the predownloaded Veeam ONE setup file is used for
                installation.
                > Provided value has higher priority than the `distribution` property value.
            allow_auto_reboot (bool | Unset): Indicates whether a server must be automatically rebooted after the
                installation is complete.
            stop_all_activities (bool | Unset): Indicates whether all other tasks must be stopped during installation. Can
                be enabled only for update installation.
            use_management_agent_credentials (bool | Unset): Indicates whether management agent credentials must be used as
                service account credentials.
                > Provided value has higher priority than the `adminCredentials` property value.
            admin_credentials (ManagementAgentCredentials | Unset):  Example: {'username': 'hv1\\dma', 'password':
                'Password1'}.
    """

    answer_xml: str
    distribution: VOneDeploymentDistributionSource | Unset = UNSET
    use_predownloaded_iso: bool | Unset = UNSET
    allow_auto_reboot: bool | Unset = UNSET
    stop_all_activities: bool | Unset = UNSET
    use_management_agent_credentials: bool | Unset = UNSET
    admin_credentials: ManagementAgentCredentials | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        answer_xml = self.answer_xml

        distribution: dict[str, Any] | Unset = UNSET
        if not isinstance(self.distribution, Unset):
            distribution = self.distribution.to_dict()

        use_predownloaded_iso = self.use_predownloaded_iso

        allow_auto_reboot = self.allow_auto_reboot

        stop_all_activities = self.stop_all_activities

        use_management_agent_credentials = self.use_management_agent_credentials

        admin_credentials: dict[str, Any] | Unset = UNSET
        if not isinstance(self.admin_credentials, Unset):
            admin_credentials = self.admin_credentials.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "answerXml": answer_xml,
            }
        )
        if distribution is not UNSET:
            field_dict["distribution"] = distribution
        if use_predownloaded_iso is not UNSET:
            field_dict["usePredownloadedIso"] = use_predownloaded_iso
        if allow_auto_reboot is not UNSET:
            field_dict["allowAutoReboot"] = allow_auto_reboot
        if stop_all_activities is not UNSET:
            field_dict["stopAllActivities"] = stop_all_activities
        if use_management_agent_credentials is not UNSET:
            field_dict["useManagementAgentCredentials"] = use_management_agent_credentials
        if admin_credentials is not UNSET:
            field_dict["adminCredentials"] = admin_credentials

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.management_agent_credentials import ManagementAgentCredentials
        from ..models.v_one_deployment_distribution_source import VOneDeploymentDistributionSource

        d = dict(src_dict)
        answer_xml = d.pop("answerXml")

        _distribution = d.pop("distribution", UNSET)
        distribution: VOneDeploymentDistributionSource | Unset
        if isinstance(_distribution, Unset):
            distribution = UNSET
        else:
            distribution = VOneDeploymentDistributionSource.from_dict(_distribution)

        use_predownloaded_iso = d.pop("usePredownloadedIso", UNSET)

        allow_auto_reboot = d.pop("allowAutoReboot", UNSET)

        stop_all_activities = d.pop("stopAllActivities", UNSET)

        use_management_agent_credentials = d.pop("useManagementAgentCredentials", UNSET)

        _admin_credentials = d.pop("adminCredentials", UNSET)
        admin_credentials: ManagementAgentCredentials | Unset
        if isinstance(_admin_credentials, Unset):
            admin_credentials = UNSET
        else:
            admin_credentials = ManagementAgentCredentials.from_dict(_admin_credentials)

        v_one_deployment_configuration = cls(
            answer_xml=answer_xml,
            distribution=distribution,
            use_predownloaded_iso=use_predownloaded_iso,
            allow_auto_reboot=allow_auto_reboot,
            stop_all_activities=stop_all_activities,
            use_management_agent_credentials=use_management_agent_credentials,
            admin_credentials=admin_credentials,
        )

        v_one_deployment_configuration.additional_properties = d
        return v_one_deployment_configuration

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
