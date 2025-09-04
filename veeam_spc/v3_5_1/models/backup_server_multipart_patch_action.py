from enum import Enum


class BackupServerMultipartPatchAction(str, Enum):
    EXECUTEFILE = "ExecuteFile"
    REPLACEFILESANDRESTART = "ReplaceFilesAndRestart"

    def __str__(self) -> str:
        return str(self.value)
