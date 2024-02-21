# clerk_client.InstanceSettingsApi

All URIs are relative to *https://api.clerk.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**update_instance**](InstanceSettingsApi.md#update_instance) | **PATCH** /instance | Update instance settings
[**update_instance_organization_settings**](InstanceSettingsApi.md#update_instance_organization_settings) | **PATCH** /instance/organization_settings | Update instance organization settings
[**update_instance_restrictions**](InstanceSettingsApi.md#update_instance_restrictions) | **PATCH** /instance/restrictions | Update instance restrictions

# **update_instance**
> update_instance(body=body)

Update instance settings

Updates the settings of an instance

### Example

```python
from __future__ import print_function
import time
import clerk_client
from clerk_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = clerk_client.InstanceSettingsApi(clerk_client.ApiClient(configuration))
body = clerk_client.InstanceBody()  # InstanceBody |  (optional)

try:
    # Update instance settings
    api_instance.update_instance(body=body)
except ApiException as e:
    print("Exception when calling InstanceSettingsApi->update_instance: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**InstanceBody**](InstanceBody.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_instance_organization_settings**
> OrganizationSettings update_instance_organization_settings(body=body)

Update instance organization settings

Updates the organization settings of the instance

### Example

```python
from __future__ import print_function
import time
import clerk_client
from clerk_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = clerk_client.InstanceSettingsApi(clerk_client.ApiClient(configuration))
body = clerk_client.InstanceOrganizationSettingsBody()  # InstanceOrganizationSettingsBody |  (optional)

try:
    # Update instance organization settings
    api_response = api_instance.update_instance_organization_settings(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InstanceSettingsApi->update_instance_organization_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**InstanceOrganizationSettingsBody**](InstanceOrganizationSettingsBody.md)|  | [optional] 

### Return type

[**OrganizationSettings**](OrganizationSettings.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_instance_restrictions**
> InstanceRestrictions update_instance_restrictions(body=body)

Update instance restrictions

Updates the restriction settings of an instance

### Example

```python
from __future__ import print_function
import time
import clerk_client
from clerk_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = clerk_client.InstanceSettingsApi(clerk_client.ApiClient(configuration))
body = clerk_client.InstanceRestrictionsBody()  # InstanceRestrictionsBody |  (optional)

try:
    # Update instance restrictions
    api_response = api_instance.update_instance_restrictions(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InstanceSettingsApi->update_instance_restrictions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**InstanceRestrictionsBody**](InstanceRestrictionsBody.md)|  | [optional] 

### Return type

[**InstanceRestrictions**](InstanceRestrictions.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

