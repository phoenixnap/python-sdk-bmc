# coding: utf-8

"""
    Network Storage API

    Create, list, edit, and delete storage networks with the Network Storage API. Use storage networks to expand storage capacity on a private network. <br> <span class='pnap-api-knowledge-base-link'> Knowledge base articles to help you can be found <a href='https://phoenixnap.com/kb/bare-metal-cloud-storage' target='_blank'>here</a> </span> <br> <b>All URLs are relative to (https://api.phoenixnap.com/network-storage/v1/)</b> 

    The version of the OpenAPI document: 1.0
    Contact: support@phoenixnap.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel, field_validator
from pydantic import Field
from typing_extensions import Annotated
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class NfsPermissionsUpdate(BaseModel):
    """
    Update NFS specific permissions on a volume.
    """ # noqa: E501
    read_write: Optional[List[Annotated[str, Field(strict=True)]]] = Field(default=None, description="Read/Write access.", alias="readWrite")
    read_only: Optional[List[Annotated[str, Field(strict=True)]]] = Field(default=None, description="Read only access.", alias="readOnly")
    root_squash: Optional[List[Annotated[str, Field(strict=True)]]] = Field(default=None, description="Root squash permission.", alias="rootSquash")
    no_squash: Optional[List[Annotated[str, Field(strict=True)]]] = Field(default=None, description="No squash permission.", alias="noSquash")
    all_squash: Optional[List[Annotated[str, Field(strict=True)]]] = Field(default=None, description="All squash permission.", alias="allSquash")
    __properties: ClassVar[List[str]] = ["readWrite", "readOnly", "rootSquash", "noSquash", "allSquash"]

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
        """Create an instance of NfsPermissionsUpdate from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={
            },
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of NfsPermissionsUpdate from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
        })
        return _obj


