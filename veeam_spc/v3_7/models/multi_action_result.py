from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.e_action_result_status import EActionResultStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.result import Result


T = TypeVar("T", bound="MultiActionResult")


@_attrs_define
class MultiActionResult:
    """Result of an operation performed on multiple objects. Reconstructed from the response example in the source
    document, which references this schema without defining it.

        Attributes:
            results (list[Result] | Unset):
            message (None | str | Unset):
            status (EActionResultStatus | Unset):
            is_multi_action_result (bool | Unset):
    """

    results: list[Result] | Unset = UNSET
    message: None | str | Unset = UNSET
    status: EActionResultStatus | Unset = UNSET
    is_multi_action_result: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        results: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.results, Unset):
            results = []
            for results_item_data in self.results:
                results_item = results_item_data.to_dict()
                results.append(results_item)

        message: None | str | Unset
        if isinstance(self.message, Unset):
            message = UNSET
        else:
            message = self.message

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        is_multi_action_result = self.is_multi_action_result

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if results is not UNSET:
            field_dict["results"] = results
        if message is not UNSET:
            field_dict["message"] = message
        if status is not UNSET:
            field_dict["status"] = status
        if is_multi_action_result is not UNSET:
            field_dict["isMultiActionResult"] = is_multi_action_result

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.result import Result

        d = dict(src_dict)
        _results = d.pop("results", UNSET)
        results: list[Result] | Unset = UNSET
        if _results is not UNSET:
            results = []
            for results_item_data in _results:
                results_item = Result.from_dict(results_item_data)

                results.append(results_item)

        def _parse_message(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        message = _parse_message(d.pop("message", UNSET))

        _status = d.pop("status", UNSET)
        status: EActionResultStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = EActionResultStatus(_status)

        is_multi_action_result = d.pop("isMultiActionResult", UNSET)

        multi_action_result = cls(
            results=results,
            message=message,
            status=status,
            is_multi_action_result=is_multi_action_result,
        )

        multi_action_result.additional_properties = d
        return multi_action_result

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
