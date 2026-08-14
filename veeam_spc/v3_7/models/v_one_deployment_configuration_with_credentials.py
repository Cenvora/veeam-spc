from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.v_one_deployment_configuration import VOneDeploymentConfiguration
    from ..models.v_one_deployment_license_settings import VOneDeploymentLicenseSettings


T = TypeVar("T", bound="VOneDeploymentConfigurationWithCredentials")


@_attrs_define
class VOneDeploymentConfigurationWithCredentials:
    r"""
    Example:
        {'configuration': {'distribution': {'filePath':
            '\\\\tech.local\\tech\\VSPC\\VBR\\13\\Butler\\VeeamONE_13.0.0.5457_20250723.iso', 'userName': 'vspc\\admin',
            'password': 'Password1'}, 'usePredownloadedIso': None, 'answerXml': '<?xml version="1.0"
            encoding="utf-8"?>\r\n<unattendedInstallationConfiguration bundle="Vo" mode="install" version="1.0">\r\n
            <properties>\r\n\r\n    <!--License agreements-->\r\n    <property name="ACCEPT_EULA" value="1" />\r\n
            <property name="ACCEPT_LICENSING_POLICY" value="1" />\r\n    <property name="ACCEPT_THIRDPARTY_LICENSES"
            value="1" />\r\n    <property name="ACCEPT_REQUIRED_SOFTWARE" value="1" />\r\n\r\n    <!--License file-->\r\n
            <property name="VO_LICENSE_FILE" value="" />\r\n    <property name="VO_LICENSE_AUTOUPDATE" value="1" />\r\n\r\n
            <!--Standalone components-->\r\n    <property name="VO_SERVER_COMPONENT" value="1" />\r\n    <property
            name="VO_WEB_COMPONENT" value="1" />\r\n    <property name="VO_CLIENT_COMPONENT" value="1" />\r\n\r\n    <!--
            Service account-->\r\n    <property name="VO_SERVICE_USER" value="vspc\\administrator" />\r\n    <property
            name="VO_SERVICE_PASSWORD" value="Password1" hidden="1" />\r\n\r\n    <!--Database configuration-->\r\n
            <property name="VO_SQLSERVER_INSTALL" value="1" />\r\n    <property name="VO_SQLSERVER_SERVER"
            value="localhost\\VEEAMSQL2017" />\r\n    <property name="VO_SQLSERVER_DATABASE" value="VeeamONE" />\r\n
            <property name="VO_SQLSERVER_AUTHENTICATION" value="0" />\r\n    <property name="VO_SQLSERVER_USERNAME" value=""
            />\r\n    <property name="VO_SQLSERVER_PASSWORD" value="" hidden="1"/>\r\n\r\n    <!-- Reporting database
            configuration-->\r\n    <property name="VO_POSTGRESQL_INSTALL" value="1" />\r\n    <property
            name="VO_POSTGRESQL_SERVER" value="localhost" />\r\n    <property name="VO_POSTGRESQL_PORT" value="5432" />\r\n
            <property name="VO_POSTGRESQL_DATABASE" value="VeeamONEWarehouse" />\r\n    <property
            name="VO_POSTGRESQL_AUTHENTICATION" value="0" />\r\n    <property name="VO_POSTGRESQL_USERNAME" value="postgres"
            />\r\n    <property name="VO_POSTGRESQL_PASSWORD" value="" hidden="1"/>\r\n\r\n    <!--Data collection
            mode-->\r\n    <property name="VO_INSTALLATION_TYPE" value="2" />\r\n\r\n    <!--Ports configuration-->\r\n
            <property name="VO_MONITORING_SERVICE_PORT" value="2714" />\r\n    <property name="VO_REPORTING_SERVICE_PORT"
            value="2742" />\r\n    <property name="VO_CACHING_SERVICE_PORT" value="2743" />\r\n    <property
            name="VO_INTERNAL_WEB_API_PORT" value="2741"  />\r\n    <property name="VO_WEBSITE_PORT" value="1239" />\r\n
            <property name="VO_AGENT_SERVICE_PORT" value="2805" />\r\n\r\n    <!--Certificate configuration-->\r\n
            <property name="VO_CERTIFICATE_THUMBPRINT" value="" />\r\n\r\n    <!--Data locations-->\r\n    <property
            name="INSTALLDIR" value="C:\\Program Files\\Veeam\\Veeam ONE" />\r\n    <property name="VO_PERFCACHE"
            value="C:\\PerfCache" />\r\n\r\n    <!--Server connection-->\r\n    <property name="VO_CONNECTION_SERVER_NAME"
            value="" />\r\n    <property name="VO_CONNECTION_WEB_API_PORT" value="" />\r\n    <property
            name="VO_CONNECTION_USER" value="" />\r\n    <property name="VO_CONNECTION_PASSWORD" value="" hidden="1"
            />\r\n\r\n    <!--Setup settings-->\r\n    <property name="REBOOT_IF_REQUIRED" value="0" />\r\n    <property
            name="DONT_ADD_USER_TO_ADMINS" value="1" />\r\n\r\n  </properties>\r\n</unattendedInstallationConfiguration>',
            'allowAutoReboot': True, 'stopAllActivities': None, 'useManagementAgentCredentials': None, 'adminCredentials':
            {'username': 'vspc\\administrator', 'password': 'Password1'}}, 'licenseSettings': {'licenseFileContent': 'BADANB
            gkqhkiG9w0BAQEFAASCAmEwggJdAgEAAoGBAIPK6bojg0Tj/GcvQvg5iTFpmGbAdAFXRmOE4L5gDiYdTIPSMMJnGDITqF33lTX6nkVA5EQQy14xH
            ziMvONEmHkIsNwudIthody3H07aiKp+fakIwlCAsFCC3TnSHBuc1+Xp0r8L9ILi9UNWmss/XdsXiaPZd03daAR2JLUzXp3zAgMBAAECgYB6sez4u
            tkZyLqSAaDyYPZFh0430tHs8ah5PBrTga+KclpqmsOEKOCQtlZX7Qf/seupA6m/aHc8oLS1O+kaGCFtpwsFSnin/7f8vXXlDpFSZYfWO+1u7W0ub
            50E9zmSH/Uup4QFPQm20Vf45Frq1KTpJfkywMKf5jbNwaEcEmFvYQJBAONHojOa1sAijDMUqdq4sZdIhvnz9EdCalzNGO3GCWV0ptwLGh7V4zP0h
            eQnl1aaz/Tt9QJ7RlOUZomNIc/0siMCQQCUclNptWWp72iG0QmwVEmvn9vs8nlunGbmBBeo++a/46T51qU2GQxRSSi1M8T8aXrxHwA8HFjd5T1PK
            17tBJnxAkEAtYfMlP0yU2oEovP5KppkNhoWvOPOE3CHtbGXHKsVbDR85bn0VfauLxw6KN46cVDbkpzRGfdOV4lrUKgp/ohKEwJAN62N1bdA83Ula
            nObQ7TJkoLOFVh47WDiQ2HDkhExYkW7Ci5U9y577T0YdKZ/OwFBKJEtIF6tgkTKMxicWSABsQJBANKIj6wkNfnxn5EwniB1959xNS0PrpeaLVedE
            hW2HJKrBBzQKpfv0A3aGl1CwTAfld0lNiFJ7jMo1J6rlDHXw9QwggJeAgEAAoGBAJ5ghbXlirsjv5Fdn7BFruUfE1w48BPp0M3jUIQXsN3bB4nj5
            a5soCQjKVN80p9N5j+ns53Opd/7Zm6nBFhwJ+ahG2DkMvvN6ceS4gUQIJfQqcWJmJV8876I+MAr6WpA4yG2kBOntXw4kmB0dbNLsG5KRp96/Y30h
            aSaJhicd27tAgMBAAECgYEAhOTZTdheoMlOZdv5sx/FsdxxkmD0ksEPxLOJTE3Uy1SO7tWcVNAxUCFw++0xjxr+qUs/HJvZ9Cgvu4nJy6vQzhNPw
            A09Yjw7IDVE73/wKydmdbI9sW4vSxpAHzP3khahqMCeAMjfoY1Ji/G0tiFtgUGY4cqhoM3eMGVyTfUroMECQQDLwmxU7vncEirPyRUj7S21ns9EI
            eKrgHChMk+wwdX3XBABCji5IKPNMheMCuOjzxFMLZxZQSNWBuRg57I9fdn7AkEAxvt2eRTcqHz7gNuKYP4bam9ODAVkVOkYFXSv2PjsohI1FALVB
            Affu7E0mJFbbs8aL1vO5wbr2bbYVuApjr+uNwJBAMgI6Dd9oPgnMbZpz4JEr3I1JX/a0F/UKT5nWQrLUNaVn/SVZ1h/ra+d9LX8Xr0LZQznXi3Vn
            +4tt/lWnYp2yg8CQHMTzyqrhAn1bkbRsS/zBcwCXzLYk3P/8qvF9kUXgVMiEIxoLuXL3/reuzpZJnXpVI17HSfDevdIpclojuA9vvUCQQCcxDFk/
            oAFnwIND7Xy5Jy0fzCCzvWW05mVCzYAnj2rKIw6y+q55jE6hExG1Z8Pfn36MS/cw1GmNlvKeq9hG+8b=', 'licenseUid': None,
            'licenseSource': 'LicenseFileContent'}}

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
        license_settings (VOneDeploymentLicenseSettings):
    """

    configuration: VOneDeploymentConfiguration
    license_settings: VOneDeploymentLicenseSettings
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        configuration = self.configuration.to_dict()

        license_settings = self.license_settings.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "configuration": configuration,
                "licenseSettings": license_settings,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.v_one_deployment_configuration import VOneDeploymentConfiguration
        from ..models.v_one_deployment_license_settings import VOneDeploymentLicenseSettings

        d = dict(src_dict)
        configuration = VOneDeploymentConfiguration.from_dict(d.pop("configuration"))

        license_settings = VOneDeploymentLicenseSettings.from_dict(d.pop("licenseSettings"))

        v_one_deployment_configuration_with_credentials = cls(
            configuration=configuration,
            license_settings=license_settings,
        )

        v_one_deployment_configuration_with_credentials.additional_properties = d
        return v_one_deployment_configuration_with_credentials

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
