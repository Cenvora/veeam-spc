<h1 align="center">
<br>
<img src="./media/Veeam_logo_2024_RGB_main_20.png" alt="Veeam Logo" height="100"></a>
<br>
<br>
Veeam Service Provider Console Python API Wrapper
</h1>

<h4 align="center">
Python package for interacting with the Veeam Service Provider Console REST API
</h4>

<!-- Summary -->
This module allows for interaction with Veeam Service Provider Console via their <a href="https://helpcenter.veeam.com/docs/vac/rest/reference/vspc-rest.html">REST API</a>
<!-- Summary -->

## How to support new API versions
1. Download the OpenAPI yaml into openapi_schemas
2. Fix the OpenAPI yaml to conform to proper standards: `python fix_openapi_yaml.py .\openapi_schemas\vspc_rest_{vspc_version}.yaml .\openapi_schemas\vspc_rest_{vspc_version}_fixed.yaml`
3. Run `openapi-python-client generate --path ".\openapi_schemas\vspc_rest_{vspc_version}_fixed.yaml" --output-path ".\veeam_spc\v{api_version}" --overwrite`
4. Fix any warnings/errors (application/binary+base64 can be ignored)
5. Write tests
6. If an older API has been deprecated, delete its folder and yaml

## Install
TODO: Write this

## Usage Example
```
# Import in the client, api, and necessary models
from veeam_spc.v3_5_1 import Client, api
from veeam_spc.v3_5_1.models import CreateUserRequest

client = Client(base_url="https://server:1280/api/v3")

# Create the request body using the model
body = CreateUserRequest(
    username="newuser",
    password="securepassword",
    email="user@example.com"
    # ...other required fields
)

# Pass the body to the endpoint function
response = api.create_user.sync(client=client, json_body=body)

print(response.parsed)
```

## Contributing
TODO: Write this