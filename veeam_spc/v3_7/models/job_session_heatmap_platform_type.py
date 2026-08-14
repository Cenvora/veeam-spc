from enum import Enum


class JobSessionHeatmapPlatformType(str, Enum):
    AHV = "AHV"
    AWS = "Aws"
    AZURE = "Azure"
    GOOGLE = "Google"
    HPEMORPHEUSVMESSENTIALS = "HpeMorpheusVmEssentials"
    HYPERV = "HyperV"
    KUBEVIRT = "KubeVirt"
    MICROSOFT365 = "Microsoft365"
    PHYSICAL = "Physical"
    PROXMOXVE = "ProxmoxVe"
    RHV = "RHV"
    SANGFORASV = "SangforAsv"
    SCALECOMPUTING = "ScaleComputing"
    UNKNOWN = "Unknown"
    VCD = "VCD"
    VSPHERE = "VSphere"
    XCP_NG = "XCP_ng"

    def __str__(self) -> str:
        return str(self.value)
