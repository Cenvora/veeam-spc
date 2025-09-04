from enum import Enum


class IdentityProviderRoleMappingRuleExpand(str, Enum):
    IDENTITYPROVIDER = "IdentityProvider"

    def __str__(self) -> str:
        return str(self.value)
