# swagger_client.DomainsApi

All URIs are relative to *https://api.clerk.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_domain**](DomainsApi.md#add_domain) | **POST** /domains | Add a domain
[**delete_domain**](DomainsApi.md#delete_domain) | **DELETE** /domains/{domain_id} | Delete a satellite domain
[**list_domains**](DomainsApi.md#list_domains) | **GET** /domains | List all instance domains
[**update_domain**](DomainsApi.md#update_domain) | **PATCH** /domains/{domain_id} | Update a domain

# **add_domain**
> Domain add_domain(body=body)

Add a domain

Add a new domain for your instance. Useful in the case of multi-domain instances, allows adding satellite domains to an instance. The new domain must have a `name`. The domain name can contain the port for development instances, like `localhost:3000`. At the moment, instances can have only one primary domain, so the `is_satellite` parameter must be set to `true`. If you're planning to configure the new satellite domain to run behind a proxy, pass the `proxy_url` parameter accordingly.

### Example

```python
from __future__ import print_function
import time
import clerk_client
from clerk_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = clerk_client.DomainsApi(clerk_client.ApiClient(configuration))
body = clerk_client.DomainsBody()  # DomainsBody |  (optional)

try:
    # Add a domain
    api_response = api_instance.add_domain(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DomainsApi->add_domain: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DomainsBody**](DomainsBody.md)|  | [optional] 

### Return type

[**Domain**](Domain.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_domain**
> DeletedObject delete_domain(domain_id)

Delete a satellite domain

Deletes a satellite domain for the instance. It is currently not possible to delete the instance's primary domain.

### Example

```python
from __future__ import print_function
import time
import clerk_client
from clerk_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = clerk_client.DomainsApi(clerk_client.ApiClient(configuration))
domain_id = 'domain_id_example'  # str | The ID of the domain that will be deleted. Must be a satellite domain.

try:
    # Delete a satellite domain
    api_response = api_instance.delete_domain(domain_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DomainsApi->delete_domain: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_id** | **str**| The ID of the domain that will be deleted. Must be a satellite domain. | 

### Return type

[**DeletedObject**](DeletedObject.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_domains**
> Domains list_domains()

List all instance domains

Use this endpoint to get a list of all domains for an instance. The response will contain the primary domain for the instance and any satellite domains. Each domain in the response contains information about the URLs where Clerk operates and the required CNAME targets.

### Example

```python
from __future__ import print_function
import time
import clerk_client
from clerk_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = clerk_client.DomainsApi(clerk_client.ApiClient(configuration))

try:
    # List all instance domains
    api_response = api_instance.list_domains()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DomainsApi->list_domains: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Domains**](Domains.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_domain**
> Domain update_domain(body, domain_id)

Update a domain

The `proxy_url` can be updated only for production instances. Update one of the instance's domains. Both primary and satellite domains can be updated. If you choose to use Clerk via proxy, use this endpoint to specify the `proxy_url`. Whenever you decide you'd rather switch to DNS setup for Clerk, simply set `proxy_url` to `null` for the domain. When you update a production instance's primary domain name, you have to make sure that you've completed all the necessary setup steps for DNS and emails to work. Expect downtime otherwise. Updating a primary domain's name will also update the instance's home origin, affecting the default application paths.

### Example

```python
from __future__ import print_function
import time
import clerk_client
from clerk_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = clerk_client.DomainsApi(clerk_client.ApiClient(configuration))
body = clerk_client.DomainsDomainIdBody()  # DomainsDomainIdBody | 
domain_id = 'domain_id_example'  # str | The ID of the domain that will be updated.

try:
    # Update a domain
    api_response = api_instance.update_domain(body, domain_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DomainsApi->update_domain: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DomainsDomainIdBody**](DomainsDomainIdBody.md)|  | 
 **domain_id** | **str**| The ID of the domain that will be updated. | 

### Return type

[**Domain**](Domain.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

