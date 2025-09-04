from enum import Enum


class BackupProxyType(str, Enum):
    CDP = "CDP"
    FILE = "File"
    HYPERV = "HyperV"
    HYPERVOFFHOST = "HyperVOffhost"
    UNKNOWN = "Unknown"
    VSPHERE = "vSphere"

    def __str__(self) -> str:
        return str(self.value)
