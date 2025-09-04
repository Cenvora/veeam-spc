from enum import Enum


class LinuxPostgreSqlApplicationAwareProcessingSettingsAuthType(str, Enum):
    PSQLPASSWORD = "PSQLPassword"
    PSQLPASSWORDFILE = "PSQLPasswordFile"
    PSQLPEER = "PSQLPeer"

    def __str__(self) -> str:
        return str(self.value)
