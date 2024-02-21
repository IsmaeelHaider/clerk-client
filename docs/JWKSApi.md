# clerk_client.JWKSApi

All URIs are relative to *https://api.clerk.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_jwks**](JWKSApi.md#get_jwks) | **GET** /jwks | Retrieve the JSON Web Key Set of the instance

# **get_jwks**
> get_jwks()

Retrieve the JSON Web Key Set of the instance

Retrieve the JSON Web Key Set of the instance

### Example

```python
from __future__ import print_function
import time
import clerk_client
from clerk_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = clerk_client.JWKSApi(clerk_client.ApiClient(configuration))

try:
    # Retrieve the JSON Web Key Set of the instance
    api_instance.get_jwks()
except ApiException as e:
    print("Exception when calling JWKSApi->get_jwks: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

