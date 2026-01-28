from enum import Enum


class PublicCloudGuestOsCredentialsRole(str, Enum):
    COMPANYADMINISTRATOR = "companyAdministrator"
    SERVICEPROVIDERADMINISTRATOR = "serviceProviderAdministrator"

    def __str__(self) -> str:
        return str(self.value)
