from enum import Enum


class BackupServerJobType(str, Enum):
    AGENTBACKUPJOB = "AgentBackupJob"
    AGENTPOLICY = "AgentPolicy"
    AHVSTORAGESNAPSHOTJOB = "AhvStorageSnapshotJob"
    AWSBACKUPJOB = "AwsBackupJob"
    AZUREBACKUPJOB = "AzureBackupJob"
    BACKUPCOPY = "BackupCopy"
    BACKUPFILE = "BackupFile"
    BACKUPFILECOPY = "BackupFileCopy"
    BACKUPTOTAPE = "BackupToTape"
    BACKUPVM = "BackupVm"
    CDPREPLICATIONVM = "CdpReplicationVM"
    COPYFILE = "CopyFile"
    COPYVM = "CopyVm"
    FILETOTAPE = "FileToTape"
    GOOGLEBACKUPJOB = "GoogleBackupJob"
    OBJECTSTORAGEBACKUP = "ObjectStorageBackup"
    OBJECTSTORAGEBACKUPCOPY = "ObjectStorageBackupCopy"
    ORACLELOGBACKUP = "OracleLogBackup"
    POSTGRESQLLOGBACKUP = "PostgreSqlLogBackup"
    REPLICATIONVM = "ReplicationVM"
    SIMPLEBACKUPCOPY = "SimpleBackupCopy"
    SQLLOGBACKUP = "SqlLogBackup"
    SUREBACKUP = "SureBackup"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
