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


class SellerBidsMessage(object):
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
        'seller_bids': 'list[SellerBidInfoMessage]'
    }

    attribute_map = {
        'campaign_id': 'campaignId',
        'seller_bids': 'sellerBids'
    }

    def __init__(self, campaign_id=None, seller_bids=None):  # noqa: E501
        """SellerBidsMessage - a model defined in OpenAPI"""  # noqa: E501

        self._campaign_id = None
        self._seller_bids = None
        self.discriminator = None

        if campaign_id is not None:
            self.campaign_id = campaign_id
        if seller_bids is not None:
            self.seller_bids = seller_bids

    @property
    def campaign_id(self):
        """Gets the campaign_id of this SellerBidsMessage.  # noqa: E501


        :return: The campaign_id of this SellerBidsMessage.  # noqa: E501
        :rtype: int
        """
        return self._campaign_id

    @campaign_id.setter
    def campaign_id(self, campaign_id):
        """Sets the campaign_id of this SellerBidsMessage.


        :param campaign_id: The campaign_id of this SellerBidsMessage.  # noqa: E501
        :type: int
        """

        self._campaign_id = campaign_id

    @property
    def seller_bids(self):
        """Gets the seller_bids of this SellerBidsMessage.  # noqa: E501


        :return: The seller_bids of this SellerBidsMessage.  # noqa: E501
        :rtype: list[SellerBidInfoMessage]
        """
        return self._seller_bids

    @seller_bids.setter
    def seller_bids(self, seller_bids):
        """Sets the seller_bids of this SellerBidsMessage.


        :param seller_bids: The seller_bids of this SellerBidsMessage.  # noqa: E501
        :type: list[SellerBidInfoMessage]
        """

        self._seller_bids = seller_bids

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
        if not isinstance(other, SellerBidsMessage):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
