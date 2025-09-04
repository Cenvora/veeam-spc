from collections.abc import Mapping
from typing import Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.backup_server_public_cloud_appliance_management_type import BackupServerPublicCloudApplianceManagementType
from ..models.backup_server_public_cloud_appliance_platform import BackupServerPublicCloudAppliancePlatform
from ..models.backup_server_public_cloud_appliance_status import BackupServerPublicCloudApplianceStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="BackupServerPublicCloudAppliance")


@_attrs_define
class BackupServerPublicCloudAppliance:
    """
    Attributes:
        instance_uid (Union[Unset, UUID]): UID assigned to a Veeam Backup for Public Clouds appliance.
        resource_id (Union[Unset, str]): Resource ID of a Veeam Backup for Public Clouds appliance.
        backup_server_uid (Union[Unset, UUID]): UID assigned to a Veeam Backup & Replication server.
        public_address (Union[Unset, str]): URL of a Veeam Backup for Public Clouds appliance.
        description (Union[Unset, str]): Description of a Veeam Backup for Public Clouds appliance.
        region (Union[Unset, str]): Region where a Veeam Backup for Public Clouds appliance is located.
        certificate_thumbprint (Union[Unset, str]): Thumbprint of a security certificate.
        remote_ui_access_enabled (Union[Unset, bool]): Indicates whether the Veeam Backup for Public Clouds appliance
            interface can be accessed in Veeam Service Provider Console.
        self_service_portal_url (Union[Unset, str]): URL of the Veeam Backup for Public Clouds portal.
        organization_uid (Union[Unset, UUID]): UID assigned to an organization that owns a Veeam Backup & Replication
            server on which a Veeam Backup for Public Clouds appliance is registered.
        mapped_organization_uid (Union[Unset, UUID]): UID assigned to an organization to which a Veeam Backup for Public
            Clouds appliance is assigned.
        location_uid (Union[Unset, UUID]): UID assigned to a Veeam Backup for Public Clouds appliance location.
        management_agent_uid (Union[Unset, UUID]): UID assigned to a management agent installed on a Veeam Backup for
            Public Clouds appliance server.
        version (Union[Unset, str]): Version of a Veeam Backup for Public Clouds appliance.
        status (Union[Unset, BackupServerPublicCloudApplianceStatus]): Status of a Veeam Backup for Public Clouds
            appliance.
        status_message (Union[Unset, str]): Message that contains information on the status of a Veeam Backup for Public
            Clouds appliance.
        platform (Union[Unset, BackupServerPublicCloudAppliancePlatform]): Platform of a Veeam Backup for Public Clouds
            appliance.
        management_type (Union[Unset, BackupServerPublicCloudApplianceManagementType]): Management type of a Veeam
            Backup for Public Clouds appliance.
    """

    instance_uid: Union[Unset, UUID] = UNSET
    resource_id: Union[Unset, str] = UNSET
    backup_server_uid: Union[Unset, UUID] = UNSET
    public_address: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    region: Union[Unset, str] = UNSET
    certificate_thumbprint: Union[Unset, str] = UNSET
    remote_ui_access_enabled: Union[Unset, bool] = UNSET
    self_service_portal_url: Union[Unset, str] = UNSET
    organization_uid: Union[Unset, UUID] = UNSET
    mapped_organization_uid: Union[Unset, UUID] = UNSET
    location_uid: Union[Unset, UUID] = UNSET
    management_agent_uid: Union[Unset, UUID] = UNSET
    version: Union[Unset, str] = UNSET
    status: Union[Unset, BackupServerPublicCloudApplianceStatus] = UNSET
    status_message: Union[Unset, str] = UNSET
    platform: Union[Unset, BackupServerPublicCloudAppliancePlatform] = UNSET
    management_type: Union[Unset, BackupServerPublicCloudApplianceManagementType] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        instance_uid: Union[Unset, str] = UNSET
        if not isinstance(self.instance_uid, Unset):
            instance_uid = str(self.instance_uid)

        resource_id = self.resource_id

        backup_server_uid: Union[Unset, str] = UNSET
        if not isinstance(self.backup_server_uid, Unset):
            backup_server_uid = str(self.backup_server_uid)

        public_address = self.public_address

        description = self.description

        region = self.region

        certificate_thumbprint = self.certificate_thumbprint

        remote_ui_access_enabled = self.remote_ui_access_enabled

        self_service_portal_url = self.self_service_portal_url

        organization_uid: Union[Unset, str] = UNSET
        if not isinstance(self.organization_uid, Unset):
            organization_uid = str(self.organization_uid)

        mapped_organization_uid: Union[Unset, str] = UNSET
        if not isinstance(self.mapped_organization_uid, Unset):
            mapped_organization_uid = str(self.mapped_organization_uid)

        location_uid: Union[Unset, str] = UNSET
        if not isinstance(self.location_uid, Unset):
            location_uid = str(self.location_uid)

        management_agent_uid: Union[Unset, str] = UNSET
        if not isinstance(self.management_agent_uid, Unset):
            management_agent_uid = str(self.management_agent_uid)

        version = self.version

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        status_message = self.status_message

        platform: Union[Unset, str] = UNSET
        if not isinstance(self.platform, Unset):
            platform = self.platform.value

        management_type: Union[Unset, str] = UNSET
        if not isinstance(self.management_type, Unset):
            management_type = self.management_type.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if instance_uid is not UNSET:
            field_dict["instanceUid"] = instance_uid
        if resource_id is not UNSET:
            field_dict["resourceId"] = resource_id
        if backup_server_uid is not UNSET:
            field_dict["backupServerUid"] = backup_server_uid
        if public_address is not UNSET:
            field_dict["publicAddress"] = public_address
        if description is not UNSET:
            field_dict["description"] = description
        if region is not UNSET:
            field_dict["region"] = region
        if certificate_thumbprint is not UNSET:
            field_dict["certificateThumbprint"] = certificate_thumbprint
        if remote_ui_access_enabled is not UNSET:
            field_dict["remoteUiAccessEnabled"] = remote_ui_access_enabled
        if self_service_portal_url is not UNSET:
            field_dict["selfServicePortalUrl"] = self_service_portal_url
        if organization_uid is not UNSET:
            field_dict["organizationUid"] = organization_uid
        if mapped_organization_uid is not UNSET:
            field_dict["mappedOrganizationUid"] = mapped_organization_uid
        if location_uid is not UNSET:
            field_dict["locationUid"] = location_uid
        if management_agent_uid is not UNSET:
            field_dict["managementAgentUid"] = management_agent_uid
        if version is not UNSET:
            field_dict["version"] = version
        if status is not UNSET:
            field_dict["status"] = status
        if status_message is not UNSET:
            field_dict["statusMessage"] = status_message
        if platform is not UNSET:
            field_dict["platform"] = platform
        if management_type is not UNSET:
            field_dict["managementType"] = management_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _instance_uid = d.pop("instanceUid", UNSET)
        instance_uid: Union[Unset, UUID]
        if isinstance(_instance_uid, Unset):
            instance_uid = UNSET
        else:
            instance_uid = UUID(_instance_uid)

        resource_id = d.pop("resourceId", UNSET)

        _backup_server_uid = d.pop("backupServerUid", UNSET)
        backup_server_uid: Union[Unset, UUID]
        if isinstance(_backup_server_uid, Unset):
            backup_server_uid = UNSET
        else:
            backup_server_uid = UUID(_backup_server_uid)

        public_address = d.pop("publicAddress", UNSET)

        description = d.pop("description", UNSET)

        region = d.pop("region", UNSET)

        certificate_thumbprint = d.pop("certificateThumbprint", UNSET)

        remote_ui_access_enabled = d.pop("remoteUiAccessEnabled", UNSET)

        self_service_portal_url = d.pop("selfServicePortalUrl", UNSET)

        _organization_uid = d.pop("organizationUid", UNSET)
        organization_uid: Union[Unset, UUID]
        if isinstance(_organization_uid, Unset):
            organization_uid = UNSET
        else:
            organization_uid = UUID(_organization_uid)

        _mapped_organization_uid = d.pop("mappedOrganizationUid", UNSET)
        mapped_organization_uid: Union[Unset, UUID]
        if isinstance(_mapped_organization_uid, Unset):
            mapped_organization_uid = UNSET
        else:
            mapped_organization_uid = UUID(_mapped_organization_uid)

        _location_uid = d.pop("locationUid", UNSET)
        location_uid: Union[Unset, UUID]
        if isinstance(_location_uid, Unset):
            location_uid = UNSET
        else:
            location_uid = UUID(_location_uid)

        _management_agent_uid = d.pop("managementAgentUid", UNSET)
        management_agent_uid: Union[Unset, UUID]
        if isinstance(_management_agent_uid, Unset):
            management_agent_uid = UNSET
        else:
            management_agent_uid = UUID(_management_agent_uid)

        version = d.pop("version", UNSET)

        _status = d.pop("status", UNSET)
        status: Union[Unset, BackupServerPublicCloudApplianceStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = BackupServerPublicCloudApplianceStatus(_status)

        status_message = d.pop("statusMessage", UNSET)

        _platform = d.pop("platform", UNSET)
        platform: Union[Unset, BackupServerPublicCloudAppliancePlatform]
        if isinstance(_platform, Unset):
            platform = UNSET
        else:
            platform = BackupServerPublicCloudAppliancePlatform(_platform)

        _management_type = d.pop("managementType", UNSET)
        management_type: Union[Unset, BackupServerPublicCloudApplianceManagementType]
        if isinstance(_management_type, Unset):
            management_type = UNSET
        else:
            management_type = BackupServerPublicCloudApplianceManagementType(_management_type)

        backup_server_public_cloud_appliance = cls(
            instance_uid=instance_uid,
            resource_id=resource_id,
            backup_server_uid=backup_server_uid,
            public_address=public_address,
            description=description,
            region=region,
            certificate_thumbprint=certificate_thumbprint,
            remote_ui_access_enabled=remote_ui_access_enabled,
            self_service_portal_url=self_service_portal_url,
            organization_uid=organization_uid,
            mapped_organization_uid=mapped_organization_uid,
            location_uid=location_uid,
            management_agent_uid=management_agent_uid,
            version=version,
            status=status,
            status_message=status_message,
            platform=platform,
            management_type=management_type,
        )

        backup_server_public_cloud_appliance.additional_properties = d
        return backup_server_public_cloud_appliance

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
