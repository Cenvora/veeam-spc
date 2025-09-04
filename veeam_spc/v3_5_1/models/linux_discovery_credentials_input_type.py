from enum import Enum


class LinuxDiscoveryCredentialsInputType(str, Enum):
    LINUXBASED = "LinuxBased"
    LINUXCERTIFICATE = "LinuxCertificate"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
