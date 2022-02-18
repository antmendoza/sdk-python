import unittest

from serverlessworkflow.sdk.hydrate import ArrayOf


class AnyClass:
    def __init__(self, **kwargs):
        pass

class TestHydrateArrayOf(unittest.TestCase):

    def test_load_function_ref(self):
        result = ArrayOf(AnyClass).hydrate([{}, {}])
        self.assertTrue(isinstance(result[0], AnyClass))
        self.assertTrue(isinstance(result[1], AnyClass))
