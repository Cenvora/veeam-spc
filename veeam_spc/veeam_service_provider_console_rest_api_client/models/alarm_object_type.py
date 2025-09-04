from enum import Enum


class AlarmObjectType(str, Enum):
    BACKUPAGENT = "BackupAgent"
    BACKUPMICROSOFT365SERVER = "BackupMicrosoft365Server"
    BACKUPPROXY = "BackupProxy"
    BACKUPREPOSITORY = "BackupRepository"
    BACKUPSERVER = "BackupServer"
    BACKUPSERVERJOB = "BackupServerJob"
    BACKUPWANACCELERATOR = "BackupWanAccelerator"
    CLOUDGATEWAY = "CloudGateway"
    CLOUDREPOSITORY = "CloudRepository"
    COMPANY = "Company"
    DISCOVERYRULE = "DiscoveryRule"
    ENTERPRISEMANAGERSERVER = "EnterpriseManagerServer"
    FAILOVERPLAN = "FailoverPlan"
    INTEGRATOR = "Integrator"
    INTERNAL = "Internal"
    LOCATION = "Location"
    MANAGEMENTAGENT = "ManagementAgent"
    OBJECTENTITY = "ObjectEntity"
    RESELLER = "Reseller"
    RESELLERCLOUDREPOSITORY = "ResellerCloudRepository"
    SITE = "Site"
    UNKNOWN = "Unknown"
    USER = "User"
    VBAPPLIANCE = "VbAppliance"
    VONESERVER = "VOneServer"

    def __str__(self) -> str:
        return str(self.value)
