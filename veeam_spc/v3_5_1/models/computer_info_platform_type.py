from enum import Enum


class ComputerInfoPlatformType(str, Enum):
    AMAZON = "Amazon"
    AZURE = "Azure"
    GOOGLE = "Google"
    HYPERV = "HyperV"
    LINUX = "Linux"
    MAC = "Mac"
    OTHER = "Other"
    UNKNOWN = "Unknown"
    VSPHERE = "vSphere"
    WINDOWS = "Windows"

    def __str__(self) -> str:
        return str(self.value)
