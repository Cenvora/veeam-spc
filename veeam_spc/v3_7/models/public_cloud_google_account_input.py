from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PublicCloudGoogleAccountInput")


@_attrs_define
class PublicCloudGoogleAccountInput:
    r"""
    Example:
        {'name': 'Provider', 'description': 'Provider Account', 'jsonConfiguration': '{"type":"service_account","project
            _id":"vspc","private_key_id":"4a79cbf96aa94266407fa1a8fd39d6983989fd8","private_key":"-----BEGINPRIVATEKEY-----
            \\nMIIEowIBAAKCAQEAsUyvEXIzY2iHzUwtNCUTUDEGeEaWt667b8tbbehcmJmieP42T5bh0lIWvET9h03LGutYD4f0lH74EihHaBHt45B4ei9Ei
            JGATPgLfdc4MOsiQcbf6HjrkuVzru4SDnesUEkDYczXNh/int7Uvuhafv0hKu3ZOfQPtPmJKBc+fQCBt6ZgSxQ1BqOR+p8MCkxxVr4zUphsQCU+k
            CWzilyPlFHSKtb/JggDGMnLiZiY1MnU1FkC4rTY2COlcNzq8PtEF6BuAO1L1788eh+h2oesG78kttuNmtTrXFlaCFzwOGmoKg2aAPIJVYNt5V3Ve
            vm9kzcx5BAjeiKUZipGH8XQIDAQABAoIBABlUflJ8wVC7d2NiNbcUcOztBCKc2x2E7ixrnjVWlBwNHwQwNWwrfznAFpVxOdNhztmas+sMHmo0tZZ
            KgOEiZp0zX7L9G8pzFyRn76Rb4iBDB5LkKcsZs3Y6J8vfIV9Fw614sO4BCOInrgXKihR4N62a1mk+r+EyuCe/2tOKdpf/BKjGLX9hhEglMFpscsC
            K6vMya+Eo1mpjTlqsTCQQEs031kRCcRFq4VBaLx/xgCAVLA0vTBUeGV7hx/VpGU3yy+flI+O3ny6lwaThe6ulkh3Y7S/dAyp6JYt/kmi6ZD0My8x
            TiOd4fw+zqDrt5UtROGAVMKHpCT7g9ElyGTLsTUCgYEA1sxtK2U/PVWsjq/ZK388zuSJ2QXMch+65xM+JZkPtbohzjlIFmGGyTN+kkMC3H1/xe+/
            y0GrB9OdzqLqiQQhOkXkzHuMAbqGoGKcywO1KqrKeD1C3Z4/ha4yLALF5M/ihCvCZ2k5mmfwCKX+5+kPhaqUOeJoO0C4DxLwdiI508CgYEA007jZ
            qvy/3ct2LtREZgqsHggoyZOtYwtL8bvNuIMX/Z/fDlsdhjqFJCmYzgmVzpGpruac9dSBdPbOIs6cnkdnvdttwPgX9lrlW7DXFNCiXWdCTN7UlVDI
            KRCDjIlVKgsoI7EKewT6oGzjfhgejTRp4a8XvQfxqUWVOx4cIy9tpMCgYEAl2h5+4De1ukxPVMPDe4eeuf1kxjXSAq9wGx8dqPL/c+XENo2CFuSg
            EetOaOL7fVipXGjnFOsxF88/CY0lLXfPxDfIU6sywXUtuJhKVYBDj9Pb7G2iWH1X4W8sxoEd5W/0B56g5ivyArkJJc98oxRRcLMQ0MybFElGdLmw
            7lSp1kCgYB08nE6jqnTJ3ORQsJwWWYu+p0djoL7SVRs383e8yZkKfmOl/1mMw3CSfg8a4QUvKUDfErUF/RGU2U9mxjC6DMzmr73Dkcs5Rj8wCuRO
            mdVymkaAYscGyImu6HvV2N/wf/I8JqylPzEyfnE9hT3Lapm7FPuvW+kshN09tcFe283zwKBgBg/NFAjO0CniYina6FM9KH4uk//5JZ9nXV9nkBRi
            ykIzeWURcf1WfbpPIeQgIcx6/CKb/Peay41OIvN2gegyhLFaPbylN1xkBq9Yc5xkxKapReH+yIoiwO86Cc4QJVjLp3pQBy0+lXRwyRMg5sEcBQeQ
            GBu5JpJh0hQTQ0Drj+i\\n-----ENDPRIVATEKEY-----
            \\n","client_email":"provider@mycompany.iam.gserviceaccount.com","client_id":"218140769437899532786","auth_uri":
            "https://accounts.google.com/o/oauth2/auth","token_uri":"https://oauth2.googleapis.com/token","auth_provider_x50
            9_cert_url":"https://www.googleapis.com/oauth2/v1/certs","client_x509_cert_url":"https://www.googleapis.com/robo
            t/v1/metadata/x509/provider%40mycompany.iam.gserviceaccount.com","universe_domain":"googleapis.com"}'}

    Attributes:
        name (str): Name of a Google Cloud account.
        json_configuration (str): Configuration file of a Google Cloud account in the `JSON` format.
        description (str | Unset): Description of a Google Cloud account.
    """

    name: str
    json_configuration: str
    description: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        json_configuration = self.json_configuration

        description = self.description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "jsonConfiguration": json_configuration,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        json_configuration = d.pop("jsonConfiguration")

        description = d.pop("description", UNSET)

        public_cloud_google_account_input = cls(
            name=name,
            json_configuration=json_configuration,
            description=description,
        )

        public_cloud_google_account_input.additional_properties = d
        return public_cloud_google_account_input

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
