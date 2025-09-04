from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.organization_type import OrganizationType
from ..types import UNSET, Unset

T = TypeVar("T", bound="Organization")


@_attrs_define
class Organization:
    """
    Attributes:
        name (str): Name of an organization.
        instance_uid (Union[Unset, UUID]): UID assigned to an organization.
        alias (Union[None, Unset, str]): Alias of an organization.
        type_ (Union[Unset, OrganizationType]): Type of an organization.
        tax_id (Union[None, Unset, str]): Organization Tax ID.
        email (Union[None, Unset, str]): Contact email address.
        phone (Union[None, Unset, str]): Telephone number of a primary contact of an organization.
        country (Union[None, Unset, int]): System ID assigned to an organization country of residence.
        state (Union[None, Unset, int]): System ID assigned to a USA state where an organization is located.
        country_name (Union[None, Unset, str]): Country name.
        region_name (Union[None, Unset, str]): Region name.
        city (Union[None, Unset, str]): City where an organization is located.
        street (Union[None, Unset, str]): Street where an organization is located.
        location_admin_0_code (Union[None, Unset, str]): Code of a country where an organization is located.
        location_admin_1_code (Union[None, Unset, str]): Code of a state, region or area where an organization is
            located.
        location_admin_2_code (Union[None, Unset, str]): Code of a district or municipality where an organization is
            located.
        notes (Union[None, Unset, str]): Additional information about an organization.
        zip_code (Union[None, Unset, str]): Postal code.
        website (Union[None, Unset, str]): Organization website.
        veeam_tenant_id (Union[None, Unset, str]): ID of an organization used in Veeam records.
        company_id (Union[None, Unset, str]): ID of an organization used for 3rd party applications.
    """

    name: str
    instance_uid: Union[Unset, UUID] = UNSET
    alias: Union[None, Unset, str] = UNSET
    type_: Union[Unset, OrganizationType] = UNSET
    tax_id: Union[None, Unset, str] = UNSET
    email: Union[None, Unset, str] = UNSET
    phone: Union[None, Unset, str] = UNSET
    country: Union[None, Unset, int] = UNSET
    state: Union[None, Unset, int] = UNSET
    country_name: Union[None, Unset, str] = UNSET
    region_name: Union[None, Unset, str] = UNSET
    city: Union[None, Unset, str] = UNSET
    street: Union[None, Unset, str] = UNSET
    location_admin_0_code: Union[None, Unset, str] = UNSET
    location_admin_1_code: Union[None, Unset, str] = UNSET
    location_admin_2_code: Union[None, Unset, str] = UNSET
    notes: Union[None, Unset, str] = UNSET
    zip_code: Union[None, Unset, str] = UNSET
    website: Union[None, Unset, str] = UNSET
    veeam_tenant_id: Union[None, Unset, str] = UNSET
    company_id: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        instance_uid: Union[Unset, str] = UNSET
        if not isinstance(self.instance_uid, Unset):
            instance_uid = str(self.instance_uid)

        alias: Union[None, Unset, str]
        if isinstance(self.alias, Unset):
            alias = UNSET
        else:
            alias = self.alias

        type_: Union[Unset, str] = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        tax_id: Union[None, Unset, str]
        if isinstance(self.tax_id, Unset):
            tax_id = UNSET
        else:
            tax_id = self.tax_id

        email: Union[None, Unset, str]
        if isinstance(self.email, Unset):
            email = UNSET
        else:
            email = self.email

        phone: Union[None, Unset, str]
        if isinstance(self.phone, Unset):
            phone = UNSET
        else:
            phone = self.phone

        country: Union[None, Unset, int]
        if isinstance(self.country, Unset):
            country = UNSET
        else:
            country = self.country

        state: Union[None, Unset, int]
        if isinstance(self.state, Unset):
            state = UNSET
        else:
            state = self.state

        country_name: Union[None, Unset, str]
        if isinstance(self.country_name, Unset):
            country_name = UNSET
        else:
            country_name = self.country_name

        region_name: Union[None, Unset, str]
        if isinstance(self.region_name, Unset):
            region_name = UNSET
        else:
            region_name = self.region_name

        city: Union[None, Unset, str]
        if isinstance(self.city, Unset):
            city = UNSET
        else:
            city = self.city

        street: Union[None, Unset, str]
        if isinstance(self.street, Unset):
            street = UNSET
        else:
            street = self.street

        location_admin_0_code: Union[None, Unset, str]
        if isinstance(self.location_admin_0_code, Unset):
            location_admin_0_code = UNSET
        else:
            location_admin_0_code = self.location_admin_0_code

        location_admin_1_code: Union[None, Unset, str]
        if isinstance(self.location_admin_1_code, Unset):
            location_admin_1_code = UNSET
        else:
            location_admin_1_code = self.location_admin_1_code

        location_admin_2_code: Union[None, Unset, str]
        if isinstance(self.location_admin_2_code, Unset):
            location_admin_2_code = UNSET
        else:
            location_admin_2_code = self.location_admin_2_code

        notes: Union[None, Unset, str]
        if isinstance(self.notes, Unset):
            notes = UNSET
        else:
            notes = self.notes

        zip_code: Union[None, Unset, str]
        if isinstance(self.zip_code, Unset):
            zip_code = UNSET
        else:
            zip_code = self.zip_code

        website: Union[None, Unset, str]
        if isinstance(self.website, Unset):
            website = UNSET
        else:
            website = self.website

        veeam_tenant_id: Union[None, Unset, str]
        if isinstance(self.veeam_tenant_id, Unset):
            veeam_tenant_id = UNSET
        else:
            veeam_tenant_id = self.veeam_tenant_id

        company_id: Union[None, Unset, str]
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
        if instance_uid is not UNSET:
            field_dict["instanceUid"] = instance_uid
        if alias is not UNSET:
            field_dict["alias"] = alias
        if type_ is not UNSET:
            field_dict["type"] = type_
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

        _instance_uid = d.pop("instanceUid", UNSET)
        instance_uid: Union[Unset, UUID]
        if isinstance(_instance_uid, Unset):
            instance_uid = UNSET
        else:
            instance_uid = UUID(_instance_uid)

        def _parse_alias(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        alias = _parse_alias(d.pop("alias", UNSET))

        _type_ = d.pop("type", UNSET)
        type_: Union[Unset, OrganizationType]
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = OrganizationType(_type_)

        def _parse_tax_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        tax_id = _parse_tax_id(d.pop("taxId", UNSET))

        def _parse_email(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        email = _parse_email(d.pop("email", UNSET))

        def _parse_phone(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        phone = _parse_phone(d.pop("phone", UNSET))

        def _parse_country(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        country = _parse_country(d.pop("country", UNSET))

        def _parse_state(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        state = _parse_state(d.pop("state", UNSET))

        def _parse_country_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        country_name = _parse_country_name(d.pop("countryName", UNSET))

        def _parse_region_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        region_name = _parse_region_name(d.pop("regionName", UNSET))

        def _parse_city(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        city = _parse_city(d.pop("city", UNSET))

        def _parse_street(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        street = _parse_street(d.pop("street", UNSET))

        def _parse_location_admin_0_code(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        location_admin_0_code = _parse_location_admin_0_code(d.pop("locationAdmin0Code", UNSET))

        def _parse_location_admin_1_code(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        location_admin_1_code = _parse_location_admin_1_code(d.pop("locationAdmin1Code", UNSET))

        def _parse_location_admin_2_code(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        location_admin_2_code = _parse_location_admin_2_code(d.pop("locationAdmin2Code", UNSET))

        def _parse_notes(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        notes = _parse_notes(d.pop("notes", UNSET))

        def _parse_zip_code(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        zip_code = _parse_zip_code(d.pop("zipCode", UNSET))

        def _parse_website(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        website = _parse_website(d.pop("website", UNSET))

        def _parse_veeam_tenant_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        veeam_tenant_id = _parse_veeam_tenant_id(d.pop("veeamTenantId", UNSET))

        def _parse_company_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        company_id = _parse_company_id(d.pop("companyId", UNSET))

        organization = cls(
            name=name,
            instance_uid=instance_uid,
            alias=alias,
            type_=type_,
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

        organization.additional_properties = d
        return organization

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
