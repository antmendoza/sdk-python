from __future__ import annotations

import json
from typing import Union, Dict, List

import yaml

from serverlessworkflow.sdk.auth_def import AuthDef
from serverlessworkflow.sdk.error_def import ErrorDef
from serverlessworkflow.sdk.event_def import EventDef
from serverlessworkflow.sdk.foreach_state import ForEachState
from serverlessworkflow.sdk.function import Function
from serverlessworkflow.sdk.inject_state import InjectState
from serverlessworkflow.sdk.metadata import Metadata
from serverlessworkflow.sdk.operation_state import OperationState
from serverlessworkflow.sdk.retry_def import RetryDef
from serverlessworkflow.sdk.start_def import StartDef
from serverlessworkflow.sdk.state import State
from serverlessworkflow.sdk.test import Attributes
from serverlessworkflow.sdk.workflow_time_out import WorkflowTimeOut


def is_inject_state(state: State):
    return state['type'] == 'inject'


def is_operation_state(state: State):
    return state['type'] == 'operation'


def is_foreach_state(state: State):
    return state['type'] == 'foreach'


class DataInputSchema:
    schema: str
    failOnValidationErrors: bool


class Workflow:
    id: str = None
    key: str = None
    name: str = None
    description: str = None
    version: str = None
    annotations: [str] = None
    dataInputSchema: Union[str, DataInputSchema] = None
    secrets: str = None  # Secrets
    constants: Union[str, Dict[str, Dict]] = None
    start: Union[str, StartDef] = None
    specVersion: str = None
    expressionLang: str = None
    timeouts: Union[str, WorkflowTimeOut] = None
    errors: Union[str, List[ErrorDef]] = None
    keepActive: bool = None
    metadata: Metadata = None
    events: Union[str, List[EventDef]] = None
    functions: (str | [Function]) = None
    autoRetries: bool = None
    retries: Union[str, List[RetryDef]] = None
    auth: Union[str, List[AuthDef]] = None
    states: [State] = None

    def __init__(self,
                 id_: str = None,
                 key: str = None,
                 name: str = None,
                 version: str = None,
                 description: str = None,
                 specVersion: str = None,
                 annotations: [str] = None,
                 dataInputSchema: Union[str, DataInputSchema] = None,
                 secrets: str = None,  # Secrets
                 constants: Union[str, Dict[str, Dict]] = None,
                 start: Union[str, StartDef] = None,
                 expressionLang: str = None,
                 timeouts: Union[str, WorkflowTimeOut] = None,
                 errors: Union[str, List[ErrorDef]] = None,
                 keepActive: bool = None,
                 metadata: Metadata = None,
                 events: Union[str, List[EventDef]] = None,
                 autoRetries: bool = None,
                 retries: Union[str, List[RetryDef]] = None,
                 auth: Union[str, List[AuthDef]] = None,
                 states: [State] = None,
                 functions: (str | [Function]) = None
                 , **kwargs):

        Attributes(locals(), kwargs, self.load_properties).set_to_object(self)

    def to_json(self) -> str:
        return json.dumps(self,
                          default=lambda o: o.__dict__,
                          indent=4)

    def to_yaml(self):
        yaml.emitter.Emitter.process_tag = lambda x: None
        return yaml.dump(self,
                         sort_keys=False,
                         # , default_flow_style=False,
                         allow_unicode=True,
                         )

    @classmethod
    def from_source(cls, source: str):
        try:
            loaded_data = yaml.safe_load(source)
            return cls(**loaded_data)
        except Exception:
            raise Exception("Format not supported")

    @staticmethod
    def load_properties(final_value, local):
        if local == 'states' and final_value:
            final_value = Workflow.load_states(final_value)
        if local == 'functions' and final_value:
            final_value = Workflow.load_functions(final_value)
        return final_value

    @staticmethod
    def load_states(states: [State]):
        result = []
        for state in states:
            if is_inject_state(state):
                result.append(InjectState(**(state)))
            elif is_operation_state(state):
                result.append(OperationState(**(state)))
            elif is_foreach_state(state):
                result.append(ForEachState(**(state)))
            else:
                result.append(State(**(state)))

        return result

    def __repr__(self):
        return "{!r}".format(self.__dict__)

    @staticmethod
    def load_functions(functions: (str | [Function])):
        if type(functions) is str:
            return functions

        return [Function(**function) if type(function) is not Function else function for function in functions]
