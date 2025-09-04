from enum import Enum


class BackupServerCloudDirectorInventoryType(str, Enum):
    CLOUDDIRECTORSERVER = "CloudDirectorServer"
    DATASTORE = "Datastore"
    NETWORK = "Network"
    ORGANIZATION = "Organization"
    ORGANIZATIONVDC = "OrganizationVDC"
    STORAGEPOLICY = "StoragePolicy"
    UNKNOWN = "Unknown"
    VAPP = "vApp"
    VCENTER = "vCenter"
    VIRTUALMACHINE = "VirtualMachine"
    VMTEMPLATE = "VmTemplate"

    def __str__(self) -> str:
        return str(self.value)
