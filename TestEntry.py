import Xrm as Xrm
from uuid import UUID


def main():
    osp = fetch_auth()
    x = osp.Delete('accounts', 'ADDC96D6-B5F4-E811-A94D-000D3A1F667C')
    print(x.status_code)
    





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
