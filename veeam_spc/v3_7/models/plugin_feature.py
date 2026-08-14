from enum import Enum


class PluginFeature(str, Enum):
    AGENT = "Agent"
    DATAPURGE = "DataPurge"
    HEALTHMONITORING = "HealthMonitoring"
    LEASEDDATABASE = "LeasedDatabase"
    LOGSDOWNLOAD = "LogsDownload"
    READINESSCHECK = "ReadinessCheck"
    RESTAPIKEY = "RestApiKey"

    def __str__(self) -> str:
        return str(self.value)
