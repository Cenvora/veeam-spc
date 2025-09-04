from enum import Enum


class GetCustomWelcomeEmailTemplatesOrganizationScope(str, Enum):
    CHILDOBJECTS = "ChildObjects"
    CURRENTOBJECT = "CurrentObject"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
