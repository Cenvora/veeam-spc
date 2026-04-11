from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.vbr_deployment_license_settings_license_source import VbrDeploymentLicenseSettingsLicenseSource
from ..types import UNSET, Unset

T = TypeVar("T", bound="VbrDeploymentLicenseSettings")


@_attrs_define
class VbrDeploymentLicenseSettings:
    """
    Attributes:
        license_source (VbrDeploymentLicenseSettingsLicenseSource): Source of a license file.
        license_file_content (None | str | Unset): License file content in the Base64 format.
        license_uid (None | Unset | UUID): UID assigned to a license.
    """

    license_source: VbrDeploymentLicenseSettingsLicenseSource
    license_file_content: None | str | Unset = UNSET
    license_uid: None | Unset | UUID = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        license_source = self.license_source.value

        license_file_content: None | str | Unset
        if isinstance(self.license_file_content, Unset):
            license_file_content = UNSET
        else:
            license_file_content = self.license_file_content

        license_uid: None | str | Unset
        if isinstance(self.license_uid, Unset):
            license_uid = UNSET
        elif isinstance(self.license_uid, UUID):
            license_uid = str(self.license_uid)
        else:
            license_uid = self.license_uid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "licenseSource": license_source,
            }
        )
        if license_file_content is not UNSET:
            field_dict["licenseFileContent"] = license_file_content
        if license_uid is not UNSET:
            field_dict["licenseUid"] = license_uid

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        license_source = VbrDeploymentLicenseSettingsLicenseSource(d.pop("licenseSource"))

        def _parse_license_file_content(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        license_file_content = _parse_license_file_content(d.pop("licenseFileContent", UNSET))

        def _parse_license_uid(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                license_uid_type_0 = UUID(data)

                return license_uid_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        license_uid = _parse_license_uid(d.pop("licenseUid", UNSET))

        vbr_deployment_license_settings = cls(
            license_source=license_source,
            license_file_content=license_file_content,
            license_uid=license_uid,
        )

        vbr_deployment_license_settings.additional_properties = d
        return vbr_deployment_license_settings

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
