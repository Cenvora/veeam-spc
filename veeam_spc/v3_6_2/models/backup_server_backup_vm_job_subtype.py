from enum import Enum


class BackupServerBackupVmJobSubtype(str, Enum):
    HPEMORPHEUSVMESSENTIALS = "HpeMorpheusVmEssentials"
    HYPERV = "HyperV"
    NUTANIXAHV = "NutanixAhv"
    OVIRTKVM = "OVirtKvm"
    PROXMOXVE = "ProxmoxVe"
    SCALECOMPUTING = "ScaleComputing"
    UNKNOWN = "Unknown"
    VCD = "Vcd"
    VSPHERE = "VSphere"

    def __str__(self) -> str:
        return str(self.value)
