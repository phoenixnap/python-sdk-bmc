# coding: utf-8

"""
    Billing API

    Automate your infrastructure billing with the Bare Metal Cloud Billing API. Reserve your server instances to ensure guaranteed resource availability for 12, 24, and 36 months. Retrieve your server’s rated usage for a given period and enable or disable auto-renewals.<br> <br> <span class='pnap-api-knowledge-base-link'> Knowledge base articles to help you can be found <a href='https://phoenixnap.com/kb/phoenixnap-bare-metal-cloud-billing-models' target='_blank'>here</a> </span><br> <br> <b>All URLs are relative to (https://api.phoenixnap.com/billing/v1/)</b> 

    The version of the OpenAPI document: 0.1
    Contact: support@phoenixnap.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
import pprint
import re  # noqa: F401
from enum import Enum



try:
    from typing import Self
except ImportError:
    from typing_extensions import Self


class ReservationModelEnum(str, Enum):
    """
    The reservation model.
    """

    """
    allowed enum values
    """
    ONE_MONTH_RESERVATION = 'ONE_MONTH_RESERVATION'
    TWELVE_MONTHS_RESERVATION = 'TWELVE_MONTHS_RESERVATION'
    TWENTY_FOUR_MONTHS_RESERVATION = 'TWENTY_FOUR_MONTHS_RESERVATION'
    THIRTY_SIX_MONTHS_RESERVATION = 'THIRTY_SIX_MONTHS_RESERVATION'
    FREE_TIER = 'FREE_TIER'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of ReservationModelEnum from a JSON string"""
        return cls(json.loads(json_str))


