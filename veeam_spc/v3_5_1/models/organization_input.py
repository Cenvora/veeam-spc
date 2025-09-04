from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="OrganizationInput")


@_attrs_define
class OrganizationInput:
    """
    Attributes:
        name (str): Name of an organization.
        alias (Union[Unset, str]): Alias of an organization.
        tax_id (Union[Unset, str]): Organization Tax ID.
        email (Union[Unset, str]): Contact email address.
        phone (Union[Unset, str]): Telephone number of a primary contact of an organization.
        country (Union[Unset, int]): System ID assigned to an organization country of residence.
        state (Union[Unset, int]): System ID assigned to a USA state where an organization is located.
        country_name (Union[Unset, str]): Country name.
        region_name (Union[Unset, str]): Region name.
        city (Union[Unset, str]): City where an organization is located.
        street (Union[Unset, str]): Street where an organization is located.
        location_admin_0_code (Union[Unset, str]): Code of a country where an organization is located.
        location_admin_1_code (Union[Unset, str]): Code of a state, region or area where an organization is located.
        location_admin_2_code (Union[Unset, str]): Code of a district or municipality where an organization is located.
        notes (Union[Unset, str]): Additional information about an organization.
        zip_code (Union[Unset, str]): Postal code.
        website (Union[Unset, str]): Organization website.
        veeam_tenant_id (Union[Unset, str]): ID of an organization used in Veeam records.
        company_id (Union[Unset, str]): ID of an organization used for 3rd party applications.
    """

    name: str
    alias: Union[Unset, str] = UNSET
    tax_id: Union[Unset, str] = UNSET
    email: Union[Unset, str] = UNSET
    phone: Union[Unset, str] = UNSET
    country: Union[Unset, int] = UNSET
    state: Union[Unset, int] = UNSET
    country_name: Union[Unset, str] = UNSET
    region_name: Union[Unset, str] = UNSET
    city: Union[Unset, str] = UNSET
    street: Union[Unset, str] = UNSET
    location_admin_0_code: Union[Unset, str] = UNSET
    location_admin_1_code: Union[Unset, str] = UNSET
    location_admin_2_code: Union[Unset, str] = UNSET
    notes: Union[Unset, str] = UNSET
    zip_code: Union[Unset, str] = UNSET
    website: Union[Unset, str] = UNSET
    veeam_tenant_id: Union[Unset, str] = UNSET
    company_id: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        alias = self.alias

        tax_id = self.tax_id

        email = self.email

        phone = self.phone

        country = self.country

        state = self.state

        country_name = self.country_name

        region_name = self.region_name

        city = self.city

        street = self.street

        location_admin_0_code = self.location_admin_0_code

        location_admin_1_code = self.location_admin_1_code

        location_admin_2_code = self.location_admin_2_code

        notes = self.notes

        zip_code = self.zip_code

        website = self.website

        veeam_tenant_id = self.veeam_tenant_id

        company_id = self.company_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if alias is not UNSET:
            field_dict["alias"] = alias
        if tax_id is not UNSET:
            field_dict["taxId"] = tax_id
        if email is not UNSET:
            field_dict["email"] = email
        if phone is not UNSET:
            field_dict["phone"] = phone
        if country is not UNSET:
            field_dict["country"] = country
        if state is not UNSET:
            field_dict["state"] = state
        if country_name is not UNSET:
            field_dict["countryName"] = country_name
        if region_name is not UNSET:
            field_dict["regionName"] = region_name
        if city is not UNSET:
            field_dict["city"] = city
        if street is not UNSET:
            field_dict["street"] = street
        if location_admin_0_code is not UNSET:
            field_dict["locationAdmin0Code"] = location_admin_0_code
        if location_admin_1_code is not UNSET:
            field_dict["locationAdmin1Code"] = location_admin_1_code
        if location_admin_2_code is not UNSET:
            field_dict["locationAdmin2Code"] = location_admin_2_code
        if notes is not UNSET:
            field_dict["notes"] = notes
        if zip_code is not UNSET:
            field_dict["zipCode"] = zip_code
        if website is not UNSET:
            field_dict["website"] = website
        if veeam_tenant_id is not UNSET:
            field_dict["veeamTenantId"] = veeam_tenant_id
        if company_id is not UNSET:
            field_dict["companyId"] = company_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        alias = d.pop("alias", UNSET)

        tax_id = d.pop("taxId", UNSET)

        email = d.pop("email", UNSET)

        phone = d.pop("phone", UNSET)

        country = d.pop("country", UNSET)

        state = d.pop("state", UNSET)

        country_name = d.pop("countryName", UNSET)

        region_name = d.pop("regionName", UNSET)

        city = d.pop("city", UNSET)

        street = d.pop("street", UNSET)

        location_admin_0_code = d.pop("locationAdmin0Code", UNSET)

        location_admin_1_code = d.pop("locationAdmin1Code", UNSET)

        location_admin_2_code = d.pop("locationAdmin2Code", UNSET)

        notes = d.pop("notes", UNSET)

        zip_code = d.pop("zipCode", UNSET)

        website = d.pop("website", UNSET)

        veeam_tenant_id = d.pop("veeamTenantId", UNSET)

        company_id = d.pop("companyId", UNSET)

        organization_input = cls(
            name=name,
            alias=alias,
            tax_id=tax_id,
            email=email,
            phone=phone,
            country=country,
            state=state,
            country_name=country_name,
            region_name=region_name,
            city=city,
            street=street,
            location_admin_0_code=location_admin_0_code,
            location_admin_1_code=location_admin_1_code,
            location_admin_2_code=location_admin_2_code,
            notes=notes,
            zip_code=zip_code,
            website=website,
            veeam_tenant_id=veeam_tenant_id,
            company_id=company_id,
        )

        organization_input.additional_properties = d
        return organization_input

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
