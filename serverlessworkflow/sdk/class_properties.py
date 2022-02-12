import dataclasses
from typing import Any


@dataclasses.dataclass
class Attribute:
    def __init__(self, key: str, value: Any):
        self.key = key
        self.value = value


class ClassProperties:
    def __init__(self, local_attributes, kwargs, load_properties):
        self.attributes = ClassProperties.load(local_attributes, kwargs, load_properties)

    def set_to_object(self, obj):
        for attr in self.attributes:
            obj.__setattr__(attr.key, attr.value)

    @staticmethod
    def dummy(property_key, property_value):
        return property_value

    @staticmethod
    def load(local_attributes, kwargs, load_properties):
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

            if final_value is None:
                continue

            final_value = load_properties(local, final_value)

            if final_value is not None:
                key_ = local.replace("_", "")
                # self.__setattr__(key_, final_value)
                _attributes.append(Attribute(key_, final_value))

        # duplicated
        for k in kwargs.keys():
            final_value = kwargs[k]
            if final_value == "true":
                final_value = True

            if final_value is None:
                continue

            final_value = load_properties(k, final_value)

            if final_value is not None:
                key_ = k.replace("_", "")
                # self.__setattr__(key_, final_value)
                _attributes.append(Attribute(key_, final_value))
        # duplicated
        return _attributes
