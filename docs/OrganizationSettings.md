# OrganizationSettings

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** | String representing the object&#x27;s type. Objects of the same type share the same value. | 
**enabled** | **bool** |  | 
**max_allowed_memberships** | **int** |  | 
**max_allowed_roles** | **int** |  | [optional] 
**max_allowed_permissions** | **int** |  | [optional] 
**creator_role** | **str** | The role key that a user will be assigned after creating an organization. | 
**admin_delete_enabled** | **bool** | The default for whether an admin can delete an organization with the Frontend API. | 
**domains_enabled** | **bool** |  | 
**domains_enrollment_modes** | **list[str]** |  | 
**domains_default_role** | **str** | The role key that it will be used in order to create an organization invitation or suggestion. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

