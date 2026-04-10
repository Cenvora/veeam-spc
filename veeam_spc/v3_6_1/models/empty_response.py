from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.empty_response_data import EmptyResponseData
    from ..models.response_error import ResponseError
    from ..models.response_metadata_type_0 import ResponseMetadataType0


T = TypeVar("T", bound="EmptyResponse")


@_attrs_define
class EmptyResponse:
    """
    Attributes:
        errors (list['ResponseError']):
        data (Union[Unset, EmptyResponseData]):
        meta (Union['ResponseMetadataType0', None, Unset]):
    """

    errors: list["ResponseError"]
    data: Union[Unset, "EmptyResponseData"] = UNSET
    meta: Union["ResponseMetadataType0", None, Unset] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.response_metadata_type_0 import ResponseMetadataType0

        errors = []
        for errors_item_data in self.errors:
            errors_item = errors_item_data.to_dict()
            errors.append(errors_item)

        data: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.data, Unset):
            data = self.data.to_dict()

        meta: Union[None, Unset, dict[str, Any]]
        if isinstance(self.meta, Unset):
            meta = UNSET
        elif isinstance(self.meta, ResponseMetadataType0):
            meta = self.meta.to_dict()
        else:
            meta = self.meta

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "errors": errors,
            }
        )
        if data is not UNSET:
            field_dict["data"] = data
        if meta is not UNSET:
            field_dict["meta"] = meta

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.empty_response_data import EmptyResponseData
        from ..models.response_error import ResponseError
        from ..models.response_metadata_type_0 import ResponseMetadataType0

        d = dict(src_dict)
        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:
            errors_item = ResponseError.from_dict(errors_item_data)

            errors.append(errors_item)

        _data = d.pop("data", UNSET)
        data: Union[Unset, EmptyResponseData]
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = EmptyResponseData.from_dict(_data)

        def _parse_meta(data: object) -> Union["ResponseMetadataType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_response_metadata_type_0 = ResponseMetadataType0.from_dict(data)

                return componentsschemas_response_metadata_type_0
            except:  # noqa: E722
                pass
            return cast(Union["ResponseMetadataType0", None, Unset], data)

        meta = _parse_meta(d.pop("meta", UNSET))

        empty_response = cls(
            errors=errors,
            data=data,
            meta=meta,
        )

        empty_response.additional_properties = d
        return empty_response

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
