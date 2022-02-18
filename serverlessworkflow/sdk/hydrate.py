class Hydratable:
    def hydrate(self, value):
        pass


class ArrayOfType(Hydratable):
    def __init__(self, Type):
        self.Type = Type

    def hydrate(self, value):
        return [self.Type(**v) if type(v) is not self.Type else v for v in value]


class ComplexType(Hydratable):
    def __init__(self, Type):
        self.Type = Type

    def hydrate(self, value):
        return self.Type(**value) if type(value) is not self.Type else value


class SimpleType(Hydratable):
    def __init__(self, Type):
        self.Type = Type

    def hydrate(self, value):
        if type(value) is self.Type:
            return value


class UnionOfType(Hydratable):
    types: [Hydratable]

    def __init__(self, types: [Hydratable]):
        self.types = types

    def hydrate(self, value):

        for t in self.types:
            if t.hydrate(value) is not None:
                return t.hydrate(value)

        return None
