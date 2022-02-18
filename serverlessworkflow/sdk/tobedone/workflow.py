from __future__ import annotations

import json

import yaml

from serverlessworkflow.sdk.auth_def import AuthDef
from serverlessworkflow.sdk.class_properties import Fields
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
from serverlessworkflow.sdk.tobedone.workflow_time_out import WorkflowTimeOut


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
    dataInputSchema: (str | DataInputSchema) = None
    secrets: str = None  # Secrets
    constants: (str | dict[str, dict]) = None
    start: (str | StartDef) = None
    specVersion: str = None
    expressionLang: str = None
    timeouts: (str | WorkflowTimeOut) = None
    errors: (str | [ErrorDef]) = None
    keepActive: bool = None
    metadata: Metadata = None
    events: (str | [EventDef]) = None
    functions: (str | [Function]) = None
    autoRetries: bool = None
    retries: (str | [RetryDef]) = None
    auth: (str, [AuthDef]) = None
    states: [State] = None

    def __init__(self,
                 id_: str = None,
                 key: str = None,
                 name: str = None,
                 version: str = None,
                 description: str = None,
                 specVersion: str = None,
                 annotations: [str] = None,
                 dataInputSchema: (str | DataInputSchema) = None,
                 secrets: str = None,  # Secrets
                 constants: (str | dict[str, dict]) = None,
                 start: (str | StartDef) = None,
                 expressionLang: str = None,
                 timeouts: (str | WorkflowTimeOut) = None,
                 errors: (str | [ErrorDef]) = None,
                 keepActive: bool = None,
                 metadata: Metadata = None,
                 events: (str | [EventDef]) = None,
                 autoRetries: bool = None,
                 retries: (str | [RetryDef]) = None,
                 auth: (str | [AuthDef]) = None,
                 states: [State] = None,
                 functions: (str | [Function]) = None
                 , **kwargs):

        Fields(locals(), kwargs, Workflow.load_properties).set_to_object(self)

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
    def load_properties(k, final_value):
        if k == 'states' and final_value:
            final_value = Workflow.load_states(final_value)
        if k == 'functions' and final_value:
            final_value = Workflow.load_functions(final_value)
        return final_value

    @staticmethod
    def load_states(states: [State]):
        result = []
        for raw_state in states:
            state = State(**raw_state)
            if state.is_inject_state():
                result.append(InjectState(**raw_state))
            elif state.is_operation_state():
                result.append(OperationState(**raw_state))
            elif state.is_foreach_state():
                result.append(ForEachState(**raw_state))
            else:
                result.append(state)

        return result

    def __repr__(self):
        return "{!r}".format(self.__dict__)

    @staticmethod
    def load_functions(functions: (str | [Function])):
        if type(functions) is str:
            return functions

        return [Function(**function) if type(function) is not Function else function for function in functions]
