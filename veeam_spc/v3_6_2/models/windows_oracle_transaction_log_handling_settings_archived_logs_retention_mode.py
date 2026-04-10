from enum import Enum


class WindowsOracleTransactionLogHandlingSettingsArchivedLogsRetentionMode(str, Enum):
    DELETELOGSOLDERTHANHOURS = "DeleteLogsOlderThanHours"
    DELETELOGSOVERGB = "DeleteLogsOverGb"
    DONOTDELETEARCHIVEDLOGS = "DoNotDeleteArchivedLogs"

    def __str__(self) -> str:
        return str(self.value)
