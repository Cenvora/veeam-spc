from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.deployment_log_status import DeploymentLogStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.deployment_log_entry import DeploymentLogEntry


T = TypeVar("T", bound="DeploymentLog")


@_attrs_define
class DeploymentLog:
    """
    Attributes:
        complete_percentage (Union[Unset, int]): Percentage of deployment progress.
        status (Union[Unset, DeploymentLogStatus]): Deployment status.
        log_entries (Union[Unset, list['DeploymentLogEntry']]): Log entry containing details about deployment process.
    """

    complete_percentage: Union[Unset, int] = UNSET
    status: Union[Unset, DeploymentLogStatus] = UNSET
    log_entries: Union[Unset, list["DeploymentLogEntry"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        complete_percentage = self.complete_percentage

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        log_entries: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.log_entries, Unset):
            log_entries = []
            for log_entries_item_data in self.log_entries:
                log_entries_item = log_entries_item_data.to_dict()
                log_entries.append(log_entries_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if complete_percentage is not UNSET:
            field_dict["completePercentage"] = complete_percentage
        if status is not UNSET:
            field_dict["status"] = status
        if log_entries is not UNSET:
            field_dict["logEntries"] = log_entries

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.deployment_log_entry import DeploymentLogEntry

        d = dict(src_dict)
        complete_percentage = d.pop("completePercentage", UNSET)

        _status = d.pop("status", UNSET)
        status: Union[Unset, DeploymentLogStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = DeploymentLogStatus(_status)

        log_entries = []
        _log_entries = d.pop("logEntries", UNSET)
        for log_entries_item_data in _log_entries or []:
            log_entries_item = DeploymentLogEntry.from_dict(log_entries_item_data)

            log_entries.append(log_entries_item)

        deployment_log = cls(
            complete_percentage=complete_percentage,
            status=status,
            log_entries=log_entries,
        )

        deployment_log.additional_properties = d
        return deployment_log

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
