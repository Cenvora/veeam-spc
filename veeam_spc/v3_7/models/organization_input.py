from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="OrganizationInput")


@_attrs_define
class OrganizationInput:
    """
    Attributes:
        name (str): Name of an organization.
        alias (str | Unset): Alias of an organization.
        tax_id (str | Unset): Organization Tax ID.
        legal_name (str | Unset): Legal name of an organization.
        email (str | Unset): Contact email address.
        phone (str | Unset): Telephone number of a primary contact of an organization.
        country (int | Unset): System ID assigned to an organization country of residence.
        state (int | Unset): System ID assigned to a USA state where an organization is located.
        country_name (str | Unset): Country name.
        region_name (str | Unset): Region name.
        city (str | Unset): City where an organization is located.
        street (str | Unset): Street where an organization is located.
        location_admin_0_code (str | Unset): Code of a country where an organization is located.
        location_admin_1_code (str | Unset): Code of a state, region or area where an organization is located.
        location_admin_2_code (str | Unset): Code of a district or municipality where an organization is located.
        notes (str | Unset): Additional information about an organization.
        zip_code (str | Unset): Postal code.
        domain (str | Unset): Organization domain.
        website (str | Unset): Organization website.
        veeam_tenant_id (str | Unset): ID of an organization used in Veeam records.
        company_id (str | Unset): ID of an organization used for 3rd party applications.
    """

    name: str
    alias: str | Unset = UNSET
    tax_id: str | Unset = UNSET
    legal_name: str | Unset = UNSET
    email: str | Unset = UNSET
    phone: str | Unset = UNSET
    country: int | Unset = UNSET
    state: int | Unset = UNSET
    country_name: str | Unset = UNSET
    region_name: str | Unset = UNSET
    city: str | Unset = UNSET
    street: str | Unset = UNSET
    location_admin_0_code: str | Unset = UNSET
    location_admin_1_code: str | Unset = UNSET
    location_admin_2_code: str | Unset = UNSET
    notes: str | Unset = UNSET
    zip_code: str | Unset = UNSET
    domain: str | Unset = UNSET
    website: str | Unset = UNSET
    veeam_tenant_id: str | Unset = UNSET
    company_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        alias = self.alias

        tax_id = self.tax_id

        legal_name = self.legal_name

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

        domain = self.domain

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
        if legal_name is not UNSET:
            field_dict["legalName"] = legal_name
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
        if domain is not UNSET:
            field_dict["domain"] = domain
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

        legal_name = d.pop("legalName", UNSET)

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

        domain = d.pop("domain", UNSET)

        website = d.pop("website", UNSET)

        veeam_tenant_id = d.pop("veeamTenantId", UNSET)

        company_id = d.pop("companyId", UNSET)

        organization_input = cls(
            name=name,
            alias=alias,
            tax_id=tax_id,
            legal_name=legal_name,
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
            domain=domain,
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
