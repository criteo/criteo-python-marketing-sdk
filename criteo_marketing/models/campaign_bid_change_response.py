# coding: utf-8

"""
    Marketing API v.1.0

    IMPORTANT: This swagger links to Criteo production environment. Any test applied here will thus impact real campaigns.  # noqa: E501

    The version of the OpenAPI document: v.1.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class CampaignBidChangeResponse(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'campaign_id': 'int',
        'error_code': 'str',
        'error_message': 'str',
        'categories': 'list[CategoryUpdateError]'
    }

    attribute_map = {
        'campaign_id': 'campaignId',
        'error_code': 'errorCode',
        'error_message': 'errorMessage',
        'categories': 'categories'
    }

    def __init__(self, campaign_id=None, error_code=None, error_message=None, categories=None):  # noqa: E501
        """CampaignBidChangeResponse - a model defined in OpenAPI"""  # noqa: E501

        self._campaign_id = None
        self._error_code = None
        self._error_message = None
        self._categories = None
        self.discriminator = None

        if campaign_id is not None:
            self.campaign_id = campaign_id
        if error_code is not None:
            self.error_code = error_code
        if error_message is not None:
            self.error_message = error_message
        if categories is not None:
            self.categories = categories

    @property
    def campaign_id(self):
        """Gets the campaign_id of this CampaignBidChangeResponse.  # noqa: E501


        :return: The campaign_id of this CampaignBidChangeResponse.  # noqa: E501
        :rtype: int
        """
        return self._campaign_id

    @campaign_id.setter
    def campaign_id(self, campaign_id):
        """Sets the campaign_id of this CampaignBidChangeResponse.


        :param campaign_id: The campaign_id of this CampaignBidChangeResponse.  # noqa: E501
        :type: int
        """

        self._campaign_id = campaign_id

    @property
    def error_code(self):
        """Gets the error_code of this CampaignBidChangeResponse.  # noqa: E501


        :return: The error_code of this CampaignBidChangeResponse.  # noqa: E501
        :rtype: str
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        """Sets the error_code of this CampaignBidChangeResponse.


        :param error_code: The error_code of this CampaignBidChangeResponse.  # noqa: E501
        :type: str
        """

        self._error_code = error_code

    @property
    def error_message(self):
        """Gets the error_message of this CampaignBidChangeResponse.  # noqa: E501


        :return: The error_message of this CampaignBidChangeResponse.  # noqa: E501
        :rtype: str
        """
        return self._error_message

    @error_message.setter
    def error_message(self, error_message):
        """Sets the error_message of this CampaignBidChangeResponse.


        :param error_message: The error_message of this CampaignBidChangeResponse.  # noqa: E501
        :type: str
        """

        self._error_message = error_message

    @property
    def categories(self):
        """Gets the categories of this CampaignBidChangeResponse.  # noqa: E501


        :return: The categories of this CampaignBidChangeResponse.  # noqa: E501
        :rtype: list[CategoryUpdateError]
        """
        return self._categories

    @categories.setter
    def categories(self, categories):
        """Sets the categories of this CampaignBidChangeResponse.


        :param categories: The categories of this CampaignBidChangeResponse.  # noqa: E501
        :type: list[CategoryUpdateError]
        """

        self._categories = categories

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, CampaignBidChangeResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
