from .auth import * 
import requests
import json


class update_record():
    
    request_type = 1

    def __init__(self, entity_type, auth_context, guid = None, data=None):
        '''Takes Updates Target record with passed in data.
        
        :param str entity_type: String of the records WebAPI entity identifier.
        :param str auth_context: The user_context
        :param str password: The password of the user named in the username
            parameter.
        '''
        self.entity_type = entity_type
        self.auth_context = auth_context
        if data is not None:
            self.data = data
        if guid is not None:
            self.guid = guid
        else:
            raise Exception('Must pass guid into class instantiation')

    @property
    def build_update_url(self):
        return self.auth_context.get_auth_value('resource') + self.auth_context.api_query_stem + f'{self.entity_type}({self.guid})'
