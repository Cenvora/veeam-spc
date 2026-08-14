from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.create_public_cloud_google_account_response_200 import CreatePublicCloudGoogleAccountResponse200
from ...models.error_response import ErrorResponse
from ...models.public_cloud_google_account_input import PublicCloudGoogleAccountInput
from ...types import UNSET, Response, Unset


def _get_kwargs(
    site_uid: UUID,
    *,
    body: PublicCloudGoogleAccountInput,
    select: str | Unset = UNSET,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_request_id, Unset):
        headers["X-Request-id"] = x_request_id

    if not isinstance(x_client_version, Unset):
        headers["X-Client-Version"] = x_client_version

    params: dict[str, Any] = {}

    params["select"] = select

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/infrastructure/sites/{site_uid}/publicCloud/google/accounts".format(
            site_uid=quote(str(site_uid), safe=""),
        ),
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | CreatePublicCloudGoogleAccountResponse200 | ErrorResponse:
    if response.status_code == 200:
        response_200 = CreatePublicCloudGoogleAccountResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 202:
        response_202 = cast(Any, None)
        return response_202

    response_default = ErrorResponse.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | CreatePublicCloudGoogleAccountResponse200 | ErrorResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    site_uid: UUID,
    *,
    client: AuthenticatedClient,
    body: PublicCloudGoogleAccountInput,
    select: str | Unset = UNSET,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Response[Any | CreatePublicCloudGoogleAccountResponse200 | ErrorResponse]:
    r"""Create Google Cloud Account

     Creates a Google Cloud account in a Veeam Cloud Connect site with the specified UID.

    Args:
        site_uid (UUID):
        select (str | Unset):
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):
        body (PublicCloudGoogleAccountInput):  Example: {'name': 'Provider', 'description':
            'Provider Account', 'jsonConfiguration': '{"type":"service_account","project_id":"vspc","p
            rivate_key_id":"4a79cbf96aa94266407fa1a8fd39d6983989fd8","private_key":"-----BEGINPRIVATEK
            EY-----
            \\nMIIEowIBAAKCAQEAsUyvEXIzY2iHzUwtNCUTUDEGeEaWt667b8tbbehcmJmieP42T5bh0lIWvET9h03LGutYD4f
            0lH74EihHaBHt45B4ei9EiJGATPgLfdc4MOsiQcbf6HjrkuVzru4SDnesUEkDYczXNh/int7Uvuhafv0hKu3ZOfQPt
            PmJKBc+fQCBt6ZgSxQ1BqOR+p8MCkxxVr4zUphsQCU+kCWzilyPlFHSKtb/JggDGMnLiZiY1MnU1FkC4rTY2COlcNz
            q8PtEF6BuAO1L1788eh+h2oesG78kttuNmtTrXFlaCFzwOGmoKg2aAPIJVYNt5V3Vevm9kzcx5BAjeiKUZipGH8XQI
            DAQABAoIBABlUflJ8wVC7d2NiNbcUcOztBCKc2x2E7ixrnjVWlBwNHwQwNWwrfznAFpVxOdNhztmas+sMHmo0tZZKg
            OEiZp0zX7L9G8pzFyRn76Rb4iBDB5LkKcsZs3Y6J8vfIV9Fw614sO4BCOInrgXKihR4N62a1mk+r+EyuCe/2tOKdpf
            /BKjGLX9hhEglMFpscsCK6vMya+Eo1mpjTlqsTCQQEs031kRCcRFq4VBaLx/xgCAVLA0vTBUeGV7hx/VpGU3yy+flI
            +O3ny6lwaThe6ulkh3Y7S/dAyp6JYt/kmi6ZD0My8xTiOd4fw+zqDrt5UtROGAVMKHpCT7g9ElyGTLsTUCgYEA1sxt
            K2U/PVWsjq/ZK388zuSJ2QXMch+65xM+JZkPtbohzjlIFmGGyTN+kkMC3H1/xe+/y0GrB9OdzqLqiQQhOkXkzHuMAb
            qGoGKcywO1KqrKeD1C3Z4/ha4yLALF5M/ihCvCZ2k5mmfwCKX+5+kPhaqUOeJoO0C4DxLwdiI508CgYEA007jZqvy/
            3ct2LtREZgqsHggoyZOtYwtL8bvNuIMX/Z/fDlsdhjqFJCmYzgmVzpGpruac9dSBdPbOIs6cnkdnvdttwPgX9lrlW7
            DXFNCiXWdCTN7UlVDIKRCDjIlVKgsoI7EKewT6oGzjfhgejTRp4a8XvQfxqUWVOx4cIy9tpMCgYEAl2h5+4De1ukxP
            VMPDe4eeuf1kxjXSAq9wGx8dqPL/c+XENo2CFuSgEetOaOL7fVipXGjnFOsxF88/CY0lLXfPxDfIU6sywXUtuJhKVY
            BDj9Pb7G2iWH1X4W8sxoEd5W/0B56g5ivyArkJJc98oxRRcLMQ0MybFElGdLmw7lSp1kCgYB08nE6jqnTJ3ORQsJwW
            WYu+p0djoL7SVRs383e8yZkKfmOl/1mMw3CSfg8a4QUvKUDfErUF/RGU2U9mxjC6DMzmr73Dkcs5Rj8wCuROmdVymk
            aAYscGyImu6HvV2N/wf/I8JqylPzEyfnE9hT3Lapm7FPuvW+kshN09tcFe283zwKBgBg/NFAjO0CniYina6FM9KH4u
            k//5JZ9nXV9nkBRiykIzeWURcf1WfbpPIeQgIcx6/CKb/Peay41OIvN2gegyhLFaPbylN1xkBq9Yc5xkxKapReH+yI
            oiwO86Cc4QJVjLp3pQBy0+lXRwyRMg5sEcBQeQGBu5JpJh0hQTQ0Drj+i\\n-----ENDPRIVATEKEY-----
            \\n","client_email":"provider@mycompany.iam.gserviceaccount.com","client_id":"218140769437
            899532786","auth_uri":"https://accounts.google.com/o/oauth2/auth","token_uri":"https://oau
            th2.googleapis.com/token","auth_provider_x509_cert_url":"https://www.googleapis.com/oauth2
            /v1/certs","client_x509_cert_url":"https://www.googleapis.com/robot/v1/metadata/x509/provi
            der%40mycompany.iam.gserviceaccount.com","universe_domain":"googleapis.com"}'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CreatePublicCloudGoogleAccountResponse200 | ErrorResponse]
    """

    kwargs = _get_kwargs(
        site_uid=site_uid,
        body=body,
        select=select,
        x_request_id=x_request_id,
        x_client_version=x_client_version,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    site_uid: UUID,
    *,
    client: AuthenticatedClient,
    body: PublicCloudGoogleAccountInput,
    select: str | Unset = UNSET,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Any | CreatePublicCloudGoogleAccountResponse200 | ErrorResponse | None:
    r"""Create Google Cloud Account

     Creates a Google Cloud account in a Veeam Cloud Connect site with the specified UID.

    Args:
        site_uid (UUID):
        select (str | Unset):
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):
        body (PublicCloudGoogleAccountInput):  Example: {'name': 'Provider', 'description':
            'Provider Account', 'jsonConfiguration': '{"type":"service_account","project_id":"vspc","p
            rivate_key_id":"4a79cbf96aa94266407fa1a8fd39d6983989fd8","private_key":"-----BEGINPRIVATEK
            EY-----
            \\nMIIEowIBAAKCAQEAsUyvEXIzY2iHzUwtNCUTUDEGeEaWt667b8tbbehcmJmieP42T5bh0lIWvET9h03LGutYD4f
            0lH74EihHaBHt45B4ei9EiJGATPgLfdc4MOsiQcbf6HjrkuVzru4SDnesUEkDYczXNh/int7Uvuhafv0hKu3ZOfQPt
            PmJKBc+fQCBt6ZgSxQ1BqOR+p8MCkxxVr4zUphsQCU+kCWzilyPlFHSKtb/JggDGMnLiZiY1MnU1FkC4rTY2COlcNz
            q8PtEF6BuAO1L1788eh+h2oesG78kttuNmtTrXFlaCFzwOGmoKg2aAPIJVYNt5V3Vevm9kzcx5BAjeiKUZipGH8XQI
            DAQABAoIBABlUflJ8wVC7d2NiNbcUcOztBCKc2x2E7ixrnjVWlBwNHwQwNWwrfznAFpVxOdNhztmas+sMHmo0tZZKg
            OEiZp0zX7L9G8pzFyRn76Rb4iBDB5LkKcsZs3Y6J8vfIV9Fw614sO4BCOInrgXKihR4N62a1mk+r+EyuCe/2tOKdpf
            /BKjGLX9hhEglMFpscsCK6vMya+Eo1mpjTlqsTCQQEs031kRCcRFq4VBaLx/xgCAVLA0vTBUeGV7hx/VpGU3yy+flI
            +O3ny6lwaThe6ulkh3Y7S/dAyp6JYt/kmi6ZD0My8xTiOd4fw+zqDrt5UtROGAVMKHpCT7g9ElyGTLsTUCgYEA1sxt
            K2U/PVWsjq/ZK388zuSJ2QXMch+65xM+JZkPtbohzjlIFmGGyTN+kkMC3H1/xe+/y0GrB9OdzqLqiQQhOkXkzHuMAb
            qGoGKcywO1KqrKeD1C3Z4/ha4yLALF5M/ihCvCZ2k5mmfwCKX+5+kPhaqUOeJoO0C4DxLwdiI508CgYEA007jZqvy/
            3ct2LtREZgqsHggoyZOtYwtL8bvNuIMX/Z/fDlsdhjqFJCmYzgmVzpGpruac9dSBdPbOIs6cnkdnvdttwPgX9lrlW7
            DXFNCiXWdCTN7UlVDIKRCDjIlVKgsoI7EKewT6oGzjfhgejTRp4a8XvQfxqUWVOx4cIy9tpMCgYEAl2h5+4De1ukxP
            VMPDe4eeuf1kxjXSAq9wGx8dqPL/c+XENo2CFuSgEetOaOL7fVipXGjnFOsxF88/CY0lLXfPxDfIU6sywXUtuJhKVY
            BDj9Pb7G2iWH1X4W8sxoEd5W/0B56g5ivyArkJJc98oxRRcLMQ0MybFElGdLmw7lSp1kCgYB08nE6jqnTJ3ORQsJwW
            WYu+p0djoL7SVRs383e8yZkKfmOl/1mMw3CSfg8a4QUvKUDfErUF/RGU2U9mxjC6DMzmr73Dkcs5Rj8wCuROmdVymk
            aAYscGyImu6HvV2N/wf/I8JqylPzEyfnE9hT3Lapm7FPuvW+kshN09tcFe283zwKBgBg/NFAjO0CniYina6FM9KH4u
            k//5JZ9nXV9nkBRiykIzeWURcf1WfbpPIeQgIcx6/CKb/Peay41OIvN2gegyhLFaPbylN1xkBq9Yc5xkxKapReH+yI
            oiwO86Cc4QJVjLp3pQBy0+lXRwyRMg5sEcBQeQGBu5JpJh0hQTQ0Drj+i\\n-----ENDPRIVATEKEY-----
            \\n","client_email":"provider@mycompany.iam.gserviceaccount.com","client_id":"218140769437
            899532786","auth_uri":"https://accounts.google.com/o/oauth2/auth","token_uri":"https://oau
            th2.googleapis.com/token","auth_provider_x509_cert_url":"https://www.googleapis.com/oauth2
            /v1/certs","client_x509_cert_url":"https://www.googleapis.com/robot/v1/metadata/x509/provi
            der%40mycompany.iam.gserviceaccount.com","universe_domain":"googleapis.com"}'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CreatePublicCloudGoogleAccountResponse200 | ErrorResponse
    """

    return sync_detailed(
        site_uid=site_uid,
        client=client,
        body=body,
        select=select,
        x_request_id=x_request_id,
        x_client_version=x_client_version,
    ).parsed


async def asyncio_detailed(
    site_uid: UUID,
    *,
    client: AuthenticatedClient,
    body: PublicCloudGoogleAccountInput,
    select: str | Unset = UNSET,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Response[Any | CreatePublicCloudGoogleAccountResponse200 | ErrorResponse]:
    r"""Create Google Cloud Account

     Creates a Google Cloud account in a Veeam Cloud Connect site with the specified UID.

    Args:
        site_uid (UUID):
        select (str | Unset):
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):
        body (PublicCloudGoogleAccountInput):  Example: {'name': 'Provider', 'description':
            'Provider Account', 'jsonConfiguration': '{"type":"service_account","project_id":"vspc","p
            rivate_key_id":"4a79cbf96aa94266407fa1a8fd39d6983989fd8","private_key":"-----BEGINPRIVATEK
            EY-----
            \\nMIIEowIBAAKCAQEAsUyvEXIzY2iHzUwtNCUTUDEGeEaWt667b8tbbehcmJmieP42T5bh0lIWvET9h03LGutYD4f
            0lH74EihHaBHt45B4ei9EiJGATPgLfdc4MOsiQcbf6HjrkuVzru4SDnesUEkDYczXNh/int7Uvuhafv0hKu3ZOfQPt
            PmJKBc+fQCBt6ZgSxQ1BqOR+p8MCkxxVr4zUphsQCU+kCWzilyPlFHSKtb/JggDGMnLiZiY1MnU1FkC4rTY2COlcNz
            q8PtEF6BuAO1L1788eh+h2oesG78kttuNmtTrXFlaCFzwOGmoKg2aAPIJVYNt5V3Vevm9kzcx5BAjeiKUZipGH8XQI
            DAQABAoIBABlUflJ8wVC7d2NiNbcUcOztBCKc2x2E7ixrnjVWlBwNHwQwNWwrfznAFpVxOdNhztmas+sMHmo0tZZKg
            OEiZp0zX7L9G8pzFyRn76Rb4iBDB5LkKcsZs3Y6J8vfIV9Fw614sO4BCOInrgXKihR4N62a1mk+r+EyuCe/2tOKdpf
            /BKjGLX9hhEglMFpscsCK6vMya+Eo1mpjTlqsTCQQEs031kRCcRFq4VBaLx/xgCAVLA0vTBUeGV7hx/VpGU3yy+flI
            +O3ny6lwaThe6ulkh3Y7S/dAyp6JYt/kmi6ZD0My8xTiOd4fw+zqDrt5UtROGAVMKHpCT7g9ElyGTLsTUCgYEA1sxt
            K2U/PVWsjq/ZK388zuSJ2QXMch+65xM+JZkPtbohzjlIFmGGyTN+kkMC3H1/xe+/y0GrB9OdzqLqiQQhOkXkzHuMAb
            qGoGKcywO1KqrKeD1C3Z4/ha4yLALF5M/ihCvCZ2k5mmfwCKX+5+kPhaqUOeJoO0C4DxLwdiI508CgYEA007jZqvy/
            3ct2LtREZgqsHggoyZOtYwtL8bvNuIMX/Z/fDlsdhjqFJCmYzgmVzpGpruac9dSBdPbOIs6cnkdnvdttwPgX9lrlW7
            DXFNCiXWdCTN7UlVDIKRCDjIlVKgsoI7EKewT6oGzjfhgejTRp4a8XvQfxqUWVOx4cIy9tpMCgYEAl2h5+4De1ukxP
            VMPDe4eeuf1kxjXSAq9wGx8dqPL/c+XENo2CFuSgEetOaOL7fVipXGjnFOsxF88/CY0lLXfPxDfIU6sywXUtuJhKVY
            BDj9Pb7G2iWH1X4W8sxoEd5W/0B56g5ivyArkJJc98oxRRcLMQ0MybFElGdLmw7lSp1kCgYB08nE6jqnTJ3ORQsJwW
            WYu+p0djoL7SVRs383e8yZkKfmOl/1mMw3CSfg8a4QUvKUDfErUF/RGU2U9mxjC6DMzmr73Dkcs5Rj8wCuROmdVymk
            aAYscGyImu6HvV2N/wf/I8JqylPzEyfnE9hT3Lapm7FPuvW+kshN09tcFe283zwKBgBg/NFAjO0CniYina6FM9KH4u
            k//5JZ9nXV9nkBRiykIzeWURcf1WfbpPIeQgIcx6/CKb/Peay41OIvN2gegyhLFaPbylN1xkBq9Yc5xkxKapReH+yI
            oiwO86Cc4QJVjLp3pQBy0+lXRwyRMg5sEcBQeQGBu5JpJh0hQTQ0Drj+i\\n-----ENDPRIVATEKEY-----
            \\n","client_email":"provider@mycompany.iam.gserviceaccount.com","client_id":"218140769437
            899532786","auth_uri":"https://accounts.google.com/o/oauth2/auth","token_uri":"https://oau
            th2.googleapis.com/token","auth_provider_x509_cert_url":"https://www.googleapis.com/oauth2
            /v1/certs","client_x509_cert_url":"https://www.googleapis.com/robot/v1/metadata/x509/provi
            der%40mycompany.iam.gserviceaccount.com","universe_domain":"googleapis.com"}'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CreatePublicCloudGoogleAccountResponse200 | ErrorResponse]
    """

    kwargs = _get_kwargs(
        site_uid=site_uid,
        body=body,
        select=select,
        x_request_id=x_request_id,
        x_client_version=x_client_version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    site_uid: UUID,
    *,
    client: AuthenticatedClient,
    body: PublicCloudGoogleAccountInput,
    select: str | Unset = UNSET,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Any | CreatePublicCloudGoogleAccountResponse200 | ErrorResponse | None:
    r"""Create Google Cloud Account

     Creates a Google Cloud account in a Veeam Cloud Connect site with the specified UID.

    Args:
        site_uid (UUID):
        select (str | Unset):
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):
        body (PublicCloudGoogleAccountInput):  Example: {'name': 'Provider', 'description':
            'Provider Account', 'jsonConfiguration': '{"type":"service_account","project_id":"vspc","p
            rivate_key_id":"4a79cbf96aa94266407fa1a8fd39d6983989fd8","private_key":"-----BEGINPRIVATEK
            EY-----
            \\nMIIEowIBAAKCAQEAsUyvEXIzY2iHzUwtNCUTUDEGeEaWt667b8tbbehcmJmieP42T5bh0lIWvET9h03LGutYD4f
            0lH74EihHaBHt45B4ei9EiJGATPgLfdc4MOsiQcbf6HjrkuVzru4SDnesUEkDYczXNh/int7Uvuhafv0hKu3ZOfQPt
            PmJKBc+fQCBt6ZgSxQ1BqOR+p8MCkxxVr4zUphsQCU+kCWzilyPlFHSKtb/JggDGMnLiZiY1MnU1FkC4rTY2COlcNz
            q8PtEF6BuAO1L1788eh+h2oesG78kttuNmtTrXFlaCFzwOGmoKg2aAPIJVYNt5V3Vevm9kzcx5BAjeiKUZipGH8XQI
            DAQABAoIBABlUflJ8wVC7d2NiNbcUcOztBCKc2x2E7ixrnjVWlBwNHwQwNWwrfznAFpVxOdNhztmas+sMHmo0tZZKg
            OEiZp0zX7L9G8pzFyRn76Rb4iBDB5LkKcsZs3Y6J8vfIV9Fw614sO4BCOInrgXKihR4N62a1mk+r+EyuCe/2tOKdpf
            /BKjGLX9hhEglMFpscsCK6vMya+Eo1mpjTlqsTCQQEs031kRCcRFq4VBaLx/xgCAVLA0vTBUeGV7hx/VpGU3yy+flI
            +O3ny6lwaThe6ulkh3Y7S/dAyp6JYt/kmi6ZD0My8xTiOd4fw+zqDrt5UtROGAVMKHpCT7g9ElyGTLsTUCgYEA1sxt
            K2U/PVWsjq/ZK388zuSJ2QXMch+65xM+JZkPtbohzjlIFmGGyTN+kkMC3H1/xe+/y0GrB9OdzqLqiQQhOkXkzHuMAb
            qGoGKcywO1KqrKeD1C3Z4/ha4yLALF5M/ihCvCZ2k5mmfwCKX+5+kPhaqUOeJoO0C4DxLwdiI508CgYEA007jZqvy/
            3ct2LtREZgqsHggoyZOtYwtL8bvNuIMX/Z/fDlsdhjqFJCmYzgmVzpGpruac9dSBdPbOIs6cnkdnvdttwPgX9lrlW7
            DXFNCiXWdCTN7UlVDIKRCDjIlVKgsoI7EKewT6oGzjfhgejTRp4a8XvQfxqUWVOx4cIy9tpMCgYEAl2h5+4De1ukxP
            VMPDe4eeuf1kxjXSAq9wGx8dqPL/c+XENo2CFuSgEetOaOL7fVipXGjnFOsxF88/CY0lLXfPxDfIU6sywXUtuJhKVY
            BDj9Pb7G2iWH1X4W8sxoEd5W/0B56g5ivyArkJJc98oxRRcLMQ0MybFElGdLmw7lSp1kCgYB08nE6jqnTJ3ORQsJwW
            WYu+p0djoL7SVRs383e8yZkKfmOl/1mMw3CSfg8a4QUvKUDfErUF/RGU2U9mxjC6DMzmr73Dkcs5Rj8wCuROmdVymk
            aAYscGyImu6HvV2N/wf/I8JqylPzEyfnE9hT3Lapm7FPuvW+kshN09tcFe283zwKBgBg/NFAjO0CniYina6FM9KH4u
            k//5JZ9nXV9nkBRiykIzeWURcf1WfbpPIeQgIcx6/CKb/Peay41OIvN2gegyhLFaPbylN1xkBq9Yc5xkxKapReH+yI
            oiwO86Cc4QJVjLp3pQBy0+lXRwyRMg5sEcBQeQGBu5JpJh0hQTQ0Drj+i\\n-----ENDPRIVATEKEY-----
            \\n","client_email":"provider@mycompany.iam.gserviceaccount.com","client_id":"218140769437
            899532786","auth_uri":"https://accounts.google.com/o/oauth2/auth","token_uri":"https://oau
            th2.googleapis.com/token","auth_provider_x509_cert_url":"https://www.googleapis.com/oauth2
            /v1/certs","client_x509_cert_url":"https://www.googleapis.com/robot/v1/metadata/x509/provi
            der%40mycompany.iam.gserviceaccount.com","universe_domain":"googleapis.com"}'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CreatePublicCloudGoogleAccountResponse200 | ErrorResponse
    """

    return (
        await asyncio_detailed(
            site_uid=site_uid,
            client=client,
            body=body,
            select=select,
            x_request_id=x_request_id,
            x_client_version=x_client_version,
        )
    ).parsed
