from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.backup_server_license import BackupServerLicense
    from ..models.response_error import ResponseError
    from ..models.response_metadata import ResponseMetadata


T = TypeVar("T", bound="UpdateBackupServerLicenseResponse200")


@_attrs_define
class UpdateBackupServerLicenseResponse200:
    """
    Attributes:
        data (BackupServerLicense):  Example: {'backupServerUid': 'DF997BD3-4AE9-4841-8152-8FF5CC703EAB',
            'contactPerson': 'John Smith', 'edition': 'Enterprise Plus', 'company': 'Veeam', 'email':
            'John.Smith@veeam.com', 'units': 1000, 'unitType': 'Instances', 'usedUnits': 100, 'status': 'Valid',
            'cloudConnect': 'Yes', 'autoUpdateEnabled': True, 'packages': ['Suite'], 'type': 'Rental', 'supportIds':
            ['987412365'], 'licenseIds': ['514c45eb-9543-4799-8003-1e59385b774c'], 'expirationDate':
            '2018-10-24T14:00:00.0000000-07:00', 'supportExpirationDate': '2018-10-24T14:00:00.0000000-07:00'}.
        meta (Union[Unset, ResponseMetadata]):
        errors (Union[Unset, list['ResponseError']]):
    """

    data: "BackupServerLicense"
    meta: Union[Unset, "ResponseMetadata"] = UNSET
    errors: Union[Unset, list["ResponseError"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data = self.data.to_dict()

        meta: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.meta, Unset):
            meta = self.meta.to_dict()

        errors: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.errors, Unset):
            errors = []
            for errors_item_data in self.errors:
                errors_item = errors_item_data.to_dict()
                errors.append(errors_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "data": data,
            }
        )
        if meta is not UNSET:
            field_dict["meta"] = meta
        if errors is not UNSET:
            field_dict["errors"] = errors

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.backup_server_license import BackupServerLicense
        from ..models.response_error import ResponseError
        from ..models.response_metadata import ResponseMetadata

        d = dict(src_dict)
        data = BackupServerLicense.from_dict(d.pop("data"))

        _meta = d.pop("meta", UNSET)
        meta: Union[Unset, ResponseMetadata]
        if isinstance(_meta, Unset):
            meta = UNSET
        else:
            meta = ResponseMetadata.from_dict(_meta)

        errors = []
        _errors = d.pop("errors", UNSET)
        for errors_item_data in _errors or []:
            errors_item = ResponseError.from_dict(errors_item_data)

            errors.append(errors_item)

        update_backup_server_license_response_200 = cls(
            data=data,
            meta=meta,
            errors=errors,
        )

        update_backup_server_license_response_200.additional_properties = d
        return update_backup_server_license_response_200

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
