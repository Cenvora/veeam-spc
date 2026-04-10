from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PublicCloudGoogleAppliance")


@_attrs_define
class PublicCloudGoogleAppliance:
    """
    Attributes:
        account_uid (UUID): UID assigned to a Google Cloud account used to access a Veeam Backup for Google Cloud
            appliance.
        guest_os_credentials_uid (UUID): UID assigned to guest OS credentials record.
        instance_uid (Union[Unset, UUID]): UID assigned to a Veeam Backup for Google Cloud appliance.
        name (Union[Unset, str]): Name of a Veeam Backup for Google Cloud appliance.
        description (Union[None, Unset, str]): Description of a Veeam Backup for Google Cloud appliance.
        management_agent_uid (Union[Unset, UUID]): UID assigned to management agent installed on a Veeam Backup for
            Google Cloud appliance server.
        certificate_thumbprint (Union[Unset, str]): Thumbprint of a security certificate.
        public_address (Union[Unset, str]): IP address or DNS name of a Veeam Backup for Google Cloud appliance.
        private_network_address (Union[None, Unset, str]): Private IP address or DNS name of a Google Cloud network.
        virtual_machine_id (Union[Unset, str]): ID assigned to a VM on which a Veeam Backup for Google Cloud appliance
            is deployed.
        data_center_id (Union[Unset, str]): ID assigned to a Google Cloud datacenter.
        availability_zone_id (Union[Unset, str]): ID assigned to an availability zone.
    """

    account_uid: UUID
    guest_os_credentials_uid: UUID
    instance_uid: Union[Unset, UUID] = UNSET
    name: Union[Unset, str] = UNSET
    description: Union[None, Unset, str] = UNSET
    management_agent_uid: Union[Unset, UUID] = UNSET
    certificate_thumbprint: Union[Unset, str] = UNSET
    public_address: Union[Unset, str] = UNSET
    private_network_address: Union[None, Unset, str] = UNSET
    virtual_machine_id: Union[Unset, str] = UNSET
    data_center_id: Union[Unset, str] = UNSET
    availability_zone_id: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        account_uid = str(self.account_uid)

        guest_os_credentials_uid = str(self.guest_os_credentials_uid)

        instance_uid: Union[Unset, str] = UNSET
        if not isinstance(self.instance_uid, Unset):
            instance_uid = str(self.instance_uid)

        name = self.name

        description: Union[None, Unset, str]
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        management_agent_uid: Union[Unset, str] = UNSET
        if not isinstance(self.management_agent_uid, Unset):
            management_agent_uid = str(self.management_agent_uid)

        certificate_thumbprint = self.certificate_thumbprint

        public_address = self.public_address

        private_network_address: Union[None, Unset, str]
        if isinstance(self.private_network_address, Unset):
            private_network_address = UNSET
        else:
            private_network_address = self.private_network_address

        virtual_machine_id = self.virtual_machine_id

        data_center_id = self.data_center_id

        availability_zone_id = self.availability_zone_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "accountUid": account_uid,
                "guestOsCredentialsUid": guest_os_credentials_uid,
            }
        )
        if instance_uid is not UNSET:
            field_dict["instanceUid"] = instance_uid
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if management_agent_uid is not UNSET:
            field_dict["managementAgentUid"] = management_agent_uid
        if certificate_thumbprint is not UNSET:
            field_dict["certificateThumbprint"] = certificate_thumbprint
        if public_address is not UNSET:
            field_dict["publicAddress"] = public_address
        if private_network_address is not UNSET:
            field_dict["privateNetworkAddress"] = private_network_address
        if virtual_machine_id is not UNSET:
            field_dict["virtualMachineId"] = virtual_machine_id
        if data_center_id is not UNSET:
            field_dict["dataCenterId"] = data_center_id
        if availability_zone_id is not UNSET:
            field_dict["availabilityZoneId"] = availability_zone_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        account_uid = UUID(d.pop("accountUid"))

        guest_os_credentials_uid = UUID(d.pop("guestOsCredentialsUid"))

        _instance_uid = d.pop("instanceUid", UNSET)
        instance_uid: Union[Unset, UUID]
        if isinstance(_instance_uid, Unset):
            instance_uid = UNSET
        else:
            instance_uid = UUID(_instance_uid)

        name = d.pop("name", UNSET)

        def _parse_description(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        description = _parse_description(d.pop("description", UNSET))

        _management_agent_uid = d.pop("managementAgentUid", UNSET)
        management_agent_uid: Union[Unset, UUID]
        if isinstance(_management_agent_uid, Unset):
            management_agent_uid = UNSET
        else:
            management_agent_uid = UUID(_management_agent_uid)

        certificate_thumbprint = d.pop("certificateThumbprint", UNSET)

        public_address = d.pop("publicAddress", UNSET)

        def _parse_private_network_address(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        private_network_address = _parse_private_network_address(d.pop("privateNetworkAddress", UNSET))

        virtual_machine_id = d.pop("virtualMachineId", UNSET)

        data_center_id = d.pop("dataCenterId", UNSET)

        availability_zone_id = d.pop("availabilityZoneId", UNSET)

        public_cloud_google_appliance = cls(
            account_uid=account_uid,
            guest_os_credentials_uid=guest_os_credentials_uid,
            instance_uid=instance_uid,
            name=name,
            description=description,
            management_agent_uid=management_agent_uid,
            certificate_thumbprint=certificate_thumbprint,
            public_address=public_address,
            private_network_address=private_network_address,
            virtual_machine_id=virtual_machine_id,
            data_center_id=data_center_id,
            availability_zone_id=availability_zone_id,
        )

        public_cloud_google_appliance.additional_properties = d
        return public_cloud_google_appliance

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
