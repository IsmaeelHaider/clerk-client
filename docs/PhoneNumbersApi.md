# clerk_client.PhoneNumbersApi

All URIs are relative to *https://api.clerk.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_phone_number**](PhoneNumbersApi.md#create_phone_number) | **POST** /phone_numbers | Create a phone number
[**delete_phone_number**](PhoneNumbersApi.md#delete_phone_number) | **DELETE** /phone_numbers/{phone_number_id} | Delete a phone number
[**get_phone_number**](PhoneNumbersApi.md#get_phone_number) | **GET** /phone_numbers/{phone_number_id} | Retrieve a phone number
[**update_phone_number**](PhoneNumbersApi.md#update_phone_number) | **PATCH** /phone_numbers/{phone_number_id} | Update a phone number

# **create_phone_number**
> PhoneNumber create_phone_number(body=body)

Create a phone number

Create a new phone number

### Example

```python
from __future__ import print_function
import time
import clerk_client
from clerk_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = clerk_client.PhoneNumbersApi(clerk_client.ApiClient(configuration))
body = clerk_client.PhoneNumbersBody()  # PhoneNumbersBody |  (optional)

try:
    # Create a phone number
    api_response = api_instance.create_phone_number(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PhoneNumbersApi->create_phone_number: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PhoneNumbersBody**](PhoneNumbersBody.md)|  | [optional] 

### Return type

[**PhoneNumber**](PhoneNumber.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_phone_number**
> DeletedObject delete_phone_number(phone_number_id)

Delete a phone number

Delete the phone number with the given ID

### Example

```python
from __future__ import print_function
import time
import clerk_client
from clerk_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = clerk_client.PhoneNumbersApi(clerk_client.ApiClient(configuration))
phone_number_id = 'phone_number_id_example'  # str | The ID of the phone number to delete

try:
    # Delete a phone number
    api_response = api_instance.delete_phone_number(phone_number_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PhoneNumbersApi->delete_phone_number: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **phone_number_id** | **str**| The ID of the phone number to delete | 

### Return type

[**DeletedObject**](DeletedObject.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_phone_number**
> PhoneNumber get_phone_number(phone_number_id)

Retrieve a phone number

Returns the details of a phone number

### Example

```python
from __future__ import print_function
import time
import clerk_client
from clerk_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = clerk_client.PhoneNumbersApi(clerk_client.ApiClient(configuration))
phone_number_id = 'phone_number_id_example'  # str | The ID of the phone number to retrieve

try:
    # Retrieve a phone number
    api_response = api_instance.get_phone_number(phone_number_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PhoneNumbersApi->get_phone_number: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **phone_number_id** | **str**| The ID of the phone number to retrieve | 

### Return type

[**PhoneNumber**](PhoneNumber.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_phone_number**
> PhoneNumber update_phone_number(phone_number_id, body=body)

Update a phone number

Updates a phone number

### Example

```python
from __future__ import print_function
import time
import clerk_client
from clerk_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = clerk_client.PhoneNumbersApi(clerk_client.ApiClient(configuration))
phone_number_id = 'phone_number_id_example'  # str | The ID of the phone number to update
body = clerk_client.PhoneNumbersPhoneNumberIdBody()  # PhoneNumbersPhoneNumberIdBody |  (optional)

try:
    # Update a phone number
    api_response = api_instance.update_phone_number(phone_number_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PhoneNumbersApi->update_phone_number: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **phone_number_id** | **str**| The ID of the phone number to update | 
 **body** | [**PhoneNumbersPhoneNumberIdBody**](PhoneNumbersPhoneNumberIdBody.md)|  | [optional] 

### Return type

[**PhoneNumber**](PhoneNumber.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

