# swagger_client.OrganizationMembershipsApi

All URIs are relative to *https://api.clerk.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_organization_membership**](OrganizationMembershipsApi.md#create_organization_membership) | **POST** /organizations/{organization_id}/memberships | Create a new organization membership
[**delete_organization_membership**](OrganizationMembershipsApi.md#delete_organization_membership) | **DELETE** /organizations/{organization_id}/memberships/{user_id} | Remove a member from an organization
[**list_organization_memberships**](OrganizationMembershipsApi.md#list_organization_memberships) | **GET** /organizations/{organization_id}/memberships | Get a list of all members of an organization
[**update_organization_membership**](OrganizationMembershipsApi.md#update_organization_membership) | **PATCH** /organizations/{organization_id}/memberships/{user_id} | Update an organization membership
[**update_organization_membership_metadata**](OrganizationMembershipsApi.md#update_organization_membership_metadata) | **PATCH** /organizations/{organization_id}/memberships/{user_id}/metadata | Merge and update organization membership metadata

# **create_organization_membership**
> OrganizationMembership create_organization_membership(body, organization_id)

Create a new organization membership

Adds a user as a member to the given organization. Only users in the same instance as the organization can be added as members.

### Example

```python
from __future__ import print_function
import time
import clerk_client
from clerk_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = clerk_client.OrganizationMembershipsApi(clerk_client.ApiClient(configuration))
body = clerk_client.OrganizationIdMembershipsBody()  # OrganizationIdMembershipsBody | 
organization_id = 'organization_id_example'  # str | The ID of the organization where the new membership will be created

try:
    # Create a new organization membership
    api_response = api_instance.create_organization_membership(body, organization_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationMembershipsApi->create_organization_membership: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**OrganizationIdMembershipsBody**](OrganizationIdMembershipsBody.md)|  | 
 **organization_id** | **str**| The ID of the organization where the new membership will be created | 

### Return type

[**OrganizationMembership**](OrganizationMembership.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_organization_membership**
> OrganizationMembership delete_organization_membership(organization_id, user_id)

Remove a member from an organization

Removes the given membership from the organization

### Example

```python
from __future__ import print_function
import time
import clerk_client
from clerk_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = clerk_client.OrganizationMembershipsApi(clerk_client.ApiClient(configuration))
organization_id = 'organization_id_example'  # str | The ID of the organization the membership belongs to
user_id = 'user_id_example'  # str | The ID of the user that this membership belongs to

try:
    # Remove a member from an organization
    api_response = api_instance.delete_organization_membership(organization_id, user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationMembershipsApi->delete_organization_membership: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| The ID of the organization the membership belongs to | 
 **user_id** | **str**| The ID of the user that this membership belongs to | 

### Return type

[**OrganizationMembership**](OrganizationMembership.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_organization_memberships**
> OrganizationMemberships list_organization_memberships(organization_id, limit=limit, offset=offset, order_by=order_by)

Get a list of all members of an organization

Retrieves all user memberships for the given organization

### Example

```python
from __future__ import print_function
import time
import clerk_client
from clerk_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = clerk_client.OrganizationMembershipsApi(clerk_client.ApiClient(configuration))
organization_id = 'organization_id_example'  # str | The organization ID.
limit = 10  # float | Applies a limit to the number of results returned. Can be used for paginating the results together with `offset`. Must be an integer greater than zero and less than 500. By default, if not supplied, a limit of 10 is used. (optional) (default to 10)
offset = 0  # float | Skip the first `offset` results when paginating. Needs to be an integer greater or equal to zero. To be used in conjunction with `limit`. (optional) (default to 0)
order_by = 'order_by_example'  # str | Sorts organizations memberships by phone_number, email_address, created_at, first_name, last_name or username. By prepending one of those values with + or -, we can choose to sort in ascending (ASC) or descending (DESC) order.\" (optional)

try:
    # Get a list of all members of an organization
    api_response = api_instance.list_organization_memberships(organization_id, limit=limit, offset=offset,
                                                              order_by=order_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationMembershipsApi->list_organization_memberships: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| The organization ID. | 
 **limit** | **float**| Applies a limit to the number of results returned. Can be used for paginating the results together with &#x60;offset&#x60;. Must be an integer greater than zero and less than 500. By default, if not supplied, a limit of 10 is used. | [optional] [default to 10]
 **offset** | **float**| Skip the first &#x60;offset&#x60; results when paginating. Needs to be an integer greater or equal to zero. To be used in conjunction with &#x60;limit&#x60;. | [optional] [default to 0]
 **order_by** | **str**| Sorts organizations memberships by phone_number, email_address, created_at, first_name, last_name or username. By prepending one of those values with + or -, we can choose to sort in ascending (ASC) or descending (DESC) order.\&quot; | [optional] 

### Return type

[**OrganizationMemberships**](OrganizationMemberships.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_organization_membership**
> OrganizationMembership update_organization_membership(body, organization_id, user_id)

Update an organization membership

Updates the properties of an existing organization membership

### Example

```python
from __future__ import print_function
import time
import clerk_client
from clerk_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = clerk_client.OrganizationMembershipsApi(clerk_client.ApiClient(configuration))
body = clerk_client.MembershipsUserIdBody()  # MembershipsUserIdBody | 
organization_id = 'organization_id_example'  # str | The ID of the organization the membership belongs to
user_id = 'user_id_example'  # str | The ID of the user that this membership belongs to

try:
    # Update an organization membership
    api_response = api_instance.update_organization_membership(body, organization_id, user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationMembershipsApi->update_organization_membership: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MembershipsUserIdBody**](MembershipsUserIdBody.md)|  | 
 **organization_id** | **str**| The ID of the organization the membership belongs to | 
 **user_id** | **str**| The ID of the user that this membership belongs to | 

### Return type

[**OrganizationMembership**](OrganizationMembership.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_organization_membership_metadata**
> OrganizationMembership update_organization_membership_metadata(body, organization_id, user_id)

Merge and update organization membership metadata

Update an organization membership's metadata attributes by merging existing values with the provided parameters. Metadata values will be updated via a deep merge. Deep means that any nested JSON objects will be merged as well. You can remove metadata keys at any level by setting their value to `null`.

### Example

```python
from __future__ import print_function
import time
import clerk_client
from clerk_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = clerk_client.OrganizationMembershipsApi(clerk_client.ApiClient(configuration))
body = clerk_client.UserIdMetadataBody1()  # UserIdMetadataBody1 | 
organization_id = 'organization_id_example'  # str | The ID of the organization the membership belongs to
user_id = 'user_id_example'  # str | The ID of the user that this membership belongs to

try:
    # Merge and update organization membership metadata
    api_response = api_instance.update_organization_membership_metadata(body, organization_id, user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationMembershipsApi->update_organization_membership_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UserIdMetadataBody1**](UserIdMetadataBody1.md)|  | 
 **organization_id** | **str**| The ID of the organization the membership belongs to | 
 **user_id** | **str**| The ID of the user that this membership belongs to | 

### Return type

[**OrganizationMembership**](OrganizationMembership.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

