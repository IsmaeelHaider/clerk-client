# swagger_client.OAuthApplicationsApi

All URIs are relative to *https://api.clerk.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_o_auth_application**](OAuthApplicationsApi.md#create_o_auth_application) | **POST** /oauth_applications | Create an OAuth application
[**delete_o_auth_application**](OAuthApplicationsApi.md#delete_o_auth_application) | **DELETE** /oauth_applications/{oauth_application_id} | Delete an OAuth application
[**get_o_auth_application**](OAuthApplicationsApi.md#get_o_auth_application) | **GET** /oauth_applications/{oauth_application_id} | Retrieve an OAuth application by ID
[**list_o_auth_applications**](OAuthApplicationsApi.md#list_o_auth_applications) | **GET** /oauth_applications | Get a list of OAuth applications for an instance
[**rotate_o_auth_application_secret**](OAuthApplicationsApi.md#rotate_o_auth_application_secret) | **POST** /oauth_applications/{oauth_application_id}/rotate_secret | Rotate the client secret of the given OAuth application
[**update_o_auth_application**](OAuthApplicationsApi.md#update_o_auth_application) | **PATCH** /oauth_applications/{oauth_application_id} | Update an OAuth application

# **create_o_auth_application**
> OAuthApplicationWithSecret create_o_auth_application(body=body)

Create an OAuth application

Creates a new OAuth application with the given name and callback URL for an instance. The callback URL must be a valid url. All URL schemes are allowed such as `http://`, `https://`, `myapp://`, etc...

### Example

```python
from __future__ import print_function
import time
import clerk_client
from clerk_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = clerk_client.OAuthApplicationsApi(clerk_client.ApiClient(configuration))
body = clerk_client.OauthApplicationsBody()  # OauthApplicationsBody |  (optional)

try:
    # Create an OAuth application
    api_response = api_instance.create_o_auth_application(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OAuthApplicationsApi->create_o_auth_application: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**OauthApplicationsBody**](OauthApplicationsBody.md)|  | [optional] 

### Return type

[**OAuthApplicationWithSecret**](OAuthApplicationWithSecret.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_o_auth_application**
> DeletedObject delete_o_auth_application(oauth_application_id)

Delete an OAuth application

Deletes the given OAuth application. This is not reversible.

### Example

```python
from __future__ import print_function
import time
import clerk_client
from clerk_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = clerk_client.OAuthApplicationsApi(clerk_client.ApiClient(configuration))
oauth_application_id = 'oauth_application_id_example'  # str | The ID of the OAuth application to delete

try:
    # Delete an OAuth application
    api_response = api_instance.delete_o_auth_application(oauth_application_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OAuthApplicationsApi->delete_o_auth_application: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **oauth_application_id** | **str**| The ID of the OAuth application to delete | 

### Return type

[**DeletedObject**](DeletedObject.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_o_auth_application**
> OAuthApplication get_o_auth_application(oauth_application_id)

Retrieve an OAuth application by ID

Fetches the OAuth application whose ID matches the provided `id` in the path.

### Example

```python
from __future__ import print_function
import time
import clerk_client
from clerk_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = clerk_client.OAuthApplicationsApi(clerk_client.ApiClient(configuration))
oauth_application_id = 'oauth_application_id_example'  # str | The ID of the OAuth application

try:
    # Retrieve an OAuth application by ID
    api_response = api_instance.get_o_auth_application(oauth_application_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OAuthApplicationsApi->get_o_auth_application: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **oauth_application_id** | **str**| The ID of the OAuth application | 

### Return type

[**OAuthApplication**](OAuthApplication.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_o_auth_applications**
> OAuthApplications list_o_auth_applications(limit=limit, offset=offset)

Get a list of OAuth applications for an instance

This request returns the list of OAuth applications for an instance. Results can be paginated using the optional `limit` and `offset` query parameters. The OAuth applications are ordered by descending creation date. Most recent OAuth applications will be returned first.

### Example

```python
from __future__ import print_function
import time
import clerk_client
from clerk_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = clerk_client.OAuthApplicationsApi(clerk_client.ApiClient(configuration))
limit = 10  # float | Applies a limit to the number of results returned. Can be used for paginating the results together with `offset`. Must be an integer greater than zero and less than 500. By default, if not supplied, a limit of 10 is used. (optional) (default to 10)
offset = 0  # float | Skip the first `offset` results when paginating. Needs to be an integer greater or equal to zero. To be used in conjunction with `limit`. (optional) (default to 0)

try:
    # Get a list of OAuth applications for an instance
    api_response = api_instance.list_o_auth_applications(limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OAuthApplicationsApi->list_o_auth_applications: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **float**| Applies a limit to the number of results returned. Can be used for paginating the results together with &#x60;offset&#x60;. Must be an integer greater than zero and less than 500. By default, if not supplied, a limit of 10 is used. | [optional] [default to 10]
 **offset** | **float**| Skip the first &#x60;offset&#x60; results when paginating. Needs to be an integer greater or equal to zero. To be used in conjunction with &#x60;limit&#x60;. | [optional] [default to 0]

### Return type

[**OAuthApplications**](OAuthApplications.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rotate_o_auth_application_secret**
> OAuthApplicationWithSecret rotate_o_auth_application_secret(oauth_application_id)

Rotate the client secret of the given OAuth application

Rotates the OAuth application's client secret. When the client secret is rotated, make sure to update it in authorized OAuth clients.

### Example

```python
from __future__ import print_function
import time
import clerk_client
from clerk_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = clerk_client.OAuthApplicationsApi(clerk_client.ApiClient(configuration))
oauth_application_id = 'oauth_application_id_example'  # str | The ID of the OAuth application for which to rotate the client secret

try:
    # Rotate the client secret of the given OAuth application
    api_response = api_instance.rotate_o_auth_application_secret(oauth_application_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OAuthApplicationsApi->rotate_o_auth_application_secret: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **oauth_application_id** | **str**| The ID of the OAuth application for which to rotate the client secret | 

### Return type

[**OAuthApplicationWithSecret**](OAuthApplicationWithSecret.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_o_auth_application**
> OAuthApplication update_o_auth_application(body, oauth_application_id)

Update an OAuth application

Updates an existing OAuth application

### Example

```python
from __future__ import print_function
import time
import clerk_client
from clerk_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = clerk_client.OAuthApplicationsApi(clerk_client.ApiClient(configuration))
body = clerk_client.OauthApplicationsOauthApplicationIdBody()  # OauthApplicationsOauthApplicationIdBody | 
oauth_application_id = 'oauth_application_id_example'  # str | The ID of the OAuth application to update

try:
    # Update an OAuth application
    api_response = api_instance.update_o_auth_application(body, oauth_application_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OAuthApplicationsApi->update_o_auth_application: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**OauthApplicationsOauthApplicationIdBody**](OauthApplicationsOauthApplicationIdBody.md)|  | 
 **oauth_application_id** | **str**| The ID of the OAuth application to update | 

### Return type

[**OAuthApplication**](OAuthApplication.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

