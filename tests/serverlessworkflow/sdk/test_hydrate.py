import unittest

from serverlessworkflow.sdk.hydrate import ArrayTypeOf, ComplexTypeOf, UnionTypeOf, SimpleTypeOf


class AnyClass:
    def __init__(self, **kwargs):
        pass


class TestHydrateArrayOf(unittest.TestCase):

    def test_hydrate(self):
        result_object = ArrayTypeOf(AnyClass).hydrate([{}, {}])
        self.assertTrue(isinstance(result_object[0], AnyClass))
        self.assertTrue(isinstance(result_object[1], AnyClass))

        result_string = ArrayTypeOf(str).hydrate(["one", "two"])
        self.assertTrue(isinstance(result_string[0], str))
        self.assertTrue(isinstance(result_string[1], str))


class TestHydrateUnionOfType(unittest.TestCase):

    def test_hydrate(self):
        result_string = UnionTypeOf([SimpleTypeOf(str), ComplexTypeOf(AnyClass)]).hydrate("anyValue")
        self.assertTrue(isinstance(result_string, str))

        result_class = UnionTypeOf([SimpleTypeOf(str), ComplexTypeOf(AnyClass)]).hydrate({})
        self.assertTrue(isinstance(result_class, AnyClass))
