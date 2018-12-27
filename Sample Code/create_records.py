from .. import Xrm
from uuid import UUID


def main():
    connection = fetch_auth()
    entity = entity()
    entity.EntityType = 'account'
    entity.Attributes = {'name':'This is a test record', 'description':'This is another attribute in our test record.'}
    response = connection.Create(entity)
    print(response.status_code)
    





def fetch_auth():
    cc = Xrm.ClientCredentials()
    cc.CRMUrl = "https://coltonlathrop.api.crm.dynamics.com"
    cc.Password = "Fargoctslabs!"
    cc.Username = "admin@coltonlathrop.net"
    osp = Xrm.OrganizationServiceProxy()
    osp.ClientCredentials = cc
    osp.Authenticate()
    return osp



if __name__ == "__main__":
    main()
