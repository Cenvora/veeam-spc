from enum import Enum


class BackupServerVmJobObjectPlatform(str, Enum):
    HYPERV = "HyperV"
    UNKNOWN = "Unknown"
    VCD = "Vcd"
    VSPHERE = "vSphere"

    def __str__(self) -> str:
        return str(self.value)
