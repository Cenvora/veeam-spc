from enum import Enum


class BackupServerBackupVmJobSubtype(str, Enum):
    HYPERV = "HyperV"
    UNKNOWN = "Unknown"
    VCD = "Vcd"
    VSPHERE = "VSphere"

    def __str__(self) -> str:
        return str(self.value)
