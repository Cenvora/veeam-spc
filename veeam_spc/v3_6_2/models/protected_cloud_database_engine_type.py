from enum import Enum


class ProtectedCloudDatabaseEngineType(str, Enum):
    AURORADBMYSQL = "AuroraDbMySql"
    AURORADBPOSTGRES = "AuroraDbPostgres"
    AWSREDSHIFT = "AwsRedshift"
    AWSREDSHIFTSERVERLESS = "AwsRedshiftServerless"
    AZURECOSMOSDB = "AzureCosmosDb"
    AZURESQL = "AzureSql"
    CLOUDSPANNER = "CloudSpanner"
    DYNAMODB = "DynamoDb"
    GREMLIN = "Gremlin"
    MARIADB = "MariaDb"
    MONGODB = "MongoDb"
    MSSQL = "MsSql"
    MYSQL = "MySql"
    NOSQL = "NoSql"
    ORACLEDB = "OracleDb"
    POSTGRES = "Postgres"
    TABLE = "Table"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
