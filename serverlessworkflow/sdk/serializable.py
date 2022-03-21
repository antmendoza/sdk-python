import copy


class Serializable:
    def serialize(self):

        self_copy = copy.deepcopy(self)

        for k in self_copy.__dict__:
            attribute_value = self_copy.__getattribute__(k)
            if isinstance(attribute_value, list):
                elements: list = attribute_value
                for element in elements:
                    if isinstance(element, Serializable):
                        elements.remove(element)
                        elements.append(element.serialize())

            if isinstance(attribute_value, Serializable):
                self_copy.__setattr__(k, attribute_value.serialize())

        if hasattr(self_copy, '_default_values'):
            for k in self_copy._default_values.keys():
                if self_copy._initial_values.get(k) is None:
                    delattr(self_copy, k)
            delattr(self_copy, '_default_values')


        if hasattr(self_copy, '_initial_values'):
            delattr(self_copy, '_initial_values')

        return self_copy