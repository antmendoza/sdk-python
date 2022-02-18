import unittest

from serverlessworkflow.sdk.hydrate import ArrayOfType, ComplexType, UnionOfType, SimpleType


class AnyClass:
    def __init__(self, **kwargs):
        pass


class TestHydrateArrayOf(unittest.TestCase):

    def test_load_function_ref(self):
        result = ArrayOfType(AnyClass).hydrate([{}, {}])
        self.assertTrue(isinstance(result[0], AnyClass))
        self.assertTrue(isinstance(result[1], AnyClass))


class TestHydrateUnionOfType(unittest.TestCase):

    def test_load_function_ref(self):
        result_string = UnionOfType([SimpleType(str), ComplexType(AnyClass)]).hydrate("anyValue")
        self.assertTrue(isinstance(result_string, str))

        result_class = UnionOfType([SimpleType(str), ComplexType(AnyClass)]).hydrate({})
        self.assertTrue(isinstance(result_class, AnyClass))
