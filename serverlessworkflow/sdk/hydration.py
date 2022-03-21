from __future__ import annotations

import dataclasses
from abc import ABC, abstractmethod
from typing import Any


class HydratableType(ABC):
    @abstractmethod
    def hydrate(self, value):
        pass


class ArrayTypeOf(HydratableType):
    def __init__(self, Type):
        self.Type = Type

    def hydrate(self, value):
        return [self.Type(**v) if type(v) is not self.Type else v for v in value]


class ComplexTypeOf(HydratableType):
    def __init__(self, Type):
        self.Type = Type

    def hydrate(self, value):
        return self.Type(**value) if type(value) is not self.Type else value


class SimpleTypeOf(HydratableType):
    def __init__(self, Type):
        self.Type = Type

    def hydrate(self, value):
        if type(value) is self.Type:
            return value


class UnionTypeOf(HydratableType):
    types: [HydratableType]

    def __init__(self, types: [HydratableType]):
        self.types = types

    def hydrate(self, value):

        for t in self.types:
            if t.hydrate(value) is not None:
                return t.hydrate(value)

        return None


class HydratableParameter:
    def __init__(self, value: Any):
        self.complex_type = None
        self.simple_type = None
        self.value = value

    def hydrateAs(self, hydratable: HydratableType):
        return hydratable.hydrate(self.value)


@dataclasses.dataclass
class Field:
    def __init__(self, key: str, value: Any):
        self.key = key
        self.value = value


class Fields:
    def __init__(self, local_attributes, kwargs, f_hydration, default_values={}):
        self.fields = Fields.load(local_attributes, kwargs, f_hydration, default_values)

    def set_to_object(self, obj):
        for f in self.fields:
            obj.__setattr__(f.key, f.value)

    @staticmethod
    def default_hydration(property_key, property_value):
        return property_value

    @staticmethod
    def load(fields, kwargs, f_hydration, default_values={}):

        _attributes: [Field] = []
        initial_values = {}
        k: str
        for k in list(fields):
            if k in ["self", "kwargs"]:
                continue
            if k.startswith("_"):
                continue
            final_value = fields.get(k)

            if final_value == "true":
                final_value = True

            initial_values[k] = final_value

            if final_value is None and default_values.get(k):
                final_value = default_values.get(k)

            if final_value is None:
                continue

            final_value = f_hydration(k, final_value)

            if final_value is not None:
                key_ = k.replace("_", "")
                # self.__setattr__(key_, final_value)
                _attributes.append(Field(key_, final_value))


            _attributes.append(Field("initial_values", initial_values))
            _attributes.append(Field("default_values", default_values))

        for k in kwargs.keys():
            final_value = kwargs[k]
            if final_value == "true":
                final_value = True

            initial_values[k] = final_value

            if final_value is None and default_values.get(k):
                final_value = default_values.get(k)

            if final_value is None:
                continue

            final_value = f_hydration(k, final_value)

            if final_value is not None:
                key_ = k.replace("_", "")
                # self.__setattr__(key_, final_value)
                _attributes.append(Field(key_, final_value))


            _attributes.append(Field("initial_values", initial_values))
            _attributes.append(Field("default_values", default_values))

        return _attributes
