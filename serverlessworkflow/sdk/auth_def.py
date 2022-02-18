from __future__ import annotations

from enum import Enum

from serverlessworkflow.sdk.basic_props_def import BasicPropsDef
from serverlessworkflow.sdk.bearer_props_def import BearerPropsDef
from serverlessworkflow.sdk.class_properties import Fields
from serverlessworkflow.sdk.oauth2props_def import Oauth2PropsDef


class Scheme(Enum):
    BASIC = "basic"
    BEARER = "bearer"
    OAUTH2 = "oauth2"


class AuthDef:
    name: str = None
    scheme: Scheme = None
    properties: (str | (BasicPropsDef | BearerPropsDef | Oauth2PropsDef)) = None

    def __init__(self,
                 name: str = None,
                 scheme: Scheme = None,
                 properties: (str | (BasicPropsDef | BearerPropsDef | Oauth2PropsDef)) = None,
                 **kwargs):
        Fields(locals(), kwargs, Fields.no_hydration).set_to_object(self)
