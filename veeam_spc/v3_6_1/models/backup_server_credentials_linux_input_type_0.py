from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BackupServerCredentialsLinuxInputType0")


@_attrs_define
class BackupServerCredentialsLinuxInputType0:
    """
    Attributes:
        username (str): User name.
        password (Union[None, Unset, str]): Password.
        description (Union[None, Unset, str]): Description of credentials.
        mapped_organization_uid (Union[None, UUID, Unset]): UID of a company to whom credentials must be assigned.
        ssh_port (Union[Unset, int]): SSH port used to connect to a Linux server. Default: 22.
        auto_elevated (Union[Unset, bool]): Indicates whether the account that owns credentials has permissions of a
            root user. Default: False.
        add_to_sudoers (Union[Unset, bool]): Indicates whether the account that owns credentials is added to the sudoers
            file. Default: False.
        use_su (Union[Unset, bool]): Indicates whether the `su` command is used for Linux distributions where the `sudo`
            command is not available. Default: False.
        private_key (Union[None, Unset, str]): Private key.
        passphrase (Union[None, Unset, str]): Passphrase for the private key.
        root_password (Union[None, Unset, str]): Password of a root account.
    """

    username: str
    password: Union[None, Unset, str] = UNSET
    description: Union[None, Unset, str] = UNSET
    mapped_organization_uid: Union[None, UUID, Unset] = UNSET
    ssh_port: Union[Unset, int] = 22
    auto_elevated: Union[Unset, bool] = False
    add_to_sudoers: Union[Unset, bool] = False
    use_su: Union[Unset, bool] = False
    private_key: Union[None, Unset, str] = UNSET
    passphrase: Union[None, Unset, str] = UNSET
    root_password: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        username = self.username

        password: Union[None, Unset, str]
        if isinstance(self.password, Unset):
            password = UNSET
        else:
            password = self.password

        description: Union[None, Unset, str]
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        mapped_organization_uid: Union[None, Unset, str]
        if isinstance(self.mapped_organization_uid, Unset):
            mapped_organization_uid = UNSET
        elif isinstance(self.mapped_organization_uid, UUID):
            mapped_organization_uid = str(self.mapped_organization_uid)
        else:
            mapped_organization_uid = self.mapped_organization_uid

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

        root_password: Union[None, Unset, str]
        if isinstance(self.root_password, Unset):
            root_password = UNSET
        else:
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

        def _parse_password(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        password = _parse_password(d.pop("password", UNSET))

        def _parse_description(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_mapped_organization_uid(data: object) -> Union[None, UUID, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                mapped_organization_uid_type_0 = UUID(data)

                return mapped_organization_uid_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID, Unset], data)

        mapped_organization_uid = _parse_mapped_organization_uid(d.pop("mappedOrganizationUid", UNSET))

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

        def _parse_root_password(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        root_password = _parse_root_password(d.pop("rootPassword", UNSET))

        backup_server_credentials_linux_input_type_0 = cls(
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

        backup_server_credentials_linux_input_type_0.additional_properties = d
        return backup_server_credentials_linux_input_type_0

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
