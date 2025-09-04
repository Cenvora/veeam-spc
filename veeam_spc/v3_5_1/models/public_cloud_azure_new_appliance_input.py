from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.public_cloud_azure_new_appliance_input_account import PublicCloudAzureNewApplianceInputAccount
    from ..models.public_cloud_azure_new_appliance_input_guest_os_credentials import (
        PublicCloudAzureNewApplianceInputGuestOsCredentials,
    )
    from ..models.public_cloud_azure_new_appliance_input_ip_address import PublicCloudAzureNewApplianceInputIpAddress
    from ..models.public_cloud_azure_new_appliance_input_network import PublicCloudAzureNewApplianceInputNetwork
    from ..models.public_cloud_azure_new_appliance_input_virtual_machine import (
        PublicCloudAzureNewApplianceInputVirtualMachine,
    )


T = TypeVar("T", bound="PublicCloudAzureNewApplianceInput")


@_attrs_define
class PublicCloudAzureNewApplianceInput:
    """
    Attributes:
        account (PublicCloudAzureNewApplianceInputAccount):
        virtual_machine (PublicCloudAzureNewApplianceInputVirtualMachine):
        ip_address (PublicCloudAzureNewApplianceInputIpAddress):
        guest_os_credentials (PublicCloudAzureNewApplianceInputGuestOsCredentials):
        network (Union[Unset, PublicCloudAzureNewApplianceInputNetwork]): Veeam Backup for Public Clouds appliance
            network resources.
            >If you send the `null` value, all required resources will be created automatically.
    """

    account: "PublicCloudAzureNewApplianceInputAccount"
    virtual_machine: "PublicCloudAzureNewApplianceInputVirtualMachine"
    ip_address: "PublicCloudAzureNewApplianceInputIpAddress"
    guest_os_credentials: "PublicCloudAzureNewApplianceInputGuestOsCredentials"
    network: Union[Unset, "PublicCloudAzureNewApplianceInputNetwork"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        account = self.account.to_dict()

        virtual_machine = self.virtual_machine.to_dict()

        ip_address = self.ip_address.to_dict()

        guest_os_credentials = self.guest_os_credentials.to_dict()

        network: Union[Unset, dict[str, Any]] = UNSET
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
        from ..models.public_cloud_azure_new_appliance_input_account import PublicCloudAzureNewApplianceInputAccount
        from ..models.public_cloud_azure_new_appliance_input_guest_os_credentials import (
            PublicCloudAzureNewApplianceInputGuestOsCredentials,
        )
        from ..models.public_cloud_azure_new_appliance_input_ip_address import (
            PublicCloudAzureNewApplianceInputIpAddress,
        )
        from ..models.public_cloud_azure_new_appliance_input_network import PublicCloudAzureNewApplianceInputNetwork
        from ..models.public_cloud_azure_new_appliance_input_virtual_machine import (
            PublicCloudAzureNewApplianceInputVirtualMachine,
        )

        d = dict(src_dict)
        account = PublicCloudAzureNewApplianceInputAccount.from_dict(d.pop("account"))

        virtual_machine = PublicCloudAzureNewApplianceInputVirtualMachine.from_dict(d.pop("virtualMachine"))

        ip_address = PublicCloudAzureNewApplianceInputIpAddress.from_dict(d.pop("ipAddress"))

        guest_os_credentials = PublicCloudAzureNewApplianceInputGuestOsCredentials.from_dict(
            d.pop("guestOsCredentials")
        )

        _network = d.pop("network", UNSET)
        network: Union[Unset, PublicCloudAzureNewApplianceInputNetwork]
        if isinstance(_network, Unset):
            network = UNSET
        else:
            network = PublicCloudAzureNewApplianceInputNetwork.from_dict(_network)

        public_cloud_azure_new_appliance_input = cls(
            account=account,
            virtual_machine=virtual_machine,
            ip_address=ip_address,
            guest_os_credentials=guest_os_credentials,
            network=network,
        )

        public_cloud_azure_new_appliance_input.additional_properties = d
        return public_cloud_azure_new_appliance_input

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
