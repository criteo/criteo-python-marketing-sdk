# criteo_marketing.BudgetsApi

All URIs are relative to *https://api.criteo.com/marketing*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get**](BudgetsApi.md#get) | **GET** /v1/budgets | Gets budgets


# **get**
> list[BudgetMessage] get(authorization, advertiser_ids=advertiser_ids, budget_ids=budget_ids, only_active_campaigns=only_active_campaigns)

Gets budgets

Get the list of budgets with the specified filters.  If an advertiser or a budget is requested but is missing from current user's portfolio, it will not be included in the list.  If neither budgets ids nor advertisers ids are provided, then the user's portfolio will be used.

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
api_instance = criteo_marketing.BudgetsApi(criteo_marketing.ApiClient(configuration))
authorization = 'Bearer VALID_JWT_TOKEN_BASE64' # str | JWT Bearer Token (default to 'Bearer VALID_JWT_TOKEN_BASE64')
advertiser_ids = 'advertiser_ids_example' # str | Optional. One or more advertiser ids, E.g. 78, 12932, 45236. If the requested advertiser ids are not part of the user's portfolio, they will be skipped. (optional)
budget_ids = 'budget_ids_example' # str | Optional. One or more budget ids, E.g. 75, 1931, 532. If the requested budget ids are not part of the user's portfolio, they will be skipped. (optional)
only_active_campaigns = True # bool | Optional. Filters by campaign status, allowing to only display active campaigns or not. Default value is true. (optional)

try:
    # Gets budgets
    api_response = api_instance.get(authorization, advertiser_ids=advertiser_ids, budget_ids=budget_ids, only_active_campaigns=only_active_campaigns)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BudgetsApi->get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| JWT Bearer Token | [default to &#39;Bearer VALID_JWT_TOKEN_BASE64&#39;]
 **advertiser_ids** | **str**| Optional. One or more advertiser ids, E.g. 78, 12932, 45236. If the requested advertiser ids are not part of the user&#39;s portfolio, they will be skipped. | [optional] 
 **budget_ids** | **str**| Optional. One or more budget ids, E.g. 75, 1931, 532. If the requested budget ids are not part of the user&#39;s portfolio, they will be skipped. | [optional] 
 **only_active_campaigns** | **bool**| Optional. Filters by campaign status, allowing to only display active campaigns or not. Default value is true. | [optional] 

### Return type

[**list[BudgetMessage]**](BudgetMessage.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

