# clerk_client.UsersApi

All URIs are relative to *https://api.clerk.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ban_user**](UsersApi.md#ban_user) | **POST** /users/{user_id}/ban | Ban a user
[**create_user**](UsersApi.md#create_user) | **POST** /users | Create a new user
[**delete_user**](UsersApi.md#delete_user) | **DELETE** /users/{user_id} | Delete a user
[**delete_user_profile_image**](UsersApi.md#delete_user_profile_image) | **DELETE** /users/{user_id}/profile_image | Delete user profile image
[**disable_mfa**](UsersApi.md#disable_mfa) | **DELETE** /users/{user_id}/mfa | Disable a user&#x27;s MFA methods
[**get_o_auth_access_token**](UsersApi.md#get_o_auth_access_token) | **GET** /users/{user_id}/oauth_access_tokens/{provider} | Retrieve the OAuth access token of a user
[**get_user**](UsersApi.md#get_user) | **GET** /users/{user_id} | Retrieve a user
[**get_user_list**](UsersApi.md#get_user_list) | **GET** /users | List all users
[**get_users_count**](UsersApi.md#get_users_count) | **GET** /users/count | Count users
[**lock_user**](UsersApi.md#lock_user) | **POST** /users/{user_id}/lock | Lock a user
[**set_user_profile_image**](UsersApi.md#set_user_profile_image) | **POST** /users/{user_id}/profile_image | Set user profile image
[**unban_user**](UsersApi.md#unban_user) | **POST** /users/{user_id}/unban | Unban a user
[**unlock_user**](UsersApi.md#unlock_user) | **POST** /users/{user_id}/unlock | Unlock a user
[**update_user**](UsersApi.md#update_user) | **PATCH** /users/{user_id} | Update a user
[**update_user_metadata**](UsersApi.md#update_user_metadata) | **PATCH** /users/{user_id}/metadata | Merge and update a user&#x27;s metadata
[**users_get_organization_memberships**](UsersApi.md#users_get_organization_memberships) | **GET** /users/{user_id}/organization_memberships | Retrieve all memberships for a user
[**verify_password**](UsersApi.md#verify_password) | **POST** /users/{user_id}/verify_password | Verify the password of a user
[**verify_totp**](UsersApi.md#verify_totp) | **POST** /users/{user_id}/verify_totp | Verify a TOTP or backup code for a user

# **ban_user**
> User ban_user(user_id)

Ban a user

Marks the given user as banned, which means that all their sessions are revoked and they are not allowed to sign in again.

### Example

```python
from __future__ import print_function
import time
import clerk_client
from clerk_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = clerk_client.UsersApi(clerk_client.ApiClient(configuration))
user_id = 'user_id_example'  # str | The ID of the user to ban

try:
    # Ban a user
    api_response = api_instance.ban_user(user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->ban_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The ID of the user to ban | 

### Return type

[**User**](User.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_user**
> User create_user(body)

Create a new user

Creates a new user. Your user management settings determine how you should setup your user model.  Any email address and phone number created using this method will be marked as verified.  Note: If you are performing a migration, check out our guide on [zero downtime migrations](https://clerk.com/docs/deployments/migrate-overview).  A rate limit rule of 20 requests per 10 seconds is applied to this endpoint.

### Example

```python
from __future__ import print_function
import time
import clerk_client
from clerk_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = clerk_client.UsersApi(clerk_client.ApiClient(configuration))
body = clerk_client.UsersBody()  # UsersBody | 

try:
    # Create a new user
    api_response = api_instance.create_user(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->create_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UsersBody**](UsersBody.md)|  | 

### Return type

[**User**](User.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_user**
> DeletedObject delete_user(user_id)

Delete a user

Delete the specified user

### Example

```python
from __future__ import print_function
import time
import clerk_client
from clerk_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = clerk_client.UsersApi(clerk_client.ApiClient(configuration))
user_id = 'user_id_example'  # str | The ID of the user to delete

try:
    # Delete a user
    api_response = api_instance.delete_user(user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->delete_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The ID of the user to delete | 

### Return type

[**DeletedObject**](DeletedObject.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_user_profile_image**
> User delete_user_profile_image(user_id)

Delete user profile image

Delete a user's profile image

### Example

```python
from __future__ import print_function
import time
import clerk_client
from clerk_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = clerk_client.UsersApi(clerk_client.ApiClient(configuration))
user_id = 'user_id_example'  # str | The ID of the user to delete the profile image for

try:
    # Delete user profile image
    api_response = api_instance.delete_user_profile_image(user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->delete_user_profile_image: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The ID of the user to delete the profile image for | 

### Return type

[**User**](User.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **disable_mfa**
> InlineResponse2004 disable_mfa(user_id)

Disable a user's MFA methods

Disable all of a user's MFA methods (e.g. OTP sent via SMS, TOTP on their authenticator app) at once.

### Example

```python
from __future__ import print_function
import time
import clerk_client
from clerk_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = clerk_client.UsersApi(clerk_client.ApiClient(configuration))
user_id = 'user_id_example'  # str | The ID of the user whose MFA methods are to be disabled

try:
    # Disable a user's MFA methods
    api_response = api_instance.disable_mfa(user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->disable_mfa: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The ID of the user whose MFA methods are to be disabled | 

### Return type

[**InlineResponse2004**](InlineResponse2004.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_o_auth_access_token**
> list[InlineResponse2001] get_o_auth_access_token(user_id, provider)

Retrieve the OAuth access token of a user

Fetch the corresponding OAuth access token for a user that has previously authenticated with a particular OAuth provider. For OAuth 2.0, if the access token has expired and we have a corresponding refresh token, the access token will be refreshed transparently the new one will be returned.

### Example

```python
from __future__ import print_function
import time
import clerk_client
from clerk_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = clerk_client.UsersApi(clerk_client.ApiClient(configuration))
user_id = 'user_id_example'  # str | The ID of the user for which to retrieve the OAuth access token
provider = 'provider_example'  # str | The ID of the OAuth provider (e.g. `oauth_google`)

try:
    # Retrieve the OAuth access token of a user
    api_response = api_instance.get_o_auth_access_token(user_id, provider)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->get_o_auth_access_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The ID of the user for which to retrieve the OAuth access token | 
 **provider** | **str**| The ID of the OAuth provider (e.g. &#x60;oauth_google&#x60;) | 

### Return type

[**list[InlineResponse2001]**](InlineResponse2001.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user**
> User get_user(user_id)

Retrieve a user

Retrieve the details of a user

### Example

```python
from __future__ import print_function
import time
import clerk_client
from clerk_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = clerk_client.UsersApi(clerk_client.ApiClient(configuration))
user_id = 'user_id_example'  # str | The ID of the user to retrieve

try:
    # Retrieve a user
    api_response = api_instance.get_user(user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->get_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The ID of the user to retrieve | 

### Return type

[**User**](User.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_list**
> list[User] get_user_list(email_address=email_address, phone_number=phone_number, external_id=external_id, username=username, web3_wallet=web3_wallet, user_id=user_id, organization_id=organization_id, query=query, last_active_at_since=last_active_at_since, limit=limit, offset=offset, order_by=order_by)

List all users

Returns a list of all users. The users are returned sorted by creation date, with the newest users appearing first.

### Example

```python
from __future__ import print_function
import time
import clerk_client
from clerk_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = clerk_client.UsersApi(clerk_client.ApiClient(configuration))
email_address = [
    'email_address_example']  # list[str] | Returns users with the specified email addresses. Accepts up to 100 email addresses. Any email addresses not found are ignored. (optional)
phone_number = [
    'phone_number_example']  # list[str] | Returns users with the specified phone numbers. Accepts up to 100 phone numbers. Any phone numbers not found are ignored. (optional)
external_id = [
    'external_id_example']  # list[str] | Returns users with the specified external ids. For each external id, the `+` and `-` can be prepended to the id, which denote whether the respective external id should be included or excluded from the result set. Accepts up to 100 external ids. Any external ids not found are ignored. (optional)
username = [
    'username_example']  # list[str] | Returns users with the specified usernames. Accepts up to 100 usernames. Any usernames not found are ignored. (optional)
web3_wallet = [
    'web3_wallet_example']  # list[str] | Returns users with the specified web3 wallet addresses. Accepts up to 100 web3 wallet addresses. Any web3 wallet addressed not found are ignored. (optional)
user_id = [
    'user_id_example']  # list[str] | Returns users with the user ids specified. For each user id, the `+` and `-` can be prepended to the id, which denote whether the respective user id should be included or excluded from the result set. Accepts up to 100 user ids. Any user ids not found are ignored. (optional)
organization_id = [
    'organization_id_example']  # list[str] | Returns users that have memberships to the given organizations. For each organization id, the `+` and `-` can be prepended to the id, which denote whether the respective organization should be included or excluded from the result set. Accepts up to 100 organization ids. (optional)
query = 'query_example'  # str | Returns users that match the given query. For possible matches, we check the email addresses, phone numbers, usernames, web3 wallets, user ids, first and last names. The query value doesn't need to match the exact value you are looking for, it is capable of partial matches as well. (optional)
last_active_at_since = 56  # int | Returns users that had session activity since the given date, with day precision. Providing a value with higher precision than day will result in an error. Example: use 1700690400000 to retrieve users that had session activity from 2023-11-23 until the current day. (optional)
limit = 10  # float | Applies a limit to the number of results returned. Can be used for paginating the results together with `offset`. Must be an integer greater than zero and less than 500. By default, if not supplied, a limit of 10 is used. (optional) (default to 10)
offset = 0  # float | Skip the first `offset` results when paginating. Needs to be an integer greater or equal to zero. To be used in conjunction with `limit`. (optional) (default to 0)
order_by = '-created_at'  # str | Allows to return users in a particular order. At the moment, you can order the returned users by their `created_at`,`updated_at`,`email_address`,`web3wallet`,`first_name`,`last_name`,`phone_number`,`username`,`last_active_at`,`last_sign_in_at`. In order to specify the direction, you can use the `+/-` symbols prepended in the property to order by. For example, if you want users to be returned in descending order according to their `created_at` property, you can use `-created_at`. If you don't use `+` or `-`, then `+` is implied. We only support one `order_by` parameter, and if multiple `order_by` parameters are provided, we will only keep the first one. For example, if you pass `order_by=username&order_by=created_at`, we will consider only the first `order_by` parameter, which is `username`. The `created_at` parameter will be ignored in this case. (optional) (default to -created_at)

try:
    # List all users
    api_response = api_instance.get_user_list(email_address=email_address, phone_number=phone_number,
                                              external_id=external_id, username=username, web3_wallet=web3_wallet,
                                              user_id=user_id, organization_id=organization_id, query=query,
                                              last_active_at_since=last_active_at_since, limit=limit, offset=offset,
                                              order_by=order_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->get_user_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email_address** | [**list[str]**](str.md)| Returns users with the specified email addresses. Accepts up to 100 email addresses. Any email addresses not found are ignored. | [optional] 
 **phone_number** | [**list[str]**](str.md)| Returns users with the specified phone numbers. Accepts up to 100 phone numbers. Any phone numbers not found are ignored. | [optional] 
 **external_id** | [**list[str]**](str.md)| Returns users with the specified external ids. For each external id, the &#x60;+&#x60; and &#x60;-&#x60; can be prepended to the id, which denote whether the respective external id should be included or excluded from the result set. Accepts up to 100 external ids. Any external ids not found are ignored. | [optional] 
 **username** | [**list[str]**](str.md)| Returns users with the specified usernames. Accepts up to 100 usernames. Any usernames not found are ignored. | [optional] 
 **web3_wallet** | [**list[str]**](str.md)| Returns users with the specified web3 wallet addresses. Accepts up to 100 web3 wallet addresses. Any web3 wallet addressed not found are ignored. | [optional] 
 **user_id** | [**list[str]**](str.md)| Returns users with the user ids specified. For each user id, the &#x60;+&#x60; and &#x60;-&#x60; can be prepended to the id, which denote whether the respective user id should be included or excluded from the result set. Accepts up to 100 user ids. Any user ids not found are ignored. | [optional] 
 **organization_id** | [**list[str]**](str.md)| Returns users that have memberships to the given organizations. For each organization id, the &#x60;+&#x60; and &#x60;-&#x60; can be prepended to the id, which denote whether the respective organization should be included or excluded from the result set. Accepts up to 100 organization ids. | [optional] 
 **query** | **str**| Returns users that match the given query. For possible matches, we check the email addresses, phone numbers, usernames, web3 wallets, user ids, first and last names. The query value doesn&#x27;t need to match the exact value you are looking for, it is capable of partial matches as well. | [optional] 
 **last_active_at_since** | **int**| Returns users that had session activity since the given date, with day precision. Providing a value with higher precision than day will result in an error. Example: use 1700690400000 to retrieve users that had session activity from 2023-11-23 until the current day. | [optional] 
 **limit** | **float**| Applies a limit to the number of results returned. Can be used for paginating the results together with &#x60;offset&#x60;. Must be an integer greater than zero and less than 500. By default, if not supplied, a limit of 10 is used. | [optional] [default to 10]
 **offset** | **float**| Skip the first &#x60;offset&#x60; results when paginating. Needs to be an integer greater or equal to zero. To be used in conjunction with &#x60;limit&#x60;. | [optional] [default to 0]
 **order_by** | **str**| Allows to return users in a particular order. At the moment, you can order the returned users by their &#x60;created_at&#x60;,&#x60;updated_at&#x60;,&#x60;email_address&#x60;,&#x60;web3wallet&#x60;,&#x60;first_name&#x60;,&#x60;last_name&#x60;,&#x60;phone_number&#x60;,&#x60;username&#x60;,&#x60;last_active_at&#x60;,&#x60;last_sign_in_at&#x60;. In order to specify the direction, you can use the &#x60;+/-&#x60; symbols prepended in the property to order by. For example, if you want users to be returned in descending order according to their &#x60;created_at&#x60; property, you can use &#x60;-created_at&#x60;. If you don&#x27;t use &#x60;+&#x60; or &#x60;-&#x60;, then &#x60;+&#x60; is implied. We only support one &#x60;order_by&#x60; parameter, and if multiple &#x60;order_by&#x60; parameters are provided, we will only keep the first one. For example, if you pass &#x60;order_by&#x3D;username&amp;order_by&#x3D;created_at&#x60;, we will consider only the first &#x60;order_by&#x60; parameter, which is &#x60;username&#x60;. The &#x60;created_at&#x60; parameter will be ignored in this case. | [optional] [default to -created_at]

### Return type

[**list[User]**](User.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_users_count**
> TotalCount get_users_count(email_address=email_address, phone_number=phone_number, external_id=external_id, username=username, web3_wallet=web3_wallet, user_id=user_id, query=query)

Count users

Returns a total count of all users that match the given filtering criteria.

### Example

```python
from __future__ import print_function
import time
import clerk_client
from clerk_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = clerk_client.UsersApi(clerk_client.ApiClient(configuration))
email_address = [
    'email_address_example']  # list[str] | Counts users with the specified email addresses. Accepts up to 100 email addresses. Any email addresses not found are ignored. (optional)
phone_number = [
    'phone_number_example']  # list[str] | Counts users with the specified phone numbers. Accepts up to 100 phone numbers. Any phone numbers not found are ignored. (optional)
external_id = [
    'external_id_example']  # list[str] | Counts users with the specified external ids. Accepts up to 100 external ids. Any external ids not found are ignored. (optional)
username = [
    'username_example']  # list[str] | Counts users with the specified usernames. Accepts up to 100 usernames. Any usernames not found are ignored. (optional)
web3_wallet = [
    'web3_wallet_example']  # list[str] | Counts users with the specified web3 wallet addresses. Accepts up to 100 web3 wallet addresses. Any web3 wallet addressed not found are ignored. (optional)
user_id = [
    'user_id_example']  # list[str] | Counts users with the user ids specified. Accepts up to 100 user ids. Any user ids not found are ignored. (optional)
query = 'query_example'  # str | Counts users that match the given query. For possible matches, we check the email addresses, phone numbers, usernames, web3 wallets, user ids, first and last names. The query value doesn't need to match the exact value you are looking for, it is capable of partial matches as well. (optional)

try:
    # Count users
    api_response = api_instance.get_users_count(email_address=email_address, phone_number=phone_number,
                                                external_id=external_id, username=username, web3_wallet=web3_wallet,
                                                user_id=user_id, query=query)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->get_users_count: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email_address** | [**list[str]**](str.md)| Counts users with the specified email addresses. Accepts up to 100 email addresses. Any email addresses not found are ignored. | [optional] 
 **phone_number** | [**list[str]**](str.md)| Counts users with the specified phone numbers. Accepts up to 100 phone numbers. Any phone numbers not found are ignored. | [optional] 
 **external_id** | [**list[str]**](str.md)| Counts users with the specified external ids. Accepts up to 100 external ids. Any external ids not found are ignored. | [optional] 
 **username** | [**list[str]**](str.md)| Counts users with the specified usernames. Accepts up to 100 usernames. Any usernames not found are ignored. | [optional] 
 **web3_wallet** | [**list[str]**](str.md)| Counts users with the specified web3 wallet addresses. Accepts up to 100 web3 wallet addresses. Any web3 wallet addressed not found are ignored. | [optional] 
 **user_id** | [**list[str]**](str.md)| Counts users with the user ids specified. Accepts up to 100 user ids. Any user ids not found are ignored. | [optional] 
 **query** | **str**| Counts users that match the given query. For possible matches, we check the email addresses, phone numbers, usernames, web3 wallets, user ids, first and last names. The query value doesn&#x27;t need to match the exact value you are looking for, it is capable of partial matches as well. | [optional] 

### Return type

[**TotalCount**](TotalCount.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **lock_user**
> User lock_user(user_id)

Lock a user

Marks the given user as locked, which means they are not allowed to sign in again until the lock expires. Lock duration can be configured in the instance's restrictions settings.

### Example

```python
from __future__ import print_function
import time
import clerk_client
from clerk_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = clerk_client.UsersApi(clerk_client.ApiClient(configuration))
user_id = 'user_id_example'  # str | The ID of the user to lock

try:
    # Lock a user
    api_response = api_instance.lock_user(user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->lock_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The ID of the user to lock | 

### Return type

[**User**](User.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_user_profile_image**
> User set_user_profile_image(file, user_id)

Set user profile image

Update a user's profile image

### Example

```python
from __future__ import print_function
import time
import clerk_client
from clerk_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = clerk_client.UsersApi(clerk_client.ApiClient(configuration))
file = 'file_example'  # str | 
user_id = 'user_id_example'  # str | The ID of the user to update the profile image for

try:
    # Set user profile image
    api_response = api_instance.set_user_profile_image(file, user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->set_user_profile_image: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **str**|  | 
 **user_id** | **str**| The ID of the user to update the profile image for | 

### Return type

[**User**](User.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unban_user**
> User unban_user(user_id)

Unban a user

Removes the ban mark from the given user.

### Example

```python
from __future__ import print_function
import time
import clerk_client
from clerk_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = clerk_client.UsersApi(clerk_client.ApiClient(configuration))
user_id = 'user_id_example'  # str | The ID of the user to unban

try:
    # Unban a user
    api_response = api_instance.unban_user(user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->unban_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The ID of the user to unban | 

### Return type

[**User**](User.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unlock_user**
> User unlock_user(user_id)

Unlock a user

Removes the lock from the given user.

### Example

```python
from __future__ import print_function
import time
import clerk_client
from clerk_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = clerk_client.UsersApi(clerk_client.ApiClient(configuration))
user_id = 'user_id_example'  # str | The ID of the user to unlock

try:
    # Unlock a user
    api_response = api_instance.unlock_user(user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->unlock_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The ID of the user to unlock | 

### Return type

[**User**](User.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_user**
> User update_user(body, user_id)

Update a user

Update a user's attributes.  You can set the user's primary contact identifiers (email address and phone numbers) by updating the `primary_email_address_id` and `primary_phone_number_id` attributes respectively. Both IDs should correspond to verified identifications that belong to the user.  You can remove a user's username by setting the username attribute to null or the blank string \"\". This is a destructive action; the identification will be deleted forever. Usernames can be removed only if they are optional in your instance settings and there's at least one other identifier which can be used for authentication.  This endpoint allows changing a user's password. When passing the `password` parameter directly you have two further options. You can ignore the password policy checks for your instance by setting the `skip_password_checks` parameter to `true`. You can also choose to sign the user out of all their active sessions on any device once the password is updated. Just set `sign_out_of_other_sessions` to `true`.

### Example

```python
from __future__ import print_function
import time
import clerk_client
from clerk_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = clerk_client.UsersApi(clerk_client.ApiClient(configuration))
body = clerk_client.UsersUserIdBody()  # UsersUserIdBody | 
user_id = 'user_id_example'  # str | The ID of the user to update

try:
    # Update a user
    api_response = api_instance.update_user(body, user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->update_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UsersUserIdBody**](UsersUserIdBody.md)|  | 
 **user_id** | **str**| The ID of the user to update | 

### Return type

[**User**](User.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_user_metadata**
> User update_user_metadata(user_id, body=body)

Merge and update a user's metadata

Update a user's metadata attributes by merging existing values with the provided parameters.  This endpoint behaves differently than the *Update a user* endpoint. Metadata values will not be replaced entirely. Instead, a deep merge will be performed. Deep means that any nested JSON objects will be merged as well.  You can remove metadata keys at any level by setting their value to `null`.

### Example

```python
from __future__ import print_function
import time
import clerk_client
from clerk_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = clerk_client.UsersApi(clerk_client.ApiClient(configuration))
user_id = 'user_id_example'  # str | The ID of the user whose metadata will be updated and merged
body = clerk_client.UserIdMetadataBody()  # UserIdMetadataBody |  (optional)

try:
    # Merge and update a user's metadata
    api_response = api_instance.update_user_metadata(user_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->update_user_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The ID of the user whose metadata will be updated and merged | 
 **body** | [**UserIdMetadataBody**](UserIdMetadataBody.md)|  | [optional] 

### Return type

[**User**](User.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_get_organization_memberships**
> OrganizationMemberships users_get_organization_memberships(user_id, limit=limit, offset=offset)

Retrieve all memberships for a user

Retrieve a paginated list of the user's organization memberships

### Example

```python
from __future__ import print_function
import time
import clerk_client
from clerk_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = clerk_client.UsersApi(clerk_client.ApiClient(configuration))
user_id = 'user_id_example'  # str | The ID of the user whose organization memberships we want to retrieve
limit = 10  # float | Applies a limit to the number of results returned. Can be used for paginating the results together with `offset`. Must be an integer greater than zero and less than 500. By default, if not supplied, a limit of 10 is used. (optional) (default to 10)
offset = 0  # float | Skip the first `offset` results when paginating. Needs to be an integer greater or equal to zero. To be used in conjunction with `limit`. (optional) (default to 0)

try:
    # Retrieve all memberships for a user
    api_response = api_instance.users_get_organization_memberships(user_id, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->users_get_organization_memberships: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The ID of the user whose organization memberships we want to retrieve | 
 **limit** | **float**| Applies a limit to the number of results returned. Can be used for paginating the results together with &#x60;offset&#x60;. Must be an integer greater than zero and less than 500. By default, if not supplied, a limit of 10 is used. | [optional] [default to 10]
 **offset** | **float**| Skip the first &#x60;offset&#x60; results when paginating. Needs to be an integer greater or equal to zero. To be used in conjunction with &#x60;limit&#x60;. | [optional] [default to 0]

### Return type

[**OrganizationMemberships**](OrganizationMemberships.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **verify_password**
> InlineResponse2002 verify_password(user_id, body=body)

Verify the password of a user

Check that the user's password matches the supplied input. Useful for custom auth flows and re-verification.

### Example

```python
from __future__ import print_function
import time
import clerk_client
from clerk_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = clerk_client.UsersApi(clerk_client.ApiClient(configuration))
user_id = 'user_id_example'  # str | The ID of the user for whom to verify the password
body = clerk_client.UserIdVerifyPasswordBody()  # UserIdVerifyPasswordBody |  (optional)

try:
    # Verify the password of a user
    api_response = api_instance.verify_password(user_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->verify_password: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The ID of the user for whom to verify the password | 
 **body** | [**UserIdVerifyPasswordBody**](UserIdVerifyPasswordBody.md)|  | [optional] 

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **verify_totp**
> InlineResponse2003 verify_totp(user_id, body=body)

Verify a TOTP or backup code for a user

Verify that the provided TOTP or backup code is valid for the user. Verifying a backup code will result it in being consumed (i.e. it will become invalid). Useful for custom auth flows and re-verification.

### Example

```python
from __future__ import print_function
import time
import clerk_client
from clerk_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = clerk_client.UsersApi(clerk_client.ApiClient(configuration))
user_id = 'user_id_example'  # str | The ID of the user for whom to verify the TOTP
body = clerk_client.UserIdVerifyTotpBody()  # UserIdVerifyTotpBody |  (optional)

try:
    # Verify a TOTP or backup code for a user
    api_response = api_instance.verify_totp(user_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->verify_totp: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The ID of the user for whom to verify the TOTP | 
 **body** | [**UserIdVerifyTotpBody**](UserIdVerifyTotpBody.md)|  | [optional] 

### Return type

[**InlineResponse2003**](InlineResponse2003.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

