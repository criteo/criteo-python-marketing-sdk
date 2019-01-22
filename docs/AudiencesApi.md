# criteo_marketing.AudiencesApi

All URIs are relative to *https://api.criteo.com/marketing*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_remove_users_to_audience**](AudiencesApi.md#add_remove_users_to_audience) | **PATCH** /v1/audiences/userlist/{audienceId} | Add/Remove users to an Audience.
[**create_audience**](AudiencesApi.md#create_audience) | **POST** /v1/audiences/userlist | Create a new Audience.
[**delete_audience**](AudiencesApi.md#delete_audience) | **DELETE** /v1/audiences/{audienceId} | Delete an Audience.
[**get_audiences**](AudiencesApi.md#get_audiences) | **GET** /v1/audiences | Get the list of Audiences.
[**remove_users_from_audience**](AudiencesApi.md#remove_users_from_audience) | **DELETE** /v1/audiences/userlist/{audienceId}/users | Remove all users from an Audience.
[**update_audience_metadata**](AudiencesApi.md#update_audience_metadata) | **PUT** /v1/audiences/{audienceId} | Update an Audience metadata.


# **add_remove_users_to_audience**
> AudiencePatchResponse add_remove_users_to_audience(audience_id, authorization, audience_patch_request)

Add/Remove users to an Audience.

Add/Remove users to an Audience.

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
api_instance = criteo_marketing.AudiencesApi(criteo_marketing.ApiClient(configuration))
audience_id = 56 # int | Mandatory. The id of the audience to add or remove users to.
authorization = 'Bearer VALID_JWT_TOKEN_BASE64' # str | JWT Bearer Token (default to 'Bearer VALID_JWT_TOKEN_BASE64')
audience_patch_request = criteo_marketing.AudiencePatchRequest() # AudiencePatchRequest | Mandatory. The request to create the Audience.

try:
    # Add/Remove users to an Audience.
    api_response = api_instance.add_remove_users_to_audience(audience_id, authorization, audience_patch_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AudiencesApi->add_remove_users_to_audience: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **audience_id** | **int**| Mandatory. The id of the audience to add or remove users to. | 
 **authorization** | **str**| JWT Bearer Token | [default to &#39;Bearer VALID_JWT_TOKEN_BASE64&#39;]
 **audience_patch_request** | [**AudiencePatchRequest**](AudiencePatchRequest.md)| Mandatory. The request to create the Audience. | 

### Return type

[**AudiencePatchResponse**](AudiencePatchResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded, text/html
 - **Accept**: application/json, text/json, application/xml, text/xml, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_audience**
> AudienceCreateResponse create_audience(authorization, audience_create_request)

Create a new Audience.

Create a new Audience for the given Advertiser.

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
api_instance = criteo_marketing.AudiencesApi(criteo_marketing.ApiClient(configuration))
authorization = 'Bearer VALID_JWT_TOKEN_BASE64' # str | JWT Bearer Token (default to 'Bearer VALID_JWT_TOKEN_BASE64')
audience_create_request = criteo_marketing.AudienceCreateRequest() # AudienceCreateRequest | 

try:
    # Create a new Audience.
    api_response = api_instance.create_audience(authorization, audience_create_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AudiencesApi->create_audience: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| JWT Bearer Token | [default to &#39;Bearer VALID_JWT_TOKEN_BASE64&#39;]
 **audience_create_request** | [**AudienceCreateRequest**](AudienceCreateRequest.md)|  | 

### Return type

[**AudienceCreateResponse**](AudienceCreateResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded, text/html
 - **Accept**: application/json, text/json, application/xml, text/xml, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_audience**
> object delete_audience(audience_id, authorization)

Delete an Audience.

Delete an Audience.

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
api_instance = criteo_marketing.AudiencesApi(criteo_marketing.ApiClient(configuration))
audience_id = 56 # int | Mandatory. The id of the audience to delete.
authorization = 'Bearer VALID_JWT_TOKEN_BASE64' # str | JWT Bearer Token (default to 'Bearer VALID_JWT_TOKEN_BASE64')

try:
    # Delete an Audience.
    api_response = api_instance.delete_audience(audience_id, authorization)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AudiencesApi->delete_audience: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **audience_id** | **int**| Mandatory. The id of the audience to delete. | 
 **authorization** | **str**| JWT Bearer Token | [default to &#39;Bearer VALID_JWT_TOKEN_BASE64&#39;]

### Return type

**object**

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_audiences**
> AudiencesGetResponse get_audiences(authorization, advertiser_id=advertiser_id)

Get the list of Audiences.

Get the list of Audiences for the given Advertiser.

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
api_instance = criteo_marketing.AudiencesApi(criteo_marketing.ApiClient(configuration))
authorization = 'Bearer VALID_JWT_TOKEN_BASE64' # str | JWT Bearer Token (default to 'Bearer VALID_JWT_TOKEN_BASE64')
advertiser_id = 56 # int | Mandatory. Advertiser to get all Audiences for. (optional)

try:
    # Get the list of Audiences.
    api_response = api_instance.get_audiences(authorization, advertiser_id=advertiser_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AudiencesApi->get_audiences: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| JWT Bearer Token | [default to &#39;Bearer VALID_JWT_TOKEN_BASE64&#39;]
 **advertiser_id** | **int**| Mandatory. Advertiser to get all Audiences for. | [optional] 

### Return type

[**AudiencesGetResponse**](AudiencesGetResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_users_from_audience**
> object remove_users_from_audience(audience_id, authorization)

Remove all users from an Audience.

Remove all users from an Audience.

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
api_instance = criteo_marketing.AudiencesApi(criteo_marketing.ApiClient(configuration))
audience_id = 56 # int | Mandatory. The id of the audience to empty.
authorization = 'Bearer VALID_JWT_TOKEN_BASE64' # str | JWT Bearer Token (default to 'Bearer VALID_JWT_TOKEN_BASE64')

try:
    # Remove all users from an Audience.
    api_response = api_instance.remove_users_from_audience(audience_id, authorization)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AudiencesApi->remove_users_from_audience: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **audience_id** | **int**| Mandatory. The id of the audience to empty. | 
 **authorization** | **str**| JWT Bearer Token | [default to &#39;Bearer VALID_JWT_TOKEN_BASE64&#39;]

### Return type

**object**

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_audience_metadata**
> object update_audience_metadata(audience_id, authorization, audience_put_request)

Update an Audience metadata.

Update an Audience metadata.

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
api_instance = criteo_marketing.AudiencesApi(criteo_marketing.ApiClient(configuration))
audience_id = 56 # int | Mandatory. The id of the Audience to update.
authorization = 'Bearer VALID_JWT_TOKEN_BASE64' # str | JWT Bearer Token (default to 'Bearer VALID_JWT_TOKEN_BASE64')
audience_put_request = criteo_marketing.AudiencePutRequest() # AudiencePutRequest | Mandatory. The request to update the Audience metadata.

try:
    # Update an Audience metadata.
    api_response = api_instance.update_audience_metadata(audience_id, authorization, audience_put_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AudiencesApi->update_audience_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **audience_id** | **int**| Mandatory. The id of the Audience to update. | 
 **authorization** | **str**| JWT Bearer Token | [default to &#39;Bearer VALID_JWT_TOKEN_BASE64&#39;]
 **audience_put_request** | [**AudiencePutRequest**](AudiencePutRequest.md)| Mandatory. The request to update the Audience metadata. | 

### Return type

**object**

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded, text/html
 - **Accept**: application/json, text/json, application/xml, text/xml, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

