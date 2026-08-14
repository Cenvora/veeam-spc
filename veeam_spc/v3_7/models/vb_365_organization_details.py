from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.vb_365_hybrid_organization import Vb365HybridOrganization
    from ..models.vb_365_microsoft_365_organization import Vb365Microsoft365Organization
    from ..models.vb_365_on_premises_microsoft_organization import Vb365OnPremisesMicrosoftOrganization


T = TypeVar("T", bound="Vb365OrganizationDetails")


@_attrs_define
class Vb365OrganizationDetails:
    """
    Attributes:
        microsoft_365_organization_details (Vb365Microsoft365Organization | Unset):  Example: {'isTeamsOnline': True,
            'isTeamsChatsOnline': False, 'exchangeAndSharePointOnlineConnectionSettings':
            {'modernAppOnlyAuthenticationSettings': {'configureApplication': False, 'userCode': None, 'newApplicationName':
            None, 'applicationId': 'ae61e533-82c7-4cb6-a030-78ae589cf49d', 'applicationCertificate': 'MIIEoQIBAAKCAQBJ4W/TVQ
            eIynO0BL/f/lc65mUzZmput1JCZsMLcjQB9eAteBVl5NRN4O5jUrWqXwk1IX17qtDiu3L8O07e0HlL+nHkRYeUDaztVbyhtvKc+YwNwZTQP8IvnW
            Bpgrd2uJw167I7iQ5nuN2O7QL/8idBiKhgsOKz9frPMSp/QIXA3MQoi+Yp8TiyDvGps+iMn1KpLgkHehlXUFmuZvi27T6wSZGh97rHekpIj9bSir
            ZFcG+7qupx8HFE4wNdhvxcvbmNkfMaJTmmi3YzGKYESwNyvwAIuohq1MoeQmNf1Q50NO04GOOPY+66uykOQkDkTa8/Vu90O6cux6/Ntyt04hndAg
            MBAAECggEABtA/m+HPnBHvsb5uY531NX1h/+eGEUfe0jjf7AJQQY4HaqoUbx03ZydDVO2fy2KQWtIH3IvYT9CxvglKMMpRJWynbEHtSv4n4Itzpg
            ZVQZzSCcK8kqgOpI2DArgHa2+DGIXwHgV5yp8F79Rz3l7at/R+csxdW/NnegwyuyGcNDkOjp8//HcrHQXPjljF5mwh4UZCFUvscKVjQbsOpiMvGe
            GN3z0/ZfKHi2egEA4+t1NLJykDiovNamtxE2xDkU8TXwn9STI8owzmxGtAA4HXDMuUQ0UXqxN0ED3WLJeqEKa0vuQ34+so5sa6EiwhF3q5rs0HFM
            klvUOxfnhgcpxgkQKBgQCMsiDpIh8BDKTxF20b8Az7NDtvm78vxfhF2rnCYIh9Q+3VKxbvoiNNTTJmlGT4Hi5App3l2GKIvRVZ9mE/vbtcWDk71/
            GgyiyuLixJYrY9gy2kYTz84R8v4ZMhjLB+Ba7VXkGU2u/Mj5LXzsQWCYRelC9DWlgcoReRXMHUbP4XwKBgQCGbYgE1gvW5ZYyi3xTrUIw8Bz7iUt
            bkO2Dg8egWLAYzRJizis6fd30xIG3wNheMVa/qqU3RrvS62N0QHZBjXJTH27li8JVQ9mfVbGZxcRLEwimBSEf5SNFlucwq02kvdJnL6vx5fE0XUz
            iDPcgIUF9LO+VcCFKXE7kVNn1P/KHQwKBgDsxJc9vX4Pdgfc8V9cNIyj8TJUj/UdoDo+bnhSwsIbSLlwfyHRjrbY3zsqZ4JdIQWlQ+B/dJxWm5Cz
            Z83f3/WTh3zNxlZTOID/Q/qL4Qf4DFe/4RyyyaAnUvMmcYpTcb6qrQSnJ4P0U18fyjdLQblYtpmrhK5mx7eMQq/QOwZAoGAU3ftTjtt7Ihv44CSu
            Q5KnEJrbJAKV5e8sr1/lYOcDDpBYVJsqwv+Zn4hoWw/rPTrzWTy40irVULNZSCljPx78TsCS8uk5faUSQgXl8ihoo/1/cgPklNfvFT/xkuHkXRAE
            cwa8r95Lq+EDpRIWg3sMQJW3S5brWV1ovdAwrRrLisCgYAk+F2L604Ss7zgEbBGJEQoD+OFVP29WSrKThtVLaabYP1N8qVr+W/P5ojRZ94aqZ0wB
            LfklfdejOp399llcoFoMShc1k+ScpYZb7k3cHhLGdZsm+gCNuVQZlpYWvhnSjOfEHafQRckxtPtvVTVda/uHtWNwoDv39eSXMS4WLprug==',
            'applicationCertificatePassword': 'Password1', 'sharePointSettings': {'sharePointSaveAllWebParts': False,
            'officeOrganizationName': 'mycompany.onmicrosoft.com'}, 'exchangeSettings': {'account':
            'admin@mycompany.onmicrosoft.com'}}, 'modernAuthenticationWithLegacyProtocolsSettings': None,
            'basicAuthenticationSettings': None}, 'region': 'Default'}.
        on_premises_organization_details (Vb365OnPremisesMicrosoftOrganization | Unset):
        hybrid_organization_details (Vb365HybridOrganization | Unset):
    """

    microsoft_365_organization_details: Vb365Microsoft365Organization | Unset = UNSET
    on_premises_organization_details: Vb365OnPremisesMicrosoftOrganization | Unset = UNSET
    hybrid_organization_details: Vb365HybridOrganization | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        microsoft_365_organization_details: dict[str, Any] | Unset = UNSET
        if not isinstance(self.microsoft_365_organization_details, Unset):
            microsoft_365_organization_details = self.microsoft_365_organization_details.to_dict()

        on_premises_organization_details: dict[str, Any] | Unset = UNSET
        if not isinstance(self.on_premises_organization_details, Unset):
            on_premises_organization_details = self.on_premises_organization_details.to_dict()

        hybrid_organization_details: dict[str, Any] | Unset = UNSET
        if not isinstance(self.hybrid_organization_details, Unset):
            hybrid_organization_details = self.hybrid_organization_details.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if microsoft_365_organization_details is not UNSET:
            field_dict["microsoft365OrganizationDetails"] = microsoft_365_organization_details
        if on_premises_organization_details is not UNSET:
            field_dict["onPremisesOrganizationDetails"] = on_premises_organization_details
        if hybrid_organization_details is not UNSET:
            field_dict["hybridOrganizationDetails"] = hybrid_organization_details

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.vb_365_hybrid_organization import Vb365HybridOrganization
        from ..models.vb_365_microsoft_365_organization import Vb365Microsoft365Organization
        from ..models.vb_365_on_premises_microsoft_organization import Vb365OnPremisesMicrosoftOrganization

        d = dict(src_dict)
        _microsoft_365_organization_details = d.pop("microsoft365OrganizationDetails", UNSET)
        microsoft_365_organization_details: Vb365Microsoft365Organization | Unset
        if isinstance(_microsoft_365_organization_details, Unset):
            microsoft_365_organization_details = UNSET
        else:
            microsoft_365_organization_details = Vb365Microsoft365Organization.from_dict(
                _microsoft_365_organization_details
            )

        _on_premises_organization_details = d.pop("onPremisesOrganizationDetails", UNSET)
        on_premises_organization_details: Vb365OnPremisesMicrosoftOrganization | Unset
        if isinstance(_on_premises_organization_details, Unset):
            on_premises_organization_details = UNSET
        else:
            on_premises_organization_details = Vb365OnPremisesMicrosoftOrganization.from_dict(
                _on_premises_organization_details
            )

        _hybrid_organization_details = d.pop("hybridOrganizationDetails", UNSET)
        hybrid_organization_details: Vb365HybridOrganization | Unset
        if isinstance(_hybrid_organization_details, Unset):
            hybrid_organization_details = UNSET
        else:
            hybrid_organization_details = Vb365HybridOrganization.from_dict(_hybrid_organization_details)

        vb_365_organization_details = cls(
            microsoft_365_organization_details=microsoft_365_organization_details,
            on_premises_organization_details=on_premises_organization_details,
            hybrid_organization_details=hybrid_organization_details,
        )

        vb_365_organization_details.additional_properties = d
        return vb_365_organization_details

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
