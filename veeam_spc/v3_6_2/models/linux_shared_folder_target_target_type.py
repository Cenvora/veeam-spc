from enum import Enum


class LinuxSharedFolderTargetTargetType(str, Enum):
    NFS = "NFS"
    SMB = "SMB"

    def __str__(self) -> str:
        return str(self.value)
