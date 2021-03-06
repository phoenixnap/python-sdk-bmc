# pnap-rancher-solution-api
Simplify enterprise-grade Kubernetes cluster operations and management with Rancher on Bare Metal Cloud.
Deploy Kubernetes clusters using a few API calls.<br>
<br>
<span class='pnap-api-knowledge-base-link'>
Knowledge base articles to help you can be found
<a href='https://phoenixnap.com/kb/rancher-bmc-integration-kubernetes' target='_blank'>here</a>
</span><br>
<br>
<b>All URLs are relative to (https://api.phoenixnap.com/solutions/rancher/v1beta)</b>


This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 0.1
For more information, please visit [https://phoenixnap.com/](https://phoenixnap.com/)

## Requirements.

Python >=3.6

## Installation & Usage
### pip install

You can install this package directly from the [Python Package Index](https://pypi.org/) using:

```sh
pip install pnap_rancher_solution_api
```

Then import the package:
```python
import pnap_rancher_solution_api
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import pnap_rancher_solution_api
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import time
import pnap_rancher_solution_api
from pprint import pprint
from pnap_rancher_solution_api.api import clusters_api
from pnap_rancher_solution_api.model.cluster import Cluster
from pnap_rancher_solution_api.model.delete_result import DeleteResult
from pnap_rancher_solution_api.model.error import Error
# Defining the host is optional and defaults to https://api.phoenixnap.com/solutions/rancher/v1beta
# See configuration.py for a list of all supported configuration parameters.
configuration = pnap_rancher_solution_api.Configuration(
    host = "https://api.phoenixnap.com/solutions/rancher/v1beta"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: OAuth2
configuration = pnap_rancher_solution_api.Configuration(
    host = "https://api.phoenixnap.com/solutions/rancher/v1beta"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'


# Enter a context with an instance of the API client
with pnap_rancher_solution_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = clusters_api.ClustersApi(api_client)
    
    try:
        # Cluster list.
        api_response = api_instance.clusters_get()
        pprint(api_response)
    except pnap_rancher_solution_api.ApiException as e:
        print("Exception when calling ClustersApi->clusters_get: %s\n" % e)
```
To generate a token using the [python-keycloak](https://pypi.org/project/python-keycloak/) library:

```python
from keycloak import KeycloakOpenID

clientId = "YOUR_CLIENT_ID"
clientSecret = "YOUR_CLIENT_SECRET"
serverUrl = "https://auth.phoenixnap.com/auth/"
realmName = "BMC"
grantType = "client_credentials"

keycloakOpenId =  KeycloakOpenID(server_url=serverUrl,
                        realm_name=realmName,
                        client_id=clientId,
                        client_secret_key=clientSecret)

ACCESS_TOKEN = keycloakOpenId.token(grant_type=grantType)['access_token']
```

## Documentation for API Endpoints

All URIs are relative to *https://api.phoenixnap.com/solutions/rancher/v1beta*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*ClustersApi* | [**clusters_get**](docs/ClustersApi.md#clusters_get) | **GET** /clusters | Cluster list.
*ClustersApi* | [**clusters_id_delete**](docs/ClustersApi.md#clusters_id_delete) | **DELETE** /clusters/{id} | Delete a cluster.
*ClustersApi* | [**clusters_id_get**](docs/ClustersApi.md#clusters_id_get) | **GET** /clusters/{id} | Retrieve a Cluster
*ClustersApi* | [**clusters_post**](docs/ClustersApi.md#clusters_post) | **POST** /clusters | Create a Rancher Server Deployment.


## Documentation For Models

 - [Cluster](docs/Cluster.md)
 - [DeleteResult](docs/DeleteResult.md)
 - [Error](docs/Error.md)
 - [Node](docs/Node.md)
 - [NodePool](docs/NodePool.md)
 - [RancherClusterCertificates](docs/RancherClusterCertificates.md)
 - [RancherClusterConfig](docs/RancherClusterConfig.md)
 - [RancherServerMetadata](docs/RancherServerMetadata.md)
 - [SshConfig](docs/SshConfig.md)
 - [WorkloadClusterConfig](docs/WorkloadClusterConfig.md)


## Documentation For Authorization


## OAuth2

- **Type**: OAuth
- **Flow**: application
- **Authorization URL**: 
- **Scopes**: 
 - **bmc**: Grants full access to bmc-api.
 - **bmc.read**: Grants read only access to bmc-api.


## Author

support@phoenixnap.com


## Notes for Large OpenAPI documents
If the OpenAPI document is large, imports in pnap_rancher_solution_api.apis and pnap_rancher_solution_api.models may fail with a
RecursionError indicating the maximum recursion limit has been exceeded. In that case, there are a couple of solutions:

Solution 1:
Use specific imports for apis and models like:
- `from pnap_rancher_solution_api.api.default_api import DefaultApi`
- `from pnap_rancher_solution_api.model.pet import Pet`

Solution 2:
Before importing the package, adjust the maximum recursion limit as shown below:
```
import sys
sys.setrecursionlimit(1500)
import pnap_rancher_solution_api
from pnap_rancher_solution_api.apis import *
from pnap_rancher_solution_api.models import *
```