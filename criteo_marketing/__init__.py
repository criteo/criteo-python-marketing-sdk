# coding: utf-8

# flake8: noqa

"""
    Marketing API v.1.0

    IMPORTANT: This swagger links to Criteo production environment. Any test applied here will thus impact real campaigns.  # noqa: E501

    The version of the OpenAPI document: v.1.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

__version__ = "1.0.171"

# import apis into sdk package
from criteo_marketing.api.advertisers_api import AdvertisersApi
from criteo_marketing.api.audiences_api import AudiencesApi
from criteo_marketing.api.authentication_api import AuthenticationApi
from criteo_marketing.api.budgets_api import BudgetsApi
from criteo_marketing.api.campaigns_api import CampaignsApi
from criteo_marketing.api.categories_api import CategoriesApi
from criteo_marketing.api.portfolio_api import PortfolioApi
from criteo_marketing.api.publishers_api import PublishersApi
from criteo_marketing.api.sellers_api import SellersApi
from criteo_marketing.api.sellers_v2_api import SellersV2Api
from criteo_marketing.api.sellers_v2_stats_api import SellersV2StatsApi
from criteo_marketing.api.statistics_api import StatisticsApi

# import ApiClient
from criteo_marketing.api_client import ApiClient
from criteo_marketing.configuration import Configuration
from criteo_marketing.exceptions import OpenApiException
from criteo_marketing.exceptions import ApiTypeError
from criteo_marketing.exceptions import ApiValueError
from criteo_marketing.exceptions import ApiKeyError
from criteo_marketing.exceptions import ApiException
# import models into sdk package
from criteo_marketing.models.advertiser_campaign_message import AdvertiserCampaignMessage
from criteo_marketing.models.advertiser_info_message import AdvertiserInfoMessage
from criteo_marketing.models.advertiser_quota_message import AdvertiserQuotaMessage
from criteo_marketing.models.audience_create_request import AudienceCreateRequest
from criteo_marketing.models.audience_create_response import AudienceCreateResponse
from criteo_marketing.models.audience_patch_request import AudiencePatchRequest
from criteo_marketing.models.audience_patch_response import AudiencePatchResponse
from criteo_marketing.models.audience_put_request import AudiencePutRequest
from criteo_marketing.models.audience_response import AudienceResponse
from criteo_marketing.models.audiences_get_response import AudiencesGetResponse
from criteo_marketing.models.bid_message import BidMessage
from criteo_marketing.models.budget_message import BudgetMessage
from criteo_marketing.models.campaign_bid_change_request import CampaignBidChangeRequest
from criteo_marketing.models.campaign_bid_change_response import CampaignBidChangeResponse
from criteo_marketing.models.campaign_bid_message import CampaignBidMessage
from criteo_marketing.models.campaign_message import CampaignMessage
from criteo_marketing.models.campaign_report_query_message import CampaignReportQueryMessage
from criteo_marketing.models.catalog_product import CatalogProduct
from criteo_marketing.models.catalog_product_v3 import CatalogProductV3
from criteo_marketing.models.category_bid_change_request import CategoryBidChangeRequest
from criteo_marketing.models.category_bid_message import CategoryBidMessage
from criteo_marketing.models.category_message import CategoryMessage
from criteo_marketing.models.category_update_error import CategoryUpdateError
from criteo_marketing.models.category_update_input import CategoryUpdateInput
from criteo_marketing.models.category_updates_per_catalog import CategoryUpdatesPerCatalog
from criteo_marketing.models.category_updates_per_catalog_error import CategoryUpdatesPerCatalogError
from criteo_marketing.models.check_result import CheckResult
from criteo_marketing.models.client_registration_request_message import ClientRegistrationRequestMessage
from criteo_marketing.models.client_registration_response_message import ClientRegistrationResponseMessage
from criteo_marketing.models.create_seller_budget_mapi_message import CreateSellerBudgetMapiMessage
from criteo_marketing.models.create_seller_campaign_message_mapi import CreateSellerCampaignMessageMapi
from criteo_marketing.models.custom_attribute_v3 import CustomAttributeV3
from criteo_marketing.models.error_source import ErrorSource
from criteo_marketing.models.google_product import GoogleProduct
from criteo_marketing.models.google_product_v3 import GoogleProductV3
from criteo_marketing.models.i_throttling_configuration import IThrottlingConfiguration
from criteo_marketing.models.inline_response200 import InlineResponse200
from criteo_marketing.models.installment import Installment
from criteo_marketing.models.installment_amount import InstallmentAmount
from criteo_marketing.models.installment_v3 import InstallmentV3
from criteo_marketing.models.loyalty_points_v3 import LoyaltyPointsV3
from criteo_marketing.models.loyaty_points import LoyatyPoints
from criteo_marketing.models.mapi_user_message import MapiUserMessage
from criteo_marketing.models.marketplace_campaign_message import MarketplaceCampaignMessage
from criteo_marketing.models.message_with_details_campaign_bid_change_response import MessageWithDetailsCampaignBidChangeResponse
from criteo_marketing.models.message_with_details_category_updates_per_catalog_error import MessageWithDetailsCategoryUpdatesPerCatalogError
from criteo_marketing.models.policy_route_info import PolicyRouteInfo
from criteo_marketing.models.portfolio_message import PortfolioMessage
from criteo_marketing.models.price import Price
from criteo_marketing.models.product_importer_batch import ProductImporterBatch
from criteo_marketing.models.product_importer_message import ProductImporterMessage
from criteo_marketing.models.product_shipping_dimension_v3 import ProductShippingDimensionV3
from criteo_marketing.models.product_shipping_v3 import ProductShippingV3
from criteo_marketing.models.product_shipping_weight_v3 import ProductShippingWeightV3
from criteo_marketing.models.product_tax_v3 import ProductTaxV3
from criteo_marketing.models.product_unit_pricing_base_measure_v3 import ProductUnitPricingBaseMeasureV3
from criteo_marketing.models.publisher_file_stats_message import PublisherFileStatsMessage
from criteo_marketing.models.publisher_stats_message import PublisherStatsMessage
from criteo_marketing.models.publisher_stats_query_message import PublisherStatsQueryMessage
from criteo_marketing.models.route_policy import RoutePolicy
from criteo_marketing.models.seller_base import SellerBase
from criteo_marketing.models.seller_bid_info_message import SellerBidInfoMessage
from criteo_marketing.models.seller_bids_message import SellerBidsMessage
from criteo_marketing.models.seller_budget_create_message import SellerBudgetCreateMessage
from criteo_marketing.models.seller_budget_info_message import SellerBudgetInfoMessage
from criteo_marketing.models.seller_budget_message import SellerBudgetMessage
from criteo_marketing.models.seller_budget_response_message import SellerBudgetResponseMessage
from criteo_marketing.models.seller_budget_update_message import SellerBudgetUpdateMessage
from criteo_marketing.models.seller_budgets_create_message import SellerBudgetsCreateMessage
from criteo_marketing.models.seller_budgets_message import SellerBudgetsMessage
from criteo_marketing.models.seller_budgets_update_message import SellerBudgetsUpdateMessage
from criteo_marketing.models.seller_campaign_message import SellerCampaignMessage
from criteo_marketing.models.seller_campaign_update import SellerCampaignUpdate
from criteo_marketing.models.seller_info_message import SellerInfoMessage
from criteo_marketing.models.seller_message import SellerMessage
from criteo_marketing.models.service_status_check_result import ServiceStatusCheckResult
from criteo_marketing.models.shipping import Shipping
from criteo_marketing.models.shipping_size import ShippingSize
from criteo_marketing.models.stats_query_message import StatsQueryMessage
from criteo_marketing.models.stats_query_message_ex import StatsQueryMessageEx
from criteo_marketing.models.tax import Tax
from criteo_marketing.models.throttle_policy import ThrottlePolicy
from criteo_marketing.models.throttle_policy_rates import ThrottlePolicyRates
from criteo_marketing.models.unit_measure import UnitMeasure
from criteo_marketing.models.update_seller_budget_message import UpdateSellerBudgetMessage
from criteo_marketing.models.update_seller_budget_message_base import UpdateSellerBudgetMessageBase

