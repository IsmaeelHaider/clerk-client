# JwtTemplatesBody

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | JWT template name | [optional] 
**claims** | **object** | JWT template claims in JSON format | [optional] 
**lifetime** | **float** | JWT token lifetime | [optional] 
**allowed_clock_skew** | **float** | JWT token allowed clock skew | [optional] 
**custom_signing_key** | **bool** | Whether a custom signing key/algorithm is also provided for this template | [optional] 
**signing_algorithm** | **str** | The custom signing algorithm to use when minting JWTs | [optional] 
**signing_key** | **str** | The custom signing private key to use when minting JWTs | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

