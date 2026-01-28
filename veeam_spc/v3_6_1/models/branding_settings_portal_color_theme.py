from enum import Enum


class BrandingSettingsPortalColorTheme(str, Enum):
    BLUE = "Blue"
    GREEN = "Green"
    GREY = "Grey"
    PINK = "Pink"
    RED = "Red"
    TURQUOISE = "Turquoise"
    UNKNOWN = "Unknown"
    YELLOW = "Yellow"

    def __str__(self) -> str:
        return str(self.value)
