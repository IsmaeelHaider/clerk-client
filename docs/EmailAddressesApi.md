# swagger_client.EmailAddressesApi

All URIs are relative to *https://api.clerk.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_email_address**](EmailAddressesApi.md#create_email_address) | **POST** /email_addresses | Create an email address
[**delete_email_address**](EmailAddressesApi.md#delete_email_address) | **DELETE** /email_addresses/{email_address_id} | Delete an email address
[**get_email_address**](EmailAddressesApi.md#get_email_address) | **GET** /email_addresses/{email_address_id} | Retrieve an email address
[**update_email_address**](EmailAddressesApi.md#update_email_address) | **PATCH** /email_addresses/{email_address_id} | Update an email address

# **create_email_address**
> EmailAddress create_email_address(body=body)

Create an email address

Create a new email address

### Example

```python
from __future__ import print_function
import time
import clerk_client
from clerk_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = clerk_client.EmailAddressesApi(clerk_client.ApiClient(configuration))
body = clerk_client.EmailAddressesBody()  # EmailAddressesBody |  (optional)

try:
    # Create an email address
    api_response = api_instance.create_email_address(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EmailAddressesApi->create_email_address: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EmailAddressesBody**](EmailAddressesBody.md)|  | [optional] 

### Return type

[**EmailAddress**](EmailAddress.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_email_address**
> DeletedObject delete_email_address(email_address_id)

Delete an email address

Delete the email address with the given ID

### Example

```python
from __future__ import print_function
import time
import clerk_client
from clerk_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = clerk_client.EmailAddressesApi(clerk_client.ApiClient(configuration))
email_address_id = 'email_address_id_example'  # str | The ID of the email address to delete

try:
    # Delete an email address
    api_response = api_instance.delete_email_address(email_address_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EmailAddressesApi->delete_email_address: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email_address_id** | **str**| The ID of the email address to delete | 

### Return type

[**DeletedObject**](DeletedObject.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_email_address**
> EmailAddress get_email_address(email_address_id)

Retrieve an email address

Returns the details of an email address.

### Example

```python
from __future__ import print_function
import time
import clerk_client
from clerk_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = clerk_client.EmailAddressesApi(clerk_client.ApiClient(configuration))
email_address_id = 'email_address_id_example'  # str | The ID of the email address to retrieve

try:
    # Retrieve an email address
    api_response = api_instance.get_email_address(email_address_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EmailAddressesApi->get_email_address: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email_address_id** | **str**| The ID of the email address to retrieve | 

### Return type

[**EmailAddress**](EmailAddress.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_email_address**
> EmailAddress update_email_address(email_address_id, body=body)

Update an email address

Updates an email address.

### Example

```python
from __future__ import print_function
import time
import clerk_client
from clerk_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = clerk_client.EmailAddressesApi(clerk_client.ApiClient(configuration))
email_address_id = 'email_address_id_example'  # str | The ID of the email address to update
body = clerk_client.EmailAddressesEmailAddressIdBody()  # EmailAddressesEmailAddressIdBody |  (optional)

try:
    # Update an email address
    api_response = api_instance.update_email_address(email_address_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EmailAddressesApi->update_email_address: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email_address_id** | **str**| The ID of the email address to update | 
 **body** | [**EmailAddressesEmailAddressIdBody**](EmailAddressesEmailAddressIdBody.md)|  | [optional] 

### Return type

[**EmailAddress**](EmailAddress.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

