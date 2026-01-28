from enum import Enum


class ProtectedCloudDatabaseBackupBackupType(str, Enum):
    ARCHIVE = "Archive"
    BACKUP = "Backup"
    REPLICASNAPSHOT = "ReplicaSnapshot"
    SNAPSHOT = "Snapshot"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
