class Workflow:
    id = None
    key = None
    name = None
    description = None
    version = None
    annotations = None
    dataInputSchema = None
    schema = None
    failOnValidationErrors = None
    secrets = None
    constants = None
    start = None
    specVersion = None
    expressionLang = None
    timeouts = None
    errors = None
    keepActive = None
    metadata = None
    events = None
    functions = None
    autoRetries = None
    retries = None
    auth = None
    states = None

    def __init__(self,
                 id=None,
                 key=None,
                 name=None,
                 description=None,
                 version=None,
                 annotations=None,
                 dataInputSchema=None,
                 schema=None,
                 failOnValidationErrors=None,
                 secrets=None,
                 constants=None,
                 start=None,
                 specVersion=None,
                 expressionLang=None,
                 timeouts=None,
                 errors=None,
                 keepActive=None,
                 metadata=None,
                 events=None,
                 functions=None,
                 autoRetries=None,
                 retries=None,
                 auth=None,
                 states=None,
                 **kwargs):

        # duplicated
        for local in list(locals()):
            if local in ["self", "kwargs"]:
                continue
            value = locals().get(local)
            if not value:
                continue
            if value == "true":
                value = True
            # duplicated

            self.__setattr__(local.replace("_", ""), value)

        # duplicated
        for k in kwargs.keys():
            value = kwargs[k]
            if value == "true":
                value = True

            self.__setattr__(k.replace("_", ""), value)
            # duplicated
