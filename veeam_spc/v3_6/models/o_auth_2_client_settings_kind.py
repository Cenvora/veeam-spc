from enum import Enum


class OAuth2ClientSettingsKind(str, Enum):
    AZURE = "Azure"
    AZURECHINACLOUD = "AzureChinaCloud"
    AZUREGERMANY = "AzureGermany"
    AZUREGOVCLOUD = "AzureGovCloud"
    GOOGLE = "Google"

    def __str__(self) -> str:
        return str(self.value)
