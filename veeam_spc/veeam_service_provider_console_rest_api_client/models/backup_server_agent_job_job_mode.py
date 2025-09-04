from enum import Enum


class BackupServerAgentJobJobMode(str, Enum):
    MANAGEDBYAGENT = "ManagedByAgent"
    MANAGEDBYBACKUPSERVER = "ManagedByBackupServer"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
