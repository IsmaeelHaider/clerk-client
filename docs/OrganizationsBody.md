# OrganizationsBody

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the new organization | 
**created_by** | **str** | The ID of the User who will become the administrator for the new organization | 
**private_metadata** | **object** | Metadata saved on the organization, accessible only from the Backend API | [optional] 
**public_metadata** | **object** | Metadata saved on the organization, read-only from the Frontend API and fully accessible (read/write) from the Backend API | [optional] 
**slug** | **str** | A slug for the new organization. Can contain only lowercase alphanumeric characters and the dash \&quot;-\&quot;. Must be unique for the instance. | [optional] 
**max_allowed_memberships** | **int** | The maximum number of memberships allowed for this organization | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

