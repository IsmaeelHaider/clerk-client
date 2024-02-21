# clerk_client.JWTTemplatesApi

All URIs are relative to *https://api.clerk.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_jwt_template**](JWTTemplatesApi.md#create_jwt_template) | **POST** /jwt_templates | Create a JWT template
[**delete_jwt_template**](JWTTemplatesApi.md#delete_jwt_template) | **DELETE** /jwt_templates/{template_id} | Delete a Template
[**get_jwt_template**](JWTTemplatesApi.md#get_jwt_template) | **GET** /jwt_templates/{template_id} | Retrieve a template
[**list_jwt_templates**](JWTTemplatesApi.md#list_jwt_templates) | **GET** /jwt_templates | List all templates
[**update_jwt_template**](JWTTemplatesApi.md#update_jwt_template) | **PATCH** /jwt_templates/{template_id} | Update a JWT template

# **create_jwt_template**
> JWTTemplate create_jwt_template(body=body)

Create a JWT template

Create a new JWT template

### Example

```python
from __future__ import print_function
import time
import clerk_client
from clerk_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = clerk_client.JWTTemplatesApi(clerk_client.ApiClient(configuration))
body = clerk_client.JwtTemplatesBody()  # JwtTemplatesBody |  (optional)

try:
    # Create a JWT template
    api_response = api_instance.create_jwt_template(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JWTTemplatesApi->create_jwt_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**JwtTemplatesBody**](JwtTemplatesBody.md)|  | [optional] 

### Return type

[**JWTTemplate**](JWTTemplate.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_jwt_template**
> DeletedObject delete_jwt_template(template_id)

Delete a Template

### Example

```python
from __future__ import print_function
import time
import clerk_client
from clerk_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = clerk_client.JWTTemplatesApi(clerk_client.ApiClient(configuration))
template_id = 'template_id_example'  # str | JWT Template ID

try:
    # Delete a Template
    api_response = api_instance.delete_jwt_template(template_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JWTTemplatesApi->delete_jwt_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **str**| JWT Template ID | 

### Return type

[**DeletedObject**](DeletedObject.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_jwt_template**
> JWTTemplate get_jwt_template(template_id)

Retrieve a template

Retrieve the details of a given JWT template

### Example

```python
from __future__ import print_function
import time
import clerk_client
from clerk_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = clerk_client.JWTTemplatesApi(clerk_client.ApiClient(configuration))
template_id = 'template_id_example'  # str | JWT Template ID

try:
    # Retrieve a template
    api_response = api_instance.get_jwt_template(template_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JWTTemplatesApi->get_jwt_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **str**| JWT Template ID | 

### Return type

[**JWTTemplate**](JWTTemplate.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_jwt_templates**
> list[JWTTemplate] list_jwt_templates()

List all templates

### Example

```python
from __future__ import print_function
import time
import clerk_client
from clerk_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = clerk_client.JWTTemplatesApi(clerk_client.ApiClient(configuration))

try:
    # List all templates
    api_response = api_instance.list_jwt_templates()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JWTTemplatesApi->list_jwt_templates: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[JWTTemplate]**](JWTTemplate.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_jwt_template**
> JWTTemplate update_jwt_template(template_id, body=body)

Update a JWT template

Updates an existing JWT template

### Example

```python
from __future__ import print_function
import time
import clerk_client
from clerk_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = clerk_client.JWTTemplatesApi(clerk_client.ApiClient(configuration))
template_id = 'template_id_example'  # str | The ID of the JWT template to update
body = clerk_client.JwtTemplatesTemplateIdBody()  # JwtTemplatesTemplateIdBody |  (optional)

try:
    # Update a JWT template
    api_response = api_instance.update_jwt_template(template_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JWTTemplatesApi->update_jwt_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **str**| The ID of the JWT template to update | 
 **body** | [**JwtTemplatesTemplateIdBody**](JwtTemplatesTemplateIdBody.md)|  | [optional] 

### Return type

[**JWTTemplate**](JWTTemplate.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

