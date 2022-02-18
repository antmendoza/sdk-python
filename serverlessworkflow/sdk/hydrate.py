class ArrayOf:
    def __init__(self, Type):
        self.Type = Type

    def hydrate(self, value):
        return [self.Type(**v) if type(v) is not self.Type else v for v in value]


class ComplexType:
    def __init__(self, Type):
        self.Type = Type

    def hydrate(self, value):
        return self.Type(**value) if type(value) is not self.Type else value