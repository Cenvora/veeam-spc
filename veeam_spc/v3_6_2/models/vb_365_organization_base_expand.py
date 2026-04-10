from enum import Enum


class Vb365OrganizationBaseExpand(str, Enum):
    ORGANIZATIONDETAILS = "OrganizationDetails"
    VB365SERVER = "Vb365Server"

    def __str__(self) -> str:
        return str(self.value)
