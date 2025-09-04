from enum import Enum


class PublicCloudSqlAccountDatabaseType(str, Enum):
    AWSSQL = "AwsSql"
    AZURESQL = "AzureSql"
    GCPMYSQLBUILTIN = "GcpMySqlBuiltIn"
    GCPPOSTGRES = "GcpPostgres"

    def __str__(self) -> str:
        return str(self.value)
