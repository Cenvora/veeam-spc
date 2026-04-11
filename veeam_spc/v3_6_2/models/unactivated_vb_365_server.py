from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.unactivated_vb_365_server_status import UnactivatedVb365ServerStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="UnactivatedVb365Server")


@_attrs_define
class UnactivatedVb365Server:
    """
    Attributes:
        unique_uid (None | Unset | UUID): Temporary UID assigned to an unactivated Veeam Backup for Microsoft 365
            server.
        location_uid (UUID | Unset): UID assigned to a Veeam Backup for Microsoft 365 server location.
        organization_uid (UUID | Unset): UID assigned to an organization.
        management_agent_uid (UUID | Unset): UID assigned to a management agent installed on a Veeam Backup for
            Microsoft 365 Server.
        name (str | Unset): Host name of a Veeam Backup for Microsoft 365 server.
        version (str | Unset): Veeam Backup for Microsoft 365 version installed on a server.
        status (UnactivatedVb365ServerStatus | Unset): Veeam Backup for Microsoft 365 server status.
    """

    unique_uid: None | Unset | UUID = UNSET
    location_uid: UUID | Unset = UNSET
    organization_uid: UUID | Unset = UNSET
    management_agent_uid: UUID | Unset = UNSET
    name: str | Unset = UNSET
    version: str | Unset = UNSET
    status: UnactivatedVb365ServerStatus | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        unique_uid: None | str | Unset
        if isinstance(self.unique_uid, Unset):
            unique_uid = UNSET
        elif isinstance(self.unique_uid, UUID):
            unique_uid = str(self.unique_uid)
        else:
            unique_uid = self.unique_uid

        location_uid: str | Unset = UNSET
        if not isinstance(self.location_uid, Unset):
            location_uid = str(self.location_uid)

        organization_uid: str | Unset = UNSET
        if not isinstance(self.organization_uid, Unset):
            organization_uid = str(self.organization_uid)

        management_agent_uid: str | Unset = UNSET
        if not isinstance(self.management_agent_uid, Unset):
            management_agent_uid = str(self.management_agent_uid)

        name = self.name

        version = self.version

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if unique_uid is not UNSET:
            field_dict["uniqueUid"] = unique_uid
        if location_uid is not UNSET:
            field_dict["locationUid"] = location_uid
        if organization_uid is not UNSET:
            field_dict["organizationUid"] = organization_uid
        if management_agent_uid is not UNSET:
            field_dict["managementAgentUid"] = management_agent_uid
        if name is not UNSET:
            field_dict["name"] = name
        if version is not UNSET:
            field_dict["version"] = version
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_unique_uid(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                unique_uid_type_0 = UUID(data)

                return unique_uid_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        unique_uid = _parse_unique_uid(d.pop("uniqueUid", UNSET))

        _location_uid = d.pop("locationUid", UNSET)
        location_uid: UUID | Unset
        if isinstance(_location_uid, Unset):
            location_uid = UNSET
        else:
            location_uid = UUID(_location_uid)

        _organization_uid = d.pop("organizationUid", UNSET)
        organization_uid: UUID | Unset
        if isinstance(_organization_uid, Unset):
            organization_uid = UNSET
        else:
            organization_uid = UUID(_organization_uid)

        _management_agent_uid = d.pop("managementAgentUid", UNSET)
        management_agent_uid: UUID | Unset
        if isinstance(_management_agent_uid, Unset):
            management_agent_uid = UNSET
        else:
            management_agent_uid = UUID(_management_agent_uid)

        name = d.pop("name", UNSET)

        version = d.pop("version", UNSET)

        _status = d.pop("status", UNSET)
        status: UnactivatedVb365ServerStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = UnactivatedVb365ServerStatus(_status)

        unactivated_vb_365_server = cls(
            unique_uid=unique_uid,
            location_uid=location_uid,
            organization_uid=organization_uid,
            management_agent_uid=management_agent_uid,
            name=name,
            version=version,
            status=status,
        )

        unactivated_vb_365_server.additional_properties = d
        return unactivated_vb_365_server

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
