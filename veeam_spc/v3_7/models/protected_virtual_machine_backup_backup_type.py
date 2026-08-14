from enum import Enum


class ProtectedVirtualMachineBackupBackupType(str, Enum):
    BACKUP = "Backup"
    BACKUPCOPY = "BackupCopy"
    BACKUPTOTAPE = "BackupToTape"
    ORPHANED = "Orphaned"
    REPLICATION = "Replication"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
