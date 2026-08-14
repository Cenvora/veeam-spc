from enum import Enum


class VOneDeploymentLicenseSettingsLicenseSource(str, Enum):
    ANSWERXML = "AnswerXml"
    LICENSEFILECONTENT = "LicenseFileContent"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
