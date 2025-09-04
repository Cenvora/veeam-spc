from collections.abc import Mapping
from typing import Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.e_azure_environment_id_readonly import EAzureEnvironmentIdReadonly
from ..types import UNSET, Unset

T = TypeVar("T", bound="PublicCloudAzureAppliance")


@_attrs_define
class PublicCloudAzureAppliance:
    """
    Attributes:
        guest_os_credentials_uid (UUID): UID assigned to guest OS credentials record.
        account_uid (UUID): UID assigned to an account in Microsoft Azure.
        instance_uid (Union[Unset, UUID]): UID assigned to a Veeam Backup for Public Clouds appliance.
        management_agent_uid (Union[Unset, UUID]): UID assigned to management agent installed on a server where Veeam
            Backup for Public Clouds appliance is deployed.
        environment (Union[Unset, EAzureEnvironmentIdReadonly]): Type of a Microsoft Azure cloud environment.
        subscription_id (Union[Unset, str]): ID assigned to a Microsoft Azure subscription.
        tenant_id (Union[Unset, str]): ID assigned to a tenant available to a Microsoft Azure account.
        description (Union[Unset, str]): Description of a Veeam Backup for Public Clouds appliance.
        public_address (Union[Unset, str]): URL of a Veeam Backup for Public Clouds appliance.
        private_network_address (Union[Unset, str]): Private IP address or DNS name of a network.
        virtual_machine_id (Union[Unset, str]): ID assigned to a VM.
        certificate_thumbprint (Union[Unset, str]): Thumbprint of a security certificate.
        data_center_id (Union[Unset, str]): ID assigned to a Microsoft Azure datacenter
    """

    guest_os_credentials_uid: UUID
    account_uid: UUID
    instance_uid: Union[Unset, UUID] = UNSET
    management_agent_uid: Union[Unset, UUID] = UNSET
    environment: Union[Unset, EAzureEnvironmentIdReadonly] = UNSET
    subscription_id: Union[Unset, str] = UNSET
    tenant_id: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    public_address: Union[Unset, str] = UNSET
    private_network_address: Union[Unset, str] = UNSET
    virtual_machine_id: Union[Unset, str] = UNSET
    certificate_thumbprint: Union[Unset, str] = UNSET
    data_center_id: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        guest_os_credentials_uid = str(self.guest_os_credentials_uid)

        account_uid = str(self.account_uid)

        instance_uid: Union[Unset, str] = UNSET
        if not isinstance(self.instance_uid, Unset):
            instance_uid = str(self.instance_uid)

        management_agent_uid: Union[Unset, str] = UNSET
        if not isinstance(self.management_agent_uid, Unset):
            management_agent_uid = str(self.management_agent_uid)

        environment: Union[Unset, str] = UNSET
        if not isinstance(self.environment, Unset):
            environment = self.environment.value

        subscription_id = self.subscription_id

        tenant_id = self.tenant_id

        description = self.description

        public_address = self.public_address

        private_network_address = self.private_network_address

        virtual_machine_id = self.virtual_machine_id

        certificate_thumbprint = self.certificate_thumbprint

        data_center_id = self.data_center_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "guestOsCredentialsUid": guest_os_credentials_uid,
                "accountUid": account_uid,
            }
        )
        if instance_uid is not UNSET:
            field_dict["instanceUid"] = instance_uid
        if management_agent_uid is not UNSET:
            field_dict["managementAgentUid"] = management_agent_uid
        if environment is not UNSET:
            field_dict["environment"] = environment
        if subscription_id is not UNSET:
            field_dict["subscriptionId"] = subscription_id
        if tenant_id is not UNSET:
            field_dict["tenantId"] = tenant_id
        if description is not UNSET:
            field_dict["description"] = description
        if public_address is not UNSET:
            field_dict["publicAddress"] = public_address
        if private_network_address is not UNSET:
            field_dict["privateNetworkAddress"] = private_network_address
        if virtual_machine_id is not UNSET:
            field_dict["virtualMachineId"] = virtual_machine_id
        if certificate_thumbprint is not UNSET:
            field_dict["certificateThumbprint"] = certificate_thumbprint
        if data_center_id is not UNSET:
            field_dict["dataCenterId"] = data_center_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        guest_os_credentials_uid = UUID(d.pop("guestOsCredentialsUid"))

        account_uid = UUID(d.pop("accountUid"))

        _instance_uid = d.pop("instanceUid", UNSET)
        instance_uid: Union[Unset, UUID]
        if isinstance(_instance_uid, Unset):
            instance_uid = UNSET
        else:
            instance_uid = UUID(_instance_uid)

        _management_agent_uid = d.pop("managementAgentUid", UNSET)
        management_agent_uid: Union[Unset, UUID]
        if isinstance(_management_agent_uid, Unset):
            management_agent_uid = UNSET
        else:
            management_agent_uid = UUID(_management_agent_uid)

        _environment = d.pop("environment", UNSET)
        environment: Union[Unset, EAzureEnvironmentIdReadonly]
        if isinstance(_environment, Unset):
            environment = UNSET
        else:
            environment = EAzureEnvironmentIdReadonly(_environment)

        subscription_id = d.pop("subscriptionId", UNSET)

        tenant_id = d.pop("tenantId", UNSET)

        description = d.pop("description", UNSET)

        public_address = d.pop("publicAddress", UNSET)

        private_network_address = d.pop("privateNetworkAddress", UNSET)

        virtual_machine_id = d.pop("virtualMachineId", UNSET)

        certificate_thumbprint = d.pop("certificateThumbprint", UNSET)

        data_center_id = d.pop("dataCenterId", UNSET)

        public_cloud_azure_appliance = cls(
            guest_os_credentials_uid=guest_os_credentials_uid,
            account_uid=account_uid,
            instance_uid=instance_uid,
            management_agent_uid=management_agent_uid,
            environment=environment,
            subscription_id=subscription_id,
            tenant_id=tenant_id,
            description=description,
            public_address=public_address,
            private_network_address=private_network_address,
            virtual_machine_id=virtual_machine_id,
            certificate_thumbprint=certificate_thumbprint,
            data_center_id=data_center_id,
        )

        public_cloud_azure_appliance.additional_properties = d
        return public_cloud_azure_appliance

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
