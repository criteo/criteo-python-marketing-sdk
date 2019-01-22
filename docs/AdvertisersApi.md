# criteo_marketing.AdvertisersApi

All URIs are relative to *https://api.criteo.com/marketing*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_campaigns**](AdvertisersApi.md#get_campaigns) | **GET** /v1/advertisers/{advertiserId}/campaigns | Gets all advertiser&#39;s campaigns
[**get_categories**](AdvertisersApi.md#get_categories) | **GET** /v1/advertisers/{advertiserId}/categories | Gets all advertiser&#39;s categories
[**get_category**](AdvertisersApi.md#get_category) | **GET** /v1/advertisers/{advertiserId}/categories/{categoryHashCode} | Gets a specific advertiser&#39;s category


# **get_campaigns**
> list[CampaignMessage] get_campaigns(advertiser_id, authorization)

Gets all advertiser's campaigns

Get the list of all the campaigns linked to the requested advertiser.

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
api_instance = criteo_marketing.AdvertisersApi(criteo_marketing.ApiClient(configuration))
advertiser_id = 56 # int | Mandatory. The id of the advertiser to return.
authorization = 'Bearer VALID_JWT_TOKEN_BASE64' # str | JWT Bearer Token (default to 'Bearer VALID_JWT_TOKEN_BASE64')

try:
    # Gets all advertiser's campaigns
    api_response = api_instance.get_campaigns(advertiser_id, authorization)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdvertisersApi->get_campaigns: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **advertiser_id** | **int**| Mandatory. The id of the advertiser to return. | 
 **authorization** | **str**| JWT Bearer Token | [default to &#39;Bearer VALID_JWT_TOKEN_BASE64&#39;]

### Return type

[**list[CampaignMessage]**](CampaignMessage.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_categories**
> list[CampaignMessage] get_categories(advertiser_id, authorization, enabled_only=enabled_only)

Gets all advertiser's categories

Get the list of all the categories linked to the requested advertiser.

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
api_instance = criteo_marketing.AdvertisersApi(criteo_marketing.ApiClient(configuration))
advertiser_id = 56 # int | Mandatory. The id of the advertiser to return.
authorization = 'Bearer VALID_JWT_TOKEN_BASE64' # str | JWT Bearer Token (default to 'Bearer VALID_JWT_TOKEN_BASE64')
enabled_only = True # bool | Optional. Returns only categories you can bid on. Defaults to false. (optional)

try:
    # Gets all advertiser's categories
    api_response = api_instance.get_categories(advertiser_id, authorization, enabled_only=enabled_only)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdvertisersApi->get_categories: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **advertiser_id** | **int**| Mandatory. The id of the advertiser to return. | 
 **authorization** | **str**| JWT Bearer Token | [default to &#39;Bearer VALID_JWT_TOKEN_BASE64&#39;]
 **enabled_only** | **bool**| Optional. Returns only categories you can bid on. Defaults to false. | [optional] 

### Return type

[**list[CampaignMessage]**](CampaignMessage.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_category**
> list[CampaignMessage] get_category(advertiser_id, category_hash_code, authorization)

Gets a specific advertiser's category

Get a specific category linked to the requested advertiser.

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
api_instance = criteo_marketing.AdvertisersApi(criteo_marketing.ApiClient(configuration))
advertiser_id = 56 # int | Mandatory. The id of the advertiser to return.
category_hash_code = 56 # int | Mandatory. The id of the category to return.
authorization = 'Bearer VALID_JWT_TOKEN_BASE64' # str | JWT Bearer Token (default to 'Bearer VALID_JWT_TOKEN_BASE64')

try:
    # Gets a specific advertiser's category
    api_response = api_instance.get_category(advertiser_id, category_hash_code, authorization)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdvertisersApi->get_category: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **advertiser_id** | **int**| Mandatory. The id of the advertiser to return. | 
 **category_hash_code** | **int**| Mandatory. The id of the category to return. | 
 **authorization** | **str**| JWT Bearer Token | [default to &#39;Bearer VALID_JWT_TOKEN_BASE64&#39;]

### Return type

[**list[CampaignMessage]**](CampaignMessage.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

