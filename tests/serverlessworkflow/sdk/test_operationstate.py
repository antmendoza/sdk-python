import unittest
from typing import Any


def load(key: str, value: Any):
    if type(value) is str:
        return value

    if type(value) is int:
        return value

    print(type(value))


class TestOperationState(unittest.TestCase):

    def test_load_str(self):
        value: str = "anyvalue"
        self.assertEqual(load("", value), value)


    def test_load_int(self):
        value: int = 3
        self.assertEqual(load("", value), value)


    def test_load_int(self):
        value: int = 3
        self.assertEqual(load("", value), value)
