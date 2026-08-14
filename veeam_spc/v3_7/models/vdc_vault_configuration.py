from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

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
        status_message (str | Unset): Status message.
        last_update (datetime.date | Unset): Date of the latest status update.
    """

    status: VdcVaultConfigurationStatus
    status_message: str | Unset = UNSET
    last_update: datetime.date | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status = self.status.value

        status_message = self.status_message

        last_update: str | Unset = UNSET
        if not isinstance(self.last_update, Unset):
            last_update = self.last_update.isoformat()

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

        status_message = d.pop("statusMessage", UNSET)

        _last_update = d.pop("lastUpdate", UNSET)
        last_update: datetime.date | Unset
        if isinstance(_last_update, Unset):
            last_update = UNSET
        else:
            last_update = isoparse(_last_update).date()

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
