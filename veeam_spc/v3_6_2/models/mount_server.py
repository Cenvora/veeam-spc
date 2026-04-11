from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.backup_server_mount_server_type import BackupServerMountServerType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.backup_server_mount_server_options import BackupServerMountServerOptions


T = TypeVar("T", bound="MountServer")


@_attrs_define
class MountServer:
    """
    Attributes:
        id (UUID | Unset):
        type_ (BackupServerMountServerType | Unset): Mount server type.
        settings (BackupServerMountServerOptions | Unset):
        is_default (bool | None | Unset):
    """

    id: UUID | Unset = UNSET
    type_: BackupServerMountServerType | Unset = UNSET
    settings: BackupServerMountServerOptions | Unset = UNSET
    is_default: bool | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        settings: dict[str, Any] | Unset = UNSET
        if not isinstance(self.settings, Unset):
            settings = self.settings.to_dict()

        is_default: bool | None | Unset
        if isinstance(self.is_default, Unset):
            is_default = UNSET
        else:
            is_default = self.is_default

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if type_ is not UNSET:
            field_dict["type"] = type_
        if settings is not UNSET:
            field_dict["settings"] = settings
        if is_default is not UNSET:
            field_dict["isDefault"] = is_default

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.backup_server_mount_server_options import BackupServerMountServerOptions

        d = dict(src_dict)
        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id, Unset):
            id = UNSET
        else:
            id = UUID(_id)

        _type_ = d.pop("type", UNSET)
        type_: BackupServerMountServerType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = BackupServerMountServerType(_type_)

        _settings = d.pop("settings", UNSET)
        settings: BackupServerMountServerOptions | Unset
        if isinstance(_settings, Unset):
            settings = UNSET
        else:
            settings = BackupServerMountServerOptions.from_dict(_settings)

        def _parse_is_default(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_default = _parse_is_default(d.pop("isDefault", UNSET))

        mount_server = cls(
            id=id,
            type_=type_,
            settings=settings,
            is_default=is_default,
        )

        mount_server.additional_properties = d
        return mount_server

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
