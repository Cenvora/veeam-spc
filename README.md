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
This project is an independent, open source Python client for the Veeam Service Provider Console <a href="https://helpcenter.veeam.com/docs/vac/rest/reference/vspc-rest.html">REST API</a>. It is not affiliated with, endorsed by, or sponsored by Veeam Software.
<!-- Summary -->

## Supported Versions

<table>
  <thead>
    <tr>
      <th>VSPC Version</th>
      <th>API Version</th>
      <th>Supported</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>9 / 3.6</td>
      <td>3.6</td>
      <td style="text-align:center;">&#10060;</td>
    </tr>
    <tr>
      <td>8.1 / 3.5.1</td>
      <td>3.5.1</td>
      <td style="text-align:center;">&#9989;</td>
    </tr>
    <tr>
      <td>&lt; 8.1 / 3.5.1</td>
      <td>&lt; 3.5.1</td>
      <td style="text-align:center;">&#10060;</td>
    </tr>
  </tbody>
</table>

## How to support new API versions
1. Download the OpenAPI yaml into openapi_schemas
2. Fix the OpenAPI yaml to conform to proper standards: `python fix_openapi_yaml.py .\openapi_schemas\vspc_rest_{vspc_version}.yaml .\openapi_schemas\vspc_rest_{vspc_version}_fixed.yaml`
3. Run `openapi-python-client generate --path ".\openapi_schemas\vspc_rest_{vspc_version}_fixed.yaml" --output-path ".\veeam_spc" --overwrite`
4. Fix any warnings/errors (application/binary+base64 can be ignored)
5. Rename the folder to match the API version (i.e., `v3.5.1`)
6. Update pyproject.toml to support the new packages
7. Write pytest tests
8. If an older API has been deprecated, delete its folder and yaml, then remove it from pyproject.toml

## Install
### From PyPi
`pip install veeam-spc`


### From Source
Clone the repository and install dependencies:
```sh
git clone https://github.com/Cenvora/veeam-spc.git
cd veeam-spc
pip install -e .
```

## Usage Tips
- For endpoints requiring authentication, pass the appropriate credentials when creating the `Client`.
- To support multiple API versions, import the client and models from the desired versioned subpackage (e.g., `veeam_spc.v3_5_1`).
- For file downloads (PDF, CSV, etc.), access the raw response content: `response.content`.
- Refer to the generated `api` and `models` modules for available endpoints and request/response schemas.


## Usage
First, create a client:

```python
from veeam_spc.v3_5_1 import Client
client = Client(base_url="https://server:1280/api/v3")
```

If the endpoints you're going to hit require authentication, use `AuthenticatedClient` (if available):

```python
from veeam_spc.v3_5_1 import AuthenticatedClient
client = AuthenticatedClient(base_url="https://server:1280/api/v3", token="SuperSecretToken")
```

Now call your endpoint and use your models:

```python
from veeam_spc.v3_5_1.models import CreateUserRequest
from veeam_spc.v3_5_1.api.users import create_user
from veeam_spc.v3_5_1.types import Response

from veeam_spc.v3_5_1.api.users import get_current_user

# Authenticate using a REST API token
client = AuthenticatedClient(base_url="https://server:1280/api/v3", token="SuperSecretToken")

with client:
    user = get_current_user.sync(client=client)
    response: Response = get_current_user.sync_detailed(client=client)
```

Or do the same thing with an async version:

```python
from veeam_spc.v3_5_1.models import CreateUserRequest
from veeam_spc.v3_5_1.api.users import create_user
from veeam_spc.v3_5_1.types import Response

client = AuthenticatedClient(base_url="https://server:1280/api/v3", token="SuperSecretToken")

async with client:
    user = await create_user.asyncio(client=client, json_body=body)
    response: Response = await create_user.asyncio_detailed(client=client, json_body=body)
```

### SSL Verification
By default, HTTPS APIs will verify SSL certificates. You can pass a custom certificate bundle or disable verification (not recommended):

```python
client = AuthenticatedClient(
    base_url="https://internal_api.example.com/api/v3",
    token="SuperSecretToken",
    verify_ssl="/path/to/certificate_bundle.pem",
)

# Disable SSL verification (security risk)
client = AuthenticatedClient(
    base_url="https://internal_api.example.com/api/v3",
    token="SuperSecretToken",
    verify_ssl=False
)
```

### Advanced Customizations
You can customize the underlying `httpx.Client` or `httpx.AsyncClient`:

```python
from veeam_spc.v3_5_1 import Client
def log_request(request):
    print(f"Request event hook: {request.method} {request.url} - Waiting for response")
def log_response(response):
    request = response.request
    print(f"Response event hook: {request.method} {request.url} - Status {response.status_code}")
client = Client(
    base_url="https://server:1280/api/v3",
    httpx_args={"event_hooks": {"request": [log_request], "response": [log_response]}},
)
# Or get the underlying httpx client to modify directly with client.get_httpx_client() or client.get_async_httpx_client()
```

## Building / Publishing
This project uses [Poetry](https://python-poetry.org/) for dependencies and packaging:
1. Update metadata in pyproject.toml (authors, version)
2. Configure private repositories if needed
    - `poetry config repositories.<your-repository-name> <url>`
    - `poetry config http-basic.<your-repository-name> <username> <password>`
3. Publish: `poetry publish --build -r <your-repository-name>` or `poetry publish --build` for PyPI

To install into another project without publishing:
1. If using Poetry: `poetry add <path-to-this-client>`
2. If not using Poetry:
    - Build a wheel: `poetry build -f wheel`
    - Install: `pip install <path-to-wheel>`

## Contributing
Contributions are welcome! To contribute:
- Fork the repository
- Create a feature branch
- Make your changes and add tests
- Submit a pull request with a clear description

Please follow PEP8 style and include docstrings for new functions/classes.

## 🤝 Core Contributors
This project is made possible thanks to the efforts of our core contributors:

- [Jonah May](https://github.com/JonahMMay)  
- [Maurice Kevenaar](https://github.com/mkevenaar)  
- [CyberFortress](https://cyberfortress.com)  
- [Integra Cloud Solutions B.V.](https://integra-cs.nl/)  

We’re grateful for their continued support and contributions.
