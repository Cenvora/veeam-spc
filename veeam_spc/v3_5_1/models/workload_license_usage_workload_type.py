from enum import Enum


class WorkloadLicenseUsageWorkloadType(str, Enum):
    CC_SERVER_BACKUP = "CC_Server_Backup"
    CC_VM_BACKUP = "CC_VM_Backup"
    CC_VM_REPLICA = "CC_VM_Replica"
    CC_WORKSTATION_BACKUP = "CC_Workstation_Backup"
    DYNAMIC = "Dynamic"
    UNKNOWN = "Unknown"
    VAC_SERVER_AGENT = "VAC_Server_Agent"
    VAC_WORKSTATION_AGENT = "VAC_Workstation_Agent"
    VB365_USER = "VB365_User"
    VBR_APPLICATION_PLUGINS = "VBR_Application_Plugins"
    VBR_CLOUD_DATABASE = "VBR_Cloud_Database"
    VBR_CLOUD_FILE_SHARE = "VBR_Cloud_File_Share"
    VBR_CLOUD_VM = "VBR_Cloud_VM"
    VBR_NAS_BACKUP = "VBR_NAS_Backup"
    VBR_NAS_SERVER = "VBR_NAS_Server"
    VBR_SERVER_AGENT = "VBR_Server_Agent"
    VBR_TAPE_BACKUP = "VBR_Tape_Backup"
    VBR_TAPE_SERVER = "VBR_Tape_Server"
    VBR_VM = "VBR_VM"
    VBR_WORKSTATION_AGENT = "VBR_Workstation_Agent"
    VONE_CLOUD_DATABASE = "VONE_Cloud_Database"
    VONE_CLOUD_FILE_SHARE = "VONE_Cloud_File_Share"
    VONE_CLOUD_VM = "VONE_Cloud_VM"
    VONE_NAS_BACKUP = "VONE_Nas_Backup"
    VONE_SERVER_AGENT = "VONE_Server_Agent"
    VONE_TAPE_BACKUP = "VONE_Tape_Backup"
    VONE_USER = "VONE_User"
    VONE_VM = "VONE_VM"
    VONE_WORKSTATION_AGENT = "VONE_Workstation_Agent"

    def __str__(self) -> str:
        return str(self.value)
