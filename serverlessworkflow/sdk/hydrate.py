from __future__ import annotations

from typing import Any


class HydratableType:
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

    def hydrateAs(self, hydratable):
        return hydratable.hydrate(self.value)
