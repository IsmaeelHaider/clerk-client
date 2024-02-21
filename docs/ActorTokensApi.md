# swagger_client.ActorTokensApi

All URIs are relative to *https://api.clerk.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_actor_token**](ActorTokensApi.md#create_actor_token) | **POST** /actor_tokens | Create actor token
[**revoke_actor_token**](ActorTokensApi.md#revoke_actor_token) | **POST** /actor_tokens/{actor_token_id}/revoke | Revoke actor token

# **create_actor_token**
> ActorToken create_actor_token(body=body)

Create actor token

Create an actor token that can be used to impersonate the given user. The `actor` parameter needs to include at least a \"sub\" key whose value is the ID of the actor (impersonating) user.

### Example

```python
from __future__ import print_function
import time
import clerk_client
from clerk_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = clerk_client.ActorTokensApi(clerk_client.ApiClient(configuration))
body = clerk_client.ActorTokensBody()  # ActorTokensBody |  (optional)

try:
    # Create actor token
    api_response = api_instance.create_actor_token(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActorTokensApi->create_actor_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ActorTokensBody**](ActorTokensBody.md)|  | [optional] 

### Return type

[**ActorToken**](ActorToken.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **revoke_actor_token**
> ActorToken revoke_actor_token(actor_token_id)

Revoke actor token

Revokes a pending actor token.

### Example

```python
from __future__ import print_function
import time
import clerk_client
from clerk_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = clerk_client.ActorTokensApi(clerk_client.ApiClient(configuration))
actor_token_id = 'actor_token_id_example'  # str | The ID of the actor token to be revoked.

try:
    # Revoke actor token
    api_response = api_instance.revoke_actor_token(actor_token_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActorTokensApi->revoke_actor_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **actor_token_id** | **str**| The ID of the actor token to be revoked. | 

### Return type

[**ActorToken**](ActorToken.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

