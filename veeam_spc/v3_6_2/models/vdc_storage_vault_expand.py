from enum import Enum


class VdcStorageVaultExpand(str, Enum):
    VDCVAULTCOUNTRY = "VdcVaultCountry"
    VDCVAULTDATACENTER = "VdcVaultDataCenter"
    VDCVAULTSUBSCRIPTION = "VdcVaultSubscription"
    VDCVAULTTENANT = "VdcVaultTenant"

    def __str__(self) -> str:
        return str(self.value)
