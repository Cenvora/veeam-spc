from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.response_error import ResponseError
    from ..models.response_metadata_type_0 import ResponseMetadataType0
    from ..models.vb_365_microsoft_365_organization import Vb365Microsoft365Organization


T = TypeVar("T", bound="CreateVb365Microsoft365OrganizationResponse200")


@_attrs_define
class CreateVb365Microsoft365OrganizationResponse200:
    """
    Attributes:
        data (Vb365Microsoft365Organization):  Example: {'isTeamsOnline': True, 'isTeamsChatsOnline': False,
            'exchangeAndSharePointOnlineConnectionSettings': {'modernAppOnlyAuthenticationSettings':
            {'configureApplication': False, 'userCode': None, 'newApplicationName': None, 'applicationId':
            'ae61e533-82c7-4cb6-a030-78ae589cf49d', 'applicationCertificate': 'MIIEoQIBAAKCAQBJ4W/TVQeIynO0BL/f/lc65mUzZmput
            1JCZsMLcjQB9eAteBVl5NRN4O5jUrWqXwk1IX17qtDiu3L8O07e0HlL+nHkRYeUDaztVbyhtvKc+YwNwZTQP8IvnWBpgrd2uJw167I7iQ5nuN2O7
            QL/8idBiKhgsOKz9frPMSp/QIXA3MQoi+Yp8TiyDvGps+iMn1KpLgkHehlXUFmuZvi27T6wSZGh97rHekpIj9bSirZFcG+7qupx8HFE4wNdhvxcv
            bmNkfMaJTmmi3YzGKYESwNyvwAIuohq1MoeQmNf1Q50NO04GOOPY+66uykOQkDkTa8/Vu90O6cux6/Ntyt04hndAgMBAAECggEABtA/m+HPnBHvs
            b5uY531NX1h/+eGEUfe0jjf7AJQQY4HaqoUbx03ZydDVO2fy2KQWtIH3IvYT9CxvglKMMpRJWynbEHtSv4n4ItzpgZVQZzSCcK8kqgOpI2DArgHa
            2+DGIXwHgV5yp8F79Rz3l7at/R+csxdW/NnegwyuyGcNDkOjp8//HcrHQXPjljF5mwh4UZCFUvscKVjQbsOpiMvGeGN3z0/ZfKHi2egEA4+t1NLJ
            ykDiovNamtxE2xDkU8TXwn9STI8owzmxGtAA4HXDMuUQ0UXqxN0ED3WLJeqEKa0vuQ34+so5sa6EiwhF3q5rs0HFMklvUOxfnhgcpxgkQKBgQCMs
            iDpIh8BDKTxF20b8Az7NDtvm78vxfhF2rnCYIh9Q+3VKxbvoiNNTTJmlGT4Hi5App3l2GKIvRVZ9mE/vbtcWDk71/GgyiyuLixJYrY9gy2kYTz84
            R8v4ZMhjLB+Ba7VXkGU2u/Mj5LXzsQWCYRelC9DWlgcoReRXMHUbP4XwKBgQCGbYgE1gvW5ZYyi3xTrUIw8Bz7iUtbkO2Dg8egWLAYzRJizis6fd
            30xIG3wNheMVa/qqU3RrvS62N0QHZBjXJTH27li8JVQ9mfVbGZxcRLEwimBSEf5SNFlucwq02kvdJnL6vx5fE0XUziDPcgIUF9LO+VcCFKXE7kVN
            n1P/KHQwKBgDsxJc9vX4Pdgfc8V9cNIyj8TJUj/UdoDo+bnhSwsIbSLlwfyHRjrbY3zsqZ4JdIQWlQ+B/dJxWm5CzZ83f3/WTh3zNxlZTOID/Q/q
            L4Qf4DFe/4RyyyaAnUvMmcYpTcb6qrQSnJ4P0U18fyjdLQblYtpmrhK5mx7eMQq/QOwZAoGAU3ftTjtt7Ihv44CSuQ5KnEJrbJAKV5e8sr1/lYOc
            DDpBYVJsqwv+Zn4hoWw/rPTrzWTy40irVULNZSCljPx78TsCS8uk5faUSQgXl8ihoo/1/cgPklNfvFT/xkuHkXRAEcwa8r95Lq+EDpRIWg3sMQJW
            3S5brWV1ovdAwrRrLisCgYAk+F2L604Ss7zgEbBGJEQoD+OFVP29WSrKThtVLaabYP1N8qVr+W/P5ojRZ94aqZ0wBLfklfdejOp399llcoFoMShc
            1k+ScpYZb7k3cHhLGdZsm+gCNuVQZlpYWvhnSjOfEHafQRckxtPtvVTVda/uHtWNwoDv39eSXMS4WLprug==',
            'applicationCertificatePassword': 'Password1', 'sharePointSettings': {'sharePointSaveAllWebParts': False,
            'officeOrganizationName': 'mycompany.onmicrosoft.com'}, 'exchangeSettings': {'account':
            'admin@mycompany.onmicrosoft.com'}}, 'modernAuthenticationWithLegacyProtocolsSettings': None,
            'basicAuthenticationSettings': None}, 'region': 'Default'}.
        meta (None | ResponseMetadataType0 | Unset):
        errors (list[ResponseError] | None | Unset):
    """

    data: Vb365Microsoft365Organization
    meta: None | ResponseMetadataType0 | Unset = UNSET
    errors: list[ResponseError] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.response_metadata_type_0 import ResponseMetadataType0

        data = self.data.to_dict()

        meta: dict[str, Any] | None | Unset
        if isinstance(self.meta, Unset):
            meta = UNSET
        elif isinstance(self.meta, ResponseMetadataType0):
            meta = self.meta.to_dict()
        else:
            meta = self.meta

        errors: list[dict[str, Any]] | None | Unset
        if isinstance(self.errors, Unset):
            errors = UNSET
        elif isinstance(self.errors, list):
            errors = []
            for errors_type_0_item_data in self.errors:
                errors_type_0_item = errors_type_0_item_data.to_dict()
                errors.append(errors_type_0_item)

        else:
            errors = self.errors

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
        from ..models.response_error import ResponseError
        from ..models.response_metadata_type_0 import ResponseMetadataType0
        from ..models.vb_365_microsoft_365_organization import Vb365Microsoft365Organization

        d = dict(src_dict)
        data = Vb365Microsoft365Organization.from_dict(d.pop("data"))

        def _parse_meta(data: object) -> None | ResponseMetadataType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_response_metadata_type_0 = ResponseMetadataType0.from_dict(data)

                return componentsschemas_response_metadata_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | ResponseMetadataType0 | Unset, data)

        meta = _parse_meta(d.pop("meta", UNSET))

        def _parse_errors(data: object) -> list[ResponseError] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                errors_type_0 = []
                _errors_type_0 = data
                for errors_type_0_item_data in _errors_type_0:
                    errors_type_0_item = ResponseError.from_dict(errors_type_0_item_data)

                    errors_type_0.append(errors_type_0_item)

                return errors_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ResponseError] | None | Unset, data)

        errors = _parse_errors(d.pop("errors", UNSET))

        create_vb_365_microsoft_365_organization_response_200 = cls(
            data=data,
            meta=meta,
            errors=errors,
        )

        create_vb_365_microsoft_365_organization_response_200.additional_properties = d
        return create_vb_365_microsoft_365_organization_response_200

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
