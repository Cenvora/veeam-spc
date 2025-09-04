from enum import Enum


class WindowsPolicyPeriodicallyLogBackupSettingsBackupRetentionMode(str, Enum):
    KEEPLASTDAYS = "KeepLastDays"
    UNTILBACKUPISDELETED = "UntilBackupIsDeleted"

    def __str__(self) -> str:
        return str(self.value)
