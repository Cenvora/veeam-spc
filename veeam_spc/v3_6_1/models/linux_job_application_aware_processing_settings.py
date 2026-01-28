from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.linux_my_sql_application_aware_processing_settings import LinuxMySqlApplicationAwareProcessingSettings
    from ..models.linux_oracle_application_aware_processing_settings import (
        LinuxOracleApplicationAwareProcessingSettings,
    )
    from ..models.linux_postgre_sql_application_aware_processing_settings import (
        LinuxPostgreSqlApplicationAwareProcessingSettings,
    )


T = TypeVar("T", bound="LinuxJobApplicationAwareProcessingSettings")


@_attrs_define
class LinuxJobApplicationAwareProcessingSettings:
    """
    Attributes:
        oracle_aap_settings (Union[Unset, LinuxOracleApplicationAwareProcessingSettings]):
        my_sql_aap_settings (Union[Unset, LinuxMySqlApplicationAwareProcessingSettings]):
        postgre_sql_aap_settings (Union[Unset, LinuxPostgreSqlApplicationAwareProcessingSettings]):
    """

    oracle_aap_settings: Union[Unset, "LinuxOracleApplicationAwareProcessingSettings"] = UNSET
    my_sql_aap_settings: Union[Unset, "LinuxMySqlApplicationAwareProcessingSettings"] = UNSET
    postgre_sql_aap_settings: Union[Unset, "LinuxPostgreSqlApplicationAwareProcessingSettings"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        oracle_aap_settings: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.oracle_aap_settings, Unset):
            oracle_aap_settings = self.oracle_aap_settings.to_dict()

        my_sql_aap_settings: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.my_sql_aap_settings, Unset):
            my_sql_aap_settings = self.my_sql_aap_settings.to_dict()

        postgre_sql_aap_settings: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.postgre_sql_aap_settings, Unset):
            postgre_sql_aap_settings = self.postgre_sql_aap_settings.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if oracle_aap_settings is not UNSET:
            field_dict["oracleAapSettings"] = oracle_aap_settings
        if my_sql_aap_settings is not UNSET:
            field_dict["mySqlAapSettings"] = my_sql_aap_settings
        if postgre_sql_aap_settings is not UNSET:
            field_dict["postgreSqlAapSettings"] = postgre_sql_aap_settings

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.linux_my_sql_application_aware_processing_settings import (
            LinuxMySqlApplicationAwareProcessingSettings,
        )
        from ..models.linux_oracle_application_aware_processing_settings import (
            LinuxOracleApplicationAwareProcessingSettings,
        )
        from ..models.linux_postgre_sql_application_aware_processing_settings import (
            LinuxPostgreSqlApplicationAwareProcessingSettings,
        )

        d = dict(src_dict)
        _oracle_aap_settings = d.pop("oracleAapSettings", UNSET)
        oracle_aap_settings: Union[Unset, LinuxOracleApplicationAwareProcessingSettings]
        if isinstance(_oracle_aap_settings, Unset):
            oracle_aap_settings = UNSET
        else:
            oracle_aap_settings = LinuxOracleApplicationAwareProcessingSettings.from_dict(_oracle_aap_settings)

        _my_sql_aap_settings = d.pop("mySqlAapSettings", UNSET)
        my_sql_aap_settings: Union[Unset, LinuxMySqlApplicationAwareProcessingSettings]
        if isinstance(_my_sql_aap_settings, Unset):
            my_sql_aap_settings = UNSET
        else:
            my_sql_aap_settings = LinuxMySqlApplicationAwareProcessingSettings.from_dict(_my_sql_aap_settings)

        _postgre_sql_aap_settings = d.pop("postgreSqlAapSettings", UNSET)
        postgre_sql_aap_settings: Union[Unset, LinuxPostgreSqlApplicationAwareProcessingSettings]
        if isinstance(_postgre_sql_aap_settings, Unset):
            postgre_sql_aap_settings = UNSET
        else:
            postgre_sql_aap_settings = LinuxPostgreSqlApplicationAwareProcessingSettings.from_dict(
                _postgre_sql_aap_settings
            )

        linux_job_application_aware_processing_settings = cls(
            oracle_aap_settings=oracle_aap_settings,
            my_sql_aap_settings=my_sql_aap_settings,
            postgre_sql_aap_settings=postgre_sql_aap_settings,
        )

        linux_job_application_aware_processing_settings.additional_properties = d
        return linux_job_application_aware_processing_settings

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
