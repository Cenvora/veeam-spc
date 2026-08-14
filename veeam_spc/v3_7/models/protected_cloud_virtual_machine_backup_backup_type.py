from enum import Enum


class ProtectedCloudVirtualMachineBackupBackupType(str, Enum):
    BACKUP = "Backup"
    BACKUPCOPY = "BackupCopy"
    BACKUPTOTAPE = "BackupToTape"
    PUBLICCLOUDARCHIVE = "PublicCloudArchive"
    REPLICASNAPSHOT = "ReplicaSnapshot"
    SNAPSHOT = "Snapshot"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
