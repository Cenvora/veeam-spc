from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.public_cloud_azure_add_existing_appliance_input_account import (
        PublicCloudAzureAddExistingApplianceInputAccount,
    )
    from ..models.public_cloud_azure_add_existing_appliance_input_guest_os_credentials import (
        PublicCloudAzureAddExistingApplianceInputGuestOsCredentials,
    )
    from ..models.public_cloud_azure_add_existing_appliance_input_network import (
        PublicCloudAzureAddExistingApplianceInputNetwork,
    )
    from ..models.public_cloud_azure_add_existing_appliance_input_virtual_machine import (
        PublicCloudAzureAddExistingApplianceInputVirtualMachine,
    )


T = TypeVar("T", bound="PublicCloudAzureAddExistingApplianceInput")


@_attrs_define
class PublicCloudAzureAddExistingApplianceInput:
    """
    Attributes:
        account (PublicCloudAzureAddExistingApplianceInputAccount):
        virtual_machine (PublicCloudAzureAddExistingApplianceInputVirtualMachine):
        guest_os_credentials (PublicCloudAzureAddExistingApplianceInputGuestOsCredentials):
        network (Union[Unset, PublicCloudAzureAddExistingApplianceInputNetwork]):
    """

    account: "PublicCloudAzureAddExistingApplianceInputAccount"
    virtual_machine: "PublicCloudAzureAddExistingApplianceInputVirtualMachine"
    guest_os_credentials: "PublicCloudAzureAddExistingApplianceInputGuestOsCredentials"
    network: Union[Unset, "PublicCloudAzureAddExistingApplianceInputNetwork"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        account = self.account.to_dict()

        virtual_machine = self.virtual_machine.to_dict()

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
                "guestOsCredentials": guest_os_credentials,
            }
        )
        if network is not UNSET:
            field_dict["network"] = network

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.public_cloud_azure_add_existing_appliance_input_account import (
            PublicCloudAzureAddExistingApplianceInputAccount,
        )
        from ..models.public_cloud_azure_add_existing_appliance_input_guest_os_credentials import (
            PublicCloudAzureAddExistingApplianceInputGuestOsCredentials,
        )
        from ..models.public_cloud_azure_add_existing_appliance_input_network import (
            PublicCloudAzureAddExistingApplianceInputNetwork,
        )
        from ..models.public_cloud_azure_add_existing_appliance_input_virtual_machine import (
            PublicCloudAzureAddExistingApplianceInputVirtualMachine,
        )

        d = dict(src_dict)
        account = PublicCloudAzureAddExistingApplianceInputAccount.from_dict(d.pop("account"))

        virtual_machine = PublicCloudAzureAddExistingApplianceInputVirtualMachine.from_dict(d.pop("virtualMachine"))

        guest_os_credentials = PublicCloudAzureAddExistingApplianceInputGuestOsCredentials.from_dict(
            d.pop("guestOsCredentials")
        )

        _network = d.pop("network", UNSET)
        network: Union[Unset, PublicCloudAzureAddExistingApplianceInputNetwork]
        if isinstance(_network, Unset):
            network = UNSET
        else:
            network = PublicCloudAzureAddExistingApplianceInputNetwork.from_dict(_network)

        public_cloud_azure_add_existing_appliance_input = cls(
            account=account,
            virtual_machine=virtual_machine,
            guest_os_credentials=guest_os_credentials,
            network=network,
        )

        public_cloud_azure_add_existing_appliance_input.additional_properties = d
        return public_cloud_azure_add_existing_appliance_input

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
