from serverlessworkflow.sdk.hydration import Fields
from serverlessworkflow.sdk.metadata import Metadata
from serverlessworkflow.sdk.serializable import Serializable


class Oauth2PropsDef(Serializable):
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
        Serializable.__init__(self)
        Fields(locals(), kwargs, Fields.default_hydration).set_to_object(self)
