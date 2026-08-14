from enum import Enum


class PublicCloudDatabaseType(str, Enum):
    AWSDYNAMODB = "AwsDynamoDb"
    AWSRDS = "AwsRds"
    AWSREDSHIFT = "AwsRedshift"
    AWSREDSHIFTSERVERLESS = "AwsRedshiftServerless"
    AZURECOSMOSDB = "AzureCosmosDb"
    AZURESQL = "AzureSql"
    GOOGLECLOUDSPANNER = "GoogleCloudSpanner"
    GOOGLESQL = "GoogleSql"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
