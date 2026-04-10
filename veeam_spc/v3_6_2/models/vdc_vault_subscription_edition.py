from enum import Enum


class VdcVaultSubscriptionEdition(str, Enum):
    ADVANCEDCORE = "AdvancedCore"
    ADVANCEDNONCORE = "AdvancedNonCore"
    FOUNDATIONCORE = "FoundationCore"
    FOUNDATIONNONCORE = "FoundationNonCore"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
