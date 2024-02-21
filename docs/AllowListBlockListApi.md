# clerk_client.AllowListBlockListApi

All URIs are relative to *https://api.clerk.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_allowlist_identifier**](AllowListBlockListApi.md#create_allowlist_identifier) | **POST** /allowlist_identifiers | Add identifier to the allow-list
[**create_blocklist_identifier**](AllowListBlockListApi.md#create_blocklist_identifier) | **POST** /blocklist_identifiers | Add identifier to the block-list
[**delete_allowlist_identifier**](AllowListBlockListApi.md#delete_allowlist_identifier) | **DELETE** /allowlist_identifiers/{identifier_id} | Delete identifier from allow-list
[**delete_blocklist_identifier**](AllowListBlockListApi.md#delete_blocklist_identifier) | **DELETE** /blocklist_identifiers/{identifier_id} | Delete identifier from block-list
[**list_allowlist_identifiers**](AllowListBlockListApi.md#list_allowlist_identifiers) | **GET** /allowlist_identifiers | List all identifiers on the allow-list
[**list_blocklist_identifiers**](AllowListBlockListApi.md#list_blocklist_identifiers) | **GET** /blocklist_identifiers | List all identifiers on the block-list

# **create_allowlist_identifier**
> AllowlistIdentifier create_allowlist_identifier(body=body)

Add identifier to the allow-list

Create an identifier allowed to sign up to an instance

### Example

```python
from __future__ import print_function
import time
import clerk_client
from clerk_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = clerk_client.AllowListBlockListApi(clerk_client.ApiClient(configuration))
body = clerk_client.AllowlistIdentifiersBody()  # AllowlistIdentifiersBody |  (optional)

try:
    # Add identifier to the allow-list
    api_response = api_instance.create_allowlist_identifier(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AllowListBlockListApi->create_allowlist_identifier: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AllowlistIdentifiersBody**](AllowlistIdentifiersBody.md)|  | [optional] 

### Return type

[**AllowlistIdentifier**](AllowlistIdentifier.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_blocklist_identifier**
> BlocklistIdentifier create_blocklist_identifier(body=body)

Add identifier to the block-list

Create an identifier that is blocked from accessing an instance

### Example

```python
from __future__ import print_function
import time
import clerk_client
from clerk_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = clerk_client.AllowListBlockListApi(clerk_client.ApiClient(configuration))
body = clerk_client.BlocklistIdentifiersBody()  # BlocklistIdentifiersBody |  (optional)

try:
    # Add identifier to the block-list
    api_response = api_instance.create_blocklist_identifier(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AllowListBlockListApi->create_blocklist_identifier: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**BlocklistIdentifiersBody**](BlocklistIdentifiersBody.md)|  | [optional] 

### Return type

[**BlocklistIdentifier**](BlocklistIdentifier.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_allowlist_identifier**
> DeletedObject delete_allowlist_identifier(identifier_id)

Delete identifier from allow-list

Delete an identifier from the instance allow-list

### Example

```python
from __future__ import print_function
import time
import clerk_client
from clerk_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = clerk_client.AllowListBlockListApi(clerk_client.ApiClient(configuration))
identifier_id = 'identifier_id_example'  # str | The ID of the identifier to delete from the allow-list

try:
    # Delete identifier from allow-list
    api_response = api_instance.delete_allowlist_identifier(identifier_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AllowListBlockListApi->delete_allowlist_identifier: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier_id** | **str**| The ID of the identifier to delete from the allow-list | 

### Return type

[**DeletedObject**](DeletedObject.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_blocklist_identifier**
> DeletedObject delete_blocklist_identifier(identifier_id)

Delete identifier from block-list

Delete an identifier from the instance block-list

### Example

```python
from __future__ import print_function
import time
import clerk_client
from clerk_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = clerk_client.AllowListBlockListApi(clerk_client.ApiClient(configuration))
identifier_id = 'identifier_id_example'  # str | The ID of the identifier to delete from the block-list

try:
    # Delete identifier from block-list
    api_response = api_instance.delete_blocklist_identifier(identifier_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AllowListBlockListApi->delete_blocklist_identifier: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier_id** | **str**| The ID of the identifier to delete from the block-list | 

### Return type

[**DeletedObject**](DeletedObject.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_allowlist_identifiers**
> list[AllowlistIdentifier] list_allowlist_identifiers()

List all identifiers on the allow-list

Get a list of all identifiers allowed to sign up to an instance

### Example

```python
from __future__ import print_function
import time
import clerk_client
from clerk_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = clerk_client.AllowListBlockListApi(clerk_client.ApiClient(configuration))

try:
    # List all identifiers on the allow-list
    api_response = api_instance.list_allowlist_identifiers()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AllowListBlockListApi->list_allowlist_identifiers: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[AllowlistIdentifier]**](AllowlistIdentifier.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_blocklist_identifiers**
> BlocklistIdentifiers list_blocklist_identifiers()

List all identifiers on the block-list

Get a list of all identifiers which are not allowed to access an instance

### Example

```python
from __future__ import print_function
import time
import clerk_client
from clerk_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = clerk_client.AllowListBlockListApi(clerk_client.ApiClient(configuration))

try:
    # List all identifiers on the block-list
    api_response = api_instance.list_blocklist_identifiers()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AllowListBlockListApi->list_blocklist_identifiers: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**BlocklistIdentifiers**](BlocklistIdentifiers.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

