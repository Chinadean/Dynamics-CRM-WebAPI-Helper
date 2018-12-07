import Xrm as Xrm
from uuid import UUID


def main():
    osp = fetch_auth()
    for i in range(1000):
        x = osp.RetrieveAll('accounts', '0FB5275C-B2F4-E811-A94E-000D3A4E8995')
        print(str(x.status_code) + ' : ' + str(i))


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
