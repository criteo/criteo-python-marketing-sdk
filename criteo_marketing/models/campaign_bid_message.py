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


class CampaignBidMessage(object):
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
        'campaign_name': 'str',
        'campaign_bid': 'BidMessage',
        'categories': 'list[CategoryBidMessage]',
        'campaign_status': 'str'
    }

    attribute_map = {
        'campaign_id': 'campaignId',
        'campaign_name': 'campaignName',
        'campaign_bid': 'campaignBid',
        'categories': 'categories',
        'campaign_status': 'campaignStatus'
    }

    def __init__(self, campaign_id=None, campaign_name=None, campaign_bid=None, categories=None, campaign_status=None):  # noqa: E501
        """CampaignBidMessage - a model defined in OpenAPI"""  # noqa: E501

        self._campaign_id = None
        self._campaign_name = None
        self._campaign_bid = None
        self._categories = None
        self._campaign_status = None
        self.discriminator = None

        if campaign_id is not None:
            self.campaign_id = campaign_id
        if campaign_name is not None:
            self.campaign_name = campaign_name
        if campaign_bid is not None:
            self.campaign_bid = campaign_bid
        if categories is not None:
            self.categories = categories
        if campaign_status is not None:
            self.campaign_status = campaign_status

    @property
    def campaign_id(self):
        """Gets the campaign_id of this CampaignBidMessage.  # noqa: E501


        :return: The campaign_id of this CampaignBidMessage.  # noqa: E501
        :rtype: int
        """
        return self._campaign_id

    @campaign_id.setter
    def campaign_id(self, campaign_id):
        """Sets the campaign_id of this CampaignBidMessage.


        :param campaign_id: The campaign_id of this CampaignBidMessage.  # noqa: E501
        :type: int
        """

        self._campaign_id = campaign_id

    @property
    def campaign_name(self):
        """Gets the campaign_name of this CampaignBidMessage.  # noqa: E501


        :return: The campaign_name of this CampaignBidMessage.  # noqa: E501
        :rtype: str
        """
        return self._campaign_name

    @campaign_name.setter
    def campaign_name(self, campaign_name):
        """Sets the campaign_name of this CampaignBidMessage.


        :param campaign_name: The campaign_name of this CampaignBidMessage.  # noqa: E501
        :type: str
        """

        self._campaign_name = campaign_name

    @property
    def campaign_bid(self):
        """Gets the campaign_bid of this CampaignBidMessage.  # noqa: E501


        :return: The campaign_bid of this CampaignBidMessage.  # noqa: E501
        :rtype: BidMessage
        """
        return self._campaign_bid

    @campaign_bid.setter
    def campaign_bid(self, campaign_bid):
        """Sets the campaign_bid of this CampaignBidMessage.


        :param campaign_bid: The campaign_bid of this CampaignBidMessage.  # noqa: E501
        :type: BidMessage
        """

        self._campaign_bid = campaign_bid

    @property
    def categories(self):
        """Gets the categories of this CampaignBidMessage.  # noqa: E501


        :return: The categories of this CampaignBidMessage.  # noqa: E501
        :rtype: list[CategoryBidMessage]
        """
        return self._categories

    @categories.setter
    def categories(self, categories):
        """Sets the categories of this CampaignBidMessage.


        :param categories: The categories of this CampaignBidMessage.  # noqa: E501
        :type: list[CategoryBidMessage]
        """

        self._categories = categories

    @property
    def campaign_status(self):
        """Gets the campaign_status of this CampaignBidMessage.  # noqa: E501


        :return: The campaign_status of this CampaignBidMessage.  # noqa: E501
        :rtype: str
        """
        return self._campaign_status

    @campaign_status.setter
    def campaign_status(self, campaign_status):
        """Sets the campaign_status of this CampaignBidMessage.


        :param campaign_status: The campaign_status of this CampaignBidMessage.  # noqa: E501
        :type: str
        """

        self._campaign_status = campaign_status

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
        if not isinstance(other, CampaignBidMessage):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
