# ProductTaxV3

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rate** | **float** | The percentage of tax rate that applies to the item price. | [optional] 
**country** | **str** | The country within which the item is taxed, specified as a CLDR territory code. | [optional] 
**region** | **str** | The geographic region to which the tax rate applies. | [optional] 
**tax_ship** | **bool** | Set to true if tax is charged on shipping. | [optional] 
**location_id** | [**object**](.md) | The numeric ID of a location that the tax rate applies to as defined in the AdWords API. | [optional] 
**postal_code** | **str** | The postal code range that the tax rate applies to, represented by a ZIP code, a ZIP code prefix using * wildcard, a range between two ZIP codes or two ZIP code prefixes of equal length. Examples: 94114, 94*, 94002-95460, 94*-95*. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


