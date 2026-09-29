from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PublicCloudAwsAppliance")


@_attrs_define
class PublicCloudAwsAppliance:
    """
    Attributes:
        account_uid (UUID): UID assigned to an AWS account used to access a Veeam Backup for Public Clouds appliance.
        guest_os_credentials_uid (UUID): UID assigned to guest OS credentials record.
        management_agent_uid (UUID | Unset): UID assigned to management agent installed on a server where Veeam Backup
            for Public Clouds appliance is deployed.
        instance_uid (UUID | Unset): UID assigned to a Veeam Backup for Public Clouds appliance.
        description (None | str | Unset): Description of a Veeam Backup for Public Clouds appliance.
        public_address (str | Unset): URL of a Veeam Backup for Public Clouds appliance.
        private_network_address (None | str | Unset): Private IP address or DNS name of a network.
        certificate_thumbprint (str | Unset): Thumbprint of a security certificate.
        data_center_id (str | Unset): ID assigned to an AWS datacenter.
        region_id (str | Unset): ID assigned to an AWS region.
        resource_id (str | Unset): ID assigned to an AWS network resource.
    """

    account_uid: UUID
    guest_os_credentials_uid: UUID
    management_agent_uid: UUID | Unset = UNSET
    instance_uid: UUID | Unset = UNSET
    description: None | str | Unset = UNSET
    public_address: str | Unset = UNSET
    private_network_address: None | str | Unset = UNSET
    certificate_thumbprint: str | Unset = UNSET
    data_center_id: str | Unset = UNSET
    region_id: str | Unset = UNSET
    resource_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        account_uid = str(self.account_uid)

        guest_os_credentials_uid = str(self.guest_os_credentials_uid)

        management_agent_uid: str | Unset = UNSET
        if not isinstance(self.management_agent_uid, Unset):
            management_agent_uid = str(self.management_agent_uid)

        instance_uid: str | Unset = UNSET
        if not isinstance(self.instance_uid, Unset):
            instance_uid = str(self.instance_uid)

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        public_address = self.public_address

        private_network_address: None | str | Unset
        if isinstance(self.private_network_address, Unset):
            private_network_address = UNSET
        else:
            private_network_address = self.private_network_address

        certificate_thumbprint = self.certificate_thumbprint

        data_center_id = self.data_center_id

        region_id = self.region_id

        resource_id = self.resource_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "accountUid": account_uid,
                "guestOsCredentialsUid": guest_os_credentials_uid,
            }
        )
        if management_agent_uid is not UNSET:
            field_dict["managementAgentUid"] = management_agent_uid
        if instance_uid is not UNSET:
            field_dict["instanceUid"] = instance_uid
        if description is not UNSET:
            field_dict["description"] = description
        if public_address is not UNSET:
            field_dict["publicAddress"] = public_address
        if private_network_address is not UNSET:
            field_dict["privateNetworkAddress"] = private_network_address
        if certificate_thumbprint is not UNSET:
            field_dict["certificateThumbprint"] = certificate_thumbprint
        if data_center_id is not UNSET:
            field_dict["dataCenterId"] = data_center_id
        if region_id is not UNSET:
            field_dict["regionId"] = region_id
        if resource_id is not UNSET:
            field_dict["resourceId"] = resource_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        account_uid = UUID(d.pop("accountUid"))

        guest_os_credentials_uid = UUID(d.pop("guestOsCredentialsUid"))

        _management_agent_uid = d.pop("managementAgentUid", UNSET)
        management_agent_uid: UUID | Unset
        if isinstance(_management_agent_uid, Unset):
            management_agent_uid = UNSET
        else:
            management_agent_uid = UUID(_management_agent_uid)

        _instance_uid = d.pop("instanceUid", UNSET)
        instance_uid: UUID | Unset
        if isinstance(_instance_uid, Unset):
            instance_uid = UNSET
        else:
            instance_uid = UUID(_instance_uid)

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        public_address = d.pop("publicAddress", UNSET)

        def _parse_private_network_address(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        private_network_address = _parse_private_network_address(d.pop("privateNetworkAddress", UNSET))

        certificate_thumbprint = d.pop("certificateThumbprint", UNSET)

        data_center_id = d.pop("dataCenterId", UNSET)

        region_id = d.pop("regionId", UNSET)

        resource_id = d.pop("resourceId", UNSET)

        public_cloud_aws_appliance = cls(
            account_uid=account_uid,
            guest_os_credentials_uid=guest_os_credentials_uid,
            management_agent_uid=management_agent_uid,
            instance_uid=instance_uid,
            description=description,
            public_address=public_address,
            private_network_address=private_network_address,
            certificate_thumbprint=certificate_thumbprint,
            data_center_id=data_center_id,
            region_id=region_id,
            resource_id=resource_id,
        )

        public_cloud_aws_appliance.additional_properties = d
        return public_cloud_aws_appliance

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
