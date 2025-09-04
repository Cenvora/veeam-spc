from enum import Enum


class Vb365BackupRepositoryYearlyRetentionPeriod(str, Enum):
    KEEP = "Keep"
    UNKNOWN = "Unknown"
    YEAR1 = "Year1"
    YEARS10 = "Years10"
    YEARS2 = "Years2"
    YEARS25 = "Years25"
    YEARS3 = "Years3"
    YEARS5 = "Years5"
    YEARS7 = "Years7"

    def __str__(self) -> str:
        return str(self.value)
