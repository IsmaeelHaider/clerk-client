# swagger_client.RedirectURLsApi

All URIs are relative to *https://api.clerk.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_redirect_url**](RedirectURLsApi.md#create_redirect_url) | **POST** /redirect_urls | Create a redirect URL
[**delete_redirect_url**](RedirectURLsApi.md#delete_redirect_url) | **DELETE** /redirect_urls/{id} | Delete a redirect URL
[**get_redirect_url**](RedirectURLsApi.md#get_redirect_url) | **GET** /redirect_urls/{id} | Retrieve a redirect URL
[**list_redirect_urls**](RedirectURLsApi.md#list_redirect_urls) | **GET** /redirect_urls | List all redirect URLs

# **create_redirect_url**
> RedirectURL create_redirect_url(body=body)

Create a redirect URL

Create a redirect URL

### Example

```python
from __future__ import print_function
import time
import clerk_client
from clerk_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = clerk_client.RedirectURLsApi(clerk_client.ApiClient(configuration))
body = clerk_client.RedirectUrlsBody()  # RedirectUrlsBody |  (optional)

try:
    # Create a redirect URL
    api_response = api_instance.create_redirect_url(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RedirectURLsApi->create_redirect_url: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RedirectUrlsBody**](RedirectUrlsBody.md)|  | [optional] 

### Return type

[**RedirectURL**](RedirectURL.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_redirect_url**
> DeletedObject delete_redirect_url(id)

Delete a redirect URL

Remove the selected redirect URL from the whitelist of the instance

### Example

```python
from __future__ import print_function
import time
import clerk_client
from clerk_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = clerk_client.RedirectURLsApi(clerk_client.ApiClient(configuration))
id = 'id_example'  # str | The ID of the redirect URL

try:
    # Delete a redirect URL
    api_response = api_instance.delete_redirect_url(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RedirectURLsApi->delete_redirect_url: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the redirect URL | 

### Return type

[**DeletedObject**](DeletedObject.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_redirect_url**
> RedirectURL get_redirect_url(id)

Retrieve a redirect URL

Retrieve the details of the redirect URL with the given ID

### Example

```python
from __future__ import print_function
import time
import clerk_client
from clerk_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = clerk_client.RedirectURLsApi(clerk_client.ApiClient(configuration))
id = 'id_example'  # str | The ID of the redirect URL

try:
    # Retrieve a redirect URL
    api_response = api_instance.get_redirect_url(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RedirectURLsApi->get_redirect_url: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the redirect URL | 

### Return type

[**RedirectURL**](RedirectURL.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_redirect_urls**
> list[RedirectURL] list_redirect_urls()

List all redirect URLs

Lists all whitelisted redirect_urls for the instance

### Example

```python
from __future__ import print_function
import time
import clerk_client
from clerk_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = clerk_client.RedirectURLsApi(clerk_client.ApiClient(configuration))

try:
    # List all redirect URLs
    api_response = api_instance.list_redirect_urls()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RedirectURLsApi->list_redirect_urls: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[RedirectURL]**](RedirectURL.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

