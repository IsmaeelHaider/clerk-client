# clerk_client.ClientsApi

All URIs are relative to *https://api.clerk.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_client**](ClientsApi.md#get_client) | **GET** /clients/{client_id} | Get a client
[**get_client_list**](ClientsApi.md#get_client_list) | **GET** /clients | List all clients
[**verify_client**](ClientsApi.md#verify_client) | **POST** /clients/verify | Verify a client

# **get_client**
> Client get_client(client_id)

Get a client

Returns the details of a client.

### Example

```python
from __future__ import print_function
import time
import clerk_client
from clerk_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = clerk_client.ClientsApi(clerk_client.ApiClient(configuration))
client_id = 'client_id_example'  # str | Client ID.

try:
    # Get a client
    api_response = api_instance.get_client(client_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClientsApi->get_client: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**| Client ID. | 

### Return type

[**Client**](Client.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_client_list**
> list[Client] get_client_list(limit=limit, offset=offset)

List all clients

Returns a list of all clients. The clients are returned sorted by creation date, with the newest clients appearing first. Warning: the endpoint is being deprecated and will be removed in future versions.

### Example

```python
from __future__ import print_function
import time
import clerk_client
from clerk_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = clerk_client.ClientsApi(clerk_client.ApiClient(configuration))
limit = 10  # float | Applies a limit to the number of results returned. Can be used for paginating the results together with `offset`. Must be an integer greater than zero and less than 500. By default, if not supplied, a limit of 10 is used. (optional) (default to 10)
offset = 0  # float | Skip the first `offset` results when paginating. Needs to be an integer greater or equal to zero. To be used in conjunction with `limit`. (optional) (default to 0)

try:
    # List all clients
    api_response = api_instance.get_client_list(limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClientsApi->get_client_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **float**| Applies a limit to the number of results returned. Can be used for paginating the results together with &#x60;offset&#x60;. Must be an integer greater than zero and less than 500. By default, if not supplied, a limit of 10 is used. | [optional] [default to 10]
 **offset** | **float**| Skip the first &#x60;offset&#x60; results when paginating. Needs to be an integer greater or equal to zero. To be used in conjunction with &#x60;limit&#x60;. | [optional] [default to 0]

### Return type

[**list[Client]**](Client.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **verify_client**
> Client verify_client(body=body)

Verify a client

Verifies the client in the provided token

### Example

```python
from __future__ import print_function
import time
import clerk_client
from clerk_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = clerk_client.ClientsApi(clerk_client.ApiClient(configuration))
body = clerk_client.ClientsVerifyBody()  # ClientsVerifyBody | Parameters. (optional)

try:
    # Verify a client
    api_response = api_instance.verify_client(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClientsApi->verify_client: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ClientsVerifyBody**](ClientsVerifyBody.md)| Parameters. | [optional] 

### Return type

[**Client**](Client.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

