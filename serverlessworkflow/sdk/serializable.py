import copy
import traceback


class Serializable:

    def __init__(self):
        self._default_values = {}
        self._initial_values = {}

    def serialize(self):

        try:
            self_copy: Serializable = copy.deepcopy(self)

            for k in self_copy.__dict__:
                attribute_value = self_copy.__getattribute__(k)
                if isinstance(attribute_value, list):
                    elements: list = attribute_value
                    for element in elements.copy():
                        if isinstance(element, Serializable):
                            elements.remove(element)
                            serialize = element.serialize()
                            elements.append(serialize)

                if isinstance(attribute_value, Serializable):
                    self_copy.__setattr__(k, attribute_value.serialize())

            for k in self_copy._default_values.keys():
                if self_copy._initial_values.get(k) is None:
                    delattr(self_copy, k)

            delattr(self_copy, '_default_values')
            delattr(self_copy, '_initial_values')

            return self_copy

        except Exception as e:
            traceback.print_exc()
            raise e
