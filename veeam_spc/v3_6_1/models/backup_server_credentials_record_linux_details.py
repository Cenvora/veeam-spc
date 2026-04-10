from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BackupServerCredentialsRecordLinuxDetails")


@_attrs_define
class BackupServerCredentialsRecordLinuxDetails:
    """Details of credentials used to access Linux computers.

    Attributes:
        ssh_port (Union[Unset, int]): SSH port used to connect to a Linux server. Default: 22.
        auto_elevated (Union[Unset, bool]): Indicates whether the account that owns credentials has permissions of a
            root user. Default: False.
        add_to_sudoers (Union[Unset, bool]): Indicates whether the account that owns credentials is added to the sudoers
            file. Default: False.
        use_su (Union[Unset, bool]): Indicates whether the `su` command is used for Linux distributions where the `sudo`
            command is not available. Default: False.
        private_key (Union[None, Unset, str]): Private key.
        passphrase (Union[None, Unset, str]): Passphrase for the private key.
    """

    ssh_port: Union[Unset, int] = 22
    auto_elevated: Union[Unset, bool] = False
    add_to_sudoers: Union[Unset, bool] = False
    use_su: Union[Unset, bool] = False
    private_key: Union[None, Unset, str] = UNSET
    passphrase: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ssh_port = self.ssh_port

        auto_elevated = self.auto_elevated

        add_to_sudoers = self.add_to_sudoers

        use_su = self.use_su

        private_key: Union[None, Unset, str]
        if isinstance(self.private_key, Unset):
            private_key = UNSET
        else:
            private_key = self.private_key

        passphrase: Union[None, Unset, str]
        if isinstance(self.passphrase, Unset):
            passphrase = UNSET
        else:
            passphrase = self.passphrase

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ssh_port is not UNSET:
            field_dict["sshPort"] = ssh_port
        if auto_elevated is not UNSET:
            field_dict["autoElevated"] = auto_elevated
        if add_to_sudoers is not UNSET:
            field_dict["addToSudoers"] = add_to_sudoers
        if use_su is not UNSET:
            field_dict["useSu"] = use_su
        if private_key is not UNSET:
            field_dict["privateKey"] = private_key
        if passphrase is not UNSET:
            field_dict["passphrase"] = passphrase

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        ssh_port = d.pop("sshPort", UNSET)

        auto_elevated = d.pop("autoElevated", UNSET)

        add_to_sudoers = d.pop("addToSudoers", UNSET)

        use_su = d.pop("useSu", UNSET)

        def _parse_private_key(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        private_key = _parse_private_key(d.pop("privateKey", UNSET))

        def _parse_passphrase(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        passphrase = _parse_passphrase(d.pop("passphrase", UNSET))

        backup_server_credentials_record_linux_details = cls(
            ssh_port=ssh_port,
            auto_elevated=auto_elevated,
            add_to_sudoers=add_to_sudoers,
            use_su=use_su,
            private_key=private_key,
            passphrase=passphrase,
        )

        backup_server_credentials_record_linux_details.additional_properties = d
        return backup_server_credentials_record_linux_details

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
