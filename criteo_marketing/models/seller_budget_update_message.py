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


class SellerBudgetUpdateMessage(object):
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
        'budget_id': 'int',
        'amount': 'float',
        'end_date': 'datetime',
        'status': 'str'
    }

    attribute_map = {
        'budget_id': 'budgetId',
        'amount': 'amount',
        'end_date': 'endDate',
        'status': 'status'
    }

    def __init__(self, budget_id=None, amount=None, end_date=None, status=None):  # noqa: E501
        """SellerBudgetUpdateMessage - a model defined in OpenAPI"""  # noqa: E501

        self._budget_id = None
        self._amount = None
        self._end_date = None
        self._status = None
        self.discriminator = None

        if budget_id is not None:
            self.budget_id = budget_id
        if amount is not None:
            self.amount = amount
        if end_date is not None:
            self.end_date = end_date
        if status is not None:
            self.status = status

    @property
    def budget_id(self):
        """Gets the budget_id of this SellerBudgetUpdateMessage.  # noqa: E501


        :return: The budget_id of this SellerBudgetUpdateMessage.  # noqa: E501
        :rtype: int
        """
        return self._budget_id

    @budget_id.setter
    def budget_id(self, budget_id):
        """Sets the budget_id of this SellerBudgetUpdateMessage.


        :param budget_id: The budget_id of this SellerBudgetUpdateMessage.  # noqa: E501
        :type: int
        """

        self._budget_id = budget_id

    @property
    def amount(self):
        """Gets the amount of this SellerBudgetUpdateMessage.  # noqa: E501


        :return: The amount of this SellerBudgetUpdateMessage.  # noqa: E501
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this SellerBudgetUpdateMessage.


        :param amount: The amount of this SellerBudgetUpdateMessage.  # noqa: E501
        :type: float
        """

        self._amount = amount

    @property
    def end_date(self):
        """Gets the end_date of this SellerBudgetUpdateMessage.  # noqa: E501


        :return: The end_date of this SellerBudgetUpdateMessage.  # noqa: E501
        :rtype: datetime
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """Sets the end_date of this SellerBudgetUpdateMessage.


        :param end_date: The end_date of this SellerBudgetUpdateMessage.  # noqa: E501
        :type: datetime
        """

        self._end_date = end_date

    @property
    def status(self):
        """Gets the status of this SellerBudgetUpdateMessage.  # noqa: E501


        :return: The status of this SellerBudgetUpdateMessage.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this SellerBudgetUpdateMessage.


        :param status: The status of this SellerBudgetUpdateMessage.  # noqa: E501
        :type: str
        """

        self._status = status

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
        if not isinstance(other, SellerBudgetUpdateMessage):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
