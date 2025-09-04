from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Vb365JobItemSite")


@_attrs_define
class Vb365JobItemSite:
    """
    Attributes:
        id (str): ID assigned to a site.
        title (str): Title of a site.
        url (str): Site URL.
        name (Union[Unset, str]): Name of a site.
        parent_url (Union[Unset, str]): Parent URL of a site.
        is_cloud (Union[Unset, bool]): Indicates whether a site is cloud-based.
        is_personal (Union[Unset, bool]): Indicates whether a site is personal.
        is_available (Union[Unset, bool]): Indicates whether a site can be included in a backup job.
        site_collection_error (Union[Unset, str]): Message for site collection processing error.
    """

    id: str
    title: str
    url: str
    name: Union[Unset, str] = UNSET
    parent_url: Union[Unset, str] = UNSET
    is_cloud: Union[Unset, bool] = UNSET
    is_personal: Union[Unset, bool] = UNSET
    is_available: Union[Unset, bool] = UNSET
    site_collection_error: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        title = self.title

        url = self.url

        name = self.name

        parent_url = self.parent_url

        is_cloud = self.is_cloud

        is_personal = self.is_personal

        is_available = self.is_available

        site_collection_error = self.site_collection_error

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "title": title,
                "url": url,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if parent_url is not UNSET:
            field_dict["parentUrl"] = parent_url
        if is_cloud is not UNSET:
            field_dict["isCloud"] = is_cloud
        if is_personal is not UNSET:
            field_dict["isPersonal"] = is_personal
        if is_available is not UNSET:
            field_dict["isAvailable"] = is_available
        if site_collection_error is not UNSET:
            field_dict["siteCollectionError"] = site_collection_error

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        title = d.pop("title")

        url = d.pop("url")

        name = d.pop("name", UNSET)

        parent_url = d.pop("parentUrl", UNSET)

        is_cloud = d.pop("isCloud", UNSET)

        is_personal = d.pop("isPersonal", UNSET)

        is_available = d.pop("isAvailable", UNSET)

        site_collection_error = d.pop("siteCollectionError", UNSET)

        vb_365_job_item_site = cls(
            id=id,
            title=title,
            url=url,
            name=name,
            parent_url=parent_url,
            is_cloud=is_cloud,
            is_personal=is_personal,
            is_available=is_available,
            site_collection_error=site_collection_error,
        )

        vb_365_job_item_site.additional_properties = d
        return vb_365_job_item_site

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
