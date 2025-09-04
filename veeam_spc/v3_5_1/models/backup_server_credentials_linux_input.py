from collections.abc import Mapping
from typing import Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BackupServerCredentialsLinuxInput")


@_attrs_define
class BackupServerCredentialsLinuxInput:
    """
    Attributes:
        username (str): User name.
        password (Union[Unset, str]): Password.
        description (Union[Unset, str]): Description of credentials.
        mapped_organization_uid (Union[Unset, UUID]): UID of a company to whom credentials must be assigned.
        ssh_port (Union[Unset, int]): SSH port used to connect to a Linux server. Default: 22.
        auto_elevated (Union[Unset, bool]): Indicates whether the account that owns credentials has permissions of a
            root user. Default: False.
        add_to_sudoers (Union[Unset, bool]): Indicates whether the account that owns credentials is added to the sudoers
            file. Default: False.
        use_su (Union[Unset, bool]): Indicates whether the `su` command is used for Linux distributions where the `sudo`
            command is not available. Default: False.
        private_key (Union[Unset, str]): Private key.
        passphrase (Union[Unset, str]): Passphrase for the private key.
        root_password (Union[Unset, str]): Password of a root account.
    """

    username: str
    password: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    mapped_organization_uid: Union[Unset, UUID] = UNSET
    ssh_port: Union[Unset, int] = 22
    auto_elevated: Union[Unset, bool] = False
    add_to_sudoers: Union[Unset, bool] = False
    use_su: Union[Unset, bool] = False
    private_key: Union[Unset, str] = UNSET
    passphrase: Union[Unset, str] = UNSET
    root_password: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        username = self.username

        password = self.password

        description = self.description

        mapped_organization_uid: Union[Unset, str] = UNSET
        if not isinstance(self.mapped_organization_uid, Unset):
            mapped_organization_uid = str(self.mapped_organization_uid)

        ssh_port = self.ssh_port

        auto_elevated = self.auto_elevated

        add_to_sudoers = self.add_to_sudoers

        use_su = self.use_su

        private_key = self.private_key

        passphrase = self.passphrase

        root_password = self.root_password

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "username": username,
            }
        )
        if password is not UNSET:
            field_dict["password"] = password
        if description is not UNSET:
            field_dict["description"] = description
        if mapped_organization_uid is not UNSET:
            field_dict["mappedOrganizationUid"] = mapped_organization_uid
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
        if root_password is not UNSET:
            field_dict["rootPassword"] = root_password

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        username = d.pop("username")

        password = d.pop("password", UNSET)

        description = d.pop("description", UNSET)

        _mapped_organization_uid = d.pop("mappedOrganizationUid", UNSET)
        mapped_organization_uid: Union[Unset, UUID]
        if isinstance(_mapped_organization_uid, Unset):
            mapped_organization_uid = UNSET
        else:
            mapped_organization_uid = UUID(_mapped_organization_uid)

        ssh_port = d.pop("sshPort", UNSET)

        auto_elevated = d.pop("autoElevated", UNSET)

        add_to_sudoers = d.pop("addToSudoers", UNSET)

        use_su = d.pop("useSu", UNSET)

        private_key = d.pop("privateKey", UNSET)

        passphrase = d.pop("passphrase", UNSET)

        root_password = d.pop("rootPassword", UNSET)

        backup_server_credentials_linux_input = cls(
            username=username,
            password=password,
            description=description,
            mapped_organization_uid=mapped_organization_uid,
            ssh_port=ssh_port,
            auto_elevated=auto_elevated,
            add_to_sudoers=add_to_sudoers,
            use_su=use_su,
            private_key=private_key,
            passphrase=passphrase,
            root_password=root_password,
        )

        backup_server_credentials_linux_input.additional_properties = d
        return backup_server_credentials_linux_input

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
