# criteo_marketing.PublishersApi

All URIs are relative to *https://api.criteo.com/marketing*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_stats**](PublishersApi.md#get_stats) | **POST** /v1/publishers/stats | 


# **get_stats**
> list[PublisherStatsMessage] get_stats(authorization, query_message)



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
api_instance = criteo_marketing.PublishersApi(criteo_marketing.ApiClient(configuration))
authorization = 'Bearer VALID_JWT_TOKEN_BASE64' # str | JWT Bearer Token (default to 'Bearer VALID_JWT_TOKEN_BASE64')
query_message = criteo_marketing.PublisherStatsQueryMessage() # PublisherStatsQueryMessage | 

try:
    api_response = api_instance.get_stats(authorization, query_message)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PublishersApi->get_stats: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| JWT Bearer Token | [default to &#39;Bearer VALID_JWT_TOKEN_BASE64&#39;]
 **query_message** | [**PublisherStatsQueryMessage**](PublisherStatsQueryMessage.md)|  | 

### Return type

[**list[PublisherStatsMessage]**](PublisherStatsMessage.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded, text/html
 - **Accept**: application/json, text/json, application/xml, text/xml, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Stats returned OK. |  -  |
**401** | Authentication failed. |  -  |
**403** | API account not eligible to use this feature. |  -  |
**429** | Throttling failure. Maximum sending rate exceeded. |  -  |
**500** | Unknown error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

