import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.proxy_product import ProxyProduct
from ..types import UNSET, Unset

T = TypeVar("T", bound="ProxySession")


@_attrs_define
class ProxySession:
    """
    Attributes:
        user_uid (Union[Unset, UUID]): UID of a user that created a proxy session.
        management_agent_uid (Union[Unset, UUID]): UID assigned to a management agent.
        product (Union[Unset, ProxyProduct]): Veeam product that accepts proxied requests.
        creation_time (Union[Unset, datetime.datetime]): Date and time when a proxy session was created.
        last_action_time (Union[Unset, datetime.datetime]): Date and time of the latest action performed inside a proxy
            session.
    """

    user_uid: Union[Unset, UUID] = UNSET
    management_agent_uid: Union[Unset, UUID] = UNSET
    product: Union[Unset, ProxyProduct] = UNSET
    creation_time: Union[Unset, datetime.datetime] = UNSET
    last_action_time: Union[Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        user_uid: Union[Unset, str] = UNSET
        if not isinstance(self.user_uid, Unset):
            user_uid = str(self.user_uid)

        management_agent_uid: Union[Unset, str] = UNSET
        if not isinstance(self.management_agent_uid, Unset):
            management_agent_uid = str(self.management_agent_uid)

        product: Union[Unset, str] = UNSET
        if not isinstance(self.product, Unset):
            product = self.product.value

        creation_time: Union[Unset, str] = UNSET
        if not isinstance(self.creation_time, Unset):
            creation_time = self.creation_time.isoformat()

        last_action_time: Union[Unset, str] = UNSET
        if not isinstance(self.last_action_time, Unset):
            last_action_time = self.last_action_time.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if user_uid is not UNSET:
            field_dict["userUid"] = user_uid
        if management_agent_uid is not UNSET:
            field_dict["managementAgentUid"] = management_agent_uid
        if product is not UNSET:
            field_dict["product"] = product
        if creation_time is not UNSET:
            field_dict["creationTime"] = creation_time
        if last_action_time is not UNSET:
            field_dict["lastActionTime"] = last_action_time

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _user_uid = d.pop("userUid", UNSET)
        user_uid: Union[Unset, UUID]
        if isinstance(_user_uid, Unset):
            user_uid = UNSET
        else:
            user_uid = UUID(_user_uid)

        _management_agent_uid = d.pop("managementAgentUid", UNSET)
        management_agent_uid: Union[Unset, UUID]
        if isinstance(_management_agent_uid, Unset):
            management_agent_uid = UNSET
        else:
            management_agent_uid = UUID(_management_agent_uid)

        _product = d.pop("product", UNSET)
        product: Union[Unset, ProxyProduct]
        if isinstance(_product, Unset):
            product = UNSET
        else:
            product = ProxyProduct(_product)

        _creation_time = d.pop("creationTime", UNSET)
        creation_time: Union[Unset, datetime.datetime]
        if isinstance(_creation_time, Unset):
            creation_time = UNSET
        else:
            creation_time = isoparse(_creation_time)

        _last_action_time = d.pop("lastActionTime", UNSET)
        last_action_time: Union[Unset, datetime.datetime]
        if isinstance(_last_action_time, Unset):
            last_action_time = UNSET
        else:
            last_action_time = isoparse(_last_action_time)

        proxy_session = cls(
            user_uid=user_uid,
            management_agent_uid=management_agent_uid,
            product=product,
            creation_time=creation_time,
            last_action_time=last_action_time,
        )

        proxy_session.additional_properties = d
        return proxy_session

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
