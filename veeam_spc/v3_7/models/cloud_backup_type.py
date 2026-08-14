from enum import Enum


class CloudBackupType(str, Enum):
    AHV = "AHV"
    AMAZON = "Amazon"
    AZURE = "Azure"
    GOOGLE = "Google"
    HPEMORPHEUSVMESSENTIALS = "HpeMorpheusVmEssentials"
    HYPERV = "HyperV"
    KUBEVIRT = "KubeVirt"
    LINUX = "Linux"
    MAC = "Mac"
    NAS = "NAS"
    PROXMOXVE = "ProxmoxVe"
    RHV = "RHV"
    SANGFORASV = "SangforAsv"
    SCALECOMPUTING = "ScaleComputing"
    TAPE = "Tape"
    UNKNOWN = "Unknown"
    VCD = "VCD"
    VSPHERE = "VSphere"
    WINDOWS = "Windows"
    XCP_NG = "XCP_ng"

    def __str__(self) -> str:
        return str(self.value)
