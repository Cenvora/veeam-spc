from collections.abc import Mapping
from typing import Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.custom_welcome_email_template_organization_scope import CustomWelcomeEmailTemplateOrganizationScope
from ..models.custom_welcome_email_template_organization_type import CustomWelcomeEmailTemplateOrganizationType
from ..types import UNSET, Unset

T = TypeVar("T", bound="CustomWelcomeEmailTemplate")


@_attrs_define
class CustomWelcomeEmailTemplate:
    """
    Attributes:
        organization_uid (Union[Unset, UUID]): UID assigned to an organization.
        organization_type (Union[Unset, CustomWelcomeEmailTemplateOrganizationType]): Type of an organization.
        organization_scope (Union[Unset, CustomWelcomeEmailTemplateOrganizationScope]): Scope of notified organizations.
        email_content (Union[Unset, str]): Content of an email message.
        show_self_service_section (Union[Unset, bool]): Indicates whether the **Self-service** section is included in
            the email message. Default: True.
        is_default (Union[Unset, bool]): Indicates whether an email message template is selected by default. Default:
            True.
    """

    organization_uid: Union[Unset, UUID] = UNSET
    organization_type: Union[Unset, CustomWelcomeEmailTemplateOrganizationType] = UNSET
    organization_scope: Union[Unset, CustomWelcomeEmailTemplateOrganizationScope] = UNSET
    email_content: Union[Unset, str] = UNSET
    show_self_service_section: Union[Unset, bool] = True
    is_default: Union[Unset, bool] = True
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        organization_uid: Union[Unset, str] = UNSET
        if not isinstance(self.organization_uid, Unset):
            organization_uid = str(self.organization_uid)

        organization_type: Union[Unset, str] = UNSET
        if not isinstance(self.organization_type, Unset):
            organization_type = self.organization_type.value

        organization_scope: Union[Unset, str] = UNSET
        if not isinstance(self.organization_scope, Unset):
            organization_scope = self.organization_scope.value

        email_content = self.email_content

        show_self_service_section = self.show_self_service_section

        is_default = self.is_default

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if organization_uid is not UNSET:
            field_dict["organizationUid"] = organization_uid
        if organization_type is not UNSET:
            field_dict["organizationType"] = organization_type
        if organization_scope is not UNSET:
            field_dict["organizationScope"] = organization_scope
        if email_content is not UNSET:
            field_dict["emailContent"] = email_content
        if show_self_service_section is not UNSET:
            field_dict["showSelfServiceSection"] = show_self_service_section
        if is_default is not UNSET:
            field_dict["isDefault"] = is_default

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _organization_uid = d.pop("organizationUid", UNSET)
        organization_uid: Union[Unset, UUID]
        if isinstance(_organization_uid, Unset):
            organization_uid = UNSET
        else:
            organization_uid = UUID(_organization_uid)

        _organization_type = d.pop("organizationType", UNSET)
        organization_type: Union[Unset, CustomWelcomeEmailTemplateOrganizationType]
        if isinstance(_organization_type, Unset):
            organization_type = UNSET
        else:
            organization_type = CustomWelcomeEmailTemplateOrganizationType(_organization_type)

        _organization_scope = d.pop("organizationScope", UNSET)
        organization_scope: Union[Unset, CustomWelcomeEmailTemplateOrganizationScope]
        if isinstance(_organization_scope, Unset):
            organization_scope = UNSET
        else:
            organization_scope = CustomWelcomeEmailTemplateOrganizationScope(_organization_scope)

        email_content = d.pop("emailContent", UNSET)

        show_self_service_section = d.pop("showSelfServiceSection", UNSET)

        is_default = d.pop("isDefault", UNSET)

        custom_welcome_email_template = cls(
            organization_uid=organization_uid,
            organization_type=organization_type,
            organization_scope=organization_scope,
            email_content=email_content,
            show_self_service_section=show_self_service_section,
            is_default=is_default,
        )

        custom_welcome_email_template.additional_properties = d
        return custom_welcome_email_template

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
