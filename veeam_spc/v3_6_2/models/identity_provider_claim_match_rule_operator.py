from enum import Enum


class IdentityProviderClaimMatchRuleOperator(str, Enum):
    CONTAINS = "Contains"
    EQUALS = "Equals"
    MATCHREGEX = "MatchRegex"
    NOTCONTAINS = "NotContains"
    NOTEQUALS = "NotEquals"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
