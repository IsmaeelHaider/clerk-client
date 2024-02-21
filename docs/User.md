# User

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**object** | **str** | String representing the object&#x27;s type. Objects of the same type share the same value.  | [optional] 
**external_id** | **str** |  | [optional] 
**primary_email_address_id** | **str** |  | [optional] 
**primary_phone_number_id** | **str** |  | [optional] 
**primary_web3_wallet_id** | **str** |  | [optional] 
**username** | **str** |  | [optional] 
**first_name** | **str** |  | [optional] 
**last_name** | **str** |  | [optional] 
**profile_image_url** | **str** |  | [optional] 
**image_url** | **str** |  | [optional] 
**has_image** | **bool** |  | [optional] 
**public_metadata** | **object** |  | [optional] 
**private_metadata** | **object** |  | [optional] 
**unsafe_metadata** | **object** |  | [optional] 
**email_addresses** | [**list[EmailAddress]**](EmailAddress.md) |  | [optional] 
**phone_numbers** | [**list[PhoneNumber]**](PhoneNumber.md) |  | [optional] 
**web3_wallets** | [**list[Web3Wallet]**](Web3Wallet.md) |  | [optional] 
**password_enabled** | **bool** |  | [optional] 
**two_factor_enabled** | **bool** |  | [optional] 
**totp_enabled** | **bool** |  | [optional] 
**backup_code_enabled** | **bool** |  | [optional] 
**external_accounts** | **list[object]** |  | [optional] 
**saml_accounts** | [**list[SAMLAccount]**](SAMLAccount.md) |  | [optional] 
**last_sign_in_at** | **int** | Unix timestamp of last sign-in.  | [optional] 
**banned** | **bool** | Flag to denote whether user is banned or not.  | [optional] 
**locked** | **bool** | Flag to denote whether user is currently locked, i.e. restricted from signing in or not.  | [optional] 
**lockout_expires_in_seconds** | **int** | The number of seconds remaining until the lockout period expires for a locked user. A null value for a locked user indicates that lockout never expires.  | [optional] 
**verification_attempts_remaining** | **int** | The number of verification attempts remaining until the user is locked. Null if account lockout is not enabled. Note: if a user is locked explicitly via the Backend API, they may still have verification attempts remaining.  | [optional] 
**updated_at** | **int** | Unix timestamp of last update.  | [optional] 
**created_at** | **int** | Unix timestamp of creation.  | [optional] 
**delete_self_enabled** | **bool** | If enabled, user can delete themselves via FAPI.  | [optional] 
**create_organization_enabled** | **bool** | If enabled, user can create organizations via FAPI.  | [optional] 
**last_active_at** | **int** | Unix timestamp of the latest session activity, with day precision.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

