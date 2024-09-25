# coding: utf-8

"""
LocalStack REST API

No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

The version of the OpenAPI document: 3.7.3.dev45
Contact: info@localstack.cloud
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501

from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, field_validator
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing_extensions import Annotated
from localstack.generated.models.fault_rule_error import FaultRuleError
from typing import Optional, Set
from typing_extensions import Self


class FaultRule(BaseModel):
    """
    Each rule represents the conditions for a fault and its detrimental effects.
    """  # noqa: E501

    region: Optional[Annotated[str, Field(strict=True)]] = Field(
        default=None,
        description="Region name, e.g., 'ap-south-1'. If omitted, all regions are affected.",
    )
    service: Optional[Annotated[str, Field(strict=True)]] = Field(
        default=None,
        description="Name of the service, e.g., 'kinesis'. If omitted, all services are affected.",
    )
    operation: Optional[Annotated[str, Field(strict=True)]] = Field(
        default=None,
        description="Name of the operation, e.g., 'PutRecord'. If omitted, all operations are affected.",
    )
    probability: Optional[
        Union[
            Annotated[float, Field(le=1, strict=True, ge=0)],
            Annotated[int, Field(le=1, strict=True, ge=0)],
        ]
    ] = Field(
        default=None,
        description="Probability of invoking this rule, e.g., 0.5. If omitted, 1.0 is used.",
    )
    description: Optional[Annotated[str, Field(strict=True, max_length=8192)]] = Field(
        default=None,
        description="A description of this rule. This field has no effect.",
    )
    error: Optional[FaultRuleError] = None
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = [
        "region",
        "service",
        "operation",
        "probability",
        "description",
        "error",
    ]

    @field_validator("region")
    def region_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^[a-zA-Z0-9-]+$", value):
            raise ValueError(r"must validate the regular expression /^[a-zA-Z0-9-]+$/")
        return value

    @field_validator("service")
    def service_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^[a-zA-Z0-9-_]+$", value):
            raise ValueError(r"must validate the regular expression /^[a-zA-Z0-9-_]+$/")
        return value

    @field_validator("operation")
    def operation_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^[a-zA-Z]+$", value):
            raise ValueError(r"must validate the regular expression /^[a-zA-Z]+$/")
        return value

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of FaultRule from a JSON string"""
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
        excluded_fields: Set[str] = set(
            [
                "additional_properties",
            ]
        )

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of error
        if self.error:
            _dict["error"] = self.error.to_dict()
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of FaultRule from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "region": obj.get("region"),
                "service": obj.get("service"),
                "operation": obj.get("operation"),
                "probability": obj.get("probability"),
                "description": obj.get("description"),
                "error": FaultRuleError.from_dict(obj["error"])
                if obj.get("error") is not None
                else None,
            }
        )
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj
