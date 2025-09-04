from enum import Enum


class Collation(str, Enum):
    IGNORECASE = "ignorecase"
    LEXICOGRAPHIC = "lexicographic"
    ORDINAL = "ordinal"

    def __str__(self) -> str:
        return str(self.value)
