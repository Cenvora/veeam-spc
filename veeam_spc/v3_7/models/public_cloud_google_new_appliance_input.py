from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.public_cloud_google_new_appliance_input_account import PublicCloudGoogleNewApplianceInputAccount
    from ..models.public_cloud_google_new_appliance_input_guest_os_credentials import (
        PublicCloudGoogleNewApplianceInputGuestOsCredentials,
    )
    from ..models.public_cloud_google_new_appliance_input_ip_address import PublicCloudGoogleNewApplianceInputIpAddress
    from ..models.public_cloud_google_new_appliance_input_network_type_0 import (
        PublicCloudGoogleNewApplianceInputNetworkType0,
    )
    from ..models.public_cloud_google_new_appliance_input_virtual_machine import (
        PublicCloudGoogleNewApplianceInputVirtualMachine,
    )


T = TypeVar("T", bound="PublicCloudGoogleNewApplianceInput")


@_attrs_define
class PublicCloudGoogleNewApplianceInput:
    """
    Example:
        {'account': {'accountUid': '69d70dc2-25d4-4e82-a0fc-d89c1d847ec7', 'dataCenterId': 'europe4',
            'availabilityZoneId': 'europe4-a'}, 'virtualMachine': {'virtualMachineName': 'vba1', 'description': 'Backup
            appliance VM'}, 'network': None, 'ipAddress': {'applianceIp': {'applianceIpAddressId': '34.90.208.126',
            'newIpAddressType': 'dynamic'}, 'backupServerIpAddresses': '172.24.147.188'}, 'guestOsCredentials':
            {'guestOsCredentialsUid': '9d8ac737-5ca0-44b8-8195-890a66f93606', 'sshPublicKey': '-----BEGIN PUBLIC KEY-----MII
            BIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAsUyvEXIzY2iHzUwtNCUTUDEGeEaWt667b8tbbehcmJmieP42T5bh0lIWvET9h03LGutYD4f
            0lH74EihHaBHt45B4ei9EiJGATPgLfdc4MOsiQcbf6HjrkuVzru4SDnesUEkDYczXNh/int7Uvuhafv0hKu3ZOfQPtPmJKBc+fQCBt6ZgSxQ1BqO
            R+p8MCkxxVr4zUphsQCU+2kCWzilyPlFHSKtb/JggDGMnLiZiY1MnU1FkC4rTY2COlcNzq8+PtEF6BuAO1L1788eh+h2oesG78kttuNmtTrXFlaC
            FzwOGmoKg2aAPIJVYNt5V3Vevm9kzcx5BAjeiKUZipGH8XQIDAQAB-----END PUBLIC KEY-----', 'timeZoneId': 'Pacific Standard
            Time'}}

    Attributes:
        account (PublicCloudGoogleNewApplianceInputAccount):
        virtual_machine (PublicCloudGoogleNewApplianceInputVirtualMachine):
        ip_address (PublicCloudGoogleNewApplianceInputIpAddress):
        guest_os_credentials (PublicCloudGoogleNewApplianceInputGuestOsCredentials):
        network (None | PublicCloudGoogleNewApplianceInputNetworkType0 | Unset): Veeam Backup for Google Cloud appliance
            network resources.
            > If you provide the `null` value, all required resources will be created automatically.
    """

    account: PublicCloudGoogleNewApplianceInputAccount
    virtual_machine: PublicCloudGoogleNewApplianceInputVirtualMachine
    ip_address: PublicCloudGoogleNewApplianceInputIpAddress
    guest_os_credentials: PublicCloudGoogleNewApplianceInputGuestOsCredentials
    network: None | PublicCloudGoogleNewApplianceInputNetworkType0 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.public_cloud_google_new_appliance_input_network_type_0 import (
            PublicCloudGoogleNewApplianceInputNetworkType0,
        )

        account = self.account.to_dict()

        virtual_machine = self.virtual_machine.to_dict()

        ip_address = self.ip_address.to_dict()

        guest_os_credentials = self.guest_os_credentials.to_dict()

        network: dict[str, Any] | None | Unset
        if isinstance(self.network, Unset):
            network = UNSET
        elif isinstance(self.network, PublicCloudGoogleNewApplianceInputNetworkType0):
            network = self.network.to_dict()
        else:
            network = self.network

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
        from ..models.public_cloud_google_new_appliance_input_account import PublicCloudGoogleNewApplianceInputAccount
        from ..models.public_cloud_google_new_appliance_input_guest_os_credentials import (
            PublicCloudGoogleNewApplianceInputGuestOsCredentials,
        )
        from ..models.public_cloud_google_new_appliance_input_ip_address import (
            PublicCloudGoogleNewApplianceInputIpAddress,
        )
        from ..models.public_cloud_google_new_appliance_input_network_type_0 import (
            PublicCloudGoogleNewApplianceInputNetworkType0,
        )
        from ..models.public_cloud_google_new_appliance_input_virtual_machine import (
            PublicCloudGoogleNewApplianceInputVirtualMachine,
        )

        d = dict(src_dict)
        account = PublicCloudGoogleNewApplianceInputAccount.from_dict(d.pop("account"))

        virtual_machine = PublicCloudGoogleNewApplianceInputVirtualMachine.from_dict(d.pop("virtualMachine"))

        ip_address = PublicCloudGoogleNewApplianceInputIpAddress.from_dict(d.pop("ipAddress"))

        guest_os_credentials = PublicCloudGoogleNewApplianceInputGuestOsCredentials.from_dict(
            d.pop("guestOsCredentials")
        )

        def _parse_network(data: object) -> None | PublicCloudGoogleNewApplianceInputNetworkType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                network_type_0 = PublicCloudGoogleNewApplianceInputNetworkType0.from_dict(data)

                return network_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | PublicCloudGoogleNewApplianceInputNetworkType0 | Unset, data)

        network = _parse_network(d.pop("network", UNSET))

        public_cloud_google_new_appliance_input = cls(
            account=account,
            virtual_machine=virtual_machine,
            ip_address=ip_address,
            guest_os_credentials=guest_os_credentials,
            network=network,
        )

        public_cloud_google_new_appliance_input.additional_properties = d
        return public_cloud_google_new_appliance_input

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
