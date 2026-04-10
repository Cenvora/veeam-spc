from enum import Enum


class CloudBackupType(str, Enum):
    AHV = "AHV"
    AMAZON = "Amazon"
    AZURE = "Azure"
    GOOGLE = "Google"
    HYPERV = "HyperV"
    LINUX = "Linux"
    MAC = "Mac"
    NAS = "NAS"
    PROXMOXVE = "ProxmoxVe"
    RHV = "RHV"
    SCALECOMPUTING = "ScaleComputing"
    TAPE = "Tape"
    UNKNOWN = "Unknown"
    VCD = "VCD"
    VSPHERE = "VSphere"
    WINDOWS = "Windows"

    def __str__(self) -> str:
        return str(self.value)
