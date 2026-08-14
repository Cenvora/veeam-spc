from enum import Enum


class Saml2ServiceCertificateConfigurationMetadataPublishOverride(str, Enum):
    DONOTPUBLISH = "DoNotPublish"
    NONE = "None"
    PUBLISHENCRYPTION = "PublishEncryption"
    PUBLISHSIGNING = "PublishSigning"
    PUBLISHUNSPECIFIED = "PublishUnspecified"

    def __str__(self) -> str:
        return str(self.value)
