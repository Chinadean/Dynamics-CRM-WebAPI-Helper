from .auth import * 
import requests
import json


class retrieve_record():
    
    request_type = 2

    def __init__(self, entity_type, guid, auth_context, columns=None):
        '''Takes WebAPI entity identifier and an authcontext to build create.
        
        :param str entity_type: String of the records WebAPI entity identifier.
        :param str auth_context: The user_context
        :param str password: The password of the user named in the username
            parameter.
        :param list columns: Columns to fetch, leave null if fetching all.
        '''
        self.entity_type = entity_type
        self.auth_context = auth_context
        if columns is not None:
            self.columns = columns
        else:
            self.columns = None
        if guid is not None:
            self.guid = guid
        else:
            raise Exception('Must pass guid into class instantiation')
        

    @property
    def build_retrieve_url(self):
        return self.auth_context.get_auth_value('resource') + self.auth_context.api_query_stem + f'{self.entity_type}({self.guid}){self.build_columns()}'

    def build_columns(self):
        ret_str = '?$select='
        if self.columns == None:
            return ''
        else:
            for i in self.columns:
                ret_str += f'{i},'
            return ret_str

