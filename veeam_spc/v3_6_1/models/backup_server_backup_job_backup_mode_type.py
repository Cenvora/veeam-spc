from enum import Enum


class BackupServerBackupJobBackupModeType(str, Enum):
    FULL = "Full"
    INCREMENTAL = "Incremental"
    REVERSEINCREMENTAL = "ReverseIncremental"
    TRANSFORM = "Transform"
    TRANSFORMFOREVERINCREMENTAL = "TransformForeverIncremental"

    def __str__(self) -> str:
        return str(self.value)
