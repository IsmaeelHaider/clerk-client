# OrganizationMembership

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**object** | **str** | String representing the object&#x27;s type. Objects of the same type share the same value.  | [optional] 
**role** | **str** |  | [optional] 
**permissions** | **list[str]** |  | [optional] 
**public_metadata** | **object** | Metadata saved on the organization membership, accessible from both Frontend and Backend APIs | [optional] 
**private_metadata** | **object** | Metadata saved on the organization membership, accessible only from the Backend API | [optional] 
**organization** | **AllOfOrganizationMembershipOrganization** |  | [optional] 
**public_user_data** | [**OrganizationMembershipPublicUserData**](OrganizationMembershipPublicUserData.md) |  | [optional] 
**created_at** | **int** | Unix timestamp of creation. | [optional] 
**updated_at** | **int** | Unix timestamp of last update. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

