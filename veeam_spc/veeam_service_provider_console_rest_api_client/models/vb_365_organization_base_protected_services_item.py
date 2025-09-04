from enum import Enum


class Vb365OrganizationBaseProtectedServicesItem(str, Enum):
    EXCHANGEONLINE = "ExchangeOnline"
    MICROSOFTEXCHANGESERVER = "MicrosoftExchangeServer"
    MICROSOFTSHAREPOINTSERVER = "MicrosoftSharePointServer"
    MICROSOFTTEAMS = "MicrosoftTeams"
    MICROSOFTTEAMSCHATS = "MicrosoftTeamsChats"
    SHAREPOINTONLINEANDONEDRIVEFORBUSINESS = "SharePointOnlineAndOneDriveForBusiness"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
