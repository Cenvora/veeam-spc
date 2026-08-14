from enum import Enum


class LabelScope(str, Enum):
    AGENTS = "Agents"
    VBRREPOSITORIES = "VbrRepositories"

    def __str__(self) -> str:
        return str(self.value)
