import Xrm as Xrm
from uuid import UUID


def main():
    osp = fetch_auth()
    x = osp.DeleteField('accounts', '76412F49-A703-E911-A952-000D3A4E820A', 'description')
    print(x.status_code)
    print(x.text)





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
