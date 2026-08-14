from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.deploy_schedule import DeploySchedule
    from ..models.vbr_deployment_configuration_with_credentials import VbrDeploymentConfigurationWithCredentials


T = TypeVar("T", bound="VbrScheduledDeploymentConfigurationWithCredentials")


@_attrs_define
class VbrScheduledDeploymentConfigurationWithCredentials:
    r"""
    Example:
        {'configuration': {'configuration': {'distribution': {'filePath':
            '\\\\tech.local\\tech\\VSPC\\VBR\\13\\Butler\\VeeamBackup&Replication_13.iso', 'userName': 'tech\\svc-datam',
            'password': 'n_59=r2wc%k8Rx.X'}, 'usePredownloadedIso': False, 'answerXml': '<?xml version="1.0"
            encoding="utf-8"?>\r\n<unattendedInstallationConfiguration bundle="VBR" mode="install">\r\n
            <properties>\r\n\r\n    <!--License agreements-->\r\n    <property name="ACCEPT_EULA" value="1" />\r\n
            <property name="ACCEPT_LICENSING_POLICY" value="1" />\r\n    <property name="ACCEPT_THIRDPARTY_LICENSES"
            value="1" />\r\n    <property name="ACCEPT_REQUIRED_SOFTWARE" value="1" />\r\n\r\n    <!--License file-->\r\n
            <property name="VBR_LICENSE_FILE" value="" />\r\n    <property name="VBR_LICENSE_AUTOUPDATE" value="1"
            />\r\n\r\n    <!--Service account-->\r\n    <property name="VBR_SERVICE_USER" value="vspc1\\administrator"
            />\r\n    <property name="VBR_SERVICE_PASSWORD" value="Password1" hidden="1" />\r\n\r\n    <!--Database
            configuration-->\r\n    <property name="VBR_SQLSERVER_INSTALL" value="0" />\r\n    <property
            name="VBR_SQLSERVER_ENGINE" value="1" />\r\n    <property name="VBR_SQLSERVER_SERVER" value="localhost" />\r\n
            <property name="VBR_SQLSERVER_DATABASE" value="VeeamBackup" />\r\n    <property
            name="VBR_SQLSERVER_AUTHENTICATION" value="1" />\r\n    <property name="VBR_SQLSERVER_USERNAME" value="postgres"
            />\r\n    <property name="VBR_SQLSERVER_PASSWORD" value="Password1" hidden="1"/>\r\n\r\n    <!--Ports
            configuration-->\r\n    <property name="VBRC_SERVICE_PORT" value="9393" />\r\n    <property
            name="VBR_SERVICE_PORT" value="9392" />\r\n    <property name="VBR_SECURE_CONNECTIONS_PORT" value="9401" />\r\n
            <property name="VBR_RESTSERVICE_PORT" value="9419" />\r\n\r\n    <!--Data locations-->\r\n    <property
            name="INSTALLDIR" value="C:\\Program Files\\Veeam\\Backup and Replication" />\r\n    <property
            name="VM_CATALOGPATH" value="C:\\VBRCatalog" />\r\n    <property name="VBR_IRCACHE"
            value="C:\\ProgramData\\Veeam\\Backup\\IRCache" />\r\n\r\n    <!--Automatic update settings-->\r\n    <property
            name="VBR_CHECK_UPDATES" value="1" />\r\n\r\n    <!--Plug-ins for Veeam Backup & Replication-->\r\n    <property
            name="AHV_INSTALL" value="0" />\r\n    <property name="RHV_INSTALL" value="0" />\r\n    <property
            name="AWS_INSTALL" value="0" />\r\n    <property name="AZURE_INSTALL" value="0" />\r\n    <property
            name="GCP_INSTALL" value="0" />\r\n    <property name="KASTEN_INSTALL" value="0" />\r\n\r\n
            </properties>\r\n</unattendedInstallationConfiguration>', 'allowAutoReboot': True, 'stopAllActivities': False,
            'useManagementAgentCredentials': False, 'adminCredentials': {'username': 'vspc1\\administrator', 'password':
            'Password1'}}, 'licenseSettings': {'licenseFileContent': 'BADANBgkqhkiG9w0BAQEFAASCAmEwggJdAgEAAoGBAIPK6bojg0Tj/
            GcvQvg5iTFpmGbAdAFXRmOE4L5gDiYdTIPSMMJnGDITqF33lTX6nkVA5EQQy14xHziMvONEmHkIsNwudIthody3H07aiKp+fakIwlCAsFCC3TnSH
            Buc1+Xp0r8L9ILi9UNWmss/XdsXiaPZd03daAR2JLUzXp3zAgMBAAECgYB6sez4utkZyLqSAaDyYPZFh0430tHs8ah5PBrTga+KclpqmsOEKOCQt
            lZX7Qf/seupA6m/aHc8oLS1O+kaGCFtpwsFSnin/7f8vXXlDpFSZYfWO+1u7W0ub50E9zmSH/Uup4QFPQm20Vf45Frq1KTpJfkywMKf5jbNwaEcE
            mFvYQJBAONHojOa1sAijDMUqdq4sZdIhvnz9EdCalzNGO3GCWV0ptwLGh7V4zP0heQnl1aaz/Tt9QJ7RlOUZomNIc/0siMCQQCUclNptWWp72iG0
            QmwVEmvn9vs8nlunGbmBBeo++a/46T51qU2GQxRSSi1M8T8aXrxHwA8HFjd5T1PK17tBJnxAkEAtYfMlP0yU2oEovP5KppkNhoWvOPOE3CHtbGXH
            KsVbDR85bn0VfauLxw6KN46cVDbkpzRGfdOV4lrUKgp/ohKEwJAN62N1bdA83UlanObQ7TJkoLOFVh47WDiQ2HDkhExYkW7Ci5U9y577T0YdKZ/O
            wFBKJEtIF6tgkTKMxicWSABsQJBANKIj6wkNfnxn5EwniB1959xNS0PrpeaLVedEhW2HJKrBBzQKpfv0A3aGl1CwTAfld0lNiFJ7jMo1J6rlDHXw
            9QwggJeAgEAAoGBAJ5ghbXlirsjv5Fdn7BFruUfE1w48BPp0M3jUIQXsN3bB4nj5a5soCQjKVN80p9N5j+ns53Opd/7Zm6nBFhwJ+ahG2DkMvvN6
            ceS4gUQIJfQqcWJmJV8876I+MAr6WpA4yG2kBOntXw4kmB0dbNLsG5KRp96/Y30haSaJhicd27tAgMBAAECgYEAhOTZTdheoMlOZdv5sx/Fsdxxk
            mD0ksEPxLOJTE3Uy1SO7tWcVNAxUCFw++0xjxr+qUs/HJvZ9Cgvu4nJy6vQzhNPwA09Yjw7IDVE73/wKydmdbI9sW4vSxpAHzP3khahqMCeAMjfo
            Y1Ji/G0tiFtgUGY4cqhoM3eMGVyTfUroMECQQDLwmxU7vncEirPyRUj7S21ns9EIeKrgHChMk+wwdX3XBABCji5IKPNMheMCuOjzxFMLZxZQSNWB
            uRg57I9fdn7AkEAxvt2eRTcqHz7gNuKYP4bam9ODAVkVOkYFXSv2PjsohI1FALVBAffu7E0mJFbbs8aL1vO5wbr2bbYVuApjr+uNwJBAMgI6Dd9o
            PgnMbZpz4JEr3I1JX/a0F/UKT5nWQrLUNaVn/SVZ1h/ra+d9LX8Xr0LZQznXi3Vn+4tt/lWnYp2yg8CQHMTzyqrhAn1bkbRsS/zBcwCXzLYk3P/8
            qvF9kUXgVMiEIxoLuXL3/reuzpZJnXpVI17HSfDevdIpclojuA9vvUCQQCcxDFk/oAFnwIND7Xy5Jy0fzCCzvWW05mVCzYAnj2rKIw6y+q55jE6h
            ExG1Z8Pfn36MS/cw1GmNlvKeq9hG+8b=', 'licenseUid': None, 'licenseSource': 'LicenseFileContent'}, 'credentials':
            {'tenantName': 'alphaadmin', 'tenantPassword': 'Password1'}}, 'schedule': {'dateTime':
            '2025-07-23T19:55:26.3617936-05:00'}}

    Attributes:
        configuration (VbrDeploymentConfigurationWithCredentials):  Example: {'configuration': {'distribution':
            {'filePath': '\\\\tech.local\\tech\\VSPC\\VBR\\13\\Butler\\VeeamBackup&Replication_13.iso', 'userName':
            'tech\\svc-datam', 'password': 'n_59=r2wc%k8Rx.X'}, 'usePredownloadedIso': False, 'answerXml': '<?xml
            version="1.0" encoding="utf-8"?>\r\n<unattendedInstallationConfiguration bundle="VBR" mode="install">\r\n
            <properties>\r\n\r\n    <!--License agreements-->\r\n    <property name="ACCEPT_EULA" value="1" />\r\n
            <property name="ACCEPT_LICENSING_POLICY" value="1" />\r\n    <property name="ACCEPT_THIRDPARTY_LICENSES"
            value="1" />\r\n    <property name="ACCEPT_REQUIRED_SOFTWARE" value="1" />\r\n\r\n    <!--License file-->\r\n
            <property name="VBR_LICENSE_FILE" value="" />\r\n    <property name="VBR_LICENSE_AUTOUPDATE" value="1"
            />\r\n\r\n    <!--Service account-->\r\n    <property name="VBR_SERVICE_USER" value="vspc1\\administrator"
            />\r\n    <property name="VBR_SERVICE_PASSWORD" value="Password1" hidden="1" />\r\n\r\n    <!--Database
            configuration-->\r\n    <property name="VBR_SQLSERVER_INSTALL" value="0" />\r\n    <property
            name="VBR_SQLSERVER_ENGINE" value="1" />\r\n    <property name="VBR_SQLSERVER_SERVER" value="localhost" />\r\n
            <property name="VBR_SQLSERVER_DATABASE" value="VeeamBackup" />\r\n    <property
            name="VBR_SQLSERVER_AUTHENTICATION" value="1" />\r\n    <property name="VBR_SQLSERVER_USERNAME" value="postgres"
            />\r\n    <property name="VBR_SQLSERVER_PASSWORD" value="Password1" hidden="1"/>\r\n\r\n    <!--Ports
            configuration-->\r\n    <property name="VBRC_SERVICE_PORT" value="9393" />\r\n    <property
            name="VBR_SERVICE_PORT" value="9392" />\r\n    <property name="VBR_SECURE_CONNECTIONS_PORT" value="9401" />\r\n
            <property name="VBR_RESTSERVICE_PORT" value="9419" />\r\n\r\n    <!--Data locations-->\r\n    <property
            name="INSTALLDIR" value="C:\\Program Files\\Veeam\\Backup and Replication" />\r\n    <property
            name="VM_CATALOGPATH" value="C:\\VBRCatalog" />\r\n    <property name="VBR_IRCACHE"
            value="C:\\ProgramData\\Veeam\\Backup\\IRCache" />\r\n\r\n    <!--Automatic update settings-->\r\n    <property
            name="VBR_CHECK_UPDATES" value="1" />\r\n\r\n    <!--Plug-ins for Veeam Backup & Replication-->\r\n    <property
            name="AHV_INSTALL" value="0" />\r\n    <property name="RHV_INSTALL" value="0" />\r\n    <property
            name="AWS_INSTALL" value="0" />\r\n    <property name="AZURE_INSTALL" value="0" />\r\n    <property
            name="GCP_INSTALL" value="0" />\r\n    <property name="KASTEN_INSTALL" value="0" />\r\n\r\n
            </properties>\r\n</unattendedInstallationConfiguration>', 'allowAutoReboot': True, 'stopAllActivities': False,
            'useManagementAgentCredentials': False, 'adminCredentials': {'username': 'vspc1\\administrator', 'password':
            'Password1'}}, 'licenseSettings': {'licenseFileContent': 'BADANBgkqhkiG9w0BAQEFAASCAmEwggJdAgEAAoGBAIPK6bojg0Tj/
            GcvQvg5iTFpmGbAdAFXRmOE4L5gDiYdTIPSMMJnGDITqF33lTX6nkVA5EQQy14xHziMvONEmHkIsNwudIthody3H07aiKp+fakIwlCAsFCC3TnSH
            Buc1+Xp0r8L9ILi9UNWmss/XdsXiaPZd03daAR2JLUzXp3zAgMBAAECgYB6sez4utkZyLqSAaDyYPZFh0430tHs8ah5PBrTga+KclpqmsOEKOCQt
            lZX7Qf/seupA6m/aHc8oLS1O+kaGCFtpwsFSnin/7f8vXXlDpFSZYfWO+1u7W0ub50E9zmSH/Uup4QFPQm20Vf45Frq1KTpJfkywMKf5jbNwaEcE
            mFvYQJBAONHojOa1sAijDMUqdq4sZdIhvnz9EdCalzNGO3GCWV0ptwLGh7V4zP0heQnl1aaz/Tt9QJ7RlOUZomNIc/0siMCQQCUclNptWWp72iG0
            QmwVEmvn9vs8nlunGbmBBeo++a/46T51qU2GQxRSSi1M8T8aXrxHwA8HFjd5T1PK17tBJnxAkEAtYfMlP0yU2oEovP5KppkNhoWvOPOE3CHtbGXH
            KsVbDR85bn0VfauLxw6KN46cVDbkpzRGfdOV4lrUKgp/ohKEwJAN62N1bdA83UlanObQ7TJkoLOFVh47WDiQ2HDkhExYkW7Ci5U9y577T0YdKZ/O
            wFBKJEtIF6tgkTKMxicWSABsQJBANKIj6wkNfnxn5EwniB1959xNS0PrpeaLVedEhW2HJKrBBzQKpfv0A3aGl1CwTAfld0lNiFJ7jMo1J6rlDHXw
            9QwggJeAgEAAoGBAJ5ghbXlirsjv5Fdn7BFruUfE1w48BPp0M3jUIQXsN3bB4nj5a5soCQjKVN80p9N5j+ns53Opd/7Zm6nBFhwJ+ahG2DkMvvN6
            ceS4gUQIJfQqcWJmJV8876I+MAr6WpA4yG2kBOntXw4kmB0dbNLsG5KRp96/Y30haSaJhicd27tAgMBAAECgYEAhOTZTdheoMlOZdv5sx/Fsdxxk
            mD0ksEPxLOJTE3Uy1SO7tWcVNAxUCFw++0xjxr+qUs/HJvZ9Cgvu4nJy6vQzhNPwA09Yjw7IDVE73/wKydmdbI9sW4vSxpAHzP3khahqMCeAMjfo
            Y1Ji/G0tiFtgUGY4cqhoM3eMGVyTfUroMECQQDLwmxU7vncEirPyRUj7S21ns9EIeKrgHChMk+wwdX3XBABCji5IKPNMheMCuOjzxFMLZxZQSNWB
            uRg57I9fdn7AkEAxvt2eRTcqHz7gNuKYP4bam9ODAVkVOkYFXSv2PjsohI1FALVBAffu7E0mJFbbs8aL1vO5wbr2bbYVuApjr+uNwJBAMgI6Dd9o
            PgnMbZpz4JEr3I1JX/a0F/UKT5nWQrLUNaVn/SVZ1h/ra+d9LX8Xr0LZQznXi3Vn+4tt/lWnYp2yg8CQHMTzyqrhAn1bkbRsS/zBcwCXzLYk3P/8
            qvF9kUXgVMiEIxoLuXL3/reuzpZJnXpVI17HSfDevdIpclojuA9vvUCQQCcxDFk/oAFnwIND7Xy5Jy0fzCCzvWW05mVCzYAnj2rKIw6y+q55jE6h
            ExG1Z8Pfn36MS/cw1GmNlvKeq9hG+8b=', 'licenseUid': None, 'licenseSource': 'LicenseFileContent'}, 'credentials':
            {'tenantName': 'alphaadmin', 'tenantPassword': 'Password1'}}.
        schedule (DeploySchedule):
    """

    configuration: VbrDeploymentConfigurationWithCredentials
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
        from ..models.vbr_deployment_configuration_with_credentials import VbrDeploymentConfigurationWithCredentials

        d = dict(src_dict)
        configuration = VbrDeploymentConfigurationWithCredentials.from_dict(d.pop("configuration"))

        schedule = DeploySchedule.from_dict(d.pop("schedule"))

        vbr_scheduled_deployment_configuration_with_credentials = cls(
            configuration=configuration,
            schedule=schedule,
        )

        vbr_scheduled_deployment_configuration_with_credentials.additional_properties = d
        return vbr_scheduled_deployment_configuration_with_credentials

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
