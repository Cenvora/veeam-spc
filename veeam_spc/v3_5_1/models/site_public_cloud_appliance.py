from collections.abc import Mapping
from typing import Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.backup_server_public_cloud_appliance_platform import BackupServerPublicCloudAppliancePlatform
from ..models.backup_server_public_cloud_appliance_status import BackupServerPublicCloudApplianceStatus
from ..models.e_vb_appliance_deployment_status import EVbApplianceDeploymentStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="SitePublicCloudAppliance")


@_attrs_define
class SitePublicCloudAppliance:
    """
    Attributes:
        instance_uid (Union[Unset, UUID]): UID assigned to a Veeam Backup for Public Clouds appliance.
        site_uid (Union[Unset, UUID]): UID assigned to a Veeam Cloud Connect site.
        public_address (Union[Unset, str]): URL of a Veeam Backup for Public Clouds appliance.
        appliance_name (Union[Unset, str]): Name of a Veeam Backup for Public Clouds appliance.
        description (Union[Unset, str]): Description of a Veeam Backup for Public Clouds appliance.
        region (Union[Unset, str]): Region where a Veeam Backup for Public Clouds appliance is located.
        certificate_thumbprint (Union[Unset, str]): Thumbprint of a security certificate.
        remote_ui_access_enabled (Union[Unset, bool]): Indicates whether the Veeam Backup for Public Clouds appliance
            can be accessed in Veeam Service Provider Console.
        self_service_portal_url (Union[Unset, str]): URL of the Veeam Backup for Public Clouds portal.
        organization_uid (Union[Unset, UUID]): UID assigned to an organization that owns a Veeam Cloud Connect site on
            which a Veeam Backup for Public Clouds appliance is registered.
        mapped_organization_uid (Union[Unset, UUID]): UID assigned to an organization to which a Veeam Backup for Public
            Clouds appliance is assigned.
        management_agent_uid (Union[Unset, UUID]): UID assigned to a management agent installed on a Veeam Backup for
            Public Clouds appliance server.
        version (Union[Unset, str]): Version of a Veeam Backup for Public Clouds appliance.
        status (Union[Unset, BackupServerPublicCloudApplianceStatus]): Status of a Veeam Backup for Public Clouds
            appliance.
        status_message (Union[Unset, str]): Message that contains information on the status of a Veeam Backup for Public
            Clouds appliance.
        platform (Union[Unset, BackupServerPublicCloudAppliancePlatform]): Platform of a Veeam Backup for Public Clouds
            appliance.
        deployment_status (Union[Unset, EVbApplianceDeploymentStatus]): Deployment status.
    """

    instance_uid: Union[Unset, UUID] = UNSET
    site_uid: Union[Unset, UUID] = UNSET
    public_address: Union[Unset, str] = UNSET
    appliance_name: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    region: Union[Unset, str] = UNSET
    certificate_thumbprint: Union[Unset, str] = UNSET
    remote_ui_access_enabled: Union[Unset, bool] = UNSET
    self_service_portal_url: Union[Unset, str] = UNSET
    organization_uid: Union[Unset, UUID] = UNSET
    mapped_organization_uid: Union[Unset, UUID] = UNSET
    management_agent_uid: Union[Unset, UUID] = UNSET
    version: Union[Unset, str] = UNSET
    status: Union[Unset, BackupServerPublicCloudApplianceStatus] = UNSET
    status_message: Union[Unset, str] = UNSET
    platform: Union[Unset, BackupServerPublicCloudAppliancePlatform] = UNSET
    deployment_status: Union[Unset, EVbApplianceDeploymentStatus] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        instance_uid: Union[Unset, str] = UNSET
        if not isinstance(self.instance_uid, Unset):
            instance_uid = str(self.instance_uid)

        site_uid: Union[Unset, str] = UNSET
        if not isinstance(self.site_uid, Unset):
            site_uid = str(self.site_uid)

        public_address = self.public_address

        appliance_name = self.appliance_name

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

        deployment_status: Union[Unset, str] = UNSET
        if not isinstance(self.deployment_status, Unset):
            deployment_status = self.deployment_status.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if instance_uid is not UNSET:
            field_dict["instanceUid"] = instance_uid
        if site_uid is not UNSET:
            field_dict["siteUid"] = site_uid
        if public_address is not UNSET:
            field_dict["publicAddress"] = public_address
        if appliance_name is not UNSET:
            field_dict["applianceName"] = appliance_name
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
        if deployment_status is not UNSET:
            field_dict["deploymentStatus"] = deployment_status

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

        _site_uid = d.pop("siteUid", UNSET)
        site_uid: Union[Unset, UUID]
        if isinstance(_site_uid, Unset):
            site_uid = UNSET
        else:
            site_uid = UUID(_site_uid)

        public_address = d.pop("publicAddress", UNSET)

        appliance_name = d.pop("applianceName", UNSET)

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

        _deployment_status = d.pop("deploymentStatus", UNSET)
        deployment_status: Union[Unset, EVbApplianceDeploymentStatus]
        if isinstance(_deployment_status, Unset):
            deployment_status = UNSET
        else:
            deployment_status = EVbApplianceDeploymentStatus(_deployment_status)

        site_public_cloud_appliance = cls(
            instance_uid=instance_uid,
            site_uid=site_uid,
            public_address=public_address,
            appliance_name=appliance_name,
            description=description,
            region=region,
            certificate_thumbprint=certificate_thumbprint,
            remote_ui_access_enabled=remote_ui_access_enabled,
            self_service_portal_url=self_service_portal_url,
            organization_uid=organization_uid,
            mapped_organization_uid=mapped_organization_uid,
            management_agent_uid=management_agent_uid,
            version=version,
            status=status,
            status_message=status_message,
            platform=platform,
            deployment_status=deployment_status,
        )

        site_public_cloud_appliance.additional_properties = d
        return site_public_cloud_appliance

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
