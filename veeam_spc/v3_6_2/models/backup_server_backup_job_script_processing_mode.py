from enum import Enum


class BackupServerBackupJobScriptProcessingMode(str, Enum):
    DISABLEEXEC = "disableExec"
    IGNOREEXECFAILURES = "ignoreExecFailures"
    REQUIRESUCCESS = "requireSuccess"

    def __str__(self) -> str:
        return str(self.value)
