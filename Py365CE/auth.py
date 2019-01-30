from adal import *
from datetime import datetime
import requests
import json


class client_context(AuthenticationContext):
    '''Implements AuthenticationContext from Python Adal Library
    Adds additional functionality for Executing Py365CE Request Classes'''

    default_headers = {'Content-Type': 'application/json; charset=utf-8',
                            'OData-MaxVersion': '4.0',
                            'OData-Version': '4.0',
                            'Accept': 'application/json'}
    api_query_stem = '/api/data/v9.0/'
    _session = None
    _debug = False
    _affinity_reset = None

    def __init__(self, tenant, Debug=False, AffinityReset=None):
        if self._session == None:
            self._session = requests.session()
        self._debug = Debug
        self._affinity_reset = AffinityReset
        for i in self.default_headers:
            self._session.headers.update({i:self.default_headers[i]})
        super(client_context, self).__init__(tenant)
    
    def execute(self, request):
        # TODO: Add additional request types as they are created.
        if not self.is_authed:
            raise AuthException('User_Context is not authed.')
        self._session.headers.update({'Authorization':'Bearer ' + self.get_auth_value('accessToken')})
        if request.request_type == 0: # create_record
            url = request.build_create_url
            data = request.data
            return self.execute_post(url, data, Debug=self._debug)
        elif  request.request_type == 1:
            pass
        elif  request.request_type == 2:
            pass
        elif  request.request_type == 3: # delete_record
            return self.execute_delete(request, Debug=self._debug)
        raise TypeError('Argument does not have value request_type.')
        
    def execute_get(self, url, data=None, Debug=False):
        pass
    
    def execute_post(self, url, data, Debug=False):
        return self._session.post(url, data=json.dumps(data))

    def execute_patch(self, url, data, Debug=False):
        pass
    
    def execute_delete(self, url, data=None, Debug=False):
        pass
    
    def execute_put(self, request):
        pass 
   
    @property
    def is_authed(self):
        if len(self.cache._cache) >= 1:
            if not (datetime.strptime(self.get_auth_value('expiresOn'), '%Y-%m-%d %H:%M:%S.%f') < datetime.now()):
                self.default_headers.update({'Authorization':'Bearer ' + self.get_auth_value('accessToken')})
                return True
            else:
                return False
        else:
            return False

    def get_auth_value(self, val, item=0):
        if len(self.cache._cache) >= 1:
            try:
                return list(self.cache._cache.values())[item][val]
            except:
                raise AttributeError(f'{val} is not in the token cache. ' +
                                     f'Verify items: {list(list(self.cache._cache.values())[item].keys())}')
        else:
            raise AttributeError(f'Have you forgotten to acquire a token?.')

    def lazy_acquire_token_with_username_password(self, resource, username, password):
        '''Gets a token for a given resource via user credentails.
        Does not require clientId, we user another embedded clientId.
        
        :param str resource: A URI that identifies the resource for which the 
            token is valid.
        :param str username: The username of the user on behalf this
            application is authenticating.
        :param str password: The password of the user named in the username
            parameter.
        :returns: dict with several keys, include "accessToken" and
            "refreshToken".
        '''
        return super(client_context, self).acquire_token_with_username_password(resource, username, password, '51f81489-12ee-4a9e-aaae-a2591f45987d')

class AuthException(Exception):
    pass
    