from enum import Enum


class CompanyStatus(str, Enum):
    ACTIVE = "Active"
    DISABLED = "Disabled"
    REMOVED_CREATING = "REMOVED_Creating"
    REMOVED_DELETED = "REMOVED_Deleted"
    REMOVED_DELETING = "REMOVED_Deleting"
    REMOVED_EXPIRED = "REMOVED_Expired"
    REMOVED_SITERESOURCECREATING = "REMOVED_SiteResourceCreating"
    REMOVED_SITERESOURCECREATIONFAILED = "REMOVED_SiteResourceCreationFailed"
    REMOVED_SITERESOURCEUPDATEFAILED = "REMOVED_SiteResourceUpdateFailed"
    REMOVED_SITERESOURCEUPDATING = "REMOVED_SiteResourceUpdating"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
