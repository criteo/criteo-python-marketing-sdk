# coding: utf-8

"""
    Marketing API v.1.0

    IMPORTANT: This swagger links to Criteo production environment. Any test applied here will thus impact real campaigns.  # noqa: E501

    OpenAPI spec version: v.1.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from criteo_marketing.api_client import ApiClient


class StatisticsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_stats(self, authorization, stats_query_message_ex, **kwargs):  # noqa: E501
        """Generates a statistics report  # noqa: E501

        <b>ReportType</b>: The type of report to generate. Possible values: CampaignPerformance, FacebookDPA, TransactionID. <i>(mandatory)</i><br /><b>AdvertiserIds</b>: The list of advertiser ids, comma-separated. Advertisers not in your portfolio will be skipped. If not present, all the advertisers in the portfolio will be used. <i>(optional)</i><br /><b>StartDate, EndDate</b>: Start date (beginning of day) and end date (end of day) to be used for the report generation. Format to use: yyyy-MM-dd (e.g. 2017-10-30). <i>(mandatory)</i><br /><b>Dimensions</b>: The dimensions to be used in the report. Between one and three. Possible values: CampaignId, AdvertiserId, Category, Hour, Day, Week, Month, Year. <i>(mandatory)</i><br /><b>Metrics</b>: The metrics to be used in the report. For a list of possible values, please see the full documentation. <i>(mandatory)</i><br /><b>Format</b>: The file format of the generated report. Possible values: Csv, Excel, Xml, Json <i>(mandatory)</i><br /><b>Currency</b>: The currency to be used in the report. Three-letter capitals. For a list of possible values, please see the full documentation. If not set, the user's preference setting will be used. <i>(optional)</i><br /><b>Timezone</b>: Timezone to be used in the report. Possible values: GMT, PST, JST. If not set, the user's preference setting will be used. <i>(optional)</i><br /><b>IgnoreXDevice</b>: Ignore cross-device data. Also can explicitly set to null for TransactionID ReportType to get all data. Defaults to false. <i>(optional)</i><br /><h4>Functional cases</h4>              Statistic export in a file might be corrupted through Swagger. It's recommended to access this file through a CURL request or other programmatic methods.              <h4>Validation rules</h4>              StartDate and EndDate are mandatory.<br />              StartDate should come before, or be equal to EndDate.<br />              The requested dimensions must be in a supported combination.<br />              At least one metric must be provided.<br />              All metrics must be supported.<br />              The selected advertisers must have at least one campaign.<br />              Seller dimension is not supported.<br /><h4>Response custom headers</h4>              If you are asking for a CampaignPerformance report and sales metrics are late, response will have a custom header <b>latest-available-sales</b>, a datetime with format <b>yyyy-MM-dd HH:mm</b> using the requested timezone.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_stats(authorization, stats_query_message_ex, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str authorization: JWT Bearer Token (required)
        :param StatsQueryMessageEx stats_query_message_ex: The report query details (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_stats_with_http_info(authorization, stats_query_message_ex, **kwargs)  # noqa: E501
        else:
            (data) = self.get_stats_with_http_info(authorization, stats_query_message_ex, **kwargs)  # noqa: E501
            return data

    def get_stats_with_http_info(self, authorization, stats_query_message_ex, **kwargs):  # noqa: E501
        """Generates a statistics report  # noqa: E501

        <b>ReportType</b>: The type of report to generate. Possible values: CampaignPerformance, FacebookDPA, TransactionID. <i>(mandatory)</i><br /><b>AdvertiserIds</b>: The list of advertiser ids, comma-separated. Advertisers not in your portfolio will be skipped. If not present, all the advertisers in the portfolio will be used. <i>(optional)</i><br /><b>StartDate, EndDate</b>: Start date (beginning of day) and end date (end of day) to be used for the report generation. Format to use: yyyy-MM-dd (e.g. 2017-10-30). <i>(mandatory)</i><br /><b>Dimensions</b>: The dimensions to be used in the report. Between one and three. Possible values: CampaignId, AdvertiserId, Category, Hour, Day, Week, Month, Year. <i>(mandatory)</i><br /><b>Metrics</b>: The metrics to be used in the report. For a list of possible values, please see the full documentation. <i>(mandatory)</i><br /><b>Format</b>: The file format of the generated report. Possible values: Csv, Excel, Xml, Json <i>(mandatory)</i><br /><b>Currency</b>: The currency to be used in the report. Three-letter capitals. For a list of possible values, please see the full documentation. If not set, the user's preference setting will be used. <i>(optional)</i><br /><b>Timezone</b>: Timezone to be used in the report. Possible values: GMT, PST, JST. If not set, the user's preference setting will be used. <i>(optional)</i><br /><b>IgnoreXDevice</b>: Ignore cross-device data. Also can explicitly set to null for TransactionID ReportType to get all data. Defaults to false. <i>(optional)</i><br /><h4>Functional cases</h4>              Statistic export in a file might be corrupted through Swagger. It's recommended to access this file through a CURL request or other programmatic methods.              <h4>Validation rules</h4>              StartDate and EndDate are mandatory.<br />              StartDate should come before, or be equal to EndDate.<br />              The requested dimensions must be in a supported combination.<br />              At least one metric must be provided.<br />              All metrics must be supported.<br />              The selected advertisers must have at least one campaign.<br />              Seller dimension is not supported.<br /><h4>Response custom headers</h4>              If you are asking for a CampaignPerformance report and sales metrics are late, response will have a custom header <b>latest-available-sales</b>, a datetime with format <b>yyyy-MM-dd HH:mm</b> using the requested timezone.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_stats_with_http_info(authorization, stats_query_message_ex, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str authorization: JWT Bearer Token (required)
        :param StatsQueryMessageEx stats_query_message_ex: The report query details (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['authorization', 'stats_query_message_ex']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_stats" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'authorization' is set
        if ('authorization' not in local_var_params or
                local_var_params['authorization'] is None):
            raise ValueError("Missing the required parameter `authorization` when calling `get_stats`")  # noqa: E501
        # verify the required parameter 'stats_query_message_ex' is set
        if ('stats_query_message_ex' not in local_var_params or
                local_var_params['stats_query_message_ex'] is None):
            raise ValueError("Missing the required parameter `stats_query_message_ex` when calling `get_stats`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'authorization' in local_var_params:
            header_params['Authorization'] = local_var_params['authorization']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'stats_query_message_ex' in local_var_params:
            body_params = local_var_params['stats_query_message_ex']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'text/json', 'application/xml', 'text/xml', 'text/html'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'text/json', 'application/xml', 'text/xml', 'application/x-www-form-urlencoded', 'text/html'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Authorization']  # noqa: E501

        return self.api_client.call_api(
            '/v1/statistics', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='str',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)
