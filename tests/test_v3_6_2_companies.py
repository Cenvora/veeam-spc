from veeam_spc.v3_6_2.models.get_companies_response_200 import GetCompaniesResponse200


def test_get_companies_allows_null_nested_company_services():
    payload = {
        "data": [
            {
                "ownerCredentials": {
                    "userName": "company-owner",
                },
                "companyServices": {
                    "hostedServices": None,
                    "remoteServices": None,
                },
            }
        ]
    }

    response = GetCompaniesResponse200.from_dict(payload)

    assert response.data[0].company_services is not None
    assert response.data[0].company_services.hosted_services is None
    assert response.data[0].company_services.remote_services is None
