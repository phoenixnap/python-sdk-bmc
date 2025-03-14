# coding: utf-8

# flake8: noqa

"""
    Locations API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0
    Contact: support@phoenixnap.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


__version__ = "2.0.5.dev"

# import apis into sdk package
from pnap_location_api.api.locations_api import LocationsApi

# import ApiClient
from pnap_location_api.api_response import ApiResponse
from pnap_location_api.api_client import ApiClient
from pnap_location_api.configuration import Configuration
from pnap_location_api.exceptions import OpenApiException
from pnap_location_api.exceptions import ApiTypeError
from pnap_location_api.exceptions import ApiValueError
from pnap_location_api.exceptions import ApiKeyError
from pnap_location_api.exceptions import ApiAttributeError
from pnap_location_api.exceptions import ApiException

# import models into sdk package
from pnap_location_api.models.error import Error
from pnap_location_api.models.location import Location
from pnap_location_api.models.location_enum import LocationEnum
from pnap_location_api.models.product_category import ProductCategory
from pnap_location_api.models.product_category_enum import ProductCategoryEnum
