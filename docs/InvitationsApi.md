# clerk_client.InvitationsApi

All URIs are relative to *https://api.clerk.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_invitation**](InvitationsApi.md#create_invitation) | **POST** /invitations | Create an invitation
[**list_invitations**](InvitationsApi.md#list_invitations) | **GET** /invitations | List all invitations
[**revoke_invitation**](InvitationsApi.md#revoke_invitation) | **POST** /invitations/{invitation_id}/revoke | Revokes an invitation

# **create_invitation**
> Invitation create_invitation(body=body)

Create an invitation

Creates a new invitation for the given email address and sends the invitation email. Keep in mind that you cannot create an invitation if there is already one for the given email address. Also, trying to create an invitation for an email address that already exists in your application will result to an error.

### Example

```python
from __future__ import print_function
import time
import clerk_client
from clerk_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = clerk_client.InvitationsApi(clerk_client.ApiClient(configuration))
body = clerk_client.InvitationsBody()  # InvitationsBody | Required parameters (optional)

try:
    # Create an invitation
    api_response = api_instance.create_invitation(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvitationsApi->create_invitation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**InvitationsBody**](InvitationsBody.md)| Required parameters | [optional] 

### Return type

[**Invitation**](Invitation.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_invitations**
> list[Invitation] list_invitations(limit=limit, offset=offset, status=status)

List all invitations

Returns all non-revoked invitations for your application, sorted by creation date

### Example

```python
from __future__ import print_function
import time
import clerk_client
from clerk_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = clerk_client.InvitationsApi(clerk_client.ApiClient(configuration))
limit = 10  # float | Applies a limit to the number of results returned. Can be used for paginating the results together with `offset`. Must be an integer greater than zero and less than 500. By default, if not supplied, a limit of 10 is used. (optional) (default to 10)
offset = 0  # float | Skip the first `offset` results when paginating. Needs to be an integer greater or equal to zero. To be used in conjunction with `limit`. (optional) (default to 0)
status = 'status_example'  # str | Filter invitations based on their status (optional)

try:
    # List all invitations
    api_response = api_instance.list_invitations(limit=limit, offset=offset, status=status)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvitationsApi->list_invitations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **float**| Applies a limit to the number of results returned. Can be used for paginating the results together with &#x60;offset&#x60;. Must be an integer greater than zero and less than 500. By default, if not supplied, a limit of 10 is used. | [optional] [default to 10]
 **offset** | **float**| Skip the first &#x60;offset&#x60; results when paginating. Needs to be an integer greater or equal to zero. To be used in conjunction with &#x60;limit&#x60;. | [optional] [default to 0]
 **status** | **str**| Filter invitations based on their status | [optional] 

### Return type

[**list[Invitation]**](Invitation.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **revoke_invitation**
> InlineResponse2005 revoke_invitation(invitation_id)

Revokes an invitation

Revokes the given invitation. Revoking an invitation will prevent the user from using the invitation link that was sent to them. However, it doesn't prevent the user from signing up if they follow the sign up flow. Only active (i.e. non-revoked) invitations can be revoked.

### Example

```python
from __future__ import print_function
import time
import clerk_client
from clerk_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = clerk_client.InvitationsApi(clerk_client.ApiClient(configuration))
invitation_id = 'invitation_id_example'  # str | The ID of the invitation to be revoked

try:
    # Revokes an invitation
    api_response = api_instance.revoke_invitation(invitation_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvitationsApi->revoke_invitation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invitation_id** | **str**| The ID of the invitation to be revoked | 

### Return type

[**InlineResponse2005**](InlineResponse2005.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

