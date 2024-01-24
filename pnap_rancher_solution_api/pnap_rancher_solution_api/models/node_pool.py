# coding: utf-8

"""
    Rancher Solution API

    Simplify enterprise-grade Kubernetes cluster operations and management with Rancher on Bare Metal Cloud. Deploy Kubernetes clusters using a few API calls.<br> <br> <span class='pnap-api-knowledge-base-link'> Knowledge base articles to help you can be found <a href='https://phoenixnap.com/kb/rancher-bmc-integration-kubernetes' target='_blank'>here</a> </span><br> <br> <b>All URLs are relative to (https://api.phoenixnap.com/solutions/rancher/v1beta)</b> 

    The version of the OpenAPI document: 0.1
    Contact: support@phoenixnap.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel, StrictInt, StrictStr, field_validator
from pydantic import Field
from typing_extensions import Annotated
from pnap_rancher_solution_api.models.node import Node
from pnap_rancher_solution_api.models.ssh_config import SshConfig
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class NodePool(BaseModel):
    """
    Node Pool Configuration. A node pool contains the name and configuration for a cluster's node pool. Node pools are set of nodes with a common configuration and specification.
    """ # noqa: E501
    name: Optional[Annotated[str, Field(min_length=1, strict=True, max_length=100)]] = Field(default=None, description="The name of the node pool.")
    node_count: Optional[StrictInt] = Field(default=None, description="Number of configured nodes, currently only node counts of 1 and 3 are possible.", alias="nodeCount")
    server_type: Optional[StrictStr] = Field(default='s0.d1.small', description="Node server type. Cannot be changed once a server is created. Currently this field should be set to either `s0.d1.small`, `s0.d1.medium`, `s1.c1.small`, `s1.c1.medium`, `s1.c2.medium`, `s1.c2.large`, `s2.c1.small`, `s2.c1.medium`, `s2.c1.large`, `s2.c2.small`, `s2.c2.medium`, `s2.c2.large`, `s1.e1.small`, `s1.e1.medium`, `s1.e1.large`.", alias="serverType")
    ssh_config: Optional[SshConfig] = Field(default=None, alias="sshConfig")
    nodes: Optional[List[Node]] = Field(default=None, description="(Read-only) The nodes associated with this node pool.")
    __properties: ClassVar[List[str]] = ["name", "nodeCount", "serverType", "sshConfig", "nodes"]

    @field_validator('name')
    def name_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^(?=.*[a-zA-Z])([a-zA-Z0-9().-])+$", value):
            raise ValueError(r"must validate the regular expression /^(?=.*[a-zA-Z])([a-zA-Z0-9().-])+$/")
        return value

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
        """Create an instance of NodePool from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * OpenAPI `readOnly` fields are excluded.
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={
                "nodes",
            },
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of ssh_config
        if self.ssh_config:
            _dict['sshConfig'] = self.ssh_config.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in nodes (list)
        _items = []
        if self.nodes:
            for _item in self.nodes:
                if _item:
                    _items.append(_item.to_dict())
            _dict['nodes'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of NodePool from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "name": obj.get("name"),
            "nodeCount": obj.get("nodeCount"),
            "serverType": obj.get("serverType") if obj.get("serverType") is not None else 's0.d1.small',
            "sshConfig": SshConfig.from_dict(obj.get("sshConfig")) if obj.get("sshConfig") is not None else None,
            "nodes": [Node.from_dict(_item) for _item in obj.get("nodes")] if obj.get("nodes") is not None else None
        })
        return _obj

