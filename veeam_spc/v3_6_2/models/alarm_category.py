from enum import Enum


class AlarmCategory(str, Enum):
    BACKUPAGENT = "BackupAgent"
    BACKUPAGENTJOB = "BackupAgentJob"
    BACKUPAPPLIANCE = "BackupAppliance"
    BACKUPCLOUDGATEWAY = "BackupCloudGateway"
    BACKUPLICENSE = "BackupLicense"
    BACKUPMICROSOFT365SERVER = "BackupMicrosoft365Server"
    BACKUPPROXY = "BackupProxy"
    BACKUPREPOSITORY = "BackupRepository"
    BACKUPSERVER = "BackupServer"
    BACKUPSERVERAGENTJOB = "BackupServerAgentJob"
    BACKUPTENANTREPOSITORY = "BackupTenantRepository"
    BACKUPVMJOB = "BackupVmJob"
    BACKUPWANACCELERATOR = "BackupWanAccelerator"
    COMPANY = "Company"
    DISCOVERYRULE = "DiscoveryRule"
    ENTERPRISEMANAGER = "EnterpriseManager"
    INTEGRATOR = "Integrator"
    INTERNAL = "Internal"
    LOCATION = "Location"
    MANAGEMENTAGENT = "ManagementAgent"
    ONESERVER = "OneServer"
    RESELLER = "Reseller"
    RESELLERCLOUDREPOSITORY = "ResellerCloudRepository"
    SITE = "Site"
    SUREBACKUPJOB = "SureBackupJob"
    UNKNOWN = "Unknown"
    USER = "User"
    VMFAILOVERPLAN = "VmFailoverPlan"

    def __str__(self) -> str:
        return str(self.value)
