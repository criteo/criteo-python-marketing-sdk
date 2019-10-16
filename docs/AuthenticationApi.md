# criteo_marketing.AuthenticationApi

All URIs are relative to *https://api.criteo.com/marketing*

Method | HTTP request | Description
------------- | ------------- | -------------
[**o_auth2_token_post**](AuthenticationApi.md#o_auth2_token_post) | **POST** /oauth2/token | Authenticates provided credentials and returns an access token


# **o_auth2_token_post**
> InlineResponse200 o_auth2_token_post(client_id=client_id, client_secret=client_secret, grant_type=grant_type)

Authenticates provided credentials and returns an access token

Get the token necessary to perform any action through our API. You can create your API User in our Criteo platform <a href='https://marketing.criteo.com' target='_blank'>here</a>. If you forgot your credentials (client_id and/or client_secret) you will need to reset them there.

### Example

```python
from __future__ import print_function
import time
import criteo_marketing
from criteo_marketing.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = criteo_marketing.AuthenticationApi()
client_id = 'client_id_example' # str | API Client-Id or Username (optional)
client_secret = 'client_secret_example' # str | API Client secret or password (optional)
grant_type = 'client_credentials' # str | Other grant types are not available (optional) (default to 'client_credentials')

try:
    # Authenticates provided credentials and returns an access token
    api_response = api_instance.o_auth2_token_post(client_id=client_id, client_secret=client_secret, grant_type=grant_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticationApi->o_auth2_token_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**| API Client-Id or Username | [optional] 
 **client_secret** | **str**| API Client secret or password | [optional] 
 **grant_type** | **str**| Other grant types are not available | [optional] [default to &#39;client_credentials&#39;]

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad request, invalid syntax |  -  |
**403** | Forbidden |  -  |
**429** | Rate limit reached |  -  |
**500** | Unknown Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

