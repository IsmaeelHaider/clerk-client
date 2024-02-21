# clerk_client.OrganizationsApi

All URIs are relative to *https://api.clerk.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_organization**](OrganizationsApi.md#create_organization) | **POST** /organizations | Create an organization
[**delete_organization**](OrganizationsApi.md#delete_organization) | **DELETE** /organizations/{organization_id} | Delete an organization
[**delete_organization_logo**](OrganizationsApi.md#delete_organization_logo) | **DELETE** /organizations/{organization_id}/logo | 
[**get_organization**](OrganizationsApi.md#get_organization) | **GET** /organizations/{organization_id} | Retrieve an organization by ID or slug
[**list_organizations**](OrganizationsApi.md#list_organizations) | **GET** /organizations | Get a list of organizations for an instance
[**merge_organization_metadata**](OrganizationsApi.md#merge_organization_metadata) | **PATCH** /organizations/{organization_id}/metadata | Merge and update metadata for an organization
[**update_organization**](OrganizationsApi.md#update_organization) | **PATCH** /organizations/{organization_id} | Update an organization
[**upload_organization_logo**](OrganizationsApi.md#upload_organization_logo) | **PUT** /organizations/{organization_id}/logo | Upload a logo for the organization

# **create_organization**
> Organization create_organization(body=body)

Create an organization

Creates a new organization with the given name for an instance. In order to successfully create an organization you need to provide the ID of the User who will become the organization administrator. You can specify an optional slug for the new organization. If provided, the organization slug can contain only lowercase alphanumeric characters (letters and digits) and the dash \"-\". Organization slugs must be unique for the instance. You can provide additional metadata for the organization and set any custom attribute you want. Organizations support private and public metadata. Private metadata can only be accessed from the Backend API. Public metadata can be accessed from the Backend API, and are read-only from the Frontend API.

### Example

```python
from __future__ import print_function
import time
import clerk_client
from clerk_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = clerk_client.OrganizationsApi(clerk_client.ApiClient(configuration))
body = clerk_client.OrganizationsBody()  # OrganizationsBody |  (optional)

try:
    # Create an organization
    api_response = api_instance.create_organization(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationsApi->create_organization: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**OrganizationsBody**](OrganizationsBody.md)|  | [optional] 

### Return type

[**Organization**](Organization.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_organization**
> DeletedObject delete_organization(organization_id)

Delete an organization

Deletes the given organization. Please note that deleting an organization will also delete all memberships and invitations. This is not reversible.

### Example

```python
from __future__ import print_function
import time
import clerk_client
from clerk_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = clerk_client.OrganizationsApi(clerk_client.ApiClient(configuration))
organization_id = 'organization_id_example'  # str | The ID of the organization to delete

try:
    # Delete an organization
    api_response = api_instance.delete_organization(organization_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationsApi->delete_organization: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| The ID of the organization to delete | 

### Return type

[**DeletedObject**](DeletedObject.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_organization_logo**
> Organization delete_organization_logo(organization_id)



Delete the organization's logo.

### Example

```python
from __future__ import print_function
import time
import clerk_client
from clerk_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = clerk_client.OrganizationsApi(clerk_client.ApiClient(configuration))
organization_id = 'organization_id_example'  # str | The ID of the organization for which the logo will be deleted.

try:
    api_response = api_instance.delete_organization_logo(organization_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationsApi->delete_organization_logo: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| The ID of the organization for which the logo will be deleted. | 

### Return type

[**Organization**](Organization.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_organization**
> Organization get_organization(organization_id)

Retrieve an organization by ID or slug

Fetches the organization whose ID or slug matches the provided `id_or_slug` URL query parameter.

### Example

```python
from __future__ import print_function
import time
import clerk_client
from clerk_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = clerk_client.OrganizationsApi(clerk_client.ApiClient(configuration))
organization_id = 'organization_id_example'  # str | The ID or slug of the organization

try:
    # Retrieve an organization by ID or slug
    api_response = api_instance.get_organization(organization_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationsApi->get_organization: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| The ID or slug of the organization | 

### Return type

[**Organization**](Organization.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_organizations**
> Organizations list_organizations(limit=limit, offset=offset, include_members_count=include_members_count, query=query, order_by=order_by)

Get a list of organizations for an instance

This request returns the list of organizations for an instance. Results can be paginated using the optional `limit` and `offset` query parameters. The organizations are ordered by descending creation date. Most recent organizations will be returned first.

### Example

```python
from __future__ import print_function
import time
import clerk_client
from clerk_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = clerk_client.OrganizationsApi(clerk_client.ApiClient(configuration))
limit = 10  # float | Applies a limit to the number of results returned. Can be used for paginating the results together with `offset`. Must be an integer greater than zero and less than 500. By default, if not supplied, a limit of 10 is used. (optional) (default to 10)
offset = 0  # float | Skip the first `offset` results when paginating. Needs to be an integer greater or equal to zero. To be used in conjunction with `limit`. (optional) (default to 0)
include_members_count = true  # bool | Flag to denote whether the member counts of each organization should be included in the response or not. (optional)
query = 'query_example'  # str | Returns organizations with ID, name, or slug that match the given query. Uses exact match for organization ID and partial match for name and slug. (optional)
order_by = '-created_at'  # str | Allows to return organizations in a particular order. At the moment, you can order the returned organizations either by their `name`, `created_at` or `members_count`. In order to specify the direction, you can use the `+/-` symbols prepended in the property to order by. For example, if you want organizations to be returned in descending order according to their `created_at` property, you can use `-created_at`. If you don't use `+` or `-`, then `+` is implied. Defaults to `-created_at`. (optional) (default to -created_at)

try:
    # Get a list of organizations for an instance
    api_response = api_instance.list_organizations(limit=limit, offset=offset,
                                                   include_members_count=include_members_count, query=query,
                                                   order_by=order_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationsApi->list_organizations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **float**| Applies a limit to the number of results returned. Can be used for paginating the results together with &#x60;offset&#x60;. Must be an integer greater than zero and less than 500. By default, if not supplied, a limit of 10 is used. | [optional] [default to 10]
 **offset** | **float**| Skip the first &#x60;offset&#x60; results when paginating. Needs to be an integer greater or equal to zero. To be used in conjunction with &#x60;limit&#x60;. | [optional] [default to 0]
 **include_members_count** | **bool**| Flag to denote whether the member counts of each organization should be included in the response or not. | [optional] 
 **query** | **str**| Returns organizations with ID, name, or slug that match the given query. Uses exact match for organization ID and partial match for name and slug. | [optional] 
 **order_by** | **str**| Allows to return organizations in a particular order. At the moment, you can order the returned organizations either by their &#x60;name&#x60;, &#x60;created_at&#x60; or &#x60;members_count&#x60;. In order to specify the direction, you can use the &#x60;+/-&#x60; symbols prepended in the property to order by. For example, if you want organizations to be returned in descending order according to their &#x60;created_at&#x60; property, you can use &#x60;-created_at&#x60;. If you don&#x27;t use &#x60;+&#x60; or &#x60;-&#x60;, then &#x60;+&#x60; is implied. Defaults to &#x60;-created_at&#x60;. | [optional] [default to -created_at]

### Return type

[**Organizations**](Organizations.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **merge_organization_metadata**
> Organization merge_organization_metadata(body, organization_id)

Merge and update metadata for an organization

Update organization metadata attributes by merging existing values with the provided parameters. Metadata values will be updated via a deep merge. Deep meaning that any nested JSON objects will be merged as well. You can remove metadata keys at any level by setting their value to `null`.

### Example

```python
from __future__ import print_function
import time
import clerk_client
from clerk_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = clerk_client.OrganizationsApi(clerk_client.ApiClient(configuration))
body = clerk_client.OrganizationIdMetadataBody()  # OrganizationIdMetadataBody | 
organization_id = 'organization_id_example'  # str | The ID of the organization for which metadata will be merged or updated

try:
    # Merge and update metadata for an organization
    api_response = api_instance.merge_organization_metadata(body, organization_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationsApi->merge_organization_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**OrganizationIdMetadataBody**](OrganizationIdMetadataBody.md)|  | 
 **organization_id** | **str**| The ID of the organization for which metadata will be merged or updated | 

### Return type

[**Organization**](Organization.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_organization**
> Organization update_organization(body, organization_id)

Update an organization

Updates an existing organization

### Example

```python
from __future__ import print_function
import time
import clerk_client
from clerk_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = clerk_client.OrganizationsApi(clerk_client.ApiClient(configuration))
body = clerk_client.OrganizationsOrganizationIdBody()  # OrganizationsOrganizationIdBody | 
organization_id = 'organization_id_example'  # str | The ID of the organization to update

try:
    # Update an organization
    api_response = api_instance.update_organization(body, organization_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationsApi->update_organization: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**OrganizationsOrganizationIdBody**](OrganizationsOrganizationIdBody.md)|  | 
 **organization_id** | **str**| The ID of the organization to update | 

### Return type

[**Organization**](Organization.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_organization_logo**
> OrganizationWithLogo upload_organization_logo(organization_id, uploader_user_id=uploader_user_id, file=file)

Upload a logo for the organization

Set or replace an organization's logo, by uploading an image file. This endpoint uses the `multipart/form-data` request content type and accepts a file of image type. The file size cannot exceed 10MB. Only the following file content types are supported: `image/jpeg`, `image/png`, `image/gif`, `image/webp`, `image/x-icon`, `image/vnd.microsoft.icon`.

### Example

```python
from __future__ import print_function
import time
import clerk_client
from clerk_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = clerk_client.OrganizationsApi(clerk_client.ApiClient(configuration))
organization_id = 'organization_id_example'  # str | The ID of the organization for which to upload a logo
uploader_user_id = 'uploader_user_id_example'  # str |  (optional)
file = 'file_example'  # str |  (optional)

try:
    # Upload a logo for the organization
    api_response = api_instance.upload_organization_logo(organization_id, uploader_user_id=uploader_user_id, file=file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationsApi->upload_organization_logo: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| The ID of the organization for which to upload a logo | 
 **uploader_user_id** | **str**|  | [optional] 
 **file** | **str**|  | [optional] 

### Return type

[**OrganizationWithLogo**](OrganizationWithLogo.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

