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
    
    @property
    def build_delete_url(self):
        return self.auth_context.get_auth_value('resource') + self.auth_context.api_query_stem + self.entity_type + f'({self.guid})'

