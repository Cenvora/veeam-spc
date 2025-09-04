from enum import Enum


class LinuxMySqlApplicationAwareProcessingSettingsAuthType(str, Enum):
    MYSQLPASSWORD = "MySQLPassword"
    MYSQLPASSWORDFILE = "MySQLPasswordFile"

    def __str__(self) -> str:
        return str(self.value)
