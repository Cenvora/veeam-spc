from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.server_current_license_usage_server_type import ServerCurrentLicenseUsageServerType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.current_license_usage_workload import CurrentLicenseUsageWorkload


T = TypeVar("T", bound="ServerCurrentLicenseUsage")


@_attrs_define
class ServerCurrentLicenseUsage:
    """
    Attributes:
        server_uid (Union[Unset, UUID]): Server UID.
        server_type (Union[Unset, ServerCurrentLicenseUsageServerType]): Veeam product installed on the server.
        workloads (Union[Unset, list['CurrentLicenseUsageWorkload']]): License usage by each workload type.
    """

    server_uid: Union[Unset, UUID] = UNSET
    server_type: Union[Unset, ServerCurrentLicenseUsageServerType] = UNSET
    workloads: Union[Unset, list["CurrentLicenseUsageWorkload"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        server_uid: Union[Unset, str] = UNSET
        if not isinstance(self.server_uid, Unset):
            server_uid = str(self.server_uid)

        server_type: Union[Unset, str] = UNSET
        if not isinstance(self.server_type, Unset):
            server_type = self.server_type.value

        workloads: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.workloads, Unset):
            workloads = []
            for workloads_item_data in self.workloads:
                workloads_item = workloads_item_data.to_dict()
                workloads.append(workloads_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if server_uid is not UNSET:
            field_dict["serverUid"] = server_uid
        if server_type is not UNSET:
            field_dict["serverType"] = server_type
        if workloads is not UNSET:
            field_dict["workloads"] = workloads

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.current_license_usage_workload import CurrentLicenseUsageWorkload

        d = dict(src_dict)
        _server_uid = d.pop("serverUid", UNSET)
        server_uid: Union[Unset, UUID]
        if isinstance(_server_uid, Unset):
            server_uid = UNSET
        else:
            server_uid = UUID(_server_uid)

        _server_type = d.pop("serverType", UNSET)
        server_type: Union[Unset, ServerCurrentLicenseUsageServerType]
        if isinstance(_server_type, Unset):
            server_type = UNSET
        else:
            server_type = ServerCurrentLicenseUsageServerType(_server_type)

        workloads = []
        _workloads = d.pop("workloads", UNSET)
        for workloads_item_data in _workloads or []:
            workloads_item = CurrentLicenseUsageWorkload.from_dict(workloads_item_data)

            workloads.append(workloads_item)

        server_current_license_usage = cls(
            server_uid=server_uid,
            server_type=server_type,
            workloads=workloads,
        )

        server_current_license_usage.additional_properties = d
        return server_current_license_usage

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
