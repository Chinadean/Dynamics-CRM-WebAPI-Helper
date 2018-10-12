import requests
import json

class OrganizationServiceProxy():
    """
    Use: Used as the primary method for firing org side actions.
    """

    def Authenticate():
        pass

    def Create(entity):
        pass

    def Delete(string, guid):
        pass

    def Execute(request):
        pass

    def Retrieve(string, guid, columnSet):
        pass

    def RetrieveMultiple(queryBase):
        pass

    def Update(entity):
        pass

    pass

class ClientCredentials():
    """
    Use: Used to contain the client credentials used by the user for connection. 
    """
    pass

class ConnectionString():
    """
    Use: Used as a substitute to specify certain connection parameters used.
    """
    pass

class SecurityTokenResponse():
    """
    Use: Used for the user to retreive the Oauth2 Security Token currently in user by OrganizationServiceProxy.
    """
    pass

class ServiceUrls():    
    """
    Use: Used by OrganizationServiceProxy to return the ServiceUrls in relation to the connected instance.
    """
    pass

class Entity():
    """
    Use: Used to represent an entity within CRM - Either Referenced or Non-Referenced.
    """
    pass

class EntityCollection():
    """
    Use: Used a container of Entity types.
    """
    pass

class OptonSetValue():
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




