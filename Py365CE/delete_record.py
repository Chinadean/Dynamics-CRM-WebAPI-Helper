from .auth import * 
import requests
import json


class delete_record():
    
    request_type = 3

    def __init__(self, entity_type, auth_context, guid=None):
        '''Takes WebAPI entity identifier and an authcontext to build create.
        
        :param str entity_type: String of the records WebAPI entity identifier.
        :param str auth_context: The user_context
        :param str password: The password of the user named in the username
            parameter.
        '''
        self.entity_type = entity_type
        self.auth_context = auth_context
        if guid is not None:
            self.guid = guid
    
    def execute(self, context=None, debug=False):
        '''Executes the delete_record.
        
        :param user_context context: (optional) Pass is new user_context if needed here.
        :param bool debug: (optional) Sets the option to verify certificate.
        :returns: Requests response object.
        '''
        if context is not None:
            self.auth_context = context
        if not self.auth_context.is_authed:
            raise AuthException('User_Context is not authed.')
        if self.guid is None:
            raise AttributeError('Guid is required to delete.')
        return requests.post(self.build_delete_url, headers=self.auth_context.default_headers, verify=not debug)
    
    @property
    def build_delete_url(self):
        return self.auth_context.get_auth_value('resource') + self.auth_context.api_query_stem + self.entity_type + f'({self.guid})'

