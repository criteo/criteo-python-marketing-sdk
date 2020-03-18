# criteo_marketing.SellersV2Api

All URIs are relative to *https://api.criteo.com/marketing*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_seller_budgets**](SellersV2Api.md#create_seller_budgets) | **POST** /v2/crp/budgets | Create a collection of budgets.
[**create_seller_campaigns_by_seller**](SellersV2Api.md#create_seller_campaigns_by_seller) | **POST** /v2/crp/sellers/{sellerId}/seller-campaigns | Create a SellerCampaign
[**create_sellers**](SellersV2Api.md#create_sellers) | **POST** /v2/crp/advertisers/{advertiserId}/sellers | Create new sellers for an advertiser
[**get_advertiser**](SellersV2Api.md#get_advertiser) | **GET** /v2/crp/advertisers/{advertiserId} | Get an advertiser.
[**get_advertiser_campaigns**](SellersV2Api.md#get_advertiser_campaigns) | **GET** /v2/crp/advertisers/{advertiserId}/campaigns | Get the collection of CRP campaigns associated with the advertiserId.
[**get_advertisers**](SellersV2Api.md#get_advertisers) | **GET** /v2/crp/advertisers | Get the collection of advertisers associated with the user.
[**get_budgets_by_seller**](SellersV2Api.md#get_budgets_by_seller) | **GET** /v2/crp/sellers/{sellerId}/budgets | Get a collection of budgets for this seller.
[**get_budgets_by_seller_campaign_id**](SellersV2Api.md#get_budgets_by_seller_campaign_id) | **GET** /v2/crp/seller-campaigns/{sellerCampaignId}/budgets | Get a collection of budgets for this seller campaign.
[**get_seller**](SellersV2Api.md#get_seller) | **GET** /v2/crp/sellers/{sellerId} | Get details for a seller.
[**get_seller_budget**](SellersV2Api.md#get_seller_budget) | **GET** /v2/crp/budgets/{budgetId} | Get details for a budget.
[**get_seller_budgets**](SellersV2Api.md#get_seller_budgets) | **GET** /v2/crp/budgets | Get a collection of budgets.
[**get_seller_campaign**](SellersV2Api.md#get_seller_campaign) | **GET** /v2/crp/seller-campaigns/{sellerCampaignId} | Get details for a seller campaign.
[**get_seller_campaigns**](SellersV2Api.md#get_seller_campaigns) | **GET** /v2/crp/seller-campaigns | Get a collection of seller campaigns.
[**get_seller_campaigns_by_seller**](SellersV2Api.md#get_seller_campaigns_by_seller) | **GET** /v2/crp/sellers/{sellerId}/seller-campaigns | Get a collection of seller campaigns for this seller.
[**get_sellers**](SellersV2Api.md#get_sellers) | **GET** /v2/crp/sellers | Get a collection of sellers.
[**update_seller_budget**](SellersV2Api.md#update_seller_budget) | **PATCH** /v2/crp/budgets/{budgetId} | Modify a single budget.
[**update_seller_budgets**](SellersV2Api.md#update_seller_budgets) | **PATCH** /v2/crp/budgets | Modify a collection of budgets.
[**update_seller_campaign**](SellersV2Api.md#update_seller_campaign) | **PATCH** /v2/crp/seller-campaigns/{sellerCampaignId} | Update an existing seller campaign.
[**update_seller_campaigns**](SellersV2Api.md#update_seller_campaigns) | **PATCH** /v2/crp/seller-campaigns | Update a collection of seller campaigns.


# **create_seller_budgets**
> list[SellerBudgetMessage] create_seller_budgets(authorization, create_seller_budgets)

Create a collection of budgets.

Create one or more new budgets to enable spending with the given limitations.  All three types of budgets can be created this way.                The following constraints apply when creating a new budget.                • <b>sellerId</b>: the seller MUST be supplied<br />  • <b>campaignIds</b>: a non-empty array of campaign ids MUST be supplied<br />  • <b>budgetType</b>: a budget type MUST be supplied<br />  • <b>amount</b>: an amount MAY be supplied only if the type is not Uncapped and if supplied it MUST be non-negative<br />  • <b>startDate</b>: a future start date MUST be supplied<br />  • <b>endDate</b>: an end date MAY be supplied and if supplied MUST be greater than the start date<br />                Other attributes MUST NOT be supplied.

### Example

* Api Key Authentication (Authorization):
```python
from __future__ import print_function
import time
import criteo_marketing
from criteo_marketing.rest import ApiException
from pprint import pprint
configuration = criteo_marketing.Configuration()
# Configure API key authorization: Authorization
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to https://api.criteo.com/marketing
configuration.host = "https://api.criteo.com/marketing"
# Create an instance of the API class
api_instance = criteo_marketing.SellersV2Api(criteo_marketing.ApiClient(configuration))
authorization = 'Bearer VALID_JWT_TOKEN_BASE64' # str | JWT Bearer Token (default to 'Bearer VALID_JWT_TOKEN_BASE64')
create_seller_budgets = [criteo_marketing.CreateSellerBudgetMapiMessage()] # list[CreateSellerBudgetMapiMessage] | 

try:
    # Create a collection of budgets.
    api_response = api_instance.create_seller_budgets(authorization, create_seller_budgets)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SellersV2Api->create_seller_budgets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| JWT Bearer Token | [default to &#39;Bearer VALID_JWT_TOKEN_BASE64&#39;]
 **create_seller_budgets** | [**list[CreateSellerBudgetMapiMessage]**](CreateSellerBudgetMapiMessage.md)|  | 

### Return type

[**list[SellerBudgetMessage]**](SellerBudgetMessage.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded, text/html
 - **Accept**: application/json, text/json, application/xml, text/xml, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Authentication failed. |  -  |
**403** | You do not have access to the requested records |  -  |
**429** | Throttling failure. Maximum sending rate exceeded. |  -  |
**500** | Unknown error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_seller_campaigns_by_seller**
> SellerCampaignMessage create_seller_campaigns_by_seller(seller_id, authorization, seller_campaign)

Create a SellerCampaign

Associate an existing Seller with an existing Campaign allowing for budget creation

### Example

* Api Key Authentication (Authorization):
```python
from __future__ import print_function
import time
import criteo_marketing
from criteo_marketing.rest import ApiException
from pprint import pprint
configuration = criteo_marketing.Configuration()
# Configure API key authorization: Authorization
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to https://api.criteo.com/marketing
configuration.host = "https://api.criteo.com/marketing"
# Create an instance of the API class
api_instance = criteo_marketing.SellersV2Api(criteo_marketing.ApiClient(configuration))
seller_id = 'seller_id_example' # str | Supply a generated Id of an existing Seller
authorization = 'Bearer VALID_JWT_TOKEN_BASE64' # str | JWT Bearer Token (default to 'Bearer VALID_JWT_TOKEN_BASE64')
seller_campaign = criteo_marketing.CreateSellerCampaignMessageMapi() # CreateSellerCampaignMessageMapi | Supply the campaign Id and bid to create the mapping

try:
    # Create a SellerCampaign
    api_response = api_instance.create_seller_campaigns_by_seller(seller_id, authorization, seller_campaign)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SellersV2Api->create_seller_campaigns_by_seller: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **seller_id** | **str**| Supply a generated Id of an existing Seller | 
 **authorization** | **str**| JWT Bearer Token | [default to &#39;Bearer VALID_JWT_TOKEN_BASE64&#39;]
 **seller_campaign** | [**CreateSellerCampaignMessageMapi**](CreateSellerCampaignMessageMapi.md)| Supply the campaign Id and bid to create the mapping | 

### Return type

[**SellerCampaignMessage**](SellerCampaignMessage.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded, text/html
 - **Accept**: application/json, text/json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Authentication failed. |  -  |
**403** | You do not have access to the requested records |  -  |
**429** | Throttling failure. Maximum sending rate exceeded. |  -  |
**500** | Unknown error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_sellers**
> list[SellerBase] create_sellers(advertiser_id, authorization, seller_names, partner_id=partner_id)

Create new sellers for an advertiser

### Example

* Api Key Authentication (Authorization):
```python
from __future__ import print_function
import time
import criteo_marketing
from criteo_marketing.rest import ApiException
from pprint import pprint
configuration = criteo_marketing.Configuration()
# Configure API key authorization: Authorization
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to https://api.criteo.com/marketing
configuration.host = "https://api.criteo.com/marketing"
# Create an instance of the API class
api_instance = criteo_marketing.SellersV2Api(criteo_marketing.ApiClient(configuration))
advertiser_id = 56 # int | 
authorization = 'Bearer VALID_JWT_TOKEN_BASE64' # str | JWT Bearer Token (default to 'Bearer VALID_JWT_TOKEN_BASE64')
seller_names = ['seller_names_example'] # list[str] | 
partner_id = 56 # int |  (optional)

try:
    # Create new sellers for an advertiser
    api_response = api_instance.create_sellers(advertiser_id, authorization, seller_names, partner_id=partner_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SellersV2Api->create_sellers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **advertiser_id** | **int**|  | 
 **authorization** | **str**| JWT Bearer Token | [default to &#39;Bearer VALID_JWT_TOKEN_BASE64&#39;]
 **seller_names** | [**list[str]**](str.md)|  | 
 **partner_id** | **int**|  | [optional] 

### Return type

[**list[SellerBase]**](SellerBase.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded, text/html
 - **Accept**: application/json, text/json, application/xml, text/xml, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Authentication failed. |  -  |
**403** | You do not have access to the requested records |  -  |
**429** | Throttling failure. Maximum sending rate exceeded. |  -  |
**500** | Unknown error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_advertiser**
> AdvertiserInfoMessage get_advertiser(advertiser_id, authorization)

Get an advertiser.

### Example

* Api Key Authentication (Authorization):
```python
from __future__ import print_function
import time
import criteo_marketing
from criteo_marketing.rest import ApiException
from pprint import pprint
configuration = criteo_marketing.Configuration()
# Configure API key authorization: Authorization
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to https://api.criteo.com/marketing
configuration.host = "https://api.criteo.com/marketing"
# Create an instance of the API class
api_instance = criteo_marketing.SellersV2Api(criteo_marketing.ApiClient(configuration))
advertiser_id = 56 # int | 
authorization = 'Bearer VALID_JWT_TOKEN_BASE64' # str | JWT Bearer Token (default to 'Bearer VALID_JWT_TOKEN_BASE64')

try:
    # Get an advertiser.
    api_response = api_instance.get_advertiser(advertiser_id, authorization)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SellersV2Api->get_advertiser: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **advertiser_id** | **int**|  | 
 **authorization** | **str**| JWT Bearer Token | [default to &#39;Bearer VALID_JWT_TOKEN_BASE64&#39;]

### Return type

[**AdvertiserInfoMessage**](AdvertiserInfoMessage.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Authentication failed. |  -  |
**403** | You do not have access to the requested records |  -  |
**429** | Throttling failure. Maximum sending rate exceeded. |  -  |
**500** | Unknown error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_advertiser_campaigns**
> list[AdvertiserCampaignMessage] get_advertiser_campaigns(advertiser_id, authorization)

Get the collection of CRP campaigns associated with the advertiserId.

### Example

* Api Key Authentication (Authorization):
```python
from __future__ import print_function
import time
import criteo_marketing
from criteo_marketing.rest import ApiException
from pprint import pprint
configuration = criteo_marketing.Configuration()
# Configure API key authorization: Authorization
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to https://api.criteo.com/marketing
configuration.host = "https://api.criteo.com/marketing"
# Create an instance of the API class
api_instance = criteo_marketing.SellersV2Api(criteo_marketing.ApiClient(configuration))
advertiser_id = 56 # int | 
authorization = 'Bearer VALID_JWT_TOKEN_BASE64' # str | JWT Bearer Token (default to 'Bearer VALID_JWT_TOKEN_BASE64')

try:
    # Get the collection of CRP campaigns associated with the advertiserId.
    api_response = api_instance.get_advertiser_campaigns(advertiser_id, authorization)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SellersV2Api->get_advertiser_campaigns: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **advertiser_id** | **int**|  | 
 **authorization** | **str**| JWT Bearer Token | [default to &#39;Bearer VALID_JWT_TOKEN_BASE64&#39;]

### Return type

[**list[AdvertiserCampaignMessage]**](AdvertiserCampaignMessage.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Authentication failed. |  -  |
**403** | You do not have access to the requested records |  -  |
**429** | Throttling failure. Maximum sending rate exceeded. |  -  |
**500** | Unknown error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_advertisers**
> list[AdvertiserInfoMessage] get_advertisers(authorization)

Get the collection of advertisers associated with the user.

### Example

* Api Key Authentication (Authorization):
```python
from __future__ import print_function
import time
import criteo_marketing
from criteo_marketing.rest import ApiException
from pprint import pprint
configuration = criteo_marketing.Configuration()
# Configure API key authorization: Authorization
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to https://api.criteo.com/marketing
configuration.host = "https://api.criteo.com/marketing"
# Create an instance of the API class
api_instance = criteo_marketing.SellersV2Api(criteo_marketing.ApiClient(configuration))
authorization = 'Bearer VALID_JWT_TOKEN_BASE64' # str | JWT Bearer Token (default to 'Bearer VALID_JWT_TOKEN_BASE64')

try:
    # Get the collection of advertisers associated with the user.
    api_response = api_instance.get_advertisers(authorization)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SellersV2Api->get_advertisers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| JWT Bearer Token | [default to &#39;Bearer VALID_JWT_TOKEN_BASE64&#39;]

### Return type

[**list[AdvertiserInfoMessage]**](AdvertiserInfoMessage.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Authentication failed. |  -  |
**403** | You do not have access to the requested records |  -  |
**429** | Throttling failure. Maximum sending rate exceeded. |  -  |
**500** | Unknown error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_budgets_by_seller**
> list[SellerBudgetMessage] get_budgets_by_seller(seller_id, authorization, status=status, with_balance=with_balance, with_spend=with_spend, end_after_date=end_after_date, start_before_date=start_before_date, campaign_id=campaign_id, type=type)

Get a collection of budgets for this seller.

Return a collection of budgets for this seller filtered by optional filter parameters.  If all parameters are omitted the entire collection to which the user has  access is returned, except those whose endDate is in the past. Returned budgets must satisfy all supplied filter  criteria if multiple parameters are used. See the budgets endpoint for additional details.

### Example

* Api Key Authentication (Authorization):
```python
from __future__ import print_function
import time
import criteo_marketing
from criteo_marketing.rest import ApiException
from pprint import pprint
configuration = criteo_marketing.Configuration()
# Configure API key authorization: Authorization
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to https://api.criteo.com/marketing
configuration.host = "https://api.criteo.com/marketing"
# Create an instance of the API class
api_instance = criteo_marketing.SellersV2Api(criteo_marketing.ApiClient(configuration))
seller_id = 'seller_id_example' # str | Return only budgets belonging to the given seller.
authorization = 'Bearer VALID_JWT_TOKEN_BASE64' # str | JWT Bearer Token (default to 'Bearer VALID_JWT_TOKEN_BASE64')
status = 'status_example' # str | Return only budgets with the given status. (optional)
with_balance = True # bool | Return only budgets with the given status. (optional)
with_spend = True # bool | Return budgets with any positive spend. (optional)
end_after_date = '2013-10-20T19:20:30+01:00' # datetime | Return budgets that end after the given date using the `yyyy-MM-DD` format.              If param is not provided, default behavior is to only return budgets that have not yet ended. (optional)
start_before_date = '2013-10-20T19:20:30+01:00' # datetime | Return budgets that start on or before the given date using the `yyyy-MM-DD` format. (optional)
campaign_id = 56 # int | Return only budgets that pay for a given campaign. (optional)
type = 'type_example' # str | Return only budgets with the given budget type. (optional)

try:
    # Get a collection of budgets for this seller.
    api_response = api_instance.get_budgets_by_seller(seller_id, authorization, status=status, with_balance=with_balance, with_spend=with_spend, end_after_date=end_after_date, start_before_date=start_before_date, campaign_id=campaign_id, type=type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SellersV2Api->get_budgets_by_seller: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **seller_id** | **str**| Return only budgets belonging to the given seller. | 
 **authorization** | **str**| JWT Bearer Token | [default to &#39;Bearer VALID_JWT_TOKEN_BASE64&#39;]
 **status** | **str**| Return only budgets with the given status. | [optional] 
 **with_balance** | **bool**| Return only budgets with the given status. | [optional] 
 **with_spend** | **bool**| Return budgets with any positive spend. | [optional] 
 **end_after_date** | **datetime**| Return budgets that end after the given date using the &#x60;yyyy-MM-DD&#x60; format.              If param is not provided, default behavior is to only return budgets that have not yet ended. | [optional] 
 **start_before_date** | **datetime**| Return budgets that start on or before the given date using the &#x60;yyyy-MM-DD&#x60; format. | [optional] 
 **campaign_id** | **int**| Return only budgets that pay for a given campaign. | [optional] 
 **type** | **str**| Return only budgets with the given budget type. | [optional] 

### Return type

[**list[SellerBudgetMessage]**](SellerBudgetMessage.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | List of errors encountered |  -  |
**401** | Authentication failed. |  -  |
**403** | You do not have access to the requested records |  -  |
**429** | Throttling failure. Maximum sending rate exceeded. |  -  |
**500** | Unknown error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_budgets_by_seller_campaign_id**
> list[SellerBudgetMessage] get_budgets_by_seller_campaign_id(seller_campaign_id, authorization, status=status, with_balance=with_balance, with_spend=with_spend, end_after_date=end_after_date, start_before_date=start_before_date, type=type)

Get a collection of budgets for this seller campaign.

Return a collection of budgets for this seller campaign filtered by optional filter parameters.  If all parameters are omitted the entire collection to which the user has  access is returned, except those whose endDate is in the past. Returned budgets must satisfy all supplied filter  criteria if multiple parameters are used.                See the budgets endpoint for additional details.

### Example

* Api Key Authentication (Authorization):
```python
from __future__ import print_function
import time
import criteo_marketing
from criteo_marketing.rest import ApiException
from pprint import pprint
configuration = criteo_marketing.Configuration()
# Configure API key authorization: Authorization
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to https://api.criteo.com/marketing
configuration.host = "https://api.criteo.com/marketing"
# Create an instance of the API class
api_instance = criteo_marketing.SellersV2Api(criteo_marketing.ApiClient(configuration))
seller_campaign_id = 'seller_campaign_id_example' # str | Return only budgets belonging to the given seller campaign.
authorization = 'Bearer VALID_JWT_TOKEN_BASE64' # str | JWT Bearer Token (default to 'Bearer VALID_JWT_TOKEN_BASE64')
status = 'status_example' # str | Return only budgets with the given status. (optional)
with_balance = True # bool | Return only budgets with a positive balance. (optional)
with_spend = True # bool | Return budgets with a positive spend. (optional)
end_after_date = '2013-10-20T19:20:30+01:00' # datetime | Return budgets that end after the given date using the `yyyy-MM-DD` format.               If param is not provided, default behavior is to only return budgets that have not yet ended. (optional)
start_before_date = '2013-10-20T19:20:30+01:00' # datetime | Return budgets that start on or before the given date using the `yyyy-MM-DD` format. (optional)
type = 'type_example' # str | Return only budgets with the given budget type. (optional)

try:
    # Get a collection of budgets for this seller campaign.
    api_response = api_instance.get_budgets_by_seller_campaign_id(seller_campaign_id, authorization, status=status, with_balance=with_balance, with_spend=with_spend, end_after_date=end_after_date, start_before_date=start_before_date, type=type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SellersV2Api->get_budgets_by_seller_campaign_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **seller_campaign_id** | **str**| Return only budgets belonging to the given seller campaign. | 
 **authorization** | **str**| JWT Bearer Token | [default to &#39;Bearer VALID_JWT_TOKEN_BASE64&#39;]
 **status** | **str**| Return only budgets with the given status. | [optional] 
 **with_balance** | **bool**| Return only budgets with a positive balance. | [optional] 
 **with_spend** | **bool**| Return budgets with a positive spend. | [optional] 
 **end_after_date** | **datetime**| Return budgets that end after the given date using the &#x60;yyyy-MM-DD&#x60; format.               If param is not provided, default behavior is to only return budgets that have not yet ended. | [optional] 
 **start_before_date** | **datetime**| Return budgets that start on or before the given date using the &#x60;yyyy-MM-DD&#x60; format. | [optional] 
 **type** | **str**| Return only budgets with the given budget type. | [optional] 

### Return type

[**list[SellerBudgetMessage]**](SellerBudgetMessage.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | List of errors encountered |  -  |
**401** | Authentication failed. |  -  |
**403** | You do not have access to the requested records |  -  |
**429** | Throttling failure. Maximum sending rate exceeded. |  -  |
**500** | Unknown error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_seller**
> SellerBase get_seller(seller_id, authorization)

Get details for a seller.

Returns details for the selected seller.  For example                    {          \"id\" : \"123456\"          \"sellerName\": \"HBogart\",      }

### Example

* Api Key Authentication (Authorization):
```python
from __future__ import print_function
import time
import criteo_marketing
from criteo_marketing.rest import ApiException
from pprint import pprint
configuration = criteo_marketing.Configuration()
# Configure API key authorization: Authorization
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to https://api.criteo.com/marketing
configuration.host = "https://api.criteo.com/marketing"
# Create an instance of the API class
api_instance = criteo_marketing.SellersV2Api(criteo_marketing.ApiClient(configuration))
seller_id = 'seller_id_example' # str | Id of the seller.
authorization = 'Bearer VALID_JWT_TOKEN_BASE64' # str | JWT Bearer Token (default to 'Bearer VALID_JWT_TOKEN_BASE64')

try:
    # Get details for a seller.
    api_response = api_instance.get_seller(seller_id, authorization)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SellersV2Api->get_seller: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **seller_id** | **str**| Id of the seller. | 
 **authorization** | **str**| JWT Bearer Token | [default to &#39;Bearer VALID_JWT_TOKEN_BASE64&#39;]

### Return type

[**SellerBase**](SellerBase.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | List of errors encountered |  -  |
**401** | Authentication failed. |  -  |
**403** | You do not have access to the requested records |  -  |
**429** | Throttling failure. Maximum sending rate exceeded. |  -  |
**500** | Unknown error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_seller_budget**
> SellerBudgetMessage get_seller_budget(budget_id, authorization)

Get details for a budget.

Return a budget. For example:                    {          \"id\": \"1759183\",          \"sellerId\": \"321392\",          \"campaignIds\": [              143962          ],          \"budgetType\": \"Capped\",          \"amount\": 1000,          \"startDate\": \"2021-01-11\",          \"endDate\": \"2021-01-12\",          \"spend\": null,          \"status\": \"Active\"      }                A budget limits the spend of a seller for one or more campaigns.                There are three types of budget:<br /><b>Uncapped</b> budgets put no limit on the total amount of spend.<br /><b>Capped</b> budgets limit the total spend to a fixed amount.<br /><b>Daily</b> budgets limit daily spend to a fixed amount.<br />                In addition, budgets can limit the spend to a specific range of dates using  the start and end date attributes. Finally a budget must be active to be used.                <b>Spend</b> approximates the current spend against this budget. There may be a lag  between when an ad is clicked and the time it accrues to the spend.  Daily budgets  show spend against the most recent day only.

### Example

* Api Key Authentication (Authorization):
```python
from __future__ import print_function
import time
import criteo_marketing
from criteo_marketing.rest import ApiException
from pprint import pprint
configuration = criteo_marketing.Configuration()
# Configure API key authorization: Authorization
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to https://api.criteo.com/marketing
configuration.host = "https://api.criteo.com/marketing"
# Create an instance of the API class
api_instance = criteo_marketing.SellersV2Api(criteo_marketing.ApiClient(configuration))
budget_id = 56 # int | Id of the budget.
authorization = 'Bearer VALID_JWT_TOKEN_BASE64' # str | JWT Bearer Token (default to 'Bearer VALID_JWT_TOKEN_BASE64')

try:
    # Get details for a budget.
    api_response = api_instance.get_seller_budget(budget_id, authorization)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SellersV2Api->get_seller_budget: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **budget_id** | **int**| Id of the budget. | 
 **authorization** | **str**| JWT Bearer Token | [default to &#39;Bearer VALID_JWT_TOKEN_BASE64&#39;]

### Return type

[**SellerBudgetMessage**](SellerBudgetMessage.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | List of errors encountered |  -  |
**401** | Authentication failed. |  -  |
**403** | You do not have access to the requested records |  -  |
**429** | Throttling failure. Maximum sending rate exceeded. |  -  |
**500** | Unknown error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_seller_budgets**
> list[SellerBudgetMessage] get_seller_budgets(authorization, status=status, with_balance=with_balance, with_spend=with_spend, end_after_date=end_after_date, start_before_date=start_before_date, campaign_id=campaign_id, seller_id=seller_id, type=type)

Get a collection of budgets.

Return a collection of budgets filtered by optional filter parameters.  If all parameters are omitted the entire collection to which the user has  access is returned, except those whose endDate is in the past. Returned budgets must satisfy all supplied filter  criteria if multiple parameters are used.                <b>Date filter.</b> Filtering can return only budgets that were active for a  date range by specifying the startBeforeDate and endAfterDate. Leaving off the startBeforeDate  value makes budgets with any startDate qualify, whereas when leaving off the endAfterDate value will only return  budgets whose endDate has not already passed. To get budgets that were active  on a specific date, set both values to that day.                <b>Spend.</b> If the endAfterDate is supplied, the spend excludes spend that  happened after that date. In the case of a daily budget, only the spend for  the final day is displayed.                See the budgets endpoint for additional details.

### Example

* Api Key Authentication (Authorization):
```python
from __future__ import print_function
import time
import criteo_marketing
from criteo_marketing.rest import ApiException
from pprint import pprint
configuration = criteo_marketing.Configuration()
# Configure API key authorization: Authorization
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to https://api.criteo.com/marketing
configuration.host = "https://api.criteo.com/marketing"
# Create an instance of the API class
api_instance = criteo_marketing.SellersV2Api(criteo_marketing.ApiClient(configuration))
authorization = 'Bearer VALID_JWT_TOKEN_BASE64' # str | JWT Bearer Token (default to 'Bearer VALID_JWT_TOKEN_BASE64')
status = 'status_example' # str | Return only budgets with the given status. (optional)
with_balance = True # bool | Return only budgets with the given status. (optional)
with_spend = True # bool | Return budgets with any positive spend. (optional)
end_after_date = '2013-10-20T19:20:30+01:00' # datetime | Return budgets that end after the given date using the `yyyy-MM-DD` format.               If param is not provided, default behavior is to only return budgets that have not yet ended. (optional)
start_before_date = '2013-10-20T19:20:30+01:00' # datetime | Return budgets that start on or before the given date using the `yyyy-MM-DD` format. (optional)
campaign_id = 56 # int | Return only budgets that pay for a given campaign. (optional)
seller_id = 'seller_id_example' # str | Return only budgets belonging to the given seller. (optional)
type = 'type_example' # str | Return only budgets with the given budget type. (optional)

try:
    # Get a collection of budgets.
    api_response = api_instance.get_seller_budgets(authorization, status=status, with_balance=with_balance, with_spend=with_spend, end_after_date=end_after_date, start_before_date=start_before_date, campaign_id=campaign_id, seller_id=seller_id, type=type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SellersV2Api->get_seller_budgets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| JWT Bearer Token | [default to &#39;Bearer VALID_JWT_TOKEN_BASE64&#39;]
 **status** | **str**| Return only budgets with the given status. | [optional] 
 **with_balance** | **bool**| Return only budgets with the given status. | [optional] 
 **with_spend** | **bool**| Return budgets with any positive spend. | [optional] 
 **end_after_date** | **datetime**| Return budgets that end after the given date using the &#x60;yyyy-MM-DD&#x60; format.               If param is not provided, default behavior is to only return budgets that have not yet ended. | [optional] 
 **start_before_date** | **datetime**| Return budgets that start on or before the given date using the &#x60;yyyy-MM-DD&#x60; format. | [optional] 
 **campaign_id** | **int**| Return only budgets that pay for a given campaign. | [optional] 
 **seller_id** | **str**| Return only budgets belonging to the given seller. | [optional] 
 **type** | **str**| Return only budgets with the given budget type. | [optional] 

### Return type

[**list[SellerBudgetMessage]**](SellerBudgetMessage.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | List of errors encountered |  -  |
**401** | Authentication failed. |  -  |
**403** | You do not have access to the requested records |  -  |
**429** | Throttling failure. Maximum sending rate exceeded. |  -  |
**500** | Unknown error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_seller_campaign**
> SellerCampaignMessage get_seller_campaign(seller_campaign_id, authorization)

Get details for a seller campaign.

Return details for a seller campaign.  For example,                    {          \"id\": \"543210.123456\",          \"suspendedSince\": \"2018-07-30\",          \"sellerId\": \"543210\",          \"campaignId\": 123456,          \"bid\": 1.55      }                An active seller campaign is one for which the value of <b>suspendedSince</b> is null and  the <b>bid</b> is positive. The currency of the bid is the <b>bidCurrency</b> of the  associated campaign.                Any active seller campaign must also have an active total (capped or uncapped) budget.  It may optionally have an active daily budget as well to further limit spending.

### Example

* Api Key Authentication (Authorization):
```python
from __future__ import print_function
import time
import criteo_marketing
from criteo_marketing.rest import ApiException
from pprint import pprint
configuration = criteo_marketing.Configuration()
# Configure API key authorization: Authorization
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to https://api.criteo.com/marketing
configuration.host = "https://api.criteo.com/marketing"
# Create an instance of the API class
api_instance = criteo_marketing.SellersV2Api(criteo_marketing.ApiClient(configuration))
seller_campaign_id = 'seller_campaign_id_example' # str | Id of the seller campaign.
authorization = 'Bearer VALID_JWT_TOKEN_BASE64' # str | JWT Bearer Token (default to 'Bearer VALID_JWT_TOKEN_BASE64')

try:
    # Get details for a seller campaign.
    api_response = api_instance.get_seller_campaign(seller_campaign_id, authorization)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SellersV2Api->get_seller_campaign: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **seller_campaign_id** | **str**| Id of the seller campaign. | 
 **authorization** | **str**| JWT Bearer Token | [default to &#39;Bearer VALID_JWT_TOKEN_BASE64&#39;]

### Return type

[**SellerCampaignMessage**](SellerCampaignMessage.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | List of errors encountered |  -  |
**401** | Authentication failed. |  -  |
**403** | You do not have access to the requested records |  -  |
**429** | Throttling failure. Maximum sending rate exceeded. |  -  |
**500** | Unknown error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_seller_campaigns**
> list[SellerCampaignMessage] get_seller_campaigns(authorization, seller_status=seller_status, seller_id=seller_id, campaign_id=campaign_id, budget_status=budget_status)

Get a collection of seller campaigns.

Return a collection of seller campaigns filtered by optional filter parameters.  If all parameters are omitted the entire collection to which the user has  access is returned. Returned sellers must satisfy all supplied filter  criteria if multiple parameters are used.

### Example

* Api Key Authentication (Authorization):
```python
from __future__ import print_function
import time
import criteo_marketing
from criteo_marketing.rest import ApiException
from pprint import pprint
configuration = criteo_marketing.Configuration()
# Configure API key authorization: Authorization
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to https://api.criteo.com/marketing
configuration.host = "https://api.criteo.com/marketing"
# Create an instance of the API class
api_instance = criteo_marketing.SellersV2Api(criteo_marketing.ApiClient(configuration))
authorization = 'Bearer VALID_JWT_TOKEN_BASE64' # str | JWT Bearer Token (default to 'Bearer VALID_JWT_TOKEN_BASE64')
seller_status = 'seller_status_example' # str | Return only seller campaigns for sellers with the given status. (optional)
seller_id = 'seller_id_example' # str | Return only seller campaigns belonging to the given seller. (optional)
campaign_id = 56 # int | Return only seller campaigns associated with the given campaign. (optional)
budget_status = 'budget_status_example' # str | Return only seller campaigns whose budget has the given status. (optional)

try:
    # Get a collection of seller campaigns.
    api_response = api_instance.get_seller_campaigns(authorization, seller_status=seller_status, seller_id=seller_id, campaign_id=campaign_id, budget_status=budget_status)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SellersV2Api->get_seller_campaigns: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| JWT Bearer Token | [default to &#39;Bearer VALID_JWT_TOKEN_BASE64&#39;]
 **seller_status** | **str**| Return only seller campaigns for sellers with the given status. | [optional] 
 **seller_id** | **str**| Return only seller campaigns belonging to the given seller. | [optional] 
 **campaign_id** | **int**| Return only seller campaigns associated with the given campaign. | [optional] 
 **budget_status** | **str**| Return only seller campaigns whose budget has the given status. | [optional] 

### Return type

[**list[SellerCampaignMessage]**](SellerCampaignMessage.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | List of errors encountered |  -  |
**401** | Authentication failed. |  -  |
**403** | You do not have access to the requested records |  -  |
**429** | Throttling failure. Maximum sending rate exceeded. |  -  |
**500** | Unknown error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_seller_campaigns_by_seller**
> list[SellerCampaignMessage] get_seller_campaigns_by_seller(seller_id, authorization, seller_status=seller_status, campaign_id=campaign_id, budget_status=budget_status)

Get a collection of seller campaigns for this seller.

Return a collection of seller campaigns for this seller filtered by optional filter parameters.  If all parameters are omitted the entire collection to which the user has  access is returned. Returned sellers must satisfy all supplied filter  criteria if multiple parameters are used.  See the seller campaigns endpoint for additional details.

### Example

* Api Key Authentication (Authorization):
```python
from __future__ import print_function
import time
import criteo_marketing
from criteo_marketing.rest import ApiException
from pprint import pprint
configuration = criteo_marketing.Configuration()
# Configure API key authorization: Authorization
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to https://api.criteo.com/marketing
configuration.host = "https://api.criteo.com/marketing"
# Create an instance of the API class
api_instance = criteo_marketing.SellersV2Api(criteo_marketing.ApiClient(configuration))
seller_id = 'seller_id_example' # str | Return only seller campaigns belonging to the given seller.
authorization = 'Bearer VALID_JWT_TOKEN_BASE64' # str | JWT Bearer Token (default to 'Bearer VALID_JWT_TOKEN_BASE64')
seller_status = 'seller_status_example' # str | Return only seller campaigns for sellers with the given status. (optional)
campaign_id = 56 # int | Return only seller campaigns associated with the given campaign. (optional)
budget_status = 'budget_status_example' # str | Return only seller campaigns whose budget has the given status. (optional)

try:
    # Get a collection of seller campaigns for this seller.
    api_response = api_instance.get_seller_campaigns_by_seller(seller_id, authorization, seller_status=seller_status, campaign_id=campaign_id, budget_status=budget_status)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SellersV2Api->get_seller_campaigns_by_seller: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **seller_id** | **str**| Return only seller campaigns belonging to the given seller. | 
 **authorization** | **str**| JWT Bearer Token | [default to &#39;Bearer VALID_JWT_TOKEN_BASE64&#39;]
 **seller_status** | **str**| Return only seller campaigns for sellers with the given status. | [optional] 
 **campaign_id** | **int**| Return only seller campaigns associated with the given campaign. | [optional] 
 **budget_status** | **str**| Return only seller campaigns whose budget has the given status. | [optional] 

### Return type

[**list[SellerCampaignMessage]**](SellerCampaignMessage.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | List of errors encountered |  -  |
**401** | Authentication failed. |  -  |
**403** | You do not have access to the requested records |  -  |
**429** | Throttling failure. Maximum sending rate exceeded. |  -  |
**500** | Unknown error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sellers**
> list[SellerBase] get_sellers(authorization, seller_status=seller_status, with_products=with_products, with_budget_status=with_budget_status, seller_name=seller_name)

Get a collection of sellers.

Return a collection of sellers filtered by optional filter parameters.  If all parameters are omitted the entire collection to which the user has  access is returned. Returned sellers must satisfy all supplied filter  criteria if multiple parameters are used.

### Example

* Api Key Authentication (Authorization):
```python
from __future__ import print_function
import time
import criteo_marketing
from criteo_marketing.rest import ApiException
from pprint import pprint
configuration = criteo_marketing.Configuration()
# Configure API key authorization: Authorization
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to https://api.criteo.com/marketing
configuration.host = "https://api.criteo.com/marketing"
# Create an instance of the API class
api_instance = criteo_marketing.SellersV2Api(criteo_marketing.ApiClient(configuration))
authorization = 'Bearer VALID_JWT_TOKEN_BASE64' # str | JWT Bearer Token (default to 'Bearer VALID_JWT_TOKEN_BASE64')
seller_status = 'seller_status_example' # str | Return only sellers with specific status. (optional)
with_products = True # bool | Return only sellers with or without products in catalog. (optional)
with_budget_status = 'with_budget_status_example' # str | Return only sellers with specific budget status. (optional)
seller_name = 'seller_name_example' # str | Return only sellers with the matching name. (optional)

try:
    # Get a collection of sellers.
    api_response = api_instance.get_sellers(authorization, seller_status=seller_status, with_products=with_products, with_budget_status=with_budget_status, seller_name=seller_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SellersV2Api->get_sellers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| JWT Bearer Token | [default to &#39;Bearer VALID_JWT_TOKEN_BASE64&#39;]
 **seller_status** | **str**| Return only sellers with specific status. | [optional] 
 **with_products** | **bool**| Return only sellers with or without products in catalog. | [optional] 
 **with_budget_status** | **str**| Return only sellers with specific budget status. | [optional] 
 **seller_name** | **str**| Return only sellers with the matching name. | [optional] 

### Return type

[**list[SellerBase]**](SellerBase.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | List of errors encountered |  -  |
**401** | Authentication failed. |  -  |
**403** | You do not have access to the requested records |  -  |
**429** | Throttling failure. Maximum sending rate exceeded. |  -  |
**500** | Unknown error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_seller_budget**
> SellerBudgetMessage update_seller_budget(budget_id, authorization, message)

Modify a single budget.

Modify an existing active budget to change its limitations or status.  All three types of budgets can be modified.                See the additional restrictions listed in the PATCH budgets endpoint.

### Example

* Api Key Authentication (Authorization):
```python
from __future__ import print_function
import time
import criteo_marketing
from criteo_marketing.rest import ApiException
from pprint import pprint
configuration = criteo_marketing.Configuration()
# Configure API key authorization: Authorization
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to https://api.criteo.com/marketing
configuration.host = "https://api.criteo.com/marketing"
# Create an instance of the API class
api_instance = criteo_marketing.SellersV2Api(criteo_marketing.ApiClient(configuration))
budget_id = 56 # int | 
authorization = 'Bearer VALID_JWT_TOKEN_BASE64' # str | JWT Bearer Token (default to 'Bearer VALID_JWT_TOKEN_BASE64')
message = criteo_marketing.UpdateSellerBudgetMessageBase() # UpdateSellerBudgetMessageBase | 

try:
    # Modify a single budget.
    api_response = api_instance.update_seller_budget(budget_id, authorization, message)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SellersV2Api->update_seller_budget: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **budget_id** | **int**|  | 
 **authorization** | **str**| JWT Bearer Token | [default to &#39;Bearer VALID_JWT_TOKEN_BASE64&#39;]
 **message** | [**UpdateSellerBudgetMessageBase**](UpdateSellerBudgetMessageBase.md)|  | 

### Return type

[**SellerBudgetMessage**](SellerBudgetMessage.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/x-www-form-urlencoded, text/html
 - **Accept**: application/json, text/json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Authentication failed. |  -  |
**403** | You do not have access to the requested records |  -  |
**429** | Throttling failure. Maximum sending rate exceeded. |  -  |
**500** | Unknown error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_seller_budgets**
> list[SellerBudgetMessage] update_seller_budgets(authorization, update_seller_budgets)

Modify a collection of budgets.

Modify one or more existing active budgets to change their limitations or status.  All three types of budgets can be modified.                The following constraints apply when modifying an existing budget.                • <b>campaignIds</b>: a non-empty subset of the original campaign ids MAY be supplied<br />  • <b>amount</b>: an amount MAY be supplied only if the type is not Uncapped and if supplied it MUST be non-negative<br />  • <b>startDate</b>: a future start date MAY be supplied for budgets that have not yet started<br />  • <b>endDate</b>: an end date MAY be supplied and if supplied MUST be a future date greater than the start date<br />                Other attributes MUST NOT be supplied.                Adding new campaigns to a budget is not allowed. In addition, reducing the amount for  a Capped budget to a value less than the current spend not allowed.

### Example

* Api Key Authentication (Authorization):
```python
from __future__ import print_function
import time
import criteo_marketing
from criteo_marketing.rest import ApiException
from pprint import pprint
configuration = criteo_marketing.Configuration()
# Configure API key authorization: Authorization
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to https://api.criteo.com/marketing
configuration.host = "https://api.criteo.com/marketing"
# Create an instance of the API class
api_instance = criteo_marketing.SellersV2Api(criteo_marketing.ApiClient(configuration))
authorization = 'Bearer VALID_JWT_TOKEN_BASE64' # str | JWT Bearer Token (default to 'Bearer VALID_JWT_TOKEN_BASE64')
update_seller_budgets = [criteo_marketing.UpdateSellerBudgetMessage()] # list[UpdateSellerBudgetMessage] | 

try:
    # Modify a collection of budgets.
    api_response = api_instance.update_seller_budgets(authorization, update_seller_budgets)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SellersV2Api->update_seller_budgets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| JWT Bearer Token | [default to &#39;Bearer VALID_JWT_TOKEN_BASE64&#39;]
 **update_seller_budgets** | [**list[UpdateSellerBudgetMessage]**](UpdateSellerBudgetMessage.md)|  | 

### Return type

[**list[SellerBudgetMessage]**](SellerBudgetMessage.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded, text/html
 - **Accept**: application/json, text/json, application/xml, text/xml, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Authentication failed. |  -  |
**403** | You do not have access to the requested records |  -  |
**429** | Throttling failure. Maximum sending rate exceeded. |  -  |
**500** | Unknown error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_seller_campaign**
> SellerCampaignMessage update_seller_campaign(seller_campaign_id, bid, authorization)

Update an existing seller campaign.

Patching a seller campaign allows the bid to be modified. The bid must be a non-negative value.  Setting the bid to zero will make a seller campaign inactive.                The currency used for bids will be the default currency of the campaign.

### Example

* Api Key Authentication (Authorization):
```python
from __future__ import print_function
import time
import criteo_marketing
from criteo_marketing.rest import ApiException
from pprint import pprint
configuration = criteo_marketing.Configuration()
# Configure API key authorization: Authorization
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to https://api.criteo.com/marketing
configuration.host = "https://api.criteo.com/marketing"
# Create an instance of the API class
api_instance = criteo_marketing.SellersV2Api(criteo_marketing.ApiClient(configuration))
seller_campaign_id = 'seller_campaign_id_example' # str | Id of the existing seller campaign to update
bid = 3.4 # float | The new bid for the seller campaign.
authorization = 'Bearer VALID_JWT_TOKEN_BASE64' # str | JWT Bearer Token (default to 'Bearer VALID_JWT_TOKEN_BASE64')

try:
    # Update an existing seller campaign.
    api_response = api_instance.update_seller_campaign(seller_campaign_id, bid, authorization)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SellersV2Api->update_seller_campaign: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **seller_campaign_id** | **str**| Id of the existing seller campaign to update | 
 **bid** | **float**| The new bid for the seller campaign. | 
 **authorization** | **str**| JWT Bearer Token | [default to &#39;Bearer VALID_JWT_TOKEN_BASE64&#39;]

### Return type

[**SellerCampaignMessage**](SellerCampaignMessage.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | List of errors encountered |  -  |
**401** | Authentication failed. |  -  |
**403** | You do not have access to the requested records |  -  |
**429** | Throttling failure. Maximum sending rate exceeded. |  -  |
**500** | Unknown error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_seller_campaigns**
> list[SellerCampaignMessage] update_seller_campaigns(authorization, campaign_messages)

Update a collection of seller campaigns.

Patching a collection of seller campaigns allows their bids to be modified.  Each bid must be a non-negative value. Setting the bid to zero will make a seller campaign inactive.                The currency used for bids will be the default currency of the campaign.

### Example

* Api Key Authentication (Authorization):
```python
from __future__ import print_function
import time
import criteo_marketing
from criteo_marketing.rest import ApiException
from pprint import pprint
configuration = criteo_marketing.Configuration()
# Configure API key authorization: Authorization
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to https://api.criteo.com/marketing
configuration.host = "https://api.criteo.com/marketing"
# Create an instance of the API class
api_instance = criteo_marketing.SellersV2Api(criteo_marketing.ApiClient(configuration))
authorization = 'Bearer VALID_JWT_TOKEN_BASE64' # str | JWT Bearer Token (default to 'Bearer VALID_JWT_TOKEN_BASE64')
campaign_messages = [criteo_marketing.SellerCampaignUpdate()] # list[SellerCampaignUpdate] | 

try:
    # Update a collection of seller campaigns.
    api_response = api_instance.update_seller_campaigns(authorization, campaign_messages)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SellersV2Api->update_seller_campaigns: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| JWT Bearer Token | [default to &#39;Bearer VALID_JWT_TOKEN_BASE64&#39;]
 **campaign_messages** | [**list[SellerCampaignUpdate]**](SellerCampaignUpdate.md)|  | 

### Return type

[**list[SellerCampaignMessage]**](SellerCampaignMessage.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded, text/html
 - **Accept**: application/json, text/json, application/xml, text/xml, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | List of errors encountered |  -  |
**401** | Authentication failed. |  -  |
**403** | You do not have access to the requested records |  -  |
**429** | Throttling failure. Maximum sending rate exceeded. |  -  |
**500** | Unknown error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

