from enum import Enum


class BackupServerCdpReplicationJobShortTermRetentionUnit(str, Enum):
    DAYS = "Days"
    HOURS = "Hours"
    MINUTES = "Minutes"
    SECONDS = "Seconds"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
