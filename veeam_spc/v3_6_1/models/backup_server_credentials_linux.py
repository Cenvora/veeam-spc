import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="BackupServerCredentialsLinux")


@_attrs_define
class BackupServerCredentialsLinux:
    """
    Attributes:
        username (str): User name.
        instance_uid (Union[Unset, UUID]): UID assigned to a credentials record.
        description (Union[None, Unset, str]): Description of credentials.
        creation_time (Union[Unset, datetime.datetime]): Date and time when credentials were created.
        ssh_port (Union[Unset, int]): SSH port used to connect to a Linux server. Default: 22.
        auto_elevated (Union[Unset, bool]): Indicates whether the account that owns credentials has permissions of a
            root user. Default: False.
        add_to_sudoers (Union[Unset, bool]): Indicates whether the account that owns credentials is added to the sudoers
            file. Default: False.
        use_su (Union[Unset, bool]): Indicates whether the `su` command is used for Linux distributions where the `sudo`
            command is not available. Default: False.
        private_key (Union[None, Unset, str]): Private key.
        passphrase (Union[None, Unset, str]): Passphrase for the private key.
        mapped_organization_uid (Union[None, UUID, Unset]): UID of a company to whom credentials are assigned.
        mapped_organization_name (Union[None, Unset, str]): Name of a company to whom credentials are assigned.
    """

    username: str
    instance_uid: Union[Unset, UUID] = UNSET
    description: Union[None, Unset, str] = UNSET
    creation_time: Union[Unset, datetime.datetime] = UNSET
    ssh_port: Union[Unset, int] = 22
    auto_elevated: Union[Unset, bool] = False
    add_to_sudoers: Union[Unset, bool] = False
    use_su: Union[Unset, bool] = False
    private_key: Union[None, Unset, str] = UNSET
    passphrase: Union[None, Unset, str] = UNSET
    mapped_organization_uid: Union[None, UUID, Unset] = UNSET
    mapped_organization_name: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        username = self.username

        instance_uid: Union[Unset, str] = UNSET
        if not isinstance(self.instance_uid, Unset):
            instance_uid = str(self.instance_uid)

        description: Union[None, Unset, str]
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        creation_time: Union[Unset, str] = UNSET
        if not isinstance(self.creation_time, Unset):
            creation_time = self.creation_time.isoformat()

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

        mapped_organization_uid: Union[None, Unset, str]
        if isinstance(self.mapped_organization_uid, Unset):
            mapped_organization_uid = UNSET
        elif isinstance(self.mapped_organization_uid, UUID):
            mapped_organization_uid = str(self.mapped_organization_uid)
        else:
            mapped_organization_uid = self.mapped_organization_uid

        mapped_organization_name: Union[None, Unset, str]
        if isinstance(self.mapped_organization_name, Unset):
            mapped_organization_name = UNSET
        else:
            mapped_organization_name = self.mapped_organization_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "username": username,
            }
        )
        if instance_uid is not UNSET:
            field_dict["instanceUid"] = instance_uid
        if description is not UNSET:
            field_dict["description"] = description
        if creation_time is not UNSET:
            field_dict["creationTime"] = creation_time
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
        if mapped_organization_uid is not UNSET:
            field_dict["mappedOrganizationUid"] = mapped_organization_uid
        if mapped_organization_name is not UNSET:
            field_dict["mappedOrganizationName"] = mapped_organization_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        username = d.pop("username")

        _instance_uid = d.pop("instanceUid", UNSET)
        instance_uid: Union[Unset, UUID]
        if isinstance(_instance_uid, Unset):
            instance_uid = UNSET
        else:
            instance_uid = UUID(_instance_uid)

        def _parse_description(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        description = _parse_description(d.pop("description", UNSET))

        _creation_time = d.pop("creationTime", UNSET)
        creation_time: Union[Unset, datetime.datetime]
        if isinstance(_creation_time, Unset):
            creation_time = UNSET
        else:
            creation_time = isoparse(_creation_time)

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

        def _parse_mapped_organization_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        mapped_organization_name = _parse_mapped_organization_name(d.pop("mappedOrganizationName", UNSET))

        backup_server_credentials_linux = cls(
            username=username,
            instance_uid=instance_uid,
            description=description,
            creation_time=creation_time,
            ssh_port=ssh_port,
            auto_elevated=auto_elevated,
            add_to_sudoers=add_to_sudoers,
            use_su=use_su,
            private_key=private_key,
            passphrase=passphrase,
            mapped_organization_uid=mapped_organization_uid,
            mapped_organization_name=mapped_organization_name,
        )

        backup_server_credentials_linux.additional_properties = d
        return backup_server_credentials_linux

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
