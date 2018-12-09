import Xrm as Xrm
from uuid import UUID


def main():
    #osp = fetch_auth()
    x = Xrm.SelectColumns()
    x.append('a')
    print(x[0])
    x[0] = 'dd'
    x.pop(0)





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
