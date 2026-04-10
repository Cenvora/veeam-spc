from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.proxy_product import ProxyProduct
from ..types import UNSET, Unset

T = TypeVar("T", bound="ProxyProductInformation")


@_attrs_define
class ProxyProductInformation:
    """
    Attributes:
        proxy_product (Union[Unset, ProxyProduct]): Veeam product that accepts proxied requests.
        proxy_product_url_representation (Union[Unset, str]): Part of URL path that must be used to proxy requests to a
            Veeam product.
    """

    proxy_product: Union[Unset, ProxyProduct] = UNSET
    proxy_product_url_representation: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        proxy_product: Union[Unset, str] = UNSET
        if not isinstance(self.proxy_product, Unset):
            proxy_product = self.proxy_product.value

        proxy_product_url_representation = self.proxy_product_url_representation

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if proxy_product is not UNSET:
            field_dict["proxyProduct"] = proxy_product
        if proxy_product_url_representation is not UNSET:
            field_dict["proxyProductUrlRepresentation"] = proxy_product_url_representation

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _proxy_product = d.pop("proxyProduct", UNSET)
        proxy_product: Union[Unset, ProxyProduct]
        if isinstance(_proxy_product, Unset):
            proxy_product = UNSET
        else:
            proxy_product = ProxyProduct(_proxy_product)

        proxy_product_url_representation = d.pop("proxyProductUrlRepresentation", UNSET)

        proxy_product_information = cls(
            proxy_product=proxy_product,
            proxy_product_url_representation=proxy_product_url_representation,
        )

        proxy_product_information.additional_properties = d
        return proxy_product_information

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
