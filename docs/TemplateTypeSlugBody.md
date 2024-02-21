# TemplateTypeSlugBody

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The user-friendly name of the template | [optional] 
**subject** | **str** | The email subject. Applicable only to email templates. | [optional] 
**markup** | **str** | The editor markup used to generate the body of the template | [optional] 
**body** | **str** | The template body before variable interpolation | [optional] 
**delivered_by_clerk** | **bool** | Whether Clerk should deliver emails or SMS messages based on the current template | [optional] 
**from_email_name** | **str** | The local part of the From email address that will be used for emails. For example, in the address &#x27;hello@example.com&#x27;, the local part is &#x27;hello&#x27;. Applicable only to email templates. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

