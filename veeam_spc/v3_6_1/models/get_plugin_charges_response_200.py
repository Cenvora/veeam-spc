from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.plugin_charge import PluginCharge
    from ..models.response_error import ResponseError
    from ..models.response_metadata_type_0 import ResponseMetadataType0


T = TypeVar("T", bound="GetPluginChargesResponse200")


@_attrs_define
class GetPluginChargesResponse200:
    """
    Attributes:
        data (list['PluginCharge']):
        meta (Union['ResponseMetadataType0', None, Unset]):
        errors (Union[None, Unset, list['ResponseError']]):
    """

    data: list["PluginCharge"]
    meta: Union["ResponseMetadataType0", None, Unset] = UNSET
    errors: Union[None, Unset, list["ResponseError"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.response_metadata_type_0 import ResponseMetadataType0

        data = []
        for data_item_data in self.data:
            data_item = data_item_data.to_dict()
            data.append(data_item)

        meta: Union[None, Unset, dict[str, Any]]
        if isinstance(self.meta, Unset):
            meta = UNSET
        elif isinstance(self.meta, ResponseMetadataType0):
            meta = self.meta.to_dict()
        else:
            meta = self.meta

        errors: Union[None, Unset, list[dict[str, Any]]]
        if isinstance(self.errors, Unset):
            errors = UNSET
        elif isinstance(self.errors, list):
            errors = []
            for errors_type_0_item_data in self.errors:
                errors_type_0_item = errors_type_0_item_data.to_dict()
                errors.append(errors_type_0_item)

        else:
            errors = self.errors

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
        from ..models.plugin_charge import PluginCharge
        from ..models.response_error import ResponseError
        from ..models.response_metadata_type_0 import ResponseMetadataType0

        d = dict(src_dict)
        data = []
        _data = d.pop("data")
        for data_item_data in _data:
            data_item = PluginCharge.from_dict(data_item_data)

            data.append(data_item)

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

        def _parse_errors(data: object) -> Union[None, Unset, list["ResponseError"]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                errors_type_0 = []
                _errors_type_0 = data
                for errors_type_0_item_data in _errors_type_0:
                    errors_type_0_item = ResponseError.from_dict(errors_type_0_item_data)

                    errors_type_0.append(errors_type_0_item)

                return errors_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list["ResponseError"]], data)

        errors = _parse_errors(d.pop("errors", UNSET))

        get_plugin_charges_response_200 = cls(
            data=data,
            meta=meta,
            errors=errors,
        )

        get_plugin_charges_response_200.additional_properties = d
        return get_plugin_charges_response_200

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
