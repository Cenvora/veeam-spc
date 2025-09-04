from enum import Enum


class WindowsApplicationAwareProcessingSettingsTransactionLogProcessingMode(str, Enum):
    PERFORMCOPYONLY = "PerformCopyOnly"
    PROCESSTRANSACTIONLOGSWITHJOB = "ProcessTransactionLogsWithJob"

    def __str__(self) -> str:
        return str(self.value)
