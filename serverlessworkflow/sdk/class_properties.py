import dataclasses
from typing import Any


@dataclasses.dataclass
class Field:
    def __init__(self, key: str, value: Any):
        self.key = key
        self.value = value


class Fields:
    def __init__(self, local_attributes, kwargs, f_hydration):
        self.fields = Fields.load(local_attributes, kwargs, f_hydration)

    def set_to_object(self, obj):
        for f in self.fields:
            obj.__setattr__(f.key, f.value)

    @staticmethod
    def no_hydration(property_key, property_value):
        return property_value

    @staticmethod
    def load(fields, kwargs, f_hydration):

        _attributes: [Field] = []
        key: str
        for key in list(fields):
            if key in ["self", "kwargs"]:
                continue
            if key.startswith("_"):
                continue
            final_value = fields.get(key)
            initial_value = fields.get(key)

            if final_value == "true":
                final_value = True

            if final_value is None:
                continue

            final_value = f_hydration(key, final_value)

            if final_value is not None:
                key_ = key.replace("_", "")
                # self.__setattr__(key_, final_value)
                _attributes.append(Field(key_, final_value))

        for k in kwargs.keys():
            final_value = kwargs[k]
            if final_value == "true":
                final_value = True

            if final_value is None:
                continue

            final_value = f_hydration(k, final_value)

            if final_value is not None:
                key_ = k.replace("_", "")
                # self.__setattr__(key_, final_value)
                _attributes.append(Field(key_, final_value))

        return _attributes
