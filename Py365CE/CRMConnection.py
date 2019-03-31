from adal import *
from datetime import datetime
import requests
import json


class CRMConnection(AuthenticationContext):
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
        self._session = requests.session()
        self._debug = Debug
        self._affinity_reset = AffinityReset
        for i in self.default_headers:
            self._session.headers.update({i:self.default_headers[i]})
        super(CRMConnection, self).__init__(tenant)        
        
    def Get(self, url, data=None):
        return self._session.get(url, data=json.dumps(data))
    
    def Post(self, url, data):
        return self._session.post(url, data=json.dumps(data))

    def Patch(self, url, data):
        return self._session.patch(url, data=json.dumps(data))
    
    def Delete(self, url, data=None):
        return self._session.delete(url)
   
    def dump_affinity_token(self):
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
        return super(CRMConnection, self).acquire_token_with_username_password(resource, username, password, '51f81489-12ee-4a9e-aaae-a2591f45987d')

    