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


class SellerBudgetsMessage(object):
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
        'seller_budgets': 'list[SellerBudgetResponseMessage]'
    }

    attribute_map = {
        'campaign_id': 'campaignId',
        'seller_budgets': 'sellerBudgets'
    }

    def __init__(self, campaign_id=None, seller_budgets=None):  # noqa: E501
        """SellerBudgetsMessage - a model defined in OpenAPI"""  # noqa: E501

        self._campaign_id = None
        self._seller_budgets = None
        self.discriminator = None

        if campaign_id is not None:
            self.campaign_id = campaign_id
        if seller_budgets is not None:
            self.seller_budgets = seller_budgets

    @property
    def campaign_id(self):
        """Gets the campaign_id of this SellerBudgetsMessage.  # noqa: E501


        :return: The campaign_id of this SellerBudgetsMessage.  # noqa: E501
        :rtype: int
        """
        return self._campaign_id

    @campaign_id.setter
    def campaign_id(self, campaign_id):
        """Sets the campaign_id of this SellerBudgetsMessage.


        :param campaign_id: The campaign_id of this SellerBudgetsMessage.  # noqa: E501
        :type: int
        """

        self._campaign_id = campaign_id

    @property
    def seller_budgets(self):
        """Gets the seller_budgets of this SellerBudgetsMessage.  # noqa: E501


        :return: The seller_budgets of this SellerBudgetsMessage.  # noqa: E501
        :rtype: list[SellerBudgetResponseMessage]
        """
        return self._seller_budgets

    @seller_budgets.setter
    def seller_budgets(self, seller_budgets):
        """Sets the seller_budgets of this SellerBudgetsMessage.


        :param seller_budgets: The seller_budgets of this SellerBudgetsMessage.  # noqa: E501
        :type: list[SellerBudgetResponseMessage]
        """

        self._seller_budgets = seller_budgets

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
        if not isinstance(other, SellerBudgetsMessage):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
