from enum import Enum


class CompanyStatus(str, Enum):
    ACTIVE = "Active"
    CREATING = "Creating"
    DELETED = "Deleted"
    DELETING = "Deleting"
    DISABLED = "Disabled"
    EXPIRED = "Expired"
    SITERESOURCECREATING = "SiteResourceCreating"
    SITERESOURCECREATIONFAILED = "SiteResourceCreationFailed"
    SITERESOURCEUPDATEFAILED = "SiteResourceUpdateFailed"
    SITERESOURCEUPDATING = "SiteResourceUpdating"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
