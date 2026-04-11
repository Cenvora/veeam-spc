from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="OrganizationInput")


@_attrs_define
class OrganizationInput:
    """
    Attributes:
        name (str): Name of an organization.
        alias (None | str | Unset): Alias of an organization.
        tax_id (None | str | Unset): Organization Tax ID.
        email (None | str | Unset): Contact email address.
        phone (None | str | Unset): Telephone number of a primary contact of an organization.
        country (int | None | Unset): System ID assigned to an organization country of residence.
        state (int | None | Unset): System ID assigned to a USA state where an organization is located.
        country_name (None | str | Unset): Country name.
        region_name (None | str | Unset): Region name.
        city (None | str | Unset): City where an organization is located.
        street (None | str | Unset): Street where an organization is located.
        location_admin_0_code (None | str | Unset): Code of a country where an organization is located.
        location_admin_1_code (None | str | Unset): Code of a state, region or area where an organization is located.
        location_admin_2_code (None | str | Unset): Code of a district or municipality where an organization is located.
        notes (None | str | Unset): Additional information about an organization.
        zip_code (None | str | Unset): Postal code.
        website (None | str | Unset): Organization website.
        veeam_tenant_id (None | str | Unset): ID of an organization used in Veeam records.
        company_id (None | str | Unset): ID of an organization used for 3rd party applications.
    """

    name: str
    alias: None | str | Unset = UNSET
    tax_id: None | str | Unset = UNSET
    email: None | str | Unset = UNSET
    phone: None | str | Unset = UNSET
    country: int | None | Unset = UNSET
    state: int | None | Unset = UNSET
    country_name: None | str | Unset = UNSET
    region_name: None | str | Unset = UNSET
    city: None | str | Unset = UNSET
    street: None | str | Unset = UNSET
    location_admin_0_code: None | str | Unset = UNSET
    location_admin_1_code: None | str | Unset = UNSET
    location_admin_2_code: None | str | Unset = UNSET
    notes: None | str | Unset = UNSET
    zip_code: None | str | Unset = UNSET
    website: None | str | Unset = UNSET
    veeam_tenant_id: None | str | Unset = UNSET
    company_id: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        alias: None | str | Unset
        if isinstance(self.alias, Unset):
            alias = UNSET
        else:
            alias = self.alias

        tax_id: None | str | Unset
        if isinstance(self.tax_id, Unset):
            tax_id = UNSET
        else:
            tax_id = self.tax_id

        email: None | str | Unset
        if isinstance(self.email, Unset):
            email = UNSET
        else:
            email = self.email

        phone: None | str | Unset
        if isinstance(self.phone, Unset):
            phone = UNSET
        else:
            phone = self.phone

        country: int | None | Unset
        if isinstance(self.country, Unset):
            country = UNSET
        else:
            country = self.country

        state: int | None | Unset
        if isinstance(self.state, Unset):
            state = UNSET
        else:
            state = self.state

        country_name: None | str | Unset
        if isinstance(self.country_name, Unset):
            country_name = UNSET
        else:
            country_name = self.country_name

        region_name: None | str | Unset
        if isinstance(self.region_name, Unset):
            region_name = UNSET
        else:
            region_name = self.region_name

        city: None | str | Unset
        if isinstance(self.city, Unset):
            city = UNSET
        else:
            city = self.city

        street: None | str | Unset
        if isinstance(self.street, Unset):
            street = UNSET
        else:
            street = self.street

        location_admin_0_code: None | str | Unset
        if isinstance(self.location_admin_0_code, Unset):
            location_admin_0_code = UNSET
        else:
            location_admin_0_code = self.location_admin_0_code

        location_admin_1_code: None | str | Unset
        if isinstance(self.location_admin_1_code, Unset):
            location_admin_1_code = UNSET
        else:
            location_admin_1_code = self.location_admin_1_code

        location_admin_2_code: None | str | Unset
        if isinstance(self.location_admin_2_code, Unset):
            location_admin_2_code = UNSET
        else:
            location_admin_2_code = self.location_admin_2_code

        notes: None | str | Unset
        if isinstance(self.notes, Unset):
            notes = UNSET
        else:
            notes = self.notes

        zip_code: None | str | Unset
        if isinstance(self.zip_code, Unset):
            zip_code = UNSET
        else:
            zip_code = self.zip_code

        website: None | str | Unset
        if isinstance(self.website, Unset):
            website = UNSET
        else:
            website = self.website

        veeam_tenant_id: None | str | Unset
        if isinstance(self.veeam_tenant_id, Unset):
            veeam_tenant_id = UNSET
        else:
            veeam_tenant_id = self.veeam_tenant_id

        company_id: None | str | Unset
        if isinstance(self.company_id, Unset):
            company_id = UNSET
        else:
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

        def _parse_alias(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        alias = _parse_alias(d.pop("alias", UNSET))

        def _parse_tax_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tax_id = _parse_tax_id(d.pop("taxId", UNSET))

        def _parse_email(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        email = _parse_email(d.pop("email", UNSET))

        def _parse_phone(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        phone = _parse_phone(d.pop("phone", UNSET))

        def _parse_country(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        country = _parse_country(d.pop("country", UNSET))

        def _parse_state(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        state = _parse_state(d.pop("state", UNSET))

        def _parse_country_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        country_name = _parse_country_name(d.pop("countryName", UNSET))

        def _parse_region_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        region_name = _parse_region_name(d.pop("regionName", UNSET))

        def _parse_city(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        city = _parse_city(d.pop("city", UNSET))

        def _parse_street(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        street = _parse_street(d.pop("street", UNSET))

        def _parse_location_admin_0_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        location_admin_0_code = _parse_location_admin_0_code(d.pop("locationAdmin0Code", UNSET))

        def _parse_location_admin_1_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        location_admin_1_code = _parse_location_admin_1_code(d.pop("locationAdmin1Code", UNSET))

        def _parse_location_admin_2_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        location_admin_2_code = _parse_location_admin_2_code(d.pop("locationAdmin2Code", UNSET))

        def _parse_notes(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        notes = _parse_notes(d.pop("notes", UNSET))

        def _parse_zip_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        zip_code = _parse_zip_code(d.pop("zipCode", UNSET))

        def _parse_website(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        website = _parse_website(d.pop("website", UNSET))

        def _parse_veeam_tenant_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        veeam_tenant_id = _parse_veeam_tenant_id(d.pop("veeamTenantId", UNSET))

        def _parse_company_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        company_id = _parse_company_id(d.pop("companyId", UNSET))

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
