from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.webhook_auth_type import WebhookAuthType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.webhook_configuration_custom_headers import WebhookConfigurationCustomHeaders


T = TypeVar("T", bound="WebhookConfiguration")


@_attrs_define
class WebhookConfiguration:
    """
    Attributes:
        name (str): Display name of the webhook.
        url (str): Target URL for the webhook.
        auth_type (WebhookAuthType): Authentication method for the webhook.
        instance_uid (UUID | Unset): UID assigned to a webhook configuration.
        organization_uid (UUID | Unset): UID of the organization that owns this webhook.
        auth_value (str | Unset): Authentication secret (write-only, never returned in GET responses).
        custom_headers (WebhookConfigurationCustomHeaders | Unset): Custom HTTP headers to include in webhook requests.
        skip_certificate_validation (bool | Unset): Whether to skip TLS certificate validation. Default: False.
        is_enabled (bool | Unset): Whether the webhook is enabled. Default: True.
        timeout_seconds (int | Unset): Timeout in seconds for each webhook request. Default: 30.
        description (str | Unset): Description of the webhook configuration.
    """

    name: str
    url: str
    auth_type: WebhookAuthType
    instance_uid: UUID | Unset = UNSET
    organization_uid: UUID | Unset = UNSET
    auth_value: str | Unset = UNSET
    custom_headers: WebhookConfigurationCustomHeaders | Unset = UNSET
    skip_certificate_validation: bool | Unset = False
    is_enabled: bool | Unset = True
    timeout_seconds: int | Unset = 30
    description: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        url = self.url

        auth_type = self.auth_type.value

        instance_uid: str | Unset = UNSET
        if not isinstance(self.instance_uid, Unset):
            instance_uid = str(self.instance_uid)

        organization_uid: str | Unset = UNSET
        if not isinstance(self.organization_uid, Unset):
            organization_uid = str(self.organization_uid)

        auth_value = self.auth_value

        custom_headers: dict[str, Any] | Unset = UNSET
        if not isinstance(self.custom_headers, Unset):
            custom_headers = self.custom_headers.to_dict()

        skip_certificate_validation = self.skip_certificate_validation

        is_enabled = self.is_enabled

        timeout_seconds = self.timeout_seconds

        description = self.description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "url": url,
                "authType": auth_type,
            }
        )
        if instance_uid is not UNSET:
            field_dict["instanceUid"] = instance_uid
        if organization_uid is not UNSET:
            field_dict["organizationUid"] = organization_uid
        if auth_value is not UNSET:
            field_dict["authValue"] = auth_value
        if custom_headers is not UNSET:
            field_dict["customHeaders"] = custom_headers
        if skip_certificate_validation is not UNSET:
            field_dict["skipCertificateValidation"] = skip_certificate_validation
        if is_enabled is not UNSET:
            field_dict["isEnabled"] = is_enabled
        if timeout_seconds is not UNSET:
            field_dict["timeoutSeconds"] = timeout_seconds
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.webhook_configuration_custom_headers import WebhookConfigurationCustomHeaders

        d = dict(src_dict)
        name = d.pop("name")

        url = d.pop("url")

        auth_type = WebhookAuthType(d.pop("authType"))

        _instance_uid = d.pop("instanceUid", UNSET)
        instance_uid: UUID | Unset
        if isinstance(_instance_uid, Unset):
            instance_uid = UNSET
        else:
            instance_uid = UUID(_instance_uid)

        _organization_uid = d.pop("organizationUid", UNSET)
        organization_uid: UUID | Unset
        if isinstance(_organization_uid, Unset):
            organization_uid = UNSET
        else:
            organization_uid = UUID(_organization_uid)

        auth_value = d.pop("authValue", UNSET)

        _custom_headers = d.pop("customHeaders", UNSET)
        custom_headers: WebhookConfigurationCustomHeaders | Unset
        if isinstance(_custom_headers, Unset):
            custom_headers = UNSET
        else:
            custom_headers = WebhookConfigurationCustomHeaders.from_dict(_custom_headers)

        skip_certificate_validation = d.pop("skipCertificateValidation", UNSET)

        is_enabled = d.pop("isEnabled", UNSET)

        timeout_seconds = d.pop("timeoutSeconds", UNSET)

        description = d.pop("description", UNSET)

        webhook_configuration = cls(
            name=name,
            url=url,
            auth_type=auth_type,
            instance_uid=instance_uid,
            organization_uid=organization_uid,
            auth_value=auth_value,
            custom_headers=custom_headers,
            skip_certificate_validation=skip_certificate_validation,
            is_enabled=is_enabled,
            timeout_seconds=timeout_seconds,
            description=description,
        )

        webhook_configuration.additional_properties = d
        return webhook_configuration

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
