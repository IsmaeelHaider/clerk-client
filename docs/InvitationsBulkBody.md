# InvitationsBulkBody

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email_address** | **str** | The email address of the new member that is going to be invited to the organization | 
**inviter_user_id** | **str** | The ID of the user that invites the new member to the organization. Must be an administrator in the organization. | 
**role** | **str** | The role of the new member in the organization. | 
**public_metadata** | **object** | Metadata saved on the organization invitation, read-only from the Frontend API and fully accessible (read/write) from the Backend API. | [optional] 
**private_metadata** | **object** | Metadata saved on the organization invitation, fully accessible (read/write) from the Backend API but not visible from the Frontend API. | [optional] 
**redirect_url** | **str** | Optional URL that the invitee will be redirected to once they accept the invitation by clicking the join link in the invitation email. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

