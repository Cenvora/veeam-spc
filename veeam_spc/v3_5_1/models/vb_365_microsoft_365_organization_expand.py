from enum import Enum


class Vb365Microsoft365OrganizationExpand(str, Enum):
    ORGANIZATIONBASE = "OrganizationBase"

    def __str__(self) -> str:
        return str(self.value)
