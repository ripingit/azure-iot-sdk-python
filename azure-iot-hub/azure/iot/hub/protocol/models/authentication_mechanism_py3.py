# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class AuthenticationMechanism(Model):
    """AuthenticationMechanism.

    :param symmetric_key:
    :type symmetric_key: ~protocol.models.SymmetricKey
    :param x509_thumbprint:
    :type x509_thumbprint: ~protocol.models.X509Thumbprint
    :param type: Possible values include: 'sas', 'selfSigned',
     'certificateAuthority', 'none'
    :type type: str or ~protocol.models.enum
    """

    _attribute_map = {
        'symmetric_key': {'key': 'symmetricKey', 'type': 'SymmetricKey'},
        'x509_thumbprint': {'key': 'x509Thumbprint', 'type': 'X509Thumbprint'},
        'type': {'key': 'type', 'type': 'str'},
    }

    def __init__(self, *, symmetric_key=None, x509_thumbprint=None, type=None, **kwargs) -> None:
        super(AuthenticationMechanism, self).__init__(**kwargs)
        self.symmetric_key = symmetric_key
        self.x509_thumbprint = x509_thumbprint
        self.type = type
