import json
import time
import requests


class OrganizationServiceProxy():
    """
    Use: Used as the primary method for firing org side actions.

    Attributes:
        ClientCredentials: Set by user to define the context of the OrganizationServiceProxy.
        AccessToken: Set when the request to the organization returns correctly.
        AccessTokenExpiry: Unix time value of the time the token expires.
        TokenEndpoint: Static URI string for microsoft online.
        ClientId: Static GUID for the Dynamics CRM serice Global
    """
    ClientCredentials = None
    AccessToken = None
    AccessTokenExpiry = None
    TokenEndpoint = "https://login.microsoftonline.com/common/oauth2/token"
    ClientId = "2ad88395-b77d-4561-9441-d0e40824f9bc" 

    def Authenticate(self):
        """Authenticates the current passed ClientCredentials with microsoftonline/AAD

        Args:
            self: Authenticates it's own context.

        Returns:
            Nothing. It's expected that the user manually checks the token exists.

        Raises:
            AttributeError: Please define ClientCredentials or pass ClientCredentials as correct type.
            BaseException: Access token is already set in this context.
        """
        if self.ClientCredentials == None or type(self.ClientCredentials) is not ClientCredentials:
            raise AttributeError("Please define ClientCredentials or pass ClientCredentials as correct type.")
        if self.AccessTokenExpiry != None:
            raise BaseException("Access Token is already set in this context. Please check AccessTokenExpiry and call AuthenticateForce to force the reauth flow.")

        WebformData = {
            'client_id': self.ClientId,
            'resource': self.ClientCredentials.CRMUrl,
            'username': self.ClientCredentials.Username,
            'password': self.ClientCredentials.Password,
            'grant_type': 'password'
        }
        # Makes request and returns the json dictionary.
        ResponseJson = self.ExtractSetJson(self.RequestToken(WebformData))

        # Start trying to set the OrganizationServiceProxy Authentication context.
        try:
            self.AccessToken = ResponseJson["access_token"]
            self.AccessTokenExpiry = ResponseJson["expires_on"]
        except:
            raise AttributeError("Unable to locate access_token or expires_on in response content.")

    def ExtractSetJson(self, request):
        # Future Proofing
        return request.json()

    def RequestToken(self, data):
        response = requests.post(self.TokenEndpoint, data=data)
        if response.status_code == 200:
            return response
        else:
            raise ConnectionError("Authentication has failed with response code: {0}".format([str(response.status_code)])+response.text)

    def CheckToken(self):
        """ Checks it's own token expiry to verify it's not expired, True = Good Token : False = Bad Token """
        if self.AccessTokenExpiry == None:
            return False
        elif int(self.AccessTokenExpiry) < time.time():
            return False
        else: 
            return True

    def InternalGetHeaders(self, requesttype):
        pass

    def Create(self, entity):
        pass

    def Delete(self, string, guid):
        pass

    def Execute(self, request):
        pass

    def Retrieve(self, string, guid, columnSet):
        pass

    def RetrieveMultiple(self, queryBase):
        pass

    def Update(self, entity):
        pass

    pass

class ClientCredentials():
    """
    Use: Used to contain the client credentials used by the user for connection. 
    """
    Username = None
    Password = None
    CRMUrl = None

class Entity():
    """
    Use: Used to represent an entity within CRM - Either Referenced or Non-Referenced.
    """
    Guid = None
    Attributes = {}
    EntityType = None

    def AddAttribute(self, attribute):
        self.Attributes[attribute[0]] = attribute[1]

    def GetAttributes(self):
        return self.Attributes

    def SetAttributes(self, attributes):
        self.Attributes = attributes

    def SetGuid(self, guid):
        self.Guid = guid


class EntityCollection():
    """
    Use: Used a container of Entity type.
    """
    Entities = []

class Request():
    pass

class ExecuteMultiple(Request):
    pass

class Delete(Request):
    pass

class Create(Request):
    pass



class OptionSetValue():
    """
    Use: Used to set a value of an option set used in a query.
    """
    pass

class ColumnSet():
    """
    Use: Used to define a columnset used for 
    """
    pass

class ConditionExpression():
    """
    Use: Used to define conditions for retrievemultple query expressions.
    """
    pass

class FilterExpression():
    """
    Use: Used to define the filter in a QueryBase.
    """
    pass

class QueryExpression():
    """
    Use: Used to define the query used in a retrievemultiple request.
    """
    pass




