# criteo_marketing.StatisticsApi

All URIs are relative to *https://api.criteo.com/marketing*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_stats**](StatisticsApi.md#get_stats) | **POST** /v1/statistics | Generates a statistics report


# **get_stats**
> str get_stats(authorization, stats_query)

Generates a statistics report

<b>ReportType</b>: The type of report to generate. Possible values: CampaignPerformance, FacebookDPA, TransactionID. <i>(mandatory)</i><br /><b>AdvertiserIds</b>: The list of advertiser ids, comma-separated. Advertisers not in your portfolio will be skipped. If not present, all the advertisers in the portfolio will be used. <i>(optional)</i><br /><b>StartDate, EndDate</b>: Start date (beginning of day) and end date (end of day) to be used for the report generation. Format to use: yyyy-MM-dd (e.g. 2017-10-30). <i>(mandatory)</i><br /><b>Dimensions</b>: The dimensions to be used in the report. Between one and three. Possible values: CampaignId, AdvertiserId, Category, Hour, Day, Week, Month, Year. <i>(mandatory)</i><br /><b>Metrics</b>: The metrics to be used in the report. For a list of possible values, please see the full documentation. <i>(mandatory)</i><br /><b>Format</b>: The file format of the generated report. Possible values: Csv, Excel, Xml, Json <i>(mandatory)</i><br /><b>Currency</b>: The currency to be used in the report. Three-letter capitals. For a list of possible values, please see the full documentation. If not set, the user's preference setting will be used. <i>(optional)</i><br /><b>Timezone</b>: Timezone to be used in the report. Possible values: GMT, PST, JST. If not set, the user's preference setting will be used. <i>(optional)</i><br /><b>IgnoreXDevice</b>: Ignore cross-device data. Also can explicitly set to null for TransactionID ReportType to get all data. Defaults to false. <i>(optional)</i><br /><h4>Functional cases</h4>              Statistic export in a file might be corrupted through Swagger. It's recommended to access this file through a CURL request or other programmatic methods.              <h4>Validation rules</h4>              StartDate and EndDate are mandatory.<br />              StartDate should come before, or be equal to EndDate.<br />              The requested dimensions must be in a supported combination.<br />              At least one metric must be provided.<br />              All metrics must be supported.<br />              The selected advertisers must have at least one campaign.<br />              Seller dimension is not supported.<br /><h4>Response custom headers</h4>              If you are asking for a CampaignPerformance report and sales metrics are late, response will have a custom header <b>latest-available-sales</b>, a datetime with format <b>yyyy-MM-dd HH:mm</b> using the requested timezone.

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
api_instance = criteo_marketing.StatisticsApi(criteo_marketing.ApiClient(configuration))
authorization = 'Bearer VALID_JWT_TOKEN_BASE64' # str | JWT Bearer Token (default to 'Bearer VALID_JWT_TOKEN_BASE64')
stats_query = criteo_marketing.StatsQueryMessageEx() # StatsQueryMessageEx | The report query details

try:
    # Generates a statistics report
    api_response = api_instance.get_stats(authorization, stats_query)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatisticsApi->get_stats: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| JWT Bearer Token | [default to &#39;Bearer VALID_JWT_TOKEN_BASE64&#39;]
 **stats_query** | [**StatsQueryMessageEx**](StatsQueryMessageEx.md)| The report query details | 

### Return type

**str**

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded, text/html
 - **Accept**: application/json, text/json, application/xml, text/xml, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Statistics report generated OK. |  -  |
**400** | Bad request, invalid syntax or validation error. |  -  |
**401** | Authentication failed. |  -  |
**403** | No campaigns found. |  -  |
**429** | Throttling failure. Maximum sending rate exceeded. |  -  |
**500** | Unknown error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

