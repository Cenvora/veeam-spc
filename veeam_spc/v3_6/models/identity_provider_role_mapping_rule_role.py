from enum import Enum


class IdentityProviderRoleMappingRuleRole(str, Enum):
    COMPANYADMINISTRATOR = "CompanyAdministrator"
    COMPANYINVOICEAUDITOR = "CompanyInvoiceAuditor"
    COMPANYLOCATIONADMINISTRATOR = "CompanyLocationAdministrator"
    COMPANYLOCATIONUSER = "CompanyLocationUser"
    COMPANYOWNER = "CompanyOwner"
    COMPANYTENANT = "CompanyTenant"
    PORTALADMINISTRATOR = "PortalAdministrator"
    PORTALOPERATOR = "PortalOperator"
    PORTALREADONLYOPERATOR = "PortalReadonlyOperator"
    RESELLERADMINISTRATOR = "ResellerAdministrator"
    RESELLERINVOICEAUDITOR = "ResellerInvoiceAuditor"
    RESELLEROPERATOR = "ResellerOperator"
    RESELLEROWNER = "ResellerOwner"
    RESELLERUSER = "ResellerUser"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
