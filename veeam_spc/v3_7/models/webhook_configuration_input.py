from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.webhook_auth_type import WebhookAuthType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.webhook_configuration_input_custom_headers_type_0 import WebhookConfigurationInputCustomHeadersType0


T = TypeVar("T", bound="WebhookConfigurationInput")


@_attrs_define
class WebhookConfigurationInput:
    """
    Example:
        {'name': 'Critical Alarms to PagerDuty', 'url': 'https://hooks.tech.local/services/T01ABCD/B02EFGH/notify',
            'authType': 'BearerToken', 'authValue': 'Bearer eyJhbGciOiJIUzI1Niwic2VjcmV0LXRva2VuLXZhbHVl', 'customHeaders':
            {'X-Source': 'VSPC', 'X-Environment': 'production'}, 'skipCertificateValidation': False, 'isEnabled': True,
            'timeoutSeconds': 30, 'description': 'Forwards critical alarm notifications to the operations PagerDuty
            endpoint.'}

    Attributes:
        name (str): Display name of the webhook.
        url (str): Target URL for the webhook.
        auth_type (WebhookAuthType): Authentication method for the webhook.
        auth_value (None | str | Unset): Authentication secret.
        custom_headers (None | Unset | WebhookConfigurationInputCustomHeadersType0): Custom HTTP headers to include in
            webhook requests.
        skip_certificate_validation (bool | Unset): Whether to skip TLS certificate validation. Default: False.
        is_enabled (bool | Unset): Whether the webhook is enabled. Default: True.
        timeout_seconds (int | Unset): Timeout in seconds for each webhook request. Default: 30.
        description (None | str | Unset): Description of the webhook configuration.
    """

    name: str
    url: str
    auth_type: WebhookAuthType
    auth_value: None | str | Unset = UNSET
    custom_headers: None | Unset | WebhookConfigurationInputCustomHeadersType0 = UNSET
    skip_certificate_validation: bool | Unset = False
    is_enabled: bool | Unset = True
    timeout_seconds: int | Unset = 30
    description: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.webhook_configuration_input_custom_headers_type_0 import (
            WebhookConfigurationInputCustomHeadersType0,
        )

        name = self.name

        url = self.url

        auth_type = self.auth_type.value

        auth_value: None | str | Unset
        if isinstance(self.auth_value, Unset):
            auth_value = UNSET
        else:
            auth_value = self.auth_value

        custom_headers: dict[str, Any] | None | Unset
        if isinstance(self.custom_headers, Unset):
            custom_headers = UNSET
        elif isinstance(self.custom_headers, WebhookConfigurationInputCustomHeadersType0):
            custom_headers = self.custom_headers.to_dict()
        else:
            custom_headers = self.custom_headers

        skip_certificate_validation = self.skip_certificate_validation

        is_enabled = self.is_enabled

        timeout_seconds = self.timeout_seconds

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
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
        from ..models.webhook_configuration_input_custom_headers_type_0 import (
            WebhookConfigurationInputCustomHeadersType0,
        )

        d = dict(src_dict)
        name = d.pop("name")

        url = d.pop("url")

        auth_type = WebhookAuthType(d.pop("authType"))

        def _parse_auth_value(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        auth_value = _parse_auth_value(d.pop("authValue", UNSET))

        def _parse_custom_headers(data: object) -> None | Unset | WebhookConfigurationInputCustomHeadersType0:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                custom_headers_type_0 = WebhookConfigurationInputCustomHeadersType0.from_dict(data)

                return custom_headers_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | WebhookConfigurationInputCustomHeadersType0, data)

        custom_headers = _parse_custom_headers(d.pop("customHeaders", UNSET))

        skip_certificate_validation = d.pop("skipCertificateValidation", UNSET)

        is_enabled = d.pop("isEnabled", UNSET)

        timeout_seconds = d.pop("timeoutSeconds", UNSET)

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        webhook_configuration_input = cls(
            name=name,
            url=url,
            auth_type=auth_type,
            auth_value=auth_value,
            custom_headers=custom_headers,
            skip_certificate_validation=skip_certificate_validation,
            is_enabled=is_enabled,
            timeout_seconds=timeout_seconds,
            description=description,
        )

        webhook_configuration_input.additional_properties = d
        return webhook_configuration_input

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
