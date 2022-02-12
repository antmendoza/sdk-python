from serverlessworkflow.sdk.class_properties import ClassProperties


class State:
    type: str

    def __init__(self, data: dict = None,
                 **kwargs):
        ClassProperties(locals(), kwargs, ClassProperties.dummy).set_to_object(self)

    def is_event_state(self):
        return self.type == 'switch'

    def is_operation_state(self):
        return self.type == 'operation'

    def is_switch_state(self):
        return self.type == 'switch'

    def is_sleep_state(self):
        return self.type == 'sleep'

    def is_parallel_state(self):
        return self.type == 'parallel'

    def is_inject_state(self):
        return self.type == 'inject'

    def is_foreach_state(self):
        return self.type == 'foreach'

    def is_callback_state(self):
        return self.type == 'callback'

