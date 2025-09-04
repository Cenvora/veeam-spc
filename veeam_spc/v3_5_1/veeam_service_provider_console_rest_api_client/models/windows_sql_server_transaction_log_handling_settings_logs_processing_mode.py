from enum import Enum


class WindowsSqlServerTransactionLogHandlingSettingsLogsProcessingMode(str, Enum):
    BACKUPLOGSPERIODICALLY = "BackupLogsPeriodically"
    DONOTTRUNCATELOGS = "DoNotTruncateLogs"
    TRUNCATELOGS = "TruncateLogs"

    def __str__(self) -> str:
        return str(self.value)
