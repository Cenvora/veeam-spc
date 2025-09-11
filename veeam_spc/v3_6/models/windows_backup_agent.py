from collections.abc import Mapping
from typing import Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.windows_backup_agent_cbt_driver_status import WindowsBackupAgentCbtDriverStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="WindowsBackupAgent")


@_attrs_define
class WindowsBackupAgent:
    """
    Example:
        {'instanceUid': '82b693e8-2d33-40f3-8991-a26e8bd86158', 'managementAgentUid':
            '99ea35b0-d23f-41ab-8bb3-2e06555f039b', 'cbtDriverStatus': 'NotInstalled'}

    Attributes:
        instance_uid (Union[Unset, UUID]): UID assigned to a Veeam backup agent.
        management_agent_uid (Union[Unset, UUID]): UID assigned to a management agent that is deployed along with Veeam
            backup agent.
        cbt_driver_status (Union[Unset, WindowsBackupAgentCbtDriverStatus]): CBT driver status.
    """

    instance_uid: Union[Unset, UUID] = UNSET
    management_agent_uid: Union[Unset, UUID] = UNSET
    cbt_driver_status: Union[Unset, WindowsBackupAgentCbtDriverStatus] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        instance_uid: Union[Unset, str] = UNSET
        if not isinstance(self.instance_uid, Unset):
            instance_uid = str(self.instance_uid)

        management_agent_uid: Union[Unset, str] = UNSET
        if not isinstance(self.management_agent_uid, Unset):
            management_agent_uid = str(self.management_agent_uid)

        cbt_driver_status: Union[Unset, str] = UNSET
        if not isinstance(self.cbt_driver_status, Unset):
            cbt_driver_status = self.cbt_driver_status.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if instance_uid is not UNSET:
            field_dict["instanceUid"] = instance_uid
        if management_agent_uid is not UNSET:
            field_dict["managementAgentUid"] = management_agent_uid
        if cbt_driver_status is not UNSET:
            field_dict["cbtDriverStatus"] = cbt_driver_status

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

        _management_agent_uid = d.pop("managementAgentUid", UNSET)
        management_agent_uid: Union[Unset, UUID]
        if isinstance(_management_agent_uid, Unset):
            management_agent_uid = UNSET
        else:
            management_agent_uid = UUID(_management_agent_uid)

        _cbt_driver_status = d.pop("cbtDriverStatus", UNSET)
        cbt_driver_status: Union[Unset, WindowsBackupAgentCbtDriverStatus]
        if isinstance(_cbt_driver_status, Unset):
            cbt_driver_status = UNSET
        else:
            cbt_driver_status = WindowsBackupAgentCbtDriverStatus(_cbt_driver_status)

        windows_backup_agent = cls(
            instance_uid=instance_uid,
            management_agent_uid=management_agent_uid,
            cbt_driver_status=cbt_driver_status,
        )

        windows_backup_agent.additional_properties = d
        return windows_backup_agent

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
