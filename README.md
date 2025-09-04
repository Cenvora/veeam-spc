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
1. Download the OpenAI yaml
2. Run `openapi-python-client generate --path ".\openapi_schemas\vspc_rest_{version}_fixed.yaml" --output-path ".\veeam_spc\v{version}" --overwrite`
3. Fix any warnings/errors
4. Write tests
5. If an older API has been deprecated, delete its folder and yaml

## Install
TODO: Write this

## Contributing
TODO: Write this