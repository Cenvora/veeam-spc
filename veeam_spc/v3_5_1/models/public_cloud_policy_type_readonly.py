from enum import Enum


class PublicCloudPolicyTypeReadonly(str, Enum):
    CLOUDNETWORK = "CloudNetwork"
    DATABASE = "Database"
    FILESHARE = "FileShare"
    UNKNOWN = "Unknown"
    VIRTUALMACHINE = "VirtualMachine"

    def __str__(self) -> str:
        return str(self.value)
