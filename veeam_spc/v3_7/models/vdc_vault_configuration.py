from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.vdc_vault_configuration_status import VdcVaultConfigurationStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="VdcVaultConfiguration")


@_attrs_define
class VdcVaultConfiguration:
    """
    Attributes:
        status (VdcVaultConfigurationStatus): Status of the Veeam Data Cloud Vault configuration.
        status_message (None | str | Unset): Status message.
        last_update (datetime.date | None | Unset): Date of the latest status update.
    """

    status: VdcVaultConfigurationStatus
    status_message: None | str | Unset = UNSET
    last_update: datetime.date | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status = self.status.value

        status_message: None | str | Unset
        if isinstance(self.status_message, Unset):
            status_message = UNSET
        else:
            status_message = self.status_message

        last_update: None | str | Unset
        if isinstance(self.last_update, Unset):
            last_update = UNSET
        elif isinstance(self.last_update, datetime.date):
            last_update = self.last_update.isoformat()
        else:
            last_update = self.last_update

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "status": status,
            }
        )
        if status_message is not UNSET:
            field_dict["statusMessage"] = status_message
        if last_update is not UNSET:
            field_dict["lastUpdate"] = last_update

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        status = VdcVaultConfigurationStatus(d.pop("status"))

        def _parse_status_message(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        status_message = _parse_status_message(d.pop("statusMessage", UNSET))

        def _parse_last_update(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_update_type_0 = isoparse(data).date()

                return last_update_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        last_update = _parse_last_update(d.pop("lastUpdate", UNSET))

        vdc_vault_configuration = cls(
            status=status,
            status_message=status_message,
            last_update=last_update,
        )

        vdc_vault_configuration.additional_properties = d
        return vdc_vault_configuration

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
