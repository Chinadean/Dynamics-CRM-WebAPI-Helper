from .auth import user_context
import requests
import json


class create_record():

    def __init__(self, entity_type, auth_context, data=None):
        self.entity_type = entity_type
        self.auth_context = auth_context
        if data is not None:
            self.data = data
    
    def execute(self, context=None, debug=False):
        if context is not None:
            self.auth_context = context
        assert self.auth_context.is_authed, 'user_context is not authorized.'
        assert self.data is not None, 'data is none, values required.'
        return requests.post(self.build_create_url, data=json.dumps(self.data), headers=self.auth_context.default_headers, verify=not debug)
    
    @property
    def build_create_url(self):
        return self.auth_context.get_auth_value('resource') + self.auth_context.api_query_stem + self.entity_type

