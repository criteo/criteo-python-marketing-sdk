# criteo_marketing.SellersApi

All URIs are relative to *https://api.criteo.com/marketing*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_budgets**](SellersApi.md#create_budgets) | **POST** /v1/sellers/budgets | Creates a budget for a seller/list of sellers.
[**get**](SellersApi.md#get) | **GET** /v1/sellers | Gets sellers details.
[**get_campaigns**](SellersApi.md#get_campaigns) | **GET** /v1/sellers/campaigns | Gets campaigns
[**get_stats**](SellersApi.md#get_stats) | **POST** /v1/sellers/stats | Generates a statistics report
[**update_bids**](SellersApi.md#update_bids) | **PUT** /v1/sellers/bids | Set or update a bid for a seller/list of sellers.
[**update_budgets**](SellersApi.md#update_budgets) | **PUT** /v1/sellers/budgets | Updates a budget for a seller/list of sellers.


# **create_budgets**
> SellerBudgetsMessage create_budgets(authorization, seller_budgets_create_message)

Creates a budget for a seller/list of sellers.

<b>Seller name</b>: can be retrieved from the /sellers/ endpoint. This value is case insensitive.<br /><b>Amount</b>: in your currency. Set it to \"null\" or leave empty to create an uncapped budget (with no limit).<br /><h4>Response</h4><p>              The budget's start date will be set to:<br />              • today: in case no budget is currently set for this seller<br />              • tomorrow: in case your seller already has a budget running, ending at midnight. Note that start dates are UTC+00:00 based.<br />              The budget will remain active until being completely consumed or stopped.<br /></p><h4>Validation rules</h4><p>              Budgets cannot <b>overlap</b> with each other for a specific seller.<br /></p><h4>Functional cases</h4><p>              When a seller's budget is totally consumed, display delivery will automatically stop for this specific seller.<br />              If budget needs to be updated, by: adding fund, reducing a budget amount or stopping it, refer to the “update budget” endpoint.<br /></p>

### Example

* Api Key Authentication (Authorization): 
```python
from __future__ import print_function
import time
import criteo_marketing
from criteo_marketing.rest import ApiException
from pprint import pprint

# Configure API key authorization: Authorization
configuration = criteo_marketing.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = criteo_marketing.SellersApi(criteo_marketing.ApiClient(configuration))
authorization = 'Bearer VALID_JWT_TOKEN_BASE64' # str | JWT Bearer Token (default to 'Bearer VALID_JWT_TOKEN_BASE64')
seller_budgets_create_message = criteo_marketing.SellerBudgetsCreateMessage() # SellerBudgetsCreateMessage | 

try:
    # Creates a budget for a seller/list of sellers.
    api_response = api_instance.create_budgets(authorization, seller_budgets_create_message)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SellersApi->create_budgets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| JWT Bearer Token | [default to &#39;Bearer VALID_JWT_TOKEN_BASE64&#39;]
 **seller_budgets_create_message** | [**SellerBudgetsCreateMessage**](SellerBudgetsCreateMessage.md)|  | 

### Return type

[**SellerBudgetsMessage**](SellerBudgetsMessage.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded, text/html
 - **Accept**: application/json, text/json, application/xml, text/xml, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get**
> list[SellerMessage] get(authorization, campaign_ids=campaign_ids, only_active_sellers=only_active_sellers, only_sellers_with_products_in_catalog=only_sellers_with_products_in_catalog, only_active_budgets=only_active_budgets)

Gets sellers details.

Returns a list of sellers with all their details.<br />  By default, this list will contain all active sellers that have been on-boarded onto the Criteo Reseller Program.<br />  Note that (in the situation where you would have multiple Criteo Reseller Program campaigns running at the same time) campaign filter can be applied to restrict the response to one or multiple campaign ids.<br /><h4>Functional cases</h4><p>  Only currently running and future seller budgets will be retrieved. Past sellers' budgets can be retrieved from the statistics endpoint.<br />  Seller's status has 2 possible values - Active or Inactive - which corresponds to:<br />  • <b>Active</b>: Seller in a running campaign, with a bid (CPC) and a budget &gt; 0<br />  • <b>Inactive</b>: Seller with a budget consumed or that you explicitly stopped.<br /></p>

### Example

* Api Key Authentication (Authorization): 
```python
from __future__ import print_function
import time
import criteo_marketing
from criteo_marketing.rest import ApiException
from pprint import pprint

# Configure API key authorization: Authorization
configuration = criteo_marketing.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = criteo_marketing.SellersApi(criteo_marketing.ApiClient(configuration))
authorization = 'Bearer VALID_JWT_TOKEN_BASE64' # str | JWT Bearer Token (default to 'Bearer VALID_JWT_TOKEN_BASE64')
campaign_ids = 'campaign_ids_example' # str | Optional. One or more campaign ids, E.g., 78, 12932, 45236. If any of the requested campaign ids are not Criteo Reseller Program or are not liked to advertisers in the user's portfolio, the call will fail. (optional)
only_active_sellers = True # bool | Optional. Filters by seller status, allowing to only display active sellers or not. Default value is false. (optional)
only_sellers_with_products_in_catalog = True # bool | Optional. Only return sellers that have currently products in the catalog. Default value is false. (optional)
only_active_budgets = True # bool | Optional. Will return only active budget for each seller. Default value is false (optional)

try:
    # Gets sellers details.
    api_response = api_instance.get(authorization, campaign_ids=campaign_ids, only_active_sellers=only_active_sellers, only_sellers_with_products_in_catalog=only_sellers_with_products_in_catalog, only_active_budgets=only_active_budgets)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SellersApi->get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| JWT Bearer Token | [default to &#39;Bearer VALID_JWT_TOKEN_BASE64&#39;]
 **campaign_ids** | **str**| Optional. One or more campaign ids, E.g., 78, 12932, 45236. If any of the requested campaign ids are not Criteo Reseller Program or are not liked to advertisers in the user&#39;s portfolio, the call will fail. | [optional] 
 **only_active_sellers** | **bool**| Optional. Filters by seller status, allowing to only display active sellers or not. Default value is false. | [optional] 
 **only_sellers_with_products_in_catalog** | **bool**| Optional. Only return sellers that have currently products in the catalog. Default value is false. | [optional] 
 **only_active_budgets** | **bool**| Optional. Will return only active budget for each seller. Default value is false | [optional] 

### Return type

[**list[SellerMessage]**](SellerMessage.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_campaigns**
> list[MarketplaceCampaignMessage] get_campaigns(authorization, campaign_ids=campaign_ids, advertiser_ids=advertiser_ids, status=status)

Gets campaigns

Get the list of campaigns with the specified filters.  If a campaign is requested but is missing from current user's portfolio, it will not be included in the list.  If neither campaign ids nor advertisers ids are provided, then the user's portfolio will be used.

### Example

* Api Key Authentication (Authorization): 
```python
from __future__ import print_function
import time
import criteo_marketing
from criteo_marketing.rest import ApiException
from pprint import pprint

# Configure API key authorization: Authorization
configuration = criteo_marketing.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = criteo_marketing.SellersApi(criteo_marketing.ApiClient(configuration))
authorization = 'Bearer VALID_JWT_TOKEN_BASE64' # str | JWT Bearer Token (default to 'Bearer VALID_JWT_TOKEN_BASE64')
campaign_ids = 'campaign_ids_example' # str | Optional. One or more campaign ids, E.g. 78, 12932, 45236. If any of the requested campaign ids are not Criteo Reseller Program or are not liked to advertisers in the user's portfolio, the call will fail. (optional)
advertiser_ids = 'advertiser_ids_example' # str | Optional. One or more advertiser ids, E.g. 78, 12932, 45236. If the requested advertiser ids are not part of the user's portfolio, the call will fail. (optional)
status = 'status_example' # str | Optional. Status of the campaign. By default, all campaigns are returned, regardless of their status. (optional)

try:
    # Gets campaigns
    api_response = api_instance.get_campaigns(authorization, campaign_ids=campaign_ids, advertiser_ids=advertiser_ids, status=status)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SellersApi->get_campaigns: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| JWT Bearer Token | [default to &#39;Bearer VALID_JWT_TOKEN_BASE64&#39;]
 **campaign_ids** | **str**| Optional. One or more campaign ids, E.g. 78, 12932, 45236. If any of the requested campaign ids are not Criteo Reseller Program or are not liked to advertisers in the user&#39;s portfolio, the call will fail. | [optional] 
 **advertiser_ids** | **str**| Optional. One or more advertiser ids, E.g. 78, 12932, 45236. If the requested advertiser ids are not part of the user&#39;s portfolio, the call will fail. | [optional] 
 **status** | **str**| Optional. Status of the campaign. By default, all campaigns are returned, regardless of their status. | [optional] 

### Return type

[**list[MarketplaceCampaignMessage]**](MarketplaceCampaignMessage.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_stats**
> get_stats(authorization, stats_query_message)

Generates a statistics report

<b>AdvertiserIds</b>: Optional. The list of advertiser ids, comma-separated. Advertisers not in your portfolio will be skipped. If not present, all the advertisers in the portfolio will be used.<br /><b>StartDate, EndDate</b>: Start date (beginning of day) and end date (end of day) to be used for the report generation. Format to use: yyyy-MM-dd (e.g. 2017-10-30).<br /><b>Dimensions</b>: The dimensions to be used in the report. Between one and three. Possible values: CampaignId, AdvertiserId, Seller, Day, Week, Month, Year.<br /><b>Metrics</b>: The metrics to be used in the report. Possible values: Clicks, AdvertiserCost, Displays.<br /><b>Format</b>: The file format of the generated report. Possible values: Csv, Excel, Xml, Json.<br /><b>Currency</b>: Optional. The currency to be used in the report. Three-letter capitals. For a list of possible values, please see the full documentation. If not set, the user's preference setting will be used.<br /><b>Timezone</b>: Optional. Timezone to be used in the report. Possible values: GMT, PST, JST. If not set, the user's preference setting will be used.<br /><h4>Validation rules</h4>              StartDate and EndDate are mandatory.<br />              StartDate should come before, or be equal to EndDate.<br />              The requested dimensions must be in a supported combination.<br />              At least one metric must be provided.<br />              All metrics must be supported.<br />              The selected advertisers must have at least one campaign.<br />              Seller dimension is mandatory.<br />

### Example

* Api Key Authentication (Authorization): 
```python
from __future__ import print_function
import time
import criteo_marketing
from criteo_marketing.rest import ApiException
from pprint import pprint

# Configure API key authorization: Authorization
configuration = criteo_marketing.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = criteo_marketing.SellersApi(criteo_marketing.ApiClient(configuration))
authorization = 'Bearer VALID_JWT_TOKEN_BASE64' # str | JWT Bearer Token (default to 'Bearer VALID_JWT_TOKEN_BASE64')
stats_query_message = criteo_marketing.StatsQueryMessage() # StatsQueryMessage | The report query details

try:
    # Generates a statistics report
    api_instance.get_stats(authorization, stats_query_message)
except ApiException as e:
    print("Exception when calling SellersApi->get_stats: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| JWT Bearer Token | [default to &#39;Bearer VALID_JWT_TOKEN_BASE64&#39;]
 **stats_query_message** | [**StatsQueryMessage**](StatsQueryMessage.md)| The report query details | 

### Return type

void (empty response body)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded, text/html
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_bids**
> SellerBidsMessage update_bids(authorization, seller_bids_message)

Set or update a bid for a seller/list of sellers.

<b>Seller name</b>: can be retrieved from the /sellers/ endpoint. This value is case insensitive.              <h4>Functional cases</h4><p>              In case one of the bid values cannot be updated, the whole batch will be dropped.<br /></p>

### Example

* Api Key Authentication (Authorization): 
```python
from __future__ import print_function
import time
import criteo_marketing
from criteo_marketing.rest import ApiException
from pprint import pprint

# Configure API key authorization: Authorization
configuration = criteo_marketing.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = criteo_marketing.SellersApi(criteo_marketing.ApiClient(configuration))
authorization = 'Bearer VALID_JWT_TOKEN_BASE64' # str | JWT Bearer Token (default to 'Bearer VALID_JWT_TOKEN_BASE64')
seller_bids_message = criteo_marketing.SellerBidsMessage() # SellerBidsMessage | 

try:
    # Set or update a bid for a seller/list of sellers.
    api_response = api_instance.update_bids(authorization, seller_bids_message)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SellersApi->update_bids: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| JWT Bearer Token | [default to &#39;Bearer VALID_JWT_TOKEN_BASE64&#39;]
 **seller_bids_message** | [**SellerBidsMessage**](SellerBidsMessage.md)|  | 

### Return type

[**SellerBidsMessage**](SellerBidsMessage.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded, text/html
 - **Accept**: application/json, text/json, application/xml, text/xml, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_budgets**
> SellerBudgetsMessage update_budgets(authorization, seller_budgets_update_message)

Updates a budget for a seller/list of sellers.

<b>Amount</b>: Optional. Uses the advertiser's currency. Set it to \"null\" or leave empty to create an uncapped budget (with no limit).<br /><b>Status</b>: Optional. Budget's status, possible values are: [\"Inactive\",\"Active\"]. If set to null or undefined, status does not change.              <h4>Validation rules</h4><p>              Budgets cannot <b>overlap</b> with each other for a specific seller.<br />              Budget's <b>amount</b> can be decreased if it did not start yet.<br />              Budget's <b>status</b> can only be changed from \"Active\" to \"Inactive\", if budget already started.<br /><b>Inactive</b> budgets cannot be updated.              </p><h4>Functional cases</h4><h5>Increase budget amount</h5><p>              Budget can only be increased if its end date is not reached.<br />              Amount value must include the amount that has been already spent.<br />              Example: if you want to add 50€ to a 100€ budget, you should update the amount to 150€, regardless of the amount already spent.<br />              Or, alternatively, you can set it to \"null\" or leave empty to change the budget to uncapped.<br /></p><h5>Stop budget consumption</h5><p>              Setting a currently running budget’s status to Inactive, result in:<br />              • Setting its end date to today (at 23:59:59, according to UTC+00:00)<br />              • Stopping its consumption instantly<br /></p><h5>Decrease budget amount</h5><p>              In order to decrease the amount of a currently running budget, you have to:<br />              • Stop budget consumption (making the currently running budget to end at 23:59:59, according to UTC+00:00)<br />              • Create a new budget with a dedicated amount. (that will start the following day, according to UTC+00:00)<br /></p>

### Example

* Api Key Authentication (Authorization): 
```python
from __future__ import print_function
import time
import criteo_marketing
from criteo_marketing.rest import ApiException
from pprint import pprint

# Configure API key authorization: Authorization
configuration = criteo_marketing.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = criteo_marketing.SellersApi(criteo_marketing.ApiClient(configuration))
authorization = 'Bearer VALID_JWT_TOKEN_BASE64' # str | JWT Bearer Token (default to 'Bearer VALID_JWT_TOKEN_BASE64')
seller_budgets_update_message = criteo_marketing.SellerBudgetsUpdateMessage() # SellerBudgetsUpdateMessage | 

try:
    # Updates a budget for a seller/list of sellers.
    api_response = api_instance.update_budgets(authorization, seller_budgets_update_message)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SellersApi->update_budgets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| JWT Bearer Token | [default to &#39;Bearer VALID_JWT_TOKEN_BASE64&#39;]
 **seller_budgets_update_message** | [**SellerBudgetsUpdateMessage**](SellerBudgetsUpdateMessage.md)|  | 

### Return type

[**SellerBudgetsMessage**](SellerBudgetsMessage.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded, text/html
 - **Accept**: application/json, text/json, application/xml, text/xml, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

