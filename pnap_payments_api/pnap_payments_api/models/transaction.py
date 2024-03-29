# coding: utf-8

"""
    Payments API

    Payments API are currently designed to fetch Transactions only.

    The version of the OpenAPI document: 0.1
    Contact: support@phoenixnap.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from typing import Any, ClassVar, Dict, List, Optional, Union
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr
from pydantic import Field
from pnap_payments_api.models.card_payment_method_details import CardPaymentMethodDetails
from pnap_payments_api.models.transaction_metadata import TransactionMetadata
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class Transaction(BaseModel):
    """
    Transaction response model.
    """ # noqa: E501
    id: StrictStr = Field(description="The Transaction ID.")
    status: StrictStr = Field(description="The Transaction status. Status may be: SUCCESS, PROCESSING, FAILED")
    details: Optional[StrictStr] = Field(default=None, description="Details about the transaction. Contains failure reason in case of failed transactions.")
    amount: Union[StrictFloat, StrictInt] = Field(description="The transaction amount.")
    currency: StrictStr = Field(description="The transaction currency.")
    var_date: datetime = Field(description="Date and time when transaction was created.", alias="date")
    metadata: TransactionMetadata
    card_payment_method_details: CardPaymentMethodDetails = Field(alias="cardPaymentMethodDetails")
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["id", "status", "details", "amount", "currency", "date", "metadata", "cardPaymentMethodDetails"]

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True,
        "protected_namespaces": (),
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of Transaction from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * Fields in `self.additional_properties` are added to the output dict.
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={
                "additional_properties",
            },
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of metadata
        if self.metadata:
            _dict['metadata'] = self.metadata.to_dict()
        # override the default output from pydantic by calling `to_dict()` of card_payment_method_details
        if self.card_payment_method_details:
            _dict['cardPaymentMethodDetails'] = self.card_payment_method_details.to_dict()
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of Transaction from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "status": obj.get("status"),
            "details": obj.get("details"),
            "amount": obj.get("amount"),
            "currency": obj.get("currency"),
            "date": obj.get("date"),
            "metadata": TransactionMetadata.from_dict(obj.get("metadata")) if obj.get("metadata") is not None else None,
            "cardPaymentMethodDetails": CardPaymentMethodDetails.from_dict(obj.get("cardPaymentMethodDetails")) if obj.get("cardPaymentMethodDetails") is not None else None
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


