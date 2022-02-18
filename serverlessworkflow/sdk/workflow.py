from __future__ import annotations

import copy
import json

import yaml

from serverlessworkflow.sdk.auth_def import AuthDef
from serverlessworkflow.sdk.tobedone.class_properties import Fields
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
from serverlessworkflow.sdk.tobedone.hydrate import HydratableParameter, UnionTypeOf, SimpleTypeOf, ComplexTypeOf, \
    ArrayTypeOf
from serverlessworkflow.sdk.workflow_time_out import WorkflowTimeOut


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

        Fields(locals(), kwargs, Workflow.f_hydration).set_to_object(self)

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

    def __repr__(self):
        return "{!r}".format(self.__dict__)

    @staticmethod
    def f_hydration(p_key, p_value):

        if p_key == 'dataInputSchema':
            return HydratableParameter(value=p_value).hydrateAs(UnionTypeOf([SimpleTypeOf(str),
                                                                             ComplexTypeOf(DataInputSchema)]))

        if p_key == 'constants':
            return HydratableParameter(value=p_value).hydrateAs(UnionTypeOf([SimpleTypeOf(str),
                                                                             ComplexTypeOf(dict)]))
        if p_key == 'start':
            return HydratableParameter(value=p_value).hydrateAs(UnionTypeOf([SimpleTypeOf(str),
                                                                             ComplexTypeOf(StartDef)]))

        if p_key == 'timeouts':
            return HydratableParameter(value=p_value).hydrateAs(UnionTypeOf([SimpleTypeOf(str),
                                                                             ComplexTypeOf(WorkflowTimeOut)]))

        if p_key == 'errors':
            return HydratableParameter(value=p_value).hydrateAs(UnionTypeOf([SimpleTypeOf(str),
                                                                             ArrayTypeOf(ErrorDef)]))

        if p_key == 'events':
            return HydratableParameter(value=p_value).hydrateAs(UnionTypeOf([SimpleTypeOf(str),
                                                                             ArrayTypeOf(EventDef)]))

        if p_key == 'retries':
            return HydratableParameter(value=p_value).hydrateAs(UnionTypeOf([SimpleTypeOf(str),
                                                                             ArrayTypeOf(RetryDef)]))

        if p_key == 'auth':
            return HydratableParameter(value=p_value).hydrateAs(UnionTypeOf([SimpleTypeOf(str),
                                                                             ArrayTypeOf(AuthDef)]))

        if p_key == 'states':
            result = []

            for raw_state in p_value:
                state = State(**raw_state)
                if state.is_inject_state():
                    result.append(InjectState(**raw_state))
                elif state.is_operation_state():
                    result.append(OperationState(**raw_state))
                elif state.is_foreach_state():
                    result.append(ForEachState(**raw_state))
                # TODO add states
                else:
                    result.append(state)

            return result

        if p_key == 'functions':
            return HydratableParameter(value=p_value).hydrateAs(UnionTypeOf([SimpleTypeOf(str),
                                                                             ArrayTypeOf(Function)]))

        return copy.deepcopy(p_value)

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
