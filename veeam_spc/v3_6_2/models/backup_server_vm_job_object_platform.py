from enum import Enum


class BackupServerVmJobObjectPlatform(str, Enum):
    HPEMORPHEUSVMESSENTIALS = "HpeMorpheusVmEssentials"
    HYPERV = "HyperV"
    NUTANIXAHV = "NutanixAhv"
    OVIRTKVM = "OVirtKvm"
    PROXMOXVE = "ProxmoxVe"
    SCALECOMPUTING = "ScaleComputing"
    UNKNOWN = "Unknown"
    VCD = "Vcd"
    VSPHERE = "vSphere"

    def __str__(self) -> str:
        return str(self.value)
