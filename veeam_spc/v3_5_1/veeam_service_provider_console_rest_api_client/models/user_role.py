from enum import Enum


class UserRole(str, Enum):
    COMPANYADMINISTRATOR = "CompanyAdministrator"
    COMPANYINVOICEAUDITOR = "CompanyInvoiceAuditor"
    COMPANYLOCATIONADMINISTRATOR = "CompanyLocationAdministrator"
    COMPANYLOCATIONUSER = "CompanyLocationUser"
    COMPANYOWNER = "CompanyOwner"
    COMPANYSUBTENANT = "CompanySubtenant"
    PORTALADMINISTRATOR = "PortalAdministrator"
    PORTALOPERATOR = "PortalOperator"
    PORTALREADONLYOPERATOR = "PortalReadonlyOperator"
    RESELLERADMINISTRATOR = "ResellerAdministrator"
    RESELLERINVOICEAUDITOR = "ResellerInvoiceAuditor"
    RESELLEROPERATOR = "ResellerOperator"
    RESELLEROWNER = "ResellerOwner"
    RESELLERUSER = "ResellerUser"
    SITEADMINISTRATOR = "SiteAdministrator"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
