from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.async_action_status import AsyncActionStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.async_action_info_query_parameters import AsyncActionInfoQueryParameters


T = TypeVar("T", bound="AsyncActionInfo")


@_attrs_define
class AsyncActionInfo:
    """
    Attributes:
        id (UUID): UID assigned to an async action.
        initiator_uid (UUID): UID assigned to a user who initiates an async action.
        action_name (str): Name of an operation that initiated an async action.
        status (AsyncActionStatus):
        query_parameters (AsyncActionInfoQueryParameters): Key-value map containing query parameters of the operation
            that initiated an async action.
        request_body (Union[None, Unset, str]): Content of a request body of the operation that initiated an async
            action.
    """

    id: UUID
    initiator_uid: UUID
    action_name: str
    status: AsyncActionStatus
    query_parameters: "AsyncActionInfoQueryParameters"
    request_body: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        initiator_uid = str(self.initiator_uid)

        action_name = self.action_name

        status = self.status.value

        query_parameters = self.query_parameters.to_dict()

        request_body: Union[None, Unset, str]
        if isinstance(self.request_body, Unset):
            request_body = UNSET
        else:
            request_body = self.request_body

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "initiatorUid": initiator_uid,
                "actionName": action_name,
                "status": status,
                "queryParameters": query_parameters,
            }
        )
        if request_body is not UNSET:
            field_dict["requestBody"] = request_body

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.async_action_info_query_parameters import AsyncActionInfoQueryParameters

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        initiator_uid = UUID(d.pop("initiatorUid"))

        action_name = d.pop("actionName")

        status = AsyncActionStatus(d.pop("status"))

        query_parameters = AsyncActionInfoQueryParameters.from_dict(d.pop("queryParameters"))

        def _parse_request_body(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        request_body = _parse_request_body(d.pop("requestBody", UNSET))

        async_action_info = cls(
            id=id,
            initiator_uid=initiator_uid,
            action_name=action_name,
            status=status,
            query_parameters=query_parameters,
            request_body=request_body,
        )

        async_action_info.additional_properties = d
        return async_action_info

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
