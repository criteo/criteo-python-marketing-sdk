# criteo_marketing.CampaignsApi

All URIs are relative to *https://api.criteo.com/marketing*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_bids**](CampaignsApi.md#get_bids) | **GET** /v1/campaigns/bids | Gets a the bids for campaigns and their categories
[**get_campaign**](CampaignsApi.md#get_campaign) | **GET** /v1/campaigns/{campaignId} | Gets a specific campaign
[**get_campaigns**](CampaignsApi.md#get_campaigns) | **GET** /v1/campaigns | Gets campaigns
[**get_categories**](CampaignsApi.md#get_categories) | **GET** /v1/campaigns/{campaignId}/categories | Gets categories
[**get_category**](CampaignsApi.md#get_category) | **GET** /v1/campaigns/{campaignId}/categories/{categoryHashCode} | Gets a specific category
[**update_bids**](CampaignsApi.md#update_bids) | **PUT** /v1/campaigns/bids | Update bids for campaigns and their categories


# **get_bids**
> list[CampaignBidMessage] get_bids(authorization, campaign_ids=campaign_ids, advertiser_ids=advertiser_ids, category_hash_codes=category_hash_codes, bid_type=bid_type, campaign_status=campaign_status, pending_changes=pending_changes)

Gets a the bids for campaigns and their categories

Get the campaigns' bids, as well as the bids of their categories

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
api_instance = criteo_marketing.CampaignsApi(criteo_marketing.ApiClient(configuration))
authorization = 'Bearer VALID_JWT_TOKEN_BASE64' # str | JWT Bearer Token (default to 'Bearer VALID_JWT_TOKEN_BASE64')
campaign_ids = 'campaign_ids_example' # str | Optional. The ids of the campaigns we want to get the bids on. If not specified, advertiserIds will be used. (optional)
advertiser_ids = 'advertiser_ids_example' # str | Optional. The ids of the advertisers' campaigns we want to get the bids on. If campaignIds not specified, and neither is advertiserIds, all the advertisers in the user's portfolio are used. (optional)
category_hash_codes = 'category_hash_codes_example' # str | Optional. Filters only specified categories. By default no filtering is applied. (optional)
bid_type = 'bid_type_example' # str | Optional. Filters by bid type. By default no filtering is applied. (optional)
campaign_status = 'campaign_status_example' # str | Optional. Filters by campaign status. By default no filtering is applied. (optional)
pending_changes = True # bool | Optional. Filters only pending changes or settled ones. By default no filtering is applied. (optional)

try:
    # Gets a the bids for campaigns and their categories
    api_response = api_instance.get_bids(authorization, campaign_ids=campaign_ids, advertiser_ids=advertiser_ids, category_hash_codes=category_hash_codes, bid_type=bid_type, campaign_status=campaign_status, pending_changes=pending_changes)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CampaignsApi->get_bids: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| JWT Bearer Token | [default to &#39;Bearer VALID_JWT_TOKEN_BASE64&#39;]
 **campaign_ids** | **str**| Optional. The ids of the campaigns we want to get the bids on. If not specified, advertiserIds will be used. | [optional] 
 **advertiser_ids** | **str**| Optional. The ids of the advertisers&#39; campaigns we want to get the bids on. If campaignIds not specified, and neither is advertiserIds, all the advertisers in the user&#39;s portfolio are used. | [optional] 
 **category_hash_codes** | **str**| Optional. Filters only specified categories. By default no filtering is applied. | [optional] 
 **bid_type** | **str**| Optional. Filters by bid type. By default no filtering is applied. | [optional] 
 **campaign_status** | **str**| Optional. Filters by campaign status. By default no filtering is applied. | [optional] 
 **pending_changes** | **bool**| Optional. Filters only pending changes or settled ones. By default no filtering is applied. | [optional] 

### Return type

[**list[CampaignBidMessage]**](CampaignBidMessage.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Bids returned OK. |  -  |
**401** | Authentication failed. |  -  |
**403** | There is not even one valid advertiserId or campaignId requested. |  -  |
**429** | Throttling failure. Maximum sending rate exceeded. |  -  |
**500** | Unknown error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_campaign**
> CampaignMessage get_campaign(campaign_id, authorization)

Gets a specific campaign

Get a specific campaign

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
api_instance = criteo_marketing.CampaignsApi(criteo_marketing.ApiClient(configuration))
campaign_id = 56 # int | Mandatory. The id of the campaign to return.
authorization = 'Bearer VALID_JWT_TOKEN_BASE64' # str | JWT Bearer Token (default to 'Bearer VALID_JWT_TOKEN_BASE64')

try:
    # Gets a specific campaign
    api_response = api_instance.get_campaign(campaign_id, authorization)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CampaignsApi->get_campaign: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_id** | **int**| Mandatory. The id of the campaign to return. | 
 **authorization** | **str**| JWT Bearer Token | [default to &#39;Bearer VALID_JWT_TOKEN_BASE64&#39;]

### Return type

[**CampaignMessage**](CampaignMessage.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Campaign returned OK. |  -  |
**401** | Authentication failed. |  -  |
**403** | One of the requested campaigns doesn&#39;t belong to the API user&#39;s portfolio which prevents from accessing its data. |  -  |
**404** | The requested campaign was not found. |  -  |
**429** | Throttling failure. Maximum sending rate exceeded. |  -  |
**500** | Unknown error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_campaigns**
> list[CampaignMessage] get_campaigns(authorization, campaign_ids=campaign_ids, advertiser_ids=advertiser_ids, campaign_status=campaign_status, bid_type=bid_type)

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
configuration = criteo_marketing.Configuration()
# Configure API key authorization: Authorization
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to https://api.criteo.com/marketing
configuration.host = "https://api.criteo.com/marketing"
# Create an instance of the API class
api_instance = criteo_marketing.CampaignsApi(criteo_marketing.ApiClient(configuration))
authorization = 'Bearer VALID_JWT_TOKEN_BASE64' # str | JWT Bearer Token (default to 'Bearer VALID_JWT_TOKEN_BASE64')
campaign_ids = 'campaign_ids_example' # str | Optional. One or more campaign ids, E.g., 78, 12932, 45236. If the campaign ids requested are not linked to advertisers in the user's portfolio, they will be skipped. (optional)
advertiser_ids = 'advertiser_ids_example' # str | Optional. One or more advertiser ids, E.g., 78, 12932, 45236. If the advertiser ids requested are not part of the user's portfolio, they will be skipped. (optional)
campaign_status = 'campaign_status_example' # str | Optional. Filters by campaign status. By default no filtering is applied. (optional)
bid_type = 'bid_type_example' # str | Optional. Filters by campaign bid type. By default, no filtering is applied. (optional)

try:
    # Gets campaigns
    api_response = api_instance.get_campaigns(authorization, campaign_ids=campaign_ids, advertiser_ids=advertiser_ids, campaign_status=campaign_status, bid_type=bid_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CampaignsApi->get_campaigns: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| JWT Bearer Token | [default to &#39;Bearer VALID_JWT_TOKEN_BASE64&#39;]
 **campaign_ids** | **str**| Optional. One or more campaign ids, E.g., 78, 12932, 45236. If the campaign ids requested are not linked to advertisers in the user&#39;s portfolio, they will be skipped. | [optional] 
 **advertiser_ids** | **str**| Optional. One or more advertiser ids, E.g., 78, 12932, 45236. If the advertiser ids requested are not part of the user&#39;s portfolio, they will be skipped. | [optional] 
 **campaign_status** | **str**| Optional. Filters by campaign status. By default no filtering is applied. | [optional] 
 **bid_type** | **str**| Optional. Filters by campaign bid type. By default, no filtering is applied. | [optional] 

### Return type

[**list[CampaignMessage]**](CampaignMessage.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Campaigns returned OK. |  -  |
**400** | There is not even one valid advertiserId or campaignId requested. |  -  |
**401** | Authentication failed. |  -  |
**429** | Throttling failure. Maximum sending rate exceeded. |  -  |
**500** | Unknown error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_categories**
> CategoryMessage get_categories(campaign_id, authorization, enabled_only=enabled_only)

Gets categories

Get the list of categories linked to the requested campaign.

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
api_instance = criteo_marketing.CampaignsApi(criteo_marketing.ApiClient(configuration))
campaign_id = 56 # int | Mandatory. The id of the campaign the categories are linked to.
authorization = 'Bearer VALID_JWT_TOKEN_BASE64' # str | JWT Bearer Token (default to 'Bearer VALID_JWT_TOKEN_BASE64')
enabled_only = True # bool | Optional. Returns only categories you can bid on. Defaults to false. (optional)

try:
    # Gets categories
    api_response = api_instance.get_categories(campaign_id, authorization, enabled_only=enabled_only)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CampaignsApi->get_categories: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_id** | **int**| Mandatory. The id of the campaign the categories are linked to. | 
 **authorization** | **str**| JWT Bearer Token | [default to &#39;Bearer VALID_JWT_TOKEN_BASE64&#39;]
 **enabled_only** | **bool**| Optional. Returns only categories you can bid on. Defaults to false. | [optional] 

### Return type

[**CategoryMessage**](CategoryMessage.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Categories returned OK. |  -  |
**401** | Authentication failed. |  -  |
**403** | One of the requested campaigns doesn&#39;t belong to the API user&#39;s portfolio which prevents from accessing its data. |  -  |
**404** | The requested campaign was not found. |  -  |
**429** | Throttling failure. Maximum sending rate exceeded. |  -  |
**500** | Unknown error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_category**
> CategoryMessage get_category(campaign_id, category_hash_code, authorization)

Gets a specific category

Get a specific category linked to the requested campaign.

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
api_instance = criteo_marketing.CampaignsApi(criteo_marketing.ApiClient(configuration))
campaign_id = 56 # int | Mandatory. The id of the campaign the categories are linked to.
category_hash_code = 56 # int | Mandatory. The id of the category to return.
authorization = 'Bearer VALID_JWT_TOKEN_BASE64' # str | JWT Bearer Token (default to 'Bearer VALID_JWT_TOKEN_BASE64')

try:
    # Gets a specific category
    api_response = api_instance.get_category(campaign_id, category_hash_code, authorization)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CampaignsApi->get_category: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_id** | **int**| Mandatory. The id of the campaign the categories are linked to. | 
 **category_hash_code** | **int**| Mandatory. The id of the category to return. | 
 **authorization** | **str**| JWT Bearer Token | [default to &#39;Bearer VALID_JWT_TOKEN_BASE64&#39;]

### Return type

[**CategoryMessage**](CategoryMessage.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Category returned OK. |  -  |
**401** | Authentication failed. |  -  |
**403** | One of the requested campaigns doesn&#39;t belong to the API user&#39;s portfolio which prevents from accessing its data. |  -  |
**404** | The requested category was not found for the campaign. |  -  |
**429** | Throttling failure. Maximum sending rate exceeded. |  -  |
**500** | Unknown error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_bids**
> list[CampaignMessage] update_bids(authorization, bid_changes)

Update bids for campaigns and their categories

If a campaign bid is updated, all (if any) category bids for this campaign will be updated with the new value if they are initially equal to the campaign bid.  If the category bid is not wanted to be cascaded to the categories with the same bid value, new change bids must be added in the request for the categories where the value should be kept (with the initial value).

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
api_instance = criteo_marketing.CampaignsApi(criteo_marketing.ApiClient(configuration))
authorization = 'Bearer VALID_JWT_TOKEN_BASE64' # str | JWT Bearer Token (default to 'Bearer VALID_JWT_TOKEN_BASE64')
bid_changes = [criteo_marketing.CampaignBidChangeRequest()] # list[CampaignBidChangeRequest] | Specifies the list of bid changes to be applied.

try:
    # Update bids for campaigns and their categories
    api_response = api_instance.update_bids(authorization, bid_changes)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CampaignsApi->update_bids: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| JWT Bearer Token | [default to &#39;Bearer VALID_JWT_TOKEN_BASE64&#39;]
 **bid_changes** | [**list[CampaignBidChangeRequest]**](CampaignBidChangeRequest.md)| Specifies the list of bid changes to be applied. | 

### Return type

[**list[CampaignMessage]**](CampaignMessage.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded, text/html
 - **Accept**: application/json, text/json, application/xml, text/xml, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Campaign bids updated OK. |  -  |
**400** | Invalid input. Please check returned message for details. |  -  |
**401** | Authentication failed. |  -  |
**429** | Throttling failure. Maximum sending rate exceeded. |  -  |
**500** | Unknown error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

