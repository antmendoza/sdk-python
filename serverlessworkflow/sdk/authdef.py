from enum import Enum
from typing import Union

from serverlessworkflow.sdk.basicpropsdef import BasicPropsDef
from serverlessworkflow.sdk.bearerpropsdef import BearerPropsDef
from serverlessworkflow.sdk.oauth2propsdef import Oauth2PropsDef


class Scheme(Enum):
    BASIC = "basic"
    BEARER = "bearer"
    OAUTH2 = "oauth2"


class AuthDef:
    name:str = None
    scheme : Scheme = None
    properties : Union[str, Union[BasicPropsDef, BearerPropsDef, Oauth2PropsDef]] = None

    def __init__(self,
                 name: str = None,
                 scheme : Scheme = None,
                 properties : Union[str, Union[BasicPropsDef, BearerPropsDef, Oauth2PropsDef]] = None,
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
