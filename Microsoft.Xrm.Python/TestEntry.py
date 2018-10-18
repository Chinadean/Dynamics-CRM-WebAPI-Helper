from Xrm import Xrm


x = Xrm.ClientCredentials()
x.CRMUrl = "test.com"
x.Password = "password123"
x.Username = "admin@coltonlathrop.net"

xx = Xrm.OrganizationServiceProxy()
xx.ClientCredentials = x
xx.Authenticate()

