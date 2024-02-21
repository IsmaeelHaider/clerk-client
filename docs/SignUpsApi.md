# swagger_client.SignUpsApi

All URIs are relative to *https://api.clerk.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**update_sign_up**](SignUpsApi.md#update_sign_up) | **PATCH** /sign_ups/{id} | Update a sign-up

# **update_sign_up**
> SignUp update_sign_up(id, body=body)

Update a sign-up

Update the sign-up with the given ID

### Example

```python
from __future__ import print_function
import time
import clerk_client
from clerk_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = clerk_client.SignUpsApi(clerk_client.ApiClient(configuration))
id = 'id_example'  # str | The ID of the sign-up to update
body = clerk_client.SignUpsIdBody()  # SignUpsIdBody |  (optional)

try:
    # Update a sign-up
    api_response = api_instance.update_sign_up(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SignUpsApi->update_sign_up: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the sign-up to update | 
 **body** | [**SignUpsIdBody**](SignUpsIdBody.md)|  | [optional] 

### Return type

[**SignUp**](SignUp.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

