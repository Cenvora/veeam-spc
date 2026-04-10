from enum import Enum


class BackupAgentManagementMode(str, Enum):
    MANAGEDBYCONSOLE = "ManagedByConsole"
    MANAGEDBYVBR = "ManagedByVBR"
    UNKNOWN = "Unknown"
    UNMANAGED = "UnManaged"

    def __str__(self) -> str:
        return str(self.value)
