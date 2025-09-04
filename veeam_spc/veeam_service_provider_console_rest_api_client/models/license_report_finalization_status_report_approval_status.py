from enum import Enum


class LicenseReportFinalizationStatusReportApprovalStatus(str, Enum):
    APPROVED = "Approved"
    FINALIZATION = "Finalization"
    FINALIZED = "Finalized"
    NOTAPPROVABLE = "NotApprovable"
    NOTAPPROVED = "NotApproved"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
