from enum import Enum


class BrandingSettingsManagedOrganizationsBrandingPolicy(str, Enum):
    ALLOWCUSTOMIZATION = "AllowCustomization"
    FORCEINHERITANCE = "ForceInheritance"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
