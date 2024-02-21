# clerk_client.SignInTokensApi

All URIs are relative to *https://api.clerk.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_sign_in_token**](SignInTokensApi.md#create_sign_in_token) | **POST** /sign_in_tokens | Create sign-in token
[**revoke_sign_in_token**](SignInTokensApi.md#revoke_sign_in_token) | **POST** /sign_in_tokens/{sign_in_token_id}/revoke | Revoke the given sign-in token

# **create_sign_in_token**
> SignInToken create_sign_in_token(body=body)

Create sign-in token

Creates a new sign-in token and associates it with the given user. By default, sign-in tokens expire in 30 days. You can optionally supply a different duration in seconds using the `expires_in_seconds` property.

### Example

```python
from __future__ import print_function
import time
import clerk_client
from clerk_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = clerk_client.SignInTokensApi(clerk_client.ApiClient(configuration))
body = clerk_client.SignInTokensBody()  # SignInTokensBody |  (optional)

try:
    # Create sign-in token
    api_response = api_instance.create_sign_in_token(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SignInTokensApi->create_sign_in_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SignInTokensBody**](SignInTokensBody.md)|  | [optional] 

### Return type

[**SignInToken**](SignInToken.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **revoke_sign_in_token**
> SignInToken revoke_sign_in_token(sign_in_token_id)

Revoke the given sign-in token

Revokes a pending sign-in token

### Example

```python
from __future__ import print_function
import time
import clerk_client
from clerk_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = clerk_client.SignInTokensApi(clerk_client.ApiClient(configuration))
sign_in_token_id = 'sign_in_token_id_example'  # str | The ID of the sign-in token to be revoked

try:
    # Revoke the given sign-in token
    api_response = api_instance.revoke_sign_in_token(sign_in_token_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SignInTokensApi->revoke_sign_in_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sign_in_token_id** | **str**| The ID of the sign-in token to be revoked | 

### Return type

[**SignInToken**](SignInToken.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

