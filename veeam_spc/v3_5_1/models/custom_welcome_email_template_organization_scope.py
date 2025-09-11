from enum import Enum


class CustomWelcomeEmailTemplateOrganizationScope(str, Enum):
    CHILDOBJECTS = "ChildObjects"
    CURRENTOBJECT = "CurrentObject"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
