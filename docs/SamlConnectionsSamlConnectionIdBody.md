# SamlConnectionsSamlConnectionIdBody

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the new SAML Connection | [optional] 
**domain** | **str** | The domain to use for the new SAML Connection | [optional] 
**idp_entity_id** | **str** | The entity id as provided by the IdP | [optional] 
**idp_sso_url** | **str** | The SSO url as provided by the IdP | [optional] 
**idp_certificate** | **str** | The x509 certificated as provided by the IdP | [optional] 
**idp_metadata_url** | **str** | The URL which serves the IdP metadata. If present, it takes priority over the corresponding individual properties and replaces them | [optional] 
**attribute_mapping** | [**SamlConnectionssamlConnectionIdAttributeMapping**](SamlConnectionssamlConnectionIdAttributeMapping.md) |  | [optional] 
**active** | **bool** | Activate or de-activate the SAML Connection | [optional] 
**sync_user_attributes** | **bool** | Controls whether to update the user&#x27;s attributes in each sign-in | [optional] 
**allow_subdomains** | **bool** | Allow users with an email address subdomain to use this connection in order to authenticate | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

