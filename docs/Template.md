# Template

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**object** | **str** | String representing the object&#x27;s type. Objects of the same type share the same value.  | [optional] 
**instance_id** | **str** | the id of the instance the template belongs to | [optional] 
**resource_type** | **str** | whether this is a system (default) or user overridden) template | [optional] 
**template_type** | **str** | whether this is an email or SMS template | [optional] 
**name** | **str** | user-friendly name of the template | [optional] 
**slug** | **str** | machine-friendly name of the template | [optional] 
**position** | **int** | position with the listing of templates | [optional] 
**can_revert** | **bool** | whether this template can be reverted to the corresponding system default | [optional] 
**can_delete** | **bool** | whether this template can be deleted | [optional] 
**subject** | **str** | email subject | [optional] 
**markup** | **str** | the editor markup used to generate the body of the template | [optional] 
**body** | **str** | the template body before variable interpolation | [optional] 
**available_variables** | **list[str]** | list of variables that are available for use in the template body | [optional] 
**required_variables** | **list[str]** | list of variables that must be contained in the template body | [optional] 
**from_email_name** | **str** |  | [optional] 
**delivered_by_clerk** | **bool** |  | [optional] 
**updated_at** | **int** | Unix timestamp of last update.  | [optional] 
**created_at** | **int** | Unix timestamp of creation.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

