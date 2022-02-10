from enum import Enum
from typing import Union

from serverlessworkflow.sdk.basic_props_def import BasicPropsDef
from serverlessworkflow.sdk.bearer_props_def import BearerPropsDef
from serverlessworkflow.sdk.oauth2props_def import Oauth2PropsDef
from serverlessworkflow.sdk.test import Attributes


class Scheme(Enum):
    BASIC = "basic"
    BEARER = "bearer"
    OAUTH2 = "oauth2"


class AuthDef:
    name: str = None
    scheme: Scheme = None
    properties: Union[str, Union[BasicPropsDef, BearerPropsDef, Oauth2PropsDef]] = None

    def __init__(self,
                 name: str = None,
                 scheme: Scheme = None,
                 properties: Union[str, Union[BasicPropsDef, BearerPropsDef, Oauth2PropsDef]] = None,
                 **kwargs):

        Attributes(locals(), kwargs, Attributes.dummy).set_to_object(self)
