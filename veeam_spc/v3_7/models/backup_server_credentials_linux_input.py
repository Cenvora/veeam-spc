from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BackupServerCredentialsLinuxInput")


@_attrs_define
class BackupServerCredentialsLinuxInput:
    """
    Example:
        {'username': 'admin', 'password': 'Password1', 'description': 'Credentials for Alpha company administrator',
            'mappedOrganizationUid': '988c4583-5336-4e20-892d-eabcca0b34ac', 'sshPort': 22, 'autoElevated': True,
            'addToSudoers': True, 'useSu': False, 'privateKey': '-----BEGIN RSA PRIVATE KEY-----MIIEowIBAAKCAQEAmqsrgygo+hDx
            XAZVB6nyqAL/O8h+SQn/iVcW8wfCsqw7S9KMnRvEQ3PM7ULZvOFDKCoBt1j4kHELVm3HKRtqatEyqCPrB8gBZuTVsi14naNYL40qJqgCuMCsNRos
            oG6pSUEwddSQ2uELez3eDm/f0H0kuyMf3VRqz5o3mRo0Vujs+xhD8FXQYEuTvEANetdIlA8FrQQAlx0dxTKuKK1tYvbPqASP01eHmj/Vr/nKJX/B
            oZcSSSbEwpbqS4KlQHhlC0a7x/pfTurLwNKCQJWivhab6hCUanpttac3Hb2hQFdhymoI15j571i9yXam6Ul6i9qkW+M0x7m8Kd6lrOyVnwIDAQAB
            AoIBAFib+9+2IFOzZTNdhVVQre5HWUY8xOy/R6C9Pi6ZoZePSKFVzK0tfTFPpHXBONEXFMxr1HPgCvdlbCNl3RXV2Q+9LhJaEYpxsSvrqencVx+o
            txr2+tEOrBCAgagiiLKY828+Y679ysc66sL+XLtUqJrfNy3nH5hDhrXNGlEiTB4Fi85f4us4Iqzg3Wc2TdAL6GX8qGmzopHG2PWGjHVeVnPerBfL
            gXhEtZSng3B57LGs9KQzfOi9kie0Cso3e5yorky10Y4B7cd/hioI34PZMlfSsRuc0UfnQUAtLMiLCSFBejZbyvp8EW3sVLzN/Ho1aKbQWS7A9m0F
            KKddJyVptdECgYEAx+2WSjaOL9HQMgT+j9U0DfXY321m+F/IRfcDRIBE/4fVeB2sfS5k/4zvgXEAsmoclRea7S8d2gQ81yo87mQbfkseM1SeA7uQ
            zjOTPTiIcdNip/O5kDKUMszaMqckDAVflcD8M+F+mXdoLUgFH13S/UVRHZLJUoK1wP0RmIWqLQUCgYEAxgwM+m1hXfLPQi//D1aPk1ok3n1++aSC
            kzzucrMQ+pIZOnpE6x0EOBrccc9qkYzuDAj7VTJKhD39OD8+ZIIkICo1m9RVjfP/t+mgycBp4LaFsPaq7hhJOVhU7UvupnqJpOag3VUTKeUWtxbo
            zNS/KqZa1bTq/kCEr4d42wH4mVMCgYAC3hmFvvqTHQNLdF7iWUCB4sDVk5Aih90rg7t8RAq5T410R5itwviX4cGdra1A4dy/FrOWK1LWSbFFtMli
            8fSi/xjTy6bojswo6Px3qFPsrgeAOTK0KsWNZPrMNzGBKqKQV1BGvjk+okPQQnQwWvwnvdLIBc71bAKHXhnegixKsQKBgQC0pmFgPU3HaKhtc2Jx
            F0A35M4ktMyR4uHIdJf8wCIIriOdF9Kts/YZR0c1+UD4K1koWTkI6arXHcRQ/j9nZt6VCGuGDRVNOvhTRiSIY58wfs1MMnSQYk7IpC4zlkPGT5gm
            dsjdm7CzUmh58cfAr38A5GWO8kw4R5nAkw5Gl3GwSQKBgCgsVH+KxM4Y1jTyL+p/JK3roQ4wbFPQH3yTOYbQKUcLjzXY9yQ4OecoUoXjrbsaMn6u
            nRdoSgosxP9s4OoTHpUdUfWJhhjr3zvm6/tU3dPc+U0UbUf4DZvto+JzdSVqUtBQlo5T/yYK0OIhQakvHGunaeWnj4cUT86kFzTizeJT-----END
            RSA PRIVATE KEY-----', 'passphrase': 'Passphrase1', 'rootPassword': 'Rootpass1'}

    Attributes:
        username (str): User name.
        password (str | Unset): Password.
        description (str | Unset): Description of credentials.
        mapped_organization_uid (UUID | Unset): UID of a company to whom credentials must be assigned.
        ssh_port (int | Unset): SSH port used to connect to a Linux server. Default: 22.
        auto_elevated (bool | Unset): Indicates whether the account that owns credentials has permissions of a root
            user. Default: False.
        add_to_sudoers (bool | Unset): Indicates whether the account that owns credentials is added to the sudoers file.
            Default: False.
        use_su (bool | Unset): Indicates whether the `su` command is used for Linux distributions where the `sudo`
            command is not available. Default: False.
        private_key (str | Unset): Private key.
        passphrase (str | Unset): Passphrase for the private key.
        root_password (str | Unset): Password of a root account.
    """

    username: str
    password: str | Unset = UNSET
    description: str | Unset = UNSET
    mapped_organization_uid: UUID | Unset = UNSET
    ssh_port: int | Unset = 22
    auto_elevated: bool | Unset = False
    add_to_sudoers: bool | Unset = False
    use_su: bool | Unset = False
    private_key: str | Unset = UNSET
    passphrase: str | Unset = UNSET
    root_password: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        username = self.username

        password = self.password

        description = self.description

        mapped_organization_uid: str | Unset = UNSET
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
        mapped_organization_uid: UUID | Unset
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
