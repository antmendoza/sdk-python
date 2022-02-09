import unittest

from serverlessworkflow.sdk.action import Action
from serverlessworkflow.sdk.function_ref import FunctionRef


class TestAction(unittest.TestCase):


    def test_load_function_ref(self):

        action = Action(functionRef=FunctionRef(refName="refNameTest"))
        self.assertTrue(isinstance(action.functionRef, FunctionRef))
        self.assertTrue(action.functionRef.refName, "refNameTest")

