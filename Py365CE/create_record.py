from .auth import * 
import requests
import json


class create_record():
    
    request_type = 0

    def __init__(self, entity_type, auth_context, data=None):
        '''Takes WebAPI entity identifier and an authcontext to build create.
        
        :param str entity_type: String of the records WebAPI entity identifier.
        :param str auth_context: The user_context
        :param str password: The password of the user named in the username
            parameter.
        '''
        self.entity_type = entity_type
        self.auth_context = auth_context
        if data is not None:
            self.data = data

    @property
    def build_create_url(self):
        return self.auth_context.get_auth_value('resource') + self.auth_context.api_query_stem + self.entity_type

