# InvitationsBody

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email_address** | **str** | The email address the invitation will be sent to | 
**public_metadata** | **object** | Metadata that will be attached to the newly created invitation. The value of this property should be a well-formed JSON object. Once the user accepts the invitation and signs up, these metadata will end up in the user&#x27;s public metadata. | [optional] 
**redirect_url** | **str** | Optional URL which specifies where to redirect the user once they click the invitation link. This is only required if you have implemented a [custom flow](https://clerk.com/docs/authentication/invitations#custom-flow) and you&#x27;re not using Clerk Hosted Pages or Clerk Components. | [optional] 
**notify** | **bool** | Optional flag which denotes whether an email invitation should be sent to the given email address. Defaults to true. | [optional] [default to True]
**ignore_existing** | **bool** | Whether an invitation should be created if there is already an existing invitation for this email address, or it&#x27;s claimed by another user. | [optional] [default to False]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

