import Xrm as Xrm

def main():
    osp = fetch_auth()
    ety = Xrm.Entity()
    ety.EntityType = 'accounts'
    ety.Attributes['name'] = 'taco'
    osp.Create(ety)

def fetch_auth():
    cc = Xrm.ClientCredentials()
    cc.CRMUrl = "https://colton.api.crm.dynamics.com"
    cc.Password = ""
    cc.Username = "admin@coltonlathrop.net"
    osp = Xrm.OrganizationServiceProxy()
    osp.ClientCredentials = cc
    osp.Authenticate()
    return osp



if __name__ == "__main__":
    main()
