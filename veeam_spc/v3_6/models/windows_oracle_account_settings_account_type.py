from enum import Enum


class WindowsOracleAccountSettingsAccountType(str, Enum):
    ORACLE = "Oracle"
    WINDOWS = "Windows"

    def __str__(self) -> str:
        return str(self.value)
