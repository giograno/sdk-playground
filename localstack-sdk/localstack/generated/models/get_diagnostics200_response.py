# coding: utf-8

"""
    LocalStack REST API for Community

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3.6.1.dev
    Contact: info@localstack.cloud
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List
from localstack.generated.models.get_diagnostics200_response_logs import GetDiagnostics200ResponseLogs
from localstack.generated.models.get_diagnostics200_response_version import GetDiagnostics200ResponseVersion
from localstack.generated.models.session_info import SessionInfo
from typing import Optional, Set
from typing_extensions import Self

class GetDiagnostics200Response(BaseModel):
    """
    GetDiagnostics200Response
    """ # noqa: E501
    config: Dict[str, Any]
    docker_dependent_image_hosts: Dict[str, Any] = Field(alias="docker-dependent-image-hosts")
    docker_inspect: Dict[str, Any] = Field(alias="docker-inspect")
    file_tree: Dict[str, Any] = Field(alias="file-tree")
    important_endpoints: Dict[str, Any] = Field(alias="important-endpoints")
    info: SessionInfo
    logs: GetDiagnostics200ResponseLogs
    services: Dict[str, Any]
    usage: Dict[str, Any]
    version: GetDiagnostics200ResponseVersion
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["config", "docker-dependent-image-hosts", "docker-inspect", "file-tree", "important-endpoints", "info", "logs", "services", "usage", "version"]

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
        """Create an instance of GetDiagnostics200Response from a JSON string"""
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
        excluded_fields: Set[str] = set([
            "additional_properties",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of info
        if self.info:
            _dict['info'] = self.info.to_dict()
        # override the default output from pydantic by calling `to_dict()` of logs
        if self.logs:
            _dict['logs'] = self.logs.to_dict()
        # override the default output from pydantic by calling `to_dict()` of version
        if self.version:
            _dict['version'] = self.version.to_dict()
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of GetDiagnostics200Response from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "config": obj.get("config"),
            "docker-dependent-image-hosts": obj.get("docker-dependent-image-hosts"),
            "docker-inspect": obj.get("docker-inspect"),
            "file-tree": obj.get("file-tree"),
            "important-endpoints": obj.get("important-endpoints"),
            "info": SessionInfo.from_dict(obj["info"]) if obj.get("info") is not None else None,
            "logs": GetDiagnostics200ResponseLogs.from_dict(obj["logs"]) if obj.get("logs") is not None else None,
            "services": obj.get("services"),
            "usage": obj.get("usage"),
            "version": GetDiagnostics200ResponseVersion.from_dict(obj["version"]) if obj.get("version") is not None else None
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


