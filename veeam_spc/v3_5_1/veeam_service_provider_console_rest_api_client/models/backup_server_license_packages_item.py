from enum import Enum


class BackupServerLicensePackagesItem(str, Enum):
    BACKUP = "Backup"
    ESSENTIALS = "Essentials"
    NONE = "None"
    ONE = "ONE"
    ORCHESTRATOR = "Orchestrator"
    STARTER = "Starter"
    SUITE = "Suite"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
