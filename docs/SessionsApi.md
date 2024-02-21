# swagger_client.SessionsApi

All URIs are relative to *https://api.clerk.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_session_token_from_template**](SessionsApi.md#create_session_token_from_template) | **POST** /sessions/{session_id}/tokens/{template_name} | Create a session token from a jwt template
[**get_session**](SessionsApi.md#get_session) | **GET** /sessions/{session_id} | Retrieve a session
[**get_session_list**](SessionsApi.md#get_session_list) | **GET** /sessions | List all sessions
[**revoke_session**](SessionsApi.md#revoke_session) | **POST** /sessions/{session_id}/revoke | Revoke a session
[**verify_session**](SessionsApi.md#verify_session) | **POST** /sessions/{session_id}/verify | Verify a session

# **create_session_token_from_template**
> InlineResponse200 create_session_token_from_template(session_id, template_name)

Create a session token from a jwt template

Creates a JSON Web Token(JWT) based on a session and a JWT Template name defined for your instance

### Example

```python
from __future__ import print_function
import time
import clerk_client
from clerk_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = clerk_client.SessionsApi(clerk_client.ApiClient(configuration))
session_id = 'session_id_example'  # str | The ID of the session
template_name = 'template_name_example'  # str | The name of the JWT Template defined in your instance (e.g. `custom_hasura`).

try:
    # Create a session token from a jwt template
    api_response = api_instance.create_session_token_from_template(session_id, template_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SessionsApi->create_session_token_from_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**| The ID of the session | 
 **template_name** | **str**| The name of the JWT Template defined in your instance (e.g. &#x60;custom_hasura&#x60;). | 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_session**
> Session get_session(session_id)

Retrieve a session

Retrieve the details of a session

### Example

```python
from __future__ import print_function
import time
import clerk_client
from clerk_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = clerk_client.SessionsApi(clerk_client.ApiClient(configuration))
session_id = 'session_id_example'  # str | The ID of the session

try:
    # Retrieve a session
    api_response = api_instance.get_session(session_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SessionsApi->get_session: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**| The ID of the session | 

### Return type

[**Session**](Session.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_session_list**
> list[Session] get_session_list(client_id=client_id, user_id=user_id, status=status, limit=limit, offset=offset)

List all sessions

Returns a list of all sessions. The sessions are returned sorted by creation date, with the newest sessions appearing first. **Deprecation Notice (2024-01-01):** All parameters were initially considered optional, however moving forward at least one of `client_id` or `user_id` parameters should be provided.

### Example

```python
from __future__ import print_function
import time
import clerk_client
from clerk_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = clerk_client.SessionsApi(clerk_client.ApiClient(configuration))
client_id = 'client_id_example'  # str | List sessions for the given client (optional)
user_id = 'user_id_example'  # str | List sessions for the given user (optional)
status = 'status_example'  # str | Filter sessions by the provided status (optional)
limit = 10  # float | Applies a limit to the number of results returned. Can be used for paginating the results together with `offset`. Must be an integer greater than zero and less than 500. By default, if not supplied, a limit of 10 is used. (optional) (default to 10)
offset = 0  # float | Skip the first `offset` results when paginating. Needs to be an integer greater or equal to zero. To be used in conjunction with `limit`. (optional) (default to 0)

try:
    # List all sessions
    api_response = api_instance.get_session_list(client_id=client_id, user_id=user_id, status=status, limit=limit,
                                                 offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SessionsApi->get_session_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**| List sessions for the given client | [optional] 
 **user_id** | **str**| List sessions for the given user | [optional] 
 **status** | **str**| Filter sessions by the provided status | [optional] 
 **limit** | **float**| Applies a limit to the number of results returned. Can be used for paginating the results together with &#x60;offset&#x60;. Must be an integer greater than zero and less than 500. By default, if not supplied, a limit of 10 is used. | [optional] [default to 10]
 **offset** | **float**| Skip the first &#x60;offset&#x60; results when paginating. Needs to be an integer greater or equal to zero. To be used in conjunction with &#x60;limit&#x60;. | [optional] [default to 0]

### Return type

[**list[Session]**](Session.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **revoke_session**
> Session revoke_session(session_id)

Revoke a session

Sets the status of a session as \"revoked\", which is an unauthenticated state. In multi-session mode, a revoked session will still be returned along with its client object, however the user will need to sign in again.

### Example

```python
from __future__ import print_function
import time
import clerk_client
from clerk_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = clerk_client.SessionsApi(clerk_client.ApiClient(configuration))
session_id = 'session_id_example'  # str | The ID of the session

try:
    # Revoke a session
    api_response = api_instance.revoke_session(session_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SessionsApi->revoke_session: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**| The ID of the session | 

### Return type

[**Session**](Session.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **verify_session**
> Session verify_session(session_id, body=body)

Verify a session

Returns the session if it is authenticated, otherwise returns an error. WARNING: This endpoint is deprecated and will be removed in future versions. We strongly recommend switching to networkless verification using short-lived session tokens,          which is implemented transparently in all recent SDK versions (e.g. [NodeJS SDK](https://clerk.com/docs/backend-requests/handling/nodejs#clerk-express-require-auth)).          For more details on how networkless verification works, refer to our [Session Tokens documentation](https://clerk.com/docs/backend-requests/resources/session-tokens).

### Example

```python
from __future__ import print_function
import time
import clerk_client
from clerk_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = clerk_client.SessionsApi(clerk_client.ApiClient(configuration))
session_id = 'session_id_example'  # str | The ID of the session
body = clerk_client.SessionIdVerifyBody()  # SessionIdVerifyBody | Parameters. (optional)

try:
    # Verify a session
    api_response = api_instance.verify_session(session_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SessionsApi->verify_session: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**| The ID of the session | 
 **body** | [**SessionIdVerifyBody**](SessionIdVerifyBody.md)| Parameters. | [optional] 

### Return type

[**Session**](Session.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

