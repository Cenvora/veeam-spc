from enum import Enum


class BackupServerHostType(str, Enum):
    AMAZONS3BUCKET = "AmazonS3Bucket"
    AMAZONS3SERVER = "AmazonS3Server"
    AZUREBLOBSERVER = "AzureBlobServer"
    BACKUPSERVER = "BackupServer"
    CIFSSERVER = "CifsServer"
    CIFSSERVERSHARE = "CifsServerShare"
    CIFSSHARE = "CifsShare"
    ESX = "ESX"
    ESXI = "ESXi"
    EXTERNALINFRASTRUCTURESERVER = "ExternalInfrastructureServer"
    GOOGLESTORAGEBUCKET = "GoogleStorageBucket"
    GOOGLESTORAGESERVER = "GoogleStorageServer"
    HYPERVCLUSTER = "HyperVCluster"
    HYPERVSERVER = "HyperVServer"
    LINUXHOST = "LinuxHost"
    LOCALHOST = "LocalHost"
    NASFILER = "NasFiler"
    NFSSERVER = "NfsServer"
    NFSSERVERSHARE = "NfsServerShare"
    NFSSHARE = "NfsShare"
    S3COMPATIBLEBUCKET = "S3CompatibleBucket"
    S3COMPATIBLESERVER = "S3CompatibleServer"
    SANCIFSSERVER = "SanCifsServer"
    SANNFSSERVER = "SanNfsServer"
    SCVMM = "Scvmm"
    SHARE = "Share"
    SMBCLUSTER = "SmbCluster"
    SMBSERVER = "SmbServer"
    UNKNOWN = "Unknown"
    VCDSYSTEM = "VcdSystem"
    VIRTUALCENTER = "VirtualCenter"
    WINDOWSHOST = "WindowsHost"

    def __str__(self) -> str:
        return str(self.value)
