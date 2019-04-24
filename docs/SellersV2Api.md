# criteo_marketing.SellersV2Api

All URIs are relative to *https://api.criteo.com/marketing*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_seller_budgets**](SellersV2Api.md#create_seller_budgets) | **POST** /v2/crp/budgets | 
[**get_budgets_by_seller**](SellersV2Api.md#get_budgets_by_seller) | **GET** /v2/crp/sellers/{sellerId}/budgets | 
[**get_budgets_by_seller_campaign_id**](SellersV2Api.md#get_budgets_by_seller_campaign_id) | **GET** /v2/crp/seller-campaigns/{sellerCampaignId}/budgets | 
[**get_seller**](SellersV2Api.md#get_seller) | **GET** /v2/crp/sellers/{sellerId} | 
[**get_seller_budget**](SellersV2Api.md#get_seller_budget) | **GET** /v2/crp/budgets/{budgetId} | 
[**get_seller_budgets**](SellersV2Api.md#get_seller_budgets) | **GET** /v2/crp/budgets | 
[**get_seller_campaign**](SellersV2Api.md#get_seller_campaign) | **GET** /v2/crp/seller-campaigns/{sellerCampaignId} | 
[**get_seller_campaigns**](SellersV2Api.md#get_seller_campaigns) | **GET** /v2/crp/seller-campaigns | 
[**get_seller_campaigns_by_seller**](SellersV2Api.md#get_seller_campaigns_by_seller) | **GET** /v2/crp/sellers/{sellerId}/seller-campaigns | 
[**get_sellers**](SellersV2Api.md#get_sellers) | **GET** /v2/crp/sellers | 
[**update_seller_budget**](SellersV2Api.md#update_seller_budget) | **PATCH** /v2/crp/budgets/{budgetId} | 
[**update_seller_budgets**](SellersV2Api.md#update_seller_budgets) | **PATCH** /v2/crp/budgets | 
[**update_seller_campaign**](SellersV2Api.md#update_seller_campaign) | **PATCH** /v2/crp/seller-campaigns/{sellerCampaignId} | 
[**update_seller_campaigns**](SellersV2Api.md#update_seller_campaigns) | **PATCH** /v2/crp/seller-campaigns | 


# **create_seller_budgets**
> list[SellerBudgetMessage] create_seller_budgets(authorization, create_seller_budget_mapi_message)



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
api_instance = criteo_marketing.SellersV2Api(criteo_marketing.ApiClient(configuration))
authorization = 'Bearer VALID_JWT_TOKEN_BASE64' # str | JWT Bearer Token (default to 'Bearer VALID_JWT_TOKEN_BASE64')
create_seller_budget_mapi_message = NULL # list[CreateSellerBudgetMapiMessage] | 

try:
    api_response = api_instance.create_seller_budgets(authorization, create_seller_budget_mapi_message)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SellersV2Api->create_seller_budgets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| JWT Bearer Token | [default to &#39;Bearer VALID_JWT_TOKEN_BASE64&#39;]
 **create_seller_budget_mapi_message** | [**list[CreateSellerBudgetMapiMessage]**](list.md)|  | 

### Return type

[**list[SellerBudgetMessage]**](SellerBudgetMessage.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded, text/html
 - **Accept**: application/json, text/json, application/xml, text/xml, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_budgets_by_seller**
> list[SellerBudgetMessage] get_budgets_by_seller(seller_id, authorization, status=status, with_balance=with_balance, with_spend=with_spend, end_after_date=end_after_date, start_before_date=start_before_date, campaign_id=campaign_id)



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
api_instance = criteo_marketing.SellersV2Api(criteo_marketing.ApiClient(configuration))
seller_id = 56 # int | 
authorization = 'Bearer VALID_JWT_TOKEN_BASE64' # str | JWT Bearer Token (default to 'Bearer VALID_JWT_TOKEN_BASE64')
status = 'status_example' # str |  (optional)
with_balance = True # bool |  (optional)
with_spend = True # bool |  (optional)
end_after_date = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
start_before_date = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
campaign_id = 56 # int |  (optional)

try:
    api_response = api_instance.get_budgets_by_seller(seller_id, authorization, status=status, with_balance=with_balance, with_spend=with_spend, end_after_date=end_after_date, start_before_date=start_before_date, campaign_id=campaign_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SellersV2Api->get_budgets_by_seller: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **seller_id** | **int**|  | 
 **authorization** | **str**| JWT Bearer Token | [default to &#39;Bearer VALID_JWT_TOKEN_BASE64&#39;]
 **status** | **str**|  | [optional] 
 **with_balance** | **bool**|  | [optional] 
 **with_spend** | **bool**|  | [optional] 
 **end_after_date** | **datetime**|  | [optional] 
 **start_before_date** | **datetime**|  | [optional] 
 **campaign_id** | **int**|  | [optional] 

### Return type

[**list[SellerBudgetMessage]**](SellerBudgetMessage.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_budgets_by_seller_campaign_id**
> list[SellerBudgetMessage] get_budgets_by_seller_campaign_id(seller_campaign_id, authorization, status=status, with_balance=with_balance, with_spend=with_spend, end_after_date=end_after_date, start_before_date=start_before_date)



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
api_instance = criteo_marketing.SellersV2Api(criteo_marketing.ApiClient(configuration))
seller_campaign_id = 'seller_campaign_id_example' # str | 
authorization = 'Bearer VALID_JWT_TOKEN_BASE64' # str | JWT Bearer Token (default to 'Bearer VALID_JWT_TOKEN_BASE64')
status = 'status_example' # str |  (optional)
with_balance = True # bool |  (optional)
with_spend = True # bool |  (optional)
end_after_date = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
start_before_date = '2013-10-20T19:20:30+01:00' # datetime |  (optional)

try:
    api_response = api_instance.get_budgets_by_seller_campaign_id(seller_campaign_id, authorization, status=status, with_balance=with_balance, with_spend=with_spend, end_after_date=end_after_date, start_before_date=start_before_date)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SellersV2Api->get_budgets_by_seller_campaign_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **seller_campaign_id** | **str**|  | 
 **authorization** | **str**| JWT Bearer Token | [default to &#39;Bearer VALID_JWT_TOKEN_BASE64&#39;]
 **status** | **str**|  | [optional] 
 **with_balance** | **bool**|  | [optional] 
 **with_spend** | **bool**|  | [optional] 
 **end_after_date** | **datetime**|  | [optional] 
 **start_before_date** | **datetime**|  | [optional] 

### Return type

[**list[SellerBudgetMessage]**](SellerBudgetMessage.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_seller**
> SellerBase get_seller(seller_id, authorization)



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
api_instance = criteo_marketing.SellersV2Api(criteo_marketing.ApiClient(configuration))
seller_id = 56 # int | 
authorization = 'Bearer VALID_JWT_TOKEN_BASE64' # str | JWT Bearer Token (default to 'Bearer VALID_JWT_TOKEN_BASE64')

try:
    api_response = api_instance.get_seller(seller_id, authorization)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SellersV2Api->get_seller: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **seller_id** | **int**|  | 
 **authorization** | **str**| JWT Bearer Token | [default to &#39;Bearer VALID_JWT_TOKEN_BASE64&#39;]

### Return type

[**SellerBase**](SellerBase.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_seller_budget**
> SellerBudgetMessage get_seller_budget(budget_id, authorization)



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
api_instance = criteo_marketing.SellersV2Api(criteo_marketing.ApiClient(configuration))
budget_id = 56 # int | 
authorization = 'Bearer VALID_JWT_TOKEN_BASE64' # str | JWT Bearer Token (default to 'Bearer VALID_JWT_TOKEN_BASE64')

try:
    api_response = api_instance.get_seller_budget(budget_id, authorization)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SellersV2Api->get_seller_budget: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **budget_id** | **int**|  | 
 **authorization** | **str**| JWT Bearer Token | [default to &#39;Bearer VALID_JWT_TOKEN_BASE64&#39;]

### Return type

[**SellerBudgetMessage**](SellerBudgetMessage.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_seller_budgets**
> list[SellerBudgetMessage] get_seller_budgets(authorization, status=status, with_balance=with_balance, with_spend=with_spend, end_after_date=end_after_date, start_before_date=start_before_date, campaign_id=campaign_id, seller_id=seller_id)



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
api_instance = criteo_marketing.SellersV2Api(criteo_marketing.ApiClient(configuration))
authorization = 'Bearer VALID_JWT_TOKEN_BASE64' # str | JWT Bearer Token (default to 'Bearer VALID_JWT_TOKEN_BASE64')
status = 'status_example' # str |  (optional)
with_balance = True # bool |  (optional)
with_spend = True # bool |  (optional)
end_after_date = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
start_before_date = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
campaign_id = 56 # int |  (optional)
seller_id = 56 # int |  (optional)

try:
    api_response = api_instance.get_seller_budgets(authorization, status=status, with_balance=with_balance, with_spend=with_spend, end_after_date=end_after_date, start_before_date=start_before_date, campaign_id=campaign_id, seller_id=seller_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SellersV2Api->get_seller_budgets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| JWT Bearer Token | [default to &#39;Bearer VALID_JWT_TOKEN_BASE64&#39;]
 **status** | **str**|  | [optional] 
 **with_balance** | **bool**|  | [optional] 
 **with_spend** | **bool**|  | [optional] 
 **end_after_date** | **datetime**|  | [optional] 
 **start_before_date** | **datetime**|  | [optional] 
 **campaign_id** | **int**|  | [optional] 
 **seller_id** | **int**|  | [optional] 

### Return type

[**list[SellerBudgetMessage]**](SellerBudgetMessage.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_seller_campaign**
> SellerCampaignMessage get_seller_campaign(seller_campaign_id, authorization)



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
api_instance = criteo_marketing.SellersV2Api(criteo_marketing.ApiClient(configuration))
seller_campaign_id = 'seller_campaign_id_example' # str | 
authorization = 'Bearer VALID_JWT_TOKEN_BASE64' # str | JWT Bearer Token (default to 'Bearer VALID_JWT_TOKEN_BASE64')

try:
    api_response = api_instance.get_seller_campaign(seller_campaign_id, authorization)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SellersV2Api->get_seller_campaign: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **seller_campaign_id** | **str**|  | 
 **authorization** | **str**| JWT Bearer Token | [default to &#39;Bearer VALID_JWT_TOKEN_BASE64&#39;]

### Return type

[**SellerCampaignMessage**](SellerCampaignMessage.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_seller_campaigns**
> list[SellerCampaignMessage] get_seller_campaigns(authorization, seller_status=seller_status, seller_id=seller_id, campaign_id=campaign_id, budget_status=budget_status)



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
api_instance = criteo_marketing.SellersV2Api(criteo_marketing.ApiClient(configuration))
authorization = 'Bearer VALID_JWT_TOKEN_BASE64' # str | JWT Bearer Token (default to 'Bearer VALID_JWT_TOKEN_BASE64')
seller_status = 'seller_status_example' # str |  (optional)
seller_id = 56 # int |  (optional)
campaign_id = 56 # int |  (optional)
budget_status = 'budget_status_example' # str |  (optional)

try:
    api_response = api_instance.get_seller_campaigns(authorization, seller_status=seller_status, seller_id=seller_id, campaign_id=campaign_id, budget_status=budget_status)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SellersV2Api->get_seller_campaigns: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| JWT Bearer Token | [default to &#39;Bearer VALID_JWT_TOKEN_BASE64&#39;]
 **seller_status** | **str**|  | [optional] 
 **seller_id** | **int**|  | [optional] 
 **campaign_id** | **int**|  | [optional] 
 **budget_status** | **str**|  | [optional] 

### Return type

[**list[SellerCampaignMessage]**](SellerCampaignMessage.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_seller_campaigns_by_seller**
> list[SellerCampaignMessage] get_seller_campaigns_by_seller(seller_id, authorization, seller_status=seller_status, campaign_id=campaign_id, budget_status=budget_status)



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
api_instance = criteo_marketing.SellersV2Api(criteo_marketing.ApiClient(configuration))
seller_id = 56 # int | 
authorization = 'Bearer VALID_JWT_TOKEN_BASE64' # str | JWT Bearer Token (default to 'Bearer VALID_JWT_TOKEN_BASE64')
seller_status = 'seller_status_example' # str |  (optional)
campaign_id = 56 # int |  (optional)
budget_status = 'budget_status_example' # str |  (optional)

try:
    api_response = api_instance.get_seller_campaigns_by_seller(seller_id, authorization, seller_status=seller_status, campaign_id=campaign_id, budget_status=budget_status)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SellersV2Api->get_seller_campaigns_by_seller: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **seller_id** | **int**|  | 
 **authorization** | **str**| JWT Bearer Token | [default to &#39;Bearer VALID_JWT_TOKEN_BASE64&#39;]
 **seller_status** | **str**|  | [optional] 
 **campaign_id** | **int**|  | [optional] 
 **budget_status** | **str**|  | [optional] 

### Return type

[**list[SellerCampaignMessage]**](SellerCampaignMessage.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sellers**
> list[SellerBase] get_sellers(authorization, seller_status=seller_status, with_products=with_products, with_budget_status=with_budget_status)



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
api_instance = criteo_marketing.SellersV2Api(criteo_marketing.ApiClient(configuration))
authorization = 'Bearer VALID_JWT_TOKEN_BASE64' # str | JWT Bearer Token (default to 'Bearer VALID_JWT_TOKEN_BASE64')
seller_status = 'seller_status_example' # str |  (optional)
with_products = True # bool |  (optional)
with_budget_status = 'with_budget_status_example' # str |  (optional)

try:
    api_response = api_instance.get_sellers(authorization, seller_status=seller_status, with_products=with_products, with_budget_status=with_budget_status)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SellersV2Api->get_sellers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| JWT Bearer Token | [default to &#39;Bearer VALID_JWT_TOKEN_BASE64&#39;]
 **seller_status** | **str**|  | [optional] 
 **with_products** | **bool**|  | [optional] 
 **with_budget_status** | **str**|  | [optional] 

### Return type

[**list[SellerBase]**](SellerBase.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_seller_budget**
> list[SellerBudgetMessage] update_seller_budget(budget_id, start_date, status, amount, end_date, authorization, request_body)



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
api_instance = criteo_marketing.SellersV2Api(criteo_marketing.ApiClient(configuration))
budget_id = 56 # int | 
start_date = '2013-10-20T19:20:30+01:00' # datetime | 
status = 'status_example' # str | 
amount = 'amount_example' # str | 
end_date = 'end_date_example' # str | 
authorization = 'Bearer VALID_JWT_TOKEN_BASE64' # str | JWT Bearer Token (default to 'Bearer VALID_JWT_TOKEN_BASE64')
request_body = NULL # list[int] | 

try:
    api_response = api_instance.update_seller_budget(budget_id, start_date, status, amount, end_date, authorization, request_body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SellersV2Api->update_seller_budget: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **budget_id** | **int**|  | 
 **start_date** | **datetime**|  | 
 **status** | **str**|  | 
 **amount** | **str**|  | 
 **end_date** | **str**|  | 
 **authorization** | **str**| JWT Bearer Token | [default to &#39;Bearer VALID_JWT_TOKEN_BASE64&#39;]
 **request_body** | [**list[int]**](list.md)|  | 

### Return type

[**list[SellerBudgetMessage]**](SellerBudgetMessage.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded, text/html
 - **Accept**: application/json, text/json, application/xml, text/xml, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_seller_budgets**
> list[SellerBudgetMessage] update_seller_budgets(authorization, update_seller_budget_message)



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
api_instance = criteo_marketing.SellersV2Api(criteo_marketing.ApiClient(configuration))
authorization = 'Bearer VALID_JWT_TOKEN_BASE64' # str | JWT Bearer Token (default to 'Bearer VALID_JWT_TOKEN_BASE64')
update_seller_budget_message = NULL # list[UpdateSellerBudgetMessage] | 

try:
    api_response = api_instance.update_seller_budgets(authorization, update_seller_budget_message)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SellersV2Api->update_seller_budgets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| JWT Bearer Token | [default to &#39;Bearer VALID_JWT_TOKEN_BASE64&#39;]
 **update_seller_budget_message** | [**list[UpdateSellerBudgetMessage]**](list.md)|  | 

### Return type

[**list[SellerBudgetMessage]**](SellerBudgetMessage.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded, text/html
 - **Accept**: application/json, text/json, application/xml, text/xml, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_seller_campaign**
> SellerCampaignMessage update_seller_campaign(seller_campaign_id, bid, authorization)



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
api_instance = criteo_marketing.SellersV2Api(criteo_marketing.ApiClient(configuration))
seller_campaign_id = 'seller_campaign_id_example' # str | 
bid = 3.4 # float | 
authorization = 'Bearer VALID_JWT_TOKEN_BASE64' # str | JWT Bearer Token (default to 'Bearer VALID_JWT_TOKEN_BASE64')

try:
    api_response = api_instance.update_seller_campaign(seller_campaign_id, bid, authorization)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SellersV2Api->update_seller_campaign: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **seller_campaign_id** | **str**|  | 
 **bid** | **float**|  | 
 **authorization** | **str**| JWT Bearer Token | [default to &#39;Bearer VALID_JWT_TOKEN_BASE64&#39;]

### Return type

[**SellerCampaignMessage**](SellerCampaignMessage.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_seller_campaigns**
> list[SellerCampaignMessage] update_seller_campaigns(authorization, seller_campaign_base)



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
api_instance = criteo_marketing.SellersV2Api(criteo_marketing.ApiClient(configuration))
authorization = 'Bearer VALID_JWT_TOKEN_BASE64' # str | JWT Bearer Token (default to 'Bearer VALID_JWT_TOKEN_BASE64')
seller_campaign_base = NULL # list[SellerCampaignBase] | 

try:
    api_response = api_instance.update_seller_campaigns(authorization, seller_campaign_base)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SellersV2Api->update_seller_campaigns: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| JWT Bearer Token | [default to &#39;Bearer VALID_JWT_TOKEN_BASE64&#39;]
 **seller_campaign_base** | [**list[SellerCampaignBase]**](list.md)|  | 

### Return type

[**list[SellerCampaignMessage]**](SellerCampaignMessage.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded, text/html
 - **Accept**: application/json, text/json, application/xml, text/xml, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

