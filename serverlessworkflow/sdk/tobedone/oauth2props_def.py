from serverlessworkflow.sdk.class_properties import Fields
from serverlessworkflow.sdk.tobedone.metadata import Metadata


class Oauth2PropsDef:
    authority: str = None
    grantType: str = None
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
                 grantType: str = None,
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
        Fields(locals(), kwargs, Fields.no_hydration).set_to_object(self)
