# coding: utf-8

"""
    Locations API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0
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


class LocationEnum(str, Enum):
    """
    The location code.
    """

    """
    allowed enum values
    """
    PHX = 'PHX'
    ASH = 'ASH'
    NLD = 'NLD'
    SGP = 'SGP'
    CHI = 'CHI'
    SEA = 'SEA'
    AUS = 'AUS'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of LocationEnum from a JSON string"""
        return cls(json.loads(json_str))


