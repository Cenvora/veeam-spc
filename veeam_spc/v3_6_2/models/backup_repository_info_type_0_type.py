from enum import Enum


class BackupRepositoryInfoType0Type(str, Enum):
    AMAZONS3 = "AmazonS3"
    AMAZONS3COMPATIBLE = "AmazonS3Compatible"
    AMAZONS3EXTERNAL = "AmazonS3External"
    AMAZONS3GLACIER = "AmazonS3Glacier"
    AMAZONSNOWBALL = "AmazonSnowball"
    AZUREARCHIVETIER = "AzureArchiveTier"
    AZUREEXTERNAL = "AzureExternal"
    CLOUD = "Cloud"
    DELLEMCDATADOMAIN = "DellEmcDataDomain"
    ELEVENELEVEN = "ElevenEleven"
    EXAGRID = "ExaGrid"
    FUJITSU = "Fujitsu"
    GOOGLEARCHIVETIER = "GoogleArchiveTier"
    GOOGLECLOUD = "GoogleCloud"
    HPESTOREONCE = "HpeStoreOnce"
    IBMCLOUDOBJECTSTORAGE = "IbmCloudObjectStorage"
    INFINIDAT = "Infinidat"
    LINUX = "Linux"
    LINUXHARDENED = "LinuxHardened"
    MICROSOFTAZUREARCHIVE = "MicrosoftAzureArchive"
    MICROSOFTAZUREBLOBSTORAGE = "MicrosoftAzureBlobStorage"
    MICROSOFTAZUREDATABOX = "MicrosoftAzureDataBox"
    NFS = "NFS"
    QUANTUMDXI = "QuantumDxi"
    S3COMPATIBLE = "S3Compatible"
    SANSNAPSHOT = "SanSnapshot"
    SCALEOUT = "ScaleOut"
    SHARE = "Share"
    UNKNOWN = "Unknown"
    VEEAMVAULT = "VeeamVault"
    WASABI = "Wasabi"
    WINDOWS = "Windows"

    def __str__(self) -> str:
        return str(self.value)
