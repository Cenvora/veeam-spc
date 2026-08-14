from enum import Enum


class LocalUserRuleRoleType(str, Enum):
    OPERATOR = "operator"
    PORTALADMINISTRATOR = "portalAdministrator"
    READONLYOPERATOR = "readonlyOperator"
    SITEADMINISTRATOR = "siteAdministrator"
    UNKNOWN = "unknown"

    def __str__(self) -> str:
        return str(self.value)
