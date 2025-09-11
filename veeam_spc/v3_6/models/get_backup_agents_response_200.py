from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.backup_agent import BackupAgent
    from ..models.response_error import ResponseError
    from ..models.response_metadata import ResponseMetadata


T = TypeVar("T", bound="GetBackupAgentsResponse200")


@_attrs_define
class GetBackupAgentsResponse200:
    """
    Attributes:
        data (list['BackupAgent']):
        meta (Union[Unset, ResponseMetadata]):
        errors (Union[Unset, list['ResponseError']]):
    """

    data: list["BackupAgent"]
    meta: Union[Unset, "ResponseMetadata"] = UNSET
    errors: Union[Unset, list["ResponseError"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data = []
        for data_item_data in self.data:
            data_item = data_item_data.to_dict()
            data.append(data_item)

        meta: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.meta, Unset):
            meta = self.meta.to_dict()

        errors: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.errors, Unset):
            errors = []
            for errors_item_data in self.errors:
                errors_item = errors_item_data.to_dict()
                errors.append(errors_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "data": data,
            }
        )
        if meta is not UNSET:
            field_dict["meta"] = meta
        if errors is not UNSET:
            field_dict["errors"] = errors

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.backup_agent import BackupAgent
        from ..models.response_error import ResponseError
        from ..models.response_metadata import ResponseMetadata

        d = dict(src_dict)
        data = []
        _data = d.pop("data")
        for data_item_data in _data:
            data_item = BackupAgent.from_dict(data_item_data)

            data.append(data_item)

        _meta = d.pop("meta", UNSET)
        meta: Union[Unset, ResponseMetadata]
        if isinstance(_meta, Unset):
            meta = UNSET
        else:
            meta = ResponseMetadata.from_dict(_meta)

        errors = []
        _errors = d.pop("errors", UNSET)
        for errors_item_data in _errors or []:
            errors_item = ResponseError.from_dict(errors_item_data)

            errors.append(errors_item)

        get_backup_agents_response_200 = cls(
            data=data,
            meta=meta,
            errors=errors,
        )

        get_backup_agents_response_200.additional_properties = d
        return get_backup_agents_response_200

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
