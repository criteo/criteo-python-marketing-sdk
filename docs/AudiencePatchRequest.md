# AudiencePatchRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**operation** | **str** | Mandatory. The Operation of this request. Can be either &#39;add&#39; or &#39;remove&#39;. | [optional] 
**schema** | **str** | Mandatory. The Schema specified for the identifiers. Can be &#39;email&#39;, &#39;madid&#39;, &#39;identityLink&#39; or &#39;gum&#39;. | [optional] 
**identifiers** | **list[str]** | Mandatory. The identifiers. | [optional] 
**gum_caller_id** | **int** | Optional. GumCallerId required only when patching identifiers with &#39;gum&#39; schema. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


