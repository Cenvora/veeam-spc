from collections.abc import Mapping
from typing import Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.enterprise_manager_status import EnterpriseManagerStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="EnterpriseManager")


@_attrs_define
class EnterpriseManager:
    """
    Attributes:
        instance_uid (Union[Unset, UUID]): UID assigned to a Veeam Backup Enterprise Manager server.
        name (Union[Unset, str]): Hostname of a Veeam Backup Enterprise Manager server.
        management_agent_uid (Union[Unset, UUID]): UID assigned to a management agent installed on a Veeam Backup
            Enterprise Manager server.
        installation_uid (Union[Unset, UUID]): UID assigned to a Veeam Backup Enterprise Manager installation.
        version (Union[Unset, str]): Version of a Veeam Backup Enterprise Manager.
        status (Union[Unset, EnterpriseManagerStatus]): Status of a Veeam Backup Enterprise Manager server.
    """

    instance_uid: Union[Unset, UUID] = UNSET
    name: Union[Unset, str] = UNSET
    management_agent_uid: Union[Unset, UUID] = UNSET
    installation_uid: Union[Unset, UUID] = UNSET
    version: Union[Unset, str] = UNSET
    status: Union[Unset, EnterpriseManagerStatus] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        instance_uid: Union[Unset, str] = UNSET
        if not isinstance(self.instance_uid, Unset):
            instance_uid = str(self.instance_uid)

        name = self.name

        management_agent_uid: Union[Unset, str] = UNSET
        if not isinstance(self.management_agent_uid, Unset):
            management_agent_uid = str(self.management_agent_uid)

        installation_uid: Union[Unset, str] = UNSET
        if not isinstance(self.installation_uid, Unset):
            installation_uid = str(self.installation_uid)

        version = self.version

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if instance_uid is not UNSET:
            field_dict["instanceUid"] = instance_uid
        if name is not UNSET:
            field_dict["name"] = name
        if management_agent_uid is not UNSET:
            field_dict["managementAgentUid"] = management_agent_uid
        if installation_uid is not UNSET:
            field_dict["installationUid"] = installation_uid
        if version is not UNSET:
            field_dict["version"] = version
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _instance_uid = d.pop("instanceUid", UNSET)
        instance_uid: Union[Unset, UUID]
        if isinstance(_instance_uid, Unset):
            instance_uid = UNSET
        else:
            instance_uid = UUID(_instance_uid)

        name = d.pop("name", UNSET)

        _management_agent_uid = d.pop("managementAgentUid", UNSET)
        management_agent_uid: Union[Unset, UUID]
        if isinstance(_management_agent_uid, Unset):
            management_agent_uid = UNSET
        else:
            management_agent_uid = UUID(_management_agent_uid)

        _installation_uid = d.pop("installationUid", UNSET)
        installation_uid: Union[Unset, UUID]
        if isinstance(_installation_uid, Unset):
            installation_uid = UNSET
        else:
            installation_uid = UUID(_installation_uid)

        version = d.pop("version", UNSET)

        _status = d.pop("status", UNSET)
        status: Union[Unset, EnterpriseManagerStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = EnterpriseManagerStatus(_status)

        enterprise_manager = cls(
            instance_uid=instance_uid,
            name=name,
            management_agent_uid=management_agent_uid,
            installation_uid=installation_uid,
            version=version,
            status=status,
        )

        enterprise_manager.additional_properties = d
        return enterprise_manager

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
