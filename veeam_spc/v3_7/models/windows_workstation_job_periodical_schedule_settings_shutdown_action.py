from enum import Enum


class WindowsWorkstationJobPeriodicalScheduleSettingsShutdownAction(str, Enum):
    BACKUPONCEPOWEREDON = "BackupOncePoweredOn"
    SKIPBACKUP = "SkipBackup"

    def __str__(self) -> str:
        return str(self.value)
