import json
import time
import requests
import re

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
    ApiUrl = None
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

        self.ApiUrl = self.ClientCredentials.CRMUrl + '/api/data/v9.0/'

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

    # do I really need this?
    def AuthenticateForce(self):
        """Authenticates the current passed ClientCredentials with microsoftonline/AAD

            Primarily used internally during operation to prevent request with expired token.

        Args:
            self: Authenticates it's own context.

        Returns:
            Nothing. Implied successful if no exception is thrown.

        Raises:
            AttributeError: Please define ClientCredentials or pass ClientCredentials as correct type.
            BaseException: Access token is already set in this context.
        """
        WebformData = {
            'client_id': self.ClientId,
            'resource': self.ClientCredentials.CRMUrl,
            'username': self.ClientCredentials.Username,
            'password': self.ClientCredentials.Password,
            'grant_type': 'password'
        }

        ResponseJson = self.ExtractSetJson(self.RequestToken(WebformData))

        try:
            self.AccessToken = ResponseJson["access_token"]
            self.AccessTokenExpiry = ResponseJson["expires_on"]
        except:
            raise AttributeError("Unable to locate access_token or expires_on in response content.")

    def Create(self, entity):
        """Takes an Entity class Type and verifies it has the required attributes
            Updates the passed entity with the Entity Type's Dictionary.

        Args:
            entity: Entity Type for which needs Attributes(for initial create) and EntityType.

        Returns:
            The HTTP Post Response requests object.
        """
        if self.CheckToken() == False:
            self.AuthenticateForce()

        self.VerifyEntity(entity, 'create')

        headers = {
            'Content-Type': 'application/json; charset=utf-8',
            'OData-MaxVersion': '4.0',
            'OData-Version': '4.0',
            'Accept': 'application/json',
            'Authorization': 'Bearer ' + self.AccessToken
        }

        # json.dumps to prevent invalid json error due to single quotes default by python (ez work around)
        return requests.post(self.ApiUrl+entity.EntityType, headers=headers, data=json.dumps(entity.Attributes))

    
    # TODO: Update record reference.   
    def Update(self, entity):
        """Takes an Entity class Type and verifies it has the required attributes
            Updates the passed entity with the Entity Type's Dictionary.

        Args:
            entity: Entity Type for which needs Attributes, EntityType, and Guid Passed. 

        Returns:
            The HTTP Patch Response requests object.
        """
        if self.CheckToken() == False:
            self.AuthenticateForce()

        self.VerifyEntity(entity, 'update')

        headers = {
            'Content-Type': 'application/json; charset=utf-8',
            'OData-MaxVersion': '4.0',
            'OData-Version': '4.0',
            'Accept': 'application/json',
            'Authorization': 'Bearer ' + self.AccessToken
        }

        return requests.patch(self.BuildTargetURL(entity.EntityType, entity.Guid), headers=headers, data=json.dumps(entity.Attributes))

    def BuildTargetURL(self, entitytype, entityid):
        return self.ApiUrl + entitytype + "(" + entityid + ")"

    # TODO: Delete target record. Hardcode references for Entity type compat and without object instatiation if guid is known.
    def Delete(self, string, guid): 
        pass

    # TODO: Execute the workflow request with input parameters.
    def Execute(self, request):
        pass

    # TODO: Retrieve from a guid with column set required. Use RetrieveAll if all columns needed.
    def Retrieve(self, string, guid, columnSet):
        pass

    # TODO: Retrieve Single record but all column set. Inefficient but needed for simple and hard-coded use cases.
    def RetrieveAll(self, entitytype, guid):
        pass

    # TODO: Retrieve muliple records based off the query base.
    def RetrieveMultiple(self, queryBase):
        # place holder
        pass

    def VerifyEntity(self, entity, requesttype):
        # Just learned no switch case in python - oh well

        # We check for generic availability in entity class, as these metadata schema names can be custom and 
        # we don't want to bind the user to arbitary guidlines and metadata fetches on OrgService to verify. Keep this 
        # simple, smart, and readable.

        if requesttype == 'create':
            if entity.EntityType == None:
                raise AttributeError('Object Type: Entity is missing an EntityType String.')
            if entity.Attributes == {}:
                raise AttributeError('Object Attributes: Entity is missing object attributes.')
        if requesttype == 'update':
            if entity.EntityType == None:
                raise AttributeError('Object Type: Entity is missing an EntityType String.')
            if entity.Guid == None:
                raise AttributeError('Object Guid: Entity must have valid object Guid to update.')
    
    # TODO: Setup metadata object to fetch if needed for more dynamic use cases.
    def BuildMetadata(self):
        raise NotImplementedError()
    
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
    Value = None
    
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

"""
 Start the static functions used as helpers
"""

def extract_guid(response):
	# Extracts first guid from a create response (typically only one anyways)
	guid = re.findall(r"[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[89ab][0-9a-f]{3}-[0-9a-f]{12}", response.headers['Location'])
	return guid[0]
 


