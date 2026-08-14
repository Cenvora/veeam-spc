from enum import Enum


class BackupServerBackupVmJobSubtype(str, Enum):
    HPEMORPHEUSVMESSENTIALS = "HpeMorpheusVmEssentials"
    HYPERV = "HyperV"
    KUBEVIRT = "KubeVirt"
    NUTANIXAHV = "NutanixAhv"
    OVIRTKVM = "OVirtKvm"
    PROXMOXVE = "ProxmoxVe"
    SANGFORASV = "SangforAsv"
    SCALECOMPUTING = "ScaleComputing"
    UNKNOWN = "Unknown"
    VCD = "Vcd"
    VSPHERE = "VSphere"
    XCP_NG = "XCP_ng"

    def __str__(self) -> str:
        return str(self.value)
