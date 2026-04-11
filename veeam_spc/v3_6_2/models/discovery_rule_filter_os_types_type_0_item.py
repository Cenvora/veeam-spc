from enum import Enum


class DiscoveryRuleFilterOsTypesType0Item(str, Enum):
    ALMALINUX = "AlmaLinux"
    AMAZONLINUX = "AmazonLinux"
    CENTOS = "CentOS"
    DEBIAN = "Debian"
    FEDORA = "Fedora"
    OPENSUSE = "OpenSUSE"
    ORACLELINUX = "OracleLinux"
    REDHAT = "RedHat"
    ROCKYLINUX = "RockyLinux"
    SLES = "SLES"
    UBUNTU = "Ubuntu"
    UNKNOWN = "Unknown"
    WINDOWSSERVER = "WindowsServer"
    WINDOWSWORKSTATION = "WindowsWorkstation"

    def __str__(self) -> str:
        return str(self.value)
