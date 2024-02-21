# clerk_client.EmailSMSTemplatesApi

All URIs are relative to *https://api.clerk.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_template**](EmailSMSTemplatesApi.md#get_template) | **GET** /templates/{template_type}/{slug} | Retrieve a template
[**get_template_list**](EmailSMSTemplatesApi.md#get_template_list) | **GET** /templates/{template_type} | List all templates
[**preview_template**](EmailSMSTemplatesApi.md#preview_template) | **POST** /templates/{template_type}/{slug}/preview | Preview changes to a template
[**revert_template**](EmailSMSTemplatesApi.md#revert_template) | **POST** /templates/{template_type}/{slug}/revert | Revert a template
[**toggle_template_delivery**](EmailSMSTemplatesApi.md#toggle_template_delivery) | **POST** /templates/{template_type}/{slug}/toggle_delivery | Toggle the delivery by Clerk for a template of a given type and slug
[**upsert_template**](EmailSMSTemplatesApi.md#upsert_template) | **PUT** /templates/{template_type}/{slug} | Update a template for a given type and slug

# **get_template**
> Template get_template(template_type, slug)

Retrieve a template

Returns the details of a template

### Example

```python
from __future__ import print_function
import time
import clerk_client
from clerk_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = clerk_client.EmailSMSTemplatesApi(clerk_client.ApiClient(configuration))
template_type = 'template_type_example'  # str | The type of templates to retrieve (email or SMS)
slug = 'slug_example'  # str | The slug (i.e. machine-friendly name) of the template to retrieve

try:
    # Retrieve a template
    api_response = api_instance.get_template(template_type, slug)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EmailSMSTemplatesApi->get_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_type** | **str**| The type of templates to retrieve (email or SMS) | 
 **slug** | **str**| The slug (i.e. machine-friendly name) of the template to retrieve | 

### Return type

[**Template**](Template.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_template_list**
> list[Template] get_template_list(template_type)

List all templates

Returns a list of all templates. The templates are returned sorted by position.

### Example

```python
from __future__ import print_function
import time
import clerk_client
from clerk_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = clerk_client.EmailSMSTemplatesApi(clerk_client.ApiClient(configuration))
template_type = 'template_type_example'  # str | The type of templates to list (email or SMS)

try:
    # List all templates
    api_response = api_instance.get_template_list(template_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EmailSMSTemplatesApi->get_template_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_type** | **str**| The type of templates to list (email or SMS) | 

### Return type

[**list[Template]**](Template.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **preview_template**
> object preview_template(template_type, slug, body=body)

Preview changes to a template

Returns a preview of a template for a given template_type, slug and body

### Example

```python
from __future__ import print_function
import time
import clerk_client
from clerk_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = clerk_client.EmailSMSTemplatesApi(clerk_client.ApiClient(configuration))
template_type = 'template_type_example'  # str | The type of template to preview
slug = 'slug_example'  # str | The slug of the template to preview
body = clerk_client.SlugPreviewBody()  # SlugPreviewBody | Required parameters (optional)

try:
    # Preview changes to a template
    api_response = api_instance.preview_template(template_type, slug, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EmailSMSTemplatesApi->preview_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_type** | **str**| The type of template to preview | 
 **slug** | **str**| The slug of the template to preview | 
 **body** | [**SlugPreviewBody**](SlugPreviewBody.md)| Required parameters | [optional] 

### Return type

**object**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **revert_template**
> Template revert_template(template_type, slug)

Revert a template

Reverts an updated template to its default state

### Example

```python
from __future__ import print_function
import time
import clerk_client
from clerk_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = clerk_client.EmailSMSTemplatesApi(clerk_client.ApiClient(configuration))
template_type = 'template_type_example'  # str | The type of template to revert
slug = 'slug_example'  # str | The slug of the template to revert

try:
    # Revert a template
    api_response = api_instance.revert_template(template_type, slug)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EmailSMSTemplatesApi->revert_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_type** | **str**| The type of template to revert | 
 **slug** | **str**| The slug of the template to revert | 

### Return type

[**Template**](Template.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **toggle_template_delivery**
> Template toggle_template_delivery(template_type, slug, body=body)

Toggle the delivery by Clerk for a template of a given type and slug

Toggles the delivery by Clerk for a template of a given type and slug. If disabled, Clerk will not deliver the resulting email or SMS. The app developer will need to listen to the `email.created` or `sms.created` webhooks in order to handle delivery themselves.

### Example

```python
from __future__ import print_function
import time
import clerk_client
from clerk_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = clerk_client.EmailSMSTemplatesApi(clerk_client.ApiClient(configuration))
template_type = 'template_type_example'  # str | The type of template to toggle delivery for
slug = 'slug_example'  # str | The slug of the template for which to toggle delivery
body = clerk_client.SlugToggleDeliveryBody()  # SlugToggleDeliveryBody |  (optional)

try:
    # Toggle the delivery by Clerk for a template of a given type and slug
    api_response = api_instance.toggle_template_delivery(template_type, slug, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EmailSMSTemplatesApi->toggle_template_delivery: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_type** | **str**| The type of template to toggle delivery for | 
 **slug** | **str**| The slug of the template for which to toggle delivery | 
 **body** | [**SlugToggleDeliveryBody**](SlugToggleDeliveryBody.md)|  | [optional] 

### Return type

[**Template**](Template.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upsert_template**
> Template upsert_template(template_type, slug, body=body)

Update a template for a given type and slug

Updates the existing template of the given type and slug

### Example

```python
from __future__ import print_function
import time
import clerk_client
from clerk_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = clerk_client.EmailSMSTemplatesApi(clerk_client.ApiClient(configuration))
template_type = 'template_type_example'  # str | The type of template to update
slug = 'slug_example'  # str | The slug of the template to update
body = clerk_client.TemplateTypeSlugBody()  # TemplateTypeSlugBody |  (optional)

try:
    # Update a template for a given type and slug
    api_response = api_instance.upsert_template(template_type, slug, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EmailSMSTemplatesApi->upsert_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_type** | **str**| The type of template to update | 
 **slug** | **str**| The slug of the template to update | 
 **body** | [**TemplateTypeSlugBody**](TemplateTypeSlugBody.md)|  | [optional] 

### Return type

[**Template**](Template.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

