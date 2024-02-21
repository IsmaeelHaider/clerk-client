# swagger_client.WebhooksApi

All URIs are relative to *https://api.clerk.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_svix_app**](WebhooksApi.md#create_svix_app) | **POST** /webhooks/svix | Create a Svix app
[**delete_svix_app**](WebhooksApi.md#delete_svix_app) | **DELETE** /webhooks/svix | Delete a Svix app
[**generate_svix_auth_url**](WebhooksApi.md#generate_svix_auth_url) | **POST** /webhooks/svix_url | Create a Svix Dashboard URL

# **create_svix_app**
> SvixURL create_svix_app()

Create a Svix app

Create a Svix app and associate it with the current instance

### Example

```python
from __future__ import print_function
import time
import clerk_client
from clerk_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = clerk_client.WebhooksApi(clerk_client.ApiClient(configuration))

try:
    # Create a Svix app
    api_response = api_instance.create_svix_app()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebhooksApi->create_svix_app: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**SvixURL**](SvixURL.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_svix_app**
> delete_svix_app()

Delete a Svix app

Delete a Svix app and disassociate it from the current instance

### Example

```python
from __future__ import print_function
import time
import clerk_client
from clerk_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = clerk_client.WebhooksApi(clerk_client.ApiClient(configuration))

try:
    # Delete a Svix app
    api_instance.delete_svix_app()
except ApiException as e:
    print("Exception when calling WebhooksApi->delete_svix_app: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_svix_auth_url**
> SvixURL generate_svix_auth_url()

Create a Svix Dashboard URL

Generate a new url for accessing the Svix's management dashboard for that particular instance

### Example

```python
from __future__ import print_function
import time
import clerk_client
from clerk_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = clerk_client.WebhooksApi(clerk_client.ApiClient(configuration))

try:
    # Create a Svix Dashboard URL
    api_response = api_instance.generate_svix_auth_url()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebhooksApi->generate_svix_auth_url: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**SvixURL**](SvixURL.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

