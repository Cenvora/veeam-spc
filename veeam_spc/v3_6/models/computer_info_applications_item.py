from enum import Enum


class ComputerInfoApplicationsItem(str, Enum):
    APACHESERVER = "ApacheServer"
    MICROSOFTACTIVEDIRECTORY = "MicrosoftActiveDirectory"
    MICROSOFTEXCHANGESERVER = "MicrosoftExchangeServer"
    MICROSOFTSHAREPOINT = "MicrosoftSharePoint"
    MICROSOFTSQLSERVER = "MicrosoftSqlServer"
    MONGODB = "MongoDB"
    MYSQL = "MySQL"
    ORACLE = "Oracle"
    OTHERAPP = "OtherApp"
    POSTGRESQL = "PostgreSQL"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
