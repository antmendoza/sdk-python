import copy
import json

import yaml

from serverlessworkflow.sdk.injectstate import Injectstate
from serverlessworkflow.sdk.operationstate import Operationstate
from serverlessworkflow.sdk.state import State


def is_inject_state(state: State):
    return state['type'] == 'inject'


def is_operation_state(state: State):
    return state['type'] == 'operation'


class Workflow:
    id = None
    key = None
    name = None
    description = None
    version = None
    annotations = None
    dataInputSchema = None
    schema = None
    failOnValidationErrors = None
    secrets = None
    constants = None
    start = None
    specVersion = None
    expressionLang = None
    timeouts = None
    errors = None
    keepActive = None
    metadata = None
    events = None
    functions = None
    autoRetries = None
    retries = None
    auth = None
    states = None

    def __init__(self,
                 id_=None,
                 key=None,
                 name=None,
                 version=None,
                 description=None,
                 specVersion=None,
                 annotations=None,
                 dataInputSchema=None,
                 schema=None,
                 failOnValidationErrors=None,
                 secrets=None,
                 constants=None,
                 start=None,
                 expressionLang=None,
                 timeouts=None,
                 errors=None,
                 keepActive=None,
                 metadata=None,
                 events=None,
                 autoRetries=None,
                 retries=None,
                 auth=None,
                 states=None,
                 functions=None,
                 **kwargs):

        self._default_values = {'expressionLang': 'jq'}
        self._initial_values = {}

        # duplicated
        for local in list(locals()):
            if local in ["self", "kwargs"]:
                continue
            final_value = locals().get(local)
            initial_value = locals().get(local)
            if not final_value:
                if self._default_values.get(local):
                    final_value = self._default_values.get(local)
            if final_value == "true":
                final_value = True
            # duplicated

            if local == 'states' and final_value:
                final_value = Workflow.load_states(final_value)

            self._initial_values[local] = initial_value

            if final_value is not None:
                self.__setattr__(local.replace("_", ""), final_value)

        # duplicated
        for k in kwargs.keys():
            final_value = kwargs[k]
            if final_value == "true":
                final_value = True

            self.__setattr__(k.replace("_", ""), final_value)
        # duplicated

    def to_json(self) -> str:

        deepcopy = copy.deepcopy(self)
        delattr(deepcopy, '_initial_values')
        delattr(deepcopy, '_default_values')

        for k in self._default_values.keys():
            if self._initial_values.get(k) is None:
                delattr(deepcopy, k)

        return json.dumps(deepcopy,
                          default=lambda o: o.__dict__,
                          indent=4)

    def to_yaml(self):
        deepcopy = copy.deepcopy(self)
        delattr(deepcopy, '_initial_values')
        delattr(deepcopy, '_default_values')

        for k in self._default_values.keys():
            if self._initial_values.get(k) is None:
                delattr(deepcopy, k)

        yaml.emitter.Emitter.process_tag = lambda x: None
        return yaml.dump(deepcopy,
                         sort_keys=False,
                         # , default_flow_style=False,
                         allow_unicode=True,
                         )

    @classmethod
    def from_source(cls, source: str):
        try:
            loaded_data = yaml.safe_load(source)
            loaded_data["id_"] = loaded_data["id"]
            del loaded_data["id"]
            return cls(**loaded_data)
        except Exception:
            raise Exception("Format not supported")

    @staticmethod
    def load_states(states: [State]):
        result = []
        for state in states:
            if is_inject_state(state):
                result.append(Injectstate(**(states[0])))
            elif is_operation_state(state):
                result.append(Operationstate(**(states[0])))
            else:
                result.append(State(**(states[0])))

        return result

    def __repr__(self):
        return "{!r}".format(self.__dict__)
