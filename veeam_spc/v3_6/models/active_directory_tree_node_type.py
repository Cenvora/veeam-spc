from enum import Enum


class ActiveDirectoryTreeNodeType(str, Enum):
    COMMONNAME = "CommonName"
    DOMAINCOMPONENT = "DomainComponent"
    ORGANIZATIONALUNIT = "OrganizationalUnit"

    def __str__(self) -> str:
        return str(self.value)
