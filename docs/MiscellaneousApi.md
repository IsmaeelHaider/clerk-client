# clerk_client.MiscellaneousApi

All URIs are relative to *https://api.clerk.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_public_interstitial**](MiscellaneousApi.md#get_public_interstitial) | **GET** /public/interstitial | Returns the markup for the interstitial page

# **get_public_interstitial**
> get_public_interstitial(frontend_api=frontend_api, publishable_key=publishable_key)

Returns the markup for the interstitial page

The Clerk interstitial endpoint serves an html page that loads clerk.js in order to check the user's authentication state. It is used by Clerk SDKs when the user's authentication state cannot be immediately determined.

### Example

```python
from __future__ import print_function
import time
import clerk_client
from clerk_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = clerk_client.MiscellaneousApi()
frontend_api = 'frontend_api_example'  # str | The Frontend API key of your instance (optional)
publishable_key = 'publishable_key_example'  # str | The publishable key of your instance (optional)

try:
    # Returns the markup for the interstitial page
    api_instance.get_public_interstitial(frontend_api=frontend_api, publishable_key=publishable_key)
except ApiException as e:
    print("Exception when calling MiscellaneousApi->get_public_interstitial: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **frontend_api** | **str**| The Frontend API key of your instance | [optional] 
 **publishable_key** | **str**| The publishable key of your instance | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

