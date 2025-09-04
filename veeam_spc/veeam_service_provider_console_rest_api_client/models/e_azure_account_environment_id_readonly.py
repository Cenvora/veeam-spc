from enum import Enum


class EAzureAccountEnvironmentIdReadonly(str, Enum):
    CHINA = "China"
    GLOBAL = "Global"
    USGOVERNMENT = "UsGovernment"

    def __str__(self) -> str:
        return str(self.value)
