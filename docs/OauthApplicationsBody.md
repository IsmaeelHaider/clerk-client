# OauthApplicationsBody

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the new OAuth application | 
**callback_url** | **str** | The callback URL of the new OAuth application | 
**scopes** | **str** | Define the allowed scopes for the new OAuth applications that dictate the user payload of the OAuth user info endpoint. Available scopes are &#x60;profile&#x60;, &#x60;email&#x60;, &#x60;public_metadata&#x60;, &#x60;private_metadata&#x60;. Provide the requested scopes as a string, separated by spaces. | [optional] [default to 'profile email']
**public** | **bool** | If true, this client is public and cannot securely store a client secret. Only the authorization code flow with proof key for code exchange (PKCE) may be used. Public clients cannot be updated to be confidential clients, and vice versa. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

