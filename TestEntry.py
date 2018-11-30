import Xrm as Xrm
import re

def main():
    osp = fetch_auth()
    ety = Xrm.Entity()
    ety.EntityType = 'accounts'
    ety.Attributes['name'] = 'taco'
    x = osp.Create(ety)
    print(x.status_code)
    print(x.cookies.get_dict())
    print(x.headers['Location'])
    guid = Xrm.extract_guid(x) 
    print(guid)
    ety.Guid = guid
    ety.Attributes['name'] = 'taco2'
    xx = osp.Update(ety)
    print(xx.status_code)

def fetch_auth():
    cc = Xrm.ClientCredentials()
    cc.CRMUrl = "https://coltonlathrop.api.crm.dynamics.com"
    cc.Password = ""
    cc.Username = "admin@coltonlathrop.net"
    osp = Xrm.OrganizationServiceProxy()
    osp.ClientCredentials = cc
    osp.Authenticate()
    return osp



if __name__ == "__main__":
    main()
