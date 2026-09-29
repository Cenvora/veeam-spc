from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.linux_discovery_credentials_type import LinuxDiscoveryCredentialsType
from ..types import UNSET, Unset

T = TypeVar("T", bound="LinuxDiscoveryCredentials")


@_attrs_define
class LinuxDiscoveryCredentials:
    """
    Attributes:
        username (str): User name.
        type_ (LinuxDiscoveryCredentialsType): Type of Linux credentials.
        instance_uid (UUID | Unset): UID assigned to a credentials record.
        password (None | str | Unset): Password.
        priority (int | Unset): Priority level of credentials. Default: 0.
        description (None | str | Unset): Credentials description.
        ssh_port (int | Unset): SSH port that must be used to connect to a Linux server. Default: 22.
        elevate_account_privileges (bool | Unset): Indicates whether a non-root account must be provided with root
            account privileges. Default: False.
        add_account_to_sudoers_file (bool | Unset): Indicates whether an account must be added to sudoers file. Default:
            False.
        use_su_ifsudo_fails (bool | Unset): Indicates whether the `su` command can be used instead of the `sudo`
            command. Default: False.
        root_password (None | str | Unset): Password for a root account.
        ssh_private_key (None | str | Unset): SSH private key.
        passphrase (None | str | Unset): Passphrase for the private key.
    """

    username: str
    type_: LinuxDiscoveryCredentialsType
    instance_uid: UUID | Unset = UNSET
    password: None | str | Unset = UNSET
    priority: int | Unset = 0
    description: None | str | Unset = UNSET
    ssh_port: int | Unset = 22
    elevate_account_privileges: bool | Unset = False
    add_account_to_sudoers_file: bool | Unset = False
    use_su_ifsudo_fails: bool | Unset = False
    root_password: None | str | Unset = UNSET
    ssh_private_key: None | str | Unset = UNSET
    passphrase: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        username = self.username

        type_ = self.type_.value

        instance_uid: str | Unset = UNSET
        if not isinstance(self.instance_uid, Unset):
            instance_uid = str(self.instance_uid)

        password: None | str | Unset
        if isinstance(self.password, Unset):
            password = UNSET
        else:
            password = self.password

        priority = self.priority

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        ssh_port = self.ssh_port

        elevate_account_privileges = self.elevate_account_privileges

        add_account_to_sudoers_file = self.add_account_to_sudoers_file

        use_su_ifsudo_fails = self.use_su_ifsudo_fails

        root_password: None | str | Unset
        if isinstance(self.root_password, Unset):
            root_password = UNSET
        else:
            root_password = self.root_password

        ssh_private_key: None | str | Unset
        if isinstance(self.ssh_private_key, Unset):
            ssh_private_key = UNSET
        else:
            ssh_private_key = self.ssh_private_key

        passphrase: None | str | Unset
        if isinstance(self.passphrase, Unset):
            passphrase = UNSET
        else:
            passphrase = self.passphrase

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "username": username,
                "type": type_,
            }
        )
        if instance_uid is not UNSET:
            field_dict["instanceUid"] = instance_uid
        if password is not UNSET:
            field_dict["password"] = password
        if priority is not UNSET:
            field_dict["priority"] = priority
        if description is not UNSET:
            field_dict["description"] = description
        if ssh_port is not UNSET:
            field_dict["sshPort"] = ssh_port
        if elevate_account_privileges is not UNSET:
            field_dict["elevateAccountPrivileges"] = elevate_account_privileges
        if add_account_to_sudoers_file is not UNSET:
            field_dict["addAccountToSudoersFile"] = add_account_to_sudoers_file
        if use_su_ifsudo_fails is not UNSET:
            field_dict["useSuIfsudoFails"] = use_su_ifsudo_fails
        if root_password is not UNSET:
            field_dict["rootPassword"] = root_password
        if ssh_private_key is not UNSET:
            field_dict["sshPrivateKey"] = ssh_private_key
        if passphrase is not UNSET:
            field_dict["passphrase"] = passphrase

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        username = d.pop("username")

        type_ = LinuxDiscoveryCredentialsType(d.pop("type"))

        _instance_uid = d.pop("instanceUid", UNSET)
        instance_uid: UUID | Unset
        if isinstance(_instance_uid, Unset):
            instance_uid = UNSET
        else:
            instance_uid = UUID(_instance_uid)

        def _parse_password(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        password = _parse_password(d.pop("password", UNSET))

        priority = d.pop("priority", UNSET)

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        ssh_port = d.pop("sshPort", UNSET)

        elevate_account_privileges = d.pop("elevateAccountPrivileges", UNSET)

        add_account_to_sudoers_file = d.pop("addAccountToSudoersFile", UNSET)

        use_su_ifsudo_fails = d.pop("useSuIfsudoFails", UNSET)

        def _parse_root_password(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        root_password = _parse_root_password(d.pop("rootPassword", UNSET))

        def _parse_ssh_private_key(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ssh_private_key = _parse_ssh_private_key(d.pop("sshPrivateKey", UNSET))

        def _parse_passphrase(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        passphrase = _parse_passphrase(d.pop("passphrase", UNSET))

        linux_discovery_credentials = cls(
            username=username,
            type_=type_,
            instance_uid=instance_uid,
            password=password,
            priority=priority,
            description=description,
            ssh_port=ssh_port,
            elevate_account_privileges=elevate_account_privileges,
            add_account_to_sudoers_file=add_account_to_sudoers_file,
            use_su_ifsudo_fails=use_su_ifsudo_fails,
            root_password=root_password,
            ssh_private_key=ssh_private_key,
            passphrase=passphrase,
        )

        linux_discovery_credentials.additional_properties = d
        return linux_discovery_credentials

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
