from enum import Enum
from typing import Union

from serverlessworkflow.sdk.basicpropsdef import Basicpropsdef
from serverlessworkflow.sdk.bearerpropsdef import Bearerpropsdef
from serverlessworkflow.sdk.oauth2propsdef import Oauth2propsdef


class Scheme(Enum):
    BASIC = "basic"
    BEARER = "bearer"
    OAUTH2 = "oauth2"


class Authdef:
    name:str = None
    scheme : Scheme = None
    properties : Union[str, Union[Basicpropsdef, Bearerpropsdef, Oauth2propsdef]] = None

    def __init__(self,
                 name: str = None,
                 scheme : Scheme = None,
                 properties : Union[str, Union[Basicpropsdef, Bearerpropsdef, Oauth2propsdef]] = None,
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
