from enum import Enum


class CompanyExpand(str, Enum):
    ORGANIZATION = "Organization"

    def __str__(self) -> str:
        return str(self.value)
