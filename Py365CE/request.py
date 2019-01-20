from .auth import user_context
import requests
import json

class request():
        
    default_headers = {'Content-Type': 'application/json; charset=utf-8',
                            'OData-MaxVersion': '4.0',
                            'OData-Version': '4.0',
                            'Accept': 'application/json'}

    def verify_user_context(self):
        pass
