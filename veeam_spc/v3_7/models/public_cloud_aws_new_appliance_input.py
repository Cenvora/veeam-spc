from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.public_cloud_aws_new_appliance_input_account import PublicCloudAwsNewApplianceInputAccount
    from ..models.public_cloud_aws_new_appliance_input_guest_os_credentials import (
        PublicCloudAwsNewApplianceInputGuestOsCredentials,
    )
    from ..models.public_cloud_aws_new_appliance_input_ip_address import PublicCloudAwsNewApplianceInputIpAddress
    from ..models.public_cloud_aws_new_appliance_input_network import PublicCloudAwsNewApplianceInputNetwork
    from ..models.public_cloud_aws_new_appliance_input_virtual_machine import (
        PublicCloudAwsNewApplianceInputVirtualMachine,
    )


T = TypeVar("T", bound="PublicCloudAwsNewApplianceInput")


@_attrs_define
class PublicCloudAwsNewApplianceInput:
    """
    Example:
        {'account': {'connectionUid': 'c0300e84-e8c0-40df-97f1-cbdbdcecafa9', 'accountUid':
            '73f86291-d5ff-423c-88da-9b60be21964d', 'dataCenterId': 'eu-central-1', 'regionId': 'Global'}, 'virtualMachine':
            {'virtualMachineName': 'dma12', 'description': 'Created at [1:19:55 PM] by [PortalAdministrator]'}, 'network':
            {'networkId': 'vpc-09ae9e55dd75a5f6b', 'subnetId': 'subnet-0b2131c783c96c1f9', 'securityGroupId':
            'sg-0ad0a345b8059c199'}, 'ipAddress': {'applianceIp': {'applianceIpAddressId': None, 'newIpAddressType':
            'dynamic'}, 'backupServerIpAddresses': '89.185.226.14/32'}, 'guestOsCredentials': {'guestOsCredentialsUid':
            '18f0a96a-16e1-4b27-ace3-307fd65da25a', 'keyPairName': 'VeeamDefaultKeyPair', 'timeZoneId': 'Europe/Prague'}}

    Attributes:
        account (PublicCloudAwsNewApplianceInputAccount):
        virtual_machine (PublicCloudAwsNewApplianceInputVirtualMachine):
        ip_address (PublicCloudAwsNewApplianceInputIpAddress):
        guest_os_credentials (PublicCloudAwsNewApplianceInputGuestOsCredentials):
        network (PublicCloudAwsNewApplianceInputNetwork | Unset): Veeam Backup for Public Clouds appliance network
            resources.
            >If you send the `null` value, all required resources will be created automatically.'
    """

    account: PublicCloudAwsNewApplianceInputAccount
    virtual_machine: PublicCloudAwsNewApplianceInputVirtualMachine
    ip_address: PublicCloudAwsNewApplianceInputIpAddress
    guest_os_credentials: PublicCloudAwsNewApplianceInputGuestOsCredentials
    network: PublicCloudAwsNewApplianceInputNetwork | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        account = self.account.to_dict()

        virtual_machine = self.virtual_machine.to_dict()

        ip_address = self.ip_address.to_dict()

        guest_os_credentials = self.guest_os_credentials.to_dict()

        network: dict[str, Any] | Unset = UNSET
        if not isinstance(self.network, Unset):
            network = self.network.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "account": account,
                "virtualMachine": virtual_machine,
                "ipAddress": ip_address,
                "guestOsCredentials": guest_os_credentials,
            }
        )
        if network is not UNSET:
            field_dict["network"] = network

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.public_cloud_aws_new_appliance_input_account import PublicCloudAwsNewApplianceInputAccount
        from ..models.public_cloud_aws_new_appliance_input_guest_os_credentials import (
            PublicCloudAwsNewApplianceInputGuestOsCredentials,
        )
        from ..models.public_cloud_aws_new_appliance_input_ip_address import PublicCloudAwsNewApplianceInputIpAddress
        from ..models.public_cloud_aws_new_appliance_input_network import PublicCloudAwsNewApplianceInputNetwork
        from ..models.public_cloud_aws_new_appliance_input_virtual_machine import (
            PublicCloudAwsNewApplianceInputVirtualMachine,
        )

        d = dict(src_dict)
        account = PublicCloudAwsNewApplianceInputAccount.from_dict(d.pop("account"))

        virtual_machine = PublicCloudAwsNewApplianceInputVirtualMachine.from_dict(d.pop("virtualMachine"))

        ip_address = PublicCloudAwsNewApplianceInputIpAddress.from_dict(d.pop("ipAddress"))

        guest_os_credentials = PublicCloudAwsNewApplianceInputGuestOsCredentials.from_dict(d.pop("guestOsCredentials"))

        _network = d.pop("network", UNSET)
        network: PublicCloudAwsNewApplianceInputNetwork | Unset
        if isinstance(_network, Unset):
            network = UNSET
        else:
            network = PublicCloudAwsNewApplianceInputNetwork.from_dict(_network)

        public_cloud_aws_new_appliance_input = cls(
            account=account,
            virtual_machine=virtual_machine,
            ip_address=ip_address,
            guest_os_credentials=guest_os_credentials,
            network=network,
        )

        public_cloud_aws_new_appliance_input.additional_properties = d
        return public_cloud_aws_new_appliance_input

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
