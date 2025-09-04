from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.creating_object_info import CreatingObjectInfo


T = TypeVar("T", bound="PublicCloudRepository")


@_attrs_define
class PublicCloudRepository:
    """
    Attributes:
        instance_uid (str): UID assigned to a public cloud repository.
        repository_name (str): Name of a public cloud repository.
        description (str): Description of a public cloud repository.
        platform (str): Platform of a public cloud repository.
        appliance_name (str): Name of a Veeam Backup for Public Clouds appliance to which a repository belongs.
        appliance_uid (UUID): UID assigned to a Veeam Backup for Public Clouds appliance to which a repository belongs.
        bucket (str): Name of an Amazon S3 bucket or Microsoft Azure container that is used as a backup target.
        folder (str): Name of a folder used to group backup files in a bucket or container.
        region (str): Name of a Veeam Backup for Public Clouds appliance region.
        storage_class (str): Repository storage class.
        organization_name (str): Name of an organization to which a Veeam Backup for Public Clouds appliance belongs.
        organization_uid (UUID): UID assigned to an organization to which a Veeam Backup for Public Clouds appliance
            belongs.
        site_name (str): Name of a Veeam Cloud Connect site.
        site_uid (UUID): UID assigned to a Veeam Cloud Connect site.
        creating_state (CreatingObjectInfo): Status of a repository creation.
        is_encrypted (Union[Unset, bool]): Indicates whether stored data encryption is enabled.
        immutability_enabled (Union[Unset, bool]): Indicates whether immutability is enabled.
    """

    instance_uid: str
    repository_name: str
    description: str
    platform: str
    appliance_name: str
    appliance_uid: UUID
    bucket: str
    folder: str
    region: str
    storage_class: str
    organization_name: str
    organization_uid: UUID
    site_name: str
    site_uid: UUID
    creating_state: "CreatingObjectInfo"
    is_encrypted: Union[Unset, bool] = UNSET
    immutability_enabled: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        instance_uid = self.instance_uid

        repository_name = self.repository_name

        description = self.description

        platform = self.platform

        appliance_name = self.appliance_name

        appliance_uid = str(self.appliance_uid)

        bucket = self.bucket

        folder = self.folder

        region = self.region

        storage_class = self.storage_class

        organization_name = self.organization_name

        organization_uid = str(self.organization_uid)

        site_name = self.site_name

        site_uid = str(self.site_uid)

        creating_state = self.creating_state.to_dict()

        is_encrypted = self.is_encrypted

        immutability_enabled = self.immutability_enabled

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "instanceUid": instance_uid,
                "repositoryName": repository_name,
                "description": description,
                "platform": platform,
                "applianceName": appliance_name,
                "applianceUid": appliance_uid,
                "bucket": bucket,
                "folder": folder,
                "region": region,
                "storageClass": storage_class,
                "organizationName": organization_name,
                "organizationUid": organization_uid,
                "siteName": site_name,
                "siteUid": site_uid,
                "creatingState": creating_state,
            }
        )
        if is_encrypted is not UNSET:
            field_dict["isEncrypted"] = is_encrypted
        if immutability_enabled is not UNSET:
            field_dict["immutabilityEnabled"] = immutability_enabled

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.creating_object_info import CreatingObjectInfo

        d = dict(src_dict)
        instance_uid = d.pop("instanceUid")

        repository_name = d.pop("repositoryName")

        description = d.pop("description")

        platform = d.pop("platform")

        appliance_name = d.pop("applianceName")

        appliance_uid = UUID(d.pop("applianceUid"))

        bucket = d.pop("bucket")

        folder = d.pop("folder")

        region = d.pop("region")

        storage_class = d.pop("storageClass")

        organization_name = d.pop("organizationName")

        organization_uid = UUID(d.pop("organizationUid"))

        site_name = d.pop("siteName")

        site_uid = UUID(d.pop("siteUid"))

        creating_state = CreatingObjectInfo.from_dict(d.pop("creatingState"))

        is_encrypted = d.pop("isEncrypted", UNSET)

        immutability_enabled = d.pop("immutabilityEnabled", UNSET)

        public_cloud_repository = cls(
            instance_uid=instance_uid,
            repository_name=repository_name,
            description=description,
            platform=platform,
            appliance_name=appliance_name,
            appliance_uid=appliance_uid,
            bucket=bucket,
            folder=folder,
            region=region,
            storage_class=storage_class,
            organization_name=organization_name,
            organization_uid=organization_uid,
            site_name=site_name,
            site_uid=site_uid,
            creating_state=creating_state,
            is_encrypted=is_encrypted,
            immutability_enabled=immutability_enabled,
        )

        public_cloud_repository.additional_properties = d
        return public_cloud_repository

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
