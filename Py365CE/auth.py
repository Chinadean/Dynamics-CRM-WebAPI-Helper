from adal import *


class user_context(AuthenticationContext):

    def __init__(self, authority, validate_authority=None, cache=None,
            api_version=None, timeout=None, enable_pii=False, verify_ssl=None, proxies=None):
        '''Creates a new AuthenticationContext object.
        By default the authority will be checked against a list of known Azure
        Active Directory authorities. If the authority is not recognized as 
        one of these well known authorities then token acquisition will fail.
        This behavior can be turned off via the validate_authority parameter
        below.
        :param str authority: A URL that identifies a token authority. It should be of the
            format https://login.microsoftonline.com/your_tenant
        :param bool validate_authority: (optional) Turns authority validation 
            on or off. This parameter default to true.
        :param TokenCache cache: (optional) Sets the token cache used by this 
            AuthenticationContext instance. If this parameter is not set, then
            a default is used. Cache instances is only used by that instance of
            the AuthenticationContext and are not shared unless it has been
            manually passed during the construction of other
            AuthenticationContexts.
        :param api_version: (optional) Specifies API version using on the wire.
            Historically it has a hardcoded default value as "1.0".
            Developers have been encouraged to set it as None explicitly,
            which means the underlying API version will be automatically chosen.
            Starting from ADAL Python 1.0, this default value becomes None.
        :param timeout: (optional) requests timeout. How long to wait for the server to send
            data before giving up, as a float, or a `(connect timeout,
            read timeout) <timeouts>` tuple.
        :param enable_pii: (optional) Unless this is set to True,
            there will be no Personally Identifiable Information (PII) written in log.
        :param verify_ssl: (optional) requests verify. Either a boolean, in which case it 
            controls whether we verify the server's TLS certificate, or a string, in which 
            case it must be a path to a CA bundle to use. If this value is not provided, and 
            ADAL_PYTHON_SSL_NO_VERIFY env varaible is set, behavior is equivalent to 
            verify_ssl=False.
        :param proxies: (optional) requests proxies. Dictionary mapping protocol to the URL 
            of the proxy. See http://docs.python-requests.org/en/master/user/advanced/#proxies
            for details.
        '''
        self._is_authed = False
        super(user_context, self).__init__(authority, validate_authority=validate_authority, cache=cache,
            api_version=api_version, timeout=timeout, enable_pii=enable_pii, verify_ssl=verify_ssl, proxies=proxies)

    def acquire_token_with_username_password(self, resource, username, password, client_id):
        '''Gets and Sets token for current auth context.
        
        :param str resource: A URI that identifies the resource for which the
            token is valid.
        :param str username: The username of the user on behalf this
            application is authenticating.
        :param str password: The password of the user named in the username
            parameter.
        :param str client_id: The OAuth client id of the calling application.
        '''
        super(user_context, self).acquire_token_with_username_password(resource, username, password, client_id)
