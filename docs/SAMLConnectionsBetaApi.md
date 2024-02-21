# clerk_client.SAMLConnectionsBetaApi

All URIs are relative to *https://api.clerk.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_saml_connection**](SAMLConnectionsBetaApi.md#create_saml_connection) | **POST** /saml_connections | Create a SAML Connection
[**delete_saml_connection**](SAMLConnectionsBetaApi.md#delete_saml_connection) | **DELETE** /saml_connections/{saml_connection_id} | Delete a SAML Connection
[**get_saml_connection**](SAMLConnectionsBetaApi.md#get_saml_connection) | **GET** /saml_connections/{saml_connection_id} | Retrieve a SAML Connection by ID
[**list_saml_connections**](SAMLConnectionsBetaApi.md#list_saml_connections) | **GET** /saml_connections | Get a list of SAML Connections for an instance
[**update_saml_connection**](SAMLConnectionsBetaApi.md#update_saml_connection) | **PATCH** /saml_connections/{saml_connection_id} | Update a SAML Connection

# **create_saml_connection**
> SAMLConnection create_saml_connection(body=body)

Create a SAML Connection

Refer to <a href=\"https://clerk.com/docs/authentication/saml-at-clerk#saml-at-clerk-beta\">Clerk SAML documentation</a> for more information.

### Example

```python
from __future__ import print_function
import time
import clerk_client
from clerk_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = clerk_client.SAMLConnectionsBetaApi(clerk_client.ApiClient(configuration))
body = clerk_client.SamlConnectionsBody()  # SamlConnectionsBody |  (optional)

try:
    # Create a SAML Connection
    api_response = api_instance.create_saml_connection(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SAMLConnectionsBetaApi->create_saml_connection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SamlConnectionsBody**](SamlConnectionsBody.md)|  | [optional] 

### Return type

[**SAMLConnection**](SAMLConnection.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_saml_connection**
> DeletedObject delete_saml_connection(saml_connection_id)

Delete a SAML Connection

Deletes the SAML Connection whose ID matches the provided `id` in the path. <br/> Refer to <a href=\"https://clerk.com/docs/authentication/saml-at-clerk#saml-at-clerk-beta\">Clerk SAML documentation</a> for more information.

### Example

```python
from __future__ import print_function
import time
import clerk_client
from clerk_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = clerk_client.SAMLConnectionsBetaApi(clerk_client.ApiClient(configuration))
saml_connection_id = 'saml_connection_id_example'  # str | The ID of the SAML Connection to delete

try:
    # Delete a SAML Connection
    api_response = api_instance.delete_saml_connection(saml_connection_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SAMLConnectionsBetaApi->delete_saml_connection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **saml_connection_id** | **str**| The ID of the SAML Connection to delete | 

### Return type

[**DeletedObject**](DeletedObject.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_saml_connection**
> SAMLConnection get_saml_connection(saml_connection_id)

Retrieve a SAML Connection by ID

Fetches the SAML Connection whose ID matches the provided `saml_connection_id` in the path. <br/> Refer to <a href=\"https://clerk.com/docs/authentication/saml-at-clerk#saml-at-clerk-beta\">Clerk SAML documentation</a> for more information.

### Example

```python
from __future__ import print_function
import time
import clerk_client
from clerk_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = clerk_client.SAMLConnectionsBetaApi(clerk_client.ApiClient(configuration))
saml_connection_id = 'saml_connection_id_example'  # str | The ID of the SAML Connection

try:
    # Retrieve a SAML Connection by ID
    api_response = api_instance.get_saml_connection(saml_connection_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SAMLConnectionsBetaApi->get_saml_connection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **saml_connection_id** | **str**| The ID of the SAML Connection | 

### Return type

[**SAMLConnection**](SAMLConnection.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_saml_connections**
> SAMLConnections list_saml_connections(limit=limit, offset=offset)

Get a list of SAML Connections for an instance

Returns the list of SAML Connections for an instance. Results can be paginated using the optional `limit` and `offset` query parameters. The SAML Connections are ordered by descending creation date and the most recent will be returned first. <br/> Refer to <a href=\"https://clerk.com/docs/authentication/saml-at-clerk#saml-at-clerk-beta\">Clerk SAML documentation</a> for more information.

### Example

```python
from __future__ import print_function
import time
import clerk_client
from clerk_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = clerk_client.SAMLConnectionsBetaApi(clerk_client.ApiClient(configuration))
limit = 10  # float | Applies a limit to the number of results returned. Can be used for paginating the results together with `offset`. Must be an integer greater than zero and less than 500. By default, if not supplied, a limit of 10 is used. (optional) (default to 10)
offset = 0  # float | Skip the first `offset` results when paginating. Needs to be an integer greater or equal to zero. To be used in conjunction with `limit`. (optional) (default to 0)

try:
    # Get a list of SAML Connections for an instance
    api_response = api_instance.list_saml_connections(limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SAMLConnectionsBetaApi->list_saml_connections: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **float**| Applies a limit to the number of results returned. Can be used for paginating the results together with &#x60;offset&#x60;. Must be an integer greater than zero and less than 500. By default, if not supplied, a limit of 10 is used. | [optional] [default to 10]
 **offset** | **float**| Skip the first &#x60;offset&#x60; results when paginating. Needs to be an integer greater or equal to zero. To be used in conjunction with &#x60;limit&#x60;. | [optional] [default to 0]

### Return type

[**SAMLConnections**](SAMLConnections.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_saml_connection**
> SAMLConnection update_saml_connection(body, saml_connection_id)

Update a SAML Connection

Updates the SAML Connection whose ID matches the provided `id` in the path. <br/> Refer to <a href=\"https://clerk.com/docs/authentication/saml-at-clerk#saml-at-clerk-beta\">Clerk SAML documentation</a> for more information.

### Example

```python
from __future__ import print_function
import time
import clerk_client
from clerk_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = clerk_client.SAMLConnectionsBetaApi(clerk_client.ApiClient(configuration))
body = clerk_client.SamlConnectionsSamlConnectionIdBody()  # SamlConnectionsSamlConnectionIdBody | 
saml_connection_id = 'saml_connection_id_example'  # str | The ID of the SAML Connection to update

try:
    # Update a SAML Connection
    api_response = api_instance.update_saml_connection(body, saml_connection_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SAMLConnectionsBetaApi->update_saml_connection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SamlConnectionsSamlConnectionIdBody**](SamlConnectionsSamlConnectionIdBody.md)|  | 
 **saml_connection_id** | **str**| The ID of the SAML Connection to update | 

### Return type

[**SAMLConnection**](SAMLConnection.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

