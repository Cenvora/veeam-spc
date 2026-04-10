from enum import Enum


class MacGfsYearlyRetentionSettingsUseMonthlyFullBackupForTheFollowingMonth(str, Enum):
    APR = "Apr"
    AUG = "Aug"
    DEC = "Dec"
    FEB = "Feb"
    JAN = "Jan"
    JUL = "Jul"
    JUN = "Jun"
    MAR = "Mar"
    MAY = "May"
    NOV = "Nov"
    OCT = "Oct"
    SEP = "Sep"

    def __str__(self) -> str:
        return str(self.value)
