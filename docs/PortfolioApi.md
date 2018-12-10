# criteo_marketing.PortfolioApi

All URIs are relative to *https://api.criteo.com/marketing*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_portfolio**](PortfolioApi.md#get_portfolio) | **GET** /v1/portfolio | Gets portfolio


# **get_portfolio**
> list[PortfolioMessage] get_portfolio(authorization)

Gets portfolio

### Example
```python
from __future__ import print_function
import time
import criteo_marketing
from criteo_marketing.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = criteo_marketing.PortfolioApi()
authorization = 'Bearer VALID_JWT_TOKEN_BASE64' # str | JWT Bearer Token (default to 'Bearer VALID_JWT_TOKEN_BASE64')

try:
    # Gets portfolio
    api_response = api_instance.get_portfolio(authorization)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortfolioApi->get_portfolio: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| JWT Bearer Token | [default to &#39;Bearer VALID_JWT_TOKEN_BASE64&#39;]

### Return type

[**list[PortfolioMessage]**](PortfolioMessage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

