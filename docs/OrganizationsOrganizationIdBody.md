# OrganizationsOrganizationIdBody

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**public_metadata** | **object** | Metadata saved on the organization, that is visible to both your frontend and backend. | [optional] 
**private_metadata** | **object** | Metadata saved on the organization that is only visible to your backend. | [optional] 
**name** | **str** | The new name of the organization | [optional] 
**slug** | **str** | The new slug of the organization, which needs to be unique in the instance | [optional] 
**max_allowed_memberships** | **int** | The maximum number of memberships allowed for this organization | [optional] 
**admin_delete_enabled** | **bool** | If true, an admin can delete this organization with the Frontend API. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

