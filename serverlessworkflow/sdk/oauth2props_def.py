from enum import Enum

from serverlessworkflow.sdk.class_properties import Properties
from serverlessworkflow.sdk.metadata import Metadata


class Oauth2PropsDefGrantType(Enum):
    password = "password"
    clientCredentials = "clientCredentials"
    tokenExchange = "tokenExchange"


class Oauth2PropsDef:
    authority: str = None
    grantType: Oauth2PropsDefGrantType = None
    clientId: str = None
    clientSecret: str = None
    scopes: [str] = None
    username: str = None
    password: str = None
    audiences: [str] = None
    subjectToken: str = None
    requestedSubject: str = None
    requestedIssuer: str = None
    metadata: Metadata = None

    def __init__(self,
                 authority: str = None,
                 grantType: Oauth2PropsDefGrantType = None,
                 clientId: str = None,
                 clientSecret: str = None,
                 scopes: [str] = None,
                 username: str = None,
                 password: str = None,
                 audiences: [str] = None,
                 subjectToken: str = None,
                 requestedSubject: str = None,
                 requestedIssuer: str = None,
                 metadata: Metadata = None,
                 **kwargs):
        Properties(locals(), kwargs, Properties.default).set_to_object(self)
