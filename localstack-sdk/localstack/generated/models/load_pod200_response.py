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
import json
import pprint
from pydantic import BaseModel, ConfigDict, Field, StrictStr, ValidationError, field_validator
from typing import Any, List, Optional
from localstack.generated.models.cloud_pod_event import CloudPodEvent
from localstack.generated.models.pod_completion_event import PodCompletionEvent
from localstack.generated.models.pod_service_event import PodServiceEvent
from pydantic import StrictStr, Field
from typing import Union, List, Set, Optional, Dict
from typing_extensions import Literal, Self

LOADPOD200RESPONSE_ONE_OF_SCHEMAS = ["CloudPodEvent", "PodCompletionEvent", "PodServiceEvent"]

class LoadPod200Response(BaseModel):
    """
    LoadPod200Response
    """
    # data type: CloudPodEvent
    oneof_schema_1_validator: Optional[CloudPodEvent] = None
    # data type: PodServiceEvent
    oneof_schema_2_validator: Optional[PodServiceEvent] = None
    # data type: PodCompletionEvent
    oneof_schema_3_validator: Optional[PodCompletionEvent] = None
    actual_instance: Optional[Union[CloudPodEvent, PodCompletionEvent, PodServiceEvent]] = None
    one_of_schemas: Set[str] = { "CloudPodEvent", "PodCompletionEvent", "PodServiceEvent" }

    model_config = ConfigDict(
        validate_assignment=True,
        protected_namespaces=(),
    )


    def __init__(self, *args, **kwargs) -> None:
        if args:
            if len(args) > 1:
                raise ValueError("If a position argument is used, only 1 is allowed to set `actual_instance`")
            if kwargs:
                raise ValueError("If a position argument is used, keyword arguments cannot be used.")
            super().__init__(actual_instance=args[0])
        else:
            super().__init__(**kwargs)

    @field_validator('actual_instance')
    def actual_instance_must_validate_oneof(cls, v):
        instance = LoadPod200Response.model_construct()
        error_messages = []
        match = 0
        # validate data type: CloudPodEvent
        if not isinstance(v, CloudPodEvent):
            error_messages.append(f"Error! Input type `{type(v)}` is not `CloudPodEvent`")
        else:
            match += 1
        # validate data type: PodServiceEvent
        if not isinstance(v, PodServiceEvent):
            error_messages.append(f"Error! Input type `{type(v)}` is not `PodServiceEvent`")
        else:
            match += 1
        # validate data type: PodCompletionEvent
        if not isinstance(v, PodCompletionEvent):
            error_messages.append(f"Error! Input type `{type(v)}` is not `PodCompletionEvent`")
        else:
            match += 1
        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when setting `actual_instance` in LoadPod200Response with oneOf schemas: CloudPodEvent, PodCompletionEvent, PodServiceEvent. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when setting `actual_instance` in LoadPod200Response with oneOf schemas: CloudPodEvent, PodCompletionEvent, PodServiceEvent. Details: " + ", ".join(error_messages))
        else:
            return v

    @classmethod
    def from_dict(cls, obj: Union[str, Dict[str, Any]]) -> Self:
        return cls.from_json(json.dumps(obj))

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Returns the object represented by the json string"""
        instance = cls.model_construct()
        error_messages = []
        match = 0

        # deserialize data into CloudPodEvent
        try:
            instance.actual_instance = CloudPodEvent.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into PodServiceEvent
        try:
            instance.actual_instance = PodServiceEvent.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into PodCompletionEvent
        try:
            instance.actual_instance = PodCompletionEvent.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))

        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when deserializing the JSON string into LoadPod200Response with oneOf schemas: CloudPodEvent, PodCompletionEvent, PodServiceEvent. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when deserializing the JSON string into LoadPod200Response with oneOf schemas: CloudPodEvent, PodCompletionEvent, PodServiceEvent. Details: " + ", ".join(error_messages))
        else:
            return instance

    def to_json(self) -> str:
        """Returns the JSON representation of the actual instance"""
        if self.actual_instance is None:
            return "null"

        if hasattr(self.actual_instance, "to_json") and callable(self.actual_instance.to_json):
            return self.actual_instance.to_json()
        else:
            return json.dumps(self.actual_instance)

    def to_dict(self) -> Optional[Union[Dict[str, Any], CloudPodEvent, PodCompletionEvent, PodServiceEvent]]:
        """Returns the dict representation of the actual instance"""
        if self.actual_instance is None:
            return None

        if hasattr(self.actual_instance, "to_dict") and callable(self.actual_instance.to_dict):
            return self.actual_instance.to_dict()
        else:
            # primitive type
            return self.actual_instance

    def to_str(self) -> str:
        """Returns the string representation of the actual instance"""
        return pprint.pformat(self.model_dump())

