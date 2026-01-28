from enum import Enum


class JobSessionHeatmapJobType(str, Enum):
    ARCHIVE = "Archive"
    BACKUP = "Backup"
    BACKUPCOPY = "BackupCopy"
    BACKUPTOTAPE = "BackupToTape"
    COPY = "Copy"
    FFILETOTAPE = "FfileToTape"
    REMOTESNAPSHOT = "RemoteSnapshot"
    REPLICATION = "Replication"
    SNAPSHOT = "Snapshot"
    SUREBACKUP = "SureBackup"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
