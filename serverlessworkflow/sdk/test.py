import dataclasses
from typing import Any


@dataclasses.dataclass
class Attribute:
    def __init__(self, key: str, value: Any):
        self.key = key
        self.value = value



def method_name(local_attributes, kwargs, load_properties):
    _attributes: [Attribute] = []
    # duplicated
    local: str
    for local in list(local_attributes):
        if local in ["self", "kwargs"]:
            continue
        if local.startswith("_"):
            continue
        final_value = local_attributes.get(local)
        initial_value = local_attributes.get(local)
        if final_value == "true":
            final_value = True
        # duplicated

        final_value = load_properties(final_value, local)

        if final_value is not None:
            key_ = local.replace("_", "")
            # self.__setattr__(key_, final_value)
            _attributes.append(Attribute(key_, final_value))
    # duplicated
    for k in kwargs.keys():
        final_value = kwargs[k]
        if final_value == "true":
            final_value = True

        final_value = load_properties(final_value, k)

        if final_value is not None:
            key_ = k.replace("_", "")
            # self.__setattr__(key_, final_value)
            _attributes.append(Attribute(key_, final_value))
    # duplicated
    return _attributes
