from enum import Enum


class PatchCustomWelcomeEmailTemplateOrganizationScope(str, Enum):
    CHILDOBJECTS = "ChildObjects"
    CURRENTOBJECT = "CurrentObject"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
