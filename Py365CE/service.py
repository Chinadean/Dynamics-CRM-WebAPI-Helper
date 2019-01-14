# Py365CE Auth Class - Handles Authentication to MicrosoftOnline/AAD
# Used to call your request object

import json
import requests
import time


class service():

    """
    Use: Used as the primary method for firing org side actions.

    Attributes:
        ClientCredentials: Set by user to define the context of the
        OrganizationServiceProxy.
        AccessToken: Set when the request to the organization returns
        correctly.
        AccessTokenExpiry: Unix time value of the time the token expires.
        TokenEndpoint: Static URI string for microsoft online.
        ClientId: Static GUID for the Dynamics CRM serice Global
    """
    access_token = None
    access_token_expiry = None
    token_endpoint = "https://login.microsoftonline.com/common/oauth2/token"
    client_id = "2ad88395-b77d-4561-9441-d0e40824f9bc"
    credentials = {}

    def __init__(self, username, password, url):
        self.credentials["username"] = username
        self.credentials["password"] = password
        self.credentials["url"] = url
        self.authenticate()

    def authenticate(self):
        """Authenticates the current passed ClientCredentials with microsoftonline/AAD

        Args:
            self: Authenticates it's own context.

        Returns:
            Nothing. It's expected that the user manually checks the token
            exists.

        Raises:
            AttributeError: Please define ClientCredentials or pass
            ClientCredentials as correct type.
            BaseException: Access token is already set in this context.
        """

        webform_data = {
            'client_id': self.client_id,
            'resource': self.credentials["url"],
            'username': self.credentials["username"],
            'password': self.credentials["password"],
            'grant_type': 'password'
        }

        # Makes request and returns the json dictionary.
        response_json = self.extractsetjson(self.requesttoken(webform_data))

        self.api_url = self.credentials["url"] + '/api/data/v9.0/'

        try:
            self.access_token = response_json["access_token"]
            self.access_token_expiry = response_json["expires_on"]
        except:
            raise AttributeError("Unable to parse Json Response.")

    def extractsetjson(self, request):
        # Future Proofing
        return request.json()

    def requesttoken(self, data):
        response = requests.post(self.token_endpoint, data=data)
        if response.status_code == 200:
            return response
        else:
            raise ConnectionError(f"{str(response.status_code)+response.text}")

    def checktoken(self):
        # Internal Check for Token Existance and Expiry
        if self.access_token_expiry is None:
            return False
        elif int(self.access_token_expiry) < time.time():
            return False
        else:
            return True
