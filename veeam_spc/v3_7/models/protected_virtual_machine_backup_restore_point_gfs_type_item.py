from enum import Enum


class ProtectedVirtualMachineBackupRestorePointGfsTypeItem(str, Enum):
    MONTHLY = "Monthly,"
    QUARTERLY = "Quarterly,"
    WEEKLY = "Weekly,"
    YEARLY = "Yearly"

    def __str__(self) -> str:
        return str(self.value)
