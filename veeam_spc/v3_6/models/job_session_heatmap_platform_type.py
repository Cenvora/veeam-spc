from enum import Enum


class JobSessionHeatmapPlatformType(str, Enum):
    AHV = "AHV"
    AWS = "Aws"
    AZURE = "Azure"
    GOOGLE = "Google"
    HYPERV = "HyperV"
    MICROSOFT365 = "Microsoft365"
    PHYSICAL = "Physical"
    PROXMOXVE = "ProxmoxVe"
    RHV = "RHV"
    SCALECOMPUTING = "ScaleComputing"
    UNKNOWN = "Unknown"
    VCD = "VCD"
    VSPHERE = "VSphere"

    def __str__(self) -> str:
        return str(self.value)
