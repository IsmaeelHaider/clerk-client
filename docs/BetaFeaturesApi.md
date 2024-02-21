# clerk_client.BetaFeaturesApi

All URIs are relative to *https://api.clerk.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**change_production_instance_domain**](BetaFeaturesApi.md#change_production_instance_domain) | **POST** /instance/change_domain | Update production instance domain
[**update_instance_auth_config**](BetaFeaturesApi.md#update_instance_auth_config) | **PATCH** /beta_features/instance_settings | Update instance settings
[**update_production_instance_domain**](BetaFeaturesApi.md#update_production_instance_domain) | **PUT** /beta_features/domain | Update production instance domain

# **change_production_instance_domain**
> change_production_instance_domain(body=body)

Update production instance domain

Change the domain of a production instance.  Changing the domain requires updating the [DNS records](https://clerk.com/docs/deployments/overview#dns-records) accordingly, deploying new [SSL certificates](https://clerk.com/docs/deployments/overview#deploy), updating your Social Connection's redirect URLs and setting the new keys in your code.  WARNING: Changing your domain will invalidate all current user sessions (i.e. users will be logged out). Also, while your application is being deployed, a small downtime is expected to occur.

### Example

```python
from __future__ import print_function
import time
import clerk_client
from clerk_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = clerk_client.BetaFeaturesApi(clerk_client.ApiClient(configuration))
body = clerk_client.InstanceChangeDomainBody()  # InstanceChangeDomainBody |  (optional)

try:
    # Update production instance domain
    api_instance.change_production_instance_domain(body=body)
except ApiException as e:
    print("Exception when calling BetaFeaturesApi->change_production_instance_domain: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**InstanceChangeDomainBody**](InstanceChangeDomainBody.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_instance_auth_config**
> InlineResponse2006 update_instance_auth_config(body=body)

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
api_instance = clerk_client.BetaFeaturesApi(clerk_client.ApiClient(configuration))
body = clerk_client.BetaFeaturesInstanceSettingsBody()  # BetaFeaturesInstanceSettingsBody |  (optional)

try:
    # Update instance settings
    api_response = api_instance.update_instance_auth_config(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BetaFeaturesApi->update_instance_auth_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**BetaFeaturesInstanceSettingsBody**](BetaFeaturesInstanceSettingsBody.md)|  | [optional] 

### Return type

[**InlineResponse2006**](InlineResponse2006.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_production_instance_domain**
> update_production_instance_domain(body=body)

Update production instance domain

Change the domain of a production instance.  Changing the domain requires updating the [DNS records](https://clerk.com/docs/deployments/overview#dns-records) accordingly, deploying new [SSL certificates](https://clerk.com/docs/deployments/overview#deploy), updating your Social Connection's redirect URLs and setting the new keys in your code.  WARNING: Changing your domain will invalidate all current user sessions (i.e. users will be logged out). Also, while your application is being deployed, a small downtime is expected to occur.

### Example

```python
from __future__ import print_function
import time
import clerk_client
from clerk_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = clerk_client.BetaFeaturesApi(clerk_client.ApiClient(configuration))
body = clerk_client.BetaFeaturesDomainBody()  # BetaFeaturesDomainBody |  (optional)

try:
    # Update production instance domain
    api_instance.update_production_instance_domain(body=body)
except ApiException as e:
    print("Exception when calling BetaFeaturesApi->update_production_instance_domain: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**BetaFeaturesDomainBody**](BetaFeaturesDomainBody.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

